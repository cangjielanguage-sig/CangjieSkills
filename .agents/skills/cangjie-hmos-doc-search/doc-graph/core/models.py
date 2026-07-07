"""数据模型 — 双图统一（doc/code），双语字段严格分离。

本模块定义了 doc-graph 子系统的核心数据结构：
- DocNode/CodeNode: 图谱节点，承载搜索和展示所需的所有元数据
- Edge/EdgeRelation: 边关系，区分确定性边和 LLM 推断边
- Hit/SearchResult: 搜索结果，分为直接命中和关联推荐两类

设计原则：中英文字段严格分离（keywords_zh vs keywords_en），
避免跨语言混淆导致搜索偏差；所有模型均提供 to_dict/from_dict 序列化支持。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


# === 图谱节点模型 ===

@dataclass
class DocNode:
    """文档图谱节点（1文件=1节点）— 代表一篇鸿蒙仓颉开发文档。

    关键设计：
    - 双语分离：keywords_zh/keywords_en 严格分开，搜索时独立匹配
    - layer 分层：1=指南/概览（概念层），2=API/错误码（参考层），打分时概念层权重更高
    - category 定社区：std/stdx/lang/harmonyos/tools，用于查询前缀限定范围
    """
    id: str = ""
    label: str = ""
    label_zh: str = ""
    layer: int = 1                  # 1=指南/概览, 2=API/错误码

    # 双语描述（严格分离）
    description_zh: str = ""
    description_en: str = ""

    # 双语关键词（严格分离，仅搜索词，不含描述）
    keywords_zh: list[str] = field(default_factory=list)
    keywords_en: list[str] = field(default_factory=list)

    category: str = ""              # std/stdx/lang/harmonyos/tools
    namespace: str = ""             # 命名空间（用于 ID 生成和边构建）
    source_file: str = ""

    community_id: int = -1          # 图谱社区检测结果
    degree: int = 0                 # 邻居数量
    is_god_node: bool = False       # 度最高的核心节点标记

    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "id": self.id, "label": self.label, "label_zh": self.label_zh,
            "layer": self.layer,
            "description_zh": self.description_zh, "description_en": self.description_en,
            "keywords_zh": self.keywords_zh, "keywords_en": self.keywords_en,
            "category": self.category, "namespace": self.namespace,
            "source_file": self.source_file,
            "community_id": self.community_id, "degree": self.degree,
            "is_god_node": self.is_god_node, "extra": self.extra,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "DocNode":
        return cls(
            id=d.get("id", ""), label=d.get("label", ""), label_zh=d.get("label_zh", ""),
            layer=d.get("layer", 1),
            description_zh=d.get("description_zh", ""), description_en=d.get("description_en", ""),
            keywords_zh=d.get("keywords_zh", []), keywords_en=d.get("keywords_en", []),
            category=d.get("category", ""), namespace=d.get("namespace", ""),
            source_file=d.get("source_file", ""),
            community_id=d.get("community_id", -1), degree=d.get("degree", 0),
            is_god_node=d.get("is_god_node", False), extra=d.get("extra", {}),
        )


@dataclass
class CodeNode:
    """源码图谱节点（1定义=1节点）— 代表仓颉语言中的一个类型/函数/枚举等代码定义。

    与 DocNode 的关键差异：
    - 无双语分离，keywords 存引用类型名（如 "ArrayList"）
    - methods/fields/enum_values 提供细粒度匹配维度
    - api_kind 区分 class/interface/enum/function/extension/file
    """
    id: str = ""
    label: str = ""
    api_kind: str = ""              # class/interface/enum/struct/function/extension/file

    category: str = ""
    namespace: str = ""             # 命名空间（用于 ID 生成）
    source_file: str = ""

    parent_type: str = ""           # 所属类型（如嵌套类的父类）
    methods: list[str] = field(default_factory=list)
    fields: list[str] = field(default_factory=list)  # 成员变量/属性名
    enum_values: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)  # 引用类型名

    community_id: int = -1
    degree: int = 0

    def to_dict(self) -> dict:
        return {
            "id": self.id, "label": self.label, "api_kind": self.api_kind,
            "category": self.category, "namespace": self.namespace,
            "source_file": self.source_file,
            "parent_type": self.parent_type,
            "methods": self.methods, "fields": self.fields,
            "enum_values": self.enum_values, "keywords": self.keywords,
            "community_id": self.community_id, "degree": self.degree,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "CodeNode":
        return cls(
            id=d.get("id", ""), label=d.get("label", ""), api_kind=d.get("api_kind", ""),
            category=d.get("category", ""), namespace=d.get("namespace", ""),
            source_file=d.get("source_file", ""),
            parent_type=d.get("parent_type", ""),
            methods=d.get("methods", []), fields=d.get("fields", []),
            enum_values=d.get("enum_values", []), keywords=d.get("keywords", []),
            community_id=d.get("community_id", -1), degree=d.get("degree", 0),
        )


# === 边模型 ===

class EdgeRelation(Enum):
    # 确定性边 — 建图时从文档结构/代码引用中提取，置信度高
    CONTAINS = "contains"           # 文档包含子页面/类型包含成员
    SEE_ALSO = "see_also"           # 文档间的交叉引用
    EXTENDS = "extends"             # 类继承关系
    EXTENSION_OF = "extension_of"   # 扩展关系
    USES = "uses"                    # 代码中使用/引用关系
    # LLM 语义边 — 由大模型推断，置信度较低
    RECOMMENDS_API = "recommends_api"              # 推荐搭配使用的 API
    ALTERNATIVE_TO = "alternative_to"              # 可替代方案
    TYPICALLY_USED_WITH = "typically_used_with"    # 常见组合使用
    SEMANTICALLY_SIMILAR_TO = "semantically_similar_to"  # 语义相似


@dataclass
class Edge:
    """边 — 描述两个节点之间的关系。

    confidence 三级分类：
    - EXTRACTED: 从文档结构/代码引用中确定性提取
    - INFERRED: LLM 推断（如推荐搭配）
    - AMBIGUOUS: 模糊推断，需要人工审核
    """
    source: str = ""
    target: str = ""
    relation: str = ""
    source_file: str = ""
    confidence: str = "EXTRACTED"     # EXTRACTED | INFERRED | AMBIGUOUS
    confidence_score: float = 1.0
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "source": self.source, "target": self.target,
            "relation": self.relation, "source_file": self.source_file,
            "confidence": self.confidence, "confidence_score": self.confidence_score,
            "description": self.description,
        }


# === 搜索结果模型 ===

@dataclass
class Hit:
    """单次命中结果。"""
    node_id: str
    label: str
    source_file: str
    score: float
    match_type: str = ""            # "label" | "keyword" | "description"
    related_from: str = ""          # 关联推荐时，来源节点标签
    relation_type: str = ""         # 关联边类型


@dataclass
class SearchResult:
    """搜索结果 — 将直接命中与关联推荐分离输出。

    设计逻辑：直接命中是基于查询词的语义匹配结果，
    关联推荐是基于直接命中节点的邻居边扩展，分数减半（*0.5）。
    这样用户既能看到精确匹配，也能发现上下文相关的知识。
    """
    query: str
    direct_hits: list[Hit] = field(default_factory=list)
    related_hits: list[Hit] = field(default_factory=list)
    graph_used: str = ""            # "doc" | "code" | "merged"
    latency_ms: float = 0.0

    # 兼容旧接口：paths / nodes，方便上层代码平滑迁移
    @property
    def paths(self) -> list[str]:
        """所有命中结果对应的文件路径列表（直接命中 + 关联推荐）。"""
        return [h.source_file for h in self.direct_hits] + [h.source_file for h in self.related_hits]

    @property
    def nodes(self) -> list:
        """返回兼容的节点列表（dict 形态）。"""
        result = []
        for h in self.direct_hits:
            result.append({"id": h.node_id, "label": h.label, "source_file": h.source_file, "score": h.score})
        for h in self.related_hits:
            result.append({"id": h.node_id, "label": h.label, "source_file": h.source_file, "score": h.score, "related_from": h.related_from})
        return result

    def to_brief_text(self) -> str:
        """Brief 模式输出（Agent 默认使用）。"""
        lines = []
        if self.direct_hits:
            lines.append(f"=== 直接命中 ({len(self.direct_hits)}) ===")
            for h in self.direct_hits:
                lines.append(f"[{h.score:.1f}] {h.label} | {h.source_file}")
        if self.related_hits:
            lines.append(f"\n=== 关联推荐 ({len(self.related_hits)}) ===")
            for h in self.related_hits:
                from_str = f" (来自 {h.related_from}"
                if h.relation_type:
                    from_str += f", {h.relation_type}"
                from_str += ")"
                lines.append(f"[{h.score:.1f}] {h.label} | {h.source_file}{from_str}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        """JSON 输出 — 与 unified_search.SearchResult.to_dict() 对齐。"""
        def hit_dict(h):
            d = {"label": h.label, "source_file": h.source_file, "score": h.score}
            if h.related_from:
                d["related_from"] = h.related_from
            if h.relation_type:
                d["relation_type"] = h.relation_type
            return d
        return {
            "query": self.query,
            "engine": "graph",
            "graph_used": self.graph_used,
            "latency_ms": self.latency_ms,
            "direct_hits": [hit_dict(h) for h in self.direct_hits],
            "related_hits": [hit_dict(h) for h in self.related_hits],
        }

    def to_full_text(self) -> str:
        """完整模式输出。"""
        lines = [f"查询: {self.query}", f"图谱: {self.graph_used}", f"耗时: {self.latency_ms:.1f}ms"]
        lines.append(self.to_brief_text())
        return "\n".join(lines)



