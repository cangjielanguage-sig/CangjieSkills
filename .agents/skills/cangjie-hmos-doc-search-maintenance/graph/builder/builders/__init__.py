"""图谱构建编排模块。
实际提取由 doc/ 和 code/ 负责，本模块提供：
- 文件检测（detect）
- 图操作（合并/去重/聚类/分层/保存）
- 缓存
"""
from .detect import detect, detect_incremental, classify_file, FileType, count_words
from .build import (
    build_from_json, build_subgraph, merge_graphs, save_graph,
    deduplicate_by_label, annotate_layers, load_graph,
)
from .cluster import cluster, cohesion_score, score_all, assign_communities_to_nodes
from .cache import load_cached, save_cached, cache_dir, clear_cache

__all__ = [
    "detect", "detect_incremental", "classify_file", "FileType", "count_words",
    "build_from_json", "build_subgraph", "merge_graphs", "save_graph",
    "deduplicate_by_label", "annotate_layers", "load_graph",
    "cluster", "cohesion_score", "score_all", "assign_communities_to_nodes",
    "load_cached", "save_cached", "cache_dir", "clear_cache",
]
