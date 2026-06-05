"""图分析函数 — 基于社区和拓扑的核心节点、惊奇连接计算。

依赖 NetworkX，仅在 god-nodes/surprises 命令时按需加载。
"""

from __future__ import annotations

import networkx as nx


def god_nodes(G: nx.Graph, top_n: int = 10) -> list[dict]:
    """核心节点排行 — 按度（邻居数量）从高到低排序。

    返回 list[dict]，每个 dict 包含 label、degree、source_file、node_id。
    """
    degree = dict(G.degree())
    ranked = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result = []
    for nid, deg in ranked:
        ndata = G.nodes[nid]
        result.append({
            "node_id": nid,
            "label": ndata.get("label", nid),
            "degree": deg,
            "source_file": ndata.get("source_file", ""),
        })
    return result


def surprising_connections(
    G: nx.Graph,
    communities: dict[int, list[str]],
    top_n: int = 5,
) -> list[dict]:
    """惊奇连接 — 跨社区的边，代表不同知识领域之间的意外关联。

    遍历所有边，找出 source 和 target 属于不同社区的边，
    按边权重（如果有）或目标节点度排序，返回 top_n 个最意外的连接。
    """
    node_community: dict[str, int] = {}
    for cid, members in communities.items():
        for nid in members:
            node_community[nid] = cid

    cross_edges = []
    for src, tgt, edata in G.edges(data=True):
        src_cid = node_community.get(src, -1)
        tgt_cid = node_community.get(tgt, -1)
        if src_cid != tgt_cid and src_cid >= 0 and tgt_cid >= 0:
            weight = edata.get("weight", 0.5)
            cross_edges.append({
                "source_id": src,
                "source_label": G.nodes[src].get("label", src),
                "source_community": src_cid,
                "target_id": tgt,
                "target_label": G.nodes[tgt].get("label", tgt),
                "target_community": tgt_cid,
                "relation": edata.get("relation", ""),
                "weight": weight,
            })

    cross_edges.sort(key=lambda e: e["weight"], reverse=True)
    return cross_edges[:top_n]