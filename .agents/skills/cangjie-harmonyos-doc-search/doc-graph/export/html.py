"""HTML可视化导出。整合自 graphify/export.py"""
from __future__ import annotations
import html as _html
import json
import re
from pathlib import Path
import networkx as nx


COMMUNITY_COLORS = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
]

MAX_NODES_FOR_VIZ = 5_000


def sanitize_label(label: str) -> str:
    return re.sub(r'[<>&"\']', '', str(label))


def _node_community_map(communities: dict[int, list[str]]) -> dict[str, int]:
    return {n: cid for cid, nodes in communities.items() for n in nodes}


def _html_styles() -> str:
    return """<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #0f0f1a; color: #e0e0e0; font-family: -apple-system, sans-serif; display: flex; height: 100vh; }
  #graph { flex: 1; }
  #sidebar { width: 280px; background: #1a1a2e; border-left: 1px solid #2a2a4e; overflow: hidden; }
  #search-wrap { padding: 12px; }
  #search { width: 100%; background: #0f0f1a; border: 1px solid #3a3a5e; color: #e0e0e0; padding: 7px; border-radius: 6px; }
  #info-panel { padding: 14px; min-height: 140px; }
  #legend-wrap { flex: 1; overflow-y: auto; padding: 12px; }
  .legend-item { display: flex; align-items: center; gap: 8px; padding: 4px 0; cursor: pointer; }
  .legend-dot { width: 12px; height: 12px; border-radius: 50%; }
</style>"""


def _html_script(nodes_json: str, edges_json: str, legend_json: str) -> str:
    return f"""<script>
var RAW_NODES = {nodes_json};
var RAW_EDGES = {edges_json};
var LEGEND = {legend_json};

var nodesDS = new vis.DataSet(RAW_NODES.map(function(n) {{
  return {{
    id: n.id, label: n.label, color: n.color, size: n.size,
    font: n.font, title: n.title, _community: n.community
  }};
}}));

var edgesDS = new vis.DataSet(RAW_EDGES.map(function(e, i) {{
  return {{
    id: i, from: e.from, to: e.to, title: e.title,
    dashes: e.dashes, width: e.width, color: e.color,
    arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }}
  }};
}}));

var network = new vis.Network(document.getElementById('graph'),
  {{ nodes: nodesDS, edges: edgesDS }},
  {{
    physics: {{ solver: 'forceAtlas2Based', stabilization: {{ iterations: 200 }} }},
    nodes: {{ shape: 'dot', borderWidth: 1.5 }}
  }});

function showInfo(nodeId) {{
  var n = nodesDS.get(nodeId);
  var neighbors = network.getConnectedNodes(nodeId);
  document.getElementById('info-content').innerHTML =
    '<div><b>' + n.label + '</b></div>' +
    '<div>Community: ' + n._community + '</div>' +
    '<div>Neighbors: ' + neighbors.length + '</div>';
}}

network.on('click', function(params) {{
  if (params.nodes.length > 0) showInfo(params.nodes[0]);
}});
</script>"""


def to_html(
    G: nx.Graph,
    communities: dict[int, list[str]],
    output_path: str,
    community_labels: dict[int, str] | None = None,
) -> None:
    if G.number_of_nodes() > MAX_NODES_FOR_VIZ:
        raise ValueError(f"Graph has {G.number_of_nodes()} nodes - too large for HTML viz")

    node_community = _node_community_map(communities)
    degree = dict(G.degree())
    max_deg = max(degree.values(), default=1) or 1

    vis_nodes = []
    for node_id, data in G.nodes(data=True):
        cid = node_community.get(node_id, 0)
        color = COMMUNITY_COLORS[cid % len(COMMUNITY_COLORS)]
        label = sanitize_label(data.get("label", node_id))
        deg = degree.get(node_id, 1)
        size = 10 + 30 * (deg / max_deg)
        vis_nodes.append({
            "id": node_id,
            "label": label,
            "color": {"background": color, "border": color},
            "size": round(size, 1),
            "font": {"size": 12 if deg >= max_deg * 0.15 else 0, "color": "#ffffff"},
            "title": _html.escape(label),
            "community": cid,
        })

    vis_edges = []
    for u, v, data in G.edges(data=True):
        confidence = data.get("confidence", "EXTRACTED")
        relation = data.get("relation", "")
        vis_edges.append({
            "from": u,
            "to": v,
            "title": _html.escape(f"{relation} [{confidence}]"),
            "dashes": confidence != "EXTRACTED",
            "width": 2 if confidence == "EXTRACTED" else 1,
            "color": {"opacity": 0.7 if confidence == "EXTRACTED" else 0.35},
        })

    legend_data = []
    for cid in sorted((community_labels or {}).keys()):
        color = COMMUNITY_COLORS[cid % len(COMMUNITY_COLORS)]
        lbl = _html.escape(sanitize_label((community_labels or {}).get(cid, f"Community {cid}")))
        legend_data.append({"cid": cid, "color": color, "label": lbl, "count": len(communities.get(cid, []))})

    def _js_safe(obj) -> str:
        return json.dumps(obj).replace("</", "<\\/")

    nodes_json = _js_safe(vis_nodes)
    edges_json = _js_safe(vis_edges)
    legend_json = _js_safe(legend_data)
    title = _html.escape(sanitize_label(str(output_path)))
    stats = f"{G.number_of_nodes()} nodes · {G.number_of_edges()} edges · {len(communities)} communities"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>graphify - {title}</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
{_html_styles()}
</head>
<body>
<div id="graph"></div>
<div id="sidebar">
  <div id="search-wrap"><input id="search" type="text" placeholder="Search..." autocomplete="off"></div>
  <div id="info-panel"><h3>Node Info</h3><div id="info-content"><span>Click a node</span></div></div>
  <div id="legend-wrap"><h3>Communities</h3><div id="legend"></div></div>
  <div style="padding:10px;font-size:11px;color:#555">{stats}</div>
</div>
{_html_script(nodes_json, edges_json, legend_json)}
</body>
</html>"""

    Path(output_path).write_text(html_content, encoding="utf-8")


generate_html = to_html