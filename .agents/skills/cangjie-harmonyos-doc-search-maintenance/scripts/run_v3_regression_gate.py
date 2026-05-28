#!/usr/bin/env python3
"""V3 自举回归门禁：仅跑本地 V3 + eval_queries_full（或指定 JSONL）。

与 `run_semantic_capability_gate.py`（fusion 能力门禁）拆分，避免把结构化召回与语义/融合能力绑在同一阈值上。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = ROOT / "doc-card"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SCRIPT_DIR))

from eval_bench import load_eval_set, make_v3_search, run_benchmark  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="V3 自举回归门禁（eval_queries_full 等）")
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"))
    parser.add_argument("--eval-set", default=str(DOC_CARD_DIR / "evals" / "eval_queries_full.jsonl"))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument(
        "--max-rows",
        type=int,
        default=0,
        help="最多评测前 N 条；默认 0 表示全量。用于避免 15K 全量自举集在本地门禁中运行过久。",
    )
    parser.add_argument(
        "--min-recall-at-5",
        type=float,
        default=0.0,
        help="overall recall@5 低于该阈值则 exit 1；默认 0 表示仅产出报告不强制",
    )
    parser.add_argument("--output", default="", help="可选：写入 JSON 报告")
    args = parser.parse_args()

    eval_path = Path(args.eval_set)
    if not eval_path.is_file():
        print(json.dumps({"error": "missing_eval_set", "path": str(eval_path)}, ensure_ascii=False))
        sys.exit(2)

    rows = load_eval_set(str(eval_path))
    total_rows = len(rows)
    if args.max_rows > 0:
        rows = rows[: args.max_rows]
    bench = run_benchmark(make_v3_search(str(Path(args.index_dir).resolve()), "auto"), rows, limit=args.limit)
    overall = bench["summary"]["overall"]
    payload = {
        "eval_set": str(eval_path),
        "index_dir": str(Path(args.index_dir).resolve()),
        "limit": args.limit,
        "evaluated_rows": len(rows),
        "total_rows": total_rows,
        "overall": overall,
    }
    if args.output:
        outp = Path(args.output)
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(json.dumps({**payload, "raw": bench}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if args.min_recall_at_5 > 0 and float(overall.get("recall@5", 0.0)) < args.min_recall_at_5:
        sys.exit(1)


if __name__ == "__main__":
    main()
