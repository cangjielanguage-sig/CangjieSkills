"""仓颉鸿蒙知识图谱 — Agent 编程接口。

用法：
    from query import create_session, search, find_path, explain, traverse

    # 创建会话
    session = create_session()

    # 搜索（定位文档）
    results = session.search("List 组件 onReachEnd")
    results = session.search_api("Button")
    results = session.search_concept("状态管理")

    # 图遍历（发现关联）✦ 新增
    traverse_result = session.traverse("List 组件")  # BFS 遍历
    traverse_result = session.traverse("List 组件", mode="dfs")  # DFS 遍历

    # 搜索 + 邻居 ✦ 新增
    results = session.search_with_neighbors("List 组件")

    # 查找关系
    path = session.find_path("UIAbility", "WindowStage")

    # 节点解释
    info = session.explain("List")

    # 图分析 ✦ 新增
    god_nodes = session.god_nodes()
    surprises = session.surprises()
    questions = session.suggest_questions()
    comm = session.community_info(0)
"""

import sys
import os
from pathlib import Path
from typing import Optional

# 添加项目根目录到 Python 路径
_PROJECT_ROOT = Path(__file__).resolve().parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from engines import create_engine, GraphifyEngine, list_engines
from engines.graphify_engine import expanded_query
from engines.base import GraphEngine, SearchResult
from core.search import GraphSearch
from core.smart_router import SmartRouter
from core.layer import LayerAnnotator
from core.models import QueryRecord, FeedbackRecord
from core.traversal import traverse as traverse_graph, traverse_text, god_nodes as get_god_nodes, surprising_connections as get_surprises, suggest_questions as get_suggestions, community_info as get_community_info, TraverseResult
from feedback.collector import FeedbackCollector
from feedback.analyzer import FeedbackAnalyzer
from feedback.optimizer import GraphOptimizer
from datetime import datetime


class GraphSession:
    """图谱查询会话。

    封装所有图谱操作，提供统一的查询接口。
    """

    def __init__(self, graph_dir: str = None, enable_feedback: bool = True):
        if graph_dir is None:
            graph_dir = str(_PROJECT_ROOT / "data")

        self._graph_dir = Path(graph_dir)
        preferred_merged_path = self._graph_dir / "merged" / "graph.json"
        legacy_merged_path = self._graph_dir / "merged" / "graph_layered.json"
        self._merged_path = preferred_merged_path if preferred_merged_path.exists() else legacy_merged_path
        if not self._merged_path.exists():
            rebuild_script = _PROJECT_ROOT / "scripts" / "rebuild_cangjie_graph.py"
            raise FileNotFoundError(
                "knowledge-graph-template 图谱数据缺失，无法加载 data/merged/graph.json。"
                f" 请先执行 `python {rebuild_script}` 重建默认图谱。"
            )
        self._feedback_dir = self._graph_dir / "feedback"
        self._enable_feedback = enable_feedback

        # 加载合并图谱
        self._merged_engine = GraphifyEngine()
        self._merged_engine.load(str(self._merged_path))
        self._merged_search = GraphSearch(self._merged_engine)

        # 加载子图谱
        self._subgraph_searches = {}
        subgraph_names = {
            "harmonyos": "harmonyos",
            "lang-features": "lang-features",
            "std": "std",
            "stdx": "stdx",
            "tools": "tools",
        }
        for name, dir_name in subgraph_names.items():
            graph_file = self._graph_dir / "subgraphs" / dir_name / "graph.json"
            if graph_file.exists():
                engine = GraphifyEngine()
                engine.load(str(graph_file))
                self._subgraph_searches[name] = GraphSearch(engine)

        # 创建路由器
        self._router = SmartRouter(self._merged_search, self._subgraph_searches)

        # 创建反馈系统
        if enable_feedback:
            self._collector = FeedbackCollector(str(self._feedback_dir))
            self._analyzer = FeedbackAnalyzer(str(self._feedback_dir))
            self._optimizer = GraphOptimizer(
                self._merged_search, self._collector,
                str(self._merged_path),
            )
        else:
            self._collector = None
            self._analyzer = None
            self._optimizer = None

    def search(self, query: str, limit: int = 10, force_graph: str = None) -> SearchResult:
        """智能搜索（自动选择最合适的图谱）。"""
        searcher, graph_name = self._router.route(query, force_graph=force_graph)
        expanded = expanded_query(query)
        result = searcher.search_all(expanded, limit=limit)
        result.query = query
        result.graph_used = graph_name

        if self._collector:
            self._collector.record_query(QueryRecord(
                query=query,
                timestamp=datetime.now().isoformat(),
                graph_used=graph_name,
                layer_filter=[1, 2, 3],
                result_count=len(result.paths),
                latency_ms=result.latency_ms,
                top_paths=result.paths[:3],
            ))

        return result

    def search_concept(self, query: str, limit: int = 5) -> SearchResult:
        """概念层搜索（L1）。"""
        return self._merged_search.search_concept(query, limit=limit)

    def search_api(self, query: str, limit: int = 10) -> SearchResult:
        """API 层搜索（L1+L2）。"""
        return self._merged_search.search_api(query, limit=limit)

    def search_impl(self, query: str, limit: int = 5) -> SearchResult:
        """实现层搜索（L3）。"""
        return self._merged_search.search_impl(query, limit=limit)

    def search_all(self, query: str, limit: int = 10) -> SearchResult:
        """全层搜索。"""
        return self._merged_search.search_all(query, limit=limit)

    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list:
        """查找两个节点之间的关系路径。"""
        return self._merged_search.find_path(node_a, node_b, max_depth=max_depth)

    def explain(self, node_id: str):
        """获取节点详细信息。"""
        return self._merged_search.explain(node_id)

    def neighbors(self, node_id: str, max_count: int = 20) -> list:
        """获取节点的关联节点。"""
        return self._merged_search.neighbors(node_id, max_count=max_count)

    def available_graphs(self) -> list[str]:
        """列出可用的图谱。"""
        return self._router.available_graphs()

    def add_edge(self, source: str, target: str, relation: str = "user_inferred") -> bool:
        """手动添加边。"""
        if self._optimizer:
            return self._optimizer.add_user_edge(source, target, relation)
        return self._merged_engine.add_edge(source, target, relation)

    def mark_satisfied(self, query: str, satisfied: bool) -> None:
        """标记查询满意度。"""
        if self._collector:
            self._collector.mark_satisfied(query, satisfied)

    def get_stats(self) -> dict:
        """获取图谱和使用统计。"""
        stats = {
            "merged_graph": self._merged_engine.stats,
            "subgraphs": {
                name: search.engine.stats
                for name, search in self._subgraph_searches.items()
            },
            "available_graphs": self.available_graphs(),
        }
        if self._collector:
            stats["feedback"] = self._collector.get_stats()
            stats["hot_topics"] = self._collector.get_hot_topics(top_n=10)
        return stats

    def get_analysis(self) -> dict:
        """获取反馈分析报告。"""
        if self._analyzer:
            return self._analyzer.analyze()
        return {"error": "反馈系统未启用"}

    def optimize(self) -> dict:
        """执行图谱优化。"""
        if self._optimizer:
            return self._optimizer.optimize_from_feedback()
        return {"error": "优化器未启用"}

    def traverse(self, query: str, mode: str = "bfs", depth: int = 3, token_budget: int = 2000, force_graph: str = None) -> TraverseResult:
        """图遍历（发现关联）。

        Args:
            query: 搜索关键词
            mode: 遍历模式，"bfs" 或 "dfs"
            depth: 遍历深度（1-6）
            token_budget: 输出 token 上限
            force_graph: 强制使用的图谱

        Returns:
            TraverseResult: 遍历结果
        """
        searcher, graph_name = self._router.route(query, force_graph=force_graph)
        G = searcher.engine._graph
        expanded = expanded_query(query)
        return traverse_graph(G, expanded, mode=mode, depth=min(depth, 6), token_budget=token_budget, graph_name=graph_name)

    def traverse_text(self, query: str, mode: str = "bfs", depth: int = 3, token_budget: int = 2000) -> str:
        """图遍历返回文本格式。"""
        result = self.traverse(query, mode=mode, depth=depth, token_budget=token_budget)
        return traverse_text(result)

    def search_with_neighbors(self, query: str, limit: int = 5, neighbor_count: int = 5) -> SearchResult:
        """搜索 + 关联节点。

        Args:
            query: 搜索关键词
            limit: 搜索结果数量
            neighbor_count: 每个结果的邻居数量

        Returns:
            SearchResult: 增强后的搜索结果
        """
        result = self.search(query, limit=limit)
        G = self._merged_engine._graph
        
        enriched_paths = []
        for path_info in result.paths:
            node_id = path_info.get("node_id", path_info.get("node", ""))
            neighbors = []
            for neighbor in list(G.neighbors(node_id))[:neighbor_count]:
                neighbors.append({
                    "id": neighbor,
                    "label": G.nodes[neighbor].get("label", neighbor),
                    "relation": G[node_id][neighbor].get("relation", ""),
                })
            path_info["neighbors"] = neighbors
            enriched_paths.append(path_info)
        
        result.paths = enriched_paths
        return result

    def god_nodes(self, top_n: int = 10) -> list[dict]:
        """核心节点（连接最多的节点）。"""
        G = self._merged_engine._graph
        return get_god_nodes(G, top_n=top_n)

    def surprises(self, top_n: int = 5) -> list[dict]:
        """惊奇连接（跨社区的边）。"""
        G = self._merged_engine._graph
        return get_surprises(G, top_n=top_n)

    def suggest_questions(self, top_n: int = 7) -> list[dict]:
        """建议问题（基于图结构）。"""
        G = self._merged_engine._graph
        return get_suggestions(G, top_n=top_n)

    def community_info(self, community_id: int) -> dict:
        """社区详情。"""
        G = self._merged_engine._graph
        return get_community_info(G, community_id)


def create_session(graph_dir: str = None, enable_feedback: bool = True) -> GraphSession:
    """创建查询会话。

    Args:
        graph_dir: 图谱数据目录，默认使用项目 data/ 目录
        enable_feedback: 是否启用反馈系统

    Returns:
        GraphSession 实例
    """
    return GraphSession(graph_dir=graph_dir, enable_feedback=enable_feedback)


# 便捷函数
_default_session: Optional[GraphSession] = None


def search(query: str, limit: int = 10) -> SearchResult:
    """便捷搜索函数。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.search(query, limit=limit)


def find_path(node_a: str, node_b: str, max_depth: int = 5) -> list:
    """便捷路径查找。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.find_path(node_a, node_b, max_depth=max_depth)


def explain(node_id: str):
    """便捷节点解释。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.explain(node_id)


def traverse(query: str, mode: str = "bfs", depth: int = 3) -> TraverseResult:
    """便捷图遍历。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.traverse(query, mode=mode, depth=depth)


def traverse_text(query: str, mode: str = "bfs", depth: int = 3) -> str:
    """便捷图遍历（文本格式）。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.traverse_text(query, mode=mode, depth=depth)


def god_nodes(top_n: int = 10) -> list[dict]:
    """便捷核心节点查询。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.god_nodes(top_n=top_n)


def surprises(top_n: int = 5) -> list[dict]:
    """便捷惊奇连接查询。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.surprises(top_n=top_n)


def suggest_questions(top_n: int = 7) -> list[dict]:
    """便捷建议问题查询。"""
    global _default_session
    if _default_session is None:
        _default_session = create_session()
    return _default_session.suggest_questions(top_n=top_n)
