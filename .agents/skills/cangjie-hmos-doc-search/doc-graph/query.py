"""统一查询入口 — 双图隔离（doc/code），直接接受 agent 传来的关键词。

本模块是 doc-graph 子系统对外的核心 API。GraphSession 管理 doc/code 两个搜索引擎
的生命周期，根据查询类型选择引擎或合并结果。高级图计算操作（path/god-nodes/surprises）
通过延迟加载 GraphifyEngine（需要 NetworkX）实现。

设计决策：搜索引擎（DocSearchEngine/CodeSearchEngine）与图计算引擎（GraphifyEngine）
分离，前者轻量无外部依赖，后者需要 NetworkX，仅在需要时按需加载。
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Optional

from core.models import DocNode, CodeNode, SearchResult
from graph.doc.search import DocSearchEngine
from graph.code.search import CodeSearchEngine


class GraphSession:
    """图谱查询会话 — 管理 doc/code 双引擎和 GraphifyEngine 的生命周期。

    生命周期：create_session() → 自动加载可用图谱 → search/explain/neighbors → 可选 path/god-nodes
    延迟加载：_load_engine() 仅在 path/god-nodes/surprises 等图计算命令时才加载 NetworkX 图。
    """

    def __init__(self, graph_dir: str = None):
        self.doc_engine: Optional[DocSearchEngine] = None
        self.code_engine: Optional[CodeSearchEngine] = None
        self._graph_dir = Path(graph_dir) if graph_dir else Path(__file__).resolve().parent / "data"
        self._engine = None  # GraphifyEngine 实例，延迟加载

    def _load_engine(self):
        """延迟加载 GraphifyEngine — 仅在 path/god-nodes 等图计算命令需要时触发。

        加载优先级：merged/graph.json > doc/graph.json
        （合并图谱包含更多节点，路径查找更全面）
        """
        if self._engine is not None:
            return self._engine
        from engines import GraphifyEngine
        merged_path = self._graph_dir / "merged" / "graph.json"
        doc_path = self._graph_dir / "doc" / "graph.json"
        for candidate in [merged_path, doc_path]:
            if candidate.exists():
                try:
                    eng = GraphifyEngine()
                    eng.load(str(candidate))
                    self._engine = eng
                    return eng
                except Exception:
                    continue
        return None

    def load_doc_graph(self, graph_path: str | Path | None = None) -> None:
        """加载文档图谱 — 支持 dict/list 两种节点格式，边字段兼容 edges/links 两种命名。

        优先级：显式指定路径 > doc/graph.json > merged/graph.json > 不加载
        """
        if graph_path is None:
            doc_path = self._graph_dir / "doc" / "graph.json"
            merged_path = self._graph_dir / "merged" / "graph.json"
            if doc_path.exists():
                graph_path = doc_path
            elif merged_path.exists():
                graph_path = merged_path
            else:
                return

        path = Path(graph_path)
        if not path.exists():
            return

        data = json.loads(path.read_text(encoding="utf-8"))

        # 兼容两种 JSON 格式：dict（node_id 为键）和 list（node_id 在值中）
        nodes = {}
        nodes_data = data.get("nodes", {})
        if isinstance(nodes_data, dict):
            for nid, ndata in nodes_data.items():
                nodes[nid] = DocNode.from_dict(ndata)
        elif isinstance(nodes_data, list):
            for ndata in nodes_data:
                nid = ndata.get("id", ndata.get("node_id", ""))
                if nid:
                    nodes[nid] = DocNode.from_dict(ndata)

        # 构建无向邻接表：每条边双向注册，边字段兼容 edges/links 两种命名
        neighbors = {nid: [] for nid in nodes}
        edge_list = data.get("edges", data.get("links", []))
        for edge in edge_list:
            src, tgt = edge.get("source", edge.get("source_id", "")), edge.get("target", edge.get("target_id", ""))
            relation = edge.get("relation", "see_also")
            if src in neighbors and tgt in neighbors:
                neighbors[src].append((tgt, relation))
                neighbors[tgt].append((src, relation))

        self.doc_engine = DocSearchEngine()
        self.doc_engine.build(nodes, neighbors)

    def load_code_graph(self, graph_path: str | Path | None = None) -> None:
        """加载源码图谱。"""
        if graph_path is None:
            code_path = self._graph_dir / "code" / "graph.json"
            if code_path.exists():
                graph_path = code_path
            else:
                return

        path = Path(graph_path)
        if not path.exists():
            return

        data = json.loads(path.read_text(encoding="utf-8"))

        nodes = {}
        nodes_data = data.get("nodes", {})
        if isinstance(nodes_data, dict):
            for nid, ndata in nodes_data.items():
                nodes[nid] = CodeNode.from_dict(ndata)
        elif isinstance(nodes_data, list):
            for ndata in nodes_data:
                nid = ndata.get("id", ndata.get("node_id", ""))
                if nid:
                    nodes[nid] = CodeNode.from_dict(ndata)

        neighbors = {nid: [] for nid in nodes}
        edge_list = data.get("edges", data.get("links", []))
        for edge in edge_list:
            src, tgt = edge.get("source", edge.get("source_id", "")), edge.get("target", edge.get("target_id", ""))
            relation = edge.get("relation", "uses")
            if src in neighbors and tgt in neighbors:
                neighbors[src].append((tgt, relation))
                neighbors[tgt].append((src, relation))

        self.code_engine = CodeSearchEngine()
        self.code_engine.build(nodes, neighbors)

    def search(self, query: str, top_k: int = 5, graph: str = "auto") -> SearchResult:
        """搜索图谱。直接接受 agent 传来的关键词。

        Args:
            query: 查询字符串（agent 已处理好的关键词）
            top_k: 直接命中返回数量
            graph: "doc" | "code" | "auto" | "both"
        """
        if graph == "both":
            doc_result = self._search_doc(query, top_k) if self.doc_engine else None
            code_result = self._search_code(query, top_k) if self.code_engine else None
            return self._merge_results(doc_result, code_result, query)
        elif graph == "code" and self.code_engine:
            result = self._search_code(query, top_k)
            result.query = query
            return result
        elif self.doc_engine:
            result = self._search_doc(query, top_k)
            result.query = query
            return result
        else:
            return SearchResult(query=query)

    def _search_doc(self, query: str, top_k: int) -> SearchResult:
        return self.doc_engine.search(query, top_k=top_k)

    def _search_code(self, query: str, top_k: int) -> SearchResult:
        return self.code_engine.search(query, top_k=top_k)

    def _merge_results(self, doc_result: Optional[SearchResult], code_result: Optional[SearchResult], original_query: str) -> SearchResult:
        """融合双图搜索结果 — 基于 source_file 去重，避免同一文档重复出现。

        doc 结果优先（因为是概念性文档），code 结果补充。
        取两个引擎中较大的 latency_ms 作为总耗时。
        """
        merged = SearchResult(query=original_query, graph_used="both")
        seen_paths = set()

        if doc_result:
            for h in doc_result.direct_hits:
                if h.source_file not in seen_paths:
                    seen_paths.add(h.source_file)
                    merged.direct_hits.append(h)
            for h in doc_result.related_hits:
                if h.source_file not in seen_paths:
                    seen_paths.add(h.source_file)
                    merged.related_hits.append(h)
            merged.latency_ms = max(merged.latency_ms, doc_result.latency_ms)

        if code_result:
            for h in code_result.direct_hits:
                if h.source_file not in seen_paths:
                    seen_paths.add(h.source_file)
                    merged.direct_hits.append(h)
            for h in code_result.related_hits:
                if h.source_file not in seen_paths:
                    seen_paths.add(h.source_file)
                    merged.related_hits.append(h)
            merged.latency_ms = max(merged.latency_ms, code_result.latency_ms)

        return merged

    def explain(self, node_id: str, graph: str = "doc") -> str:
        """解释节点。支持传入 label 或 node_id，自动解析。"""
        resolved = self._resolve_node_id(node_id)
        if resolved is None:
            return f"Node {node_id} not found."
        if graph == "code" and self.code_engine:
            return self.code_engine.explain(resolved)
        elif self.doc_engine:
            return self.doc_engine.explain(resolved)
        return f"Node {node_id} not found."

    def find_path(self, node_a: str, node_b: str, max_depth: int = 5) -> list:
        """查找两个节点之间的最短路径（需要 GraphifyEngine 加载 NetworkX 图）。"""
        eng = self._load_engine()
        if eng is None:
            print("提示: 需要合并图谱文件才能执行 path 命令，请先 build 或 merge")
            return []
        return eng.find_path(node_a, node_b, max_depth=max_depth)

    def _resolve_node_id(self, query: str) -> str | None:
        """将用户输入的 label/id/名称解析为内部 node_id。

        优先精确匹配 node_id，再匹配 label（大小写不敏感），最后匹配 label_zh。
        """
        for engine in (self.doc_engine, self.code_engine):
            if engine is None:
                continue
            if query in engine.nodes:
                return query
            q_lower = query.lower()
            for nid, node in engine.nodes.items():
                if node.label.lower() == q_lower:
                    return nid
                if node.label_zh and node.label_zh == query:
                    return nid
        return None

    def neighbors(self, node_id: str, max_count: int = 20) -> list:
        """获取邻居节点 — 优先从搜索引擎（内存中的邻接表），回退到 GraphifyEngine（NetworkX）。

        支持传入 label 或 node_id：若 node_id 不在引擎中，先通过 _resolve_node_id 查找。
        搜索引擎加载更快且不需要额外依赖，因此优先使用。
        """
        resolved = self._resolve_node_id(node_id)
        if resolved is None:
            return []
        if self.doc_engine and resolved in self.doc_engine.nodes:
            neighbor_ids = [nid for nid, _ in self.doc_engine.neighbors.get(resolved, [])[:max_count]]
            return [self.doc_engine.nodes[nid] for nid in neighbor_ids if nid in self.doc_engine.nodes]
        if self.code_engine and resolved in self.code_engine.nodes:
            neighbor_ids = [nid for nid, _ in self.code_engine.neighbors.get(resolved, [])[:max_count]]
            return [self.code_engine.nodes[nid] for nid in neighbor_ids if nid in self.code_engine.nodes]
        eng = self._load_engine()
        if eng is not None:
            return eng.get_neighbors(resolved, max_count=max_count)
        return []

    def god_nodes(self, top_n: int = 10) -> list[dict]:
        """核心节点（度最高）。需要 GraphifyEngine。"""
        eng = self._load_engine()
        if eng is None:
            print("提示: 需要合并图谱文件才能执行 god-nodes 命令")
            return []
        from analysis.analyze import god_nodes as _god_nodes
        return _god_nodes(eng._graph, top_n=top_n)

    def surprises(self, top_n: int = 5) -> list[dict]:
        """惊奇连接（跨社区边）。需要 GraphifyEngine。"""
        eng = self._load_engine()
        if eng is None:
            print("提示: 需要合并图谱文件才能执行 surprises 命令")
            return []
        from analysis.analyze import surprising_connections
        communities = self._extract_communities(eng._graph)
        return surprising_connections(eng._graph, communities, top_n=top_n)

    def get_stats(self) -> dict:
        """返回图谱统计。"""
        stats = {}
        if self.doc_engine:
            stats["doc_graph"] = {
                "loaded": True,
                "nodes": len(self.doc_engine.nodes),
                "edges": sum(len(v) for v in self.doc_engine.neighbors.values()) // 2,
            }
        else:
            stats["doc_graph"] = {"loaded": False}

        if self.code_engine:
            stats["code_graph"] = {
                "loaded": True,
                "nodes": len(self.code_engine.nodes),
                "edges": sum(len(v) for v in self.code_engine.neighbors.values()) // 2,
            }
        else:
            stats["code_graph"] = {"loaded": False}

        eng = self._load_engine()
        if eng is not None:
            stats["merged_graph"] = eng.stats
        return stats

    def available_graphs(self) -> list[str]:
        """列出可用图谱。"""
        graphs = []
        if self.doc_engine:
            graphs.append("doc")
        if self.code_engine:
            graphs.append("code")
        eng = self._load_engine()
        if eng is not None:
            graphs.append("merged")
        return graphs

    def _extract_communities(self, G) -> dict[int, list[str]]:
        """从 NetworkX 图中提取已有的 community 信息。"""
        communities: dict[int, list[str]] = {}
        for node_id, data in G.nodes(data=True):
            cid = data.get("community")
            if cid is not None:
                communities.setdefault(int(cid), []).append(node_id)
        return communities


def create_session(graph_dir: str = None) -> GraphSession:
    """创建查询会话，自动加载可用图谱。"""
    session = GraphSession(graph_dir=graph_dir)
    session.load_doc_graph()
    session.load_code_graph()
    return session