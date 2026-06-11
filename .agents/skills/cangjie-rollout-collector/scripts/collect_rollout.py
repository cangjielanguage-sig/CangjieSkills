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
    build_trace_window,
    compact_source,
    first_user_task,
    latest_task_window_events,
    slugify_task_id,
    windowed_task_events,
)
from ground_truth import build_prompt_summary, load_ground_truth
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
    parser.add_argument("--trace-window-file", help="JSON file returned by ground_truth_required.")
    parser.add_argument("--trace-window-json", help="Inline trace_window JSON returned by ground_truth_required.")
    parser.add_argument("--ground-truth-file", help="JSON file with user ground truth feedback.")
    parser.add_argument("--ground-truth-json", help="Inline JSON with user ground truth feedback.")
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

    raw_events = [dict(event) for event in result.get("events") or []]
    ground_truth_supplied = bool(args.ground_truth_file or args.ground_truth_json)
    trace_window_supplied = bool(args.trace_window_file or args.trace_window_json)

    if ground_truth_supplied and not trace_window_supplied:
        events = [dict(event) for event in latest_task_window_events(raw_events)]
        assign_trace_refs(events)
        print(
            json.dumps(
                trace_window_required_summary(
                    trace_outcome=determine_outcome(events),
                    collection_confidence=result.get("collection_confidence") or "low",
                    warnings=result.get("warnings") or [],
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2

    if trace_window_supplied:
        trace_window, trace_window_errors = load_trace_window(
            args.trace_window_file, args.trace_window_json
        )
        if trace_window_errors:
            events = [dict(event) for event in latest_task_window_events(raw_events)]
            assign_trace_refs(events)
            print(
                json.dumps(
                    invalid_trace_window_summary(
                        errors=trace_window_errors,
                        trace_outcome=determine_outcome(events),
                        collection_confidence=result.get("collection_confidence") or "low",
                    ),
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 2
        events, trace_window_errors = windowed_task_events(
            raw_events,
            trace_window or {},
            target_skill=args.target_skill,
            session_id=result.get("session_id"),
            source_path=result.get("source_path"),
        )
        if trace_window_errors:
            fallback_events = [dict(event) for event in latest_task_window_events(raw_events)]
            assign_trace_refs(fallback_events)
            print(
                json.dumps(
                    invalid_trace_window_summary(
                        errors=trace_window_errors,
                        trace_outcome=determine_outcome(fallback_events),
                        collection_confidence=result.get("collection_confidence") or "low",
                    ),
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 2
        events = [dict(event) for event in events]
        assign_trace_refs(events)
        original_task = str((trace_window or {}).get("original_task") or first_user_task(events))
        task_id = str(
            (trace_window or {}).get("task_id")
            or args.task_id
            or slugify_task_id(original_task, fallback=args.target_skill)
        )
    else:
        events = [dict(event) for event in latest_task_window_events(raw_events)]
        assign_trace_refs(events)
        original_task = first_user_task(events)
        task_id = args.task_id or slugify_task_id(original_task, fallback=args.target_skill)

    trace_outcome = determine_outcome(events)
    ground_truth, ground_truth_errors = load_ground_truth(
        args.ground_truth_file, args.ground_truth_json
    )
    if ground_truth_errors:
        print(
            json.dumps(
                invalid_ground_truth_summary(
                    errors=ground_truth_errors,
                    trace_outcome=trace_outcome,
                    collection_confidence=result.get("collection_confidence") or "low",
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2
    if ground_truth is None:
        print(
            json.dumps(
                ground_truth_required_summary(
                    target_skill=args.target_skill,
                    task_id=task_id,
                    original_task=original_task,
                    trace_outcome=trace_outcome,
                    collection_confidence=result.get("collection_confidence") or "low",
                    events=events,
                    trace_window=build_trace_window(
                        events=events,
                        target_skill=args.target_skill,
                        task_id=task_id,
                        original_task=original_task,
                        runtime=result.get("runtime") or args.runtime,
                        session_id=result.get("session_id"),
                        source_path=result.get("source_path"),
                    ),
                    warnings=result.get("warnings") or [],
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    rollout_id, rollout_path = allocate_rollout_path(
        workspace=workspace,
        target_skill=args.target_skill,
        task_id=task_id,
    )
    record = build_record(
        args=args,
        adapter_result=result,
        events=events,
        rollout_id=rollout_id,
        rollout_path=rollout_path,
        task_id=task_id,
        trace_outcome=trace_outcome,
        ground_truth=ground_truth,
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
    trace_outcome: str,
    ground_truth: dict[str, Any],
    original_task: str,
) -> dict[str, Any]:
    source_path = adapter_result.get("source_path")
    session_id = adapter_result.get("session_id")
    verification_count = len(verification_lines(events))
    adjudicated_outcome = ground_truth["adjudicated_outcome"]
    summary = build_summary(adjudicated_outcome, trace_outcome, len(events), verification_count)
    return {
        "rollout_id": rollout_id,
        "target_skill": args.target_skill,
        "task_id": task_id,
        "outcome": adjudicated_outcome,
        "trace_outcome": trace_outcome,
        "adjudicated_outcome": adjudicated_outcome,
        "outcome_source": "ground_truth",
        "ground_truth_status": "provided",
        "trace_runtime": adapter_result.get("runtime") or args.runtime,
        "trace_source": compact_source(adapter_result.get("runtime") or args.runtime, session_id, source_path),
        "collection_confidence": adapter_result.get("collection_confidence") or "low",
        "original_task": original_task,
        "key_constraints": "none",
        "skill_used": args.target_skill,
        "summary": summary,
        "source_path": source_path,
        "rollout_path": str(rollout_path),
        "ground_truth": ground_truth,
        "warnings": adapter_result.get("warnings") or [],
    }


def build_summary(
    adjudicated_outcome: str, trace_outcome: str, event_count: int, verification_count: int
) -> str:
    prefix = (
        f"Collected {event_count} trace events; trace_outcome={trace_outcome}; "
        f"ground_truth adjudicated outcome is {adjudicated_outcome}."
    )
    if verification_count:
        return f"{prefix} Found {verification_count} verification event(s)."
    return f"{prefix} No trace verification evidence was found."


def success_summary(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "ok",
        "rollout_path": record.get("rollout_path"),
        "rollout_id": record.get("rollout_id"),
        "outcome": record.get("outcome"),
        "trace_outcome": record.get("trace_outcome"),
        "adjudicated_outcome": record.get("adjudicated_outcome"),
        "ground_truth_status": record.get("ground_truth_status"),
        "collection_confidence": record.get("collection_confidence"),
        "warnings": record.get("warnings") or [],
    }


def load_trace_window(
    trace_window_file: str | None, trace_window_json: str | None
) -> tuple[dict[str, Any] | None, list[str]]:
    if trace_window_file and trace_window_json:
        return None, ["Use only one of --trace-window-file or --trace-window-json."]
    if not trace_window_file and not trace_window_json:
        return None, []

    try:
        if trace_window_file:
            raw = Path(trace_window_file).expanduser().read_text(encoding="utf-8-sig")
        else:
            raw = trace_window_json or ""
        payload = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"Could not read trace_window JSON: {exc}"]

    if not isinstance(payload, dict):
        return None, ["trace_window must be a JSON object."]
    return payload, []


def ground_truth_required_summary(
    *,
    target_skill: str,
    task_id: str,
    original_task: str,
    trace_outcome: str,
    collection_confidence: str,
    events: list[dict[str, Any]],
    trace_window: dict[str, Any],
    warnings: list[str],
) -> dict[str, Any]:
    return {
        "status": "ground_truth_required",
        "rollout_path": None,
        "rollout_id": None,
        "outcome": None,
        "trace_outcome": trace_outcome,
        "ground_truth_status": "required",
        "collection_confidence": collection_confidence,
        "prompt_summary": build_prompt_summary(
            target_skill=target_skill,
            task_id=task_id,
            original_task=original_task,
            trace_outcome=trace_outcome,
            collection_confidence=collection_confidence,
            events=events,
        ),
        "trace_window": trace_window,
        "warnings": warnings,
    }


def trace_window_required_summary(
    *, trace_outcome: str, collection_confidence: str, warnings: list[str]
) -> dict[str, Any]:
    return {
        "status": "trace_window_required",
        "rollout_path": None,
        "rollout_id": None,
        "outcome": None,
        "trace_outcome": trace_outcome,
        "ground_truth_status": "provided",
        "trace_window_status": "required",
        "collection_confidence": collection_confidence,
        "warnings": [
            "Ground truth was provided, but the trace_window from the ground_truth_required response is required before saving."
        ]
        + warnings,
    }


def invalid_trace_window_summary(
    *, errors: list[str], trace_outcome: str, collection_confidence: str
) -> dict[str, Any]:
    return {
        "status": "invalid_trace_window",
        "rollout_path": None,
        "rollout_id": None,
        "outcome": None,
        "trace_outcome": trace_outcome,
        "ground_truth_status": "unknown",
        "trace_window_status": "invalid",
        "collection_confidence": collection_confidence,
        "warnings": errors,
    }


def invalid_ground_truth_summary(
    *, errors: list[str], trace_outcome: str, collection_confidence: str
) -> dict[str, Any]:
    return {
        "status": "invalid_ground_truth",
        "rollout_path": None,
        "rollout_id": None,
        "outcome": None,
        "trace_outcome": trace_outcome,
        "ground_truth_status": "invalid",
        "collection_confidence": collection_confidence,
        "warnings": errors,
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
