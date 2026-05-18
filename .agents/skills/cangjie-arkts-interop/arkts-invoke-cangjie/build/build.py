#!/usr/bin/env python3
"""仓颉鸿蒙应用 跨平台构建脚本"""

import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, NoReturn, Optional

# ── 安装路径（必须通过环境变量提供，脚本内无回退路径） ───────────
#   DEVECO_HOME        DevEco Studio 根目录（其下含 sdk/、tools/、jbr/）
#   CANGJIE_SDK_HOME   仓颉 SDK 根目录（须含 compiler/）

# ── 平台配置 ─────────────────

@dataclass(frozen=True)
class PlatformSpec:
    """平台相关环境变量名与仓颉 runtime 目录名"""

    runtime_dir: str  # 可含 {arch} 占位符
    lib_var: Optional[str]  # 动态库搜索路径变量名，Windows 为 None


PLATFORMS: dict[str, PlatformSpec] = {
    "Windows": PlatformSpec(
        runtime_dir="windows_x86_64_cjnative",
        lib_var=None,
    ),
    "Linux": PlatformSpec(
        runtime_dir="linux_{arch}_cjnative",
        lib_var="LD_LIBRARY_PATH",
    ),
    "Darwin": PlatformSpec(
        runtime_dir="darwin_{arch}_cjnative",
        lib_var="DYLD_LIBRARY_PATH",
    ),
}


# ── 路径常量 ──────────────────────────────────────────────────

DEFAULT_PROJECT_ROOT = Path.cwd()
BUILD_LOG = "build.log"
# 限制 Hvigor 内 cjpm -j
_CJPM_WORKER_PATCH = Path(__file__).resolve().parent / "patch_cjpm_worker_count.js"
# .hvigor 缓存若仍引用脚手架模板路径会导致在错误工程上跑 cjpm
_HVIGOR_TEMPLATE_POISON = "skills/x2cj/scaffold/template/deveco_app".replace("\\", "/").lower()
_STRIP_KEYS_FOR_DEVECO = frozenset({
    "PYTHONPATH", "PYTHONHOME", "PYTHONSAFEPATH", "PYTHONNOUSERSITE",
    "NODE_OPTIONS", "ELECTRON_RUN_AS_NODE", "OPENSSL_CONF",
})


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


def resolve_deveco_home() -> Path:
    """从环境变量 ``DEVECO_HOME`` 解析 DevEco 根目录。"""
    raw = os.environ.get("DEVECO_HOME", "").strip()
    if not raw:
        fail("未设置环境变量 DEVECO_HOME（DevEco Studio 安装根目录）")
    return Path(raw).expanduser().resolve()


def resolve_cangjie_sdk_home() -> Path:
    """从环境变量 ``CANGJIE_SDK_HOME`` 解析仓颉 SDK 根目录。"""
    raw = os.environ.get("CANGJIE_SDK_HOME", "").strip()
    if not raw:
        fail("未设置环境变量 CANGJIE_SDK_HOME（仓颉 SDK 根目录，须含 compiler/）")
    return Path(raw).expanduser().resolve()


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

def strip_deveco_host_pollution(env: dict[str, str]) -> None:
    """去掉易干扰 cjpm/LLVM 子进程的环境变量（键名大小写不敏感）。"""
    for k in list(env.keys()):
        if k.upper() in _STRIP_KEYS_FOR_DEVECO:
            env.pop(k, None)


def run(cmd: list[str], env: dict[str, str]) -> None:
    """执行命令，实时输出并追加写入 build.log，失败时退出"""
    log(f">>> {' '.join(cmd)}", 90)
    proc = subprocess.Popen(
        cmd,
        env=env,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        errors="replace",
    )
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

# Windows：PATH 中含这些片段时，常见错误加载非 DevEco 自带的 LLVM/运行库，cjpm 可能 0xC0000005
_WIN_PATH_RISK_SUBSTR: tuple[str, ...] = (
    "conda",
    "anaconda",
    "miniconda",
    "mambaforge",
    "micromamba",
    "msys64",
    "msys32",
    "mingw",
    "ucrt64",
    "clang64",
)


def _path_flagged_risky_win(entry: str) -> bool:
    pl = entry.lower().replace("\\", "/")
    return any(s in pl for s in _WIN_PATH_RISK_SUBSTR)


def list_risky_windows_path_entries(path_value: str) -> List[str]:
    """根据一段 PATH 文本列出疑似与仓颉/cjpm LLVM 冲突的目录（只读，不修改任何 env）。"""
    if not path_value.strip():
        return []
    parts = [p.strip() for p in path_value.split(os.pathsep) if p.strip()]
    return [p for p in parts if _path_flagged_risky_win(p)]


def _windows_git_executable_dirs() -> List[Path]:
    """
    返回应加入 PATH 的目录（含 git.exe），供 cjpm 拉取 git 依赖。
    在收窄 PATH 之前用用户环境解析；并探测常见安装位置。
    """
    found: List[Path] = []
    seen: set[str] = set()

    def add(d: Path) -> None:
        if not d.is_dir():
            return
        key = os.path.normcase(str(d.resolve()))
        if key in seen:
            return
        seen.add(key)
        found.append(d)

    user_path = os.environ.get("PATH", "")
    git_exe = shutil.which("git", path=user_path or None)
    if git_exe:
        add(Path(git_exe).resolve().parent)

    for env_key in ("ProgramFiles", "ProgramFiles(x86)"):
        base = os.environ.get(env_key)
        if not base:
            continue
        root = Path(base)
        for sub in ("Git/cmd", "Git/bin"):
            d = root / sub
            if (d / "git.exe").is_file():
                add(d)

    return found


def inject_git_into_path_win(env: dict[str, str]) -> None:
    """收窄 PATH 后补回 Git，避免 cjpm 报「git is not available」。"""
    dirs = _windows_git_executable_dirs()
    if not dirs:
        log(
            "警告: 未检测到 Git（PATH 与常见安装路径均无 git.exe）。"
            "cjpm 的 git 依赖将失败，请安装 Git 并加入系统 PATH。",
            33,
        )
        return
    merge_path(env, "PATH", *dirs, prepend=False)
    log(f"已注入 Git 到 PATH: {os.pathsep.join(str(d) for d in dirs)}", 36)


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
    home = ensure(sdk / "compiler", "CANGJIE_HOME")
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
    node = deveco / "tools" / "node" / exe("node", "node")
    if not node.exists():
        node = deveco / "tools" / "node" / "bin" / exe("node", "node")
    node = ensure(node, "Node")
    hvigorw = ensure(deveco / "tools" / "hvigor" / "bin" / "hvigorw.js", "hvigorw")
    return ohpm, node, hvigorw


def _hvigor_node_cmd(node: Path, hvigorw: Path) -> list[str]:
    """node 启动 hvigorw，可选预加载 patch 以限制 cjpm -j。"""
    cmd = [str(node)]
    if _CJPM_WORKER_PATCH.is_file():
        cmd.extend(["--require", str(_CJPM_WORKER_PATCH)])
    cmd.append(str(hvigorw))
    return cmd


def ensure_local_properties(project: Path, deveco: Path) -> None:
    """无 local.properties 时写入 sdk.dir，避免 CLI 下 SDK 解析异常。"""
    lp = project / "local.properties"
    if lp.is_file():
        return
    sdk = (deveco / "sdk").resolve()
    if not sdk.is_dir():
        return
    esc = str(sdk).replace("\\", "\\\\")
    try:
        lp.write_text(f"sdk.dir={esc}\n", encoding="utf-8")
        log("已写入 local.properties（sdk.dir）", 36)
    except OSError:
        pass


def reset_hvigor_if_cache_foreign_project(project: Path) -> None:
    """file-cache 仍引用本仓库 deveco_app 模板时删除 .hvigor，避免在错误根目录调 cjpm。"""
    hvigor = project / ".hvigor"
    fc = hvigor / "cache" / "file-cache.json"
    if not fc.is_file():
        return
    try:
        data = fc.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    if _HVIGOR_TEMPLATE_POISON not in data.replace("\\", "/").lower():
        return
    log("已删除 .hvigor：file-cache 仍引用 x2cj 脚手架模板路径", 33)
    shutil.rmtree(hvigor, ignore_errors=True)


# ── 主流程 ────────────────────────────────────────────────────


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
        except (AttributeError, OSError):
            pass

    plat, spec = detect_platform()

    parser = argparse.ArgumentParser(
        description="仓颉鸿蒙应用 跨平台构建脚本",
        epilog="须预先设置环境变量: DEVECO_HOME、CANGJIE_SDK_HOME。",
    )
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT),
                        help="项目根目录路径")
    parser.add_argument(
        "--no-sanitize-path",
        action="store_true",
        help="Windows 下不将子进程 PATH 收窄为 System32（保留完整用户 PATH；调试用）",
    )
    parser.add_argument(
        "--cjpm-max-jobs",
        type=int,
        default=None,
        metavar="N",
        help="限制 DevEco 传给 cjpm 的并行度 -j（Node 预加载）；Windows 默认 1，其它平台默认不限制",
    )
    args = parser.parse_args()

    if args.cjpm_max_jobs is not None and args.cjpm_max_jobs < 1:
        fail("--cjpm-max-jobs 须为 >= 1 的整数")

    project = Path(args.project_root).expanduser().resolve()
    ensure(project, "项目路径")
    os.chdir(project)
    log(f"项目目录: {project}", 35)

    deveco = ensure(resolve_deveco_home(), "DevEco Studio")
    cangjie = ensure(resolve_cangjie_sdk_home(), "Cangjie SDK")
    log(f"DevEco: {deveco}", 36)
    log(f"Cangjie: {cangjie}", 36)

    ensure_local_properties(project, deveco)
    reset_hvigor_if_cache_foreign_project(project)

    env = os.environ.copy()
    strip_deveco_host_pollution(env)
    if plat == "Windows" and not args.no_sanitize_path:
        # 仅根据宿主原始 PATH 做启发式列举并打印，不修改 env["PATH"]（收窄在下一行整段赋值）
        removed = list_risky_windows_path_entries(os.environ.get("PATH", ""))
        if removed:
            log(
                f"原始 PATH 中识别到 {len(removed)} 条疑似冲突项（仅打印 removed，未改 env）；"
                f"子进程将收窄为 SystemRoot+System32 并注入工具链/Git"
                f"（对比用可加 --no-sanitize-path）",
                36,
            )
            for p in removed:
                log(f"  − {p}", 90)
        # 整段替换 PATH，避免 conda/msys 等与自带 LLVM 抢 DLL；再由 merge_path 注入工具链
        sysroot = os.environ.get("SystemRoot", r"C:\Windows")
        env["PATH"] = f"{sysroot}{os.pathsep}{sysroot}\\System32"
        log("Windows: PATH 基底已设为 %SystemRoot% 与 System32（与 --no-sanitize-path 互斥）", 36)
        inject_git_into_path_win(env)

    cangjie_compiler = ensure(cangjie / "compiler", "Cangjie compiler")
    env.update({
        "DEVECO_HOME": str(deveco),
        "DEVECO_SDK_HOME": str(ensure(deveco / "sdk", "DevEco SDK")),
        "CANGJIE_SDK_HOME": str(cangjie),
        "DEVECO_CANGJIE_PATH": str(cangjie),
        # cjpm.toml 中 ${DEVECO_CANGJIE_HOME}/third_party/llvm 在 compiler 根下
        "DEVECO_CANGJIE_HOME": str(cangjie_compiler),
    })
    setup_cangjie_env(env, cangjie, plat, spec)
    if plat == "Windows":
        llvm_rt = cangjie_compiler / "runtime" / "lib" / "windows_x86_64_llvm"
        if llvm_rt.is_dir():
            merge_path(env, "PATH", llvm_rt)

    java = ensure(deveco / "jbr", "Java Runtime")
    env["JAVA_HOME"] = str(java)
    merge_path(env, "PATH", java / "bin")
    log(f"Java: {java}", 36)

    ohpm, node, hvigorw = resolve_build_tools(deveco, plat)
    # NODE_HOME 必须是「含 node 可执行文件的目录」，不能是 node.exe 本身（ohpm 会拼 %NODE_HOME%\node）
    node_home = node.parent
    env["NODE_HOME"] = str(node_home)
    env["NODE_OPTS"] = "--max-old-space-size=10240"
    if plat == "Windows":
        env.setdefault("LLVM_PARALLEL_COMPILE_JOBS", "1")
        env.setdefault("OMP_NUM_THREADS", "1")
        env["LD_LIBRARY_PATH"] = str(
            cangjie_compiler / "runtime" / "lib" / "windows_x86_64_llvm"
        )
        env["AARCH64_LIBS"] = str(cangjie / "build" / "linux_ohos_aarch64_llvm" / "ohos")
        env["AARCH64_MACRO_LIBS"] = str(
            cangjie / "build" / "x86_64-w64-mingw32" / "macro" / "ohos"
        )
        env["X86_64_OHOS_LIBS"] = str(
            cangjie / "build" / "linux_ohos_x86_64_llvm" / "ohos"
        )
        env["X86_64_OHOS_MACRO_LIBS"] = str(
            cangjie / "build" / "x86_64-w64-mingw32" / "macro" / "ohos"
        )

    cjpm_jobs: Optional[int] = args.cjpm_max_jobs
    if cjpm_jobs is None and plat == "Windows":
        cjpm_jobs = 1
    if cjpm_jobs is not None:
        env["X2CJ_CJPM_MAX_JOBS"] = str(cjpm_jobs)
        if _CJPM_WORKER_PATCH.is_file():
            log(f"cjpm 并行度上限: {cjpm_jobs}（Node --require patch_cjpm_worker_count.js）", 36)
        else:
            log("警告: 缺少 patch_cjpm_worker_count.js，X2CJ_CJPM_MAX_JOBS 无法影响 cjpm -j", 33)

    # ohpm 通过 PATH 找 node；hvigorw.js 同目录下的 bin 供子进程解析 hvigor 相关命令（对齐 hvigorw.py 的 hvigor_bin_dir）
    merge_path(env, "PATH", hvigorw.parent, node_home, ohpm.parent)
    hv = _hvigor_node_cmd(node, hvigorw)
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
