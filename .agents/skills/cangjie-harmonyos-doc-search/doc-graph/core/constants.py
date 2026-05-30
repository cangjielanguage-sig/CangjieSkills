"""项目级共享常量 — 集中所有硬编码配置表，避免重复定义与不一致。

本模块定义了 doc-graph 子系统中所有搜索引擎、引擎插件和 CLI 共用的常量。
修改这些值会影响搜索打分权重、节点分类逻辑和导出配色等全局行为。
"""

# 五大知识社区：标准库/扩展标准库/语言特性/鸿蒙平台/工具链
# 搜索引擎可通过查询前缀 "std.List" 限定社区范围
COMMUNITIES = ["std", "stdx", "lang", "harmonyos", "tools"]

# 图谱层级缩写与全称，用于 CLI 输出和节点解释
# layer 1 = 概念性文档（指南/概览），layer 2 = 具体API/错误码
LAYER_NAMES = {1: "概念", 2: "API"}
LAYER_NAMES_FULL = {1: "概念层", 2: "API 层"}

# 文档图搜索打分时对不同层级的加权系数
# 概念层权重更高（2.5），因为指南性文档通常对用户更有价值
DOC_LAYER_WEIGHTS = {1: 2.5, 2: 1.8}

# 源码图 api_kind 映射：将查询中的关键词映射到节点类型
# "func" 是仓颉语言中函数声明的关键词，映射到统一的 "function"
CODE_KIND_MAP = {
    "class": "class",
    "interface": "interface",
    "enum": "enum",
    "function": "function",
    "func": "function",
    "extension": "extension",
}

# 层级判定关键词：出现这些词的节点归入对应层级
L1_KEYWORDS = {"overview", "guide", "tutorial", "概览", "指南", "介绍"}
L2_KEYWORDS = {"class", "interface", "struct", "enum", "component", "api", "reference"}

# 社区配色方案（Tableau 10），用于 HTML 导出时的节点颜色
COMMUNITY_COLORS = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
]

# 默认图谱数据目录和路径（相对于 doc-graph/ 目录）
DEFAULT_GRAPH_DIR = "data"
DEFAULT_GRAPH_PATH = "data/merged/graph.json"