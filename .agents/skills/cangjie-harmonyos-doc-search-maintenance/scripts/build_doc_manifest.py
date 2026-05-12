#!/usr/bin/env python3
"""生成当前文档文件指纹。"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_SOURCES = ("harmonyos-6.0.2-15k", "lang-features", "std", "stdx", "tools")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def title_for(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            match = re.match(r"^\s{0,3}#\s+(.+?)\s*$", line)
            if match:
                return match.group(1).strip()
    except OSError:
        return ""
    return path.stem


def build_manifest(root: Path) -> dict:
    files: list[dict] = []
    for source in DOC_SOURCES:
        source_dir = root / source
        if not source_dir.exists():
            continue
        for path in sorted(source_dir.rglob("*.md")):
            rel = path.relative_to(root).as_posix()
            files.append(
                {
                    "path": rel,
                    "sha256": sha256(path),
                    "title": title_for(path),
                    "size": path.stat().st_size,
                }
            )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "sources": list(DOC_SOURCES),
        "file_count": len(files),
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生成文档 manifest")
    parser.add_argument("--root", default=str(ROOT), help="skill 根目录")
    parser.add_argument("--output", required=True, help="输出 JSON")
    args = parser.parse_args()

    manifest = build_manifest(Path(args.root))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}: {manifest['file_count']} files")


if __name__ == "__main__":
    main()
