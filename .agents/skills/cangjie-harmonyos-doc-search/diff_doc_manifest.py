#!/usr/bin/env python3
"""对比两份文档 manifest。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def by_path(manifest: dict) -> dict[str, dict]:
    return {row["path"]: row for row in manifest.get("files", [])}


def suspected_renames(removed: list[dict], added: list[dict]) -> list[dict]:
    added_by_hash: dict[str, list[dict]] = {}
    added_by_title: dict[str, list[dict]] = {}
    for row in added:
        added_by_hash.setdefault(row.get("sha256", ""), []).append(row)
        title = str(row.get("title", "")).strip()
        if title:
            added_by_title.setdefault(title, []).append(row)

    matches: list[dict] = []
    for row in removed:
        candidates = added_by_hash.get(row.get("sha256", ""), [])
        reason = "same_sha256"
        if not candidates:
            candidates = added_by_title.get(str(row.get("title", "")).strip(), [])
            reason = "same_title"
        for candidate in candidates:
            matches.append(
                {
                    "old_path": row["path"],
                    "new_path": candidate["path"],
                    "reason": reason,
                    "title": row.get("title", ""),
                }
            )
    return matches


def diff(old: dict, new: dict) -> dict:
    old_files = by_path(old)
    new_files = by_path(new)
    added = [new_files[path] for path in sorted(set(new_files) - set(old_files))]
    removed = [old_files[path] for path in sorted(set(old_files) - set(new_files))]
    changed = [
        {
            "path": path,
            "old_sha256": old_files[path].get("sha256", ""),
            "new_sha256": new_files[path].get("sha256", ""),
            "title": new_files[path].get("title") or old_files[path].get("title", ""),
        }
        for path in sorted(set(old_files) & set(new_files))
        if old_files[path].get("sha256") != new_files[path].get("sha256")
    ]
    return {
        "old_generated_at": old.get("generated_at", ""),
        "new_generated_at": new.get("generated_at", ""),
        "counts": {
            "added": len(added),
            "removed": len(removed),
            "changed": len(changed),
            "suspected_renames": len(suspected_renames(removed, added)),
        },
        "added": added,
        "removed": removed,
        "changed": changed,
        "suspected_renames": suspected_renames(removed, added),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="对比文档 manifest")
    parser.add_argument("--old", required=True)
    parser.add_argument("--new", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = diff(load_json(Path(args.old)), load_json(Path(args.new)))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}: {data['counts']}")


if __name__ == "__main__":
    main()
