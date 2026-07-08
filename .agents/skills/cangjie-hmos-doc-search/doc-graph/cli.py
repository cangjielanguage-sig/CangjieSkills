#!/usr/bin/env python3
"""仓颉鸿蒙知识图谱 — 搜索运行时 CLI。

构建子命令已迁至 cangjie-hmos-doc-search-maintenance/graph/builder/build_cli.py。
本 CLI 仅提供搜索、遍历和导出功能。

各子命令说明：
- search: 关键词搜索图谱，定位文档/API/代码定义
- path: 查找两个节点之间的关系路径（需要 NetworkX）
- explain: 展示节点详细元数据（标签、关键词、邻居等）
- neighbors: 获取节点的直接邻居列表
- god-nodes: 度最高的核心节点排行（需要 NetworkX）
- surprises: 跨社区的惊奇连接（需要 NetworkX）
- stats/graphs: 图谱统计和可用图谱列表
- export: 导出图谱为 JSON/HTML/报告格式

用法：
    python cli.py search "List 组件" --graph doc -b -k 5
    python cli.py path "UIAbility" "WindowStage"
    python cli.py explain "List"
    python cli.py neighbors "List"
    python cli.py god-nodes
    python cli.py surprises
    python cli.py stats
    python cli.py graphs
    python cli.py export --format html --graph data/doc/graph.json
"""

import argparse
import sys
from pathlib import Path

# 将 doc-graph 目录加入 sys.path，确保子模块导入正常
_PROJECT_ROOT = Path(__file__).resolve().parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from query import create_session
from core.constants import LAYER_NAMES, DEFAULT_GRAPH_PATH


def _ensure_utf8():
    """确保 stdout/stderr 使用 UTF-8 编码 — Windows 环境下中文输出必需。"""
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')


def cmd_search(args):
    """搜索命令 — 调用 GraphSession.search() 并输出结果。"""
    session = create_session()
    result = session.search(args.query, top_k=args.limit, graph=args.graph)

    if args.json:
        import json as _j
        print(_j.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        return

    print(f"\n查询: {args.query}")
    print(f"策略: OR+累加")
    print(f"使用图谱: {result.graph_used}")
    print(f"耗时: {result.latency_ms:.1f}ms")

    # brief 模式仅输出 label + source_file，Agent 默认使用
    # full 模式输出完整信息（含查询、图谱、耗时）
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


def cmd_export(args):
    """导出命令 — 将图谱导出为 JSON/HTML/报告格式。

    支持节点裁剪：当 --max-nodes 大于 0 且图谱节点数超过限制时，
    仅保留度最高的 max-nodes 个节点，避免 HTML 导出过于庞大。
    缺少 community 信息时发出警告（社区分组是 HTML 可视化的核心）。
    """
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
        print("注意: 图谱缺少 community 信息，导出将不含社区分组。如需社区信息请通过维护 Skill 重新构建图谱。")

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


def main():
    _ensure_utf8()
    parser = argparse.ArgumentParser(description="仓颉鸿蒙知识图谱搜索 CLI（构建功能已迁至 maintenance skill）")
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    p_search = subparsers.add_parser("search", help="搜索图谱（定位文档）")
    p_search.add_argument("query", help="查询字符串")
    p_search.add_argument("--limit", "-k", type=int, default=5, help="直接命中返回数量")
    p_search.add_argument("--graph", choices=["doc", "code", "auto", "both"], default="auto", help="选择图谱")
    p_search.add_argument("--brief", "-b", action="store_true", help="仅返回 label + source_file")
    p_search.add_argument("--json", action="store_true", help="输出结构化 JSON（与 card/fusion 对齐）")
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

    p_god = subparsers.add_parser("god-nodes", help="核心节点（连接最多）")
    p_god.add_argument("--top-n", type=int, default=10, help="数量")
    p_god.set_defaults(func=cmd_god_nodes)

    p_surprises = subparsers.add_parser("surprises", help="惊奇连接（跨社区边）")
    p_surprises.add_argument("--top-n", type=int, default=5, help="数量")
    p_surprises.set_defaults(func=cmd_surprises)

    p_stats = subparsers.add_parser("stats", help="显示统计")
    p_stats.set_defaults(func=cmd_stats)

    p_graphs = subparsers.add_parser("graphs", help="列出可用图谱")
    p_graphs.set_defaults(func=cmd_graphs)

    p_export = subparsers.add_parser("export", help="导出图谱")
    p_export.add_argument("--format", choices=["json", "html", "report", "all"], default="all", help="导出格式")
    p_export.add_argument("--graph", default=DEFAULT_GRAPH_PATH, help="图谱路径")
    p_export.add_argument("--output-dir", help="输出目录")
    p_export.add_argument("--max-nodes", type=int, default=0, help="HTML导出最大节点数（0=不限制）")
    p_export.set_defaults(func=cmd_export)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()