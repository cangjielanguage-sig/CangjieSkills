#!/usr/bin/env python3
"""按用户态评测维度汇总失败原因。"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


DIMENSIONS = ("source", "category", "capability", "query_style", "difficulty")


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def summarize(rows: list[dict], k: int) -> dict:
    b_rows = [row for row in rows if row.get("group") == "B"]
    metric = f"success@{k}"
    failures = [row for row in b_rows if not row.get(metric)]
    summary: dict[str, object] = {
        "count": len(b_rows),
        metric: round(1.0 - (len(failures) / len(b_rows)), 4) if b_rows else 0.0,
        "failures": len(failures),
        "failed_reason": dict(Counter(row.get("failed_reason") or f"hit_below_{k}" for row in failures)),
    }
    for dimension in DIMENSIONS:
        groups: dict[str, list[dict]] = defaultdict(list)
        for row in b_rows:
            groups[str(row.get(dimension, "unknown"))].append(row)
        summary[f"by_{dimension}"] = {
            key: {
                "count": len(items),
                metric: round(sum(1 for item in items if item.get(metric)) / len(items), 4),
                "failures": sum(1 for item in items if not item.get(metric)),
            }
            for key, items in sorted(groups.items())
        }
    summary["top_failures"] = [
        {
            "query": row.get("query"),
            "source": row.get("source"),
            "category": row.get("category"),
            "capability": row.get("capability"),
            "query_style": row.get("query_style"),
            "difficulty": row.get("difficulty"),
            "failed_reason": row.get("failed_reason") or f"hit_below_{k}",
            "hit_rank": row.get("hit_rank"),
            "returned_top5": row.get("returned", [])[:5],
            "acceptable_paths": row.get("acceptable_paths", []),
        }
        for row in failures[:50]
    ]
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="分析用户态评测失败分布")
    parser.add_argument("details_jsonl", help="ab_test_openviking_vs_v3.py 生成的 details.jsonl")
    parser.add_argument("--k", type=int, default=5, choices=(1, 5, 10))
    parser.add_argument("--output", default="", help="可选：写入 summary JSON")
    args = parser.parse_args()

    summary = summarize(load_jsonl(Path(args.details_jsonl)), args.k)
    text = json.dumps(summary, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
