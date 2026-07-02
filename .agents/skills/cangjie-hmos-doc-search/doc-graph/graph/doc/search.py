"""文档图谱搜索引擎 — OR+累加打分策略，支持倒排索引加速。

搜索流程：分词→倒排索引定位候选→逐节点 OR+累加打分→排序→邻居扩展关联推荐。

打分策略详解（OR + 累加）：
- 多个词元独立匹配，分数累加（OR 逻辑，不要求全部匹配）
- 匹配维度优先级：label精确(100) > keyword精确(60) > label包含(40) > keyword包含(25) > description包含(20)
- 最终分数乘以层级权重（概念层 *2.5, API层 *1.8）
- god_node 在概览性查询时额外加成 1.2x
"""
from __future__ import annotations

import re
import time
from collections import defaultdict

from core.models import DocNode, Hit, SearchResult
from core.constants import DOC_LAYER_WEIGHTS
from graph.base_search import _tokenize_en, _tokenize_zh, _parse_community_prefix

LAYER_WEIGHTS: dict[int, float] = DOC_LAYER_WEIGHTS


def score_node(query: str, node: DocNode, en_terms: list[str], zh_terms: list[str]) -> tuple[float, str]:
    """OR + 累加打分策略 — 核心搜索算法。

    原则：仅基于节点语义内容（label/keyword/description）打分，
    移除建图知识（路径/ID）干扰，保证搜索结果的语义相关性。

    Args:
        query: 原始查询字符串（用于 god_node 加成判断）
        node: 待打分的文档节点
        en_terms: 英文词元列表
        zh_terms: 中文词元列表

    Returns:
        (score, best_match_type): 累加分数和最高优先级匹配类型
    """
    score = 0.0
    best_match = ""
    label_lower = node.label.lower()

    for t in en_terms:
        if t.lower() == label_lower:
            score += 100.0
            best_match = best_match or "label"
    if node.label_zh:
        for t in zh_terms:
            if t == node.label_zh:
                score += 100.0
                best_match = best_match or "label"

    for t in en_terms:
        if t.lower() in label_lower and t.lower() != label_lower:
            score += 40.0
            best_match = best_match or "label"
    if node.label_zh:
        for t in zh_terms:
            if t in node.label_zh and t != node.label_zh:
                score += 40.0
                best_match = best_match or "label"

    keywords_en_lower = [k.lower() for k in node.keywords_en]
    for t in en_terms:
        t_lower = t.lower()
        if t_lower in keywords_en_lower:
            score += 60.0
            best_match = best_match or "keyword"
    for t in zh_terms:
        if t in node.keywords_zh:
            score += 60.0
            best_match = best_match or "keyword"

    for t in en_terms:
        t_lower = t.lower()
        for kw in keywords_en_lower:
            if t_lower in kw or kw in t_lower:
                score += 25.0
                best_match = best_match or "keyword"
                break
    for t in zh_terms:
        for kw in node.keywords_zh:
            if t in kw or kw in t:
                score += 25.0
                best_match = best_match or "keyword"
                break

    for t in zh_terms:
        if node.description_zh and t in node.description_zh:
            score += 20.0
            best_match = best_match or "description"
    for t in en_terms:
        if node.description_en and t.lower() in node.description_en.lower():
            score += 20.0
            best_match = best_match or "description"

    score *= LAYER_WEIGHTS.get(node.layer, 1.0)

    if node.is_god_node and any(w in query for w in ["有哪些", "概览", "功能", "overview"]):
        score *= 1.2

    return score, best_match


class DocSearchEngine:
    """文档图搜索引擎 — 使用倒排索引加速候选定位。

    生命周期：build() 加载节点+邻居 → _build_inverted_index() 构倒排索引 → search() 查询
    与全量扫描的差异：使用倒排索引先缩小候选集，避免对全部节点逐一打分。
    """

    def __init__(self) -> None:
        self.nodes: dict[str, DocNode] = {}
        self.neighbors: dict[str, list[tuple[str, str]]] = {}
        self.inverted_index: dict[str, set[str]] = {}

    def build(self, nodes: dict[str, DocNode], neighbors: dict[str, list[tuple[str, str]]]) -> None:
        """加载节点和邻居数据，并构建倒排索引。"""
        self.nodes = nodes
        self.neighbors = neighbors
        self._build_inverted_index()

    def _build_inverted_index(self) -> None:
        """构建倒排索引 — 从节点元数据中提取所有可搜索词元，映射到节点 ID。

        索引覆盖范围：label、label_zh、keywords_en、keywords_zh、description_en、description_zh
        英文词元同时存储原始形式和小写形式，以支持大小写不敏感匹配。
        英文复合词（如 "PhotoOutput"）会被拆分为子词元（"Photo", "Output"）单独索引。
        """
        index: dict[str, set[str]] = {}
        
        def add_term(term: str, node_id: str) -> None:
            term_lower = term.lower()
            if term_lower not in index:
                index[term_lower] = set()
            index[term_lower].add(node_id)
            if term != term_lower:
                if term not in index:
                    index[term] = set()
                index[term].add(node_id)

        for nid, node in self.nodes.items():
            if node.label:
                add_term(node.label, nid)
                for part in re.findall(r'[A-Za-z]+', node.label):
                    if len(part) > 2:
                        add_term(part, nid)
            
            if node.label_zh:
                add_term(node.label_zh, nid)

            for kw in node.keywords_en:
                add_term(kw, nid)
                for part in re.findall(r'[A-Za-z]+', kw):
                    if len(part) > 2:
                        add_term(part, nid)
            
            for kw in node.keywords_zh:
                add_term(kw, nid)

            if node.description_en:
                for term in _tokenize_en(node.description_en):
                    add_term(term, nid)
            
            if node.description_zh:
                for term in _tokenize_zh(node.description_zh):
                    add_term(term, nid)

        self.inverted_index = index

    def search(self, query: str, top_k: int = 5) -> SearchResult:
        """搜索文档图 — 使用倒排索引优化候选定位。

        流程：
        1. 解析社区前缀，分离查询词元
        2. 通过倒排索引收集所有包含任一词元的节点 ID（候选集）
        3. 若候选集覆盖超过50%节点，退化为全量扫描（索引效果不佳）
        4. 对候选集逐节点调用 score_node 打分
        5. 排序取 top_k 直接命中 + 邻居扩展关联推荐
        """
        t0 = time.perf_counter()

        community, clean_query = _parse_community_prefix(query)
        en_terms = _tokenize_en(clean_query)
        zh_terms = _tokenize_zh(clean_query)
        all_terms = [t.lower() for t in en_terms] + zh_terms

        candidates = {
            nid: n for nid, n in self.nodes.items()
            if n.category == community
        } if community else self.nodes

        candidate_ids = set()
        if self.inverted_index:
            # 通过倒排索引收集包含任一查询词元的节点
            for term in all_terms:
                if term in self.inverted_index:
                    candidate_ids.update(self.inverted_index[term])
            
            # 索引无命中时退化为全量扫描
            if not candidate_ids:
                candidate_ids = set(candidates.keys())
            else:
                # 社区过滤：候选集与社区节点集取交集
                if community:
                    candidate_ids &= set(candidates.keys())
                # 倒排索引退化保护：候选集超过50%时全量扫描更高效
                if len(candidate_ids) > len(candidates) * 0.5:
                    candidate_ids = set(candidates.keys())
        else:
            candidate_ids = set(candidates.keys())

        scored = []
        for nid in candidate_ids:
            if nid not in self.nodes: continue
            node = self.nodes[nid]
            s, match_type = score_node(clean_query, node, en_terms, zh_terms)
            if s > 0:
                scored.append((nid, s, match_type))

        scored.sort(key=lambda x: -x[1])

        direct_hits = []
        for nid, s, match_type in scored[:top_k]:
            node = self.nodes[nid]
            direct_hits.append(Hit(
                node_id=nid,
                label=node.label,
                source_file=node.source_file,
                score=round(s, 1),
                match_type=match_type,
            ))

        related_hits = []
        seen_ids = {h.node_id for h in direct_hits}
        max_related = 5
        related_k = 2

        for hit in direct_hits:
            if len(related_hits) >= max_related:
                break
            for neighbor_id, relation in self.neighbors.get(hit.node_id, [])[:related_k]:
                if neighbor_id not in seen_ids and neighbor_id in self.nodes:
                    seen_ids.add(neighbor_id)
                    neighbor = self.nodes[neighbor_id]
                    related_hits.append(Hit(
                        node_id=neighbor_id,
                        label=neighbor.label,
                        source_file=neighbor.source_file,
                        score=round(hit.score * 0.5, 1),
                        match_type="related",
                        related_from=hit.label,
                        relation_type=relation,
                    ))
                    if len(related_hits) >= max_related:
                        break

        elapsed_ms = (time.perf_counter() - t0) * 1000

        return SearchResult(
            query=query,
            direct_hits=direct_hits,
            related_hits=related_hits,
            graph_used="doc",
            latency_ms=round(elapsed_ms, 1),
        )

    

    def explain(self, node_id: str) -> str:
        node = self.nodes.get(node_id)
        if not node:
            return f"Node {node_id} not found."

        lines = [f"=== {node.label} (layer={node.layer}) ==="]
        lines.append(f"ID: {node.id}")
        if node.label_zh:
            lines.append(f"中文: {node.label_zh}")
        lines.append(f"分类: {node.category}")
        lines.append(f"命名空间: {node.namespace}")
        lines.append(f"层级: {node.layer}")
        lines.append(f"God节点: {node.is_god_node}")
        if node.description_zh:
            lines.append(f"描述(zh): {node.description_zh}")
        if node.description_en:
            lines.append(f"描述(en): {node.description_en}")
        if node.keywords_zh:
            lines.append(f"关键词(zh): {', '.join(node.keywords_zh)}")
        if node.keywords_en:
            lines.append(f"关键词(en): {', '.join(node.keywords_en)}")
        lines.append(f"来源: {node.source_file}")
        lines.append(f"度: {node.degree}")

        neighbors = self.neighbors.get(node_id, [])
        if neighbors:
            lines.append(f"\n连接 ({len(neighbors)}):")
            for nid, relation in neighbors[:10]:
                n = self.nodes.get(nid)
                lines.append(f"  --{relation}--> {n.label if n else nid}")

        return "\n".join(lines)
