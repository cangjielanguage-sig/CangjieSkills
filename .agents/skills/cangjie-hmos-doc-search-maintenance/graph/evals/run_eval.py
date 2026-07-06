"""三引擎搜索对比评测 — card / graph / fusion。

本模块是 graph 分区评测的核心实现，对同一评测集分别运行三种引擎：
- card: 调用 V3 search_cards（纯规则搜索，跳过 understanding）
- graph: 调用 graphify 的 session.search（知识图谱搜索）
- fusion: 通过 unified_search.fuse_results 组合两者结果

评测指标：FULL/PARTIAL/MISS 命中率、MRR、延迟分位数、类别召回对比。
输出 Markdown 报告（含 MISS 查询对比和 fusion 补救命中分析）。

被 graph/scripts/run_graph_release_eval.py 透传调用。
"""

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

MAINTENANCE_DIR = Path(__file__).resolve().parent.parent.parent
DOC_SEARCH_DIR = MAINTENANCE_DIR.parent / "cangjie-hmos-doc-search"
EVAL_DIR = Path(__file__).resolve().parent

CARD_DIR = DOC_SEARCH_DIR / "doc-card"
GRAPH_DIR = DOC_SEARCH_DIR / "doc-graph"

# 跨分区依赖：unified_search（融合搜索）来自 doc-search，
# search_v3 来自 doc-card，query（图谱搜索）来自 doc-graph
sys.path.insert(0, str(DOC_SEARCH_DIR))
from unified_search import (
    fuse_results, extract_card_paths, Hit, SearchResult,
    _strip_top_dir, _ensure_top_dir,
)

sys.path.insert(0, str(GRAPH_DIR))
from query import create_session

sys.path.insert(0, str(CARD_DIR))
from search_v3 import load_index, search_cards, collect, collect_paths, hits_to_grouped, MODE_TYPES, TYPE_ID_KEY

KEYWORDS_PATH = EVAL_DIR / "keywords_v7_prompt.json"
DATASET_PATH = EVAL_DIR / "datasets" / "eval_queries_comprehensive_deduped.jsonl"
DEFAULT_REPORT = EVAL_DIR / "comparison_report.md"

CARD_INDEX_DIR = CARD_DIR / "index"
GRAPH_DATA_DIR = GRAPH_DIR / "data" / "doc"
GRAPH_PATH = GRAPH_DATA_DIR / "graph.json"


def load_keywords(path=None):
    with open(path or KEYWORDS_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_queries(path=None):
    queries = []
    with open(path or DATASET_PATH, encoding="utf-8") as f:
        for line in f:
            queries.append(json.loads(line))
    return queries


def norm(p):
    """路径归一化：剥离顶层目录并统一为相对路径格式。"""
    return _strip_top_dir(p).replace("\\", "/").strip("/")


def check_hit(direct_paths, related_paths, acceptable):
    """三级命中判定：FULL（直接命中）、PARTIAL（关联命中）、MISS（未命中）。
    采用子串包含匹配 + 目录级匹配，适应不同引擎的路径粒度差异。
    Card 返回 .overview.md、eval 期望 list_2more.md → 同目录内即可命中。
    """
    acceptable_n = [norm(p) for p in acceptable]
    direct_n = [norm(p) for p in direct_paths]
    related_n = [norm(p) for p in related_paths]

    def match(rp, aps):
        for ap in aps:
            if rp == ap or ap in rp or rp in ap:
                return True
            rp_dir = "/".join(rp.split("/")[:-1])
            ap_dir = "/".join(ap.split("/")[:-1])
            if rp_dir and ap_dir and rp_dir == ap_dir:
                return True
        return False

    if any(match(rp, acceptable_n) for rp in direct_n):
        return "FULL"
    if any(match(rp, acceptable_n) for rp in related_n):
        return "PARTIAL"
    return "MISS"


def compute_mrr(direct_paths, related_paths, acceptable):
    acceptable_n = [norm(p) for p in acceptable]
    all_paths = list(direct_paths) + list(related_paths)
    for i, p in enumerate(all_paths):
        rp = norm(p)
        for ap in acceptable_n:
            if rp == ap or ap in rp or rp in ap:
                return 1.0 / (i + 1)
            rp_dir = "/".join(rp.split("/")[:-1])
            ap_dir = "/".join(ap.split("/")[:-1])
            if rp_dir and ap_dir and rp_dir == ap_dir:
                return 1.0 / (i + 1)
    return 0.0


def run_card_search(card_index, query_str, limit=5):
    """V3 卡片搜索：对四种卡片类型（task/api/example/doc）分别搜索，
    合并去重后返回结果。用于评测 card 引擎的纯搜索能力。"""
    all_hits = {}
    for ct in ("task", "api", "example", "doc"):
        all_hits[ct] = search_cards(card_index["db"], query_str, MODE_TYPES[ct], limit)

    sections = {}
    paths = []
    for ct, hits in all_hits.items():
        id_key = TYPE_ID_KEY[ct]
        grouped = hits_to_grouped(hits, ct, id_key, limit)
        sections[ct] = grouped
        for item in grouped:
            for p in item.get("paths", []):
                if p not in paths:
                    paths.append(p)

    return {
        "tasks": sections.get("task", []),
        "apis": sections.get("api", []),
        "examples": sections.get("example", []),
        "docs": sections.get("doc", []),
        "paths": paths[:limit * 4],
    }


def run_graph_search(session, query_str, limit=5):
    result = session.search(query_str, top_k=limit, graph="doc")
    return {
        "direct": result.direct_hits,
        "related": result.related_hits,
    }


def search_card(card_index, query_str, limit=5):
    """Card 搜索：每张卡片取 1 条最优路径，实现真正的 Recall@N。
    
    collect_paths() 跨段（tasks/apis/docs）按 card 分数排序，
    每卡只取 paths[0]（去字母排序后即最相关路径），产出 N 条路径。
    与 Graph 的 session.search(top_k=N) 严格对齐 Recall@N 语义。
    """
    entries = collect_paths(card_index, query_str, limit)
    hits = []
    for e in entries:
        hits.append(Hit(
            node_id="", label=e.get("card", e.get("path", "")), source_file=e["path"],
            score=e.get("score", 0), match_type="v3_card", engine="card"
        ))
    return SearchResult(query=query_str, engine="card", direct_hits=hits)


def search_graph(session, query_str, limit=5):
    graph_result = run_graph_search(session, query_str, limit)
    direct = graph_result.get("direct", [])[:limit]
    related = graph_result.get("related", [])[:limit]
    for h in direct:
        h.engine = "graph"
    for h in related:
        h.engine = "graph"
    return SearchResult(
        query=query_str, engine="graph",
        direct_hits=direct, related_hits=related
    )


def search_fusion(card_index, session, query_str, limit=5):
    """融合搜索：组合 card 和 graph 结果，通过 unified_search.fuse_results 排序。
    融合后需要 _ensure_top_dir 确保路径格式统一。"""
    card_result = run_card_search(card_index, query_str, limit)
    graph_result = run_graph_search(session, query_str, limit)
    for h in graph_result.get("direct", []):
        h.engine = "graph"
    for h in graph_result.get("related", []):
        h.engine = "graph"
    result = fuse_results(query_str, card_result, graph_result, limit)
    for h in result.direct_hits:
        h.source_file = _ensure_top_dir(h.source_file)
    for h in result.related_hits:
        h.source_file = _ensure_top_dir(h.source_file)
    return result


def eval_engine(queries, keywords, engine, card_index=None, session=None, limit=5):
    """对指定引擎评测全部查询。使用 keywords（关键词文件）构造搜索查询，
    而非原始用户 query，确保评测条件一致。

    返回完整评测结果 dict，含引擎名称、命中统计、MRR、延迟、类别统计和逐条详情。"""
    results = []
    latencies = []
    cat_stats = defaultdict(lambda: {"total": 0, "full": 0, "partial": 0, "miss": 0})
    mrrs = []
    hit_counts = []

    search_fn = {
        "card": lambda q, l: search_card(card_index, q, l),
        "graph": lambda q, l: search_graph(session, q, l),
        "fusion": lambda q, l: search_fusion(card_index, session, q, l),
    }[engine]

    for idx, q in enumerate(queries):
        q_id = idx + 1
        kw = keywords.get(str(q_id), {})
        acceptable = q.get("acceptable_paths", [])
        category = q.get("category", "unknown")
        keywords_en = kw.get("keywords_en", [])
        keywords_zh = kw.get("keywords_zh", [])
        # 使用 keywords 文件中的关键词组合作为搜索查询，
        # 而非原始 query 文本，确保三种引擎输入一致
        search_q = " ".join(keywords_en + keywords_zh)

        t0 = time.perf_counter()
        result = search_fn(search_q, limit)
        latency = (time.perf_counter() - t0) * 1000
        latencies.append(latency)

        direct_paths = [h.source_file for h in result.direct_hits]
        related_paths = [h.source_file for h in result.related_hits]

        status = check_hit(direct_paths, related_paths, acceptable)
        mrr = compute_mrr(direct_paths, related_paths, acceptable)
        mrrs.append(mrr)
        hit_counts.append(len(result.direct_hits))

        cat_stats[category]["total"] += 1
        cat_stats[category][status.lower()] += 1

        top_path = direct_paths[0] if direct_paths else ""

        results.append({
            "id": q_id, "query": q.get("query", ""), "category": category,
            "status": status, "latency_ms": round(latency, 1),
            "mrr": mrr, "num_hits": len(result.direct_hits),
            "top_path": top_path, "expected": acceptable[:3],
        })

    total = len(results)
    full = sum(1 for r in results if r["status"] == "FULL")
    partial = sum(1 for r in results if r["status"] == "PARTIAL")
    miss = total - full - partial
    sorted_lat = sorted(latencies)
    avg_lat = sum(latencies) / total if total else 0
    p50 = sorted_lat[total // 2] if total else 0
    p95 = sorted_lat[int(total * 0.95)] if total > 1 else sorted_lat[-1] if total else 0
    avg_mrr = sum(mrrs) / total if total else 0
    avg_hits = sum(hit_counts) / total if total else 0

    return {
        "engine": engine, "total": total,
        "full": full, "partial": partial, "miss": miss,
        "recall": (full + partial) / total * 100 if total else 0,
        "precision1": full / total * 100 if total else 0,
        "avg_mrr": avg_mrr, "avg_hits": avg_hits,
        "avg_latency": avg_lat, "p50_latency": p50, "p95_latency": p95,
        "cat_stats": dict(cat_stats), "results": results,
    }


def generate_report(card, graph, fusion):
    engines = [card, graph, fusion]

    lines = [
        "# 三引擎搜索对比评测报告",
        "",
        f"**测试集**: {DATASET_PATH.name} ({fusion['total']} 条)",
        f"**评测引擎**: card / graph / fusion",
        f"**计时范围**: 仅纯搜索（不含 query understanding）",
        "",
        "## 1. 总体对比",
        "",
        "| 指标 | card | graph | fusion |",
        "|------|------|-------|--------|",
    ]

    def fmt_pct(n, t):
        return f"{n} ({n/t*100:.1f}%)"

    rows = [
        ("总查询数", [e["total"] for e in engines]),
        ("完全命中 FULL", [fmt_pct(e["full"], e["total"]) for e in engines]),
        ("部分命中 PARTIAL", [fmt_pct(e["partial"], e["total"]) for e in engines]),
        ("未命中 MISS", [fmt_pct(e["miss"], e["total"]) for e in engines]),
        ("Recall@5 (FULL+PARTIAL)", [f"{e['recall']:.1f}%" for e in engines]),
        ("Precision@1 (FULL)", [f"{e['precision1']:.1f}%" for e in engines]),
        ("MRR (平均倒数排名)", [f"{e['avg_mrr']:.3f}" for e in engines]),
        ("平均直接命中数", [f"{e['avg_hits']:.1f}" for e in engines]),
        ("平均搜索耗时", [f"{e['avg_latency']:.1f}ms" for e in engines]),
        ("P50 耗时", [f"{e['p50_latency']:.1f}ms" for e in engines]),
        ("P95 耗时", [f"{e['p95_latency']:.1f}ms" for e in engines]),
    ]

    for label, vals in rows:
        lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

    all_cats = sorted(set(
        list(card["cat_stats"].keys()) +
        list(graph["cat_stats"].keys()) +
        list(fusion["cat_stats"].keys())
    ))

    lines.extend([
        "",
        "## 2. 各类别 Recall@5 对比",
        "",
        "| 类别 | card | graph | fusion |",
        "|------|------|-------|--------|",
    ])
    for cat in all_cats:
        vals = []
        for e in engines:
            s = e["cat_stats"].get(cat)
            if s and s["total"] > 0:
                vals.append(f"{(s['full']+s['partial'])/s['total']*100:.1f}%")
            else:
                vals.append("—")
        lines.append(f"| {cat} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.extend([
        "",
        "## 3. 搜索耗时分布",
        "",
        "| 范围 | card | graph | fusion |",
        "|------|------|-------|--------|",
    ])
    ranges = [(0, 10), (10, 100), (100, 500), (500, 1000), (1000, 1e9)]
    labels = ["<10ms", "10-100ms", "100-500ms", "500ms-1s", ">1s"]
    for lb, (lo, hi) in zip(labels, ranges):
        vals = []
        for e in engines:
            c = sum(1 for r in e["results"] if lo <= r["latency_ms"] < hi)
            vals.append(str(c))
        lines.append(f"| {lb} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.extend([
        "",
        "## 4. MISS 查询对比",
        "",
        "| ID | 类别 | 查询 | card | graph | fusion |",
        "|---:|------|------|------|-------|--------|",
    ])
    for i in range(fusion["total"]):
        c = card["results"][i]["status"]
        g = graph["results"][i]["status"]
        f = fusion["results"][i]["status"]
        if c == "MISS" or g == "MISS" or f == "MISS":
            q = fusion["results"][i]["query"][:35]
            lines.append(f"| {i+1} | {fusion['results'][i]['category']} | {q} | {c} | {g} | {f} |")

    fusion_only = []
    for i in range(fusion["total"]):
        f_s = fusion["results"][i]["status"]
        c_s = card["results"][i]["status"]
        g_s = graph["results"][i]["status"]
        if f_s == "FULL" and (c_s == "MISS" or g_s == "MISS"):
            fusion_only.append((i + 1, fusion["results"][i]))

    if fusion_only:
        lines.extend([
            "",
            "## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）",
            "",
            f"共 {len(fusion_only)} 条：",
            "",
            "| ID | 查询 | card | graph |",
            "|---:|------|------|-------|",
        ])
        for idx, r in fusion_only:
            c = card["results"][idx - 1]["status"]
            g = graph["results"][idx - 1]["status"]
            lines.append(f"| {idx} | {r['query'][:40]} | {c} | {g} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="三引擎搜索对比评测")
    parser.add_argument("--limit", type=int, default=0, help="只测前N条（0=全量）")
    parser.add_argument("--keywords", default=None)
    parser.add_argument("--dataset", default=None)
    parser.add_argument("--output", default=str(DEFAULT_REPORT))
    args = parser.parse_args()

    keywords = load_keywords(args.keywords)
    queries = load_queries(args.dataset)
    if args.limit > 0:
        queries = queries[:args.limit]
    print(f"Loaded {len(queries)} queries")

    print(f"Loading card index: {CARD_INDEX_DIR}")
    card_index = load_index(CARD_INDEX_DIR)
    print("Card index loaded")

    print(f"Loading graph: {GRAPH_PATH}")
    session = create_session(graph_dir=str(GRAPH_DATA_DIR))
    session.doc_engine = None
    session.load_doc_graph(str(GRAPH_PATH))
    print("Graph loaded into memory")

    engine_data = {}
    for engine in ("card", "graph", "fusion"):
        print(f"\n=== Evaluating {engine} ===")
        data = eval_engine(
            queries, keywords, engine,
            card_index=card_index, session=session,
        )
        engine_data[engine] = data
        print(f"  FULL={data['full']} PARTIAL={data['partial']} MISS={data['miss']}")
        print(f"  Recall@5={data['recall']:.1f}% MRR={data['avg_mrr']:.3f} Avg={data['avg_latency']:.1f}ms")

    report = generate_report(
        engine_data["card"], engine_data["graph"], engine_data["fusion"]
    )

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()