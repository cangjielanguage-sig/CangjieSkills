#!/usr/bin/env python3
"""语义 / 融合能力门禁：调用 maintenance 的 run_ab_eval（V3 vs graphify vs fusion）。

默认评测 `real_session` + `paraphrase` + `composition` 三套独立集；与 `run_v3_regression_gate.py` 拆分。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = ROOT / "doc-card"
MAINT_SCRIPTS = ROOT.parent / "cangjie-harmonyos-doc-search-maintenance" / "scripts"
GRAPH_DATA = ROOT.parent / "knowledge-graph-template" / "data"


def main() -> None:
    parser = argparse.ArgumentParser(description="fusion 能力门禁（run_ab_eval）")
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"))
    parser.add_argument("--graph-dir", default=str(GRAPH_DATA))
    parser.add_argument("--eval-dir", default=str(DOC_CARD_DIR / "evals"))
    parser.add_argument("--splits", default="real_session,paraphrase,composition")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--output", default="", help="可选：写入 JSON 报告")
    args = parser.parse_args()

    ab_script = MAINT_SCRIPTS / "run_ab_eval.py"
    if not ab_script.is_file():
        print(json.dumps({"error": "missing_run_ab_eval", "path": str(ab_script)}, ensure_ascii=False))
        sys.exit(2)

    out_path = Path(args.output) if args.output else None
    tmp_path: Path | None = None
    if out_path is None:
        tmp = tempfile.NamedTemporaryFile(prefix="semantic-gate-", suffix=".json", delete=False)
        tmp_path = Path(tmp.name)
        tmp.close()
        out_path = tmp_path
    cmd = [
        sys.executable,
        str(ab_script),
        "--eval-dir",
        str(Path(args.eval_dir).resolve()),
        "--index-dir",
        str(Path(args.index_dir).resolve()),
        "--graph-dir",
        str(Path(args.graph_dir).resolve()),
        "--splits",
        args.splits,
        "--limit",
        str(args.limit),
        "--output",
        str(out_path.resolve()),
    ]

    subprocess.run(cmd, check=True)
    data = json.loads(out_path.read_text(encoding="utf-8"))
    if tmp_path:
        tmp_path.unlink(missing_ok=True)
    summary = {}
    for split, payload in data.get("splits", {}).items():
        summary[split] = {
            "v3": payload["v3"]["recall_at_k"],
            "graphify": payload["graphify"]["recall_at_k"],
            "fusion": payload["fusion"]["recall_at_k"],
        }
    print(json.dumps({"splits": summary}, ensure_ascii=False, indent=2))

    reasons: list[str] = []
    for split, m in summary.items():
        if m["fusion"] + 1e-9 < m["v3"]:
            reasons.append(f"{split}: fusion={m['fusion']} < v3={m['v3']}")
        if m["fusion"] + 1e-9 < m["graphify"]:
            reasons.append(f"{split}: fusion={m['fusion']} < graphify={m['graphify']}")
    if reasons:
        print(json.dumps({"status": "failed", "reasons": reasons}, ensure_ascii=False, indent=2))
        sys.exit(1)
    print(json.dumps({"status": "ok"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
