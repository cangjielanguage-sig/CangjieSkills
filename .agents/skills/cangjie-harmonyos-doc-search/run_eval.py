#!/usr/bin/env python3
"""评测脚本：对比 FTS5-only vs Hybrid (FTS5+sqlite-vec+RRF) 检索效果。"""

import json
import os
import sys
import time

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)

from build_index import fts5_search, hybrid_search

DB_PATH = os.path.join(_SCRIPT_DIR, "docs.db")
QUERIES_PATH = os.path.join(_SCRIPT_DIR, "eval_queries.jsonl")


def load_queries(path: str) -> list[dict]:
    queries = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                queries.append(json.loads(line))
    return queries


def eval_search(search_fn, queries: list[dict], limit: int = 15,
                label: str = "") -> dict:
    """运行评测，返回指标汇总。"""
    total = len(queries)
    recall_at_5 = 0
    recall_at_10 = 0
    mrr_sum = 0.0
    latencies = []
    per_category: dict[str, dict] = {}

    for q in queries:
        query = q["query"]
        expected = q["expected_paths"]
        category = q.get("category", "unknown")

        if category not in per_category:
            per_category[category] = {"total": 0, "r5": 0, "r10": 0, "mrr": 0.0}
        per_category[category]["total"] += 1

        t0 = time.perf_counter()
        results = search_fn(query, limit)
        elapsed_ms = (time.perf_counter() - t0) * 1000
        latencies.append(elapsed_ms)

        # 前缀匹配：expected 可能是目录前缀
        def matches(result_path, exp_path):
            return result_path == exp_path or result_path.startswith(exp_path + "/")

        # Recall@5: 前 5 个结果中命中任一期望路径
        hit_5 = any(
            matches(r, e) for r in results[:5] for e in expected
        )
        if hit_5:
            recall_at_5 += 1
            per_category[category]["r5"] += 1

        # Recall@10
        hit_10 = any(
            matches(r, e) for r in results[:10] for e in expected
        )
        if hit_10:
            recall_at_10 += 1
            per_category[category]["r10"] += 1

        # MRR: 第一个命中的排名倒数
        rr = 0.0
        for i, r in enumerate(results):
            if any(matches(r, e) for e in expected):
                rr = 1.0 / (i + 1)
                break
        mrr_sum += rr
        per_category[category]["mrr"] += rr

    latencies.sort()
    p50 = latencies[len(latencies) // 2] if latencies else 0
    p95 = latencies[int(len(latencies) * 0.95)] if latencies else 0

    return {
        "label": label,
        "total": total,
        "recall_at_5": recall_at_5 / total if total else 0,
        "recall_at_10": recall_at_10 / total if total else 0,
        "mrr": mrr_sum / total if total else 0,
        "latency_p50_ms": round(p50, 1),
        "latency_p95_ms": round(p95, 1),
        "per_category": {
            cat: {
                "total": v["total"],
                "recall_at_5": round(v["r5"] / v["total"], 3) if v["total"] else 0,
                "recall_at_10": round(v["r10"] / v["total"], 3) if v["total"] else 0,
                "mrr": round(v["mrr"] / v["total"], 3) if v["total"] else 0,
            }
            for cat, v in per_category.items()
        },
    }


def print_report(result: dict):
    print(f"\n{'=' * 60}")
    print(f"  {result['label']}  ({result['total']} queries)")
    print(f"{'=' * 60}")
    print(f"  Recall@5:  {result['recall_at_5']:.1%}")
    print(f"  Recall@10: {result['recall_at_10']:.1%}")
    print(f"  MRR:       {result['mrr']:.3f}")
    print(f"  Latency:   P50={result['latency_p50_ms']}ms  "
          f"P95={result['latency_p95_ms']}ms")
    print(f"\n  Per category:")
    for cat, v in sorted(result["per_category"].items()):
        print(f"    {cat:20s}  n={v['total']:2d}  "
              f"R@5={v['recall_at_5']:.1%}  R@10={v['recall_at_10']:.1%}  "
              f"MRR={v['mrr']:.3f}")


def main():
    if not os.path.exists(DB_PATH):
        print(f"数据库不存在: {DB_PATH}", file=sys.stderr)
        print("请先运行: python build_index.py build --with-vec", file=sys.stderr)
        sys.exit(1)

    queries = load_queries(QUERIES_PATH)
    print(f"加载 {len(queries)} 个评测查询", file=sys.stderr)

    # FTS5-only
    def fts5_fn(query, limit):
        return fts5_search(DB_PATH, query, limit=limit)

    # Hybrid (FTS5 + sqlite-vec + RRF)
    def hybrid_fn(query, limit):
        return hybrid_search(DB_PATH, query, limit=limit)

    print("\n运行 FTS5-only 评测...", file=sys.stderr)
    r_fts5 = eval_search(fts5_fn, queries, label="FTS5-only (BM25)")
    print_report(r_fts5)

    print("\n运行 Hybrid 评测...", file=sys.stderr)
    r_hybrid = eval_search(hybrid_fn, queries, label="Hybrid (FTS5 + sqlite-vec + RRF)")
    print_report(r_hybrid)

    # Delta
    print(f"\n{'=' * 60}")
    print(f"  Delta (Hybrid - FTS5)")
    print(f"{'=' * 60}")
    dr5 = r_hybrid["recall_at_5"] - r_fts5["recall_at_5"]
    dr10 = r_hybrid["recall_at_10"] - r_fts5["recall_at_10"]
    dmrr = r_hybrid["mrr"] - r_fts5["mrr"]
    print(f"  Recall@5:  {dr5:+.1%}")
    print(f"  Recall@10: {dr10:+.1%}")
    print(f"  MRR:       {dmrr:+.3f}")


if __name__ == "__main__":
    main()
