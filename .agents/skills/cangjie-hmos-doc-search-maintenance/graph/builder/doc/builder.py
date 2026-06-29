"""文档图谱构建器。

本模块是文档图谱构建流水线的编排层，将 extractor.py 提取的节点和边
转换为 dict[str, DocNode] + 邻接表格式，供 builders/build.py 构建 NetworkX 图。

支持缓存模式（use_cache=True）：基于 semantic cache 避免重复提取，
仅处理新增或变更的文件，增量更新节点和边。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

import networkx as nx

from core.models import DocNode, Edge, EdgeRelation
from doc.extractor import extract_doc_node, extract_overview_nodes, safe_read_text, clean_id_stem, infer_category, build_namespace, detect_doc_type_from_path


def _find_node_by_source_file(source_file: str, nodes: dict[str, DocNode]) -> Optional[str]:
    """根据 source_file 在 nodes 中查找对应的 node_id。"""
    for nid, node in nodes.items():
        if node.source_file == source_file:
            return nid
    return None


def detect_files(root_dir: Path) -> tuple[list[Path], list[Path]]:
    """扫描文档目录，返回 (overview 文件列表, 普通 md 文件列表)。
    排除 root_dir 本身的 .overview.md（与具体模块无关），保留所有子目录的 .overview.md。"""
    overviews = []
    docs = []
    for f in root_dir.rglob("*.md"):
        if f.name.startswith(".overview"):
            if f.parent == root_dir:
                continue
            overviews.append(f)
        elif not f.name.startswith(".abstract"):
            docs.append(f)
    return overviews, docs


def build_doc_graph(root_dir: Path, use_cache: bool = True) -> tuple[dict[str, DocNode], dict[str, list[tuple[str, str]]]]:
    """构建文档图谱。返回 (nodes, neighbors) 字典。

    流程：
    1. 扫描文件（detect_files）
    2. 检查缓存 → 加载已缓存节点/边 → 处理未缓存文件
    3. 构建邻接索引（双向：源→目标 + 目标→源）
    4. 计算 degree（邻接数）

    neighbors 格式: node_id → list[(neighbor_id, relation)]
    """
    overviews, docs = detect_files(root_dir)
    all_files = overviews + docs
    
    nodes: dict[str, DocNode] = {}
    edges: list[Edge] = []

    if use_cache:
        from builders.cache import check_semantic_cache, save_semantic_cache
        
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
                    from builders.cache import save_cached
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
                    from builders.cache import save_cached
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

    # see_also 边解析：基于全局文件名匹配
    # Markdown 链接的目标文件名可能存在于语料中的其他目录，
    # 通过文件名全局查找可以恢复这层语义关联。
    fname_to_node_ids: dict[str, list[str]] = {}
    for nid, node in nodes.items():
        fname = Path(node.source_file).name
        fname_to_node_ids.setdefault(fname, []).append(nid)

    source_dir_to_node_ids: dict[str, list[str]] = {}
    for nid, node in nodes.items():
        parent = str(Path(node.source_file).parent)
        source_dir_to_node_ids.setdefault(parent, []).append(nid)

    see_also_count = 0
    for nid, node in nodes.items():
        doc_path = root_dir / node.source_file
        try:
            content = safe_read_text(doc_path)
        except Exception:
            continue

        md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        for link_text, link_target in md_links:
            if not link_target.endswith(".md"):
                continue
            if not (link_target.startswith("./") or "/" in link_target):
                continue
            target_file_raw = link_target.split("#")[0]
            if not target_file_raw:
                continue
            fname = Path(target_file_raw).name
            if fname.startswith("."):
                continue

            # 三级解析策略
            target_id = None

            # 1. 精确路径解析（同目录下直接存在）
            target_path = (doc_path.parent / target_file_raw).resolve()
            root_resolved = root_dir.resolve()
            try:
                target_rel = str(target_path.relative_to(root_resolved))
                target_id = _find_node_by_source_file(target_rel, nodes)
            except ValueError:
                pass

            # 2. 同目录优先的全局文件名匹配
            if not target_id:
                candidates = fname_to_node_ids.get(fname)
                if candidates:
                    src_parent = str(Path(node.source_file).parent)
                    same_dir_hits = [c for c in candidates if str(Path(nodes[c].source_file).parent) == src_parent]
                    if same_dir_hits:
                        target_id = same_dir_hits[0]
                    elif len(candidates) == 1:
                        target_id = candidates[0]

            # 3. 目录名匹配（./xxx.md -> 目录 xxx/ 下的同名 .md 文件）
            if not target_id:
                dirname = fname[:-3]
                inner_path = f"{dirname}/{fname}"
                target_id = _find_node_by_source_file(inner_path, nodes)

            if target_id and target_id != nid:
                edges.append(Edge(
                    source=nid, target=target_id,
                    relation=EdgeRelation.SEE_ALSO.value,
                    source_file=node.source_file,
                ))
                see_also_count += 1

    print(f"  see_also 边解析: {see_also_count} 条")

    # 邻接索引：双向记录，每条边同时出现在 source 和 target 的邻居列表中
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
    """将 (DocNode, 邻接表) 转为标准 NetworkX 图（node_link_data 兼容格式）。
    委托 builders.build.build_subgraph 实现，空 dict{} 表示无 code 节点/邻接。"""
    from builders.build import build_subgraph

    return build_subgraph(nodes, neighbors, {}, {}, directed=directed)
