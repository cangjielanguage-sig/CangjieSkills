"""Graphify 图谱引擎实现。

基于 graphify 生成的 JSON 图谱文件，使用 NetworkX 进行图计算。
"""

import json
import re
import time
from pathlib import Path
from typing import Optional

import networkx as nx
from networkx.readwrite import json_graph

from .base import GraphEngine, NodeInfo, EdgeInfo, SearchResult
from .registry import register


# 分层权重配置
LAYER_WEIGHTS = {1: 1.5, 2: 2.0, 3: 0.2}

# 组件名到路径关键标识符的映射
COMPONENT_PATH_MAP = {
    "list": ["cj-scroll-swipe-list", "cj-layout-development-create-list", "list.cj"],
    "image": ["cj-common-components-image", "cj-image-", "image.cj"],
    "grid": ["cj-scroll-swipe-grid", "cj-scroll-swipe-griditem", "cj-layout-development-grid", "cj-grid-layout-", "grid.cj"],
    "griditem": ["cj-scroll-swipe-griditem"],
    "flex": ["cj-layout-development-flex-layout", "flex.cj"],
    "slider": ["cj-button-picker-slider", "slider.cj"],
    "alertdialog": ["cj-dialog-alertdialog", "alertdialog"],
    "navigation": ["cj-navigation-", "navigation.cj"],
    "web": ["cj-apis-webview", "cj-web-", "web.cj"],
    "scroll": ["cj-scroll-swipe-scroll", "scroll.cj"],
    "refresh": ["cj-scroll-swipe-refresh", "refresh.cj"],
    "button": ["cj-button-picker-button", "cj-button-", "button.cj"],
    "textinput": ["cj-common-components-text-input", "textinput.cj", "text_input"],
    "swiper": ["cj-scroll-swipe-swiper", "swiper.cj"],
    "router": ["cj-apis-uicontext-router", "router"],
    "animation": ["cj-animation-", "animation"],
    "column": ["cj-layout-development-linear", "column"],
    "row": ["cj-layout-development-linear", "row"],
    "stack": ["cj-row-column-stack", "stack"],
    "httprequest": ["cj-apis-net-http", "NetworkKit"],
    "http": ["cj-apis-net-http", "NetworkKit", "net/http"],
    "arkts": ["cangjie-arkts", "ark_interop", "FFI"],
    "aes": ["cj-crypto-aes", "CryptoArchitectureKit"],
}


def tokenize_query(query: str) -> list[str]:
    """分词查询字符串。"""
    # 先匹配复合词（包含点号）
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_.-]*|[\u3400-\u4dbf\u4e00-\u9fff]+|[0-9]+", query)
    tokens = [t.lower() for t in tokens]
    
    # 拆分包含点号的复合词
    expanded = []
    for t in tokens:
        if '.' in t:
            # 拆分 std.net -> [std, net, stdnet]
            parts = t.split('.')
            expanded.extend(parts)
            expanded.append(t.replace('.', ''))  # 合并形式
        else:
            expanded.append(t)
    
    return expanded


def normalize_path(path: str) -> str:
    """标准化文件路径。"""
    path = path.replace("\\", "/")
    for prefix in ["harmonyos-6.1-8k", "lang-features", "std", "stdx", "tools"]:
        idx = path.find(prefix + "/")
        if idx >= 0:
            return path[idx:]
    return path


def score_node(query: str, node_data: dict, query_tokens: list[str]) -> float:
    """节点打分。"""
    if not query_tokens:
        return 0.0

    label = node_data.get("label", "").lower()
    source_file = node_data.get("source_file", "").lower()
    layer = node_data.get("layer", 3)

    score = 0.0
    matched_tokens = 0

    for token in query_tokens:
        if token in label:
            score += 10.0
            matched_tokens += 1
            if label == token or label.startswith(token + " ") or label.endswith(" " + token):
                score += 15.0

    for token in query_tokens:
        if len(token) >= 3 and token in source_file:
            score += 5.0
            matched_tokens += 1

    for char in query:
        if "\u4e00" <= char <= "\u9fff" and char in label:
            score += 3.0

    if "overview" in source_file or ".abstract" in source_file or "概述" in label or "概览" in label:
        score *= 1.5

    degree = node_data.get("degree", 1)
    if degree > 20:
        score *= 1.3
    elif degree > 10:
        score *= 1.1

    if query_tokens:
        match_ratio = matched_tokens / len(query_tokens)
        score *= (1 + match_ratio)

    lowered_query = query.lower()
    for component, path_keys in COMPONENT_PATH_MAP.items():
        if component in lowered_query:
            for key in path_keys:
                if key in source_file:
                    score += 50.0
                    break

    # 组件精确匹配加分
    # 如果查询是 "Grid 布局" 但节点来自 cj-grid-layout（栅格布局），惩罚
    # 应该优先返回 cj-scroll-swipe-grid（Grid 组件）
    if "grid" in lowered_query and "布局" in query:
        if "cj-scroll-swipe-grid" in source_file or "cj-scroll-swipe-griditem" in source_file:
            score += 100.0  # 强优先 Grid 组件
        elif "cj-grid-layout" in source_file:
            score *= 0.3  # 惩罚 GridRow/GridCol 栅格布局

    # Button 组件精确匹配
    if "button" in lowered_query and "按钮" in query:
        if "cj-button-picker-button" in source_file:
            score += 100.0
        elif "cj-button-picker-slider" in source_file:
            score *= 0.3  # 惩罚 Slider

    # HttpRequest 组件精确匹配
    if "httprequest" in lowered_query or ("http" in lowered_query and "请求" in query):
        if "cj-apis-net-http" in source_file or "NetworkKit" in source_file:
            score += 100.0  # HarmonyOS NetworkKit
        elif "stdx/net/http" in source_file:
            score *= 0.5  # stdx HTTP 不是 HarmonyOS API

    score *= LAYER_WEIGHTS.get(layer, 1.0)

    return score


@register
class GraphifyEngine(GraphEngine):
    """基于 graphify JSON 图谱的引擎实现。"""

    def __init__(self):
        self._graph: Optional[nx.Graph] = None
        self._graph_path: Optional[str] = None
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
        path = Path(graph_path)
        if not path.exists():
            raise FileNotFoundError(f"图谱文件不存在: {graph_path}")

        data = json.loads(path.read_text(encoding="utf-8"))
        self._graph = json_graph.node_link_graph(data, edges="links")
        self._graph_path = str(path)

        # 构建节点索引
        self._node_index = {}
        for nid, ndata in self._graph.nodes(data=True):
            self._node_index[nid] = ndata
            self._node_index[ndata.get("norm_label", "").lower()] = ndata
            self._node_index[ndata.get("label", "").lower()] = ndata

    def _search_internal(self, query: str, layers: list[int], limit: int) -> SearchResult:
        if self._graph is None:
            raise RuntimeError("图谱未加载，请先调用 load()")

        t0 = time.perf_counter()
        query_tokens = tokenize_query(query)

        scored = []
        for nid, ndata in self._graph.nodes(data=True):
            layer = ndata.get("layer", 3)
            if layer not in layers:
                continue
            s = score_node(query, ndata, query_tokens)
            if s > 0:
                scored.append((s, nid, ndata))

        scored.sort(key=lambda x: -x[0])

        seen_paths = set()
        paths = []
        nodes = []
        for score, nid, ndata in scored:
            src = ndata.get("source_file", "")
            if src:
                normalized = normalize_path(src)
                if normalized and normalized not in seen_paths:
                    seen_paths.add(normalized)
                    paths.append(normalized)

            node_info = NodeInfo(
                id=nid,
                label=ndata.get("label", ""),
                source_file=src,
                layer=ndata.get("layer", 3),
                community=ndata.get("community", 0),
                degree=ndata.get("degree", 0),
                source_dir=ndata.get("source_dir", ""),
            )
            nodes.append(node_info)

            if len(paths) >= limit:
                break

        elapsed_ms = (time.perf_counter() - t0) * 1000

        return SearchResult(
            query=query,
            nodes=nodes,
            paths=paths,
            latency_ms=elapsed_ms,
            graph_used="graphify",
            layer_filter=layers,
        )

    def search(self, query: str, layers: list[int] = None, limit: int = 10) -> SearchResult:
        if layers is None:
            layers = [1, 2, 3]
        return self._search_internal(query, layers, limit)

    def search_concept(self, query: str, limit: int = 5) -> SearchResult:
        return self._search_internal(query, [1], limit)

    def search_api(self, query: str, limit: int = 10) -> SearchResult:
        return self._search_internal(query, [1, 2], limit)

    def search_impl(self, query: str, limit: int = 5) -> SearchResult:
        return self._search_internal(query, [3], limit)

    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list[NodeInfo]:
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
        """解析节点标识符为节点 ID。"""
        if identifier in self._graph:
            return identifier
        lower = identifier.lower()
        if lower in self._node_index:
            ndata = self._node_index[lower]
            return ndata.get("id", lower)
        return None
