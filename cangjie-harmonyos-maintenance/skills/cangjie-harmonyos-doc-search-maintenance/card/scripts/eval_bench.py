#!/usr/bin/env python3
"""文档检索评测脚本，支持 V3 本地索引和 OpenViking 远端对照组。

本模块是 card 分区评测基础设施，提供：
- load_eval_set: 加载 JSONL 评测集
- run_benchmark: 通用评测循环（recall@5/10, MRR, 延迟分位数）
- make_v3_search / make_openviking_search: 搜索函数工厂

被 run_maintenance.py 和 run_v3_regression_gate.py 调用。
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
SKILL_DIR = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = SKILL_DIR / "doc-card"
EVALS_DIR = DOC_CARD_DIR / "evals"
REMOTE_BACKENDS = ["cangjie-1.0.5", "harmonyos-6.0.2-15k"]


def load_eval_set(path: str) -> list[dict]:
    items = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def _match(result: str, expected: str) -> bool:
    """宽松路径匹配：先比较精确值，再按 # 前缀截断做子串包含匹配。
    用于应对返回路径含锚点（#section）但期望路径不含的情况。"""
    if result == expected:
        return True
    r = result.split("#")[0]
    e = expected.split("#")[0]
    return r.startswith(e) or e.startswith(r)


def recall_at_k(results: list[str], expected: list[str], k: int) -> float:
    top_k = results[:k]
    hits = sum(1 for item in expected if any(_match(result, item) for result in top_k))
    return hits / len(expected) if expected else 0.0


def mrr(results: list[str], expected: list[str]) -> float:
    for index, result in enumerate(results):
        if any(_match(result, item) for item in expected):
            return 1.0 / (index + 1)
    return 0.0


def run_benchmark(
    search_fn: Callable[[str, int], list[str]],
    eval_set: list[dict],
    limit: int = 10,
) -> dict:
    """评测循环：对每条评测查询调用 search_fn，计算 recall@5/10、MRR、延迟分位数。

    参数 search_fn: (query, limit) -> list[str]，返回路径列表。
    返回 {"summary": {overall, 按类别}, "details": 逐条结果}。
    """
    results_by_cat: dict[str, list[dict]] = {}
    all_results: list[dict] = []

    for item in eval_set:
        query = item["query"]
        expected = item["expected_paths"]
        category = item.get("category", "unknown")

        t0 = time.perf_counter()
        try:
            paths = search_fn(query, limit)
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR on '{query}': {exc}", file=sys.stderr)
            paths = []
        elapsed_ms = (time.perf_counter() - t0) * 1000

        row = {
            "query": query,
            "category": category,
            "expected": expected,
            "returned": paths[:limit],
            "recall_5": recall_at_k(paths, expected, 5),
            "recall_10": recall_at_k(paths, expected, 10),
            "mrr": mrr(paths, expected),
            "latency_ms": elapsed_ms,
        }
        all_results.append(row)
        results_by_cat.setdefault(category, []).append(row)

    def aggregate(rows: list[dict]) -> dict:
        """聚合指标计算：均值 recall/MRR + 延迟 p50/p95/p99 分位数。"""
        latencies = sorted(row["latency_ms"] for row in rows) if rows else [0.0]
        p95_index = min(len(latencies) - 1, int(len(latencies) * 0.95))
        p99_index = min(len(latencies) - 1, int(len(latencies) * 0.99))
        return {
            "count": len(rows),
            "recall@5": round(statistics.mean(row["recall_5"] for row in rows), 4) if rows else 0.0,
            "recall@10": round(statistics.mean(row["recall_10"] for row in rows), 4) if rows else 0.0,
            "mrr": round(statistics.mean(row["mrr"] for row in rows), 4) if rows else 0.0,
            "latency_p50_ms": round(statistics.median(latencies), 1),
            "latency_p95_ms": round(latencies[p95_index], 1),
            "latency_p99_ms": round(latencies[p99_index], 1),
        }

    summary = {"overall": aggregate(all_results)}
    for category in sorted(results_by_cat):
        summary[category] = aggregate(results_by_cat[category])
    return {"summary": summary, "details": all_results}


def _strip_viking(uri: str) -> str:
    """剥离 viking://resources/ 前缀，只保留相对路径"""
    tag = "resources/"
    pos = uri.find(tag)
    return uri[pos + len(tag):] if pos != -1 else uri


def make_openviking_search(host: str, port: int):
    """创建 OpenViking 远端搜索函数工厂。返回闭包 (query, limit) -> paths。
    远端接口返回 viking://resources/ 格式的 URI，需 _strip_viking 转为相对路径。"""
    base_url = f"http://{host}:{port}/api/v1/search"

    def fn(query: str, limit: int) -> list[str]:
        payload = json.dumps({
            "query": query,
            "limit": limit,
            "backends": REMOTE_BACKENDS,
        }).encode()
        req = urllib.request.Request(
            base_url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            print(f"  OpenViking 请求失败: {exc}", file=sys.stderr)
            return []
        if data.get("status") != "ok":
            print(f"  OpenViking 服务端错误: {data.get('error', '未知')}", file=sys.stderr)
            return []
        return [_strip_viking(r["uri"]) for r in data.get("results", [])]

    return fn


def make_v3_search(index_dir: str, mode: str = "auto"):
    """创建 V3 本地搜索函数工厂。动态导入 search_v3 避免硬依赖，
    加载索引后返回闭包函数 (query, limit) -> paths。"""
    sys.path.insert(0, str(DOC_CARD_DIR))
    from search_v3 import collect, load_index

    index = load_index(Path(index_dir))

    def fn(query: str, limit: int) -> list[str]:
        return collect(index, query, mode, limit)["paths"]

    return fn


def print_summary(result: dict) -> None:
    for section, metrics in result["summary"].items():
        print(f"[{section}]")
        for key, value in metrics.items():
            print(f"  {key}: {value}")
        print()

    misses = [row for row in result["details"] if row["mrr"] == 0]
    if misses:
        print(f"--- 完全未命中 ({len(misses)} 条) ---")
        for miss in misses:
            print(f"  [{miss['category']}] {miss['query']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="文档检索评测")
    parser.add_argument("--eval-set", default=str(EVALS_DIR / "eval_queries.jsonl"))
    parser.add_argument("--backend", choices=["v3", "openviking"], default="v3")
    parser.add_argument("--host", default="111.229.30.227")
    parser.add_argument("--port", type=int, default=2026)
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"), help="V3 索引目录")
    parser.add_argument("--mode", choices=["auto", "task", "api", "example", "doc"], default="auto", help="V3 查询模式")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--output", default="", help="结果输出 JSON 路径")
    args = parser.parse_args()

    eval_set = load_eval_set(args.eval_set)
    print(f"加载 {len(eval_set)} 条评测查询")

    if args.backend == "openviking":
        search_fn = make_openviking_search(args.host, args.port)
        print(f"使用 OpenViking 后端: {args.host}:{args.port}")
    else:
        search_fn = make_v3_search(args.index_dir, args.mode)
        print(f"使用 V3 后端: {args.index_dir} (mode={args.mode})")

    print(f"开始评测 (limit={args.limit})...\n")
    result = run_benchmark(search_fn, eval_set, limit=args.limit)
    print_summary(result)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
        print(f"\n详细结果已写入: {args.output}")


if __name__ == "__main__":
    main()
