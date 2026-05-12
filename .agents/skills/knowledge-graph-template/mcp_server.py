#!/usr/bin/env python3
"""MCP stdio server: 把 knowledge-graph-template 图谱暴露给 code agent。

七个工具对齐原版 graphify v7 的 MCP 协议：
- query_graph / get_node / get_neighbors / get_community
- god_nodes / graph_stats / shortest_path

启动方式：
    python mcp_server.py [--graph data/merged/graph.json]

在 claude-code settings.json 的 mcpServers 里注册：
    {
      "mcpServers": {
        "cangjie-graphify": {
          "command": "python",
          "args": ["<绝对路径>/knowledge-graph-template/mcp_server.py"]
        }
      }
    }
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from query import create_session


def make_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="query_graph",
            description="语义/关键词搜索图谱节点，返回匹配节点与对应文档路径。适合'做一个 X 功能' / 'A 和 B 怎么配合' / 跨概念关联类 query。",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "查询词或自然语言描述"},
                    "limit": {"type": "integer", "default": 10, "description": "返回节点上限"},
                    "graph": {"type": "string", "description": "可选：指定子图（harmonyos/std/stdx/lang-features/tools/merged）"},
                },
                "required": ["query"],
            },
        ),
        types.Tool(
            name="get_node",
            description="按节点 label 或 id 获取节点详情（社区归属、层级、源文件路径）。",
            inputSchema={
                "type": "object",
                "properties": {"node": {"type": "string"}},
                "required": ["node"],
            },
        ),
        types.Tool(
            name="get_neighbors",
            description="获取节点的邻居（图遍历 BFS）。适合发现'这个 API 的典型搭档' / '这个概念的相关组件'。",
            inputSchema={
                "type": "object",
                "properties": {
                    "node": {"type": "string"},
                    "depth": {"type": "integer", "default": 2},
                    "limit": {"type": "integer", "default": 30},
                },
                "required": ["node"],
            },
        ),
        types.Tool(
            name="get_community",
            description="获取某社区的全部节点。社区是图拓扑自动聚类的结果，一个社区通常对应一个功能领域。",
            inputSchema={
                "type": "object",
                "properties": {"community_id": {"type": "integer"}},
                "required": ["community_id"],
            },
        ),
        types.Tool(
            name="god_nodes",
            description="返回连接度最高的核心节点（领域里的关键 API / 概念）。适合'这个领域有哪些核心 API' query。",
            inputSchema={
                "type": "object",
                "properties": {"top_n": {"type": "integer", "default": 10}},
            },
        ),
        types.Tool(
            name="graph_stats",
            description="返回图谱规模（节点数、边数、社区数、各子图统计）。",
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="shortest_path",
            description="查两个节点之间的最短路径。适合'A 和 B 怎么关联' query。",
            inputSchema={
                "type": "object",
                "properties": {
                    "source": {"type": "string"},
                    "target": {"type": "string"},
                    "max_depth": {"type": "integer", "default": 5},
                },
                "required": ["source", "target"],
            },
        ),
    ]


def build_server(graph_dir: Path | None) -> Server:
    session = create_session(graph_dir=str(graph_dir) if graph_dir else None, enable_feedback=False)

    def _resolve_node(label_or_id: str) -> tuple[str | None, str | None, object | None]:
        """解析 label/id 到 (id, graph_name, search_engine)。

        优先走 search 找到节点所在子图；再在该子图的 search 实例上做 explain / neighbors / find_path，
        因为 merged 图在合并时会丢 id 归属信息，不少子图节点在 merged 里查不到。
        """
        hits = session.search(label_or_id, limit=1)
        if hits.nodes:
            first = hits.nodes[0]
            nid = first.id if hasattr(first, "id") else first.get("id")
            graph_name = hits.graph_used
            searcher = session._subgraph_searches.get(graph_name) if graph_name else None
            return nid, graph_name, searcher
        return None, None, None

    def _node_field(node, key: str, default=""):
        """兼容 dict / 对象两种返回形态。"""
        if isinstance(node, dict):
            return node.get(key, default)
        return getattr(node, key, default)

    server = Server("cangjie-graphify")

    @server.list_tools()
    async def _list_tools() -> list[types.Tool]:
        return make_tools()

    @server.call_tool()
    async def _call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        args = arguments or {}

        if name == "query_graph":
            result = session.search(
                args["query"],
                limit=int(args.get("limit", 10)),
                force_graph=args.get("graph"),
            )
            payload = {
                "query": args["query"],
                "graph_used": result.graph_used,
                "latency_ms": result.latency_ms,
                "paths": result.paths,
                "nodes": [
                    {
                        "label": _node_field(n, "label"),
                        "id": _node_field(n, "id"),
                        "layer": _node_field(n, "layer", 0),
                        "source_file": _node_field(n, "source_file"),
                    }
                    for n in result.nodes[: int(args.get("limit", 10))]
                ],
            }

        elif name == "get_node":
            nid, graph_name, searcher = _resolve_node(args["node"])
            if not nid:
                payload = {"error": f"node not found: {args['node']}"}
            else:
                engine = searcher or session._merged_search
                info = engine.explain(nid)
                if info is None:
                    payload = {"resolved_id": nid, "graph": graph_name, "detail": "explain returned None"}
                elif isinstance(info, dict):
                    payload = {"graph": graph_name, **info}
                else:
                    # NodeInfo dataclass
                    payload = {
                        "graph": graph_name,
                        "id": _node_field(info, "id"),
                        "label": _node_field(info, "label"),
                        "source_file": _node_field(info, "source_file"),
                        "layer": _node_field(info, "layer", 0),
                        "community": _node_field(info, "community", -1),
                        "degree": _node_field(info, "degree", 0),
                    }

        elif name == "get_neighbors":
            nid, graph_name, searcher = _resolve_node(args["node"])
            if not nid:
                payload = {"error": f"node not found: {args['node']}"}
            else:
                engine = searcher or session._merged_search
                limit = int(args.get("limit", 30))
                neighbors = engine.neighbors(nid, max_count=limit)
                payload = {
                    "node": args["node"],
                    "resolved_id": nid,
                    "graph": graph_name,
                    "neighbors": [
                        {
                            "label": _node_field(n, "label"),
                            "id": _node_field(n, "id"),
                            "layer": _node_field(n, "layer", 0),
                            "source_file": _node_field(n, "source_file"),
                            "degree": _node_field(n, "degree", 0),
                        }
                        for n in neighbors
                    ],
                    "count": len(neighbors),
                }

        elif name == "get_community":
            info = session.community_info(int(args["community_id"]))
            payload = info if isinstance(info, dict) else {"detail": str(info)}

        elif name == "god_nodes":
            nodes = session.god_nodes(top_n=int(args.get("top_n", 10)))
            payload = {"god_nodes": nodes}

        elif name == "graph_stats":
            payload = session.get_stats()

        elif name == "shortest_path":
            src_id, src_graph, src_searcher = _resolve_node(args["source"])
            tgt_id, tgt_graph, _ = _resolve_node(args["target"])
            if not src_id or not tgt_id:
                payload = {"error": f"source or target not found: source={args['source']}, target={args['target']}"}
            elif src_graph != tgt_graph:
                payload = {
                    "error": "source and target are in different subgraphs",
                    "source_graph": src_graph,
                    "target_graph": tgt_graph,
                    "hint": "merged graph deduplication pending (P1); try querying within the same domain",
                }
            else:
                engine = src_searcher or session._merged_search
                path = engine.find_path(src_id, tgt_id, max_depth=int(args.get("max_depth", 5)))
                payload = {
                    "source": args["source"],
                    "target": args["target"],
                    "resolved_source": src_id,
                    "resolved_target": tgt_id,
                    "graph": src_graph,
                    "path": [
                        {"label": _node_field(n, "label"), "id": _node_field(n, "id")}
                        for n in path
                    ] if path else [],
                    "length": len(path) if path else 0,
                }

        else:
            payload = {"error": f"unknown tool: {name}"}

        return [types.TextContent(type="text", text=json.dumps(payload, ensure_ascii=False, indent=2))]

    return server


async def main_async(graph_dir: Path | None) -> None:
    server = build_server(graph_dir)
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    parser = argparse.ArgumentParser(description="Cangjie graphify MCP server")
    parser.add_argument("--graph-dir", type=Path, default=None, help="图谱数据目录（默认：data/）")
    args = parser.parse_args()
    asyncio.run(main_async(args.graph_dir))


if __name__ == "__main__":
    main()
