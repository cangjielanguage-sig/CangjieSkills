"""搜索基类。封装通用的搜索流程。"""
from __future__ import annotations

import re
import time
from abc import ABC, abstractmethod
from typing import Any

from core.models import Hit, SearchResult
from core.constants import COMMUNITIES


def _parse_community_prefix(query: str) -> tuple[str | None, str]:
    for comm in COMMUNITIES:
        match = re.match(rf"^{comm}[\.\s]+", query, re.IGNORECASE)
        if match:
            return comm, query[match.end():]
    return None, query


def _tokenize_zh(query: str) -> list[str]:
    return re.findall(r"[\u4e00-\u9fff]+", query)


def _tokenize_en(query: str) -> list[str]:
    return re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z_][A-Za-z0-9_]*", query)


class BaseSearchEngine(ABC):
    """搜索基类。"""

    def __init__(self) -> None:
        self.nodes: dict[str, Any] = {}
        self.neighbors: dict[str, list[tuple[str, str]]] = {}

    def build(self, nodes: dict[str, Any], neighbors: dict[str, list[tuple[str, str]]]) -> None:
        self.nodes = nodes
        self.neighbors = neighbors
        self._post_build()

    def _post_build(self) -> None:
        """构建后钩子，子类可覆写以构建索引等。"""
        pass

    @abstractmethod
    def _tokenize_query(self, query: str) -> list[str]:
        """分词。"""
        pass

    @abstractmethod
    def _score_node(self, query: str, node: Any, tokens: list[str]) -> tuple[float, str]:
        """打分。"""
        pass

    def search(self, query: str, top_k: int = 5) -> SearchResult:
        t0 = time.perf_counter()

        community, clean_query = _parse_community_prefix(query)
        tokens = self._tokenize_query(clean_query)

        candidates = {
            nid: n for nid, n in self.nodes.items()
            if n.category == community
        } if community else self.nodes

        # 打分
        scored = []
        for nid, node in candidates.items():
            s, match_type = self._score_node(clean_query, node, tokens)
            if s > 0:
                scored.append((nid, s, match_type))

        scored.sort(key=lambda x: -x[1])

        # 结果构建
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
            graph_used="doc", # 子类应覆写或设置
            latency_ms=round(elapsed_ms, 1),
        )
