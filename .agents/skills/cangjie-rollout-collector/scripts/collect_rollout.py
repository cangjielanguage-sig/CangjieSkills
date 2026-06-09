#!/usr/bin/env python3
"""Collect trace data and persist a Rollout Record."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from adapters import collect_trace
from collector_core import (
    allocate_rollout_path,
    assign_trace_refs,
    compact_source,
    first_user_task,
    latest_task_events,
    slugify_task_id,
)
from outcome import determine_outcome, verification_lines
from rollout_renderer import render_rollout


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Collect agent trace events and save a Rollout Record."
    )
    parser.add_argument("--runtime", required=True, help="Trace runtime, e.g. codex.")
    parser.add_argument("--workspace", required=True, help="Workspace where records are saved.")
    parser.add_argument("--target-skill", required=True, help="Target skill name for the record.")
    parser.add_argument("--task-id", help="Stable task id. Generated from the task when omitted.")
    parser.add_argument("--trace-file", help="Explicit trace/log file path.")
    parser.add_argument("--session-id", help="Explicit runtime session id.")
    args = parser.parse_args()

    workspace = Path(args.workspace).expanduser().resolve(strict=False)
    result = collect_trace(
        runtime=args.runtime,
        workspace=workspace,
        trace_file=Path(args.trace_file) if args.trace_file else None,
        session_id=args.session_id,
    )

    if result.get("status") != "ok":
        print(json.dumps(error_summary(result), ensure_ascii=False, indent=2))
        return 2

    events = [dict(event) for event in latest_task_events(result.get("events") or [])]
    assign_trace_refs(events)
    original_task = first_user_task(events)
    task_id = args.task_id or slugify_task_id(original_task, fallback=args.target_skill)
    rollout_id, rollout_path = allocate_rollout_path(
        workspace=workspace,
        target_skill=args.target_skill,
        task_id=task_id,
    )
    outcome = determine_outcome(events)
    record = build_record(
        args=args,
        adapter_result=result,
        events=events,
        rollout_id=rollout_id,
        rollout_path=rollout_path,
        task_id=task_id,
        outcome=outcome,
        original_task=original_task,
    )

    rollout_path.parent.mkdir(parents=True, exist_ok=True)
    rollout_path.write_text(render_rollout(record, events), encoding="utf-8")

    print(json.dumps(success_summary(record), ensure_ascii=False, indent=2))
    return 0


def build_record(
    args: argparse.Namespace,
    adapter_result: dict[str, Any],
    events: list[dict[str, Any]],
    rollout_id: str,
    rollout_path: Path,
    task_id: str,
    outcome: str,
    original_task: str,
) -> dict[str, Any]:
    source_path = adapter_result.get("source_path")
    session_id = adapter_result.get("session_id")
    verification_count = len(verification_lines(events))
    summary = build_summary(outcome, len(events), verification_count)
    return {
        "rollout_id": rollout_id,
        "target_skill": args.target_skill,
        "task_id": task_id,
        "outcome": outcome,
        "trace_runtime": adapter_result.get("runtime") or args.runtime,
        "trace_source": compact_source(adapter_result.get("runtime") or args.runtime, session_id, source_path),
        "collection_confidence": adapter_result.get("collection_confidence") or "low",
        "original_task": original_task,
        "key_constraints": "none",
        "skill_used": args.target_skill,
        "summary": summary,
        "source_path": source_path,
        "rollout_path": str(rollout_path),
        "warnings": adapter_result.get("warnings") or [],
    }


def build_summary(outcome: str, event_count: int, verification_count: int) -> str:
    if verification_count:
        return f"Collected {event_count} trace events and found {verification_count} verification event(s); outcome is {outcome}."
    return f"Collected {event_count} trace events with no verification evidence; outcome is {outcome}."


def success_summary(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "ok",
        "rollout_path": record.get("rollout_path"),
        "rollout_id": record.get("rollout_id"),
        "outcome": record.get("outcome"),
        "collection_confidence": record.get("collection_confidence"),
        "warnings": record.get("warnings") or [],
    }


def error_summary(result: dict[str, Any]) -> dict[str, Any]:
    summary = {
        "status": result.get("status"),
        "rollout_path": None,
        "rollout_id": None,
        "outcome": None,
        "collection_confidence": result.get("collection_confidence") or "low",
        "warnings": result.get("warnings") or [],
    }
    if "candidates" in result:
        summary["candidates"] = result["candidates"]
    return summary


if __name__ == "__main__":
    sys.exit(main())
