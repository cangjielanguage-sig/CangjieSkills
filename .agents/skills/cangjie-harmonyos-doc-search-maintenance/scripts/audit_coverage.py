#!/usr/bin/env python3
"""盘点 doc-search 当前索引对原始文档的覆盖率。"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-harmonyos-doc-search"
COVERAGE_DIR = MAINTENANCE_DIR / "records" / "coverage"

sys.path.insert(0, str(SEARCH_SKILL_DIR))

from build_index_v3 import DOC_SOURCES, discover_docs  # noqa: E402


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def card_id_key(card_type: str) -> str:
    return {
        "tasks": "task_id",
        "apis": "api_id",
        "examples": "example_id",
        "docs": "doc_id",
    }[card_type]


def path_group(path: str) -> str:
    parts = path.split("/")
    if len(parts) >= 2:
        return "/".join(parts[:2])
    return parts[0]


def ratio(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 4)


def sample_paths(paths: list[str], limit: int = 20) -> list[str]:
    return sorted(paths)[:limit]


def build_report() -> dict:
    docs = discover_docs(SEARCH_SKILL_DIR)
    all_doc_paths = sorted(record.path for record in docs)
    all_doc_set = set(all_doc_paths)
    docs_by_source = Counter(record.source for record in docs)
    docs_by_group = Counter(path_group(record.path) for record in docs)

    index_dir = SEARCH_SKILL_DIR / "index"
    cards = {
        "tasks": load_jsonl(index_dir / "tasks.jsonl"),
        "apis": load_jsonl(index_dir / "apis.jsonl"),
        "examples": load_jsonl(index_dir / "examples.jsonl"),
        "docs": load_jsonl(index_dir / "docs.jsonl"),
    }

    referenced_paths_by_type: dict[str, set[str]] = {}
    missing_paths_by_type: dict[str, set[str]] = {}
    source_path_refs_by_type: dict[str, int] = {}
    missing_card_refs: dict[str, list[dict]] = {}
    coverage_by_group_and_type: dict[str, dict[str, int]] = defaultdict(lambda: {"tasks": 0, "apis": 0, "examples": 0, "docs": 0, "any": 0})

    for card_type, rows in cards.items():
        referenced: set[str] = set()
        missing: set[str] = set()
        bad_rows: list[dict] = []
        id_key = card_id_key(card_type)
        for row in rows:
            paths = row.get("source_paths", [])
            source_path_refs_by_type[card_type] = source_path_refs_by_type.get(card_type, 0) + len(paths)
            row_missing = [path for path in paths if path not in all_doc_set]
            if row_missing:
                missing.update(row_missing)
                bad_rows.append(
                    {
                        "id": row.get(id_key),
                        "title": row.get("title") or row.get("name"),
                        "missing_source_paths": row_missing,
                    }
                )
            for path in paths:
                if path in all_doc_set:
                    referenced.add(path)
        referenced_paths_by_type[card_type] = referenced
        missing_paths_by_type[card_type] = missing
        missing_card_refs[card_type] = bad_rows[:50]
        for path in referenced:
            coverage_by_group_and_type[path_group(path)][card_type] += 1

    referenced_any = set().union(*referenced_paths_by_type.values())
    uncovered_paths = sorted(all_doc_set - referenced_any)

    for path in referenced_any:
        coverage_by_group_and_type[path_group(path)]["any"] += 1

    uncovered_by_source = Counter(path.split("/")[0] for path in uncovered_paths)
    uncovered_by_group = Counter(path_group(path) for path in uncovered_paths)
    covered_by_source = Counter(path.split("/")[0] for path in referenced_any)

    group_rows: list[dict] = []
    for group, total in docs_by_group.most_common():
        type_counts = coverage_by_group_and_type[group]
        uncovered = total - type_counts["any"]
        group_rows.append(
            {
                "group": group,
                "total_docs": total,
                "covered_docs": type_counts["any"],
                "coverage_ratio": ratio(type_counts["any"], total),
                "uncovered_docs": uncovered,
                "task_docs": type_counts["tasks"],
                "api_docs": type_counts["apis"],
                "example_docs": type_counts["examples"],
                "doc_docs": type_counts["docs"],
            }
        )

    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "search_skill_dir": str(SEARCH_SKILL_DIR),
        "sources": list(DOC_SOURCES),
        "totals": {
            "docs": len(all_doc_paths),
            "cards": {
                "tasks": len(cards["tasks"]),
                "apis": len(cards["apis"]),
                "examples": len(cards["examples"]),
                "docs": len(cards["docs"]),
            },
            "referenced_docs": {
                "tasks": len(referenced_paths_by_type["tasks"]),
                "apis": len(referenced_paths_by_type["apis"]),
                "examples": len(referenced_paths_by_type["examples"]),
                "docs": len(referenced_paths_by_type["docs"]),
                "any": len(referenced_any),
            },
            "coverage_ratio": {
                "tasks": ratio(len(referenced_paths_by_type["tasks"]), len(all_doc_paths)),
                "apis": ratio(len(referenced_paths_by_type["apis"]), len(all_doc_paths)),
                "examples": ratio(len(referenced_paths_by_type["examples"]), len(all_doc_paths)),
                "docs": ratio(len(referenced_paths_by_type["docs"]), len(all_doc_paths)),
                "any": ratio(len(referenced_any), len(all_doc_paths)),
            },
            "source_path_refs": source_path_refs_by_type,
            "uncovered_docs": len(uncovered_paths),
        },
        "by_source": {
            source: {
                "total_docs": docs_by_source[source],
                "covered_docs": covered_by_source[source],
                "coverage_ratio": ratio(covered_by_source[source], docs_by_source[source]),
                "uncovered_docs": uncovered_by_source[source],
            }
            for source in DOC_SOURCES
        },
        "integrity": {
            "missing_source_paths": {
                card_type: sorted(paths)
                for card_type, paths in missing_paths_by_type.items()
            },
            "cards_with_missing_source_paths": missing_card_refs,
        },
        "top_uncovered_groups": [
            {
                "group": group,
                "uncovered_docs": count,
                "total_docs": docs_by_group[group],
                "coverage_ratio": ratio(docs_by_group[group] - count, docs_by_group[group]),
            }
            for group, count in uncovered_by_group.most_common(30)
        ],
        "group_coverage": group_rows,
        "samples": {
            "uncovered_paths": sample_paths(uncovered_paths, limit=100),
            "covered_only_by_examples": sample_paths(
                sorted(
                    referenced_paths_by_type["examples"]
                    - referenced_paths_by_type["tasks"]
                    - referenced_paths_by_type["apis"]
                    - referenced_paths_by_type["docs"]
                ),
                limit=50,
            ),
            "task_paths": sample_paths(sorted(referenced_paths_by_type["tasks"]), limit=50),
            "api_paths": sample_paths(sorted(referenced_paths_by_type["apis"]), limit=50),
            "example_paths": sample_paths(sorted(referenced_paths_by_type["examples"]), limit=50),
            "doc_paths": sample_paths(sorted(referenced_paths_by_type["docs"]), limit=50),
        },
    }
    return report


def markdown_report(report: dict) -> str:
    totals = report["totals"]
    lines = [
        "# doc-search Coverage Audit",
        "",
        f"- generated_at: {report['generated_at']}",
        f"- search_skill_dir: `{report['search_skill_dir']}`",
        f"- sources: {', '.join(report['sources'])}",
        "",
        "## 总览",
        "",
        f"- 原始 Markdown 文档数: {totals['docs']}",
        f"- 卡片数: tasks={totals['cards']['tasks']}, apis={totals['cards']['apis']}, examples={totals['cards']['examples']}, docs={totals['cards']['docs']}",
        f"- 被任一卡片引用的文档数: {totals['referenced_docs']['any']} ({totals['coverage_ratio']['any']:.2%})",
        f"- 未被任何卡片引用的文档数: {totals['uncovered_docs']} ({(1 - totals['coverage_ratio']['any']):.2%})",
        f"- task 覆盖文档数: {totals['referenced_docs']['tasks']} ({totals['coverage_ratio']['tasks']:.2%})",
        f"- api 覆盖文档数: {totals['referenced_docs']['apis']} ({totals['coverage_ratio']['apis']:.2%})",
        f"- example 覆盖文档数: {totals['referenced_docs']['examples']} ({totals['coverage_ratio']['examples']:.2%})",
        f"- doc 覆盖文档数: {totals['referenced_docs']['docs']} ({totals['coverage_ratio']['docs']:.2%})",
        "",
        "## 分源统计",
        "",
        "| source | total_docs | covered_docs | coverage_ratio | uncovered_docs |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for source, row in report["by_source"].items():
        lines.append(
            f"| {source} | {row['total_docs']} | {row['covered_docs']} | {row['coverage_ratio']:.2%} | {row['uncovered_docs']} |"
        )

    lines.extend(
        [
            "",
            "## Top 未覆盖目录",
            "",
            "| group | uncovered_docs | total_docs | coverage_ratio |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in report["top_uncovered_groups"][:20]:
        lines.append(
            f"| {row['group']} | {row['uncovered_docs']} | {row['total_docs']} | {row['coverage_ratio']:.2%} |"
        )

    integrity = report["integrity"]["missing_source_paths"]
    lines.extend(
        [
            "",
            "## 完整性检查",
            "",
            f"- task 缺失 source_paths: {len(integrity['tasks'])}",
            f"- api 缺失 source_paths: {len(integrity['apis'])}",
            f"- example 缺失 source_paths: {len(integrity['examples'])}",
            f"- doc 缺失 source_paths: {len(integrity['docs'])}",
        ]
    )

    lines.extend(
        [
            "",
            "## 未覆盖样例",
            "",
        ]
    )
    for path in report["samples"]["uncovered_paths"][:30]:
        lines.append(f"- {path}")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    report = build_report()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    COVERAGE_DIR.mkdir(parents=True, exist_ok=True)
    json_path = COVERAGE_DIR / f"{timestamp}.json"
    md_path = COVERAGE_DIR / f"{timestamp}.md"
    latest_json = COVERAGE_DIR / "latest.json"
    latest_md = COVERAGE_DIR / "latest.md"

    json_text = json.dumps(report, ensure_ascii=False, indent=2)
    md_text = markdown_report(report)
    json_path.write_text(json_text, encoding="utf-8")
    md_path.write_text(md_text, encoding="utf-8")
    latest_json.write_text(json_text, encoding="utf-8")
    latest_md.write_text(md_text, encoding="utf-8")

    print(json.dumps({"json": str(json_path), "markdown": str(md_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
