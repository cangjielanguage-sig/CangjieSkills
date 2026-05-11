#!/usr/bin/env python3
"""把 V3 卡片索引里的高价值规则导出为 graphify 图谱的"种子"文件。

产物包含两部分：
    1. nodes 种子：V3 里的 task / api 节点定义（id / label / aliases / source_paths）。
       图谱构建时优先使用这些 id，避免 LLM 抽取把 `List` 和 `arkui.list` 拆成两个节点。
    2. edges 种子：task -> recommended_apis 的 INFERRED 边，
       给图谱补上跨文档的组合关系（做 X 功能 需要 哪些 API），
       这是冒烟测试里 graphify 单跑失败的根因。

同时提供 --validate 模式：检查现有图谱里 V3 的高价值节点是否都对上。

用法：
    # 生成种子
    python sync_v3_to_graph.py --output /tmp/v3_seeds.json

    # 校验现有图谱
    python sync_v3_to_graph.py --validate \\
        --graph ../knowledge-graph-template/data/merged/graph.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_INDEX_DIR = SKILL_DIR / "index"


def _normalize_id(raw: str) -> str:
    """和 graphify extract_ast._make_id 对齐的 id 归一化。"""
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", raw)
    return cleaned.strip("_").lower()


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def build_seeds(index_dir: Path) -> dict[str, Any]:
    tasks = _load_jsonl(index_dir / "tasks.jsonl")
    apis = _load_jsonl(index_dir / "apis.jsonl")

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    for api in apis:
        api_id = api.get("api_id", "")
        if not api_id:
            continue
        nodes.append({
            "id": _normalize_id(api_id),
            "label": api.get("name") or api_id,
            "file_type": "api",
            "layer": 2,
            "source_paths": api.get("source_paths", []),
            "aliases": api.get("aliases", []),
            "module": api.get("module", ""),
            "kind": api.get("kind", ""),
            "v3_api_id": api_id,
        })
        for related in api.get("related_apis", []):
            edges.append({
                "source": _normalize_id(api_id),
                "target": _normalize_id(related),
                "relation": "RELATED_API",
                "origin": "v3_seed",
            })

    for task in tasks:
        task_id = task.get("task_id", "")
        if not task_id:
            continue
        nodes.append({
            "id": _normalize_id(task_id),
            "label": task.get("title") or task_id,
            "file_type": "task",
            "layer": 1,
            "source_paths": task.get("source_paths", []),
            "aliases": task.get("aliases", []),
            "when_to_use": task.get("when_to_use", []),
            "v3_task_id": task_id,
        })
        for rec_api in task.get("recommended_apis", []):
            edges.append({
                "source": _normalize_id(task_id),
                "target": _normalize_id(rec_api),
                "relation": "RECOMMENDS_API",
                "origin": "v3_seed",
            })
        for opt_api in task.get("optional_apis", []):
            edges.append({
                "source": _normalize_id(task_id),
                "target": _normalize_id(opt_api),
                "relation": "OPTIONAL_API",
                "origin": "v3_seed",
            })

    return {
        "generated_from": str(index_dir),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": edges,
    }


def validate_against_graph(seeds: dict[str, Any], graph_path: Path) -> dict[str, Any]:
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    graph_ids: set[str] = {n.get("id", "") for n in graph.get("nodes", [])}
    graph_labels: dict[str, str] = {n.get("label", ""): n.get("id", "") for n in graph.get("nodes", [])}

    missing: list[dict[str, str]] = []
    label_matches: list[dict[str, str]] = []
    exact_matches = 0

    for seed in seeds["nodes"]:
        sid = seed["id"]
        label = seed["label"]
        if sid in graph_ids:
            exact_matches += 1
            continue
        if label and label in graph_labels:
            label_matches.append({
                "seed_id": sid,
                "label": label,
                "graph_id": graph_labels[label],
            })
            continue
        missing.append({
            "seed_id": sid,
            "label": label,
            "file_type": seed.get("file_type", ""),
            "module": seed.get("module", ""),
        })

    total = len(seeds["nodes"])
    report = {
        "graph": str(graph_path),
        "total_seeds": total,
        "exact_id_matches": exact_matches,
        "label_only_matches": len(label_matches),
        "missing": len(missing),
        "missing_ratio": round(len(missing) / total, 3) if total else 0.0,
        "missing_samples": missing[:20],
        "label_only_samples": label_matches[:10],
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="V3 → graphify 种子注入")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR, help="V3 索引目录")
    parser.add_argument("--output", type=Path, help="种子 JSON 输出路径")
    parser.add_argument("--validate", action="store_true", help="校验模式：比对现有图谱")
    parser.add_argument("--graph", type=Path, help="校验模式下的图谱 json 路径")
    args = parser.parse_args()

    seeds = build_seeds(args.index_dir)

    if args.validate:
        if not args.graph or not args.graph.exists():
            print("--validate requires --graph pointing to an existing graph.json", file=sys.stderr)
            sys.exit(2)
        report = validate_against_graph(seeds, args.graph)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(0 if report["missing_ratio"] < 0.3 else 1)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(seeds, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote seeds: nodes={seeds['node_count']} edges={seeds['edge_count']} -> {args.output}")
    else:
        print(json.dumps({
            "node_count": seeds["node_count"],
            "edge_count": seeds["edge_count"],
            "sample_nodes": seeds["nodes"][:3],
            "sample_edges": seeds["edges"][:5],
        }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
