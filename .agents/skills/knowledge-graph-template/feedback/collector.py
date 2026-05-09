"""用户反馈收集器。

记录每次查询的结果和用户反馈，为自动优化提供数据。
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional

from core.models import QueryRecord, FeedbackRecord


class FeedbackCollector:
    """反馈收集器。

    将查询记录和用户反馈持久化到文件。
    """

    def __init__(self, data_dir: str):
        self._data_dir = Path(data_dir)
        self._data_dir.mkdir(parents=True, exist_ok=True)
        self._queries_path = self._data_dir / "queries.jsonl"
        self._failed_path = self._data_dir / "failed_queries.jsonl"
        self._feedback_path = self._data_dir / "feedback.jsonl"
        self._hot_path = self._data_dir / "hot_topics.json"

    def record_query(self, record: QueryRecord) -> None:
        """记录一次查询。"""
        self._append_jsonl(self._queries_path, record.to_dict())

        # 如果查询未命中任何结果，记录到失败文件
        if record.result_count == 0:
            self._append_jsonl(self._failed_path, {
                "query": record.query,
                "timestamp": record.timestamp,
                "graph_used": record.graph_used,
            })

    def record_feedback(self, record: FeedbackRecord) -> None:
        """记录用户反馈。"""
        self._append_jsonl(self._feedback_path, record.to_dict())

    def mark_satisfied(self, query: str, satisfied: bool) -> None:
        """标记某次查询是否满意。

        会更新 queries.jsonl 中最近一次匹配该查询的记录。
        """
        self._update_last_query(query, {"satisfied": satisfied})

    def get_hot_topics(self, top_n: int = 20) -> list[dict]:
        """获取高频查询主题。"""
        if not self._queries_path.exists():
            return []

        counts = {}
        with open(self._queries_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    q = data.get("query", "").lower()
                    counts[q] = counts.get(q, 0) + 1

        sorted_topics = sorted(counts.items(), key=lambda x: -x[1])
        return [{"query": q, "count": c} for q, c in sorted_topics[:top_n]]

    def get_failed_queries(self, limit: int = 50) -> list[str]:
        """获取失败的查询列表。"""
        if not self._failed_path.exists():
            return []

        queries = []
        with open(self._failed_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    queries.append(data.get("query", ""))
                    if len(queries) >= limit:
                        break
        return queries

    def get_stats(self) -> dict:
        """获取反馈统计。"""
        total = self._count_lines(self._queries_path)
        failed = self._count_lines(self._failed_path)
        feedback = self._count_lines(self._feedback_path)

        satisfied = 0
        unsatisfied = 0
        if self._queries_path.exists():
            with open(self._queries_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data = json.loads(line)
                        if data.get("satisfied") is True:
                            satisfied += 1
                        elif data.get("satisfied") is False:
                            unsatisfied += 1

        return {
            "total_queries": total,
            "failed_queries": failed,
            "feedback_count": feedback,
            "satisfied": satisfied,
            "unsatisfied": unsatisfied,
            "satisfaction_rate": round(satisfied / (satisfied + unsatisfied), 2) if (satisfied + unsatisfied) > 0 else None,
        }

    def _append_jsonl(self, path: Path, data: dict) -> None:
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    def _count_lines(self, path: Path) -> int:
        if not path.exists():
            return 0
        with open(path, "r", encoding="utf-8") as f:
            return sum(1 for line in f if line.strip())

    def _update_last_query(self, query: str, updates: dict) -> None:
        if not self._queries_path.exists():
            return

        records = []
        with open(self._queries_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

        for record in reversed(records):
            if record.get("query", "").lower() == query.lower():
                record.update(updates)
                break

        with open(self._queries_path, "w", encoding="utf-8") as f:
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
