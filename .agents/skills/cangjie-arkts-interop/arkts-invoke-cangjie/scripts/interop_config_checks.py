#!/usr/bin/env python3
"""
Shared checks for ArkTS–Cangjie interop wiring:
  - cjpm.toml: [package].name, [profile.build.combined], [dependencies]
  - build-profile.json5: cangjieOptions.path → cjpm.toml, flattenLibs: true
  - src/main/cangjie/package.cj: package line, ohos.ark_interop.*, import <dep>.*

Used by scan_interop_project.py and verify_interop_structure.py.
"""

from __future__ import annotations

import re
from pathlib import Path

SKIP_DIR_NAMES = frozenset(
    {
        ".git",
        ".idea",
        ".hvigor",
        ".gradle",
        "node_modules",
        "oh_modules",
        "build",
        "dist",
        ".next",
    }
)

SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
PKG_NAME_RE = re.compile(
    r'^\s*name\s*=\s*(?:"([^"]+)"|\'([^\']+)\')\s*$'
)
# Top-level dependency key: j2cj = { ... } or "quoted-key" = ...
DEP_KEY_RE = re.compile(r"""^\s*(?:"([^"]+)"|([A-Za-z_][A-Za-z0-9_]*))\s*=\s*""")
# profile.build.combined entries
COMBINED_ENTRY_RE = re.compile(
    r'^\s*(?:"([^"]+)"|([A-Za-z_][A-Za-z0-9_]*))\s*=\s*(?:"([^"]*)"|\'([^\']*)\')\s*$'
)
FLATTEN_TRUE_RE = re.compile(r'"flattenLibs"\s*:\s*true\b')
CJPM_PATH_RE = re.compile(r'"path"\s*:\s*"([^"]*cjpm\.toml)"')
PACKAGE_LINE_RE = re.compile(r"^\s*package\s+(\S+)\s*$")
IMPORT_DEP_RE = re.compile(
    r"^\s*import\s+([A-Za-z_][A-Za-z0-9_]*)\s*\.\s*\*\s*$"
)
FIXED_ARK_INTEROP_IMPORT = "import ohos.ark_interop.*"


def should_skip_path(path: Path) -> bool:
    return any(name in SKIP_DIR_NAMES for name in path.parts)


def find_module_root_holding_oh_package(start_dir: Path) -> Path | None:
    """Walk up from start_dir looking for oh-package.json5 (Harmony module root)."""
    cur = start_dir.resolve()
    for _ in range(12):
        if (cur / "oh-package.json5").is_file():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def parse_cjpm_interop_fields(text: str) -> tuple[str | None, list[str], dict[str, str]]:
    """
    Parse minimal fields from cjpm.toml (line-oriented, tolerates common TOML).

    Returns:
      package_name or None
      dependency keys in file order (only [dependencies] table, first-level keys)
      combined map for [profile.build.combined] (key -> value string)
    """
    section = ""
    package_name: str | None = None
    dep_keys: list[str] = []
    combined: dict[str, str] = {}

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        msec = SECTION_RE.match(stripped)
        if msec:
            section = msec.group(1).strip()
            continue

        if section == "package":
            m = PKG_NAME_RE.match(stripped)
            if m:
                package_name = m.group(1) or m.group(2)
            continue

        if section == "dependencies":
            m = DEP_KEY_RE.match(stripped)
            if m:
                key = m.group(1) or m.group(2)
                dep_keys.append(key)
            continue

        if section == "profile.build.combined":
            m = COMBINED_ENTRY_RE.match(stripped)
            if m:
                key = m.group(1) or m.group(2)
                val = m.group(3) or m.group(4) or ""
                combined[key] = val
            continue

    return package_name, dep_keys, combined


def check_build_profile_json5(
    bp: Path, module_root: Path, cjpm_path: Path
) -> list[str]:
    """Check module build-profile.json5 for flattenLibs and cjpm path resolving to this cjpm.toml."""
    issues: list[str] = []
    try:
        text = bp.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [f"{bp}: 无法读取 build-profile.json5 ({e})"]

    if "cangjieOptions" not in text:
        issues.append(f"{bp}: 未发现 cangjieOptions，请配置仓颉构建选项。")
    if not FLATTEN_TRUE_RE.search(text):
        issues.append(
            f"{bp}: 未发现 \"flattenLibs\": true，请按技能文档在 cangjieOptions 中补齐。"
        )
    mpath = CJPM_PATH_RE.search(text)
    if not mpath:
        issues.append(
            f"{bp}: 未发现指向 cjpm.toml 的 \"path\" 配置（例如 \"./cjpm.toml\" 或 \"./src/main/cangjie/cjpm.toml\"）。"
        )
    else:
        rel_decl = mpath.group(1).strip().lstrip("./").replace("\\", "/")
        candidate = (module_root / rel_decl).resolve()
        try:
            if candidate != cjpm_path.resolve():
                issues.append(
                    f"{bp}: cangjieOptions.path \"{mpath.group(1)}\" 解析为 {candidate}，"
                    f"与本模块 cjpm.toml（{cjpm_path}）不一致。"
                )
        except OSError:
            issues.append(
                f"{bp}: cangjieOptions.path \"{mpath.group(1)}\" 无法相对于模块根 {module_root} 解析。"
            )
    return issues


def check_package_cj(
    package_cj: Path, package_name: str, dep_keys: list[str]
) -> list[str]:
    issues: list[str] = []
    if not package_cj.is_file():
        issues.append(
            f"{package_cj}: 缺少 package.cj，请按技能文档在仓颉根目录创建并写入 package、"
            "import ohos.ark_interop.* 及 cjpm [dependencies] 对应的 import。"
        )
        return issues

    try:
        text = package_cj.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [f"{package_cj}: 无法读取 ({e})"]

    first_pkg: str | None = None
    for line in text.splitlines():
        m = PACKAGE_LINE_RE.match(line.strip())
        if m:
            first_pkg = m.group(1)
            break
    if first_pkg is None:
        issues.append(f"{package_cj}: 未找到 package 声明行。")
    elif first_pkg != package_name:
        issues.append(
            f"{package_cj}: package 行应为 `package {package_name}`（与 cjpm [package].name 一致），"
            f"当前为 `package {first_pkg}`。"
        )

    if FIXED_ARK_INTEROP_IMPORT not in text:
        issues.append(f"{package_cj}: 缺少固定导入 `{FIXED_ARK_INTEROP_IMPORT}`。")

    imports_found = {m.group(1) for m in IMPORT_DEP_RE.finditer(text, re.MULTILINE)}
    # ohos is not a cjpm dependency key for this check
    imports_found.discard("ohos")
    missing = [k for k in dep_keys if k not in imports_found]
    if missing:
        issues.append(
            f"{package_cj}: 缺少与 cjpm.toml [dependencies] 对齐的 import："
            + ", ".join(f"`import {k}.*`" for k in missing)
        )

    return issues


def check_cjpm_combined_profile(
    cjpm_path: Path, package_name: str | None, combined: dict[str, str]
) -> list[str]:
    issues: list[str] = []
    if not package_name:
        issues.append(f"{cjpm_path}: 缺少 [package].name，无法校验 profile.build.combined。")
        return issues
    if not combined:
        issues.append(
            f"{cjpm_path}: 缺少 [profile.build.combined] 表，请添加 `{package_name} = \"dynamic\"`。"
        )
        return issues
    if package_name not in combined:
        issues.append(
            f"{cjpm_path}: [profile.build.combined] 中缺少键 `{package_name} = \"dynamic\"`。"
        )
        return issues
    val = combined[package_name]
    if val != "dynamic":
        issues.append(
            f"{cjpm_path}: [profile.build.combined] 中 `{package_name}` 当前为 \"{val}\"，"
            "技能要求为 \"dynamic\"（若工程刻意不同，请人工确认）。"
        )
    return issues


def validate_interop_config_for_cjpm(cjpm_path: Path) -> list[str]:
    """
    Run all interop config checks for one cjpm.toml path.
    Returns a list of human-readable issue strings (empty if OK).
    """
    issues: list[str] = []
    cjpm_path = cjpm_path.resolve()
    if not cjpm_path.is_file():
        return [f"{cjpm_path}: cjpm.toml 不存在。"]

    try:
        raw = cjpm_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [f"{cjpm_path}: 无法读取 ({e})"]

    package_name, dep_keys, combined = parse_cjpm_interop_fields(raw)
    issues.extend(check_cjpm_combined_profile(cjpm_path, package_name, combined))

    cangjie_root = cjpm_path.parent
    package_cj = cangjie_root / "package.cj"
    if package_name:
        issues.extend(check_package_cj(package_cj, package_name, dep_keys))

    module_root = find_module_root_holding_oh_package(cangjie_root)
    if module_root is None:
        issues.append(
            f"{cjpm_path}: 向上未找到 oh-package.json5，跳过 build-profile.json5 校验；"
            "请确认 cjpm 位于 Harmony 模块的 src/main/cangjie/ 下。"
        )
        return issues

    bp = module_root / "build-profile.json5"
    if bp.is_file():
        issues.extend(check_build_profile_json5(bp, module_root, cjpm_path))
    else:
        issues.append(f"{module_root / 'build-profile.json5'}: 缺少 build-profile.json5。")

    return issues


def collect_all_interop_config_issues(project_root: Path) -> list[str]:
    """Scan project for every cjpm.toml and aggregate config issues."""
    root = project_root.resolve()
    all_issues: list[str] = []
    for path in sorted(root.rglob("cjpm.toml")):
        if not path.is_file() or should_skip_path(path):
            continue
        all_issues.extend(validate_interop_config_for_cjpm(path))
    return all_issues
