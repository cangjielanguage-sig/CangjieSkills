#!/usr/bin/env python3
"""Rebuild the default Cangjie knowledge graph without external model keys.

Usage:
    python .agents/skills/knowledge-graph-template/scripts/rebuild_cangjie_graph.py

Generates:
    data/subgraphs/harmonyos/graph.json
    data/subgraphs/lang-features/graph.json
    data/subgraphs/std/graph.json
    data/subgraphs/stdx/graph.json
    data/subgraphs/tools/graph.json
    data/merged/graph.json
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = SKILL_DIR / "docs"
CLI = SKILL_DIR / "cli.py"
SUBGRAPHS = (
    ("harmonyos", ("harmonyos-6.1-8k", "harmonyos-6.0.2-15k", "harmonyos")),
    ("lang-features", ("lang-features",)),
    ("std", ("std",)),
    ("stdx", ("stdx",)),
    ("tools", ("tools",)),
)


def main() -> int:
    env = os.environ.copy()
    env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    graph_paths: list[Path] = []
    for name, candidates in SUBGRAPHS:
        source = resolve_source(candidates)
        output = SKILL_DIR / "data" / "subgraphs" / name / "graph.json"
        run(
            [
                sys.executable,
                str(CLI),
                "build-subgraph",
                str(source),
                "--name",
                name,
                "--llm-provider",
                "skip",
            ],
            env=env,
        )
        if not output.is_file():
            raise SystemExit(f"expected subgraph was not generated: {output}")
        graph_paths.append(output)

    merged = SKILL_DIR / "data" / "merged" / "graph.json"
    run(
        [
            sys.executable,
            str(CLI),
            "merge",
            *(str(path) for path in graph_paths),
            "--output",
            str(merged),
        ],
        env=env,
    )
    if not merged.is_file():
        raise SystemExit(f"expected merged graph was not generated: {merged}")
    print(f"[ok] rebuilt Cangjie graph: {merged}")
    return 0


def resolve_source(candidates: tuple[str, ...]) -> Path:
    for name in candidates:
        marker = DOCS_DIR / name
        if marker.is_dir():
            return marker
        if marker.is_file():
            text = marker.read_text(encoding="utf-8").strip()
            if text:
                target = (marker.parent / text).resolve(strict=False)
                if target.is_dir():
                    return target
    names = ", ".join(candidates)
    raise SystemExit(f"missing graph source docs for: {names}")


def run(command: list[str], *, env: dict[str, str]) -> None:
    print("[run] " + " ".join(command))
    subprocess.run(command, cwd=SKILL_DIR, check=True, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
