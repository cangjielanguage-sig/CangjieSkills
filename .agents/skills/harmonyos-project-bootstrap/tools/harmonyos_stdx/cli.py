"""Install and configure HarmonyOS stdx for emulator and device ABIs."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

from .archive import download, extract_archive, installation_complete, locate_binary_root, validate_zip
from .errors import SetupError
from .manifest import configure_manifest, resolve_project
from .models import PlatformPlan, Toolchain
from .policy import (
    OHOS_PLATFORMS,
    asset_name,
    asset_url,
    release_by_version,
    release_page,
    target_for_platform,
)
from .system import (
    FileLock,
    cjc_path,
    default_install_root,
    discover_cangjie_sdk,
    inspect_toolchain,
    lock_name,
    sha256_file,
)


SKILLS_ROOT = Path(__file__).resolve().parents[3]


def _configure_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def _config_helpers():
    helper_dir = SKILLS_ROOT / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.is_dir() and str(helper_dir) not in sys.path:
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import first_value, load_harmony_config
    except ImportError as exc:
        raise SetupError(f"shared cangjie.skills.toml loader is unavailable: {helper_dir}") from exc
    return first_value, load_harmony_config


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install and configure stdx for HarmonyOS x64 emulator and ARM64 device targets."
    )
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="HarmonyOS module directory or cjpm.toml")
    parser.add_argument(
        "--config",
        action="append",
        default=None,
        help="Path to cangjie.skills.toml; repeat to layer files",
    )
    parser.add_argument("--cangjie-sdk", type=Path, help="HarmonyOS Cangjie SDK root containing build-tools/bin/cjc")
    parser.add_argument("--stdx-version", help="verified compatibility override, for example 1.1.0.1")
    parser.add_argument(
        "--platform",
        action="append",
        choices=OHOS_PLATFORMS,
        help="install one HarmonyOS ABI; repeat for both (default: ohos-x64 and ohos-aarch64)",
    )
    parser.add_argument("--destination", type=Path, help="global installation root (default: ~/.cangjie/stdx)")
    parser.add_argument("--cache-dir", type=Path, help="download cache (default: <destination>/.cache)")
    parser.add_argument("--archive-dir", type=Path, help="directory containing official ZIPs for every selected ABI")
    parser.add_argument("--linkage", choices=("dynamic", "static"), default="dynamic")
    parser.add_argument("--offline", action="store_true", help="forbid downloads; require --archive-dir or cached ZIPs")
    parser.add_argument("--no-configure", action="store_true", help="install only; do not edit cjpm.toml")
    parser.add_argument("--force", action="store_true", help="redownload and re-extract selected releases")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the plan without downloading, extracting, or editing",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    return parser.parse_args(argv)


def _resolve_sdk(args: argparse.Namespace) -> Path:
    first_value, load_harmony_config = _config_helpers()
    cfg = load_harmony_config(project_root=args.project, config_paths=args.config)
    configured = getattr(getattr(cfg, "toolchain", None), "cangjie_sdk", None)
    selected = first_value(args.cangjie_sdk, os.getenv("CANGJIE_SDK_HOME"), configured)
    return Path(selected).expanduser().resolve() if selected else discover_cangjie_sdk()


def _resolve_plans(
    args: argparse.Namespace,
    toolchain: Toolchain,
) -> tuple[Path | None, Toolchain, list[PlatformPlan]]:
    _project_root, manifest = resolve_project(args.project, args.no_configure)
    active = Toolchain(toolchain.version, release_by_version(args.stdx_version)) if args.stdx_version else toolchain
    platforms = tuple(dict.fromkeys(args.platform or OHOS_PLATFORMS))
    destination = (args.destination or default_install_root()).expanduser().resolve()
    cache_dir = (args.cache_dir or destination / ".cache").expanduser().resolve()
    plans: list[PlatformPlan] = []
    for platform in platforms:
        filename = asset_name(active.release, platform)
        plans.append(
            PlatformPlan(
                platform=platform,
                target=target_for_platform(platform),
                linkage=args.linkage,
                release_page=release_page(active.release),
                asset_url=asset_url(active.release, platform),
                destination=destination,
                cache_dir=cache_dir,
                installation=destination / filename.removesuffix(".zip"),
            )
        )
    return manifest, active, plans


def _write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    encoded = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if path.is_file() and path.read_bytes() == encoded:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _local_archives(args: argparse.Namespace, plans: list[PlatformPlan], version: str) -> dict[str, Path]:
    if not args.archive_dir:
        return {}
    directory = args.archive_dir.expanduser().resolve()
    archives: dict[str, Path] = {}
    for plan in plans:
        archive = directory / f"cangjie-stdx-{plan.platform}-{version}.zip"
        validate_zip(archive)
        archives[plan.platform] = archive
    return archives


def _install_platform(
    args: argparse.Namespace,
    plan: PlatformPlan,
    version: str,
    local_archive: Path | None,
) -> dict[str, Any]:
    plan.destination.mkdir(parents=True, exist_ok=True)
    filename = f"cangjie-stdx-{plan.platform}-{version}.zip"
    lock_path = plan.destination / ".locks" / lock_name(str(plan.installation))
    with FileLock(lock_path):
        if local_archive:
            archive = local_archive
        else:
            archive = plan.cache_dir / filename
            cache_lock = plan.cache_dir / ".locks" / lock_name(str(archive.resolve()))
            with FileLock(cache_lock):
                archive = download(plan.asset_url, archive, args.force, args.offline)
        reused = plan.installation.is_dir() and installation_complete(plan.installation) and not args.force
        installation = extract_archive(archive, plan.destination, plan.installation, args.force)
        binary_root = locate_binary_root(installation, plan.linkage)
        archive_sha256 = sha256_file(archive)
        record = plan.installation / "install.json"
        if not reused or not record.is_file():
            installed_archive_sha256 = archive_sha256
            _write_json_atomic(
                record,
                {
                    "schema": 1,
                    "stdx_version": version,
                    "platform": plan.platform,
                    "target": plan.target,
                    "release_page": plan.release_page,
                    "asset_url": plan.asset_url,
                    "installation": str(plan.installation),
                    "archive_sha256": installed_archive_sha256,
                },
            )
        else:
            try:
                installed_archive_sha256 = json.loads(record.read_text(encoding="utf-8"))["archive_sha256"]
            except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
                raise SetupError(f"invalid installation record; rerun with --force: {record}: {exc}") from exc
    result = plan.as_dict()
    result.update(
        archive=str(archive),
        archive_sha256=archive_sha256,
        installed_archive_sha256=installed_archive_sha256,
        installation_reused=reused,
        binary_root=str(binary_root),
        install_record=str(record),
    )
    return result


def run(args: argparse.Namespace, toolchain: Toolchain) -> dict[str, Any]:
    manifest, active, plans = _resolve_plans(args, toolchain)
    result: dict[str, Any] = {
        "schema": 1,
        "cjc_version": active.version,
        "stdx_version": active.release.version,
        "manifest": str(manifest) if manifest else None,
        "dry_run": args.dry_run,
        "platforms": [plan.as_dict() for plan in plans],
    }
    if args.dry_run:
        return result

    archives = _local_archives(args, plans, active.release.version)
    installed = [
        _install_platform(args, plan, active.release.version, archives.get(plan.platform))
        for plan in plans
    ]
    configured = False
    if not args.no_configure:
        assert manifest is not None
        binary_roots = {item["target"]: Path(item["binary_root"]) for item in installed}
        manifest_lock = (args.destination or default_install_root()).expanduser().resolve() / ".locks" / lock_name(
            str(manifest.resolve())
        )
        with FileLock(manifest_lock):
            configured = configure_manifest(manifest, binary_roots)
    result["platforms"] = installed
    result["configured"] = configured
    return result


def _emit(result: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"Cangjie {result['cjc_version']} -> stdx {result['stdx_version']}")
    for item in result["platforms"]:
        location = item.get("binary_root") or item["installation"]
        print(f"{item['platform']} ({item['target']}): {location}")
    if result.get("manifest") and not result.get("dry_run"):
        state = "updated" if result.get("configured") else "already configured"
        print(f"cjpm.toml: {state} ({result['manifest']})")


def main(argv: list[str] | None = None) -> int:
    _configure_streams()
    args = parse_args(argv)
    try:
        sdk = _resolve_sdk(args)
        toolchain = inspect_toolchain(cjc_path(sdk))
        result = run(args, toolchain)
        _emit(result, args.json)
        if args.linkage == "static" and not args.dry_run:
            print("warning: static stdx may require additional HarmonyOS system link options", file=sys.stderr)
        return 0
    except (OSError, SetupError, ValueError) as exc:
        print(f"setup_harmonyos_stdx: {exc}", file=sys.stderr)
        return 1
