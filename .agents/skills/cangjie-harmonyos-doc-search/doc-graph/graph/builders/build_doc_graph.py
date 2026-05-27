"""文档图谱构建器（1文件=1节点）."""

from __future__ import annotations

from pathlib import Path

from core.graph import DocGraph
from core.doc_extractor import extract_doc_node, extract_overview_nodes, extract_relations


def build_doc_graph(doc_dirs: list[Path]) -> DocGraph:
    """构建文档图谱（1文件=1节点）.
    
    Args:
        doc_dirs: 文档目录列表 (e.g., [harmonyos_dir, std_dir, stdx_dir])
    """
    cg = DocGraph()
    all_nodes = []
    all_edges = []

    md_files = []
    for d in doc_dirs:
        md_files.extend(sorted(d.rglob("*.md")))
    md_files = sorted(list(set(md_files))) # Deduplicate and sort

    # Determine the common root directory for relative paths.
    # If doc_dirs contains subdirs of a common parent, use that parent.
    # Otherwise, use the first directory.
    if len(doc_dirs) > 1:
        # Try to find a common parent. 
        # For simplicity in this context, we assume doc_dirs are siblings under a common root.
        # e.g. [.../cangjie-harmonyos-doc-search/harmonyos..., .../std]
        # We can use the parent of the first dir if they share it, or just use the first dir's parent.
        # A robust way: resolve all and find common path.
        resolved = [d.resolve() for d in doc_dirs]
        common = resolved[0]
        for r in resolved[1:]:
            while not r.is_relative_to(common) and common != common.parent:
                common = common.parent
        root_dir = common
    else:
        root_dir = doc_dirs[0].resolve()

    print(f"  Using root directory for paths: {root_dir}")

    # 1. 先处理 overview 文件（创建 God Node 和 CONTAINS 边）
    for md in md_files:
        if md.name.startswith(".overview"):
            try:
                nodes, edges = extract_overview_nodes(md, root_dir)
                all_nodes.extend(nodes)
                all_edges.extend(edges)
            except Exception:
                pass

    # 2. 处理普通文档文件
    for md in md_files:
        if md.name.startswith(".overview") or md.name.startswith(".abstract"):
            continue
        try:
            node = extract_doc_node(md, root_dir)
            if node:
                all_nodes.append(node)
                all_edges.extend(extract_relations(md, root_dir))
        except Exception:
            pass

    # 3. 去重（按 ID）
    seen_ids: set[str] = set()
    for n in all_nodes:
        if n.id not in seen_ids:
            seen_ids.add(n.id)
            cg.add_node(n)

    # 4. 添加边（只添加两端都存在的边）
    for e in all_edges:
        if e.source in seen_ids and e.target in seen_ids:
            cg.add_edge(e)

    cg.compute_degrees()
    return cg
