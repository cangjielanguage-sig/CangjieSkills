"""图谱引擎插件抽象基类。

所有图谱后端（graphify、neo4j、自定义等）必须实现此接口。
职责：图计算、路径查找、导出支持（不包含搜索逻辑）。

设计说明：搜索功能由 graph/doc/search.py 和 graph/code/search.py 独立实现，
本接口仅服务于需要 NetworkX 等图计算库的高级操作（path/god-nodes/surprises），
以及图谱的加载、保存和导出。两者通过 GraphSession._load_engine() 按需桥接。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NodeInfo:
    """节点信息（用于图计算和导出）— 与搜索 Hit 模型不同，包含图拓扑属性。"""
    id: str
    label: str
    source_file: str
    layer: int = 3          # 默认3表示未分类；1=概念层, 2=API层
    community: int = 0      # 社区编号，对应 COMMUNITIES 列表的索引
    degree: int = 0         # 节点度（连接数），god-nodes 排序依据
    source_dir: str = ""    # 源文件所在目录（导出时用于分组）
    extra: dict = field(default_factory=dict)


@dataclass
class EdgeInfo:
    """边信息 — 描述两个节点之间的关系。"""
    source: str
    target: str
    relation: str = "conceptually_related_to"   # 默认关系类型
    confidence: str = "EXTRACTED"                # EXTRACTED=确定性边, INFERRED=推断边, AMBIGUOUS=模糊边
    weight: float = 1.0


class GraphEngine(ABC):
    """图谱引擎插件基类。

    实现新的图谱后端时，继承此类并实现所有抽象方法。
    注意：搜索逻辑已迁移至 graph/ 目录，本接口仅保留图计算与导出功能。

    生命周期：load() → 使用 find_path/explain_node/get_neighbors → 可选 save()
    """

    @abstractmethod
    def load(self, graph_path: str) -> None:
        """加载图谱数据。

        Args:
            graph_path: 图谱 JSON 文件路径
        """
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
