#!/usr/bin/env python3
"""盘点 doc-search 当前索引对 API 候选文档的结构化覆盖率。"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = SEARCH_SKILL_DIR / "doc-card"
DOCS_DIR = SEARCH_SKILL_DIR / "docs"
BUILDER_DIR = MAINTENANCE_DIR / "builder"
API_COVERAGE_DIR = MAINTENANCE_DIR / "records" / "api-coverage"

sys.path.insert(0, str(BUILDER_DIR))

from build_index_v3 import DOC_SOURCES, api_kind_from_path, discover_docs  # noqa: E402


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def path_group(path: str) -> str:
    parts = path.split("/")
    if len(parts) >= 2:
        return "/".join(parts[:2])
    return parts[0]


def ratio(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 4)


def sample_paths(paths: list[str], limit: int = 30) -> list[str]:
    return sorted(paths)[:limit]


def build_report(index_dir: Path, gate_threshold: float = 1.0) -> dict:
    docs = discover_docs(DOCS_DIR)
    all_doc_paths = {record.path for record in docs}

    candidate_rows = []
    for record in docs:
        candidate_kind = api_kind_from_path(record.path)
        if candidate_kind:
            candidate_rows.append(
                {
                    "path": record.path,
                    "source": record.source,
                    "group": path_group(record.path),
                    "kind": candidate_kind,
                    "title": record.title,
                }
            )

    candidate_paths = {row["path"] for row in candidate_rows}
    candidate_by_path = {row["path"]: row for row in candidate_rows}
    candidates_by_source = Counter(row["source"] for row in candidate_rows)
    candidates_by_kind = Counter(row["kind"] for row in candidate_rows)
    candidates_by_group = Counter(row["group"] for row in candidate_rows)

    apis = load_jsonl(index_dir / "apis.jsonl")
    covered_paths: set[str] = set()
    invalid_source_paths: set[str] = set()
    cards_with_invalid_source_paths: list[dict] = []
    duplicate_source_path_hits: dict[str, list[str]] = defaultdict(list)
    duplicate_name_hits: dict[str, list[str]] = defaultdict(list)

    for row in apis:
        api_id = row["api_id"]
        api_name = row.get("name") or row.get("title") or api_id
        duplicate_name_hits[api_name.lower()].append(api_id)
        invalid_for_row = []
        for path in row.get("source_paths", []):
            if path not in all_doc_paths:
                invalid_source_paths.add(path)
                invalid_for_row.append(path)
                continue
            if path in candidate_paths:
                covered_paths.add(path)
                duplicate_source_path_hits[path].append(api_id)
        if invalid_for_row:
            cards_with_invalid_source_paths.append(
                {
                    "api_id": api_id,
                    "name": api_name,
                    "invalid_source_paths": invalid_for_row,
                }
            )

    uncovered_paths = sorted(candidate_paths - covered_paths)
    covered_by_source = Counter(candidate_by_path[path]["source"] for path in covered_paths)
    covered_by_kind = Counter(candidate_by_path[path]["kind"] for path in covered_paths)
    uncovered_by_group = Counter(candidate_by_path[path]["group"] for path in uncovered_paths)

    duplicate_candidate_source_path_hits = {
        path: api_ids
        for path, api_ids in duplicate_source_path_hits.items()
        if len(api_ids) > 1
    }
    duplicate_name_hits = {
        name: api_ids
        for name, api_ids in duplicate_name_hits.items()
        if len(api_ids) > 1
    }

    gate_reasons: list[str] = []
    coverage_value = ratio(len(covered_paths), len(candidate_paths))
    if coverage_value < gate_threshold:
        gate_reasons.append(
            f"候选 API 覆盖率未达标: {coverage_value:.2%} < {gate_threshold:.2%}"
        )
    if invalid_source_paths:
        gate_reasons.append(f"api card 存在无效 source_paths: {len(invalid_source_paths)}")
    gate = {
        "threshold": gate_threshold,
        "passed": not gate_reasons,
        "reasons": gate_reasons,
    }

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "search_skill_dir": str(SEARCH_SKILL_DIR),
        "index_dir": str(index_dir),
        "sources": list(DOC_SOURCES),
        "candidates": {
            "total_docs": len(candidate_paths),
            "covered_docs": len(covered_paths),
            "uncovered_docs": len(uncovered_paths),
            "coverage_ratio": coverage_value,
            "by_source": {
                source: {
                    "total_docs": candidates_by_source[source],
                    "covered_docs": covered_by_source[source],
                    "coverage_ratio": ratio(covered_by_source[source], candidates_by_source[source]),
                }
                for source in DOC_SOURCES
            },
            "by_kind": {
                kind: {
                    "total_docs": candidates_by_kind[kind],
                    "covered_docs": covered_by_kind[kind],
                    "coverage_ratio": ratio(covered_by_kind[kind], candidates_by_kind[kind]),
                }
                for kind in sorted(candidates_by_kind)
            },
        },
        "integrity": {
            "invalid_source_paths": sorted(invalid_source_paths),
            "cards_with_invalid_source_paths": cards_with_invalid_source_paths[:100],
            "duplicate_candidate_source_path_hits": duplicate_candidate_source_path_hits,
            "duplicate_name_hits": duplicate_name_hits,
        },
        "top_uncovered_groups": [
            {
                "group": group,
                "uncovered_docs": count,
                "total_candidate_docs": candidates_by_group[group],
                "coverage_ratio": ratio(candidates_by_group[group] - count, candidates_by_group[group]),
            }
            for group, count in uncovered_by_group.most_common(30)
        ],
        "samples": {
            "uncovered_candidate_paths": sample_paths(uncovered_paths, limit=100),
            "covered_candidate_paths": sample_paths(sorted(covered_paths), limit=50),
            "duplicate_candidate_paths": sample_paths(sorted(duplicate_candidate_source_path_hits), limit=50),
        },
        "gate": gate,
    }


def markdown_report(report: dict) -> str:
    candidates = report["candidates"]
    gate = report["gate"]
    lines = [
        "# doc-search API Coverage Audit",
        "",
        f"- generated_at: {report['generated_at']}",
        f"- index_dir: `{report['index_dir']}`",
        f"- search_skill_dir: `{report['search_skill_dir']}`",
        "",
        "## 总览",
        "",
        f"- 候选 API 文档数: {candidates['total_docs']}",
        f"- 已覆盖候选 API 文档数: {candidates['covered_docs']} ({candidates['coverage_ratio']:.2%})",
        f"- 未覆盖候选 API 文档数: {candidates['uncovered_docs']}",
        f"- 门禁阈值: {gate['threshold']:.2%}",
        f"- 门禁结果: {'通过' if gate['passed'] else '失败'}",
    ]
    if gate["reasons"]:
        lines.extend(["", "## 门禁原因", ""])
        for reason in gate["reasons"]:
            lines.append(f"- {reason}")

    lines.extend(
        [
            "",
            "## 分源统计",
            "",
            "| source | total_docs | covered_docs | coverage_ratio |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for source, row in candidates["by_source"].items():
        lines.append(
            f"| {source} | {row['total_docs']} | {row['covered_docs']} | {row['coverage_ratio']:.2%} |"
        )

    lines.extend(
        [
            "",
            "## 分类型统计",
            "",
            "| kind | total_docs | covered_docs | coverage_ratio |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for kind, row in candidates["by_kind"].items():
        lines.append(
            f"| {kind} | {row['total_docs']} | {row['covered_docs']} | {row['coverage_ratio']:.2%} |"
        )

    lines.extend(
        [
            "",
            "## Top 漏网目录",
            "",
            "| group | uncovered_docs | total_candidate_docs | coverage_ratio |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in report["top_uncovered_groups"][:20]:
        lines.append(
            f"| {row['group']} | {row['uncovered_docs']} | {row['total_candidate_docs']} | {row['coverage_ratio']:.2%} |"
        )

    integrity = report["integrity"]
    lines.extend(
        [
            "",
            "## 完整性检查",
            "",
            f"- invalid source_paths: {len(integrity['invalid_source_paths'])}",
            f"- duplicate candidate source path hits: {len(integrity['duplicate_candidate_source_path_hits'])}",
            f"- duplicate api names: {len(integrity['duplicate_name_hits'])}",
            "",
            "## 漏网样例",
            "",
        ]
    )
    for path in report["samples"]["uncovered_candidate_paths"][:30]:
        lines.append(f"- {path}")

    return "\n".join(lines).strip() + "\n"


def write_report(
    report: dict,
    json_path: Path,
    md_path: Path,
    latest_json: Path | None = None,
    latest_md: Path | None = None,
) -> None:
    json_text = json.dumps(report, ensure_ascii=False, indent=2)
    md_text = markdown_report(report)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json_text, encoding="utf-8")
    md_path.write_text(md_text, encoding="utf-8")
    if latest_json is not None:
        latest_json.write_text(json_text, encoding="utf-8")
    if latest_md is not None:
        latest_md.write_text(md_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="盘点 API 候选文档的结构化覆盖率")
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"))
    parser.add_argument("--gate-threshold", type=float, default=1.0)
    args = parser.parse_args()

    report = build_report(Path(args.index_dir), gate_threshold=args.gate_threshold)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    json_path = API_COVERAGE_DIR / f"{timestamp}.json"
    md_path = API_COVERAGE_DIR / f"{timestamp}.md"
    latest_json = API_COVERAGE_DIR / "latest.json"
    latest_md = API_COVERAGE_DIR / "latest.md"
    write_report(report, json_path, md_path, latest_json=latest_json, latest_md=latest_md)
    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "passed": report["gate"]["passed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
