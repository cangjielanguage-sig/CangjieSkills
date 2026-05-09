"""GRAPH_REPORT.md 生成。整合自 graphify/report.py"""
from __future__ import annotations
from pathlib import Path
import networkx as nx


def generate_report(
    G: nx.Graph,
    communities: dict[int, list[str]],
    community_labels: dict[int, str] = {},
    output_path: str = "GRAPH_REPORT.md",
    input_tokens: int = 0,
    output_tokens: int = 0,
    corpus_path: str = "",
) -> None:
    from analysis.analyze import god_nodes, surprising_connections, suggest_questions
    from builders.cluster import cohesion_score

    god = god_nodes(G, top_n=10)
    surprises = surprising_connections(G, communities, top_n=5)
    questions = suggest_questions(G, communities, community_labels, top_n=7)

    lines = []
    lines.append("# Knowledge Graph Report")
    lines.append("")
    lines.append(f"**Nodes:** {G.number_of_nodes()}")
    lines.append(f"**Edges:** {G.number_of_edges()}")
    lines.append(f"**Communities:** {len(communities)}")
    if input_tokens or output_tokens:
        lines.append(f"**Input tokens:** {input_tokens:,}")
        lines.append(f"**Output tokens:** {output_tokens:,}")
    lines.append("")

    lines.append("## God Nodes (Most Connected)")
    lines.append("")
    lines.append("These nodes are the core abstractions of the knowledge graph:")
    lines.append("")
    for i, n in enumerate(god, 1):
        lines.append(f"{i}. `{n['label']}` - {n['degree']} edges")
    lines.append("")

    lines.append("## Surprising Connections")
    lines.append("")
    lines.append("Cross-community edges that bridge distant parts of the graph:")
    lines.append("")
    for s in surprises:
        lines.append(f"- `{s['source']}` ↔ `{s['target']}` - {s['relation']} [{s['confidence']}]")
        if "why" in s:
            lines.append(f"  - {s['why']}")
    lines.append("")

    lines.append("## Communities")
    lines.append("")
    for cid, nodes in sorted(communities.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        label = community_labels.get(cid, f"Community {cid}")
        coh = cohesion_score(G, nodes)
        lines.append(f"- **{label}** ({len(nodes)} nodes, cohesion: {coh})")
    lines.append("")

    lines.append("## Suggested Questions")
    lines.append("")
    for q in questions:
        if q["question"]:
            lines.append(f"- {q['question']}")
            lines.append(f"  - {q['why']}")
    lines.append("")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")


def load_report(path: str) -> dict:
    content = Path(path).read_text(encoding="utf-8")
    result = {
        "nodes": 0,
        "edges": 0,
        "communities": 0,
        "god_nodes": [],
        "surprises": [],
    }
    import re
    nodes_match = re.search(r"\*\*Nodes:\*\* (\d+)", content)
    if nodes_match:
        result["nodes"] = int(nodes_match.group(1))
    edges_match = re.search(r"\*\*Edges:\*\* (\d+)", content)
    if edges_match:
        result["edges"] = int(edges_match.group(1))
    return result