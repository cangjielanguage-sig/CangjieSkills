"""反馈分析器。

分析用户反馈数据，发现知识盲区和优化机会。
"""

import json
from pathlib import Path
from collections import Counter
from typing import Optional


class FeedbackAnalyzer:
    """反馈分析器。

    分析查询日志和反馈数据，输出优化建议。
    """

    def __init__(self, data_dir: str):
        self._data_dir = Path(data_dir)

    def analyze(self) -> dict:
        """执行全面分析。

        Returns:
            分析报告
        """
        return {
            "hot_topics": self._get_hot_topics(),
            "missed_queries": self._get_missed_queries(),
            "partial_hits": self._get_partial_hits(),
            "satisfaction_trend": self._get_satisfaction_trend(),
            "optimization_suggestions": self._generate_suggestions(),
        }

    def _get_hot_topics(self, top_n: int = 20) -> list[dict]:
        """获取热门查询。"""
        queries_path = self._data_dir / "queries.jsonl"
        if not queries_path.exists():
            return []

        counts = Counter()
        with open(queries_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    q = data.get("query", "").lower()
                    if q:
                        counts[q] += 1

        return [{"query": q, "count": c} for q, c in counts.most_common(top_n)]

    def _get_missed_queries(self, limit: int = 30) -> list[dict]:
        """获取完全未命中的查询。"""
        failed_path = self._data_dir / "failed_queries.jsonl"
        if not failed_path.exists():
            return []

        counts = Counter()
        with open(failed_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    q = data.get("query", "")
                    if q:
                        counts[q] += 1

        return [{"query": q, "miss_count": c} for q, c in counts.most_common(limit)]

    def _get_partial_hits(self, limit: int = 20) -> list[dict]:
        """获取部分命中的查询（有结果但不满意）。"""
        queries_path = self._data_dir / "queries.jsonl"
        if not queries_path.exists():
            return []

        partials = []
        with open(queries_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    if data.get("satisfied") is False and data.get("result_count", 0) > 0:
                        partials.append({
                            "query": data.get("query", ""),
                            "result_count": data.get("result_count", 0),
                            "graph_used": data.get("graph_used", ""),
                        })

        return partials[:limit]

    def _get_satisfaction_trend(self) -> list[dict]:
        """获取满意度趋势（按日期）。"""
        queries_path = self._data_dir / "queries.jsonl"
        if not queries_path.exists():
            return []

        daily = {}
        with open(queries_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    ts = data.get("timestamp", "")[:10]
                    if ts:
                        if ts not in daily:
                            daily[ts] = {"total": 0, "satisfied": 0}
                        daily[ts]["total"] += 1
                        if data.get("satisfied") is True:
                            daily[ts]["satisfied"] += 1

        return [
            {"date": d, "total": v["total"], "satisfied": v["satisfied"],
             "rate": round(v["satisfied"] / v["total"], 2) if v["total"] > 0 else 0}
            for d, v in sorted(daily.items())
        ]

    def _generate_suggestions(self) -> list[str]:
        """生成优化建议。"""
        suggestions = []
        missed = self._get_missed_queries()
        partials = self._get_partial_hits()

        if missed:
            suggestions.append(
                f"发现 {len(missed)} 个完全未命中的查询，建议检查是否需要补充相关文档或添加新节点。"
            )

        if partials:
            suggestions.append(
                f"发现 {len(partials)} 个部分命中的查询，建议检查相关节点的标签和边是否需要优化。"
            )

        hot = self._get_hot_topics(top_n=5)
        if hot:
            top_queries = ", ".join([h["query"] for h in hot[:3]])
            suggestions.append(
                f"热门查询: {top_queries}。建议为这些高频查询优化搜索权重或添加快捷路径。"
            )

        if not suggestions:
            suggestions.append("暂无优化建议，数据量不足。")

        return suggestions
