"""图谱搜索功能。

封装引擎的搜索能力，提供统一的搜索接口。
"""

import time
from typing import Optional

from engines.base import GraphEngine, SearchResult


class GraphSearch:
    """图谱搜索器。

    对底层引擎进行搜索封装，提供分层搜索、全量搜索等能力。
    """

    def __init__(self, engine: GraphEngine):
        self._engine = engine

    def search(self, query: str, layers: list[int] = None, limit: int = 10) -> SearchResult:
        """通用搜索。

        Args:
            query: 查询字符串
            layers: 层过滤，None 表示全部层 [1,2,3]
            limit: 返回数量
        """
        return self._engine.search(query, layers=layers, limit=limit)

    def search_concept(self, query: str, limit: int = 5) -> SearchResult:
        """概念层搜索（L1）。适合架构设计、模块探索。"""
        return self._engine.search_concept(query, limit=limit)

    def search_api(self, query: str, limit: int = 10) -> SearchResult:
        """API 层搜索（L1+L2）。适合组件查找、API 签名。"""
        return self._engine.search_api(query, limit=limit)

    def search_impl(self, query: str, limit: int = 5) -> SearchResult:
        """实现层搜索（L3）。适合实现细节、源码追溯。"""
        return self._engine.search_impl(query, limit=limit)

    def search_all(self, query: str, limit: int = 10) -> SearchResult:
        """全层搜索。概念+API 优先，实现层兜底。"""
        return self._engine.search(query, layers=[1, 2, 3], limit=limit)

    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list:
        """查找两个概念之间的关系路径。"""
        return self._engine.find_path(node_a, node_b, max_depth=max_depth)

    def explain(self, node_id: str):
        """获取节点详细解释。"""
        return self._engine.explain_node(node_id)

    def neighbors(self, node_id: str, max_count: int = 20) -> list:
        """获取节点的关联节点。"""
        return self._engine.get_neighbors(node_id, max_count=max_count)

    @property
    def engine(self) -> GraphEngine:
        return self._engine
