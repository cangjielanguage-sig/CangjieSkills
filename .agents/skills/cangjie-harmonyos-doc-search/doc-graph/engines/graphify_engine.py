"""Graphify 图谱引擎实现 — 基于 graphify 生成的 JSON 图谱文件，使用 NetworkX 进行图计算。

职责：图谱加载、路径查找、邻居获取、图谱保存（供导出和路径计算使用）。
本引擎不负责搜索逻辑（搜索由 DocSearchEngine/CodeSearchEngine 处理），
仅用于 path/god-nodes/surprises 等需要全图拓扑的高级操作。

依赖：需要安装 networkx 库。
"""

import json
from pathlib import Path
from typing import Optional

import networkx as nx
from networkx.readwrite import json_graph

from .base import GraphEngine, NodeInfo
from .registry import register


@register
class GraphifyEngine(GraphEngine):
    """基于 graphify JSON 图谱的引擎实现。

    生命周期：load() 加载 JSON → 构建节点索引 → 支持 find_path/get_neighbors/explain_node → save() 持久化变更
    节点解析：_resolve_node() 支持 ID 和 label 双查找模式，优先匹配精确 ID。
    """

    def __init__(self):
        self._graph: Optional[nx.Graph] = None
        self._graph_path: Optional[str] = None
        # 节点索引：同时按 ID、norm_label、label 三种键存储，支持模糊查找
        self._node_index: dict[str, dict] = {}

    @property
    def name(self) -> str:
        return "graphify"

    @property
    def stats(self) -> dict:
        if self._graph is None:
            return {"loaded": False}
        return {
            "loaded": True,
            "nodes": self._graph.number_of_nodes(),
            "edges": self._graph.number_of_edges(),
            "graph_path": self._graph_path,
        }

    def load(self, graph_path: str) -> None:
        """加载图谱 JSON 文件并构建 NetworkX 图 + 节点索引。

        graphify 输出的 JSON 使用 "links" 作为边字段名，
        因此 node_link_graph 需指定 edges="links"。
        """
        path = Path(graph_path)
        if not path.exists():
            raise FileNotFoundError(f"图谱文件不存在: {graph_path}")

        data = json.loads(path.read_text(encoding="utf-8"))
        # graphify 导出的 JSON 边字段名为 "links"，而非 NetworkX 默认的 "edges"
        self._graph = json_graph.node_link_graph(data, edges="links")
        self._graph_path = str(path)

        self._node_index = {}
        for nid, ndata in self._graph.nodes(data=True):
            self._node_index[nid] = nid
            norm = ndata.get("norm_label", "").lower()
            if norm:
                self._node_index[norm] = nid
            label_lower = ndata.get("label", "").lower()
            if label_lower:
                self._node_index[label_lower] = nid

    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list[NodeInfo]:
        """查找两个节点之间的最短路径（BFS），限制最大深度。

        先通过 _resolve_node 将标识符解析为图内节点 ID，
        再调用 NetworkX shortest_path 计算最短路径。
        """
        if self._graph is None:
            raise RuntimeError("图谱未加载")

        src = self._resolve_node(node_a)
        tgt = self._resolve_node(node_b)
        if src is None or tgt is None:
            return []

        try:
            path = nx.shortest_path(self._graph, source=src, target=tgt)
            path = path[:max_depth + 1]
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return []

        result = []
        for nid in path:
            ndata = self._graph.nodes[nid]
            result.append(NodeInfo(
                id=nid,
                label=ndata.get("label", ""),
                source_file=ndata.get("source_file", ""),
                layer=ndata.get("layer", 3),
            ))
        return result

    def explain_node(self, node_id: str) -> Optional[NodeInfo]:
        """获取节点详细信息 — 包含社区、度、层级等拓扑属性。"""
        if self._graph is None:
            raise RuntimeError("图谱未加载")

        nid = self._resolve_node(node_id)
        if nid is None or nid not in self._graph:
            return None

        ndata = self._graph.nodes[nid]
        return NodeInfo(
            id=nid,
            label=ndata.get("label", ""),
            source_file=ndata.get("source_file", ""),
            layer=ndata.get("layer", 3),
            community=ndata.get("community", 0),
            degree=self._graph.degree(nid),
            source_dir=ndata.get("source_dir", ""),
            extra={"norm_label": ndata.get("norm_label", "")},
        )

    def get_neighbors(self, node_id: str, max_count: int = 20) -> list[NodeInfo]:
        """获取节点的邻居列表 — 直接遍历 NetworkX 图的邻接关系。"""
        if self._graph is None:
            raise RuntimeError("图谱未加载")

        nid = self._resolve_node(node_id)
        if nid is None or nid not in self._graph:
            return []

        neighbors = []
        for neighbor_id in list(self._graph.neighbors(nid))[:max_count]:
            ndata = self._graph.nodes[neighbor_id]
            neighbors.append(NodeInfo(
                id=neighbor_id,
                label=ndata.get("label", ""),
                source_file=ndata.get("source_file", ""),
                layer=ndata.get("layer", 3),
            ))
        return neighbors

    def add_edge(self, source: str, target: str, relation: str = "user_inferred",
                 confidence: str = "INFERRED", weight: float = 0.5) -> bool:
        """添加边到图谱中 — 仅在边不存在时添加，避免重复。"""
        if self._graph is None:
            raise RuntimeError("图谱未加载")

        src = self._resolve_node(source)
        tgt = self._resolve_node(target)
        if src is None or tgt is None:
            return False

        if not self._graph.has_edge(src, tgt):
            self._graph.add_edge(src, tgt, relation=relation,
                                 confidence=confidence, weight=weight)
            return True
        return False

    def save(self, graph_path: str) -> bool:
        """保存图谱到 JSON 文件 — 使用 node_link_data 格式，边字段名为 "links"。"""
        if self._graph is None:
            return False

        data = json_graph.node_link_data(self._graph, edges="links")
        Path(graph_path).parent.mkdir(parents=True, exist_ok=True)
        Path(graph_path).write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return True

    def _resolve_node(self, identifier: str) -> Optional[str]:
        """解析节点标识符为图内节点 ID。

        查找优先级：
        1. 精确 ID 匹配（identifier 直接是图内节点 ID）
        2. 标签匹配（identifier 可能是 label 或 norm_label，通过索引反查 ID）
        """
        if identifier in self._graph:
            return identifier
        lower = identifier.lower()
        if lower in self._node_index:
            return self._node_index[lower]
        return None
