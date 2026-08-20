#!/usr/bin/env python3
"""Build wrapper with safe recovery for common Cangjie/HarmonyOS cache failures."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


KNOWN_CACHE_FAILURES = (
    "DataModelException: This data is not DataModelString",
    "DepModel::loadDepIncrementalCache",
)


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def remove_inside_project(project: Path, target: Path) -> None:
    resolved = target.resolve()
    if not is_relative_to(resolved, project):
        raise RuntimeError(f"Refusing to remove path outside project: {resolved}")
    if not resolved.exists():
        return
    if resolved.is_dir():
        shutil.rmtree(resolved)
    else:
        resolved.unlink()
    print(f"removed: {resolved}")


def cache_paths(project: Path) -> list[Path]:
    paths = [
        project / ".hvigor" / "cache",
        project / ".hvigor" / "dependencyMap",
    ]
    modules = sorted({cjpm.parent for cjpm in project.glob("*/cjpm.toml")})
    if not modules:
        modules = [project / "entry"]
    for module in modules:
        intermediates = module / "build" / "default" / "intermediates"
        paths.extend(intermediates / name for name in ("cj", "loader", "source_map"))
    return paths


def run_build(project: Path, build_script: Path, extra_args: list[str]) -> int:
    cmd = [sys.executable, "-B", str(build_script), "--project-root", str(project)]
    cmd.extend(extra_args)
    print(">>> " + " ".join(cmd))
    return subprocess.call(cmd)


def read_build_log(project: Path) -> str:
    log = project / "build.log"
    if not log.exists():
        return ""
    return log.read_text(encoding="utf-8", errors="replace")


def has_known_cache_failure(log: str) -> bool:
    return any(marker in log for marker in KNOWN_CACHE_FAILURES)


def print_analysis(project: Path) -> None:
    analyzer = Path(__file__).resolve().parent / "build_analyzer.py"
    if not analyzer.exists():
        return
    print("build log analysis:")
    subprocess.call([sys.executable, "-B", str(analyzer), "--project-root", str(project)])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root",
        default=".",
        help="HarmonyOS project root. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--build-script",
        default=None,
        help="Path to the existing build.py, relative to workspace or absolute.",
    )
    parser.add_argument(
        "--workspace-root",
        default=None,
        help="Workspace root used to resolve relative build-script paths. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--retry",
        action="store_true",
        help="Retry automatically after cleaning known project-local caches.",
    )
    parser.add_argument(
        "--clean-only",
        action="store_true",
        help="Only clean project-local caches; do not run a build.",
    )
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml.")
    parser.add_argument("--module", default=None, help="HarmonyOS module override passed to build.py.")
    parser.add_argument("--deveco-home", default=None, help="DevEco Studio install root passed to build.py.")
    parser.add_argument("--cangjie-sdk", default=None, help="Cangjie SDK root passed to build.py.")
    parser.add_argument("--ohpm-registry", default=None, help="ohpm registry URL passed to build.py.")
    tls = parser.add_mutually_exclusive_group()
    tls.add_argument("--verify-tls", dest="verify_tls", action="store_true", default=None)
    tls.add_argument("--no-verify-tls", dest="verify_tls", action="store_false", default=None)
    args = parser.parse_args()

    default_workspace = Path.cwd()
    workspace = Path(args.workspace_root).expanduser().resolve() if args.workspace_root else default_workspace
    project = Path(args.project_root).expanduser().resolve()
    if args.build_script:
        build_script = Path(args.build_script)
        if not build_script.is_absolute():
            build_script = (workspace / build_script).resolve()
    else:
        local_build_script = Path(__file__).resolve().parent / "build.py"
        if local_build_script.exists():
            build_script = local_build_script
        else:
            build_script = (workspace / "skills" / "harmonyos-build" / "build.py").resolve()

    if not project.exists():
        raise SystemExit(f"project root not found: {project}")
    if not build_script.exists():
        raise SystemExit(f"build script not found: {build_script}")

    if args.clean_only:
        for path in cache_paths(project):
            remove_inside_project(project, path)
        return 0

    extra: list[str] = []
    for config_path in args.config or []:
        extra.extend(["--config", config_path])
    for flag in ("module", "deveco_home", "cangjie_sdk", "ohpm_registry"):
        value = getattr(args, flag)
        if value:
            extra.extend(["--" + flag.replace("_", "-"), value])
    if args.verify_tls is True:
        extra.append("--verify-tls")
    elif args.verify_tls is False:
        extra.append("--no-verify-tls")

    first = run_build(project, build_script, extra)
    if first == 0:
        return first
    print_analysis(project)
    if not args.retry:
        return first

    log = read_build_log(project)
    if not has_known_cache_failure(log):
        print("build failed, but no known cache failure marker was found; not cleaning automatically")
        return first

    print("known cjpm incremental cache failure detected; cleaning project-local caches")
    for path in cache_paths(project):
        remove_inside_project(project, path)

    return run_build(project, build_script, extra)


if __name__ == "__main__":
    raise SystemExit(main())
