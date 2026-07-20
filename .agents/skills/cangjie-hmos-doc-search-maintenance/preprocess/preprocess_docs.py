#!/usr/bin/env python3
"""harmonyos-6.0.2-15k 文档预处理脚本

流水线:
  1. 拍平中间层目录 (API_Reference/source_zh_cn, Dev_Guide)
  2. 合并 Dev_Guide + API_Reference 同主题目录
  3. 移除 figures/ 冗余目录
  4. 按 API 定义拆分多定义文件 (>=2 个 class/func/enum/interface/struct/type H2)
  5. 全量链接重写 (拍平+拆分导致路径变更后修复文档链接)
  6. 生成 .overview.md + .abstract.md (纯规则, 无 LLM)
  7. 生成溯源清单 (.split-manifest.json + .preprocess-meta.json)

Usage:
  python preprocess_docs.py
  python preprocess_docs.py --input <dir> --output <dir>
  python preprocess_docs.py --skip-split  # 跳过拆分, 仅拍平+overview
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# === 默认路径 ===

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent  # .agents/skills/
SKILL_DIR = SKILLS_DIR / "cangjie-hmos-doc-search"
DOCS_DIR = SKILL_DIR / "docs"
DEFAULT_INPUT = DOCS_DIR / "harmonyos-6.0.2-15k"
DEFAULT_OUTPUT = DOCS_DIR / "harmonyos-6.0.2-15k-staged"

# === 目录映射表 ===

KIT_MAP = {
    "AbilityKit": "cj-ability", "AccessibilityKit": "cj-accessibility",
    "AdsKit": "cj-ads", "ArkData": "cj-arkdata",
    "ArkGraphics2D": "cj-arkgraphics2d", "ArkWeb": "cj-web",
    "AssetStoreKit": "cj-assetstore", "AudioKit": "cj-audio",
    "AVSessionKit": "cj-avsession", "BackgroundTasksKit": "cj-backgroundtasks",
    "BasicServicesKit": "cj-basicservices", "CalendarKit": "cj-calendar",
    "CameraKit": "cj-camera", "Common_basic_ability": "cj-common-ability",
    "ConnectivityKit": "cj-connectivity", "ContactsKit": "cj-contacts",
    "CoreFileKit": "cj-corefile", "CryptoArchitectureKit": "cj-crypto",
    "DeviceCertificateKit": "cj-devicecertificate",
    "DistributedServiceKit": "cj-distributedservice", "FormKit": "cj-form",
    "ImageKit": "cj-image", "IMEKit": "cj-ime", "InputKit": "cj-input",
    "IPCKit": "cj-ipc", "LocalizationKit": "cj-localization",
    "LocationKit": "cj-location", "MediaKit": "cj-media",
    "MediaLibraryKit": "cj-medialibrary", "NetworkKit": "cj-network",
    "NotificationKit": "cj-notification",
    "PerformanceAnalysisKit": "cj-hitrace",
    "SensorServiceKit": "cj-sensor", "TelephonyKit": "cj-telephony",
    "TestKit": "cj-test", "UniversalKeystoreKit": "cj-universalkeystore",
    "UserAuthenticationKit": "cj-userauth",
}

DEVGUIDE_MAP = {
    "accessibility": "cj-accessibility",
    "application-dev-prepare": "cj-appdev-prepare",
    "application-models": "cj-application-models",
    "application-test": "cj-test",
    "arkui-cj": "cj-arkui",
    "basic-services": "cj-basicservices",
    "cj-start": "cj-start",
    "contacts": "cj-contacts",
    "database": "cj-database",
    "distributedservice": "cj-distributedservice",
    "file-management": "cj-corefile",
    "graphics": "cj-arkgraphics2d",
    "inputmethod": "cj-ime",
    "internationalization": "cj-localization",
    "ipc": "cj-ipc",
    "location": "cj-location",
    "network": "cj-network",
    "notification": "cj-notification",
    "task-management": "cj-backgroundtasks",
    "telephony": "cj-telephony",
    "tools": "cj-tools",
    "web": "cj-web",
}

DEVGUIDE_SUBDIR_MAP = {
    "connectivity/bluetooth": "cj-connectivity/bluetooth",
    "connectivity/nfc": "cj-connectivity/nfc",
    "connectivity/wlan": "cj-connectivity/wlan",
    "device/sensor": "cj-sensor",
    "media/audio": "cj-audio",
    "media/avsession": "cj-avsession",
    "media/camera": "cj-camera",
    "media/image": "cj-image",
    "media/media": "cj-media",
    "media/medialibrary": "cj-medialibrary",
    "security/AccessToken": "cj-accesstoken",
    "security/AssetStoreKit": "cj-assetstore",
    "security/CodeProtect": "cj-codeprotect",
    "security/CryptoArchitectureKit": "cj-crypto",
    "security/DeviceCertificateKit": "cj-devicecertificate",
    "security/Password_Auto_Fill_Service": "cj-password-autofill",
    "security/UniversalKeystoreKit": "cj-universalkeystore",
    "security/UserAuthenticationKit": "cj-userauth",
}

# === 正则 ===

API_DEF_RE = re.compile(
    r'^## (class|func|enum|interface|struct|type)\s+(\w+)', re.MULTILINE
)
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
H1_RE = re.compile(r'^#\s+(.+)', re.MULTILINE)
H2_RE = re.compile(r'^##\s+(.+)', re.MULTILINE)
FUNC_DESC_RE = re.compile(r'\*\*功能[：:]\*\*\s*(.+?)(?=\n|$)')
IMG_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
TITLE_RE = re.compile(r'\s+"[^"]*"\s*$')

SKIP_MARKERS = {'.overview.md', '.abstract.md'}


# === 工具函数 ===

def read_text(path: Path) -> str:
    full = str(path.resolve())
    if sys.platform == "win32" and len(full) > 240:
        full = "\\\\?\\" + full
    return Path(full).read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sha8(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:8]


def norm_rel(path_str: str) -> str:
    """规范化相对路径 (resolve . and .., use forward slashes)."""
    normalized = os.path.normpath(path_str).replace("\\", "/")
    return normalized


def is_image_target(target: str) -> bool:
    target_clean = target.split("#")[0].split("?")[0].lower()
    return any(target_clean.endswith(ext) for ext in IMG_EXTS)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


def strip_title(target: str) -> str:
    """从 markdown 链接 target 中去除可选的标题属性。
    'path "title"' → 'path'
    'path'         → 'path'
    """
    return TITLE_RE.sub('', target).strip()


def target_exists_in_output(output_dir: Path, new_dir: str, path_part: str) -> bool:
    """检查链接 target (相对于新文件位置) 在输出目录中是否存在。"""
    if not path_part:
        return False
    target_path = output_dir / new_dir / path_part
    return target_path.exists()


# === 步骤 1-3: 拍平 + 合并 + 移除冗余 ===

def map_old_to_new(old_rel: str) -> str | None:
    """将旧相对路径映射到新相对路径。返回 None 表示跳过 (如 figures/)。
    old_rel 相对于 harmonyos-6.0.2-15k 根目录。
    """
    parts = Path(old_rel).parts

    if "figures" in parts:
        return None

    name = Path(old_rel).name
    if name in SKIP_MARKERS:
        return None  # 跳过已有的 overview/abstract (后续重新生成)

    if parts[0] == "API_Reference":
        rest = parts[2:]  # 跳过 API_Reference/source_zh_cn
        if not rest:
            return None

        if rest[0] == "apis" and len(rest) >= 2:
            kit = rest[1]
            if kit in KIT_MAP:
                new_dir = KIT_MAP[kit]
                sub = "/".join(rest[2:])
                return f"{new_dir}/{sub}" if sub else new_dir
            return None  # 未知 Kit

        if rest[0] == "arkinterop":
            sub = "/".join(rest[1:])
            return f"cj-arkts-interop/{sub}" if sub else "cj-arkts-interop"

        if rest[0] == "arkui-cj":
            sub = "/".join(rest[1:])
            return f"cj-arkui/{sub}" if sub else "cj-arkui"

        if rest[0] == "errorcodes":
            sub = "/".join(rest[1:])
            return f"errorcodes/{sub}" if sub else "errorcodes"

        if rest[0].endswith(".md"):
            return f"cj-develop-intro/{rest[0]}"

        return None

    if parts[0] == "Dev_Guide":
        rest = parts[1:]
        if not rest:
            return None

        if len(rest) >= 2:
            subdir_key = f"{rest[0]}/{rest[1]}"
            if subdir_key in DEVGUIDE_SUBDIR_MAP:
                new_dir = DEVGUIDE_SUBDIR_MAP[subdir_key]
                sub = "/".join(rest[2:])
                return f"{new_dir}/{sub}" if sub else new_dir

        if rest[0] in DEVGUIDE_MAP:
            new_dir = DEVGUIDE_MAP[rest[0]]
            sub = "/".join(rest[1:])
            return f"{new_dir}/{sub}" if sub else new_dir

        return None

    return None


def build_and_copy(input_dir: Path, output_dir: Path):
    """扫描输入目录, 构建 path_mappings, 复制 .md 文件到新位置。
    返回 (path_mappings, file_origins)。
    path_mappings: {old_rel: new_rel}
    file_origins: {new_rel: old_rel}  (用于链接重写时知道当前文件的旧位置)
    """
    path_mappings = {}
    file_origins = {}
    skipped = 0
    copied = 0

    for root, dirs, files in os.walk(input_dir):
        dirs[:] = [d for d in dirs if d != "figures"]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            abs_path = Path(root) / fname
            old_rel = abs_path.relative_to(input_dir).as_posix()
            new_rel = map_old_to_new(old_rel)
            if new_rel is None:
                skipped += 1
                continue
            dst = output_dir / new_rel
            write_text(dst, read_text(abs_path))
            path_mappings[old_rel] = new_rel
            file_origins[new_rel] = old_rel
            copied += 1

    return path_mappings, file_origins, copied, skipped


# === 步骤 4: 按 API 定义拆分 (openviking 模式) ===
#
# 拆分规则 (参考 harmonyos-6.0.2-15k_origin/cj-apis-ability):
# 1. 原 .md 文件变为同名目录: cj-apis-ability.md -> cj-apis-ability/
# 2. 目录内放命名空间子目录 (从 H1 推导): ohosabilityAbility/
# 3. 命名空间子目录内:
#    - .overview.md + .abstract.md (命名空间摘要)
#    - 每个 API 定义一个 .md 文件: class_AbilityStage.md (含公共 preamble)
#    - 大定义 (>50KB) 拆为子目录: class_WebviewController/ (含 .overview + 方法文件)
# 4. 目录级 .overview.md + .abstract.md (模块摘要, 步骤 6 自动生成)
# 5. path_mappings 更新: 原 old_rel -> 命名空间 overview 路径

API_LARGE_THRESHOLD = 50 * 1024  # 大定义阈值: 50KB


def derive_namespace_name(content: str) -> str:
    """从 H1 标题推导命名空间名。
    'ohos.ability（Ability）' -> 'ohosabilityAbility'
    'ohos.webview（Webview）' -> 'ohoswebviewWebview'
    """
    m = H1_RE.search(content)
    if not m:
        return ""
    h1 = m.group(1).strip()
    name = re.sub(r'[.（）()\s]', '', h1)
    name = re.sub(r'[^\w\u4e00-\u9fff]', '', name)
    if len(name) > 60:
        name = name[:60]
    return name


def split_content(content: str):
    """将内容按 API 定义 H2 拆分。
    返回 (module_intro, common_sections, [(type, name, section_content), ...]) 或 None。
    module_intro = H1 + 模块介绍段落 (仅用于 overview, 不注入片段)
    common_sections = 导入模块 + 权限列表 + 使用说明等 H2 公共段落 (注入每个片段)
    """
    matches = list(API_DEF_RE.finditer(content))
    if len(matches) < 2:
        return None

    full_preamble = content[:matches[0].start()].rstrip() + "\n"
    h2_match = re.search(r'^## ', full_preamble, re.MULTILINE)
    if h2_match:
        module_intro = full_preamble[:h2_match.start()].rstrip()
        common_sections = full_preamble[h2_match.start():].rstrip() + "\n"
    else:
        module_intro = full_preamble.rstrip()
        common_sections = ""

    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section = content[start:end].rstrip() + "\n"
        sections.append((m.group(1), m.group(2), section))

    return module_intro, common_sections, sections


def extract_section_func(section_content: str) -> str:
    """从 API 定义段落中提取 **功能：** 描述 (用于 overview 快速导航)。"""
    m = FUNC_DESC_RE.search(section_content)
    return m.group(1).strip() if m else ""


def make_fragment_content(common_sections: str, section: str):
    """片段 = common_sections (导入模块+权限列表+使用说明) + API 定义段落。
    不含 H1 模块介绍段落 (那段仅用于 overview)。"""
    if common_sections.strip():
        return common_sections.rstrip() + "\n\n" + section
    return section


def split_files(output_dir: Path, file_origins: dict, path_mappings: dict):
    """扫描输出目录, 拆分多定义文件。
    原 .md 文件变为同名目录, 内含命名空间子目录和拆分片段。
    每个片段包含公共 preamble。
    """
    split_manifest = []
    anchor_splits = {}
    files_to_process = list(file_origins.keys())

    split_count = 0
    total_fragments = 0

    for new_rel in files_to_process:
        file_path = output_dir / new_rel
        if not file_path.exists():
            continue
        content = read_text(file_path)

        result = split_content(content)
        if result is None:
            continue

        module_intro, common_sections, sections = result
        old_rel = file_origins[new_rel]
        parent_dir_str = str(Path(new_rel).parent)
        stem = Path(new_rel).stem

        ns_name = derive_namespace_name(content)
        if not ns_name:
            ns_name = stem

        if parent_dir_str != ".":
            split_dir_rel = f"{parent_dir_str}/{stem}"
            ns_dir_rel = f"{split_dir_rel}/{ns_name}"
        else:
            split_dir_rel = stem
            ns_dir_rel = f"{stem}/{ns_name}"

        ns_dir = output_dir / ns_dir_rel
        ns_dir.mkdir(parents=True, exist_ok=True)

        used_names = set()
        fragments = []
        for sec_type, sec_name, sec_content in sections:
            base = f"{sec_type}_{sec_name}.md"
            frag_filename = base
            if frag_filename in used_names:
                hash_input = f"{new_rel}#{sec_type}#{sec_name}#{len(used_names)}"
                h = sha8(hash_input)
                frag_filename = f"{sec_type}_{sec_name}_2more_{h}.md"
            used_names.add(frag_filename)

            frag_content = make_fragment_content(common_sections, sec_content)
            func_desc = extract_section_func(sec_content)

            if len(frag_content) > API_LARGE_THRESHOLD:
                frag_subdir_rel = f"{ns_dir_rel}/{sec_type}_{sec_name}"
                frag_subdir = output_dir / frag_subdir_rel
                frag_subdir.mkdir(parents=True, exist_ok=True)
                frag_main_path = frag_subdir / f"{sec_type}_{sec_name}_Nmore.md"
                write_text(frag_main_path, frag_content)
                frag_new_rel = f"{frag_subdir_rel}/{sec_type}_{sec_name}_Nmore.md"
            else:
                frag_path = ns_dir / frag_filename
                write_text(frag_path, frag_content)
                frag_new_rel = f"{ns_dir_rel}/{frag_filename}"

            file_origins[frag_new_rel] = old_rel
            anchor_key = f"{old_rel}#{sec_name}"
            anchor_splits[anchor_key] = frag_new_rel
            fragments.append((sec_type, sec_name, frag_filename, frag_new_rel, func_desc))
            total_fragments += 1

        ns_overview = f"# {ns_name}\n\n"
        if module_intro.strip():
            h1_match = H1_RE.search(module_intro)
            if h1_match:
                ns_overview = f"# {h1_match.group(1).strip()}\n\n"
            intro_body = re.sub(r'^#\s+.+\n?', '', module_intro).strip()
            if intro_body:
                ns_overview += intro_body + "\n\n"
        ns_overview += f"该目录包含从 `{stem}.md` 拆分出的 {len(fragments)} 个 API 定义片段。\n\n"
        ns_overview += "## 快速导航\n\n"
        for ft, fn, ff, ffull, fdesc in fragments:
            rel_link = Path(ffull).name if "/" not in ffull else str(Path(ffull).relative_to(ns_dir_rel)).replace("\\", "/")
            if fdesc:
                ns_overview += f"- [`{ff}`](./{rel_link}) - {fdesc}\n"
            else:
                ns_overview += f"- [`{ff}`](./{rel_link}) - {ft} {fn}\n"
        write_text(ns_dir / ".overview.md", ns_overview)
        write_text(ns_dir / ".abstract.md",
                   f"{ns_name}\n\n从 {stem}.md 拆分, {len(fragments)} 个 API 定义\n")

        file_path.unlink()
        del file_origins[new_rel]
        if old_rel in path_mappings:
            path_mappings[old_rel] = f"{ns_dir_rel}/.overview.md"

        split_manifest.append({
            "original_path": new_rel,
            "original_old_path": old_rel,
            "split_dir": split_dir_rel,
            "namespace_dir": ns_dir_rel,
            "fragment_count": len(fragments),
            "fragments": [
                {"path": ff, "kind": ft, "name": fn, "desc": fd}
                for ft, fn, _, ff, fd in fragments
            ],
        })
        split_count += 1

    return split_manifest, anchor_splits, split_count, total_fragments


# === 步骤 5: 全量链接重写 ===

def rewrite_links(output_dir: Path, file_origins: dict, path_mappings: dict,
                  anchor_splits: dict):
    """重写所有文档链接 (图片和外部链接跳过)。"""
    rewritten = 0
    total_links = 0
    skipped_images = 0
    skipped_external = 0
    broken = []

    for new_rel in list(file_origins.keys()):
        file_path = output_dir / new_rel
        if not file_path.exists():
            continue
        content = read_text(file_path)
        old_rel = file_origins[new_rel]
        old_dir = str(Path(old_rel).parent)
        new_dir = str(Path(new_rel).parent)
        changed = False

        def replace_link(m):
            nonlocal total_links, skipped_images, skipped_external, changed
            link_text, target = m.group(1), m.group(2)
            total_links += 1

            if is_external(target):
                skipped_external += 1
                return m.group(0)

            target_clean = strip_title(target)

            if is_image_target(target_clean):
                skipped_images += 1
                return m.group(0)

            path_part, _, anchor = target_clean.partition("#")
            if not path_part:
                return m.group(0)

            old_target = norm_rel(f"{old_dir}/{path_part}")
            if old_target in path_mappings:
                new_target_rel = path_mappings[old_target]
                if anchor:
                    anchor_key = f"{old_target}#{anchor}"
                    if anchor_key in anchor_splits:
                        new_target_rel = anchor_splits[anchor_key]
                        anchor = ""
                new_rel_path = os.path.relpath(
                    new_target_rel, new_dir
                ).replace("\\", "/")
                if anchor:
                    new_rel_path = f"{new_rel_path}#{anchor}"
                changed = True
                return f"[{link_text}]({new_rel_path})"

            if anchor:
                anchor_key = f"{old_target}#{anchor}"
                if anchor_key in anchor_splits:
                    new_target_rel = anchor_splits[anchor_key]
                    new_rel_path = os.path.relpath(
                        new_target_rel, new_dir
                    ).replace("\\", "/")
                    changed = True
                    return f"[{link_text}]({new_rel_path})"

            if target_exists_in_output(output_dir, new_dir, path_part):
                if target_clean != target:
                    changed = True
                    suffix = f"#{anchor}" if anchor else ""
                    return f"[{link_text}]({path_part}{suffix})"
                return m.group(0)

            broken.append((new_rel, link_text, target, old_target))
            return m.group(0)

        new_content = LINK_RE.sub(replace_link, content)
        if changed:
            write_text(file_path, new_content)
            rewritten += 1

    return rewritten, total_links, skipped_images, skipped_external, broken


# === 步骤 6: 生成 .overview.md + .abstract.md ===

def extract_h1(content: str) -> str:
    m = H1_RE.search(content)
    return m.group(1).strip() if m else ""


def extract_func_desc(content: str) -> str:
    m = FUNC_DESC_RE.search(content)
    return m.group(1).strip() if m else ""


def find_overview_source(dir_path: Path) -> str:
    """在目录中寻找已有的概览文件, 返回其内容。"""
    for md_file in sorted(dir_path.glob("*.md")):
        if md_file.name in SKIP_MARKERS:
            continue
        name = md_file.stem.lower()
        if "overview" in name or "intro" in name or name.startswith("cj-overview"):
            return read_text(md_file)
    for md_file in sorted(dir_path.glob("*.md")):
        if md_file.name in SKIP_MARKERS:
            continue
        return read_text(md_file)
    return ""


def generate_overviews(output_dir: Path):
    """为每个含子文档的目录生成 .overview.md + .abstract.md。"""
    generated = 0

    all_dirs = sorted(
        d for d in output_dir.rglob("*") if d.is_dir()
    )
    all_dirs.append(output_dir)

    for dir_path in all_dirs:
        if (dir_path / ".overview.md").exists():
            continue

        md_files = [
            f for f in dir_path.glob("*.md")
            if f.name not in SKIP_MARKERS
        ]
        subdirs = [d for d in dir_path.iterdir() if d.is_dir()]

        if not md_files and not subdirs:
            continue

        overview_source = find_overview_source(dir_path)
        h1 = extract_h1(overview_source) if overview_source else ""
        desc = extract_func_desc(overview_source) if overview_source else ""

        if not h1:
            dir_name = dir_path.name
            h1 = dir_name.replace("cj-", "").replace("-", " ").title()
            if dir_name == output_dir.name:
                h1 = "HarmonyOS 6.0.2 仓颉开发文档"
            elif dir_name == "errorcodes":
                h1 = "错误码"

        if not desc:
            if overview_source:
                lines = overview_source.split("\n")
                for line in lines[1:]:
                    line = line.strip()
                    if line and not line.startswith("#") and not line.startswith("```"):
                        desc = line[:200]
                        break
            if not desc:
                desc = f"该目录包含 {len(md_files)} 个文档"

        is_root = (dir_path == output_dir)

        nav_lines = []
        for sd in sorted(subdirs):
            sd_overview = sd / ".overview.md"
            sd_title = sd.name
            if sd_overview.exists():
                sd_content = read_text(sd_overview)
                sd_h1 = extract_h1(sd_content)
                if sd_h1:
                    sd_title = sd_h1
            nav_lines.append(f"- [`{sd.name}/`](./{sd.name}/) - {sd_title}")

        for md_file in sorted(md_files):
            md_content = read_text(md_file)
            md_h1 = extract_h1(md_content)
            title = md_h1 if md_h1 else md_file.stem
            nav_lines.append(f"- [`{md_file.name}`](./{md_file.name}) - {title}")

        if is_root:
            func_line = f"**功能：** 鸿蒙 HarmonyOS 6.0.2（API 15）仓颉（Cangjie）应用开发文档全集，覆盖 ArkUI 组件、应用模型、网络/媒体/安全等系统能力、错误码与开发工具。"
        else:
            func_line = f"**功能：** {desc}" if not desc.startswith("**功能") else desc

        overview_content = f"# {h1}\n\n{func_line}\n\n## 快速导航\n\n"
        overview_content += "\n".join(nav_lines)
        overview_content += "\n"

        write_text(dir_path / ".overview.md", overview_content)

        abstract_content = f"{h1}\n\n{desc[:200]}\n"
        write_text(dir_path / ".abstract.md", abstract_content)

        generated += 1

    return generated


# === 步骤 7: 生成溯源清单 ===

def generate_manifests(output_dir: Path, split_manifest: list, stats: dict):
    """生成 .split-manifest.json 和 .preprocess-meta.json。"""
    split_path = output_dir / ".split-manifest.json"
    split_data = {
        "version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "splits": split_manifest,
    }
    write_text(split_path, json.dumps(split_data, ensure_ascii=False, indent=2))

    meta_path = output_dir / ".preprocess-meta.json"
    meta_data = {
        "version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": str(stats.get("input_dir", "")),
        "output_dir": str(output_dir),
        "stats": stats,
    }
    write_text(meta_path, json.dumps(meta_data, ensure_ascii=False, indent=2))


# === 主函数 ===

def main():
    parser = argparse.ArgumentParser(description="harmonyos-6.0.2-15k 文档预处理")
    parser.add_argument("--input", default=str(DEFAULT_INPUT),
                        help="输入目录 (原始文档)")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT),
                        help="输出目录 (预处理后)")
    parser.add_argument("--skip-split", action="store_true",
                        help="跳过拆分步骤")
    args = parser.parse_args()

    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()

    if not input_dir.exists():
        print(f"ERROR: 输入目录不存在: {input_dir}")
        sys.exit(1)

    if output_dir.exists():
        print(f"清理已有输出目录: {output_dir}")
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    print(f"输入: {input_dir}")
    print(f"输出: {output_dir}")
    print()

    # 步骤 1-3: 拍平 + 合并 + 移除冗余
    print("=" * 60)
    print("步骤 1-3: 拍平目录 + 合并主题 + 移除 figures/")
    print("=" * 60)
    path_mappings, file_origins, copied, skipped = build_and_copy(
        input_dir, output_dir
    )
    print(f"  复制 .md 文件: {copied}")
    print(f"  跳过 (figures/overview/abstract): {skipped}")
    print(f"  路径映射条目: {len(path_mappings)}")
    print()

    # 步骤 4: 拆分
    split_count = 0
    total_fragments = 0
    split_manifest = []
    anchor_splits = {}

    if args.skip_split:
        print("=" * 60)
        print("步骤 4: 跳过拆分 (--skip-split)")
        print("=" * 60)
    else:
        print("=" * 60)
        print("步骤 4: 按 API 定义拆分多定义文件")
        print("=" * 60)
        split_manifest, anchor_splits, split_count, total_fragments = split_files(
            output_dir, file_origins, path_mappings
        )
        print(f"  拆分文件数: {split_count}")
        print(f"  生成片段数: {total_fragments}")
        print(f"  锚点映射数: {len(anchor_splits)}")
    print()

    # 步骤 5: 链接重写
    print("=" * 60)
    print("步骤 5: 全量链接重写")
    print("=" * 60)
    rewritten, total_links, skipped_img, skipped_ext, broken = rewrite_links(
        output_dir, file_origins, path_mappings, anchor_splits
    )
    print(f"  处理文件数: {rewritten}")
    print(f"  文档链接总数: {total_links}")
    print(f"  跳过图片链接: {skipped_img}")
    print(f"  跳过外部链接: {skipped_ext}")
    print(f"  断链数: {len(broken)}")
    if broken:
        print(f"  断链示例 (前 10):")
        for b in broken[:10]:
            print(f"    {b[0]} -> [{b[1]}]({b[2]})  (resolved: {b[3]})")
    print()

    # 步骤 6: 生成 overview/abstract
    print("=" * 60)
    print("步骤 6: 生成 .overview.md + .abstract.md")
    print("=" * 60)
    overview_count = generate_overviews(output_dir)
    print(f"  生成 overview/abstract 对数: {overview_count}")
    print()

    # 步骤 7: 生成溯源清单
    print("=" * 60)
    print("步骤 7: 生成溯源清单")
    print("=" * 60)
    stats = {
        "input_dir": str(input_dir),
        "copied_md": copied,
        "skipped": skipped,
        "split_files": split_count,
        "total_fragments": total_fragments,
        "rewritten_files": rewritten,
        "total_doc_links": total_links,
        "skipped_image_links": skipped_img,
        "skipped_external_links": skipped_ext,
        "broken_links": len(broken),
        "generated_overviews": overview_count,
        "anchor_splits": len(anchor_splits),
    }
    generate_manifests(output_dir, split_manifest, stats)
    print(f"  .split-manifest.json: {len(split_manifest)} 条拆分记录")
    print(f"  .preprocess-meta.json: 已生成")
    print()

    # 汇总
    total_md = sum(1 for _ in output_dir.rglob("*.md"))
    total_overview = sum(1 for _ in output_dir.rglob(".overview.md"))
    total_abstract = sum(1 for _ in output_dir.rglob(".abstract.md"))
    total_class_files = sum(
        1 for f in output_dir.rglob("*.md")
        if f.name.startswith(("class_", "func_", "enum_", "interface_",
                               "struct_", "type_"))
    )
    total_dirs = sum(1 for d in output_dir.rglob("*") if d.is_dir())

    print("=" * 60)
    print("汇总")
    print("=" * 60)
    print(f"  总 .md 文件数: {total_md}")
    print(f"  总目录数: {total_dirs}")
    print(f"  .overview.md 数: {total_overview}")
    print(f"  .abstract.md 数: {total_abstract}")
    print(f"  API 定义文件 (class_/func_/...): {total_class_files}")
    print(f"  断链数: {len(broken)}")
    print()
    print(f"预处理完成: {output_dir}")


if __name__ == "__main__":
    main()
