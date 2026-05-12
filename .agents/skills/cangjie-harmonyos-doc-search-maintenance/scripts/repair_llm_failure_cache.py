#!/usr/bin/env python3
"""为 cangjie-harmonyos-doc-search 的 LLM failure 生成本地 fallback 缓存。

这是维护/构建工具，不属于用户态检索 skill。用于少数卡片稳定触发服务端
403/权限类错误时，先用规则字段生成结构兼容的 LLM cache payload，使下一次
严格 rule+llm 构建可以复用缓存并完成零失败发布。

fallback 条目会带 `needs_review=true` 与 `llm-fallback-cache` tag，便于后续复核。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SKILLS_DIR = Path(__file__).resolve().parents[2]
DOC_SEARCH = SKILLS_DIR / "cangjie-harmonyos-doc-search"
sys.path.insert(0, str(DOC_SEARCH))

import build_index_v3 as b  # noqa: E402


API_ALLOWED = [
    "api_id", "name", "summary", "aliases", "when_to_use",
    "when_not_to_use", "related_apis", "tags",
    "kind", "module", "user_queries", "semantic_aliases", "intent_types", "primary_objects",
]
DOC_ALLOWED = [
    "doc_id", "title", "summary", "aliases", "source", "doc_kind",
    "when_to_use", "when_not_to_use", "tags",
    "user_queries", "semantic_aliases", "intent_types", "primary_objects",
]


def _list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def _fallback_payload(card_type: str, row: dict[str, Any]) -> dict[str, Any]:
    row_id = row[b.TYPE_ID_KEY[card_type]]
    title = str(row.get("title") or row.get("name") or row_id).strip()
    summary = str(row.get("summary") or title).strip()
    aliases = _list(row.get("aliases"))
    tags = sorted(set(_list(row.get("tags")) + ["llm-fallback-cache"]))
    user_queries = _list(row.get("user_queries"))
    if not user_queries:
        user_queries = [
            title,
            f"{title} 怎么用",
            f"查询 {title} 文档",
        ]
    semantic_aliases = _list(row.get("semantic_aliases")) or aliases[:]
    primary_objects = _list(row.get("primary_objects")) or [title]
    intent_types = _list(row.get("intent_types"))
    if not intent_types:
        intent_types = ["api_lookup" if card_type == "api" else "concept_explanation"]
    payload: dict[str, Any] = {
        "card_id": row_id,
        "summary": summary,
        "aliases": aliases,
        "user_queries": user_queries,
        "semantic_aliases": semantic_aliases,
        "intent_types": intent_types,
        "primary_objects": primary_objects,
        "when_to_use": _list(row.get("when_to_use")),
        "when_not_to_use": _list(row.get("when_not_to_use")),
        "tags": tags,
        "confidence": min(float(row.get("confidence") or 0.5), 0.6),
        "needs_review": True,
    }
    if card_type == "api":
        payload["related_apis"] = _list(row.get("related_apis"))
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="为 LLM failure 生成 fallback cache")
    parser.add_argument("--manifest", default=str(DOC_SEARCH / "index" / "manifest.json"))
    parser.add_argument("--cache-dir", required=True)
    parser.add_argument("--only-error-type", default="auth_or_permission")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures = [
        item for item in manifest.get("llm", {}).get("failures", [])
        if not args.only_error_type or item.get("error_type") == args.only_error_type
    ]
    if not failures:
        print(json.dumps({"status": "noop", "reason": "no matching failures"}, ensure_ascii=False))
        return

    docs = b.discover_docs(DOC_SEARCH)
    records_by_path = {record.path: record for record in docs}
    examples = b.find_examples(docs)
    apis = b.build_api_cards(docs, examples)
    tasks = b.build_task_cards(docs, examples)
    b.attach_example_relations(tasks, examples)
    doc_cards = b.build_doc_cards(docs)

    rows_by_type = {
        "api": {row["api_id"]: row for row in apis},
        "doc": {row["doc_id"]: row for row in doc_cards},
        "task": {row["task_id"]: row for row in tasks},
        "example": {row["example_id"]: row for row in examples},
    }
    allowed_by_type = {
        "api": API_ALLOWED,
        "doc": DOC_ALLOWED,
    }

    config = b.llm_config_from_env()
    cache_dir = Path(args.cache_dir)
    written: list[dict[str, str]] = []
    missing: list[dict[str, str]] = []
    for failure in failures:
        card_type = str(failure.get("card_type") or "")
        card_id = str(failure.get("card_id") or "")
        row = rows_by_type.get(card_type, {}).get(card_id)
        allowed = allowed_by_type.get(card_type)
        if not row or not allowed:
            missing.append({"card_type": card_type, "card_id": card_id})
            continue
        skeleton = b.compact_card(row, allowed)
        skeleton["card_id"] = card_id
        evidence_payload = {
            "card_id": card_id,
            "docs": b.evidence_for_paths(records_by_path, row.get("source_paths", [])),
        }
        fingerprint = b.prompt_fingerprint(config, card_type, skeleton, evidence_payload)
        cache_path = b.cache_file_for(cache_dir, card_type, card_id, fingerprint)
        payload = _fallback_payload(card_type, row)
        if not args.dry_run:
            b.write_llm_cache(cache_path, payload, {"fallback": True})
        written.append({"card_type": card_type, "card_id": card_id, "cache": str(cache_path)})

    print(json.dumps({"status": "ok", "written": written, "missing": missing}, ensure_ascii=False, indent=2))
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
