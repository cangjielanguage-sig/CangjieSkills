"""图谱引擎插件抽象基类。

所有图谱后端（graphify、neo4j、自定义等）必须实现此接口。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NodeInfo:
    """节点信息。"""
    id: str
    label: str
    source_file: str
    layer: int = 3
    community: int = 0
    degree: int = 0
    source_dir: str = ""
    extra: dict = field(default_factory=dict)


@dataclass
class EdgeInfo:
    """边信息。"""
    source: str
    target: str
    relation: str = "conceptually_related_to"
    confidence: str = "EXTRACTED"
    weight: float = 1.0


@dataclass
class SearchResult:
    """搜索结果。"""
    query: str
    nodes: list[NodeInfo]
    paths: list[str]
    latency_ms: float
    graph_used: str = "merged"
    layer_filter: list[int] = field(default_factory=lambda: [1, 2, 3])


class GraphEngine(ABC):
    """图谱引擎插件基类。

    实现新的图谱后端时，继承此类并实现所有抽象方法。
    """

    @abstractmethod
    def load(self, graph_path: str) -> None:
        """加载图谱数据。

        Args:
            graph_path: 图谱 JSON 文件路径
        """
        ...

    @abstractmethod
    def search(self, query: str, layers: list[int] = None, limit: int = 10) -> SearchResult:
        """搜索图谱。

        Args:
            query: 用户查询
            layers: 层过滤 [1=概念, 2=API, 3=实现]
            limit: 返回结果数量

        Returns:
            SearchResult 对象
        """
        ...

    @abstractmethod
    def search_concept(self, query: str, limit: int = 5) -> SearchResult:
        """概念层搜索（L1）。"""
        ...

    @abstractmethod
    def search_api(self, query: str, limit: int = 10) -> SearchResult:
        """API 层搜索（L1+L2）。"""
        ...

    @abstractmethod
    def search_impl(self, query: str, limit: int = 5) -> SearchResult:
        """实现层搜索（L3）。"""
        ...

    @abstractmethod
    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list[NodeInfo]:
        """查找两个节点之间的最短路径。

        Args:
            node_a: 起点节点 ID 或标签
            node_b: 终点节点 ID 或标签
            max_depth: 最大搜索深度

        Returns:
            路径上的节点列表
        """
        ...

    @abstractmethod
    def explain_node(self, node_id: str) -> Optional[NodeInfo]:
        """获取节点详细信息。

        Args:
            node_id: 节点 ID

        Returns:
            节点信息，不存在则返回 None
        """
        ...

    @abstractmethod
    def get_neighbors(self, node_id: str, max_count: int = 20) -> list[NodeInfo]:
        """获取节点的邻居。

        Args:
            node_id: 节点 ID
            max_count: 最大返回数量

        Returns:
            邻居节点列表
        """
        ...

    @abstractmethod
    def add_edge(self, source: str, target: str, relation: str = "user_inferred",
                 confidence: str = "INFERRED", weight: float = 0.5) -> bool:
        """添加新边（用于自动优化）。

        Args:
            source: 源节点 ID
            target: 目标节点 ID
            relation: 关系类型
            confidence: 置信度标签
            weight: 边权重

        Returns:
            是否成功添加
        """
        ...

    @abstractmethod
    def save(self, graph_path: str) -> bool:
        """保存图谱到文件。

        Args:
            graph_path: 保存路径

        Returns:
            是否成功
        """
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """引擎名称。"""
        ...

    @property
    @abstractmethod
    def stats(self) -> dict:
        """图谱统计信息。"""
        ...
