#!/usr/bin/env python3
"""校验用户态评测集与当前文档/索引是否一致。

本模块是 fusion 分区发布流水线中的评测集健康检查组件，用于在发布前验证：
1. 评测集中的期望路径在当前索引中是否存在（missing_path / stale_path）
2. 查询是否包含内部术语（weak_user_query），偏离真实用户意图
3. must_contain 标记是否与期望路径内容一致
4. 是否有重复查询

被 run_release_eval.py 在每个评测集评测前调用，blocking 问题会阻塞发布。
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


# 内部术语标记：包含这些词的查询可能是从规则引擎内部结构生成的，
# 而非真实用户意图，需标记为 weak_user_query
INTERNAL_WORDS = ("doc/task", "expected_paths", "acceptable_paths", ".jsonl")
DIMENSIONS = ("source", "category", "capability", "query_style", "difficulty")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if line:
                row = json.loads(line)
                row["_line"] = line_no
                rows.append(row)
    return rows


def normalize_path(path: str) -> str:
    """路径归一化：统一斜杠方向、去除锚点/查询参数、去除 .md 后缀。
    归一化后便于跨系统路径比对。"""
    value = str(path or "").replace("\\", "/").strip().split("#", 1)[0].split("?", 1)[0].strip("/")
    if value.endswith(".md"):
        value = value[:-3]
    return value


def path_variants(path: str) -> set[str]:
    """生成路径变体集合：去除 .abstract/.overview/README 等特殊后缀，
    因为同一文档可能有多种路径表述。"""
    base = normalize_path(path)
    variants = {base}
    for suffix in ("/.abstract", "/.overview", "/README", "/index"):
        if base.endswith(suffix):
            variants.add(base[: -len(suffix)])
    return {item for item in variants if item}


def paths_match(left: str, right: str) -> bool:
    """宽松路径匹配：比较所有变体组合，允许父子路径包含关系。
    用于判定评测集期望路径是否在索引中有对应文档。"""
    for left_item in path_variants(left):
        for right_item in path_variants(right):
            if left_item == right_item:
                return True
            if left_item.startswith(f"{right_item}/") or right_item.startswith(f"{left_item}/"):
                return True
    return False


def collect_string_paths(value: Any, output: set[str]) -> None:
    """递归提取 JSON 结构中所有形似路径的字符串值（含 / 但非 URL），
    用于从索引 JSONL 中收集已知文档路径集合。"""
    if isinstance(value, str):
        if "/" in value and not value.startswith(("http://", "https://")):
            output.add(normalize_path(value))
        return
    if isinstance(value, list):
        for item in value:
            collect_string_paths(item, output)
        return
    if isinstance(value, dict):
        for item in value.values():
            collect_string_paths(item, output)


def add_context(context_by_path: dict[str, str], path: str, *parts: object) -> None:
    normalized = normalize_path(path)
    if not normalized:
        return
    text = " ".join(str(part) for part in parts if part)
    if text:
        context_by_path[normalized] = " ".join(
            dict.fromkeys(part for part in (context_by_path.get(normalized, ""), text) if part)
        )


def collect_path_context(value: Any, output: set[str], context_by_path: dict[str, str], row_text: str) -> None:
    if isinstance(value, str):
        if "/" in value and not value.startswith(("http://", "https://")):
            path = normalize_path(value)
            output.add(path)
            add_context(context_by_path, path, row_text)
        return
    if isinstance(value, list):
        for item in value:
            collect_path_context(item, output, context_by_path, row_text)
        return
    if isinstance(value, dict):
        for item in value.values():
            collect_path_context(item, output, context_by_path, row_text)


def row_context(row: dict) -> str:
    keys = ("title", "name", "summary", "text", "task_id", "api_id")
    return " ".join(str(row.get(key, "")) for key in keys if row.get(key))


def load_known_paths(index_dir: Path, manifest: dict) -> tuple[set[str], dict[str, str]]:
    """从索引目录和文档 manifest 中收集所有已知路径及其上下文文字，
    返回 (known_paths_set, path→context_text 映射)。
    上下文用于 must_contain 标记的可用性检查。"""
    known: set[str] = set()
    context_by_path: dict[str, str] = {}
    for row in manifest.get("files", []):
        path = normalize_path(row.get("path", ""))
        if path:
            known.add(path)
            add_context(context_by_path, path, row.get("title", ""))
    for filename in ("tasks.jsonl", "apis.jsonl", "examples.jsonl", "docs.jsonl"):
        path = index_dir / filename
        if not path.exists():
            continue
        for row in load_jsonl(path):
            row.pop("_line", None)
            collect_string_paths(row, known)
            collect_path_context(row, known, context_by_path, row_context(row))
    return known, context_by_path


def exists_in_known(path: str, known_paths: set[str]) -> bool:
    return any(paths_match(path, known) for known in known_paths)


def context_for_path(path: str, context_by_path: dict[str, str]) -> str:
    matches = [
        text
        for known, text in context_by_path.items()
        if text and paths_match(path, known)
    ]
    return " ".join(matches).lower()


def token_available_for_path(path: str, token: str, context_by_path: dict[str, str]) -> bool:
    return str(token).lower() in context_for_path(path, context_by_path)


def weak_user_query(query: str) -> bool:
    """检测查询是否包含内部术语或仓颉技术路径，偏离真实用户意图。
    包含 doc/task、expected_paths、harmonyos/std/stdx 等路径标记的查询
    可能是从内部规则生成而非真实用户搜索。"""
    lowered = query.lower()
    if any(word in lowered for word in INTERNAL_WORDS):
        return True
    return bool(re.search(r"(^|/)(harmonyos|std|stdx|tools|lang-features)(/|$)", lowered))


def summarize_dimensions(rows: list[dict]) -> dict:
    summary: dict[str, dict] = {}
    for dimension in DIMENSIONS:
        counts = Counter(str(row.get(dimension, "unknown")) for row in rows)
        summary[dimension] = dict(sorted(counts.items()))
    return summary


def validate(rows: list[dict], known_paths: set[str], context_by_path: dict[str, str]) -> dict:
    """校验评测集健康状态。检查项包括：
    - weak_user_query: 查询含内部术语
    - duplicate_query: 重复查询
    - missing_path: 所有期望路径均不在索引中（阻塞级）
    - stale_path: 部分期望路径不在索引中
    - must_contain_maybe_too_narrow: must_contain 标记与期望路径内容不一致

    返回 {"blocking": bool, "blocking_count": int, "issues": list}。
    missing_path 类型的问题会阻塞发布。"""
    duplicate_queries = [query for query, count in Counter(row.get("query", "") for row in rows).items() if count > 1]
    issues: list[dict] = []
    query_issue_counts: dict[str, int] = defaultdict(int)

    for row in rows:
        query = str(row.get("query", ""))
        acceptable = row.get("acceptable_paths", row.get("expected_paths", []))
        if weak_user_query(query):
            issues.append({"line": row["_line"], "query": query, "type": "weak_user_query"})
            query_issue_counts["weak_user_query"] += 1
        if query in duplicate_queries:
            issues.append({"line": row["_line"], "query": query, "type": "duplicate_query"})
            query_issue_counts["duplicate_query"] += 1
        if acceptable:
            missing = [path for path in acceptable if not exists_in_known(path, known_paths)]
            if missing:
                issue_type = "missing_path" if len(missing) == len(acceptable) else "stale_path"
                issues.append(
                    {
                        "line": row["_line"],
                        "query": query,
                        "type": issue_type,
                        "missing_paths": missing,
                    }
                )
                query_issue_counts[issue_type] += 1
        must_contain = [str(token) for token in row.get("must_contain", []) if str(token).strip()]
        if must_contain and acceptable:
            absent = [
                token
                for token in must_contain
                if not any(token_available_for_path(path, token, context_by_path) for path in acceptable)
            ]
            if absent:
                issues.append(
                    {
                        "line": row["_line"],
                        "query": query,
                        "type": "must_contain_maybe_too_narrow",
                        "tokens": absent,
                    }
                )
                query_issue_counts["must_contain_maybe_too_narrow"] += 1

    blocking = [issue for issue in issues if issue["type"] == "missing_path"]
    return {
        "count": len(rows),
        "blocking": bool(blocking),
        "blocking_count": len(blocking),
        "issue_counts": dict(sorted(query_issue_counts.items())),
        "coverage": summarize_dimensions(rows),
        "issues": issues[:200],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="校验用户态评测集健康状态")
    parser.add_argument("--eval-set", required=True)
    parser.add_argument("--index-dir", required=True)
    parser.add_argument("--doc-manifest", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = load_jsonl(Path(args.eval_set))
    known_paths, context_by_path = load_known_paths(Path(args.index_dir), load_json(Path(args.doc_manifest)))
    summary = validate(rows, known_paths, context_by_path)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("count", "blocking", "blocking_count", "issue_counts")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
