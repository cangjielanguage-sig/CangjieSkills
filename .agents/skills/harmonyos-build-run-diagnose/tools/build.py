#!/usr/bin/env python3
"""Build a Cangjie HarmonyOS project with layered configuration support."""

from __future__ import annotations

import argparse
import os
import platform
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn


def _load_config_helpers():
    skills_dir = Path(__file__).resolve().parents[2]
    helper_dir = skills_dir / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.exists():
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import detect_project_runtime, first_value, load_harmony_config, path_value
        return detect_project_runtime, first_value, load_harmony_config, path_value
    except ImportError:
        return (
            lambda *_, **__: None,
            lambda *values: next((v for v in values if v is not None and v != ""), None),
            lambda **_: None,
            lambda value: Path(value).expanduser() if value else None,
        )


detect_project_runtime, first_value, load_harmony_config, path_value = _load_config_helpers()


DEVECO_HOME_WINDOWS = r"C:/Program Files/Huawei/DevEco Studio"
DEVECO_HOME_LINUX = "/opt/DevEco-Studio"
DEVECO_HOME_MACOS = "/Applications/DevEco-Studio.app/Contents"
DEFAULT_PROJECT_ROOT = Path.cwd()
DEFAULT_OHPM_REGISTRY = "https://ohpm.openharmony.cn/ohpm/"
BUILD_LOG = "build.log"


@dataclass(frozen=True)
class PlatformSpec:
    deveco_home: Path
    runtime_dir: str
    lib_var: str | None


PLATFORMS: dict[str, PlatformSpec] = {
    "Windows": PlatformSpec(Path(DEVECO_HOME_WINDOWS), "windows_x86_64_cjnative", None),
    "Linux": PlatformSpec(Path(DEVECO_HOME_LINUX), "linux_{arch}_cjnative", "LD_LIBRARY_PATH"),
    "Darwin": PlatformSpec(Path(DEVECO_HOME_MACOS), "darwin_{arch}_cjnative", "DYLD_LIBRARY_PATH"),
}


def fail(msg: str, code: int = 1) -> NoReturn:
    print(f"\033[31mERROR: {msg}\033[0m", flush=True)
    sys.exit(code)


def log(msg: str, color: int = 0) -> None:
    print(f"\033[{color}m{msg}\033[0m" if color else msg, flush=True)


def ensure(path: Path, label: str) -> Path:
    if not path.exists():
        fail(
            f"{label} not found: {path}\n"
            "Configure it with CLI options, environment variables, "
            "or ~/.cangjie/cangjie.skills.toml."
        )
    return path


def discover_default_cangjie_sdk() -> Path:
    root = Path.home() / ".cangjie-sdk"
    candidates = [
        path / "cangjie"
        for path in root.iterdir()
        if path.is_dir() and (path / "cangjie" / "build-tools" / "bin").is_dir()
    ] if root.is_dir() else []
    if not candidates:
        return root / "6.1" / "cangjie"

    def version_key(path: Path) -> tuple[int, ...]:
        parts = re.findall(r"\d+", path.parent.name)
        return tuple(int(part) for part in parts) if parts else (0,)

    return max(candidates, key=version_key)


def detect_platform() -> tuple[str, PlatformSpec]:
    name = platform.system()
    if name not in PLATFORMS:
        fail(f"unsupported platform: {name}")
    return name, PLATFORMS[name]


def host_arch() -> str:
    machine = platform.machine().lower()
    if machine in ("", "amd64", "x86_64"):
        return "x86_64"
    if machine in ("arm64", "aarch64"):
        return "aarch64"
    return machine


_ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")


def run(cmd: list[str], env: dict[str, str]) -> None:
    log(f">>> {' '.join(cmd)}", 90)
    proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace")
    with open(BUILD_LOG, "a", encoding="utf-8") as fh:
        for line in proc.stdout:  # type: ignore[union-attr]
            sys.stdout.write(line)
            fh.write(_ANSI_RE.sub("", line))
    rc = proc.wait()
    if rc:
        fail(f"command failed with exit code {rc}", rc)


def run_quiet(cmd: list[str]) -> str:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return proc.stdout.strip() if proc.returncode == 0 else ""
    except FileNotFoundError:
        return ""


def merge_path(env: dict[str, str], var: str, *dirs: Path, prepend: bool = True) -> None:
    existing = [p for p in env.get(var, "").split(os.pathsep) if p]
    new = [str(d) for d in dirs if d.exists()]
    ordered = (new + existing) if prepend else (existing + new)
    seen: set[str] = set()
    result: list[str] = []
    for entry in ordered:
        key = os.path.normcase(os.path.normpath(entry))
        if key not in seen:
            seen.add(key)
            result.append(entry)
    env[var] = os.pathsep.join(result)


def setup_cangjie_env(env: dict[str, str], sdk: Path, plat: str, spec: PlatformSpec) -> None:
    home = ensure(sdk / "build-tools", "CANGJIE_HOME")
    env["CANGJIE_HOME"] = str(home)

    rt_dir = spec.runtime_dir.format(arch=host_arch())
    rt_lib = home / "runtime" / "lib" / rt_dir
    tools_lib = home / "tools" / "lib"

    if spec.lib_var is None:
        merge_path(env, "PATH", tools_lib, home / "bin", home / "tools" / "bin", home / "lib" / rt_dir, rt_lib)
    else:
        merge_path(env, "PATH", home / "bin", home / "tools" / "bin")
        merge_path(env, spec.lib_var, rt_lib, tools_lib)

    merge_path(env, "PATH", Path.home() / ".cjpm" / "bin", prepend=False)

    if plat == "Darwin":
        setup_macos_extras(env, home)


def setup_macos_extras(env: dict[str, str], build_tools: Path) -> None:
    if not env.get("SDKROOT"):
        sdkroot = run_quiet(["xcrun", "--sdk", "macosx", "--show-sdk-path"])
        if sdkroot:
            env["SDKROOT"] = sdkroot
    run_quiet(["xattr", "-dr", "com.apple.quarantine", str(build_tools)])
    debugserver = build_tools / "third_party" / "llvm" / "bin" / "debugserver"
    if debugserver.exists():
        run_quiet([
            "codesign",
            "-s",
            "-",
            "-f",
            "--preserve-metadata=entitlements,requirements,flags,runtime",
            str(debugserver),
        ])


def resolve_build_tools(deveco: Path, plat: str) -> tuple[Path, Path, Path]:
    win_exe = {"ohpm": "ohpm.bat", "node": "node.exe"}
    exe = win_exe.get if plat == "Windows" else lambda _name, default: default
    ohpm = ensure(deveco / "tools" / "ohpm" / "bin" / exe("ohpm", "ohpm"), "ohpm")
    node = ensure(deveco / "tools" / "node" / exe("node", "node"), "Node")
    hvigorw = ensure(deveco / "tools" / "hvigor" / "bin" / "hvigorw.js", "hvigorw")
    return ohpm, node, hvigorw


def detect_default_module(project: Path) -> str:
    profile = project / "build-profile.json5"
    if not profile.exists():
        return "entry"
    text = profile.read_text(encoding="utf-8", errors="replace")
    match = re.search(r'"modules"\s*:\s*\[\s*\{\s*"name"\s*:\s*"([^"]+)"', text, re.S)
    return match.group(1) if match else "entry"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a Cangjie HarmonyOS project")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT), help="Project root path")
    parser.add_argument("--module", default=None, help="HarmonyOS module name. Defaults to config or first module in build-profile.json5.")
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml. Can be passed multiple times.")
    parser.add_argument("--deveco-home", default=None, help="DevEco Studio install root. Overrides config and built-in default.")
    parser.add_argument("--cangjie-sdk", default=None, help="Cangjie SDK root. Overrides config and built-in default.")
    parser.add_argument("--ohpm-registry", default=None, help="ohpm registry URL. Overrides config and built-in default.")
    tls = parser.add_mutually_exclusive_group()
    tls.add_argument("--verify-tls", dest="verify_tls", action="store_true", default=None)
    tls.add_argument("--no-verify-tls", dest="verify_tls", action="store_false", default=None)
    return parser.parse_args()


def main() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
        except (AttributeError, OSError):
            pass

    plat, spec = detect_platform()
    args = parse_args()
    project = ensure(Path(args.project_root).expanduser().resolve(), "Project root")
    os.chdir(project)
    log(f"Project: {project}", 35)

    cfg = load_harmony_config(project_root=project, config_paths=args.config)
    toolchain = getattr(cfg, "toolchain", None)
    runtime_cfg = getattr(cfg, "runtime", None)

    deveco = ensure(
        path_value(first_value(args.deveco_home, os.getenv("DEVECO_HOME"), getattr(toolchain, "deveco_home", None))) or spec.deveco_home,
        "DevEco Studio",
    )
    cangjie = ensure(
        path_value(first_value(args.cangjie_sdk, os.getenv("CANGJIE_SDK_HOME"), getattr(toolchain, "cangjie_sdk", None))) or discover_default_cangjie_sdk(),
        "Cangjie SDK",
    )
    ohpm_registry = first_value(args.ohpm_registry, getattr(toolchain, "ohpm_registry", None), DEFAULT_OHPM_REGISTRY)
    tls_config = getattr(toolchain, "verify_tls", None)
    verify_tls = args.verify_tls if args.verify_tls is not None else (tls_config if tls_config is not None else True)
    detected = detect_project_runtime(project, module=getattr(runtime_cfg, "module", None) if runtime_cfg else None)
    for warning in getattr(detected, "warnings", []) or []:
        log(f"WARN: {warning}", 33)
    module_name = (
        args.module
        or getattr(runtime_cfg, "module", None)
        or getattr(detected, "module", None)
        or detect_default_module(project)
    )

    log(f"DevEco: {deveco}", 36)
    log(f"Cangjie: {cangjie}", 36)
    log(f"Module: {module_name}", 36)

    env = os.environ.copy()
    env.update({
        "DEVECO_HOME": str(deveco),
        "DEVECO_SDK_HOME": str(ensure(deveco / "sdk", "DevEco SDK")),
        "CANGJIE_SDK_HOME": str(cangjie),
        "DEVECO_CANGJIE_PATH": str(cangjie),
    })
    setup_cangjie_env(env, cangjie, plat, spec)

    java = ensure(deveco / "jbr", "Java Runtime")
    env["JAVA_HOME"] = str(java)
    merge_path(env, "PATH", java / "bin")
    log(f"Java: {java}", 36)

    ohpm, node, hvigorw = resolve_build_tools(deveco, plat)
    hv = [str(node), str(hvigorw)]
    hv_opts = ["--analyze=normal", "--parallel", "--incremental", "--no-daemon"]

    open(BUILD_LOG, "w", encoding="utf-8").close()

    log("Installing dependencies...", 35)
    run([str(ohpm), "install", "--all", "--registry", str(ohpm_registry), "--strict_ssl", "true" if verify_tls else "false"], env=env)

    log("Syncing Cangjie resources...", 35)
    run([*hv, "--mode", "module", "-p", f"module={module_name}@default", "SyncCangjieResource", *hv_opts], env=env)

    log("Building HAP...", 35)
    run([*hv, "--mode", "module", "-p", "product=default", "assembleHap", *hv_opts], env=env)

    log("Build complete", 32)


if __name__ == "__main__":
    main()
