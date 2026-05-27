#!/usr/bin/env python3
"""仓颉鸿蒙知识图谱 — 命令行工具。

用法：
    python cli.py build-doc ../docs/harmonyos-6.0.2-15k [-o data/doc/graph.json] [--enhance]
    python cli.py build-code src/ [-o data/code/graph.json]
    python cli.py build docs/ [-o data/full/graph.json] [--enhance]
    python cli.py build-subgraph docs/harmonyos --name harmonyos [--enhance]
    python cli.py merge data/subgraphs/*/graph.json --output data/merged/graph.json
    python cli.py enhance-graph data/merged/graph.json --docs-dir ../docs/
    python cli.py search "List 组件"
    python cli.py path "UIAbility" "WindowStage"
    python cli.py explain "List"
    python cli.py neighbors "List"
    python cli.py god-nodes
    python cli.py surprises
    python cli.py stats
    python cli.py graphs
"""

import argparse
import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from query import create_session
from core.constants import LAYER_NAMES, LAYER_NAMES_FULL, DEFAULT_GRAPH_PATH


def _ensure_utf8():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')


def cmd_search(args):
    session = create_session()
    result = session.search(args.query, top_k=args.limit, graph=args.graph)

    print(f"\n查询: {args.query}")
    print(f"策略: OR+累加")
    print(f"使用图谱: {result.graph_used}")
    print(f"耗时: {result.latency_ms:.1f}ms")

    if args.brief:
        print(result.to_brief_text())
    else:
        print(result.to_full_text())


def cmd_path(args):
    session = create_session()
    path = session.find_path(args.node_a, args.node_b, max_depth=args.max_depth)

    print(f"\n路径: {args.node_a} → {args.node_b}")
    if path:
        for i, node in enumerate(path):
            layer_name = LAYER_NAMES.get(node.layer, "?")
            print(f"  {i+1}. [{layer_name}] {node.label}")
    else:
        print("  未找到路径")


def cmd_explain(args):
    session = create_session()
    info = session.explain(args.node)

    if info:
        print(info)
    else:
        print(f"未找到节点: {args.node}")


def cmd_stats(args):
    session = create_session()
    stats = session.get_stats()

    print("\n=== 图谱统计 ===")
    mg = stats.get("merged_graph", {})
    if mg.get("loaded"):
        print(f"合并图谱: {mg['nodes']} 节点, {mg['edges']} 边")

    for name, sg in stats.get("subgraphs", {}).items():
        if sg.get("loaded"):
            print(f"子图谱 [{name}]: {sg['nodes']} 节点, {sg['edges']} 边")

    dg = stats.get("doc_graph", {})
    if dg.get("loaded"):
        print(f"文档图: {dg['nodes']} 节点, {dg['edges']} 边")

    cg = stats.get("code_graph", {})
    if cg.get("loaded"):
        print(f"源码图: {cg['nodes']} 节点, {cg['edges']} 边")


def cmd_graphs(args):
    session = create_session()
    graphs = session.available_graphs()

    print("\n可用图谱:")
    for g in graphs:
        print(f"  - {g}")


def cmd_neighbors(args):
    session = create_session()
    neighbors = session.neighbors(args.node, max_count=args.limit)

    print(f"\n节点 {args.node} 的邻居 ({len(neighbors)} 个):")
    for n in neighbors:
        print(f"  - {n.label}")


def cmd_god_nodes(args):
    session = create_session()
    nodes = session.god_nodes(top_n=args.top_n)

    print(f"\n核心节点 (Top {args.top_n}):")
    for i, node in enumerate(nodes, 1):
        print(f"  {i}. {node['label']} (度={node['degree']}, src={node['source_file']})")


def cmd_surprises(args):
    session = create_session()
    edges = session.surprises(top_n=args.top_n)

    print(f"\n惊奇连接 (跨社区边 Top {args.top_n}):")
    for i, edge in enumerate(edges, 1):
        print(f"  {i}. {edge['source_label']} (社区 {edge['source_community']}) → {edge['target_label']} (社区 {edge['target_community']})")


def cmd_build_doc(args):
    """构建文档图。提取 → build_subgraph → nx.Graph → 可可选 enhance → cluster → annotate → save。"""
    _ensure_utf8()
    from graph.doc.builder import build_doc_graph, build_doc_nx_graph
    from graph.builders import save_graph, cluster, assign_communities_to_nodes, annotate_layers

    root = Path(args.path).resolve()
    directed = args.directed
    default_output = _PROJECT_ROOT / "data" / "doc" / "graph.json"
    output_path = Path(args.output) if args.output else default_output

    print(f"\n构建文档图: {root}")
    nodes, neighbors = build_doc_graph(root)
    print(f"  提取节点: {len(nodes)}, 边: {sum(len(v) for v in neighbors.values()) // 2}")

    G = build_doc_nx_graph(nodes, neighbors, directed=directed)
    print(f"  NetworkX: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")

    if args.enhance:
        print("\nLLM 信息增强...")
        try:
            from graph.llm.pipeline import enhance_graph_from_files
            from networkx.readwrite import json_graph as _jg
            import tempfile

            graph_data = _jg.node_link_data(G, edges="links")
            source_files = [n.source_file for n in nodes.values() if n.source_file]

            temp_output = Path(tempfile.mktemp(suffix=".json"))
            enhance_graph_from_files(
                graph_data,
                source_files,
                root,
                output_path=temp_output,
            )

            if temp_output.exists():
                from graph.builders import load_graph
                G = load_graph(temp_output)
                temp_output.unlink()
                print(f"  增强完成")
        except Exception as e:
            print(f"  LLM 增强失败: {e}")
            import traceback
            traceback.print_exc()

    _cluster_and_annotate(G)
    save_graph(G, output_path)
    print(f"\n完成！保存至 {output_path}")


def cmd_build_code(args):
    """构建源码图。提取 → build_subgraph → nx.Graph → cluster → annotate → save."""
    _ensure_utf8()
    from graph.code.builder import build_code_graph, build_code_nx_graph
    from graph.builders import save_graph, cluster, assign_communities_to_nodes, annotate_layers

    root = Path(args.path).resolve()
    directed = args.directed
    default_output = _PROJECT_ROOT / "data" / "code" / "graph.json"
    output_path = Path(args.output) if args.output else default_output

    print(f"\n构建源码图: {root}")
    nodes, neighbors = build_code_graph(root)
    print(f"  提取节点: {len(nodes)}, 边: {sum(len(v) for v in neighbors.values()) // 2}")

    G = build_code_nx_graph(nodes, neighbors, directed=directed)
    print(f"  NetworkX: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")

    _cluster_and_annotate(G)
    save_graph(G, output_path)
    print(f"\n完成！保存至 {output_path}")


def _extract_and_build(root, directed=False):
    """公共编排逻辑：扫描 → 提取 → 构建子图。"""
    from graph.builders import detect, build_subgraph

    print(f"\n扫描目录: {root}")
    detected = detect(root)
    code_files = detected.get("files", {}).get("code", [])
    doc_files = detected.get("files", {}).get("document", [])

    print(f"文件数: {detected['total_files']}")
    print(f"词数: ~{detected['total_words']}")

    if detected.get("warning"):
        print(f"警告: {detected['warning']}")

    doc_nodes = {}
    doc_neighbors = {}
    if doc_files:
        print(f"\n文档提取 ({len(doc_files)} 个文件)...")
        from graph.doc.builder import build_doc_graph
        doc_nodes, doc_neighbors = build_doc_graph(root)
        print(f"  节点: {len(doc_nodes)}, 边: {sum(len(v) for v in doc_neighbors.values()) // 2}")

    code_nodes = {}
    code_neighbors = {}
    if code_files:
        print(f"\n代码提取 ({len(code_files)} 个文件)...")
        from graph.code.builder import build_code_graph
        code_nodes, code_neighbors = build_code_graph(root)
        print(f"  节点: {len(code_nodes)}, 边: {sum(len(v) for v in code_neighbors.values()) // 2}")

    if not doc_nodes and not code_nodes:
        print("\n错误: 无提取结果，图谱为空")
        return None, None, None

    print("\n构建图谱...")
    G = build_subgraph(doc_nodes, doc_neighbors, code_nodes, code_neighbors, directed=directed)
    print(f"  节点: {G.number_of_nodes()}")
    print(f"  边: {G.number_of_edges()}")

    return G, doc_nodes, doc_neighbors


def _cluster_and_annotate(G):
    """公共聚类+分层逻辑。"""
    from graph.builders import cluster, assign_communities_to_nodes, annotate_layers

    print("\n聚类...")
    communities = cluster(G)
    assign_communities_to_nodes(G, communities)
    print(f"  社区: {len(communities)}")

    print("\n分层标注...")
    annotate_layers(G)
    layer_dist = {}
    for _, data in G.nodes(data=True):
        layer = data.get("layer", 3)
        layer_dist[layer] = layer_dist.get(layer, 0) + 1
    print(f"  L1: {layer_dist.get(1, 0)}, L2: {layer_dist.get(2, 0)}, L3: {layer_dist.get(3, 0)}")

    return communities


def cmd_build(args):
    """构建图谱。编排：doc提取 + code提取 → 合并 → 聚类 → 分层 → 保存。"""
    _ensure_utf8()
    from graph.builders import save_graph, load_graph

    root = Path(args.path).resolve()
    directed = args.directed

    default_output = _PROJECT_ROOT / "data" / "full" / "graph.json"
    output_path = Path(args.output) if args.output else default_output

    if args.cluster_only:
        if not output_path.exists():
            print(f"错误: 图谱不存在: {output_path}")
            print("  先运行 build 命令创建图谱")
            return

        print(f"\n重新聚类: {output_path}")
        G = load_graph(output_path)
        print(f"  节点: {G.number_of_nodes()}, 边: {G.number_of_edges()}")
        _cluster_and_annotate(G)
        save_graph(G, output_path)
        print(f"\n完成！图谱保存至: {output_path}")
        return

    G, doc_nodes, doc_neighbors = _extract_and_build(root, directed=directed)
    if G is None:
        return

    if args.enhance and doc_nodes:
        print("\nLLM 信息增强 (Doc Only)...")
        try:
            from graph.llm.pipeline import enhance_graph_from_files
            from networkx.readwrite import json_graph as _jg

            graph_data = _jg.node_link_data(G, edges="links")
            source_files = [n.source_file for n in doc_nodes.values() if n.source_file]

            temp_output = output_path.with_suffix(".tmp_enhanced.json")

            enhance_graph_from_files(
                graph_data,
                source_files,
                root,
                output_path=temp_output
            )

            if temp_output.exists():
                G = load_graph(temp_output)
                temp_output.unlink()
            print(f"  增强完成")
        except Exception as e:
            print(f"  LLM 增强失败: {e}")
            import traceback
            traceback.print_exc()

    _cluster_and_annotate(G)
    save_graph(G, output_path)
    print(f"\n完成！图谱保存至: {output_path}")


def cmd_build_subgraph(args):
    """构建子图谱。"""
    _ensure_utf8()
    from graph.builders import save_graph

    root = Path(args.path).resolve()
    name = args.name
    directed = args.directed

    output_dir = Path("data/subgraphs") / name
    output_path = output_dir / "graph.json"

    print(f"\n构建子图谱: {name}")
    print(f"输入目录: {root}")
    print(f"输出路径: {output_path}")

    G, doc_nodes, doc_neighbors = _extract_and_build(root, directed=directed)
    if G is None:
        return

    if args.enhance and doc_nodes:
        print("\nLLM 信息增强...")
        try:
            from graph.llm.pipeline import enhance_graph_from_files
            from networkx.readwrite import json_graph as _jg

            graph_data = _jg.node_link_data(G, edges="links")
            source_files = [n.source_file for n in doc_nodes.values() if n.source_file]

            temp_output = output_path.with_suffix(".tmp_enhanced.json")

            enhance_graph_from_files(
                graph_data,
                source_files,
                root,
                output_path=temp_output
            )

            if temp_output.exists():
                from graph.builders import load_graph
                G = load_graph(temp_output)
                temp_output.unlink()
            print(f"  增强完成")
        except Exception as e:
            print(f"  LLM 增强失败: {e}")

    _cluster_and_annotate(G)
    G.graph["subgraph_name"] = name

    save_graph(G, output_path)
    print(f"\n完成！子图谱保存至: {output_path}")


def cmd_merge(args):
    """合并多个子图谱。"""
    from graph.builders import merge_graphs

    graph_paths = args.graphs
    output_path = args.output
    deduplicate = not args.no_deduplicate
    recluster = not args.no_recluster
    directed = args.directed

    print(f"\n合并图谱:")
    print(f"  输入: {len(graph_paths)} 个图谱")
    for p in graph_paths:
        print(f"    - {p}")
    print(f"  输出: {output_path}")
    print(f"  去重: {deduplicate}")
    print(f"  重聚类: {recluster}")

    G = merge_graphs(
        graph_paths,
        output_path,
        deduplicate=deduplicate,
        recluster=recluster,
        annotate=True,
        directed=directed,
    )

    print(f"\n完成！合并图谱: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")


def cmd_export(args):
    """导出图谱。"""
    from export import to_json, to_html, generate_report
    from engines import GraphifyEngine

    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"错误: 图谱文件不存在: {graph_path}")
        return

    engine = GraphifyEngine()
    engine.load(str(graph_path))
    G = engine._graph

    max_nodes = args.max_nodes if hasattr(args, 'max_nodes') else 0
    if max_nodes > 0 and G.number_of_nodes() > max_nodes:
        print(f"图谱有 {G.number_of_nodes()} 节点，裁剪至度最高的 {max_nodes} 个节点...")
        degree = dict(G.degree())
        top_nodes = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:max_nodes]
        top_node_ids = set(n for n, _ in top_nodes)
        G = G.subgraph(top_node_ids).copy()
        print(f"裁剪后: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")

    communities: dict[int, list[str]] = {}
    for node_id, data in G.nodes(data=True):
        cid = data.get("community")
        if cid is not None:
            communities.setdefault(int(cid), []).append(node_id)

    if not communities:
        print("图谱缺少 community 信息，正在聚类...")
        from graph.builders.cluster import cluster, assign_communities_to_nodes
        communities = cluster(G)
        assign_communities_to_nodes(G, communities)

    output_dir = Path(args.output_dir) if args.output_dir else graph_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    format_name = args.format.lower()

    if format_name == "json":
        output_file = output_dir / "graph_export.json"
        to_json(G, communities, str(output_file))
        print(f"JSON 导出完成: {output_file}")

    elif format_name == "html":
        output_file = output_dir / "graph.html"
        try:
            to_html(G, communities, str(output_file))
            print(f"HTML 导出完成: {output_file}")
        except ValueError as e:
            print(f"警告: {e}")

    elif format_name == "report":
        output_file = output_dir / "GRAPH_REPORT.md"
        generate_report(G, communities, output_path=str(output_file))
        print(f"报告导出完成: {output_file}")

    elif format_name == "all":
        to_json(G, communities, str(output_dir / "graph_export.json"))
        print(f"JSON: {output_dir / 'graph_export.json'}")

        try:
            to_html(G, communities, str(output_dir / "graph.html"))
            print(f"HTML: {output_dir / 'graph.html'}")
        except ValueError as e:
            print(f"HTML: {e}")

        generate_report(G, communities, output_path=str(output_dir / "GRAPH_REPORT.md"))
        print(f"报告: {output_dir / 'GRAPH_REPORT.md'}")

    else:
        print(f"未知格式: {format_name}。可用: json, html, report, all")


def cmd_enhance_graph(args):
    """对已有图谱进行 LLM 增强。"""
    _ensure_utf8()
    from graph.llm.pipeline import enhance_graph_from_files

    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"错误: 图谱文件不存在: {graph_path}")
        return

    print(f"加载图谱: {graph_path}")
    with open(graph_path, encoding="utf-8") as f:
        graph_data = json.load(f)

    nodes = graph_data.get("nodes", [])
    if isinstance(nodes, dict):
        nodes = list(nodes.values())

    source_files = []
    for node in nodes:
        sf = node.get("source_file", "")
        if sf:
            source_files.append(sf)

    print(f"找到 {len(source_files)} 个 Doc 节点待增强")

    if args.docs_dir:
        docs_dir = Path(args.docs_dir)
    else:
        docs_dir = None

    if docs_dir and not docs_dir.exists():
        print(f"错误: 文档目录不存在: {docs_dir}")
        print("  请使用 --docs-dir 指定文档根目录")
        return

    output_path = Path(args.output) if args.output else graph_path

    enhance_graph_from_files(
        graph_data,
        source_files,
        docs_dir,
        batch_chars=args.batch_chars,
        batch_limit=args.batch_limit,
        resume=not args.no_resume,
        output_path=output_path,
        total_timeout=args.total_timeout,
    )

    print(f"\n增强完成，图谱已保存至: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="仓颉鸿蒙知识图谱 CLI")
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # ── 查询类 ──

    p_search = subparsers.add_parser("search", help="搜索图谱（定位文档）")
    p_search.add_argument("query", help="查询字符串")
    p_search.add_argument("--limit", "-k", type=int, default=5, help="直接命中返回数量")
    p_search.add_argument("--graph", choices=["doc", "code", "auto", "both"], default="auto", help="选择图谱")
    p_search.add_argument("--brief", "-b", action="store_true", help="仅返回 label + source_file")
    p_search.set_defaults(func=cmd_search)

    p_path = subparsers.add_parser("path", help="查找关系路径")
    p_path.add_argument("node_a", help="起点节点")
    p_path.add_argument("node_b", help="终点节点")
    p_path.add_argument("--max-depth", type=int, default=5, help="最大深度")
    p_path.set_defaults(func=cmd_path)

    p_explain = subparsers.add_parser("explain", help="解释节点")
    p_explain.add_argument("node", help="节点 ID 或名称")
    p_explain.set_defaults(func=cmd_explain)

    p_neighbors = subparsers.add_parser("neighbors", help="获取邻居节点")
    p_neighbors.add_argument("node", help="节点 ID 或名称")
    p_neighbors.add_argument("--limit", type=int, default=20, help="数量上限")
    p_neighbors.set_defaults(func=cmd_neighbors)

    # ── 图计算类 ──

    p_god = subparsers.add_parser("god-nodes", help="核心节点（连接最多）")
    p_god.add_argument("--top-n", type=int, default=10, help="数量")
    p_god.set_defaults(func=cmd_god_nodes)

    p_surprises = subparsers.add_parser("surprises", help="惊奇连接（跨社区边）")
    p_surprises.add_argument("--top-n", type=int, default=5, help="数量")
    p_surprises.set_defaults(func=cmd_surprises)

    # ── 信息类 ──

    p_stats = subparsers.add_parser("stats", help="显示统计")
    p_stats.set_defaults(func=cmd_stats)

    p_graphs = subparsers.add_parser("graphs", help="列出可用图谱")
    p_graphs.set_defaults(func=cmd_graphs)

    # ── 构建类 ──

    p_build_doc = subparsers.add_parser("build-doc", help="构建文档图（1文件=1节点）")
    p_build_doc.add_argument("path", help="文档输入目录")
    p_build_doc.add_argument("--output", "-o", help="输出路径（默认 data/doc/graph.json）")
    p_build_doc.add_argument("--directed", action="store_true", help="生成有向图")
    p_build_doc.add_argument("--enhance", action="store_true", help="启用 LLM 信息增强")
    p_build_doc.set_defaults(func=cmd_build_doc)

    p_build_code = subparsers.add_parser("build-code", help="构建源码图（1定义=1节点，多语言 AST）")
    p_build_code.add_argument("path", help="源码输入目录")
    p_build_code.add_argument("--output", "-o", help="输出路径（默认 data/code/graph.json）")
    p_build_code.add_argument("--directed", action="store_true", help="生成有向图")
    p_build_code.set_defaults(func=cmd_build_code)

    p_build = subparsers.add_parser("build", help="构建图谱（编排 doc + code + 可选 LLM 增强）")
    p_build.add_argument("path", nargs="?", default=".", help="输入目录（默认当前目录）")
    p_build.add_argument("--output", help="输出路径（默认 data/full/graph.json）")
    p_build.add_argument("--enhance", action="store_true", help="启用 LLM 信息增强")
    p_build.add_argument("--directed", action="store_true", help="生成有向图")
    p_build.add_argument("--cluster-only", action="store_true", help="仅重新聚类（不提取）")
    p_build.set_defaults(func=cmd_build)

    p_build_subgraph = subparsers.add_parser("build-subgraph", help="构建子图谱")
    p_build_subgraph.add_argument("path", help="输入目录")
    p_build_subgraph.add_argument("--name", required=True, help="子图谱名称（如 api/core/ui）")
    p_build_subgraph.add_argument("--enhance", action="store_true", help="启用 LLM 信息增强")
    p_build_subgraph.add_argument("--directed", action="store_true", help="生成有向图")
    p_build_subgraph.set_defaults(func=cmd_build_subgraph)

    p_merge = subparsers.add_parser("merge", help="合并多个子图谱")
    p_merge.add_argument("graphs", nargs="+", help="图谱文件路径（多个）")
    p_merge.add_argument("--output", required=True, help="合并后的输出路径")
    p_merge.add_argument("--no-deduplicate", action="store_true", help="不去重")
    p_merge.add_argument("--no-recluster", action="store_true", help="不重新聚类")
    p_merge.add_argument("--directed", action="store_true", help="生成有向图")
    p_merge.set_defaults(func=cmd_merge)

    # ── 导出/增强类 ──

    p_export = subparsers.add_parser("export", help="导出图谱")
    p_export.add_argument("--format", choices=["json", "html", "report", "all"], default="all", help="导出格式")
    p_export.add_argument("--graph", default=DEFAULT_GRAPH_PATH, help="图谱路径")
    p_export.add_argument("--output-dir", help="输出目录")
    p_export.add_argument("--max-nodes", type=int, default=0, help="HTML导出最大节点数（0=不限制，超过5000时建议设值，如5000）")
    p_export.set_defaults(func=cmd_export)

    p_enhance = subparsers.add_parser("enhance-graph", help="对已有图谱进行 LLM 增强（仅 Doc 节点）")
    p_enhance.add_argument("graph", help="图谱文件路径（JSON）")
    p_enhance.add_argument("--docs-dir", help="文档根目录（必填，不再硬编码推断）")
    p_enhance.add_argument("--output", "-o", help="输出路径（默认覆盖原文件）")
    p_enhance.add_argument("--batch-chars", type=int, default=15000, help="单批次最大字符数（默认 15000）")
    p_enhance.add_argument("--batch-limit", type=int, default=0, help="最多处理批次数（0=全量）")
    p_enhance.add_argument("--total-timeout", type=int, default=0, help="整个流程总超时秒数（0=不限制，6小时=21600）")
    p_enhance.add_argument("--no-resume", action="store_true", help="不跳过已增强节点")
    p_enhance.set_defaults(func=cmd_enhance_graph)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()