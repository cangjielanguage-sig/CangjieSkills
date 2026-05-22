#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from interop_config_checks import collect_all_interop_config_issues

FILE_PATTERNS = [
    "*.cj",
    "*.ets",
    "*.ts",
    "build-profile.json5",
    "oh-package.json5",
    "module.json5",
    "cjpm.toml",
]

MARKERS = [
    "@Interop[ArkTS]",
    "requireCJLib",
    "libark_interop_loader.so",
    "ark_interop_api",
    "CJHybridComponent",
    "registerJSFunc",
    "unregisterJSFunc",
]

LIB_CALL_RE = re.compile(r'requireCJLib\(\s*["\']([^"\']+)["\']\s*\)')
IMPORT_LIB_RE = re.compile(r'from\s+["\'](lib[^"\']+\.so)["\']')
PACKAGE_DEP_RE = re.compile(r'["\'](lib[^"\']+\.so)["\']\s*:')
EXPORT_SYMBOL_RE = re.compile(r"@Interop\[ArkTS\]\s*(?:\r?\n\s*)?public\s+(?:class|func|interface)\s+([A-Za-z_]\w*)")
DECLARE_CLASS_RE = re.compile(r"export\s+declare\s+class\s+([A-Za-z_]\w*)")
CUSTOMLIB_MEMBER_RE = re.compile(r"^\s*([A-Za-z_]\w*)\s*:", re.MULTILINE)
INTERFACE_METHOD_RE = re.compile(r"^\s*([A-Za-z_]\w*)\s*\(", re.MULTILINE)
ABI_RE = re.compile(r'"abiFilters"\s*:\s*\[(.*?)\]', re.DOTALL)
ABI_VALUE_RE = re.compile(r'"([^"]+)"')


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return any(
        name in parts
        for name in (
            ".git",
            ".idea",
            ".hvigor",
            ".gradle",
            "node_modules",
            "oh_modules",
            "build",
            "dist",
            ".next",
            "mock",
        )
    )


def collect_files(root: Path) -> list[Path]:
    seen: set[Path] = set()
    files: list[Path] = []
    for pattern in FILE_PATTERNS:
        for path in root.rglob(pattern):
            if path.is_file() and not should_skip(path):
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    files.append(path)
    return sorted(files)


def scan_file(path: Path) -> dict[str, object] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    markers = [marker for marker in MARKERS if marker in text]
    libs = LIB_CALL_RE.findall(text)
    imported_libs = IMPORT_LIB_RE.findall(text)
    package_deps = PACKAGE_DEP_RE.findall(text) if path.name == "oh-package.json5" else []
    export_names = EXPORT_SYMBOL_RE.findall(text) if path.suffix == ".cj" else []
    is_interop_decl = "ark_interop_api" in path.parts or (
        path.name in {"Index.d.ts", "Index.d.ets"} and path.parent.name.startswith("lib")
    )
    interface_methods = (
        DECLARE_CLASS_RE.findall(text) + CUSTOMLIB_MEMBER_RE.findall(text) + INTERFACE_METHOD_RE.findall(text)
        if path.suffix in {".ets", ".ts"} and is_interop_decl
        else []
    )
    abi_filters = ABI_VALUE_RE.findall(ABI_RE.search(text).group(1)) if path.name == "build-profile.json5" and ABI_RE.search(text) else []
    if not markers and not libs and not imported_libs and not package_deps and not export_names and not interface_methods and not abi_filters:
        return None

    return {
        "path": str(path),
        "markers": markers,
        "libraries": libs,
        "imported_libraries": imported_libs,
        "package_dependencies": package_deps,
        "exports": export_names,
        "interface_methods": interface_methods,
        "abi_filters": abi_filters,
    }


def build_findings(summary: dict[str, object]) -> list[str]:
    hits = summary["marker_hits"]
    findings: list[str] = []

    has_exports = any(hit["exports"] for hit in hits)
    has_loader = any("libark_interop_loader.so" in hit["markers"] for hit in hits)
    has_require = bool(summary["required_libraries"])
    has_interop_api = bool(summary["interop_api_dirs"])
    abi_filters = sorted({abi for hit in hits for abi in hit["abi_filters"]})
    package_deps = {dep for hit in hits for dep in hit["package_dependencies"]}

    export_names = sorted({name for hit in hits for name in hit["exports"]})
    interface_methods = sorted({name for hit in hits for name in hit["interface_methods"]})
    missing_in_interface = sorted(set(export_names) - set(interface_methods))
    missing_package_deps = sorted(set(summary["required_libraries"]) - package_deps)

    if not summary["candidate_cangjie_dirs"]:
        findings.append("未发现仓颉源码目录或 cjpm.toml，先确认工程是否真的接入了仓颉模块。")
    if not has_exports:
        findings.append("未发现带 @Interop[ArkTS] 的 public 导出，ArkTS 侧即使装载成功也可能没有可调用入口。")
    if has_require and not has_loader:
        findings.append("发现 requireCJLib 调用，但未发现从 libark_interop_loader.so 导入 requireCJLib，先核对导入语句。")
    if has_require and "libark_interop_loader.so" not in package_deps:
        findings.append("发现 requireCJLib 调用，但模块 oh-package.json5 未声明 libark_interop_loader.so 依赖。")
    if missing_package_deps:
        findings.append(f"这些 requireCJLib 库未出现在模块 oh-package.json5 依赖中：{', '.join(missing_package_deps)}。")
    if has_exports and not has_interop_api:
        findings.append("发现仓颉导出但未发现 ark_interop_api 目录，优先重新执行 Generate Cangjie-ArkTS Interop API。")
    if missing_in_interface:
        findings.append(f"这些仓颉导出未出现在 interop 声明里：{', '.join(missing_in_interface)}。优先重生成声明。")
    if abi_filters and "arm64-v8a" not in abi_filters:
        findings.append("abiFilters 未包含 arm64-v8a，真机运行可能失败。")
    if abi_filters and "x86_64" not in abi_filters:
        findings.append("abiFilters 未包含 x86_64，模拟器调试可能失败。")
    if has_loader and not has_require:
        findings.append("已导入 libark_interop_loader.so，但未发现 requireCJLib 的实际装载调用。")

    return findings


def build_recommendations(summary: dict[str, object]) -> list[str]:
    recs = [
        "先核对仓颉导出点、ark_interop_api 生成物、ArkTS 装载点三者是否同时存在。",
    ]
    if summary["required_libraries"]:
        libs = ", ".join(summary["required_libraries"])
        recs.append(f"优先核对 requireCJLib 中的库名是否真实存在：{libs}。")
    else:
        recs.append("当前未发现 requireCJLib 实际装载代码，若目标是 ArkTS 主调仓颉，先补装载点。")
    if summary["interop_api_dirs"]:
        recs.append("已发现 ark_interop_api，先确认调用侧引用的是最新生成物，而不是手写旧 interface。")
    else:
        recs.append("未发现 ark_interop_api，优先执行 Generate Cangjie-ArkTS Interop API。")
    recs.append("若问题仍未定位，再按“导出符号 -> 生成声明 -> 库名 -> ABI -> 线程边界”的顺序排查。")
    return recs


def summarize(root: Path) -> dict[str, object]:
    files = collect_files(root)
    hits = [item for path in files if (item := scan_file(path))]

    cangjie_dirs = sorted(
        {
            str(path.parent)
            for path in files
            if path.suffix == ".cj" or path.name == "cjpm.toml"
        }
    )
    arkts_dirs = sorted(
        {
            str(path.parent)
            for path in files
            if path.suffix in {".ets", ".ts"}
        }
    )
    interop_api_dirs = sorted(
        {
            str(path.parent)
            for path in files
            if "ark_interop_api" in path.parts
            or (path.name in {"Index.d.ts", "Index.d.ets"} and path.parent.name.startswith("lib"))
        }
    )
    libraries = sorted({lib for hit in hits for lib in hit["libraries"]})
    imported_libraries = sorted({lib for hit in hits for lib in hit["imported_libraries"]})
    package_dependencies = sorted({dep for hit in hits for dep in hit["package_dependencies"]})
    findings = build_findings(
        {
            "candidate_cangjie_dirs": cangjie_dirs,
            "candidate_arkts_dirs": arkts_dirs,
            "interop_api_dirs": interop_api_dirs,
            "required_libraries": libraries,
            "imported_libraries": imported_libraries,
            "package_dependencies": package_dependencies,
            "marker_hits": hits,
        }
    )
    recommendations = build_recommendations(
        {
            "candidate_cangjie_dirs": cangjie_dirs,
            "candidate_arkts_dirs": arkts_dirs,
            "interop_api_dirs": interop_api_dirs,
            "required_libraries": libraries,
            "imported_libraries": imported_libraries,
            "package_dependencies": package_dependencies,
            "marker_hits": hits,
        }
    )

    interop_config_issues = collect_all_interop_config_issues(root)
    findings = findings + interop_config_issues

    return {
        "root": str(root),
        "candidate_cangjie_dirs": cangjie_dirs,
        "candidate_arkts_dirs": arkts_dirs,
        "interop_api_dirs": interop_api_dirs,
        "required_libraries": libraries,
        "imported_libraries": imported_libraries,
        "package_dependencies": package_dependencies,
        "marker_hits": hits,
        "findings": findings,
        "interop_config_issues": interop_config_issues,
        "recommendations": recommendations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a HarmonyOS project for ArkTS/Cangjie interop clues."
    )
    parser.add_argument("project_root", help="Path to the HarmonyOS project root")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of human-readable text",
    )
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Project root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    summary = summarize(root)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    print(f"Project: {summary['root']}")
    print()

    print("Candidate Cangjie dirs:")
    for path in summary["candidate_cangjie_dirs"] or ["(none)"]:
        print(f"  - {path}")
    print()

    print("Candidate ArkTS dirs:")
    for path in summary["candidate_arkts_dirs"] or ["(none)"]:
        print(f"  - {path}")
    print()

    print("Interop API dirs:")
    for path in summary["interop_api_dirs"] or ["(none)"]:
        print(f"  - {path}")
    print()

    print("Libraries requested via requireCJLib:")
    for lib in summary["required_libraries"] or ["(none)"]:
        print(f"  - {lib}")
    print()

    print("Native libraries declared in oh-package.json5:")
    for lib in summary["package_dependencies"] or ["(none)"]:
        print(f"  - {lib}")
    print()

    print("Recommended next steps:")
    for item in summary["recommendations"] or ["(none)"]:
        print(f"  - {item}")
    print()

    print("Potential inconsistencies:")
    for item in summary["findings"] or ["(none found)"]:
        print(f"  - {item}")
    print()

    print("Marker hits:")
    if not summary["marker_hits"]:
        print("  - (none)")
        return 0

    for hit in summary["marker_hits"]:
        print(f"  - {hit['path']}")
        if hit["markers"]:
            print(f"    markers: {', '.join(hit['markers'])}")
        if hit["libraries"]:
            print(f"    libraries: {', '.join(hit['libraries'])}")
        if hit["package_dependencies"]:
            print(f"    package dependencies: {', '.join(hit['package_dependencies'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
