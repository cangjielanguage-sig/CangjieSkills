"""图谱自动优化器。

根据用户反馈自动优化知识图谱（新增边、调整权重等）。
"""

import json
import re
from pathlib import Path
from typing import Optional
from datetime import datetime

from core.search import GraphSearch
from core.models import FeedbackRecord
from feedback.collector import FeedbackCollector


class GraphOptimizer:
    """图谱优化器。

    基于用户反馈自动优化图谱结构。
    """

    def __init__(self, search: GraphSearch, collector: FeedbackCollector,
                 graph_save_path: str):
        self._search = search
        self._collector = collector
        self._graph_save_path = graph_save_path
        self._alias_map: dict[str, list[str]] = {}
        self._alias_path = Path(graph_save_path).parent / "aliases.json"
        self._load_aliases()

    def optimize_from_feedback(self) -> dict:
        """基于反馈数据执行优化。

        Returns:
            优化报告
        """
        report = {
            "edges_added": 0,
            "aliases_added": 0,
            "suggestions": [],
            "timestamp": datetime.now().isoformat(),
        }

        # 1. 分析失败查询，尝试添加别名
        failed = self._collector.get_failed_queries()
        for query in failed:
            self._try_add_alias(query)

        # 2. 分析部分命中查询，尝试添加关联边
        partials = self._collector.get_failed_queries()[:10]
        for query in partials:
            self._try_infer_edges(query)

        report["aliases_added"] = len(self._alias_map)
        report["suggestions"] = self._generate_suggestions()

        self._save_aliases()
        return report

    def add_user_edge(self, source: str, target: str,
                      relation: str = "user_inferred") -> bool:
        """手动添加用户发现的边。

        Args:
            source: 源节点 ID 或标签
            target: 目标节点 ID 或标签
            relation: 关系类型

        Returns:
            是否成功添加
        """
        success = self._search.engine.add_edge(
            source, target, relation=relation,
            confidence="INFERRED", weight=0.7
        )
        if success:
            self._search.engine.save(self._graph_save_path)
        return success

    def add_alias(self, canonical: str, alias: str) -> None:
        """添加节点别名。

        Args:
            canonical: 标准名称
            alias: 别名
        """
        if canonical not in self._alias_map:
            self._alias_map[canonical] = []
        if alias not in self._alias_map[canonical]:
            self._alias_map[canonical].append(alias)

    def resolve_alias(self, query: str) -> str:
        """将查询中的别名解析为标准名称。"""
        lowered = query.lower()
        for canonical, aliases in self._alias_map.items():
            for alias in aliases:
                if alias.lower() in lowered:
                    return canonical
        return query

    def _try_add_alias(self, query: str) -> None:
        """尝试为失败查询添加别名。"""
        # 提取查询中的关键词
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|[\u4e00-\u9fff]+", query)
        for token in tokens:
            if len(token) >= 3:
                result = self._search.search_api(token, limit=1)
                if result.nodes:
                    node = result.nodes[0]
                    self.add_alias(node.label, token.lower())

    def _try_infer_edges(self, query: str) -> None:
        """尝试为查询推断新边。"""
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|[\u4e00-\u9fff]+", query)
        if len(tokens) < 2:
            return

        # 查找查询中提到的多个节点
        found_nodes = []
        for token in tokens[:5]:
            result = self._search.search_api(token, limit=1)
            if result.nodes:
                found_nodes.append(result.nodes[0])

        # 如果找到多个节点，它们之间可能存在关联
        if len(found_nodes) >= 2:
            for i in range(len(found_nodes) - 1):
                self._search.engine.add_edge(
                    found_nodes[i].id, found_nodes[i + 1].id,
                    relation="co_occurrence",
                    confidence="INFERRED", weight=0.3
                )

    def _generate_suggestions(self) -> list[str]:
        """生成优化建议。"""
        suggestions = []
        failed = self._collector.get_failed_queries()
        if failed:
            suggestions.append(f"有 {len(failed)} 个失败查询需要关注")

        if len(self._alias_map) > 0:
            suggestions.append(f"新增 {len(self._alias_map)} 个别名映射")

        return suggestions

    def _load_aliases(self) -> None:
        """加载别名映射。"""
        if self._alias_path.exists():
            with open(self._alias_path, "r", encoding="utf-8") as f:
                self._alias_map = json.load(f)

    def _save_aliases(self) -> None:
        """保存别名映射。"""
        with open(self._alias_path, "w", encoding="utf-8") as f:
            json.dump(self._alias_map, f, ensure_ascii=False, indent=2)
