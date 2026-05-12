#!/usr/bin/env python3
"""校验用户态评测集与当前文档/索引是否一致。"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


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
    value = str(path or "").replace("\\", "/").strip().split("#", 1)[0].split("?", 1)[0].strip("/")
    if value.endswith(".md"):
        value = value[:-3]
    return value


def path_variants(path: str) -> set[str]:
    base = normalize_path(path)
    variants = {base}
    for suffix in ("/.abstract", "/.overview", "/README", "/index"):
        if base.endswith(suffix):
            variants.add(base[: -len(suffix)])
    return {item for item in variants if item}


def paths_match(left: str, right: str) -> bool:
    for left_item in path_variants(left):
        for right_item in path_variants(right):
            if left_item == right_item:
                return True
            if left_item.startswith(f"{right_item}/") or right_item.startswith(f"{left_item}/"):
                return True
    return False


def collect_string_paths(value: Any, output: set[str]) -> None:
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
