#!/usr/bin/env python3
"""Bounded, read-only discovery for Cangjie HarmonyOS development."""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any, Callable

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from config_loader import detect_project_runtime, find_project_root, first_value, load_harmony_config


SCHEMA_VERSION = 1
ERROR_MARKERS = (
    "[fail]",
    "failed",
    "error:",
    "not found",
    "no device",
    "connect failed",
)


def _config_source(loaded_files: list[Path], dotted_key: str) -> str | None:
    keys = dotted_key.split(".")
    for path in reversed(loaded_files):
        try:
            value: Any = tomllib.loads(path.read_text(encoding="utf-8-sig"))
            for key in keys:
                if not isinstance(value, dict) or key not in value:
                    raise KeyError(key)
                value = value[key]
            return f"config:{path}"
        except (OSError, tomllib.TOMLDecodeError, KeyError):
            continue
    return None


def _resolved(value: str | Path | None, source: str, *, exists: bool | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"value": str(value) if value is not None else None, "source": source}
    if exists is not None:
        item["exists"] = exists
    return item


def _platform_deveco_default() -> Path:
    system = platform.system()
    if system == "Windows":
        return Path("C:/Program Files/Huawei/DevEco Studio")
    if system == "Darwin":
        return Path("/Applications/DevEco-Studio.app/Contents")
    return Path("/opt/DevEco-Studio")


def _version_key(path: Path) -> tuple[int, ...]:
    parts = re.findall(r"\d+", path.parent.name)
    return tuple(int(part) for part in parts) if parts else (0,)


def _discover_cangjie_sdk() -> Path:
    root = Path.home() / ".cangjie-sdk"
    candidates = [
        path / "cangjie"
        for path in root.iterdir()
        if path.is_dir() and (path / "cangjie" / "build-tools" / "bin").is_dir()
    ] if root.is_dir() else []
    return max(candidates, key=_version_key) if candidates else root / "6.1" / "cangjie"


def _exe(name: str) -> str:
    return f"{name}.exe" if platform.system() == "Windows" else name


def _read_deveco_version(home: Path) -> str | None:
    path = home / "product-info.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        version = data.get("version") if isinstance(data, dict) else None
        return str(version) if version else None
    except (OSError, json.JSONDecodeError):
        return None


def _safe_run(command: list[str], timeout: float = 5.0) -> tuple[int | None, str]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
            check=False,
        )
        output = "\n".join(part.strip() for part in (result.stdout, result.stderr) if part.strip())
        return result.returncode, output[:4000]
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)[:1000]


def _first_line(text: str) -> str | None:
    return next((line.strip() for line in text.splitlines() if line.strip()), None)


def _device_report(
    hdc: Path | None,
    target: str,
    source: str,
    runner: Callable[[list[str], float], tuple[int | None, str]],
    enabled: bool,
) -> dict[str, Any]:
    report: dict[str, Any] = {"target": target, "source": source, "status": "not_checked", "targets": []}
    if not enabled:
        return report
    if hdc is None or not hdc.is_file():
        report["status"] = "hdc_missing"
        return report
    code, output = runner([str(hdc), "list", "targets"], 5.0)
    lines = [line.strip() for line in output.splitlines() if line.strip() and line.strip().lower() != "empty"]
    lower = output.lower()
    has_error = code != 0 or any(marker in lower for marker in ERROR_MARKERS)
    targets = [line.split()[0] for line in lines if not any(marker in line.lower() for marker in ERROR_MARKERS)]
    report["targets"] = list(dict.fromkeys(targets))
    report["status"] = "error" if has_error else ("connected" if target in targets else "not_connected")
    if has_error:
        report["detail"] = _first_line(output)
    return report


def collect_report(
    args: argparse.Namespace,
    *,
    environ: dict[str, str] | None = None,
    runner: Callable[[list[str], float], tuple[int | None, str]] = _safe_run,
) -> dict[str, Any]:
    env = environ if environ is not None else os.environ
    project = find_project_root(args.project_root)
    cfg = load_harmony_config(project_root=project, config_paths=args.config)
    toolchain = cfg.toolchain
    runtime_cfg = cfg.runtime
    detected = detect_project_runtime(project, module=first_value(args.module, runtime_cfg.module))

    deveco_value = first_value(args.deveco_home, env.get("DEVECO_HOME"), toolchain.deveco_home)
    if args.deveco_home:
        deveco_source = "cli:--deveco-home"
    elif env.get("DEVECO_HOME"):
        deveco_source = "environment:DEVECO_HOME"
    elif toolchain.deveco_home:
        deveco_source = _config_source(cfg.loaded_files, "toolchain.deveco_home") or "configuration"
    else:
        deveco_source = "automatic:platform-default"
    deveco = Path(deveco_value).expanduser().resolve() if deveco_value else _platform_deveco_default()

    cangjie_value = first_value(args.cangjie_sdk, env.get("CANGJIE_SDK_HOME"), toolchain.cangjie_sdk)
    if args.cangjie_sdk:
        cangjie_source = "cli:--cangjie-sdk"
    elif env.get("CANGJIE_SDK_HOME"):
        cangjie_source = "environment:CANGJIE_SDK_HOME"
    elif toolchain.cangjie_sdk:
        cangjie_source = _config_source(cfg.loaded_files, "toolchain.cangjie_sdk") or "configuration"
    else:
        cangjie_source = "automatic:newest-~/.cangjie-sdk"
    cangjie = Path(cangjie_value).expanduser().resolve() if cangjie_value else _discover_cangjie_sdk()

    hdc_value = first_value(args.hdc, toolchain.hdc)
    if args.hdc:
        hdc_source = "cli:--hdc"
    elif toolchain.hdc:
        hdc_source = _config_source(cfg.loaded_files, "toolchain.hdc") or "configuration"
    else:
        on_path = shutil.which("hdc")
        fallback = deveco / "sdk/default/openharmony/toolchains" / _exe("hdc")
        hdc_value = on_path or (str(fallback) if fallback.exists() else None)
        hdc_source = "automatic:PATH" if on_path else "automatic:DevEco-toolchains"
    hdc = Path(hdc_value).expanduser().resolve() if hdc_value else None

    cjc = cangjie / "build-tools/bin" / _exe("cjc")
    cjpm = cangjie / "build-tools/tools/bin" / _exe("cjpm")
    hdc_version = None
    if hdc and hdc.is_file():
        _, output = runner([str(hdc), "-v"], 5.0)
        hdc_version = _first_line(output)
    cangjie_version = None
    if cjc.is_file():
        _, output = runner([str(cjc), "--version"], 5.0)
        cangjie_version = _first_line(output)

    def runtime_value(name: str, cli_value: str | None, configured: str | None, automatic: str | None) -> dict[str, Any]:
        value = first_value(cli_value, configured, automatic)
        if cli_value:
            source = f"cli:--{name.replace('_', '-')}"
        elif configured:
            source = _config_source(cfg.loaded_files, f"runtime.{name}") or "configuration"
        else:
            source = "automatic:project"
        return _resolved(value, source)

    module = runtime_value("module", args.module, runtime_cfg.module, detected.module)
    bundle = runtime_value("bundle", args.bundle, runtime_cfg.bundle, detected.bundle)
    ability = runtime_value("ability", args.ability, runtime_cfg.ability, detected.ability)
    hap = runtime_value("hap", args.hap, runtime_cfg.hap, detected.hap)
    if hap["value"]:
        hap_path = Path(hap["value"])
        if not hap_path.is_absolute():
            hap_path = project / hap_path
        hap["path"] = str(hap_path.resolve())
        hap["exists"] = hap_path.is_file()
    else:
        hap["path"] = None
        hap["exists"] = False

    target = first_value(args.target, cfg.device.target)
    target_source = (
        "cli:--target"
        if args.target
        else (_config_source(cfg.loaded_files, "device.target") or "built-in-default")
    )
    device = _device_report(hdc, target, target_source, runner, not args.no_device_check)

    build_ready = (
        deveco.is_dir()
        and cjc.is_file()
        and cjpm.is_file()
        and bool(module["value"])
    )
    runtime_ready = (
        build_ready
        and hdc is not None
        and hdc.is_file()
        and all(item["value"] for item in (bundle, ability))
        and bool(hap["exists"])
        and device["status"] == "connected"
    )
    warnings = list(detected.warnings)
    if not (project / "build-profile.json5").is_file():
        warnings.append("project build-profile.json5 was not found")

    return {
        "schema_version": SCHEMA_VERSION,
        "ok": bool(build_ready),
        "ready": {"build": bool(build_ready), "runtime": bool(runtime_ready)},
        "project": {"root": str(project), "exists": project.is_dir()},
        "configuration": {
            "mode": "explicit" if args.config is not None else "automatic",
            "loaded_files": [str(path) for path in cfg.loaded_files],
            "final_file": str(cfg.loaded_files[-1]) if cfg.loaded_files else None,
        },
        "toolchain": {
            "deveco": {**_resolved(deveco, deveco_source, exists=deveco.is_dir()), "version": _read_deveco_version(deveco)},
            "cangjie": {
                **_resolved(cangjie, cangjie_source, exists=cangjie.is_dir()),
                "version": cangjie_version,
                "cjc": str(cjc),
                "cjpm": str(cjpm),
                "executables_ready": cjc.is_file() and cjpm.is_file(),
            },
            "hdc": {
                **_resolved(hdc, hdc_source, exists=bool(hdc and hdc.is_file())),
                "version": hdc_version,
            },
        },
        "runtime": {"module": module, "bundle": bundle, "ability": ability, "hap": hap},
        "device": device,
        "warnings": warnings,
        "inspection": {
            "bounded": True,
            "stop": (
                "Use this report as the authoritative discovery result. Do not enumerate templates, packaged "
                "knowledge bodies, indexes, .agents, oh_modules, or build trees unless a reported field is missing "
                "or a later build/runtime command fails."
            ),
        },
    }


def _human(report: dict[str, Any]) -> str:
    runtime = report["runtime"]
    toolchain = report["toolchain"]
    lines = [
        "# Cangjie HarmonyOS Doctor",
        f"project: {report['project']['root']}",
        f"config files: {', '.join(report['configuration']['loaded_files']) or '(none)'}",
        f"DevEco: {toolchain['deveco']['value']} [{toolchain['deveco']['source']}]",
        f"Cangjie: {toolchain['cangjie']['value']} [{toolchain['cangjie']['source']}]",
        f"hdc: {toolchain['hdc']['value']} [{toolchain['hdc']['source']}]",
        f"module: {runtime['module']['value']} [{runtime['module']['source']}]",
        f"bundle: {runtime['bundle']['value']} [{runtime['bundle']['source']}]",
        f"ability: {runtime['ability']['value']} [{runtime['ability']['source']}]",
        f"HAP: {runtime['hap']['path']} (exists={runtime['hap']['exists']})",
        f"device: {report['device']['target']} ({report['device']['status']})",
        f"ready: build={report['ready']['build']}, runtime={report['ready']['runtime']}",
        f"STOP: {report['inspection']['stop']}",
    ]
    for warning in report["warnings"]:
        lines.append(f"WARN: {warning}")
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--config", action="append", default=None)
    parser.add_argument("--deveco-home")
    parser.add_argument("--cangjie-sdk")
    parser.add_argument("--hdc")
    parser.add_argument("--target")
    parser.add_argument("--module")
    parser.add_argument("--bundle")
    parser.add_argument("--ability")
    parser.add_argument("--hap")
    parser.add_argument("--no-device-check", action="store_true", help="report device status as not_checked")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON only")
    parser.add_argument("--strict", action="store_true", help="exit non-zero unless build and runtime are ready")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = collect_report(args)
    except Exception as exc:  # noqa: BLE001 - diagnostic boundary
        if args.json:
            print(json.dumps({"schema_version": SCHEMA_VERSION, "ok": False, "error": str(exc)}, ensure_ascii=False))
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else _human(report))
    if args.strict and not (report["ready"]["build"] and report["ready"]["runtime"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
