"""数据模型。"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class QueryRecord:
    """查询记录。"""
    query: str
    timestamp: str
    graph_used: str
    layer_filter: list[int]
    result_count: int
    latency_ms: float
    top_paths: list[str]
    satisfied: Optional[bool] = None

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "timestamp": self.timestamp,
            "graph_used": self.graph_used,
            "layer_filter": self.layer_filter,
            "result_count": self.result_count,
            "latency_ms": round(self.latency_ms, 2),
            "top_paths": self.top_paths,
            "satisfied": self.satisfied,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "QueryRecord":
        return cls(**data)


@dataclass
class FeedbackRecord:
    """反馈记录。"""
    query: str
    timestamp: str
    feedback_type: str  # "miss", "partial", "good", "edge_add"
    details: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "timestamp": self.timestamp,
            "feedback_type": self.feedback_type,
            "details": self.details,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "FeedbackRecord":
        return cls(**data)
