#!/usr/bin/env python3
"""分析本地搜索事件日志，并生成真实 query 候选集。"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    if not path or not path.exists():
        return []
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def candidate_rows(events: list[dict], feedback: list[dict], limit: int) -> list[dict]:
    by_query: dict[str, dict] = {}
    for row in events:
        query = str(row.get("query", "")).strip()
        if not query:
            continue
        current = by_query.setdefault(
            query,
            {
                "query": query,
                "count": 0,
                "last_top_paths": [],
                "last_top_titles": [],
                "has_error": False,
                "zero_result": False,
            },
        )
        current["count"] += 1
        current["last_top_paths"] = row.get("top_paths", [])
        current["last_top_titles"] = row.get("top_titles", [])
        current["has_error"] = current["has_error"] or bool(row.get("error"))
        current["zero_result"] = current["zero_result"] or not row.get("result_count")

    for row in feedback:
        query = str(row.get("query", "")).strip()
        if not query:
            continue
        current = by_query.setdefault(
            query,
            {
                "query": query,
                "count": 0,
                "last_top_paths": row.get("observed_top_paths", []),
                "last_top_titles": row.get("observed_top_titles", []),
                "has_error": False,
                "zero_result": False,
            },
        )
        current["feedback_reason"] = row.get("reason", "real-feedback")
        current["expected_intent"] = row.get("expected_intent", "")

    picked = sorted(
        by_query.values(),
        key=lambda item: (
            0 if item.get("feedback_reason") else 1,
            0 if item.get("zero_result") else 1,
            -int(item.get("count", 0)),
            item["query"],
        ),
    )[:limit]
    rows: list[dict] = []
    for item in picked:
        rows.append(
            {
                "query": item["query"],
                "intent": item.get("expected_intent", ""),
                "category": "real_feedback" if item.get("feedback_reason") else "real_usage",
                "capability": "unknown",
                "query_style": "real",
                "difficulty": "unknown",
                "acceptable_paths": [],
                "must_contain": [],
                "source": "search-log-candidate",
                "observed_top_paths": item.get("last_top_paths", []),
                "observed_top_titles": item.get("last_top_titles", []),
                "feedback_reason": item.get("feedback_reason", ""),
                "observed_count": item.get("count", 0),
            }
        )
    return rows


def summarize(events: list[dict], feedback: list[dict], candidate_limit: int) -> dict:
    query_counts = Counter(str(row.get("query", "")) for row in events if row.get("query"))
    candidate_queries = set(query_counts)
    candidate_queries.update(str(row.get("query", "")).strip() for row in feedback if row.get("query"))
    zero_results = [row for row in events if not row.get("result_count")]
    errors = [row for row in events if row.get("error")]
    return {
        "events": len(events),
        "unique_queries": len(query_counts),
        "zero_result_events": len(zero_results),
        "error_events": len(errors),
        "feedback_rows": len(feedback),
        "top_queries": query_counts.most_common(30),
        "zero_result_queries": Counter(row.get("query", "") for row in zero_results).most_common(30),
        "error_queries": Counter(row.get("query", "") for row in errors).most_common(30),
        "feedback_reasons": Counter(row.get("reason", "unknown") for row in feedback).most_common(),
        "candidate_count": min(candidate_limit, len(candidate_queries)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="分析搜索日志并生成候选评测 query")
    parser.add_argument("--log", required=True, help="search_v3.py 生成的搜索事件 JSONL")
    parser.add_argument("--feedback", default="", help="record_search_feedback.py 生成的反馈 JSONL")
    parser.add_argument("--output-dir", required=True, help="输出目录")
    parser.add_argument("--candidate-limit", type=int, default=100)
    args = parser.parse_args()

    events = load_jsonl(Path(args.log))
    feedback = load_jsonl(Path(args.feedback)) if args.feedback else []
    output_dir = Path(args.output_dir)
    write_json(output_dir / "search-log-summary.json", summarize(events, feedback, args.candidate_limit))
    write_jsonl(
        output_dir / "eval_candidates_from_logs.jsonl",
        candidate_rows(events, feedback, args.candidate_limit),
    )
    print(f"wrote {output_dir}")


if __name__ == "__main__":
    main()
