"""构建 NetworkX 图谱。整合自 graphify/build.py，包含验证功能。"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
import networkx as nx
from .validate import validate_extraction


def _normalize_id(s: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    return cleaned.strip("_").lower()


def build_from_json(extraction: dict, *, directed: bool = False) -> nx.Graph:
    """Build a NetworkX graph from an extraction dict.

    directed=True produces a DiGraph that preserves edge direction (source→target).
    directed=False (default) produces an undirected Graph for backward compatibility.
    """
    if "edges" not in extraction and "links" in extraction:
        extraction = dict(extraction, edges=extraction["links"])

    for node in extraction.get("nodes", []):
        if isinstance(node, dict) and "source" in node and "source_file" not in node:
            node_id = node.get("id", "?")
            affected_edges = sum(
                1 for e in extraction.get("edges", [])
                if e.get("source") == node_id or e.get("target") == node_id
            )
            print(
                f"[graphify] WARNING: node '{node_id}' uses field 'source' instead of "
                f"'source_file' — {affected_edges} edge(s) may be misrouted.",
                file=sys.stderr,
            )
            node["source_file"] = node.pop("source")

    errors = validate_extraction(extraction)
    real_errors = [e for e in errors if "does not match any node id" not in e]
    if real_errors:
        print(f"[graphify] Extraction warning ({len(real_errors)} issues): {real_errors[0]}", file=sys.stderr)

    G: nx.Graph = nx.DiGraph() if directed else nx.Graph()
    for node in extraction.get("nodes", []):
        G.add_node(node["id"], **{k: v for k, v in node.items() if k != "id"})
    node_set = set(G.nodes())
    norm_to_id: dict[str, str] = {_normalize_id(nid): nid for nid in node_set}
    for edge in extraction.get("edges", []):
        if "source" not in edge and "from" in edge:
            edge["source"] = edge["from"]
        if "target" not in edge and "to" in edge:
            edge["target"] = edge["to"]
        if "source" not in edge or "target" not in edge:
            continue
        src, tgt = edge["source"], edge["target"]
        if src not in node_set:
            src = norm_to_id.get(_normalize_id(src), src)
        if tgt not in node_set:
            tgt = norm_to_id.get(_normalize_id(tgt), tgt)
        if src not in node_set or tgt not in node_set:
            continue
        attrs = {k: v for k, v in edge.items() if k not in ("source", "target")}
        attrs["_src"] = src
        attrs["_tgt"] = tgt
        G.add_edge(src, tgt, **attrs)
    hyperedges = extraction.get("hyperedges", [])
    if hyperedges:
        G.graph["hyperedges"] = hyperedges
    return G


def build(extractions: list[dict], *, directed: bool = False) -> nx.Graph:
    combined: dict = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
    for ext in extractions:
        combined["nodes"].extend(ext.get("nodes", []))
        combined["edges"].extend(ext.get("edges", []))
        combined["hyperedges"].extend(ext.get("hyperedges", []))
        combined["input_tokens"] += ext.get("input_tokens", 0)
        combined["output_tokens"] += ext.get("output_tokens", 0)
    return build_from_json(combined, directed=directed)


def _norm_label(label: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", label.lower()).strip()


def deduplicate_by_label(nodes: list[dict], edges: list[dict]) -> tuple[list[dict], list[dict]]:
    _CHUNK_SUFFIX = re.compile(r"_c\d+$")
    canonical: dict[str, dict] = {}
    remap: dict[str, str] = {}

    for node in nodes:
        key = _norm_label(node.get("label", node.get("id", "")))
        if not key:
            continue
        existing = canonical.get(key)
        if existing is None:
            canonical[key] = node
        else:
            has_suffix = bool(_CHUNK_SUFFIX.search(node["id"]))
            existing_has_suffix = bool(_CHUNK_SUFFIX.search(existing["id"]))
            if has_suffix and not existing_has_suffix:
                remap[node["id"]] = existing["id"]
            elif existing_has_suffix and not has_suffix:
                remap[existing["id"]] = node["id"]
                canonical[key] = node
            elif len(node["id"]) < len(existing["id"]):
                remap[existing["id"]] = node["id"]
                canonical[key] = node
            else:
                remap[node["id"]] = existing["id"]

    if not remap:
        return nodes, edges

    print(f"[graphify] Deduplicated {len(remap)} duplicate node(s) by label.", file=sys.stderr)
    deduped_nodes = list(canonical.values())
    deduped_edges = []
    for edge in edges:
        e = dict(edge)
        e["source"] = remap.get(e["source"], e["source"])
        e["target"] = remap.get(e["target"], e["target"])
        if e["source"] != e["target"]:
            deduped_edges.append(e)
    return deduped_nodes, deduped_edges


def build_merge(
    new_chunks: list[dict],
    graph_path: str | Path = "graphify-out/graph.json",
    prune_sources: list[str] | None = None,
    *,
    directed: bool = False,
) -> nx.Graph:
    from networkx.readwrite import json_graph as _jg

    graph_path = Path(graph_path)
    if graph_path.exists():
        data = json.loads(graph_path.read_text(encoding="utf-8"))
        try:
            existing_G = _jg.node_link_graph(data, edges="links")
        except TypeError:
            existing_G = _jg.node_link_graph(data)
        existing_nodes = [{"id": n, **existing_G.nodes[n]} for n in existing_G.nodes]
        existing_edges = [
            {"source": u, "target": v, **d} for u, v, d in existing_G.edges(data=True)
        ]
        base = [{"nodes": existing_nodes, "edges": existing_edges}]
    else:
        base = []

    all_chunks = base + list(new_chunks)
    G = build(all_chunks, directed=directed)

    if prune_sources:
        to_remove = [
            n for n, d in G.nodes(data=True)
            if d.get("source_file") in prune_sources
        ]
        G.remove_nodes_from(to_remove)
        if to_remove:
            print(f"[graphify] Pruned {len(to_remove)} node(s) from deleted sources.", file=sys.stderr)

    if graph_path.exists():
        existing_n = len(existing_nodes)
        new_n = G.number_of_nodes()
        if new_n < existing_n:
            raise ValueError(
                f"graphify: build_merge would shrink graph from {existing_n} → {new_n} nodes. "
                f"Pass prune_sources explicitly if you intend to remove nodes."
            )

    return G


def save_graph(G: nx.Graph, output_path: str | Path) -> None:
    from networkx.readwrite import json_graph as _jg
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    data = _jg.node_link_data(G, edges="links")
    data["input_tokens"] = G.graph.get("input_tokens", 0)
    data["output_tokens"] = G.graph.get("output_tokens", 0)
    
    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Graph saved: {output_path} ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


def annotate_layers(G: nx.Graph) -> None:
    """为节点标注层级（L1 概念层、L2 API 层、L3 实现层）。
    
    标注规则：
    - L1（概念层）: 文档节点、概述性节点、指南节点
    - L2（API 层）: 类/接口/组件/枚举定义
    - L3（实现层）: 函数/方法/属性/代码片段
    
    优先使用已有 layer 属性，否则根据节点特征推断。
    """
    L1_KEYWORDS = {"overview", "guide", "tutorial", "概览", "指南", "介绍", "overview", "guide"}
    L2_KEYWORDS = {"class", "interface", "struct", "enum", "component", "api", "reference"}
    
    for node_id, data in G.nodes(data=True):
        if data.get("layer") is not None:
            continue
        
        file_type = data.get("file_type", "") or ""
        label = (data.get("label", "") or "").lower()
        source_file = (data.get("source_file", "") or "").lower()
        
        if file_type == "document":
            if any(k in source_file or k in label for k in L1_KEYWORDS):
                data["layer"] = 1
            elif "api" in source_file or "reference" in source_file:
                data["layer"] = 2
            else:
                data["layer"] = 1
        elif file_type == "code":
            if any(k in label for k in L2_KEYWORDS):
                data["layer"] = 2
            elif "(" in label or "." in label:
                data["layer"] = 3
            else:
                data["layer"] = 2
        else:
            data["layer"] = 3


def load_graph(graph_path: str | Path) -> nx.Graph:
    """加载图谱 JSON 文件。"""
    from networkx.readwrite import json_graph as _jg
    
    graph_path = Path(graph_path)
    data = json.loads(graph_path.read_text(encoding="utf-8"))
    
    try:
        G = _jg.node_link_graph(data, edges="links")
    except TypeError:
        G = _jg.node_link_graph(data)
    
    return G


def merge_graphs(
    graph_paths: list[str | Path],
    output_path: str | Path,
    *,
    deduplicate: bool = True,
    recluster: bool = True,
    annotate: bool = True,
    directed: bool = False,
) -> nx.Graph:
    """合并多个独立图谱文件。
    
    Args:
        graph_paths: 图谱文件路径列表
        output_path: 合并后的输出路径
        deduplicate: 是否去重（基于 label）
        recluster: 是否重新聚类
        annotate: 是否标注层级
        directed: 是否生成有向图
    
    Returns:
        合并后的 NetworkX 图
    
    Example:
        merge_graphs(
            ["data/api/graph.json", "data/core/graph.json", "data/ui/graph.json"],
            "data/merged/graph.json"
        )
    """
    from .cluster import cluster, assign_communities_to_nodes
    
    graph_paths = [Path(p) for p in graph_paths]
    output_path = Path(output_path)
    
    print(f"\n合并图谱:")
    for p in graph_paths:
        print(f"  - {p}")
    
    all_nodes: list[dict] = []
    all_edges: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0
    
    for graph_path in graph_paths:
        if not graph_path.exists():
            print(f"  警告: 跳过不存在文件 {graph_path}")
            continue
        
        data = json.loads(graph_path.read_text(encoding="utf-8"))
        
        nodes = data.get("nodes", [])
        edges = data.get("links", []) if "links" in data else data.get("edges", [])
        
        print(f"  {graph_path.name}: {len(nodes)} 节点, {len(edges)} 边")
        
        all_nodes.extend(nodes)
        all_edges.extend(edges)
        total_input_tokens += data.get("input_tokens", 0)
        total_output_tokens += data.get("output_tokens", 0)
    
    if deduplicate:
        print(f"\n去重前: {len(all_nodes)} 节点")
        all_nodes, all_edges = deduplicate_by_label(all_nodes, all_edges)
        print(f"去重后: {len(all_nodes)} 节点")
    
    extraction = {
        "nodes": all_nodes,
        "edges": all_edges,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
    }
    
    G = build_from_json(extraction, directed=directed)
    
    print(f"\n合并图谱: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")
    
    if recluster:
        print("\n聚类...")
        communities = cluster(G)
        assign_communities_to_nodes(G, communities)
        print(f"  社区: {len(communities)}")
    
    if annotate:
        annotate_layers(G)
    
    G.graph["input_tokens"] = total_input_tokens
    G.graph["output_tokens"] = total_output_tokens
    
    save_graph(G, output_path)
    print(f"\n完成！合并图谱保存至: {output_path}")
    
    return G