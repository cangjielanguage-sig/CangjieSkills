"""搜索辅助函数 — 中英文分词与社区前缀解析。

本模块提供所有搜索引擎（DocSearchEngine/CodeSearchEngine）共享的辅助函数：
- _parse_community_prefix: 从查询中提取社区前缀（如 "std.List" → 社区 std, 查询 List）
- _tokenize_zh/_tokenize_en: 中英文分词器

关联推荐算法（各引擎内置）：对每个直接命中节点取前 2 个邻居，分数减半，最多 5 个关联结果。
"""
from __future__ import annotations

import re

from core.constants import COMMUNITIES


def _parse_community_prefix(query: str) -> tuple[str | None, str]:
    """从查询中提取社区前缀并分离。

    例如 "std.List" → ("std", "List"), "harmonyos.camera" → ("harmonyos", "camera")
    无前缀的查询如 "List 列表" → (None, "List 列表")
    返回的 community 用于过滤候选节点集，clean_query 用于实际搜索。
    """
    for comm in COMMUNITIES:
        match = re.match(rf"^{comm}[\.\s]+", query, re.IGNORECASE)
        if match:
            return comm, query[match.end():]
    return None, query


def _tokenize_zh(query: str) -> list[str]:
    """中文分词 — 提取连续中文字符段作为词元。"""
    return re.findall(r"[\u4e00-\u9fff]+", query)


def _tokenize_en(query: str) -> list[str]:
    """英文分词 — 提取标识符和普通单词，支持 @开头的仓颉注解名。"""
    return re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z_][A-Za-z0-9_]*", query)
