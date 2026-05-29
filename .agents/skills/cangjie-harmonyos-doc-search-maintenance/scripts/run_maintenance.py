#!/usr/bin/env python3
"""运行 doc-search 的重建、评测与记录沉淀流程。"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
MAINTENANCE_DIR = SCRIPT_DIR.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-harmonyos-doc-search"
RECORDS_DIR = MAINTENANCE_DIR / "records"
RUN_HISTORY_DIR = RECORDS_DIR / "run-history"
BASELINES_DIR = RECORDS_DIR / "baselines"
CHANGELOG_PATH = RECORDS_DIR / "changelog.md"
WORKFLOW_VERSION = "v3-stage3"
API_GATE_THRESHOLD = 1.0
DEFAULT_LLM_CARD_TYPES = "task,api,example,doc"

sys.path.insert(0, str(SEARCH_SKILL_DIR))
sys.path.insert(0, str(SEARCH_SKILL_DIR / "scripts"))

from build_index_v3 import build as build_index, parse_card_types  # noqa: E402
from audit_api_coverage import build_report as build_api_audit_report, write_report as write_api_audit_report  # noqa: E402
from eval_bench import load_eval_set, make_openviking_search, make_v3_search, run_benchmark  # noqa: E402


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sync_index_dir(source_dir: Path, target_dir: Path) -> list[str]:
    target_dir.mkdir(parents=True, exist_ok=True)
    synced: list[str] = []
    for name in ("manifest.json", "tasks.jsonl", "apis.jsonl", "examples.jsonl", "docs.jsonl", "aliases.json", "search.db"):
        source = source_dir / name
        target = target_dir / name
        shutil.copy2(source, target)
        synced.append(str(target))
    return synced


def overall_metrics(result: dict) -> dict:
    return result["summary"]["overall"]


def choose_publish_mode(benchmarks: dict) -> tuple[str, dict]:
    rule = overall_metrics(benchmarks["v3-rule"])
    rule_llm = overall_metrics(benchmarks["v3-rule+llm"])
    choices = {
        "rule": rule,
        "rule+llm": rule_llm,
    }
    selected_mode = max(
        choices,
        key=lambda mode: (
            choices[mode]["mrr"],
            choices[mode]["recall@5"],
            1 if mode == "rule" else 0,
        ),
    )
    compare_mode = "rule+llm" if selected_mode == "rule" else "rule"
    selected = choices[selected_mode]
    compare = choices[compare_mode]
    reason = (
        f"按 mrr 优先、recall@5 次优、rule 稳定性兜底 选择 {selected_mode}；"
        f"{selected_mode}.mrr={selected['mrr']} vs {compare_mode}.mrr={compare['mrr']}，"
        f"{selected_mode}.recall@5={selected['recall@5']} vs {compare_mode}.recall@5={compare['recall@5']}。"
    )
    return selected_mode, {
        "selected_mode": selected_mode,
        "comparison_mode": compare_mode,
        "reason": reason,
        "selected_metrics": selected,
        "comparison_metrics": compare,
    }


def llm_full_enrichment_gate(manifest: dict, llm_card_types: tuple[str, ...]) -> list[str]:
    counts = manifest.get("counts", {})
    llm = manifest.get("llm", {})
    reasons: list[str] = []
    if llm.get("failed", 0):
        reasons.append(f"rule+llm failed={llm.get('failed')}")
    expected_keys = {
        "task": ("tasks", "llm_enriched_tasks"),
        "api": ("apis", "llm_enriched_apis"),
        "example": ("examples", "llm_enriched_examples"),
        "doc": ("docs", "llm_enriched_docs"),
    }
    by_type = llm.get("by_card_type", {})
    for card_type in llm_card_types:
        total_key, enriched_key = expected_keys[card_type]
        expected = counts.get(total_key, 0)
        enriched = counts.get(enriched_key, 0)
        succeeded = by_type.get(card_type, {}).get("succeeded", enriched)
        if enriched != expected or succeeded != expected:
            reasons.append(f"{card_type}: enriched={enriched}/{expected}, succeeded={succeeded}/{expected}")
    return reasons


def llm_regression_gate(benchmarks: dict) -> list[str]:
    rule = overall_metrics(benchmarks["v3-rule"])
    rule_llm = overall_metrics(benchmarks["v3-rule+llm"])
    reasons: list[str] = []
    for key in ("recall@5", "recall@10", "mrr"):
        if rule_llm[key] < rule[key]:
            reasons.append(f"{key}: rule+llm={rule_llm[key]} < rule={rule[key]}")
    for category, rule_metrics in benchmarks["v3-rule"]["summary"].items():
        if category == "overall":
            continue
        llm_metrics = benchmarks["v3-rule+llm"]["summary"].get(category, {})
        for key in ("recall@5", "recall@10", "mrr"):
            if llm_metrics.get(key, 0) < rule_metrics.get(key, 0):
                reasons.append(f"{category}.{key}: rule+llm={llm_metrics.get(key, 0)} < rule={rule_metrics.get(key, 0)}")
    return reasons


def markdown_summary(report: dict) -> str:
    llm = report["builds"]["rule+llm"].get("llm", {})
    publish = report.get("publish_decision")
    api_audit = report.get("api_audit", {})
    lines = [
        f"# doc-search maintenance run",
        "",
        f"- **timestamp**: {report['timestamp']}",
        f"- **status**: {report.get('status', 'success')}",
        f"- **workflow_version**: {report['workflow_version']}",
        f"- **note**: {report['note'] or '无'}",
        f"- **eval_set**: `{report['eval_set']}`",
        f"- **limit**: {report['limit']}",
        "",
        "## Build",
        "",
        f"- `rule`: tasks={report['builds']['rule']['counts']['tasks']}, apis={report['builds']['rule']['counts']['apis']}, examples={report['builds']['rule']['counts']['examples']}, docs={report['builds']['rule']['counts'].get('docs', 0)}",
        f"- `rule+llm`: tasks={report['builds']['rule+llm']['counts']['tasks']}, apis={report['builds']['rule+llm']['counts']['apis']}, examples={report['builds']['rule+llm']['counts']['examples']}, docs={report['builds']['rule+llm']['counts'].get('docs', 0)}",
        f"- `rule+llm llm_stats`: requested={llm.get('requested', 0)}, succeeded={llm.get('succeeded', 0)}, failed={llm.get('failed', 0)}, skipped={llm.get('skipped', 0)}, batch_fallbacks={llm.get('batch_fallbacks', 0)}",
        f"- `rule+llm provider_status`: {llm.get('provider_status', 'unknown')}",
        f"- `rule+llm provider_stop_reason`: {llm.get('provider_stop_reason', '无')}",
        "",
        "## API Audit",
        "",
        f"- `rule`: coverage={api_audit.get('rule', {}).get('coverage_ratio', 0):.2%}, covered={api_audit.get('rule', {}).get('covered_docs', 0)}/{api_audit.get('rule', {}).get('total_docs', 0)}, invalid_paths={api_audit.get('rule', {}).get('invalid_source_paths', 0)}, passed={api_audit.get('rule', {}).get('gate_passed', False)}",
        f"- `rule+llm`: coverage={api_audit.get('rule+llm', {}).get('coverage_ratio', 0):.2%}, covered={api_audit.get('rule+llm', {}).get('covered_docs', 0)}/{api_audit.get('rule+llm', {}).get('total_docs', 0)}, invalid_paths={api_audit.get('rule+llm', {}).get('invalid_source_paths', 0)}, passed={api_audit.get('rule+llm', {}).get('gate_passed', False)}",
    ]
    if report.get("status") in {"failed_api_gate", "failed_gate", "failed_regression_gate"}:
        lines.extend(["", "## Gate Failure", ""])
        for reason in report.get("gate_failure_reasons", []):
            lines.append(f"- {reason}")
        lines.append("")
    elif publish:
        lines.extend(
            [
                "",
                "## Published Index",
                "",
                f"- `selected_publish_mode`: `{publish['selected_mode']}`",
                f"- `selection_reason`: {publish['reason']}",
                f"- `default_index_dir`: `{report['published_index']['target_dir']}`",
                f"- `published_from`: `{report['published_index']['source_dir']}`",
                "",
                "## Benchmarks",
                "",
            ]
        )
    for name, result in report["benchmarks"].items():
        if "error" in result:
            lines.extend(
                [
                    f"### {name}",
                    f"- error: {result['error']}",
                    "",
                ]
            )
            continue
        overall = result["summary"]["overall"]
        lines.extend(
            [
                f"### {name}",
                f"- recall@5: {overall['recall@5']}",
                f"- recall@10: {overall['recall@10']}",
                f"- mrr: {overall['mrr']}",
                f"- latency_p50_ms: {overall['latency_p50_ms']}",
                f"- latency_p95_ms: {overall['latency_p95_ms']}",
                "",
            ]
        )
    misses = {
        name: [row["query"] for row in result.get("details", []) if row["mrr"] == 0]
        for name, result in report["benchmarks"].items()
    }
    lines.append("## Misses")
    lines.append("")
    for name, items in misses.items():
        lines.append(f"### {name}")
        if "error" in report["benchmarks"][name]:
            lines.append(f"- skipped: {report['benchmarks'][name]['error']}")
            lines.append("")
            continue
        if not items:
            lines.append("- 无")
        else:
            for item in items[:10]:
                lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def append_changelog(timestamp: str, report: dict) -> None:
    publish = report.get("publish_decision")
    llm = report["builds"]["rule+llm"].get("llm", {})
    api_rule = report.get("api_audit", {}).get("rule", {})
    date = f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]}"
    if report.get("status") in {"failed_api_gate", "failed_gate", "failed_regression_gate"}:
        line = (
            f"- {date}：maintenance 运行失败，"
            f"{report['workflow_version']}，"
            f"门禁未通过，"
            f"coverage={api_rule.get('coverage_ratio', 0):.2%}，"
            f"reasons={'；'.join(report.get('gate_failure_reasons', []))}。"
        )
    else:
        overall = publish["selected_metrics"]
        line = (
            f"- {date}：完成一次 maintenance 运行，"
            f"{report['workflow_version']}，"
            f"发布 {publish['selected_mode']}，"
            f"api coverage={api_rule.get('coverage_ratio', 0):.2%}，"
            f"recall@5={overall['recall@5']}，mrr={overall['mrr']}，"
            f"llm failed={llm.get('failed', 0)}，"
            f"provider={llm.get('provider_status', 'unknown')}。"
        )
    existing = CHANGELOG_PATH.read_text(encoding="utf-8") if CHANGELOG_PATH.exists() else "# doc-search Maintenance Changelog\n\n"
    if not existing.endswith("\n"):
        existing += "\n"
    existing += line + "\n"
    CHANGELOG_PATH.write_text(existing, encoding="utf-8")


def check_openviking_endpoint(host: str, port: int, timeout: float = 3.0) -> str | None:
    url = f"http://{host}:{port}/api/v1/search/find"
    payload = json.dumps({"query": "list", "limit": 1}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": ",20250329.ljj",
    }
    request = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
        if body.get("status") != "ok":
            return f"OpenViking 接口返回非 ok 状态: {body.get('status')}"
        return None
    except urllib.error.HTTPError as exc:
        return f"HTTP {exc.code}: {exc.reason}"
    except urllib.error.URLError as exc:
        return f"连接错误: {exc.reason}"
    except Exception as exc:  # noqa: BLE001
        return str(exc)


def main() -> None:
    parser = argparse.ArgumentParser(description="运行 doc-search maintenance 流程")
    parser.add_argument("--eval-set", default=str(SEARCH_SKILL_DIR / "evals" / "search" / "eval_queries.jsonl"))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--host", default="111.229.30.227")
    parser.add_argument("--port", type=int, default=2026)
    parser.add_argument("--note", default="")
    parser.add_argument("--llm-card-types", default=DEFAULT_LLM_CARD_TYPES)
    parser.add_argument("--llm-concurrency", type=int, default=24)
    parser.add_argument("--llm-cache-dir", default=str(RECORDS_DIR / "llm-cache"))
    parser.add_argument("--allow-rule-fallback", action="store_true", help="允许 rule+llm 指标退化时发布 rule；默认退化即失败")
    parser.add_argument("--skip-openviking", action="store_true", help="跳过 OpenViking 远端基线评测")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUN_HISTORY_DIR / timestamp
    rule_index_dir = run_dir / "index-rule"
    rule_llm_index_dir = run_dir / "index-rule-llm"
    run_dir.mkdir(parents=True, exist_ok=True)

    eval_set = load_eval_set(args.eval_set)

    llm_card_types = parse_card_types(args.llm_card_types)
    rule_manifest = build_index(rule_index_dir, mode="rule")
    rule_llm_manifest = build_index(
        rule_llm_index_dir,
        mode="rule+llm",
        llm_card_types=llm_card_types,
        llm_concurrency=max(1, args.llm_concurrency),
        llm_cache_dir=Path(args.llm_cache_dir) if args.llm_cache_dir else None,
    )
    llm_gate_failure_reasons = llm_full_enrichment_gate(rule_llm_manifest, llm_card_types)

    api_audit_rule = build_api_audit_report(rule_index_dir, gate_threshold=API_GATE_THRESHOLD)
    api_audit_rule_llm = build_api_audit_report(rule_llm_index_dir, gate_threshold=API_GATE_THRESHOLD)
    write_api_audit_report(
        api_audit_rule,
        run_dir / "api-coverage-rule.json",
        run_dir / "api-coverage-rule.md",
    )
    write_api_audit_report(
        api_audit_rule_llm,
        run_dir / "api-coverage-rule-llm.json",
        run_dir / "api-coverage-rule-llm.md",
    )
    api_audit_summary = {
        "rule": {
            "total_docs": api_audit_rule["candidates"]["total_docs"],
            "covered_docs": api_audit_rule["candidates"]["covered_docs"],
            "coverage_ratio": api_audit_rule["candidates"]["coverage_ratio"],
            "invalid_source_paths": len(api_audit_rule["integrity"]["invalid_source_paths"]),
            "duplicate_source_path_hits": len(api_audit_rule["integrity"]["duplicate_candidate_source_path_hits"]),
            "gate_passed": api_audit_rule["gate"]["passed"],
            "gate_reasons": api_audit_rule["gate"]["reasons"],
        },
        "rule+llm": {
            "total_docs": api_audit_rule_llm["candidates"]["total_docs"],
            "covered_docs": api_audit_rule_llm["candidates"]["covered_docs"],
            "coverage_ratio": api_audit_rule_llm["candidates"]["coverage_ratio"],
            "invalid_source_paths": len(api_audit_rule_llm["integrity"]["invalid_source_paths"]),
            "duplicate_source_path_hits": len(api_audit_rule_llm["integrity"]["duplicate_candidate_source_path_hits"]),
            "gate_passed": api_audit_rule_llm["gate"]["passed"],
            "gate_reasons": api_audit_rule_llm["gate"]["reasons"],
        },
    }
    gate_failure_reasons = [
        *[f"rule+llm: {reason}" for reason in llm_gate_failure_reasons],
        *[f"rule: {reason}" for reason in api_audit_rule["gate"]["reasons"]],
        *[f"rule+llm: {reason}" for reason in api_audit_rule_llm["gate"]["reasons"]],
    ]
    if gate_failure_reasons:
        report = {
            "timestamp": timestamp,
            "status": "failed_gate",
            "workflow_version": WORKFLOW_VERSION,
            "note": args.note,
            "llm_card_types": list(llm_card_types),
            "eval_set": args.eval_set,
            "limit": args.limit,
            "builds": {
                "rule": rule_manifest,
                "rule+llm": rule_llm_manifest,
            },
            "api_audit": api_audit_summary,
            "gate_failure_reasons": gate_failure_reasons,
            "benchmarks": {},
        }
        write_text(run_dir / "report.json", json.dumps(report, ensure_ascii=False, indent=2))
        write_text(run_dir / "report.md", markdown_summary(report))
        append_changelog(timestamp, report)
        print(
            json.dumps(
                {
                    "run_dir": str(run_dir),
                    "status": "failed_gate",
                    "reasons": gate_failure_reasons,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        sys.exit(1)

    benchmarks = {
        "v3-rule": run_benchmark(make_v3_search(str(rule_index_dir), "auto"), eval_set, limit=args.limit),
        "v3-rule+llm": run_benchmark(make_v3_search(str(rule_llm_index_dir), "auto"), eval_set, limit=args.limit),
    }

    if args.skip_openviking:
        benchmarks["openviking"] = {"error": "skipped by --skip-openviking"}
    else:
        openviking_error = check_openviking_endpoint(args.host, args.port)
        if openviking_error:
            benchmarks["openviking"] = {"error": openviking_error}
        else:
            benchmarks["openviking"] = run_benchmark(make_openviking_search(args.host, args.port), eval_set, limit=args.limit)

    regression_failure_reasons = llm_regression_gate(benchmarks)
    if regression_failure_reasons and not args.allow_rule_fallback:
        report = {
            "timestamp": timestamp,
            "status": "failed_regression_gate",
            "workflow_version": WORKFLOW_VERSION,
            "note": args.note,
            "llm_card_types": list(llm_card_types),
            "eval_set": args.eval_set,
            "limit": args.limit,
            "builds": {
                "rule": rule_manifest,
                "rule+llm": rule_llm_manifest,
            },
            "api_audit": api_audit_summary,
            "gate_failure_reasons": regression_failure_reasons,
            "benchmarks": benchmarks,
        }
        write_text(run_dir / "report.json", json.dumps(report, ensure_ascii=False, indent=2))
        write_text(run_dir / "report.md", markdown_summary(report))
        append_changelog(timestamp, report)
        print(
            json.dumps(
                {
                    "run_dir": str(run_dir),
                    "status": "failed_regression_gate",
                    "reasons": regression_failure_reasons,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        sys.exit(1)

    selected_mode, publish_decision = choose_publish_mode(benchmarks)
    publish_source_dir = rule_index_dir if selected_mode == "rule" else rule_llm_index_dir
    published_files = sync_index_dir(publish_source_dir, SEARCH_SKILL_DIR / "index")
    selected_api_audit = api_audit_rule if selected_mode == "rule" else api_audit_rule_llm
    write_api_audit_report(
        selected_api_audit,
        RECORDS_DIR / "api-coverage" / f"{timestamp}.json",
        RECORDS_DIR / "api-coverage" / f"{timestamp}.md",
        latest_json=RECORDS_DIR / "api-coverage" / "latest.json",
        latest_md=RECORDS_DIR / "api-coverage" / "latest.md",
    )

    report = {
        "timestamp": timestamp,
        "status": "success",
        "workflow_version": WORKFLOW_VERSION,
        "note": args.note,
        "llm_card_types": list(llm_card_types),
        "eval_set": args.eval_set,
        "limit": args.limit,
        "builds": {
            "rule": rule_manifest,
            "rule+llm": rule_llm_manifest,
        },
        "api_audit": api_audit_summary,
        "publish_decision": publish_decision,
        "published_index": {
            "source_dir": str(publish_source_dir),
            "target_dir": str(SEARCH_SKILL_DIR / "index"),
            "files": published_files,
        },
        "benchmarks": benchmarks,
    }

    write_text(run_dir / "report.json", json.dumps(report, ensure_ascii=False, indent=2))
    write_text(run_dir / "report.md", markdown_summary(report))
    write_text(BASELINES_DIR / f"{timestamp}.json", json.dumps(report, ensure_ascii=False, indent=2))
    write_text(BASELINES_DIR / "latest.json", json.dumps(report, ensure_ascii=False, indent=2))
    append_changelog(timestamp, report)

    print(json.dumps({"run_dir": str(run_dir), "baseline": str(BASELINES_DIR / "latest.json")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
