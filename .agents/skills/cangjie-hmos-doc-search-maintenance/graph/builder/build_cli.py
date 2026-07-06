#!/usr/bin/env python3
"""知识图谱构建 CLI — 迁自 doc-graph/cli.py 的 build 子命令。

本模块是 graph 分区维护流水线中图谱构建的命令行入口，提供以下子命令：
- build-doc: 从文档语料构建文档图谱（核心流程）
- build-code: 从源码语料构建代码图谱
- merge: 合并 doc 和 code 子图谱为 merged 图谱
- enhance-graph: LLM 增强图谱节点标签/描述/关键词
- build: 全量构建（doc → merge → 可选 enhance）

跨分区依赖：调用 doc/builder.py（文档图谱构建）、llm/pipeline.py（LLM 增强）、
builders 模块（子图构建、聚类、合并）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAINTENANCE_DIR = Path(__file__).resolve().parent.parent.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-hmos-doc-search"
DOC_GRAPH_DIR = SEARCH_SKILL_DIR / "doc-graph"
BUILDER_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(BUILDER_DIR))
sys.path.insert(0, str(DOC_GRAPH_DIR))

from core.models import DocNode, CodeNode, Edge
from doc.builder import build_doc_graph
from code.builder import build_code_graph
from builders import merge_graphs, save_graph


def post_filter_graph(graph_path: Path) -> int:
    """后处理：用 extractor.py 的停词表过滤 graph.json 的噪声关键词。

    对 keywords_en 应用 EN_STOP_WORDS，对 keywords_zh 应用 TITLE_STOP_ZH。
    返回清除的噪声词总数。
    """
    if not EXTRACTOR_PATH.exists():
        print(f"  [post-filter] 跳过: 找不到 extractor.py ({EXTRACTOR_PATH})")
        return 0

    src = EXTRACTOR_PATH.read_text(encoding="utf-8")
    m_en = re.search(r"EN_STOP_WORDS\s*=\s*\{([^}]+)\}", src, re.DOTALL)
    m_zh = re.search(r"TITLE_STOP_ZH\s*=\s*\{([^}]+)\}", src, re.DOTALL)
    if not m_en or not m_zh:
        print("  [post-filter] 跳过: 无法解析停词表")
        return 0

    # Safe eval of set literals
    en_stop = eval("{" + m_en.group(1) + "}")
    zh_stop = eval("{" + m_zh.group(1) + "}")

    with open(graph_path, encoding="utf-8") as f:
        g = json.load(f)

    removed = 0
    for node in g.get("nodes", []):
        old_en = node.get("keywords_en", [])
        node["keywords_en"] = [k for k in old_en if k.lower() not in en_stop]
        removed += len(old_en) - len(node["keywords_en"])

        old_zh = node.get("keywords_zh", [])
        node["keywords_zh"] = [k for k in old_zh if k not in zh_stop]
        removed += len(old_zh) - len(node["keywords_zh"])

    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=2)

    print(f"  [post-filter] 清除 {removed} 个噪声关键词")
    return removed


def cmd_build_doc(args):
    """构建文档图谱。支持两种场景：
    - 单目录：顶层有 .md 文件或仅一个子目录时直接构建
    - 多子目录：顶层无 .md 但有多个子目录时，分别构建后合并节点和邻接表

    构建流程：extract → build_subgraph → cluster → annotate_layers → save。
    """
    root_dir = Path(args.docs_dir)
    if not root_dir.is_dir():
        print(f"错误: 文档语料目录不存在: {root_dir}")
        sys.exit(1)
    output_path = Path(args.output) if args.output else DOC_GRAPH_DIR / "data" / "doc" / "graph.json"

    sub_dirs = sorted([d for d in root_dir.iterdir() if d.is_dir() and any(f.suffix == '.md' for f in d.rglob('*.md'))])
    has_top_level_md = any(f.suffix == '.md' for f in root_dir.iterdir() if f.is_file())

    if not has_top_level_md and len(sub_dirs) == 1:
        root_dir = sub_dirs[0]
        print(f"顶层无 .md 文件，仅 1 个子目录，使用子目录作为 root: {root_dir.name}")

    if not has_top_level_md and len(sub_dirs) > 1:
        print(f"检测到 {len(sub_dirs)} 个文档子目录，分别构建后合并")
        all_nodes: dict[str, DocNode] = {}
        all_neighbors: dict[str, list[tuple[str, str]]] = {}
        for sub_dir in sub_dirs:
            print(f"  构建子目录: {sub_dir.name}")
            sub_nodes, sub_neighbors = build_doc_graph(sub_dir, use_cache=args.use_cache)
            all_nodes.update(sub_nodes)
            for nid, nbrs in sub_neighbors.items():
                all_neighbors[nid] = all_neighbors.get(nid, []) + nbrs
        from builders.build import build_subgraph
        G = build_subgraph(all_nodes, all_neighbors, {}, {}, directed=False)
    else:
        print(f"构建文档图谱: {root_dir}")
        nodes, neighbors = build_doc_graph(root_dir, use_cache=args.use_cache)
        from builders.build import build_subgraph
        G = build_subgraph(nodes, neighbors, {}, {}, directed=False)

    from builders.cluster import cluster, assign_communities_to_nodes
    communities = cluster(G)
    assign_communities_to_nodes(G, communities)
    from builders.build import annotate_layers
    annotate_layers(G)
    save_graph(G, output_path)
    print(f"完成: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")


def cmd_build_code(args):
    root_dir = Path(args.code_dir)
    if not root_dir.is_dir():
        print(f"错误: 源码语料目录不存在: {root_dir}")
        sys.exit(1)
    output_path = Path(args.output) if args.output else DOC_GRAPH_DIR / "data" / "code" / "graph.json"
    print(f"构建源码图谱: {root_dir}")
    nodes, neighbors = build_code_graph(root_dir)
    from builders.build import build_subgraph
    G = build_subgraph({}, {}, nodes, neighbors, directed=False)
    save_graph(G, output_path)
    print(f"完成: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")


def cmd_merge(args):
    graph_dir = Path(args.graph_dir) if args.graph_dir else DOC_GRAPH_DIR / "data"
    doc_path = graph_dir / "doc" / "graph.json"
    code_path = graph_dir / "code" / "graph.json"
    merged_path = graph_dir / "merged" / "graph.json"
    paths = []
    if doc_path.exists():
        paths.append(doc_path)
    if code_path.exists():
        paths.append(code_path)
    if not paths:
        print(f"错误: 未找到子图谱文件 ({doc_path}, {code_path})")
        sys.exit(1)
    print(f"合并图谱: {paths}")
    merge_graphs(paths, merged_path)
    print(f"完成: 合并图谱保存至 {merged_path}")


def cmd_enhance(args):
    """LLM 增强图谱：读取现有图谱，对每个节点的 source_file 调用 LLM
    提取更准确的标签、描述和关键词，原地更新图谱文件。
    优先使用 merged 图谱，不存在则使用 doc 图谱。"""
    graph_dir = Path(args.graph_dir) if args.graph_dir else DOC_GRAPH_DIR / "data"
    merged_path = graph_dir / "merged" / "graph.json"
    doc_path = graph_dir / "doc" / "graph.json"
    source_path = None
    for candidate in [merged_path, doc_path]:
        if candidate.exists():
            source_path = candidate
            break
    if not source_path:
        print(f"错误: 未找到图谱文件")
        sys.exit(1)
    graph_data = json.loads(source_path.read_text(encoding="utf-8"))
    docs_dir = Path(args.docs_dir) if args.docs_dir else None
    from llm.pipeline import enhance_graph_from_files
    source_files = [n.get("source_file", "") for n in graph_data.get("nodes", []) if n.get("source_file")]
    enhance_graph_from_files(
        graph_data, source_files, docs_dir or Path("."),
        max_workers=args.max_workers,
        batch_limit=args.batch_limit,
        output_path=source_path,
    )


def cmd_build(args):
    """全量构建流程：doc → 可选 code → merge → 可选 enhance。
    依次调用 cmd_build_doc、cmd_build_code、cmd_merge、cmd_enhance。"""
    docs_dir = Path(args.docs_dir)
    graph_dir = Path(args.graph_dir) if args.graph_dir else DOC_GRAPH_DIR / "data"
    print(f"=== 全量构建流程 ===")
    print(f"文档语料: {docs_dir}")
    print(f"输出目录: {graph_dir}")

    doc_output = graph_dir / "doc" / "graph.json"
    cmd_build_doc(argparse.Namespace(docs_dir=str(docs_dir), output=str(doc_output), use_cache=args.use_cache))

    if args.code_dir:
        code_output = graph_dir / "code" / "graph.json"
        cmd_build_code(argparse.Namespace(code_dir=args.code_dir, output=str(code_output)))

    cmd_merge(argparse.Namespace(graph_dir=str(graph_dir)))

    if args.enhance:
        cmd_enhance(argparse.Namespace(graph_dir=str(graph_dir), docs_dir=args.docs_dir, max_workers=args.max_workers, batch_limit=args.batch_limit))

    post_filter_graph(doc_output)

    print(f"\n=== 构建完成! 图谱保存在 {graph_dir} ===")


def main():
    parser = argparse.ArgumentParser(description="知识图谱构建 CLI")
    subparsers = parser.add_subparsers(dest="command")

    p_build_doc = subparsers.add_parser("build-doc", help="构建文档图谱")
    p_build_doc.add_argument("--docs-dir", required=True, help="文档语料目录")
    p_build_doc.add_argument("--output", help="输出路径 (默认 doc-graph/data/doc/graph.json)")
    p_build_doc.add_argument("--use-cache", action="store_true", default=True, help="使用缓存（改 extractor.py 后需清除 docs/.../graphify-out/cache/ 或传 --no-use-cache）")
    p_build_doc.add_argument("--no-use-cache", action="store_false", dest="use_cache", help="强制重建，不使用缓存")
    p_build_doc.set_defaults(func=cmd_build_doc)

    p_build_code = subparsers.add_parser("build-code", help="构建源码图谱")
    p_build_code.add_argument("--code-dir", required=True, help="源码语料目录")
    p_build_code.add_argument("--output", help="输出路径 (默认 doc-graph/data/code/graph.json)")
    p_build_code.set_defaults(func=cmd_build_code)

    p_merge = subparsers.add_parser("merge", help="合并子图谱")
    p_merge.add_argument("--graph-dir", help="图谱数据目录 (默认 doc-graph/data)")
    p_merge.set_defaults(func=cmd_merge)

    p_enhance = subparsers.add_parser("enhance-graph", help="LLM 增强图谱")
    p_enhance.add_argument("--graph-dir", help="图谱数据目录")
    p_enhance.add_argument("--docs-dir", help="文档语料目录 (用于读取原文)")
    p_enhance.add_argument("--max-workers", type=int, default=5)
    p_enhance.add_argument("--batch-limit", type=int, default=0, help="批次限制 (0=不限制)")
    p_enhance.set_defaults(func=cmd_enhance)

    p_build = subparsers.add_parser("build", help="全量构建 (doc + code + merge + enhance)")
    p_build.add_argument("--docs-dir", required=True, help="文档语料目录")
    p_build.add_argument("--code-dir", help="源码语料目录 (可选)")
    p_build.add_argument("--graph-dir", help="图谱数据目录")
    p_build.add_argument("--use-cache", action="store_true", default=True)
    p_build.add_argument("--enhance", action="store_true", help="运行 LLM 增强")
    p_build.add_argument("--max-workers", type=int, default=5)
    p_build.add_argument("--batch-limit", type=int, default=0)
    p_build.set_defaults(func=cmd_build)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()