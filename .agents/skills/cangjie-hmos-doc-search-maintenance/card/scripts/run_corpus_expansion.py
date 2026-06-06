#!/usr/bin/env python3
"""文档扩容流程入口：评估 diff、重建 V3、同步 graphify seeds、运行 AB gate。"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILLS_DIR = SCRIPT_DIR.parents[1]
DOC_SEARCH_DIR = SKILLS_DIR / "cangjie-hmos-doc-search"
BUILDER = SKILLS_DIR / "cangjie-hmos-doc-search-maintenance" / "card" / "builder" / "build_index_v3.py"
DOC_GRAPH_DIR = DOC_SEARCH_DIR / "doc-graph"


def run(cmd: list[str], *, cwd: Path | None = None, dry_run: bool = False) -> None:
    print("$ " + " ".join(str(c) for c in cmd))
    if dry_run:
        return
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def require_env() -> dict[str, str]:
    required = ["OPENAI_BASE_URL", "OPENAI_MODEL", "OPENAI_API_KEY", "LLM_CONCURRENCY", "LLM_CACHE_DIR", "GRAPHIFY_CACHE_DIR"]
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        raise SystemExit("缺少环境变量: " + ", ".join(missing) + "；请 source scripts/load_env.sh 或按 env.example 设置")
    return {key: os.environ[key] for key in required}


def count_files(root: Path) -> int:
    if not root.exists():
        return 0
    return sum(1 for p in root.rglob("*") if p.is_file())


def choose_mode(old_snapshot: Path, new_snapshot: Path, explicit: str) -> str:
    if explicit != "auto":
        return explicit
    old_count = count_files(old_snapshot)
    new_count = count_files(new_snapshot)
    if old_count == 0:
        return "full-rebuild"
    growth = max(0, new_count - old_count) / max(old_count, 1)
    if growth > 0.7:
        return "full-rebuild"
    if growth > 0.15:
        return "mixed"
    return "incremental"


def write_report(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Cangjie corpus expansion report",
        "",
        f"- timestamp: {payload['timestamp']}",
        f"- mode: {payload['mode']}",
        f"- old_snapshot: `{payload['old_snapshot']}`",
        f"- new_snapshot: `{payload['new_snapshot']}`",
        f"- old_files: {payload['old_files']}",
        f"- new_files: {payload['new_files']}",
        f"- estimated_new_files: {payload['estimated_new_files']}",
        f"- v3_candidate: `{payload['v3_candidate']}`",
        f"- graph_seeds: `{payload['graph_seeds']}`",
        f"- ab_report: `{payload['ab_report']}`",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="运行 8k→15k 等文档扩容流程")
    parser.add_argument("--old-snapshot", required=True)
    parser.add_argument("--new-snapshot", required=True)
    parser.add_argument("--mode", choices=("auto", "incremental", "mixed", "full-rebuild"), default="auto")
    parser.add_argument("--confirm-full", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--smoke-test", action="store_true")
    parser.add_argument("--max-llm-calls", type=int, default=0)
    parser.add_argument("--output-report", default="/tmp/cangjie-expansion-report.md")
    args = parser.parse_args()

    env = require_env()
    old_snapshot = Path(args.old_snapshot).resolve()
    new_snapshot = Path(args.new_snapshot).resolve()
    mode = choose_mode(old_snapshot, new_snapshot, args.mode)
    if mode == "full-rebuild" and not args.confirm_full and not args.dry_run:
        raise SystemExit("检测到 full-rebuild；请显式传 --confirm-full 确认成本")

    old_files = count_files(old_snapshot)
    new_files = count_files(new_snapshot)
    estimated_new_files = max(0, new_files - old_files)
    estimated_calls = estimated_new_files * (2 if mode == "mixed" else 1)
    if args.smoke_test:
        estimated_calls = min(estimated_calls, 100)
    if args.max_llm_calls and estimated_calls > args.max_llm_calls:
        raise SystemExit(f"预估 LLM 调用 {estimated_calls} 超过上限 {args.max_llm_calls}")

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    work_dir = Path("/tmp") / f"cangjie-expansion-{timestamp}"
    v3_candidate = work_dir / "index-candidate"
    graph_seeds = work_dir / "v3-seeds.json"
    ab_report = work_dir / "ab-report.json"

    print(json.dumps({
        "mode": mode,
        "old_files": old_files,
        "new_files": new_files,
        "estimated_new_files": estimated_new_files,
        "estimated_llm_calls": estimated_calls,
        "env": {k: ("<set>" if k == "OPENAI_API_KEY" else v) for k, v in env.items()},
        "work_dir": str(work_dir),
    }, ensure_ascii=False, indent=2))

    run([
        sys.executable,
        str(BUILDER),
        "--mode", "rule+llm",
        "--index-dir", str(v3_candidate),
        "--llm-cache-dir", env["LLM_CACHE_DIR"],
        "--llm-concurrency", env["LLM_CONCURRENCY"],
    ], dry_run=args.dry_run)

    run([
        sys.executable,
        str(SCRIPT_DIR / "sync_v3_to_graph.py"),
        "--index-dir", str(v3_candidate),
        "--output", str(graph_seeds),
    ], dry_run=args.dry_run)

    run([
        sys.executable,
        str(SCRIPT_DIR / "run_ab_eval.py"),
        "--index-dir", str(v3_candidate),
        "--graph-dir", str(DOC_GRAPH_DIR / "data"),
        "--splits", "real_session,paraphrase,composition",
        "--limit", "8",
        "--output", str(ab_report),
    ], dry_run=args.dry_run)

    payload = {
        "timestamp": timestamp,
        "mode": mode,
        "old_snapshot": str(old_snapshot),
        "new_snapshot": str(new_snapshot),
        "old_files": old_files,
        "new_files": new_files,
        "estimated_new_files": estimated_new_files,
        "v3_candidate": str(v3_candidate),
        "graph_seeds": str(graph_seeds),
        "ab_report": str(ab_report),
    }
    write_report(Path(args.output_report), payload)
    print(json.dumps({"status": "ok", "report": args.output_report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
