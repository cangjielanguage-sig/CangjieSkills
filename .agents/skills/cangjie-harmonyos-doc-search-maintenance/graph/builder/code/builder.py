"""源码图谱构建器。"""
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from core.models import CodeNode, Edge
from code.extractor import collect_files, extract_files


def detect_code_files(root_dir: Path) -> list[Path]:
    """扫描源码目录，返回支持的语言文件列表。"""
    return collect_files(root_dir)


def build_code_graph(root_dir: Path) -> tuple[dict[str, CodeNode], dict[str, list[tuple[str, str]]]]:
    """构建源码图谱。返回 (nodes, neighbors)。"""
    code_files = detect_code_files(root_dir)

    nodes_list, edges_list = extract_files(code_files, root_dir)

    nodes: dict[str, CodeNode] = {}
    for n in nodes_list:
        nodes[n.id] = n

    # 构建邻居索引
    neighbors: dict[str, list[tuple[str, str]]] = {nid: [] for nid in nodes}
    for edge in edges_list:
        src = edge.source if hasattr(edge, 'source') else edge['source']
        tgt = edge.target if hasattr(edge, 'target') else edge['target']
        rel = edge.relation if hasattr(edge, 'relation') else edge.get('relation', 'uses')
        if src in nodes and tgt in nodes:
            neighbors[src].append((tgt, rel))
            neighbors[tgt].append((src, rel))

    # 计算 degree
    for nid in nodes:
        nodes[nid].degree = len(neighbors[nid])

    return nodes, neighbors


def build_code_nx_graph(
    nodes: dict[str, CodeNode],
    neighbors: dict[str, list[tuple[str, str]]],
    *,
    directed: bool = False,
) -> nx.Graph:
    """将 (CodeNode, 邻接表) 转为标准 NetworkX 图（node_link_data 兼容格式）。"""
    from builders.build import build_subgraph

    return build_subgraph({}, {}, nodes, neighbors, directed=directed)
