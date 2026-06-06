#!/usr/bin/env python3
"""V3 / graphify / fusion 独立 AB 评测（fusion 分区版本）。

本模块是 fusion 分区维护流水线中的语义能力评测组件，与 card 分区的
run_ab_eval.py 功能一致，但评测集默认路径指向 fusion/evals 目录。

被 run_maintenance.py 的 fusion_ab_gate 调用，产物为 JSON 报告。
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
FUSION_DIR = SCRIPT_DIR.parent
MAINTENANCE_DIR = FUSION_DIR.parent
DOC_SEARCH_DIR = MAINTENANCE_DIR.parent / "cangjie-hmos-doc-search"
DOC_CARD_DIR = DOC_SEARCH_DIR / "doc-card"
DOC_GRAPH_DIR = DOC_SEARCH_DIR / "doc-graph"
DEFAULT_EVAL_DIR = FUSION_DIR / "evals"


def _import_module(name: str, path: Path):
    """跨分区动态导入模块：将 doc-card/search_v3.py 和 doc-graph/query.py
    按文件路径加载，避免对 cangjie-hmos-doc-search 产生硬依赖。"""
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# 跨分区依赖：V3 索引来自 doc-card，图谱搜索来自 doc-graph
search_v3 = _import_module("search_v3_eval", DOC_CARD_DIR / "search_v3.py")
graph_query = _import_module("graph_query_eval", DOC_GRAPH_DIR / "query.py")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no} 不是合法 JSONL: {exc}") from exc
    return rows


def norm_path(path: str) -> str:
    """路径归一化：统一斜杠方向、去除顶层 docs 前缀，便于跨引擎命中判定。"""
    normalized = path.replace("\\", "/").lower().rstrip("/")
    # 文档语料库顶层目录名会随版本变化，此处硬编码 6.0.2-15k 前缀剥离
    for prefix in ("harmonyos-6.0.2-15k/", "docs/harmonyos-6.0.2-15k/"):
        if normalized.startswith(prefix):
            return normalized[len(prefix):]
    return normalized


def path_hit(paths: list[str], acceptable_paths: list[str]) -> bool:
    """判定返回路径是否命中期望路径。采用子串包含而非精确匹配，
    因为 V3 和 graphify 的路径粒度可能不同。"""
    got = [norm_path(p) for p in paths]
    expected = [norm_path(p) for p in acceptable_paths]
    for path in got:
        if any(exp in path or path in exp for exp in expected):
            return True
    return False


def cluster_hit(paths: list[str], clusters: list[str]) -> dict[str, bool]:
    """概念聚类命中检测：aliases 将同一概念的不同表述映射到统一 cluster 名，
    用于 composition 评测集的多维度召回评估。"""
    joined = "\n".join(norm_path(p) for p in paths)
    aliases = {
        "state_management": ["state", "ui-state", "appstorage", "localstorage"],
        "jsbridge": ["javascriptproxy", "webview", "arkweb"],
        "http": ["http", "networkkit", "net-http"],
        "list": ["list", "lazyforeach"],
        "refresh": ["refresh"],
        "webview": ["webview", "arkweb"],
        "toast": ["promptaction", "toast"],
        "timer": ["time", "timer"],
        "rdb_store": ["relationalstore", "rdb"],
        "photo_picker": ["picker", "photo"],
        "request_upload": ["request", "upload"],
    }
    result: dict[str, bool] = {}
    for cluster in clusters:
        keys = aliases.get(cluster, [cluster.replace("_", "-"), cluster.replace("_", "")])
        result[cluster] = any(key.lower() in joined for key in keys)
    return result


def run_v3(index: dict[str, Any], query: str, limit: int) -> dict[str, Any]:
    """调用 V3 规则索引搜索。mode="auto" 让引擎自动选择卡片类型。"""
    result = search_v3.collect(index, query, "auto", limit)
    return {"paths": [str(p) for p in result.get("paths", [])[:limit]], "raw": result}


def run_graphify(session: Any, query: str, limit: int) -> dict[str, Any]:
    """调用 graphify 知识图谱搜索。graph="doc" 指定使用文档子图。"""
    result = session.search(query, top_k=limit, graph="doc")
    paths = [str(p) for p in result.paths[:limit]]
    return {"paths": paths, "raw": {"graph_used": result.graph_used, "nodes": [getattr(n, "label", "") for n in result.nodes[:limit]]}}


def run_fusion(index: dict[str, Any], session: Any, query: str, limit: int) -> dict[str, Any]:
    """融合搜索：先分别跑 V3 和 graphify，再去重合并结果列表。
    简单去重合并策略——V3 结果优先排列，图谱结果补充 V3 未覆盖的路径。"""
    v3 = run_v3(index, query, limit)
    graph = run_graphify(session, query, limit)
    paths: list[str] = []
    for path in v3["paths"] + graph["paths"]:
        if path not in paths:
            paths.append(path)
    return {"paths": paths, "raw": {"v3": v3["raw"], "graphify": graph["raw"]}}


def evaluate_rows(rows: list[dict[str, Any]], engine_name: str, run_one, limit: int) -> dict[str, Any]:
    """对评测集逐条运行搜索并计算指标。

    返回指标包括：
    - recall_at_k: 基础命中率
    - paraphrase_variance: 同意图不同表述的命中方差，衡量语义稳定性
    - composition_recall_at_concept: 多概念组合查询的维度召回率
    """
    cases = []
    intent_scores: dict[str, list[int]] = defaultdict(list)
    composition_scores: list[float] = []
    for row in rows:
        query = row["query"]
        out = run_one(query)
        paths = out["paths"]
        hit = path_hit(paths, row.get("acceptable_paths", []))
        case = {
            "query": query,
            "hit": hit,
            "top_paths": paths[:limit],
            "acceptable_paths": row.get("acceptable_paths", []),
        }
        if row.get("intent_id"):
            intent_scores[row["intent_id"]].append(1 if hit else 0)
        if row.get("expected_concept_clusters"):
            cluster_hits = cluster_hit(paths, row["expected_concept_clusters"])
            recall = sum(cluster_hits.values()) / len(cluster_hits) if cluster_hits else 0.0
            composition_scores.append(recall)
            case["cluster_hits"] = cluster_hits
            case["composition_recall"] = round(recall, 3)
        cases.append(case)

    total = len(cases)
    hits = sum(1 for c in cases if c["hit"])
    paraphrase_variance = {
        intent: round(statistics.pvariance(values), 4) if len(values) > 1 else 0.0
        for intent, values in intent_scores.items()
    }
    return {
        "engine": engine_name,
        "total": total,
        "hits": hits,
        "recall_at_k": round(hits / total, 4) if total else 0.0,
        "paraphrase_variance_avg": round(sum(paraphrase_variance.values()) / len(paraphrase_variance), 4) if paraphrase_variance else None,
        "paraphrase_variance_by_intent": paraphrase_variance,
        "composition_recall_at_concept": round(sum(composition_scores) / len(composition_scores), 4) if composition_scores else None,
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="运行 V3 / graphify / fusion AB 评测")
    parser.add_argument("--eval-dir", default=str(DEFAULT_EVAL_DIR))
    parser.add_argument("--splits", default="real_session,paraphrase,composition")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"))
    parser.add_argument("--graph-dir", default=str(DOC_GRAPH_DIR / "data"))
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    eval_dir = Path(args.eval_dir)
    split_files = {
        "real_session": eval_dir / "eval_queries_real_session.jsonl",
        "paraphrase": eval_dir / "eval_queries_paraphrase.jsonl",
        "composition": eval_dir / "eval_queries_composition.jsonl",
    }
    selected = [s.strip() for s in args.splits.split(",") if s.strip()]

    index = search_v3.load_index(Path(args.index_dir))
    session = graph_query.create_session(graph_dir=args.graph_dir)

    report: dict[str, Any] = {"limit": args.limit, "splits": {}}
    for split in selected:
        rows = load_jsonl(split_files[split])
        report["splits"][split] = {
            "v3": evaluate_rows(rows, "v3", lambda q: run_v3(index, q, args.limit), args.limit),
            "graphify": evaluate_rows(rows, "graphify", lambda q: run_graphify(session, q, args.limit), args.limit),
            "fusion": evaluate_rows(rows, "fusion", lambda q: run_fusion(index, session, q, args.limit), args.limit),
        }

    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
