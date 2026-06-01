#!/usr/bin/env python3
"""验证图谱数据完整性。检查 graph.json 文件是否存在且结构正确。"""
import json
import sys
from pathlib import Path

MAINTENANCE_DIR = Path(__file__).resolve().parent.parent.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-harmonyos-doc-search"
DOC_GRAPH_DATA_DIR = SEARCH_SKILL_DIR / "doc-graph" / "data"

def validate_graph(graph_path: Path) -> list[str]:
    if not graph_path.exists():
        return [f"文件不存在: {graph_path}"]
    try:
        data = json.loads(graph_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"JSON 解析失败: {graph_path}: {e}"]

    issues = []
    nodes = data.get("nodes", {})
    if isinstance(nodes, dict):
        node_count = len(nodes)
    elif isinstance(nodes, list):
        node_count = len(nodes)
    else:
        issues.append(f"nodes 字段类型异常: {type(nodes)}")
        node_count = 0

    edges = data.get("edges", data.get("links", []))
    edge_count = len(edges) if isinstance(edges, list) else 0

    if node_count == 0:
        issues.append("图谱无节点")
    if edge_count == 0 and node_count > 5:
        issues.append("图谱无边 (节点>5却无边，可能提取不完整)")

    print(f"  {graph_path.name}: {node_count} 节点, {edge_count} 边")
    return issues


def main():
    all_issues = []
    for name in ["doc/graph.json", "code/graph.json", "merged/graph.json"]:
        path = DOC_GRAPH_DATA_DIR / name
        issues = validate_graph(path)
        all_issues.extend(issues)

    if all_issues:
        print("\n问题:")
        for issue in all_issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print("\n图谱数据验证通过")


if __name__ == "__main__":
    main()