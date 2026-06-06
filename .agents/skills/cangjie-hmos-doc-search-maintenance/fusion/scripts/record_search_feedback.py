#!/usr/bin/env python3
"""把真实搜索反馈登记为候选失败 query。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def latest_event(rows: list[dict], query: str) -> dict:
    for row in reversed(rows):
        if row.get("query") == query:
            return row
    return {}


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="登记真实搜索失败反馈")
    parser.add_argument("--log", required=True, help="search_v3.py 生成的搜索事件 JSONL")
    parser.add_argument("--query", required=True, help="被反馈的原始 query")
    parser.add_argument("--out", required=True, help="失败反馈输出 JSONL")
    parser.add_argument("--reason", default="top5_not_helpful", help="失败原因")
    parser.add_argument("--expected-intent", default="", help="可选：期望意图描述")
    args = parser.parse_args()

    event = latest_event(load_jsonl(Path(args.log)), args.query)
    row = {
        "query": args.query,
        "reason": args.reason,
        "expected_intent": args.expected_intent,
        "observed_top_paths": event.get("top_paths", []),
        "observed_top_titles": event.get("top_titles", []),
        "source": "real-feedback",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    append_jsonl(Path(args.out), row)
    print(json.dumps(row, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
