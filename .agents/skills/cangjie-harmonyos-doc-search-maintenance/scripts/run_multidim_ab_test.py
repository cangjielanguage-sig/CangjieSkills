#!/usr/bin/env python3
"""多维AB评测：合并所有评测集（去重）并按维度分析。"""

import json
import hashlib
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
SKILL_DIR = SKILLS_DIR / "cangjie-harmonyos-doc-search"
EVALS_DIR = SKILL_DIR / "evals"
OUTPUT_DIR = SCRIPT_DIR / "ab-results-multidim"


def load_eval_set(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def get_query_hash(row: dict) -> str:
    """基于query和路径生成去重hash。"""
    paths = row.get("acceptable_paths") or row.get("expected_paths", [])
    key = row.get("query", "") + str(paths)
    return hashlib.md5(key.encode()).hexdigest()


def normalize_eval_row(row: dict) -> dict:
    """统一评测数据格式：将expected_paths转换为acceptable_paths。"""
    if "expected_paths" in row and "acceptable_paths" not in row:
        row["acceptable_paths"] = row.pop("expected_paths")
    return row


def merge_and_dedup() -> list[dict]:
    """合并所有评测集并去重。"""
    eval_files = [
        "eval_queries.jsonl",
        "eval_queries_user.jsonl",
        "eval_queries_user_appdev.jsonl",
        "eval_queries_user_appdev_batch2.jsonl",
        "eval_queries_user_appdev_batch3.jsonl",
        "eval_queries_user_appdev_next.jsonl",
        "eval_queries_user_appdev_frozen.jsonl",
        "eval_queries_user_appdev_blind.jsonl",
        "eval_queries_user_appdev_blind_20260424.jsonl",
        "eval_queries_app_agent_dev.jsonl",
        "eval_queries_sampled.jsonl",
    ]

    seen = set()
    merged = []

    for filename in eval_files:
        path = EVALS_DIR / filename
        if not path.exists():
            print(f"警告: {filename} 不存在，跳过")
            continue

        rows = load_eval_set(path)
        for row in rows:
            row = normalize_eval_row(row)
            h = get_query_hash(row)
            if h not in seen:
                seen.add(h)
                # 记录来源
                row["_source_file"] = filename
                merged.append(row)

    return merged


def analyze_dimensions(rows: list[dict]) -> dict:
    """按多维度统计。"""
    stats = {
        "total": len(rows),
        "by_category": defaultdict(int),
        "by_capability": defaultdict(int),
        "by_query_style": defaultdict(int),
        "by_difficulty": defaultdict(int),
        "by_source": defaultdict(int),
    }

    for row in rows:
        stats["by_category"][row.get("category", "unknown")] += 1
        stats["by_capability"][row.get("capability", "unknown")] += 1
        stats["by_query_style"][row.get("query_style", "unknown")] += 1
        stats["by_difficulty"][row.get("difficulty", "unknown")] += 1
        stats["by_source"][row.get("_source_file", "unknown")] += 1

    return stats


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("合并评测集并去重...")
    merged = merge_and_dedup()
    print(f"去重后共 {len(merged)} 条")

    # 保存合并后的评测集
    merged_path = OUTPUT_DIR / "eval_queries_merged.jsonl"
    with merged_path.open("w", encoding="utf-8") as f:
        for row in merged:
            # 移除临时字段
            row.pop("_source_file", None)
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"已保存: {merged_path}")

    # 分析维度
    stats = analyze_dimensions(merged)
    stats_path = OUTPUT_DIR / "dimension_stats.json"
    with stats_path.open("w", encoding="utf-8") as f:
        # 转换defaultdict为普通dict
        stats_json = {
            "total": stats["total"],
            "by_category": dict(stats["by_category"]),
            "by_capability": dict(stats["by_capability"]),
            "by_query_style": dict(stats["by_query_style"]),
            "by_difficulty": dict(stats["by_difficulty"]),
            "by_source": dict(stats["by_source"]),
        }
        json.dump(stats_json, f, ensure_ascii=False, indent=2)
    print(f"维度统计: {stats_path}")

    # 打印摘要
    print("\n=== 维度分布 ===")
    print(f"\n总计: {stats['total']} 条\n")

    print("按 category:")
    for k, v in sorted(stats["by_category"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n按 capability:")
    for k, v in sorted(stats["by_capability"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n按 query_style:")
    for k, v in sorted(stats["by_query_style"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n按 difficulty:")
    for k, v in sorted(stats["by_difficulty"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
