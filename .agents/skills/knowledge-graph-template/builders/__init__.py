"""图谱构建模块。整合自 graphify，包含完整的提取、构建、验证、安全功能。"""
from .detect import detect, detect_incremental, classify_file, FileType, count_words
from .build import build, build_from_json, build_merge, merge_graphs, save_graph, deduplicate_by_label, annotate_layers, load_graph
from .cluster import cluster, cohesion_score, score_all, assign_communities_to_nodes
from .cache import load_cached, save_cached, cache_dir, clear_cache, check_semantic_cache, save_semantic_cache
from .extract_ast import extract, collect_files
from .extract_semantic import extract_docs_simple
from .extract_semantic_llm import extract_docs_with_llm, extract_docs_with_llm_sync, LLMConfig
from .validate import validate_extraction, assert_valid, VALID_FILE_TYPES, VALID_CONFIDENCES
from .security import sanitize_label, validate_url, safe_fetch, safe_fetch_text, validate_graph_path

__all__ = [
    "detect",
    "detect_incremental",
    "classify_file",
    "FileType",
    "count_words",
    "build",
    "build_from_json",
    "build_merge",
    "merge_graphs",
    "save_graph",
    "deduplicate_by_label",
    "annotate_layers",
    "load_graph",
    "cluster",
    "cohesion_score",
    "score_all",
    "assign_communities_to_nodes",
    "load_cached",
    "save_cached",
    "cache_dir",
    "clear_cache",
    "check_semantic_cache",
    "save_semantic_cache",
    "extract",
    "collect_files",
    "extract_docs_simple",
    "extract_docs_with_llm",
    "extract_docs_with_llm_sync",
    "LLMConfig",
    "validate_extraction",
    "assert_valid",
    "VALID_FILE_TYPES",
    "VALID_CONFIDENCES",
    "sanitize_label",
    "validate_url",
    "safe_fetch",
    "safe_fetch_text",
    "validate_graph_path",
]