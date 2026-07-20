#!/usr/bin/env python3
"""cangjie-docs 预处理脚本 v2 — 处理 std/stdx/kernel/tools → cangjie-docs/

流水线:
  1. 复制+拍平 (_package_api/*.md → 包根，记录 path_mappings)
  2. 单定义 API 文件统一加 class_/func_/... 前缀
  3. 多定义 API 文件拆分 → 片段拍平到包根，删除原聚合文件
  4. 全量链接重写 (修复 _package_api 断链 + 拆分锚点)
  5. 生成 .overview.md + .abstract.md (含根目录 god node)
  6. 生成溯源清单 (.preprocess-meta.json + .split-manifest.json)

v2 修复:
  - P0: API 片段拍平到包根 (不再嵌套 *_package_*/中文/ 子目录)
  - P0: 全量链接重写 (修复 _package_api → 包根路径断链)
  - P1: 拆分后删除原聚合文件 (消除重复节点)
  - P1: 根目录 .overview.md (god node)
  - P1: cj-kernel 标题修正 (不再误写 "HarmonyOS 6.0.2")
  - P2: .preprocess-meta.json + .split-manifest.json

Usage:
  python cangjie_docs.py                    # 全量预处理
  python cangjie_docs.py --source std       # 仅处理 std
  python cangjie_docs.py --source std argopt # 仅处理 std/argopt 模块
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

# === 路径配置 ===

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent  # .agents/skills/
ORIGINAL_DIR = SKILLS_DIR / "cangjie-original-docs"
OUTPUT_DIR = SKILLS_DIR / "cangjie-docs"

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
    normalized = os.path.normpath(path_str).replace("\\", "/")
    return normalized


def is_image_target(target: str) -> bool:
    img_exts = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
    target_clean = target.split("#")[0].split("?")[0].lower()
    return any(target_clean.endswith(ext) for ext in img_exts)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


# === API 定义正则 (适配 cangjie-original-docs H2 模式) ===

# 主匹配: ## kind Name (支持泛型 <T>, where 子句, deprecated, backtick 转义)
API_DEF_RE_CJ = re.compile(
    r'^## (class|func|enum|interface|struct|type)\s+`?(\w+)',
    re.MULTILINE
)

# 辅助: let/const 定义
LET_CONST_RE = re.compile(
    r'^## (let|const)\s+(\w+)',
    re.MULTILINE
)

# 通用: 匹配任意 ## kind xxx H2 (用于判断是否有 API 定义)
ANY_API_H2_RE = re.compile(
    r'^## (class|func|enum|interface|struct|type|let|const)\s+',
    re.MULTILINE
)

LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
H1_RE = re.compile(r'^#\s+(.+)', re.MULTILINE)
FUNC_DESC_RE = re.compile(r'\*\*功能[：:]\*\*\s*(.+?)(?=\n|$)')
TITLE_RE = re.compile(r'\s+"[^"]*"\s*$')

SKIP_MARKERS = {'.overview.md', '.abstract.md'}


# === 名字提取 ===

def extract_api_name(header_line: str, kind: str) -> str:
    """从 H2 标题行提取干净的 API 名称。"""
    # 去掉 kind 前缀和标记
    rest = header_line.lstrip("#").strip()
    # 去掉 kind 关键字
    rest = re.sub(rf'^{kind}\s+', '', rest)
    # 去掉 backtick 转义
    rest = rest.replace('`', '')
    # 取第一个 \w+ 标识符
    m = re.match(r'([\w@]+)', rest)
    if m:
        name = m.group(1)
        if name.startswith('@'):
            name = name[1:]
        return name
    return rest[:50]


def api_kind_from_filename(name: str) -> str | None:
    for prefix in ("class_", "func_", "enum_", "interface_", "struct_", "type_", "let_", "const_"):
        if name.startswith(prefix):
            return prefix.rstrip("_")
    return None


# === 步骤 1: 复制 + 拍平 ===

def copy_std(src_root: Path, dst_root: Path, modules: list[str] | None = None
             ) -> tuple[dict, dict, int]:
    """处理 std 来源。
    
    std/{module}/{module}_package_api/*.md → cj-std/{module}/*.md (拍平)
    std/{module}/{module}_package_overview.md → cj-std/{module}/{module}_package_overview.md (保留)
    跳过 _samples/。
    返回 (path_mappings, file_origins, copied)。
    """
    path_mappings = {}    # old_rel → new_rel
    file_origins = {}     # new_rel → old_rel
    copied = 0

    for module_dir in sorted(src_root.iterdir()):
        if not module_dir.is_dir():
            continue
        module = module_dir.name
        if modules and module not in modules:
            continue

        dst_mod = dst_root / "cj-std" / module
        dst_mod.mkdir(parents=True, exist_ok=True)

        # 1) 复制 _package_api/*.md → 拍平到包根
        api_dir = module_dir / f"{module}_package_api"
        if api_dir.exists():
            for f in sorted(api_dir.rglob("*.md")):
                if f.name.startswith("."):
                    continue
                old_rel = f.relative_to(ORIGINAL_DIR).as_posix()
                new_name = f.name
                new_rel = f"cj-std/{module}/{new_name}"
                dst_file = dst_mod / new_name
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dst_file)
                path_mappings[old_rel] = new_rel
                file_origins[new_rel] = old_rel
                copied += 1

        # 2) 复制模块根目录的概览文件 (不含 _samples 和 _package_api)
        for f in sorted(module_dir.glob("*.md")):
            if f.name.startswith("."):
                continue
            old_rel = f.relative_to(ORIGINAL_DIR).as_posix()
            # 跳过已通过 _package_api 处理的 (同文件名)
            new_name = f.name
            new_rel = f"cj-std/{module}/{new_name}"
            if new_rel in file_origins:
                continue
            dst_file = dst_mod / new_name
            shutil.copy2(f, dst_file)
            path_mappings[old_rel] = new_rel
            file_origins[new_rel] = old_rel
            copied += 1

    return path_mappings, file_origins, copied


def copy_stdx(src_root: Path, dst_root: Path, modules: list[str] | None = None
              ) -> tuple[dict, dict, int]:
    """处理 stdx 来源。

    src_root/{...}/{mod}_package_api/*.md → cj-stdx/{leaf_module}/*.md (拍平)
    跳过 _samples/。
    stdx 有嵌套: encoding/json/, crypto/digest/ 等 — 用最深 _package_api 目录的父级目录名。
    """
    path_mappings = {}
    file_origins = {}
    copied = 0
    seen_modules = set()

    for f in sorted(src_root.rglob("*.md")):
        if f.name.startswith("."):
            continue
        rel_parts = list(f.relative_to(src_root).parts)

        # 跳过 _samples
        if "_samples" in rel_parts or "samples" in rel_parts:
            continue

        # 跳过非 _package_api 且不是模块根的概览文件
        api_idx = -1
        for i, p in enumerate(rel_parts):
            if p.endswith("_package_api"):
                api_idx = i
                break

        if api_idx >= 0:
            # 在 _package_api 内 → 拍平
            parent_idx = api_idx
            if parent_idx > 0:
                module_name = rel_parts[parent_idx]
                # 用父目录名作为模块名 (如 json, http, zlib)
                module_name_simple = rel_parts[parent_idx - 1]
            else:
                module_name = rel_parts[0]
                module_name_simple = module_name.replace("_package_api", "")
        else:
            # 不在 _package_api 内 → 保留在模块根
            # 找出实际模块目录: 第一层目录
            module_name_simple = rel_parts[0]
            # 多层模块如 crypto/crypto/ → 内部目录是 leaf module
            for p in rel_parts[1:]:
                if not p.endswith(("_package_api", "_samples", "_package_overview.md")):
                    if not p.endswith(".md"):
                        module_name_simple = p

        if modules and module_name_simple not in modules:
            continue
        if module_name_simple in seen_modules:
            pass  # 已在处理中
        seen_modules.add(module_name_simple)

        old_rel = f.relative_to(ORIGINAL_DIR).as_posix()

        if api_idx >= 0:
            # 拍平: _package_api 内的文件 → 放到模块根
            new_rel = f"cj-stdx/{module_name_simple}/{f.name}"
        else:
            # 保留原相对路径
            rest = f.relative_to(src_root / module_name_simple).as_posix() \
                   if (src_root / module_name_simple).exists() else f.name
            rest_simple = rest.split("/")[-1] if "/" in rest else rest
            new_rel = f"cj-stdx/{module_name_simple}/{rest_simple}"

        dst_file = output_dir / new_rel
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst_file)
        path_mappings[old_rel] = new_rel
        file_origins[new_rel] = old_rel
        copied += 1

    return path_mappings, file_origins, copied


def copy_kernel(src_root: Path, dst_root: Path, topics: list[str] | None = None
                ) -> tuple[dict, dict, int]:
    """处理 kernel 来源。
    
    kernel/source_zh_cn/{topic}/*.md → cj-kernel/{topic}/*.md (保留子目录结构)
    不拆分、不加前缀。
    """
    path_mappings = {}
    file_origins = {}
    copied = 0

    zh_dir = src_root / "source_zh_cn"
    if not zh_dir.exists():
        return path_mappings, file_origins, 0

    for topic_dir in sorted(zh_dir.iterdir()):
        if not topic_dir.is_dir():
            continue
        if topics and topic_dir.name not in topics:
            continue

        for f in sorted(topic_dir.rglob("*.md")):
            if f.name.startswith("."):
                continue
            old_rel = f.relative_to(ORIGINAL_DIR).as_posix()
            sub_rel = f.relative_to(topic_dir)
            new_rel = f"cj-kernel/{topic_dir.name}/{sub_rel.as_posix()}"
            dst_file = dst_root / new_rel
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst_file)
            path_mappings[old_rel] = new_rel
            file_origins[new_rel] = old_rel
            copied += 1

    return path_mappings, file_origins, copied


def copy_tools(src_root: Path, dst_root: Path
               ) -> tuple[dict, dict, int]:
    """处理 tools 来源。
    
    tools/source_zh_cn/**/*.md → cj-tools/**/*.md
    """
    path_mappings = {}
    file_origins = {}
    copied = 0

    zh_dir = src_root / "source_zh_cn"
    if not zh_dir.exists():
        return path_mappings, file_origins, 0

    for f in sorted(zh_dir.rglob("*.md")):
        if f.name.startswith("."):
            continue
        old_rel = f.relative_to(ORIGINAL_DIR).as_posix()
        sub_rel = f.relative_to(zh_dir)
        new_rel = f"cj-tools/{sub_rel.as_posix()}"
        dst_file = dst_root / new_rel
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst_file)
        path_mappings[old_rel] = new_rel
        file_origins[new_rel] = old_rel
        copied += 1

    return path_mappings, file_origins, copied


# === 步骤 2: 单定义 API 文件统一加前缀 ===

def rename_api_file(file_path: Path, file_origins: dict, path_mappings: dict) -> int:
    """单定义 API 文件加 class_/func_ 等前缀。

    仅处理: 恰好 1 个 API 定义，且文件名无前缀的文件。
    返回重命名数。
    """
    name = file_path.name
    if api_kind_from_filename(name):
        return 0
    if name.startswith("."):
        return 0

    try:
        content = read_text(file_path)
    except Exception:
        return 0

    # 检查 API 定义数
    api_matches = list(API_DEF_RE_CJ.finditer(content))
    lc_matches = list(LET_CONST_RE.finditer(content))

    total_matches = len(api_matches) + len(lc_matches)
    if total_matches != 1:
        return 0  # 0 个或 >1 个 → 不重命名

    # 确定类型和名称
    if api_matches:
        kind, name_match = api_matches[0].group(1), api_matches[0].group(2)
    else:
        kind, name_match = lc_matches[0].group(1), lc_matches[0].group(2)

    new_name = f"{kind}_{name_match}.md"
    if new_name == name:
        return 0

    new_path = file_path.parent / new_name
    if new_path.exists():
        # 同名文件已存在 → 加 hash 去重
        h = sha8(str(file_path))
        new_name = f"{kind}_{name_match}_{h}.md"
        new_path = file_path.parent / new_name

    file_path.rename(new_path)

    # 更新 file_origins 和 path_mappings
    old_new_rel = str(file_path.relative_to(output_dir).as_posix()) \
        .replace("\\", "/") if str(file_path.resolve()).startswith(
            str(output_dir.resolve())) else None
    new_new_rel = str(new_path.relative_to(output_dir).as_posix()).replace("\\", "/")

    if old_new_rel and old_new_rel in file_origins:
        old_rel = file_origins.pop(old_new_rel)
        file_origins[new_new_rel] = old_rel
        # 更新 path_mappings 中的旧路径映射
        for k, v in list(path_mappings.items()):
            if v == old_new_rel:
                path_mappings[k] = new_new_rel

    return 1


# === 步骤 3: API 拆分 ===

def split_api_files(sub_root: Path, file_origins: dict, path_mappings: dict
                    ) -> tuple[list, dict, int, int]:
    """对 sub_root 下的文件做 API 拆分。

    片段直接放在文件所在目录 (拍平)，不创建子目录。
    拆分后删除原聚合文件。
    跳过 cj-kernel。
    返回 (split_manifest, anchor_splits, split_count, total_fragments)。
    """
    split_manifest = []
    anchor_splits = {}
    split_count = 0
    total_fragments = 0

    files_to_check = sorted(sub_root.rglob("*.md"))
    for file_path in files_to_check:
        if file_path.name.startswith("."):
            continue

        try:
            content = read_text(file_path)
        except Exception:
            continue

        # 统计 ## class/func/enum/interface/struct/type H2
        api_matches = list(API_DEF_RE_CJ.finditer(content))
        lc_matches = list(LET_CONST_RE.finditer(content))
        all_matches = api_matches + lc_matches

        if len(all_matches) < 2:
            continue

        # 提取片段
        new_rel_prefix = file_path.relative_to(output_dir).as_posix().replace("\\", "/")
        old_rel = file_origins.get(new_rel_prefix, new_rel_prefix)

        parent_dir = file_path.parent
        used_names = set()
        fragments = []

        # 按位置排序
        merged = [(m.start(), m.group(1), m.group(2), m, 'a') for m in api_matches] + \
                 [(m.start(), m.group(1), m.group(2), m, 'l') for m in lc_matches]
        merged.sort(key=lambda x: x[0])

        for i, (start, kind, name_word, m, _) in enumerate(merged):
            end = merged[i + 1][0] if i + 1 < len(merged) else len(content)
            section = content[start:end].rstrip() + "\n"

            base = f"{kind}_{name_word}.md"
            frag_name = base
            if frag_name in used_names:
                h = sha8(f"{file_path}#{kind}#{name_word}#{len(used_names)}")
                frag_name = f"{kind}_{name_word}_2more_{h}.md"
            used_names.add(frag_name)

            frag_path = parent_dir / frag_name
            write_text(frag_path, section)

            frag_rel = frag_path.relative_to(output_dir).as_posix().replace("\\", "/")
            file_origins[frag_rel] = old_rel

            # 生成 anchor_splits: 三种格式覆盖原始文档的所有锚点模式
            # 1. 精确名称: old_rel#Iterable
            anchor_splits[f"{old_rel}#{name_word}"] = frag_rel
            # 2. kind-name 小写: old_rel#interface-iterable
            anchor_splits[f"{old_rel}#{kind}-{name_word.lower()}"] = frag_rel
            # 3. 原始 markdown 锚点: 模拟 GitHub anchor 算法
            #    保留 [a-z0-9 -], 移除其他字符, 空格替换为短横线
            header_line = content[start:content.index('\n', start) if '\n' in content[start:] else len(content)].strip()
            raw_anchor = header_line.lstrip('#').strip().lower()
            raw_anchor = raw_anchor.replace('\\', '')
            raw_anchor = re.sub(r'[^a-z0-9 -]', '', raw_anchor)     # keep only alnum + space + hyphen
            raw_anchor = raw_anchor.replace(' ', '-')                # each space → hyphen
            raw_anchor = raw_anchor.strip('-')
            anchor_splits[f"{old_rel}#{raw_anchor}"] = frag_rel

            # 4. 含 <sup>(deprecated)</sup> 的变体: 先剥离 HTML 标签再同上处理
            raw2 = header_line.lstrip('#').strip().lower()
            raw2 = raw2.replace('\\', '')
            raw2 = re.sub(r'<[^>]+>', '', raw2)                     # strip HTML tags
            raw2 = re.sub(r'[^a-z0-9 -]', '', raw2)
            raw2 = raw2.replace(' ', '-').strip('-')
            if raw2 != raw_anchor:
                anchor_splits[f"{old_rel}#{raw2}"] = frag_rel

            fragments.append({
                "path": frag_rel,
                "kind": kind,
                "name": name_word,
            })
            total_fragments += 1

        # 删除原聚合文件
        file_path.unlink()
        if new_rel_prefix in file_origins:
            del file_origins[new_rel_prefix]
        # 删除 path_mappings 中的旧条目 (聚合文件已删除，不应映射到任意片段)
        if old_rel in path_mappings:
            del path_mappings[old_rel]

        split_manifest.append({
            "original_path": new_rel_prefix,
            "original_old_path": old_rel,
            "fragment_count": len(fragments),
            "fragments": fragments,
        })
        split_count += 1

    return split_manifest, anchor_splits, split_count, total_fragments


# === 步骤 4: 全量链接重写 ===

def rewrite_links(output_dir: Path, file_origins: dict, path_mappings: dict,
                  anchor_splits: dict):
    """重写所有文档链接。"""
    rewritten = 0
    total_links = 0
    skipped_images = 0
    skipped_external = 0
    broken = []

    for new_rel in list(file_origins.keys()):
        file_path = output_dir / new_rel
        if not file_path.exists():
            continue

        try:
            content = read_text(file_path)
        except Exception:
            continue

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

            target_clean = re.sub(TITLE_RE, '', target).strip()

            if is_image_target(target_clean):
                skipped_images += 1
                return m.group(0)

            path_part, _, anchor = target_clean.partition("#")
            if not path_part:
                return m.group(0)

            # 去掉 _en/html/ 等垃圾路径 (来自原始文档的预处理残留)
            if path_part.startswith("_en/") or path_part.startswith("html/"):
                return m.group(0)

            # 标准化旧目标路径
            old_target = norm_rel(f"{old_dir}/{path_part}")

            # 0) 自引用链接: 聚合文件在拆分后的内部锚点链接 → 改为当前文件名
            if old_target == old_rel:
                if anchor:
                    new_rel_path = f"./{Path(new_rel).name}#{anchor}"
                else:
                    new_rel_path = f"./{Path(new_rel).name}"
                changed = True
                return f"[{link_text}]({new_rel_path})"

            # 1) 在 path_mappings 中查找
            if old_target in path_mappings:
                new_target_rel = path_mappings[old_target]
                # 处理锚点
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

            # 2) 仅锚点映射
            if anchor:
                anchor_key = f"{old_target}#{anchor}"
                if anchor_key in anchor_splits:
                    new_target_rel = anchor_splits[anchor_key]
                    new_rel_path = os.path.relpath(
                        new_target_rel, new_dir
                    ).replace("\\", "/")
                    changed = True
                    return f"[{link_text}]({new_rel_path})"

            # 3) 检查目标是否存在 (同名文件拍平后仍有效)
            resolved = (output_dir / new_dir / path_part).resolve()
            if resolved.exists():
                if target_clean != target:
                    changed = True
                    suffix = f"#{anchor}" if anchor else ""
                    return f"[{link_text}]({path_part}{suffix})"
                return m.group(0)

            broken.append((new_rel, link_text[:40], target, old_target))
            return m.group(0)

        new_content = LINK_RE.sub(replace_link, content)
        if changed:
            write_text(file_path, new_content)
            rewritten += 1

    return rewritten, total_links, skipped_images, skipped_external, broken


# === 步骤 5: 生成 .overview.md + .abstract.md ===

def extract_h1(content: str) -> str:
    m = H1_RE.search(content)
    return m.group(1).strip() if m else ""


def extract_func_desc(content: str) -> str:
    m = FUNC_DESC_RE.search(content)
    return m.group(1).strip() if m else ""


def find_best_source(dir_path: Path) -> str:
    """在目录中寻找最佳源文件 (用于提取 H1 和描述)。"""
    # 优先: *_package_overview.md
    for md_file in sorted(dir_path.glob("*_package_overview.md")):
        return read_text(md_file)
    # 其次: 非 split 片段的普通 md
    for md_file in sorted(dir_path.glob("*.md")):
        if md_file.name in SKIP_MARKERS:
            continue
        name = md_file.stem.lower()
        if "overview" in name or "intro" in name:
            return read_text(md_file)
    for md_file in sorted(dir_path.glob("*.md")):
        if md_file.name in SKIP_MARKERS:
            continue
        # 排除拆分后的片段 (已有前缀)
        if api_kind_from_filename(md_file.name):
            continue
        return read_text(md_file)
    return ""


def generate_overviews(output_dir: Path):
    """为每个含子文档的目录生成 .overview.md + .abstract.md。"""
    generated = 0

    all_dirs = sorted(d for d in output_dir.rglob("*") if d.is_dir())
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

        overview_source = find_best_source(dir_path)
        h1 = extract_h1(overview_source) if overview_source else ""
        desc = extract_func_desc(overview_source) if overview_source else ""

        # 确定标题
        if not h1:
            dir_name = dir_path.name
            parent_name = dir_path.parent.name if dir_path.parent != output_dir else ""

            if dir_path == output_dir:
                h1 = "仓颉编程语言文档"
            elif parent_name in ("cj-kernel", "cj-std", "cj-stdx", "cj-tools"):
                h1 = f"{dir_name} 文档"
            elif dir_name == "cj-kernel":
                h1 = "仓颉语言内核文档"
            elif dir_name == "cj-std":
                h1 = "仓颉标准库文档"
            elif dir_name == "cj-stdx":
                h1 = "仓颉扩展标准库文档"
            elif dir_name == "cj-tools":
                h1 = "仓颉工具链文档"
            else:
                h1 = dir_name.replace("cj-", "").replace("-", " ").replace("_", " ").title()

        # 修正误写: cj-kernel 标题不能是 "HarmonyOS 6.0.2"
        if "harmonyos" in h1.lower() or "harmony" in h1.lower():
            if dir_path.name == "cj-kernel" or str(dir_path).endswith("cj-kernel"):
                h1 = "仓颉语言内核文档"
            elif "kernel" in str(dir_path).lower():
                h1 = dir_path.name.replace("cj-", "").replace("-", " ").title() + " 文档"

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
        is_top_domain = dir_path.parent == output_dir

        nav_lines = []
        for sd in sorted(subdirs):
            sd_overview = sd / ".overview.md"
            sd_title = sd.name
            if sd_overview.exists():
                sd_content = read_text(sd_overview)
                sd_h1 = extract_h1(sd_content)
                if sd_h1:
                    sd_title = sd_h1[:60]
            nav_lines.append(f"- [`{sd.name}/`](./{sd.name}/) - {sd_title}")

        for md_file in sorted(md_files):
            md_content = read_text(md_file)
            md_h1 = extract_h1(md_content)
            title = md_h1 if md_h1 else md_file.stem
            # 截断长标题
            if len(title) > 80:
                title = title[:77] + "..."
            nav_lines.append(f"- [`{md_file.name}`](./{md_file.name}) - {title}")

        if is_root:
            func_line = ("**功能：** 仓颉（Cangjie）编程语言官方文档全集，"
                        "覆盖语言内核、标准库、扩展标准库与开发工具链。")
        elif is_top_domain:
            domain_name = h1
            func_line = f"**功能：** {desc}" if not desc.startswith("**功能") else desc
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


# === 步骤 6: 溯源清单 ===

def generate_manifests(output_dir: Path, split_manifest: list, stats: dict):
    split_path = output_dir / ".split-manifest.json"
    split_data = {
        "version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "splits": split_manifest,
    }
    write_text(split_path, json.dumps(split_data, ensure_ascii=False, indent=2))

    meta_path = output_dir / ".preprocess-meta.json"
    meta_data = {
        "version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": str(stats.get("input_dir", "")),
        "output_dir": str(output_dir),
        "stats": stats,
    }
    write_text(meta_path, json.dumps(meta_data, ensure_ascii=False, indent=2))


# === 主函数 ===

def main():
    global output_dir
    parser = argparse.ArgumentParser(description="cangjie-docs 预处理 v2")
    parser.add_argument("--source", nargs="+", default=[],
                        help="指定来源 (std stdx kernel tools)，可加模块名过滤")
    parser.add_argument("--output", default=str(OUTPUT_DIR), help="输出目录")
    parser.add_argument("--skip-split", action="store_true", help="跳过拆分步骤")
    parser.add_argument("--skip-links", action="store_true", help="跳过链接重写")
    args = parser.parse_args()

    output_dir = Path(args.output)
    src_std = ORIGINAL_DIR / "std"
    src_stdx = ORIGINAL_DIR / "libs_stdx"
    src_kernel = ORIGINAL_DIR / "kernel"
    src_tools = ORIGINAL_DIR / "tools"

    source_filter = None
    module_filter = None
    if args.source:
        source_filter = set()
        for s in args.source:
            if s in ("std", "stdx", "kernel", "tools"):
                source_filter.add(s)
            else:
                if module_filter is None:
                    module_filter = set()
                module_filter.add(s)
    if not source_filter:
        source_filter = {"std", "stdx", "kernel", "tools"}

    print(f"cangjie-docs 预处理 v2")
    print(f"原始文档: {ORIGINAL_DIR}")
    print(f"输出目录: {output_dir}")
    print()

    # 清理输出
    if output_dir.exists():
        print("清理旧输出...")
        shutil.rmtree(output_dir)

    all_path_mappings = {}
    all_file_origins = {}
    stats = {"input_dir": str(ORIGINAL_DIR)}

    # === 步骤 1: 复制 ===
    print("=" * 60)
    print("步骤 1: 复制 + 拍平 (记录 path_mappings)")
    print("=" * 60)

    if "std" in source_filter:
        modules = list(module_filter) if module_filter else None
        pm, fo, copied = copy_std(src_std, output_dir, modules)
        all_path_mappings.update(pm)
        all_file_origins.update(fo)
        stats["std_copied"] = copied
        print(f"  std: {copied} files copied, {len(pm)} path_mappings")

    if "stdx" in source_filter:
        modules = list(module_filter) if module_filter else None
        pm, fo, copied = copy_stdx(src_stdx, output_dir, modules)
        all_path_mappings.update(pm)
        all_file_origins.update(fo)
        stats["stdx_copied"] = copied
        print(f"  stdx: {copied} files copied, {len(pm)} path_mappings")

    if "kernel" in source_filter:
        topics = list(module_filter) if module_filter else None
        pm, fo, copied = copy_kernel(src_kernel, output_dir, topics)
        all_path_mappings.update(pm)
        all_file_origins.update(fo)
        stats["kernel_copied"] = copied
        print(f"  kernel: {copied} files copied, {len(pm)} path_mappings")

    if "tools" in source_filter:
        pm, fo, copied = copy_tools(src_tools, output_dir)
        all_path_mappings.update(pm)
        all_file_origins.update(fo)
        stats["tools_copied"] = copied
        print(f"  tools: {copied} files copied, {len(pm)} path_mappings")

    print(f"  总计: path_mappings={len(all_path_mappings)}, file_origins={len(all_file_origins)}")
    print()

    # === 步骤 2: 重命名单定义文件 ===
    print("=" * 60)
    print("步骤 2: 单定义 API 文件统一加 class_/func_ 前缀")
    print("=" * 60)
    total_renamed = 0
    for md_file in sorted(output_dir.rglob("*.md")):
        if md_file.name.startswith("."):
            continue
        total_renamed += rename_api_file(md_file, all_file_origins, all_path_mappings)
    stats["renamed_single_def"] = total_renamed
    print(f"  重命名: {total_renamed} files")
    print()

    # === 步骤 3: 拆分 ===
    split_manifest = []
    anchor_splits = {}
    split_count = 0
    total_fragments = 0

    if args.skip_split:
        print("=" * 60)
        print("步骤 3: 跳过拆分 (--skip-split)")
        print("=" * 60)
    else:
        print("=" * 60)
        print("步骤 3: API 多定义文件拆分 → 拍平到包根")
        print("=" * 60)
        for subdir in sorted(output_dir.iterdir()):
            if not subdir.is_dir():
                continue
            if subdir.name == "cj-kernel":
                print(f"  {subdir.name}: 跳过 (概念文档不拆分)")
                continue
            sm, asc, sc, tf = split_api_files(subdir, all_file_origins, all_path_mappings)
            split_manifest.extend(sm)
            anchor_splits.update(asc)
            split_count += sc
            total_fragments += tf
            if sc > 0:
                print(f"  {subdir.name}: {sc} files split → {tf} fragments")

        stats["split_count"] = split_count
        stats["total_fragments"] = total_fragments
        stats["anchor_splits"] = len(anchor_splits)
        print(f"  总计: {split_count} files split, {total_fragments} fragments, "
              f"{len(anchor_splits)} anchor_splits")
    print()

    # === 步骤 4: 链接重写 ===
    if args.skip_links:
        print("=" * 60)
        print("步骤 4: 跳过链接重写 (--skip-links)")
        print("=" * 60)
    else:
        print("=" * 60)
        print("步骤 4: 全量链接重写 (修复 _package_api 断链)")
        print("=" * 60)
        rewritten, total_links, skipped_img, skipped_ext, broken = rewrite_links(
            output_dir, all_file_origins, all_path_mappings, anchor_splits
        )
        stats["rewritten_files"] = rewritten
        stats["total_doc_links"] = total_links
        stats["skipped_image_links"] = skipped_img
        stats["skipped_external_links"] = skipped_ext
        stats["broken_links"] = len(broken)
        print(f"  处理文件数: {rewritten}")
        print(f"  文档链接总数: {total_links}")
        print(f"  跳过图片链接: {skipped_img}")
        print(f"  跳过外部链接: {skipped_ext}")
        print(f"  断链数: {len(broken)}")
        if broken and len(broken) <= 20:
            for b in broken:
                print(f"    {b[0]} -> [{b[1]}]({b[2]})")
    print()

    # === 步骤 5: Overview ===
    print("=" * 60)
    print("步骤 5: 生成 .overview.md + .abstract.md (含根 god node)")
    print("=" * 60)
    overview_count = generate_overviews(output_dir)
    stats["generated_overviews"] = overview_count
    print(f"  生成 overview/abstract 对: {overview_count}")
    print()

    # === 步骤 6: 清单 ===
    print("=" * 60)
    print("步骤 6: 生成溯源清单")
    print("=" * 60)
    generate_manifests(output_dir, split_manifest, stats)
    print(f"  .split-manifest.json: {len(split_manifest)} 条记录")
    print(f"  .preprocess-meta.json: 已生成")
    print()

    # === 汇总 ===
    total_md = sum(1 for _ in output_dir.rglob("*.md"))
    total_dirs = sum(1 for d in output_dir.rglob("*") if d.is_dir())
    total_overview = sum(1 for _ in output_dir.rglob(".overview.md"))
    total_abstract = sum(1 for _ in output_dir.rglob(".abstract.md"))
    total_api = sum(
        1 for f in output_dir.rglob("*.md")
        if f.name.startswith((
            "class_", "func_", "enum_", "interface_", "struct_", "type_", "let_", "const_"
        ))
    )

    print("=" * 60)
    print("汇总")
    print("=" * 60)
    print(f"  总 .md 文件: {total_md}")
    print(f"  总目录: {total_dirs}")
    print(f"  .overview.md: {total_overview}")
    print(f"  .abstract.md: {total_abstract}")
    print(f"  API 定义文件 (class_/func_/...): {total_api}")
    print(f"  断链数: {stats.get('broken_links', 'N/A')}")
    print()
    print(f"预处理完成: {output_dir}")


if __name__ == "__main__":
    main()
