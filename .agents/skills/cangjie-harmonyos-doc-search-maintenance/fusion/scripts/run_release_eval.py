#!/usr/bin/env python3
"""一键执行本地发布评估流水线。

这是 fusion 分区的发布门禁入口脚本，执行以下步骤：
1. 生成文档 manifest（build_doc_manifest）
2. 可选计算文档差异（diff_doc_manifest）
3. 可选重建索引（--rebuild-index）
4. 对每个评测集依次运行：
   a. validate_eval_set — 校验评测集健康状态
   b. ab_test_openviking_vs_v3 — 本地 V3 评测（--skip-a 跳过远端）
   c. analyze_user_eval_failures — 分析失败查询
5. 根据评测结果判定发布状态：pass / blocked / gray_release

gray_release 规则：blind 评测集 success@5 < 0.95 时降级为灰度发布。
门禁拆分说明见脚本顶部注释。
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SKILLS_DIR = MAINTENANCE_DIR.parent
ROOT = SKILLS_DIR / "cangjie-harmonyos-doc-search"
DOC_CARD_DIR = ROOT / "doc-card"
DOCS_DIR = ROOT / "docs"
BUILDER = SKILLS_DIR / "cangjie-harmonyos-doc-search-maintenance" / "builder" / "build_index_v3.py"
EVALS_DIR = DOC_CARD_DIR / "evals"
DEFAULT_EVAL_SETS = (
    # 评测集列表：从早期用户查询到最新盲测集，覆盖不同场景
    "eval_queries_user.jsonl",
    "eval_queries_app_agent_dev.jsonl",
    "eval_queries_user_appdev.jsonl",
    "eval_queries_user_appdev_next.jsonl",
    "eval_queries_user_appdev_frozen.jsonl",
    "eval_queries_user_appdev_batch2.jsonl",
    "eval_queries_user_appdev_batch3.jsonl",
    "eval_queries_user_appdev_blind.jsonl",
)


def run(cmd: list[str], cwd: Path) -> None:
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, cwd=str(cwd), check=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def metric_for(eval_name: str) -> dict:
    """不同评测集使用不同门禁阈值：
    - user/app_agent_dev 基础集: success@5 >= 0.98
    - blind 盲测集: success@5 >= 0.80（更宽松，因为未知查询难度更高）
    - 其他集: success@5 >= 0.95"""
    if eval_name in {"eval_queries_user.jsonl", "eval_queries_app_agent_dev.jsonl"}:
        return {"success@5": 0.98, "error_rate": 0.0}
    if "blind" in eval_name:
        return {"success@5": 0.80, "error_rate": 0.0}
    return {"success@5": 0.95, "error_rate": 0.0}


def group_overall(summary: dict) -> dict:
    """从评测 summary 中提取 Group B（本地 V3）的 overall 指标。
    Group A 为 OpenViking，此流程中 --skip-a 跳过远端。"""
    return summary.get("groups", {}).get("B", {}).get("overall", {})


def eval_status(eval_name: str, overall: dict, health: dict) -> tuple[str, list[str]]:
    """判定单个评测集的通过/阻塞状态。

    阻塞条件：eval_health blocking 标记、success@5 低于阈值、error_rate 非零。
    返回 ("pass" 或 "blocked", 原因列表)。"""
    reasons: list[str] = []
    threshold = metric_for(eval_name)
    if health.get("blocking"):
        reasons.append("eval_health_blocking")
    if overall.get("success@5", 0.0) < threshold["success@5"]:
        reasons.append(f"success@5_below_{threshold['success@5']}")
    if overall.get("error_rate", 1.0) != threshold["error_rate"]:
        reasons.append("error_rate_non_zero")
    return ("pass" if not reasons else "blocked"), reasons


def render_report(data: dict) -> str:
    lines = [
        "# Cangjie HarmonyOS Doc Search 发布评估报告",
        "",
        f"生成时间: {data['generated_at']}",
        f"结论: {data['status']}",
        "",
        "## 总览",
        "",
        "| Eval Set | Count | Success@5 | MRR | Error | Health | Status |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in data["evals"]:
        overall = row["overall"]
        lines.append(
            f"| {row['eval_set']} | {overall.get('count', 0)} | {overall.get('success@5', 0)} | "
            f"{overall.get('mrr', 0)} | {overall.get('error_rate', 0)} | "
            f"{'blocked' if row['health'].get('blocking') else 'ok'} | {row['status']} |"
        )
    lines.extend(["", "## 阻塞项", ""])
    blocked = [row for row in data["evals"] if row["status"] != "pass"]
    if not blocked:
        lines.append("无。")
    for row in blocked:
        lines.append(f"- {row['eval_set']}: {', '.join(row['reasons'])}")
    lines.extend(["", "## 说明", ""])
    lines.append("默认流程只评测本地 V3，不触发 OpenViking 远端 AB。候选集和真实反馈不会自动进入主门禁。")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="执行本地发布评估")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--index-dir", default=str(DOC_CARD_DIR / "index"))
    parser.add_argument("--rebuild-index", action="store_true")
    parser.add_argument("--previous-doc-manifest", default="")
    parser.add_argument("--eval-sets", default=",".join(DEFAULT_EVAL_SETS), help="逗号分隔评测集")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    index_dir = Path(args.index_dir)

    current_manifest = output_dir / "doc_manifest_current.json"
    run([sys.executable, str(SCRIPT_DIR / "build_doc_manifest.py"), "--root", str(DOCS_DIR), "--output", str(current_manifest)], ROOT)

    doc_diff = ""
    if args.previous_doc_manifest:
        doc_diff_path = output_dir / "doc_diff.json"
        run(
            [
                sys.executable,
                str(SCRIPT_DIR / "diff_doc_manifest.py"),
                "--old",
                args.previous_doc_manifest,
                "--new",
                str(current_manifest),
                "--output",
                str(doc_diff_path),
            ],
            ROOT,
        )
        doc_diff = str(doc_diff_path)

    if args.rebuild_index:
        run([sys.executable, str(BUILDER), "--mode", "rule", "--index-dir", str(index_dir)], ROOT)

    eval_rows: list[dict] = []
    health_summary: dict[str, dict] = {}
    for eval_name in [item.strip() for item in args.eval_sets.split(",") if item.strip()]:
        eval_path = Path(eval_name)
        if not eval_path.is_absolute():
            eval_path = EVALS_DIR / eval_name
        eval_label = eval_path.name
        if not eval_path.exists():
            print(f"skip missing eval set: {eval_name}", file=sys.stderr)
            continue
        eval_dir = output_dir / eval_path.stem
        health_path = eval_dir / "eval-health.json"
        run(
            [
                sys.executable,
                str(SCRIPT_DIR / "validate_eval_set.py"),
                "--eval-set",
                str(eval_path),
                "--index-dir",
                str(index_dir),
                "--doc-manifest",
                str(current_manifest),
                "--output",
                str(health_path),
            ],
            ROOT,
        )
        run(
            [
                sys.executable,
                str(SCRIPT_DIR / "ab_test_openviking_vs_v3.py"),
                "--skip-a",
                "--eval-set",
                str(eval_path),
                "--b-index-dir",
                str(index_dir),
                "--output-dir",
                str(eval_dir),
            ],
            ROOT,
        )
        failure_path = eval_dir / "failure-summary.json"
        run(
            [
                sys.executable,
                str(SCRIPT_DIR / "analyze_user_eval_failures.py"),
                str(eval_dir / "details.jsonl"),
                "--k",
                "5",
                "--output",
                str(failure_path),
            ],
            ROOT,
        )
        summary = load_json(eval_dir / "summary.json")
        health = load_json(health_path)
        status, reasons = eval_status(eval_label, group_overall(summary), health)
        health_summary[eval_label] = health
        eval_rows.append(
            {
                "eval_set": eval_label,
                "output_dir": str(eval_dir),
                "overall": group_overall(summary),
                "health": {
                    "blocking": health.get("blocking", False),
                    "blocking_count": health.get("blocking_count", 0),
                    "issue_counts": health.get("issue_counts", {}),
                },
                "status": status,
                "reasons": reasons,
            }
        )

    # 三级发布判定：全部 pass → pass；有 blocked → blocked；
    # blind 评测集 success@5 < 0.95 但无 blocked → gray_release（灰度发布）
    blocked = [row for row in eval_rows if row["status"] != "pass"]
    status = "pass" if not blocked else "blocked"
    if status == "pass" and any("blind" in row["eval_set"] for row in eval_rows):
        blind_rows = [row for row in eval_rows if "blind" in row["eval_set"]]
        if any(row["overall"].get("success@5", 0.0) < 0.95 for row in blind_rows):
            status = "gray_release"

    release_summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "index_dir": str(index_dir),
        "doc_manifest": str(current_manifest),
        "doc_diff": doc_diff,
        "evals": eval_rows,
    }
    write_json(output_dir / "release-summary.json", release_summary)
    write_json(output_dir / "eval-health-summary.json", health_summary)
    (output_dir / "release-report.md").write_text(render_report(release_summary), encoding="utf-8")
    print(f"release status: {status}")


if __name__ == "__main__":
    main()
