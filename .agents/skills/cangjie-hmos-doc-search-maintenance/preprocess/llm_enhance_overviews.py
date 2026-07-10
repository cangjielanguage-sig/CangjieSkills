#!/usr/bin/env python3
"""LLM 增强 overview 文件 — 参考 openviking 格式，生成中文 overview 和 abstract。

对每个 .overview.md 调用 LLM 生成：
1. 模块/目录的中文描述段落
2. 按语义分组的快速导航
3. 每个子项的详细描述

Usage:
  OPENAI_API_KEY=sk-... python llm_enhance_overviews.py --docs-dir <dir> --target <subdir>
  OPENAI_API_KEY=sk-... python llm_enhance_overviews.py --docs-dir <dir>  # 全量
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent
SKILL_DIR = SKILLS_DIR / "cangjie-hmos-doc-search"
DEFAULT_DOCS_DIR = SKILL_DIR / "docs" / "harmonyos-6.0.2-15k-staged"

API_BASE = os.environ.get("OPENAI_BASE_URL", "http://113.46.219.251:8080/v1")
API_MODEL = os.environ.get("OPENAI_MODEL", "GLM-5.2")
API_KEY = os.environ.get("OPENAI_API_KEY", "")
TEMPERATURE = 0
MAX_TOKENS = 8192
TIMEOUT = 600
MAX_RETRIES = 3
RETRY_SLEEP = 2
CONCURRENCY = 5

FUNC_DESC_RE = re.compile(r'\*\*功能[：:]\*\*\s*(.+?)(?=\n|$)')
H3_RE = re.compile(r'^###\s+(.+)', re.MULTILINE)
H1_RE = re.compile(r'^#\s+(.+)', re.MULTILINE)


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


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """调用 LLM API，返回文本响应。"""
    url = f"{API_BASE}/chat/completions"
    payload = json.dumps({
        "model": API_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        url, data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        method="POST",
    )

    last_err = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                content = data["choices"][0]["message"]["content"]
                content = content.strip()
                if not content:
                    raise ValueError("LLM 返回空内容")
                return content
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, ValueError) as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_SLEEP)
    raise RuntimeError(f"LLM 调用失败 (重试 {MAX_RETRIES} 次): {last_err}")


def collect_children_info(dir_path: Path):
    """收集目录下所有子项的摘要信息 (用于 LLM 输入)。"""
    children = []
    for item in sorted(dir_path.iterdir()):
        if item.name in [".overview.md", ".abstract.md"]:
            continue
        if item.is_dir():
            sub_ov = item / ".overview.md"
            if sub_ov.exists():
                ov_content = read_text(sub_ov)
                h1 = H1_RE.search(ov_content)
                title = h1.group(1).strip() if h1 else item.name
                first_para = ""
                for line in ov_content.split("\n")[1:]:
                    line = line.strip()
                    if line and not line.startswith("#") and not line.startswith("```"):
                        first_para = line[:200]
                        break
                children.append({
                    "type": "dir",
                    "name": item.name,
                    "title": title,
                    "desc": first_para,
                })
            else:
                children.append({
                    "type": "dir",
                    "name": item.name,
                    "title": item.name,
                    "desc": "",
                })
        elif item.suffix == ".md":
            content = read_text(item)
            type_name = item.stem
            func_m = FUNC_DESC_RE.search(content)
            func_desc = func_m.group(1).strip()[:150] if func_m else ""
            h3_m = H3_RE.search(content, re.MULTILINE)
            first_method = h3_m.group(1).strip()[:80] if h3_m else ""
            children.append({
                "type": "file",
                "name": item.name,
                "title": type_name,
                "desc": func_desc,
                "method": first_method,
            })
    return children


def get_original_h1(ov_path: Path) -> str:
    """从现有 overview 提取原始 H1 标题。"""
    if not ov_path.exists():
        return ""
    content = read_text(ov_path)
    m = H1_RE.search(content)
    return m.group(1).strip() if m else ""


def get_module_intro(ov_path: Path) -> str:
    """从现有 overview 提取模块介绍段落 (H1 之后、第一个 ## 之前)。"""
    if not ov_path.exists():
        return ""
    content = read_text(ov_path)
    lines = content.split("\n")
    intro_lines = []
    found_h1 = False
    for line in lines:
        if line.startswith("# ") and not found_h1:
            found_h1 = True
            continue
        if found_h1:
            if line.startswith("## "):
                break
            if line.strip():
                intro_lines.append(line.strip())
    return "\n".join(intro_lines)[:500]


def build_system_prompt(level: str) -> str:
    return f"""你是一个鸿蒙 HarmonyOS 仓颉（Cangjie）开发文档的技术文档编辑。
你的任务是根据提供的目录结构和子项摘要信息，为「{level}」级别的目录生成一份高质量的中文 overview 文档。

输出要求：
1. 严格输出 markdown 格式（不要输出 ```markdown 代码块标记）
2. 第一行必须是 # 标题（使用原始模块的 H1 标题，如 ohos.ability（Ability））
3. 标题后写一段 4-6 句话的中文描述段落，基于子项内容重新概括该目录的能力范围、核心功能、适用场景和目标读者，不要直接照搬原始模块介绍
4. 然后是 ## 快速导航 章节，将子项按功能语义分组（如"核心能力"、"上下文管理"、"生命周期"等），每组列出相关文件并附带一句话描述
5. 如果子项数量较少（<=5个），可以不分组，直接列出
6. 导航项格式: - [文件名](./文件名) - 一句话描述
7. 不要输出"详细描述"章节，快速导航中每项的描述已经足够
8. 描述要具体、准确，基于提供的摘要信息，不要编造不存在的功能
9. 全部使用中文"""


def build_user_prompt(dir_path: Path, level: str, children: list) -> str:
    """构建 LLM 输入。"""
    rel = dir_path.name
    ov_path = dir_path / ".overview.md"
    original_h1 = get_original_h1(ov_path)
    module_intro = get_module_intro(ov_path)

    parts = [f"目录级别: {level}"]
    parts.append(f"目录名: {rel}")
    if original_h1:
        parts.append(f"原始H1标题（请保持此标题）: {original_h1}")
    if module_intro:
        parts.append(f"\n原始模块介绍（仅供参考，请重新概括不要照搬）:\n{module_intro}")

    parts.append(f"\n该目录包含 {len(children)} 个子项:\n")

    for child in children:
        if child["type"] == "dir":
            line = f"- [子目录] {child['name']}"
            if child.get("title"):
                line += f" (标题: {child['title']})"
            if child.get("desc"):
                line += f" | {child['desc']}"
        else:
            line = f"- {child['name']}"
            if child.get("desc"):
                line += f" → {child['desc']}"
            if child.get("method"):
                line += f" (含方法: {child['method']}...)"
        parts.append(line)

    parts.append("\n请生成该目录的中文 overview 文档。")
    return "\n".join(parts)


def extract_abstract(overview_content: str) -> str:
    """从 overview 内容提取第一段作为 abstract。"""
    lines = overview_content.split("\n")
    for line in lines[1:]:
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("```"):
            return line[:500]
    return ""


def enhance_one(dir_path: Path, cache_dir: Path, dry_run: bool = False):
    """增强单个目录的 overview。"""
    ov_path = dir_path / ".overview.md"
    if not ov_path.exists():
        return None

    rel = str(dir_path.relative_to(dir_path.parent.parent))
    depth = len(dir_path.relative_to(dir_path.parent.parent.parent).parts) if dir_path != dir_path.parent else 0

    staged_root = dir_path
    while staged_root.parent != staged_root and not (staged_root / ".preprocess-meta.json").exists():
        staged_root = staged_root.parent
        if staged_root == staged_root.parent:
            break

    rel_to_staged = str(dir_path.relative_to(staged_root)).replace("\\", "/") if dir_path != staged_root else "(root)"

    parts = dir_path.relative_to(staged_root).parts
    depth = len(parts) if parts else 0
    if depth == 0:
        level = "root"
    elif depth == 1:
        level = "kit"
    elif depth == 2:
        level = "split_dir"
    elif depth == 3 and dir_path.name.startswith("ohos"):
        level = "namespace"
    elif depth >= 4:
        level = "class"
    else:
        level = "other"

    children = collect_children_info(dir_path)
    if not children:
        return None

    system_prompt = build_system_prompt(level)
    user_prompt = build_user_prompt(dir_path, level, children)

    cache_key = sha8(f"{level}|{rel_to_staged}|{user_prompt}")
    cache_file = cache_dir / f"{cache_key}.json"

    if cache_file.exists():
        cached = json.loads(cache_file.read_text(encoding="utf-8"))
        cached_overview = cached.get("overview", "").strip()
        if cached_overview:
            overview_content = cached_overview
            source = "cache"
        else:
            cache_file.unlink(missing_ok=True)
            cached_overview = None
    else:
        cached_overview = None

    if cached_overview is None:
        if dry_run:
            return {
                "level": level,
                "path": rel_to_staged,
                "children": len(children),
                "input_chars": len(user_prompt),
                "status": "dry_run",
            }
        overview_content = call_llm(system_prompt, user_prompt)
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps({
            "overview": overview_content,
            "level": level,
            "path": rel_to_staged,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        source = "llm"

    write_text(ov_path, overview_content)

    abstract = extract_abstract(overview_content)
    if abstract:
        write_text(dir_path / ".abstract.md", abstract)

    return {
        "level": level,
        "path": rel_to_staged,
        "children": len(children),
        "input_chars": len(user_prompt),
        "output_chars": len(overview_content),
        "status": source,
    }


def main():
    parser = argparse.ArgumentParser(description="LLM 增强 overview 文件")
    parser.add_argument("--docs-dir", default=str(DEFAULT_DOCS_DIR))
    parser.add_argument("--target", default="", help="只增强指定子目录 (相对路径)")
    parser.add_argument("--dry-run", action="store_true", help="仅统计不调用 LLM")
    parser.add_argument("--concurrency", type=int, default=CONCURRENCY)
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir).resolve()
    if not docs_dir.exists():
        print(f"ERROR: 目录不存在: {docs_dir}")
        sys.exit(1)

    if not API_KEY and not args.dry_run:
        print("ERROR: 请设置 OPENAI_API_KEY 环境变量")
        sys.exit(1)

    cache_dir = docs_dir / ".llm-cache"

    if args.target:
        target_dir = docs_dir / args.target
        if not target_dir.exists():
            print(f"ERROR: 目标目录不存在: {target_dir}")
            sys.exit(1)
        target_dirs = sorted(d.parent for d in target_dir.rglob(".overview.md"))
        if (target_dir / ".overview.md").exists():
            target_dirs.append(target_dir)
        target_dirs = sorted(set(target_dirs))
    else:
        target_dirs = sorted(
            d.parent for d in docs_dir.rglob(".overview.md")
        )

    print(f"API: {API_BASE} / {API_MODEL}")
    print(f"文档目录: {docs_dir}")
    print(f"目标 overview 数: {len(target_dirs)}")
    print(f"缓存目录: {cache_dir}")
    print()

    if args.dry_run:
        print("=== DRY RUN (不调用 LLM) ===")
        results = []
        for d in target_dirs:
            r = enhance_one(d, cache_dir, dry_run=True)
            if r:
                results.append(r)
        print(f"需要增强: {len(results)} 个 overview")
        total_input = sum(r["input_chars"] for r in results)
        print(f"总输入字符: {total_input:,}")
        print(f"估算输入 token: {int(total_input/3):,}")
        return

    success = 0
    failed = 0
    cached = 0

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        future_map = {pool.submit(enhance_one, d, cache_dir): d for d in target_dirs}
        for i, future in enumerate(as_completed(future_map)):
            d = future_map[future]
            try:
                result = future.result()
                if result is None:
                    continue
                status = result["status"]
                if status == "cache":
                    cached += 1
                else:
                    success += 1
                tag = "CACHE" if status == "cache" else "LLM"
                print(f"  [{i+1}/{len(target_dirs)}] [{tag}] [{result['level']}] "
                      f"{result['path']} ({result['children']} 子项, "
                      f"输入 {result.get('input_chars', 0)} 字符, "
                      f"输出 {result.get('output_chars', 0)} 字符)")
            except Exception as e:
                failed += 1
                print(f"  [FAIL] {d}: {e}")

    print()
    print(f"=== 汇总 ===")
    print(f"  LLM 新生成: {success}")
    print(f"  缓存命中: {cached}")
    print(f"  失败: {failed}")
    print(f"  总计: {success + cached + failed}")


if __name__ == "__main__":
    main()
