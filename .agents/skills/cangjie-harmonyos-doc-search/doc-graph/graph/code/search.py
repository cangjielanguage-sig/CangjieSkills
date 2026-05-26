"""源码图谱搜索引擎 — OR+累加打分 + brief模式 + 直接/关联分离。"""
from __future__ import annotations

import re
import time

from core.models import CodeNode, Hit, SearchResult
from core.constants import CODE_KIND_MAP
from graph.base_search import _tokenize_en, _parse_community_prefix


def _extract_kind_filter(query: str) -> str | None:
    query_lower = query.lower()
    for keyword, kind in CODE_KIND_MAP.items():
        if keyword in query_lower:
            return kind
    return None


def score_code_node(query: str, node: CodeNode, query_tokens: list[str]) -> tuple[float, str]:
    """OR + 累加打分策略（源码图）。

    Returns:
        (score, best_match_type)
    """
    score = 0.0
    best_match = ""
    label = node.label.lower()
    keywords = [k.lower() for k in (node.keywords or [])]
    methods = [m.lower() for m in (node.methods or [])]
    enum_values = [e.lower() for e in (node.enum_values or [])]

    for t in query_tokens:
        t_lower = t.lower()

        # label 精确匹配
        if t_lower == label:
            score += 100.0
            best_match = best_match or "label"
        # label 包含匹配
        elif t_lower in label:
            score += 60.0
            best_match = best_match or "label"
        # keywords 精确匹配
        elif t_lower in keywords:
            score += 40.0
            best_match = best_match or "keyword"
        # keywords 包含匹配
        elif any(t_lower in kw or kw in t_lower for kw in keywords):
            score += 25.0
            best_match = best_match or "keyword"
        # methods 匹配
        elif t_lower in methods:
            score += 25.0
            best_match = best_match or "method"
        # enum_values 匹配
        elif t_lower in enum_values:
            score += 25.0
            best_match = best_match or "enum_value"

    # api_kind 过滤加权
    kind_filter = _extract_kind_filter(query)
    if kind_filter and node.api_kind == kind_filter:
        score *= 1.2

    return score, best_match


class CodeSearchEngine:
    """源码图搜索引擎。"""

    def __init__(self) -> None:
        self.nodes: dict[str, CodeNode] = {}
        self.neighbors: dict[str, list[tuple[str, str]]] = {}

    def build(self, nodes: dict[str, CodeNode], neighbors: dict[str, list[tuple[str, str]]]) -> None:
        self.nodes = nodes
        self.neighbors = neighbors

    def search(self, query: str, top_k: int = 5, brief: bool = False) -> SearchResult:
        """搜索源码图。

        Args:
            query: 查询字符串
            top_k: 直接命中返回数量
            brief: 是否仅返回简要信息（兼容旧接口）
        """
        t0 = time.perf_counter()

        community, clean_query = _parse_community_prefix(query)
        en_terms = _tokenize_en(clean_query)
        query_tokens = en_terms

        candidates = {
            nid: n for nid, n in self.nodes.items()
            if n.category == community
        } if community else self.nodes

        # 打分排序
        scored = []
        for nid, node in candidates.items():
            s, match_type = score_code_node(clean_query, node, query_tokens)
            if s > 0:
                scored.append((nid, s, match_type))

        scored.sort(key=lambda x: -x[1])

        # 直接命中
        direct_hits = []
        for nid, s, match_type in scored[:top_k]:
            node = self.nodes[nid]
            direct_hits.append(Hit(
                node_id=nid,
                label=node.label,
                source_file=node.source_file,
                score=round(s, 1),
                match_type=match_type,
            ))

        # 关联推荐
        related_hits = []
        seen_ids = {h.node_id for h in direct_hits}
        max_related = 5
        related_k = 2

        for hit in direct_hits:
            if len(related_hits) >= max_related:
                break
            for neighbor_id, relation in self.neighbors.get(hit.node_id, [])[:related_k]:
                if neighbor_id not in seen_ids and neighbor_id in self.nodes:
                    seen_ids.add(neighbor_id)
                    neighbor = self.nodes[neighbor_id]
                    related_hits.append(Hit(
                        node_id=neighbor_id,
                        label=neighbor.label,
                        source_file=neighbor.source_file,
                        score=round(hit.score * 0.5, 1),
                        match_type="related",
                        related_from=hit.label,
                        relation_type=relation,
                    ))
                    if len(related_hits) >= max_related:
                        break

        elapsed_ms = (time.perf_counter() - t0) * 1000

        return SearchResult(
            query=query,
            direct_hits=direct_hits,
            related_hits=related_hits,
            graph_used="code",
            latency_ms=round(elapsed_ms, 1),
        )

    def explain(self, node_id: str) -> str:
        node = self.nodes.get(node_id)
        if not node:
            return f"Node {node_id} not found."

        lines = [f"=== {node.label} ({node.api_kind}) ==="]
        lines.append(f"社区: {node.category}")
        lines.append(f"路径: {node.source_file}")
        if node.methods:
            lines.append(f"方法 ({len(node.methods)}): {', '.join(node.methods[:10])}")
        if node.enum_values:
            lines.append(f"枚举值: {', '.join(node.enum_values)}")

        neighbors = self.neighbors.get(node_id, [])
        if neighbors:
            lines.append(f"\n关联 ({len(neighbors)}):")
            for nid, relation in neighbors[:10]:
                n = self.nodes.get(nid)
                lines.append(f"  --{relation}--> {n.label if n else nid}")

        return "\n".join(lines)
