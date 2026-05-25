#!/usr/bin/env python3
"""仓颉鸿蒙应用 跨平台构建脚本"""

import argparse
import os
import platform
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

# ── 用户可配置常量（按本机实际安装路径修改） ──────────────────
# Windows 默认路径
DEVECO_HOME_WINDOWS = r"C:/Program Files/Huawei/DevEco Studio"
# Linux 默认路径
DEVECO_HOME_LINUX = "/opt/DevEco-Studio"
# macOS 默认路径
DEVECO_HOME_MACOS = "/Applications/DevEco-Studio.app/Contents"

# ── 平台配置 ──────────────────────────────────────────────────


@dataclass(frozen=True)
class PlatformSpec:
    """平台相关路径与环境变量配置"""

    deveco_home: Path
    runtime_dir: str  # 可含 {arch} 占位符
    lib_var: str | None  # 动态库搜索路径变量名，Windows 为 None


PLATFORMS: dict[str, PlatformSpec] = {
    "Windows": PlatformSpec(
        deveco_home=Path(DEVECO_HOME_WINDOWS),
        runtime_dir="windows_x86_64_cjnative",
        lib_var=None,
    ),
    "Linux": PlatformSpec(
        deveco_home=Path(DEVECO_HOME_LINUX),
        runtime_dir="linux_{arch}_cjnative",
        lib_var="LD_LIBRARY_PATH",
    ),
    "Darwin": PlatformSpec(
        deveco_home=Path(DEVECO_HOME_MACOS),
        runtime_dir="darwin_{arch}_cjnative",
        lib_var="DYLD_LIBRARY_PATH",
    ),
}


# ── 路径常量 ──────────────────────────────────────────────────

DEFAULT_PROJECT_ROOT = Path.cwd()
DEFAULT_CANGJIE_SDK = Path.home() / ".cangjie-sdk" / "6.0" / "cangjie"
BUILD_LOG = "build.log"


# ── 基础工具 ──────────────────────────────────────────────────


def fail(msg: str, code: int = 1) -> NoReturn:
    print(f"\033[31m错误: {msg}\033[0m", flush=True)
    sys.exit(code)


def log(msg: str, color: int = 0) -> None:
    print(f"\033[{color}m{msg}\033[0m" if color else msg, flush=True)


def ensure(path: Path, label: str) -> Path:
    """校验路径存在，不存在则退出"""
    if not path.exists():
        fail(f"{label} 不存在: {path}")
    return path


def detect_platform() -> tuple[str, PlatformSpec]:
    name = platform.system()
    if name not in PLATFORMS:
        fail(f"暂不支持的平台: {name}")
    return name, PLATFORMS[name]


def host_arch() -> str:
    """主机架构归一化"""
    m = platform.machine().lower()
    if m in ("", "amd64", "x86_64"):
        return "x86_64"
    if m in ("arm64", "aarch64"):
        return "aarch64"
    return m


# ── 命令执行 ──────────────────────────────────────────────────
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")

def run(cmd: list[str], env: dict[str, str]) -> None:
    """执行命令，实时输出并追加写入 build.log，失败时退出"""
    log(f">>> {' '.join(cmd)}", 90)
    proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, errors="replace")
    with open(BUILD_LOG, "a", encoding="utf-8") as f:
        for line in proc.stdout:  # type: ignore[union-attr]
            sys.stdout.write(line)
            f.write(_ANSI_RE.sub("", line))
    rc = proc.wait()
    if rc:
        fail(f"命令失败 (exit {rc})", rc)


def run_quiet(cmd: list[str]) -> str:
    """静默执行，失败返回空串"""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return r.stdout.strip() if r.returncode == 0 else ""
    except FileNotFoundError:
        return ""


# ── 路径变量合并 ──────────────────────────────────────────────


def merge_path(env: dict[str, str], var: str, *dirs: Path, prepend: bool = True) -> None:
    """将存在的目录合并到路径变量 (默认前置)，原地修改，自动去重"""
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


# ── 仓颉 SDK 环境 ────────────────────────────────────────────


def setup_cangjie_env(env: dict[str, str], sdk: Path, plat: str, spec: PlatformSpec) -> None:
    """按 envsetup 等价规则构造仓颉 SDK 运行环境"""
    home = ensure(sdk / "build-tools", "CANGJIE_HOME")
    env["CANGJIE_HOME"] = str(home)

    rt_dir = spec.runtime_dir.format(arch=host_arch())
    rt_lib = home / "runtime" / "lib" / rt_dir
    tools_lib = home / "tools" / "lib"

    if spec.lib_var is None:
        # Windows: 所有库目录统一走 PATH
        merge_path(
            env, "PATH",
            tools_lib, home / "bin", home / "tools" / "bin",
            home / "lib" / rt_dir, rt_lib,
        )
    else:
        merge_path(env, "PATH", home / "bin", home / "tools" / "bin")
        merge_path(env, spec.lib_var, rt_lib, tools_lib)

    merge_path(env, "PATH", Path.home() / ".cjpm" / "bin", prepend=False)

    if plat == "Darwin":
        _setup_macos_extras(env, home)


def _setup_macos_extras(env: dict[str, str], build_tools: Path) -> None:
    """macOS: 设置 SDKROOT、移除隔离属性、签名 debugserver"""
    if not env.get("SDKROOT"):
        sdkroot = run_quiet(["xcrun", "--sdk", "macosx", "--show-sdk-path"])
        if sdkroot:
            env["SDKROOT"] = sdkroot

    run_quiet(["xattr", "-dr", "com.apple.quarantine", str(build_tools)])

    ds = build_tools / "third_party" / "llvm" / "bin" / "debugserver"
    if ds.exists():
        run_quiet([
            "codesign", "-s", "-", "-f",
            "--preserve-metadata=entitlements,requirements,flags,runtime",
            str(ds),
        ])


# ── DevEco 工具链 ─────────────────────────────────────────────

def resolve_build_tools(deveco: Path, plat: str) -> tuple[Path, Path, Path]:
    """定位 ohpm / node / hvigorw"""
    _WIN_EXE = {"ohpm": "ohpm.bat", "node": "node.exe"}
    exe = _WIN_EXE.get if plat == "Windows" else lambda name, d: d

    ohpm = ensure(deveco / "tools" / "ohpm" / "bin" / exe("ohpm", "ohpm"), "ohpm")
    node = ensure(deveco / "tools" / "node" / exe("node", "node"), "Node")
    hvigorw = ensure(deveco / "tools" / "hvigor" / "bin" / "hvigorw.js", "hvigorw")
    return ohpm, node, hvigorw


# ── 主流程 ────────────────────────────────────────────────────


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
        except (AttributeError, OSError):
            pass

    plat, spec = detect_platform()

    parser = argparse.ArgumentParser(description="仓颉鸿蒙应用 跨平台构建脚本")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT),
                        help="项目根目录路径")
    project = Path(parser.parse_args().project_root).expanduser().resolve()
    ensure(project, "项目路径")
    os.chdir(project)
    log(f"项目目录: {project}", 35)

    deveco = ensure(spec.deveco_home, "DevEco Studio")
    cangjie = ensure(DEFAULT_CANGJIE_SDK, "Cangjie SDK")
    log(f"DevEco: {deveco}", 36)
    log(f"Cangjie: {cangjie}", 36)

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

    open(BUILD_LOG, "w").close()

    log("安装依赖...", 35)
    run([str(ohpm), "install", "--all",
         "--registry", "https://ohpm.openharmony.cn/ohpm/",
         "--strict_ssl", "true"], env=env)

    log("同步资源...", 35)
    run([*hv, "--mode", "module", "-p", "module=entry@default",
         "SyncCangjieResource", *hv_opts], env=env)

    log("编译构建...", 35)
    run([*hv, "--mode", "module", "-p", "product=default",
         "assembleHap", *hv_opts], env=env)

    log("构建完成", 32)


if __name__ == "__main__":
    main()
