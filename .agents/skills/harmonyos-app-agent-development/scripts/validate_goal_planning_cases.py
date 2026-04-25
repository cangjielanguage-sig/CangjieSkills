#!/usr/bin/env python3
"""校验 App Agent 目标到查询计划用例的结构健康度。"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROUTES = {"direct_doc_search", "app_goal_planning", "build_diagnosis", "runtime_diagnosis"}
MODES = {"auto", "task", "api", "example", "doc"}
CAPABILITIES = {
    "ability",
    "arkui_component",
    "build",
    "diagnostics",
    "interop",
    "media",
    "navigation",
    "network",
    "permission",
    "runtime",
    "security",
    "storage",
    "webview",
}
INTERNAL_WORDS = ("acceptable_paths", "expected_paths", ".jsonl", "evals/", "index/")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line"] = line_no
            rows.append(row)
    return rows


def weak_query(query: str) -> bool:
    lowered = query.lower()
    if any(word in lowered for word in INTERNAL_WORDS):
        return True
    return bool(re.search(r"(^|/)(harmonyos|std|stdx|tools|lang-features)(/|$)", lowered))


def add_issue(issues: list[dict[str, Any]], counts: dict[str, int], row: dict[str, Any], issue_type: str, **extra: Any) -> None:
    issue = {"line": row.get("_line"), "goal": row.get("goal", ""), "type": issue_type}
    issue.update(extra)
    issues.append(issue)
    counts[issue_type] += 1


def validate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    counts: dict[str, int] = defaultdict(int)
    duplicate_goals = {goal for goal, count in Counter(str(row.get("goal", "")) for row in rows).items() if count > 1}

    for row in rows:
        goal = str(row.get("goal", "")).strip()
        route = str(row.get("route", "")).strip()
        required = [str(item).strip() for item in row.get("required_capabilities", []) if str(item).strip()]
        query_plan = row.get("query_plan", [])
        acceptance = row.get("acceptance", [])

        if not goal:
            add_issue(issues, counts, row, "missing_goal")
        if goal in duplicate_goals:
            add_issue(issues, counts, row, "duplicate_goal")
        if route not in ROUTES:
            add_issue(issues, counts, row, "invalid_route", route=route)
        if not isinstance(query_plan, list) or not query_plan:
            add_issue(issues, counts, row, "missing_query_plan")
            continue
        if not isinstance(acceptance, list) or not acceptance:
            add_issue(issues, counts, row, "missing_acceptance")

        unknown_required = [item for item in required if item not in CAPABILITIES]
        if unknown_required:
            add_issue(issues, counts, row, "unknown_required_capability", capabilities=unknown_required)

        planned_capabilities: set[str] = set()
        for index, item in enumerate(query_plan, start=1):
            if not isinstance(item, dict):
                add_issue(issues, counts, row, "invalid_query_plan_item", index=index)
                continue
            query = str(item.get("query", "")).strip()
            mode = str(item.get("mode", "")).strip()
            purpose = str(item.get("purpose", "")).strip()
            capability = str(item.get("capability", "")).strip()
            planned_capabilities.add(capability)

            if not query:
                add_issue(issues, counts, row, "missing_query", index=index)
            elif weak_query(query):
                add_issue(issues, counts, row, "weak_query", index=index, query=query)
            if mode not in MODES:
                add_issue(issues, counts, row, "invalid_mode", index=index, mode=mode)
            if not purpose:
                add_issue(issues, counts, row, "missing_purpose", index=index)
            if capability not in CAPABILITIES:
                add_issue(issues, counts, row, "invalid_capability", index=index, capability=capability)

        missing_capabilities = [item for item in required if item not in planned_capabilities]
        if missing_capabilities:
            add_issue(issues, counts, row, "capability_not_covered", capabilities=missing_capabilities)

        if route == "direct_doc_search" and len(query_plan) > 2:
            add_issue(issues, counts, row, "direct_search_over_planned", query_count=len(query_plan))
        if route == "app_goal_planning" and len(query_plan) < max(2, len(required)):
            add_issue(issues, counts, row, "goal_planning_under_planned", query_count=len(query_plan))

    blocking_types = {
        "missing_goal",
        "invalid_route",
        "missing_query_plan",
        "invalid_mode",
        "invalid_capability",
        "capability_not_covered",
    }
    blocking = [issue for issue in issues if issue["type"] in blocking_types]
    return {
        "count": len(rows),
        "blocking": bool(blocking),
        "blocking_count": len(blocking),
        "issue_counts": dict(sorted(counts.items())),
        "issues": issues[:200],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="校验 App Agent 目标规划用例")
    parser.add_argument("--eval-set", default=str(Path(__file__).resolve().parent.parent / "evals" / "goal_planning_cases.jsonl"))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    summary = validate(load_jsonl(Path(args.eval_set)))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("count", "blocking", "blocking_count", "issue_counts")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
