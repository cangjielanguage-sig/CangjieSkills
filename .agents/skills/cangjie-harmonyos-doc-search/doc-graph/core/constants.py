"""项目级共享常量。集中所有硬编码表，避免重复定义。"""

COMMUNITIES = ["std", "stdx", "lang", "harmonyos", "tools"]

LAYER_NAMES = {1: "概念", 2: "API"}
LAYER_NAMES_FULL = {1: "概念层", 2: "API 层"}

DOC_LAYER_WEIGHTS = {1: 2.5, 2: 1.8}

CODE_KIND_MAP = {
    "class": "class",
    "interface": "interface",
    "enum": "enum",
    "function": "function",
    "func": "function",
    "extension": "extension",
}

L1_KEYWORDS = {"overview", "guide", "tutorial", "概览", "指南", "介绍"}
L2_KEYWORDS = {"class", "interface", "struct", "enum", "component", "api", "reference"}

COMMUNITY_COLORS = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
]

DEFAULT_GRAPH_DIR = "data"
DEFAULT_GRAPH_PATH = "data/merged/graph.json"