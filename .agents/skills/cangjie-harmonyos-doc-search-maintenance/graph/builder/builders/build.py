"""图谱操作：合并/去重/聚类/分层/保存/加载。
实际提取由 doc/ 和 code/ 模块负责。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
import networkx as nx


def _normalize_id(s: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    return cleaned.strip("_").lower()


def build_from_json(extraction: dict, *, directed: bool = False) -> nx.Graph:
    """从提取结果 dict 构建 NetworkX 图。"""
    if "edges" not in extraction and "links" in extraction:
        extraction = dict(extraction, edges=extraction["links"])

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
        G.add_edge(src, tgt, **attrs)
    hyperedges = extraction.get("hyperedges", [])
    if hyperedges:
        G.graph["hyperedges"] = hyperedges
    return G


def _norm_label(label: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", label.lower()).strip()


def deduplicate_by_label(nodes: list[dict], edges: list[dict]) -> tuple[list[dict], list[dict]]:
    """基于 label 去重节点。"""
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

    print(f"[build] Deduplicated {len(remap)} duplicate node(s) by label.")
    deduped_nodes = list(canonical.values())
    deduped_edges = []
    for edge in edges:
        e = dict(edge)
        e["source"] = remap.get(e["source"], e["source"])
        e["target"] = remap.get(e["target"], e["target"])
        if e["source"] != e["target"]:
            deduped_edges.append(e)
    return deduped_nodes, deduped_edges


def annotate_layers(G: nx.Graph) -> None:
    """为节点标注层级（L1 概念层、L2 API 层、L3 实现层）。"""
    L1_KEYWORDS = {"overview", "guide", "tutorial", "概览", "指南", "介绍"}
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


def save_graph(G: nx.Graph, output_path: str | Path) -> None:
    from networkx.readwrite import json_graph as _jg

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = _jg.node_link_data(G, edges="links")
    data["input_tokens"] = G.graph.get("input_tokens", 0)
    data["output_tokens"] = G.graph.get("output_tokens", 0)

    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Graph saved: {output_path} ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


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
    """合并多个独立图谱文件。"""
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


def build_subgraph(
    doc_nodes: dict, doc_neighbors: dict,
    code_nodes: dict, code_neighbors: dict,
    *,
    directed: bool = False,
) -> nx.Graph:
    """从 doc/ 和 code/ 的提取结果构建 NetworkX 子图。"""
    all_nodes: list[dict] = []
    all_edges: list[dict] = []

    for nid, node in doc_nodes.items():
        d = node.to_dict() if hasattr(node, 'to_dict') else node
        all_nodes.append(d)
    for nid, nbrs in doc_neighbors.items():
        for tgt, rel in nbrs:
            all_edges.append({"source": nid, "target": tgt, "relation": rel})

    for nid, node in code_nodes.items():
        d = node.to_dict() if hasattr(node, 'to_dict') else node
        all_nodes.append(d)
    for nid, nbrs in code_neighbors.items():
        for tgt, rel in nbrs:
            all_edges.append({"source": nid, "target": tgt, "relation": rel})

    extraction = {"nodes": all_nodes, "edges": all_edges}
    return build_from_json(extraction, directed=directed)
