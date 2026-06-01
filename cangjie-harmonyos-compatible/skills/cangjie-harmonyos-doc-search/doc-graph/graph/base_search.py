"""搜索基类 — 封装通用的搜索流程（分词→打分→排序→关联推荐）。

本模块定义了所有搜索引擎共享的流程骨架和辅助函数：
- _parse_community_prefix: 从查询中提取社区前缀（如 "std.List" → 社区 std, 查询 List）
- _tokenize_zh/_tokenize_en: 中英文分词器
- BaseSearchEngine: ABC 基类，提供 search() 通用流程，子类仅需实现 _tokenize_query 和 _score_node

关联推荐算法：对每个直接命中节点取前 2 个邻居，分数减半，最多 5 个关联结果。
"""
from __future__ import annotations

import re
import time
from abc import ABC, abstractmethod
from typing import Any

from core.models import Hit, SearchResult
from core.constants import COMMUNITIES


def _parse_community_prefix(query: str) -> tuple[str | None, str]:
    """从查询中提取社区前缀并分离。

    例如 "std.List" → ("std", "List"), "harmonyos.camera" → ("harmonyos", "camera")
    无前缀的查询如 "List 列表" → (None, "List 列表")
    返回的 community 用于过滤候选节点集，clean_query 用于实际搜索。
    """
    for comm in COMMUNITIES:
        match = re.match(rf"^{comm}[\.\s]+", query, re.IGNORECASE)
        if match:
            return comm, query[match.end():]
    return None, query


def _tokenize_zh(query: str) -> list[str]:
    """中文分词 — 提取连续中文字符段作为词元。"""
    return re.findall(r"[\u4e00-\u9fff]+", query)


def _tokenize_en(query: str) -> list[str]:
    """英文分词 — 提取标识符和普通单词，支持 @开头的仓颉注解名。"""
    return re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z_][A-Za-z0-9_]*", query)


class BaseSearchEngine(ABC):
    """搜索基类 — 定义 search() 通用流程骨架。

    子类需实现：
    - _tokenize_query(): 将查询分词为词元列表
    - _score_node(): 对单个节点打分，返回 (score, match_type)

    通用流程：解析社区前缀 → 分词 → 基于社区过滤候选 → 逐节点打分 →
    排序取 top_k → 邻居扩展关联推荐 → 构建 SearchResult
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Any] = {}
        self.neighbors: dict[str, list[tuple[str, str]]] = {}

    def build(self, nodes: dict[str, Any], neighbors: dict[str, list[tuple[str, str]]]) -> None:
        """加载节点和邻居数据，并调用 _post_build 钩子。"""
        self.nodes = nodes
        self.neighbors = neighbors
        self._post_build()

    def _post_build(self) -> None:
        """构建后钩子，子类可覆写以构建索引等。"""
        pass

    @abstractmethod
    def _tokenize_query(self, query: str) -> list[str]:
        """分词 — 子类实现。"""
        pass

    @abstractmethod
    def _score_node(self, query: str, node: Any, tokens: list[str]) -> tuple[float, str]:
        """打分 — 子类实现。返回 (分数, 最佳匹配类型)。"""
        pass

    def search(self, query: str, top_k: int = 5) -> SearchResult:
        """通用搜索流程 — 分词→社区过滤→打分→排序→关联推荐。

        关联推荐算法：对每个直接命中节点取前 related_k(2) 个邻居，
        分数为原节点分数 * 0.5，最多 max_related(5) 个。
        已命中的节点不重复出现在关联结果中。
        """
        t0 = time.perf_counter()

        # 解析社区前缀：如 "std.List" 限定只在 std 社区中搜索
        community, clean_query = _parse_community_prefix(query)
        tokens = self._tokenize_query(clean_query)

        # 社区过滤：有前缀时只搜索对应社区的节点，否则搜索全部
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
