"""文档图谱构建器。"""
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from core.models import DocNode, Edge
from graph.doc.extractor import extract_doc_node, extract_overview_nodes


def detect_files(root_dir: Path) -> tuple[list[Path], list[Path]]:
    """扫描文档目录，返回 (overview 文件列表, 普通 md 文件列表)。"""
    overviews = []
    docs = []
    # 获取顶层子目录名（如 harmonyos-6.0.2-15k, std, stdx 等）
    top_level_dirs = {d.name for d in root_dir.iterdir() if d.is_dir()}
    for f in root_dir.rglob("*.md"):
        if f.name.startswith(".overview"):
            # 排除顶层目录的 .overview.md（如 harmonyos-6.0.2-15k/.overview.md）
            parent_name = f.parent.name
            if parent_name in top_level_dirs:
                continue
            overviews.append(f)
        elif not f.name.startswith(".abstract"):
            docs.append(f)
    return overviews, docs


def build_doc_graph(root_dir: Path, use_cache: bool = True) -> tuple[dict[str, DocNode], dict[str, list[tuple[str, str]]]]:
    """构建文档图谱。返回 (nodes, neighbors)。"""
    overviews, docs = detect_files(root_dir)
    all_files = overviews + docs
    
    nodes: dict[str, DocNode] = {}
    edges: list[Edge] = []

    if use_cache:
        from graph.builders.cache import check_semantic_cache, save_semantic_cache
        
        file_paths = [str(f) for f in all_files]
        cached_nodes_list, cached_edges_list, _, uncached_files = check_semantic_cache(file_paths, root_dir)
        
        print(f"  缓存命中: {len(cached_nodes_list)} 节点, {len(cached_edges_list)} 边")
        print(f"  待处理文件: {len(uncached_files)}")

        # 加载缓存结果
        for node_dict in cached_nodes_list:
            node = DocNode.from_dict(node_dict)
            nodes[node.id] = node
        
        for edge_dict in cached_edges_list:
            edges.append(Edge(
                source=edge_dict["source"], target=edge_dict["target"],
                relation=edge_dict["relation"], source_file=edge_dict.get("source_file", "")
            ))

        # 处理未缓存文件
        new_nodes_list = []
        new_edges_list = []

        for fpath_str in uncached_files:
            fpath = Path(fpath_str)
            # 判断是 overview 还是 doc
            is_overview = fpath in overviews
            
            if is_overview:
                ov_nodes, ov_edges = extract_overview_nodes(fpath, root_dir)
                for n in ov_nodes:
                    nodes[n.id] = n
                    new_nodes_list.append(n.to_dict())
                edges.extend(ov_edges)
                new_edges_list.extend([e.to_dict() for e in ov_edges])
                
                if not ov_nodes:
                    from graph.builders.cache import save_cached
                    save_cached(fpath, {"nodes": [], "edges": []}, root_dir)
            else:
                result = extract_doc_node(fpath, root_dir)
                if result:
                    node, doc_edges = result
                    nodes[node.id] = node
                    new_nodes_list.append(node.to_dict())
                    edges.extend(doc_edges)
                    new_edges_list.extend([e.to_dict() for e in doc_edges])
                else:
                    # 缓存空结果，避免下次重复检查
                    from graph.builders.cache import save_cached
                    save_cached(fpath, {"nodes": [], "edges": []}, root_dir)
        
        if new_nodes_list:
            save_semantic_cache(new_nodes_list, new_edges_list, root=root_dir)
            print(f"  已缓存: {len(new_nodes_list)} 节点")
    else:
        # 全量构建逻辑 (原有逻辑)
        # 1. 提取 overview 节点
        for ov_path in overviews:
            ov_nodes, ov_edges = extract_overview_nodes(ov_path, root_dir)
            for n in ov_nodes:
                nodes[n.id] = n
            edges.extend(ov_edges)

        # 2. 提取普通文档节点
        for doc_path in docs:
            result = extract_doc_node(doc_path, root_dir)
            if result is None:
                continue
            node, doc_edges = result
            nodes[node.id] = node
            edges.extend(doc_edges)

    # 3. 构建邻居索引
    neighbors: dict[str, list[tuple[str, str]]] = {nid: [] for nid in nodes}
    for edge in edges:
        if edge.source in nodes and edge.target in nodes:
            neighbors[edge.source].append((edge.target, edge.relation))
            neighbors[edge.target].append((edge.source, edge.relation))

    # 4. 计算 degree
    for nid in nodes:
        nodes[nid].degree = len(neighbors[nid])

    return nodes, neighbors


def build_doc_nx_graph(
    nodes: dict[str, DocNode],
    neighbors: dict[str, list[tuple[str, str]]],
    *,
    directed: bool = False,
) -> nx.Graph:
    """将 (DocNode, 邻接表) 转为标准 NetworkX 图（node_link_data 兼容格式）。"""
    from graph.builders.build import build_subgraph

    return build_subgraph(nodes, neighbors, {}, {}, directed=directed)
