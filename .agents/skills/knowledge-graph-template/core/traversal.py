"""图遍历模块。整合 graphify serve.py 的 BFS/DFS 遍历逻辑。"""
from __future__ import annotations
import unicodedata
import networkx as nx
from typing import Optional
from dataclasses import dataclass, field


def _strip_diacritics(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def score_nodes(G: nx.Graph, terms: list[str]) -> list[tuple[float, str]]:
    scored = []
    norm_terms = [_strip_diacritics(t).lower() for t in terms]
    for nid, data in G.nodes(data=True):
        norm_label = data.get("norm_label") or _strip_diacritics(data.get("label") or "").lower()
        source = (data.get("source_file") or "").lower()
        score = sum(1 for t in norm_terms if t in norm_label) + sum(0.5 for t in norm_terms if t in source)
        if score > 0:
            scored.append((score, nid))
    return sorted(scored, reverse=True)


def bfs_traverse(G: nx.Graph, start_nodes: list[str], depth: int) -> tuple[set[str], list[tuple]]:
    visited: set[str] = set(start_nodes)
    frontier = set(start_nodes)
    edges_seen: list[tuple] = []
    for _ in range(depth):
        next_frontier: set[str] = set()
        for n in frontier:
            for neighbor in G.neighbors(n):
                if neighbor not in visited:
                    next_frontier.add(neighbor)
                    edges_seen.append((n, neighbor))
        visited.update(next_frontier)
        frontier = next_frontier
    return visited, edges_seen


def dfs_traverse(G: nx.Graph, start_nodes: list[str], depth: int) -> tuple[set[str], list[tuple]]:
    visited: set[str] = set()
    edges_seen: list[tuple] = []
    stack = [(n, 0) for n in reversed(start_nodes)]
    while stack:
        node, d = stack.pop()
        if node in visited or d > depth:
            continue
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                stack.append((neighbor, d + 1))
                edges_seen.append((node, neighbor))
    return visited, edges_seen


def find_nodes_by_label(G: nx.Graph, label: str) -> list[str]:
    term = _strip_diacritics(label).lower()
    return [nid for nid, d in G.nodes(data=True)
            if term in (d.get("norm_label") or _strip_diacritics(d.get("label") or "").lower())
            or term == nid.lower()]


@dataclass
class TraverseResult:
    query: str
    mode: str
    start_nodes: list[str]
    depth: int
    nodes: list[dict] = field(default_factory=list)
    edges: list[dict] = field(default_factory=list)
    token_budget: int = 2000
    actual_tokens: int = 0
    subgraph_json: str = ""
    graph_name: str = ""


def traverse(
    G: nx.Graph,
    query: str,
    mode: str = "bfs",
    depth: int = 3,
    token_budget: int = 2000,
    graph_name: str = "",
) -> TraverseResult:
    terms = [t.lower() for t in query.split() if len(t) > 2]
    scored = score_nodes(G, terms)
    start_nodes = [nid for _, nid in scored[:3]]
    
    if not start_nodes:
        return TraverseResult(
            query=query,
            mode=mode,
            start_nodes=[],
            depth=depth,
            nodes=[],
            edges=[],
            graph_name=graph_name,
        )
    
    nodes_set, edges_list = dfs_traverse(G, start_nodes, depth) if mode == "dfs" else bfs_traverse(G, start_nodes, depth)
    
    nodes_data = []
    for nid in sorted(nodes_set, key=lambda n: G.degree(n), reverse=True):
        d = G.nodes[nid]
        nodes_data.append({
            "id": nid,
            "label": d.get("label", nid),
            "source_file": d.get("source_file", ""),
            "source_location": d.get("source_location", ""),
            "community": d.get("community", ""),
            "layer": d.get("layer", 3),
            "degree": G.degree(nid),
        })
    
    edges_data = []
    for u, v in edges_list:
        if u in nodes_set and v in nodes_set:
            raw = G[u][v]
            d = raw if not isinstance(G, (nx.MultiGraph, nx.MultiDiGraph)) else next(iter(raw.values()), {})
            edges_data.append({
                "source": u,
                "target": v,
                "source_label": G.nodes[u].get("label", u),
                "target_label": G.nodes[v].get("label", v),
                "relation": d.get("relation", ""),
                "confidence": d.get("confidence", ""),
            })
    
    import json
    subgraph_json = json.dumps({"nodes": nodes_data, "edges": edges_data}, ensure_ascii=False)
    actual_tokens = len(subgraph_json) // 3
    
    if actual_tokens > token_budget:
        nodes_data = nodes_data[:token_budget // 100]
        edges_data = edges_data[:token_budget // 50]
        subgraph_json = json.dumps({"nodes": nodes_data, "edges": edges_data}, ensure_ascii=False)
        actual_tokens = len(subgraph_json) // 3
    
    return TraverseResult(
        query=query,
        mode=mode,
        start_nodes=[G.nodes[n].get("label", n) for n in start_nodes],
        depth=depth,
        nodes=nodes_data,
        edges=edges_data,
        token_budget=token_budget,
        actual_tokens=actual_tokens,
        subgraph_json=subgraph_json,
        graph_name=graph_name,
    )


def traverse_text(result: TraverseResult) -> str:
    lines = [
        f"Traversal: {result.mode.upper()} depth={result.depth}",
        f"| Start: {result.start_nodes}",
        f"| {len(result.nodes)} nodes found",
        f"| Graph: {result.graph_name}",
        "",
    ]
    
    for node in result.nodes:
        lines.append(
            f"NODE {node['label']} "
            f"[src={node['source_file']} loc={node['source_location']} "
            f"layer={node['layer']} community={node['community']}]"
        )
    
    for edge in result.edges:
        conf_str = f" [{edge['confidence']}]" if edge['confidence'] else ""
        lines.append(
            f"EDGE {edge['source_label']} --{edge['relation']}{conf_str}--> {edge['target_label']}"
        )
    
    if result.actual_tokens > result.token_budget:
        lines.append(f"... (truncated to ~{result.token_budget} token budget)")
    
    return "\n".join(lines)


def god_nodes(G: nx.Graph, top_n: int = 10) -> list[dict]:
    degree_sorted = sorted(G.nodes(), key=lambda n: G.degree(n), reverse=True)[:top_n]
    return [
        {
            "id": n,
            "label": G.nodes[n].get("label", n),
            "degree": G.degree(n),
            "source_file": G.nodes[n].get("source_file", ""),
        }
        for n in degree_sorted
    ]


def surprising_connections(G: nx.Graph, top_n: int = 5) -> list[dict]:
    from collections import defaultdict
    
    community_edges: dict[int, int] = defaultdict(int)
    cross_community_edges: list[tuple] = []
    
    for u, v in G.edges():
        u_comm = G.nodes[u].get("community", -1)
        v_comm = G.nodes[v].get("community", -1)
        if u_comm == v_comm:
            community_edges[u_comm] += 1
        else:
            cross_community_edges.append((u, v, u_comm, v_comm))
    
    cross_community_edges.sort(key=lambda e: min(G.degree(e[0]), G.degree(e[1])), reverse=True)
    
    return [
        {
            "source": u,
            "source_label": G.nodes[u].get("label", u),
            "source_community": u_comm,
            "target": v,
            "target_label": G.nodes[v].get("label", v),
            "target_community": v_comm,
            "relation": G[u][v].get("relation", ""),
        }
        for u, v, u_comm, v_comm in cross_community_edges[:top_n]
    ]


def suggest_questions(G: nx.Graph, top_n: int = 7) -> list[dict]:
    high_degree = god_nodes(G, top_n=top_n)
    cross_edges = surprising_connections(G, top_n=min(3, top_n))
    
    questions = []
    
    for node in high_degree:
        questions.append({
            "question": f"What does {node['label']} relate to?",
            "rationale": f"Core abstraction with {node['degree']} connections",
            "target_node": node["id"],
        })
    
    for edge in cross_edges:
        questions.append({
            "question": f"How does {edge['source_label']} connect to {edge['target_label']}?",
            "rationale": f"Cross-community connection (communities {edge['source_community']} ↔ {edge['target_community']})",
            "target_nodes": [edge["source"], edge["target"]],
        })
    
    return questions[:top_n]


def community_info(G: nx.Graph, community_id: int) -> dict:
    nodes = [n for n, d in G.nodes(data=True) if d.get("community") == community_id]
    if not nodes:
        return {"error": f"Community {community_id} not found"}
    
    cohesion = 0.0
    if len(nodes) > 1:
        subgraph = G.subgraph(nodes)
        actual = subgraph.number_of_edges()
        possible = len(nodes) * (len(nodes) - 1) / 2
        cohesion = round(actual / possible, 2) if possible > 0 else 0.0
    
    top_nodes = sorted(nodes, key=lambda n: G.degree(n), reverse=True)[:5]
    
    return {
        "community_id": community_id,
        "node_count": len(nodes),
        "cohesion": cohesion,
        "top_nodes": [
            {"id": n, "label": G.nodes[n].get("label", n), "degree": G.degree(n)}
            for n in top_nodes
        ],
        "all_nodes": nodes,
    }