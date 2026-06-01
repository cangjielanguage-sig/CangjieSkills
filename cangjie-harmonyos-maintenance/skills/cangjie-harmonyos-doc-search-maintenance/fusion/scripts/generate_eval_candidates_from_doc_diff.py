#!/usr/bin/env python3
"""基于文档 diff 生成用户态评测候选 query。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def normalize_path(path: str) -> str:
    value = str(path or "").replace("\\", "/").strip().split("#", 1)[0].split("?", 1)[0].strip("/")
    if value.endswith(".md"):
        value = value[:-3]
    return value


def collect_paths(value: Any, output: set[str]) -> None:
    if isinstance(value, str):
        if "/" in value:
            output.add(normalize_path(value))
        return
    if isinstance(value, list):
        for item in value:
            collect_paths(item, output)
        return
    if isinstance(value, dict):
        for item in value.values():
            collect_paths(item, output)


def capability_for(path: str) -> str:
    lowered = path.lower()
    if "arkweb" in lowered or "/web/" in lowered:
        return "webview"
    if "network" in lowered or "net-" in lowered:
        return "network"
    if "arkui" in lowered:
        return "arkui_component"
    if "security" in lowered or "huks" in lowered or "crypto" in lowered:
        return "security"
    if "media" in lowered or "image" in lowered or "camera" in lowered:
        return "media"
    if "file" in lowered:
        return "resource_file"
    return "unknown"


def card_index(index_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for filename in ("tasks.jsonl", "apis.jsonl", "docs.jsonl"):
        for row in load_jsonl(index_dir / filename):
            paths: set[str] = set()
            collect_paths(row, paths)
            rows.append(
                {
                    "title": row.get("title") or row.get("name") or row.get("task_id") or row.get("api_id") or "",
                    "summary": row.get("summary", ""),
                    "paths": sorted(paths),
                }
            )
    return rows


def related_cards(path: str, cards: list[dict], limit: int = 4) -> list[dict]:
    normalized = normalize_path(path)
    matches = [
        card
        for card in cards
        if any(normalized == item or normalized.startswith(f"{item}/") or item.startswith(f"{normalized}/") for item in card["paths"])
    ]
    return matches[:limit]


def candidate_for(path: str, title: str, cards: list[dict], source: str) -> dict:
    cards_for_path = related_cards(path, cards)
    accepted = [path]
    for card in cards_for_path:
        for item in card["paths"]:
            if item not in accepted:
                accepted.append(item)
            if len(accepted) >= 4:
                break
        if len(accepted) >= 4:
            break
    clean_title = title or Path(path).stem
    return {
        "query": f"{clean_title} 在 App 里怎么用",
        "intent": f"查{clean_title}的开发入口和相关 API",
        "category": "doc_update_candidate",
        "capability": capability_for(path),
        "query_style": "how_to",
        "difficulty": "unknown",
        "acceptable_paths": accepted,
        "must_contain": [],
        "source": source,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="从文档 diff 生成候选评测集")
    parser.add_argument("--doc-diff", required=True)
    parser.add_argument("--index-dir", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()

    diff = load_json(Path(args.doc_diff))
    cards = card_index(Path(args.index_dir))
    rows: list[dict] = []
    for item in diff.get("added", []):
        rows.append(candidate_for(item["path"], item.get("title", ""), cards, "doc-diff-added"))
    for item in diff.get("changed", []):
        rows.append(candidate_for(item["path"], item.get("title", ""), cards, "doc-diff-changed"))
    rows = rows[: args.limit]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"wrote {output}: {len(rows)}")


if __name__ == "__main__":
    main()
