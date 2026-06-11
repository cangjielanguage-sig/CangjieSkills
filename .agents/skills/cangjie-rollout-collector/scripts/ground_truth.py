#!/usr/bin/env python3
"""Ground truth validation and prompt summaries for Rollout Records."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from collector_core import summarize_text
from outcome import VALID_OUTCOMES, verification_lines


TASK_COMPLETED_VALUES = ("yes", "partial", "no", "blocked", "unknown")
CONFIDENCE_VALUES = ("high", "medium", "low")
GROUND_TRUTH_REQUIRED_FIELDS = (
    "task_completed",
    "adjudicated_outcome",
    "result_gaps",
    "process_gaps",
    "missed_steps",
    "notes",
    "confidence",
)
SUGGESTED_QUESTIONS = [
    "目标 Skill 是否完成了这次任务？",
    "最终结果还缺少哪些点？没有则写 none。",
    "agent 执行过程是否漏了步骤、走错方向或缺少验证？没有则写 none。",
    "是否有需要 agent 回看 trace 确认的过程考察点？没有则写 none。",
]
PROCESS_REVIEW_GUIDANCE = [
    "If user feedback asks for process coverage/checkpoint confirmation, inspect prompt_summary.key_steps and the trace window before writing ground truth.",
    "Do not copy the user's process-check request into notes verbatim.",
    "Write process_gaps only for missing, wrong, or unverified process steps; otherwise use none.",
    "Write notes as the agent's verification conclusion with trace_ref evidence, for example: confirmed requested checkpoints at T009-T011.",
]
PROCESS_REVIEW_CUE_RE = re.compile(
    r"(确认|核验|验证|检查|审查|考察|覆盖|回看|复核|过程|步骤|漏步|证据|"
    r"confirm|verify|review|check|audit|process|checkpoint|coverage|step|evidence)",
    re.IGNORECASE,
)
TRACE_REF_OR_NOT_OBSERVED_RE = re.compile(r"\bT\d{3}\b|not_observed")
GENERIC_STEP_CUES = (
    "--",
    ".json",
    ".jsonl",
    ".md",
    ".py",
    "command",
    "path",
    "file",
    "read",
    "write",
    "open",
    "find",
    "search",
    "rg ",
    "grep",
    "ripgrep",
    "select-string",
    "get-content",
    "搜索",
    "文档",
    "文件",
    "路径",
)


def load_ground_truth(
    ground_truth_file: str | None, ground_truth_json: str | None
) -> tuple[dict[str, Any] | None, list[str]]:
    if ground_truth_file and ground_truth_json:
        return None, ["Use only one of --ground-truth-file or --ground-truth-json."]
    if not ground_truth_file and not ground_truth_json:
        return None, []

    try:
        if ground_truth_file:
            raw = Path(ground_truth_file).expanduser().read_text(encoding="utf-8-sig")
        else:
            raw = ground_truth_json or ""
        payload = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"Could not read ground truth JSON: {exc}"]

    return normalize_ground_truth(payload)


def normalize_ground_truth(payload: Any) -> tuple[dict[str, Any] | None, list[str]]:
    if not isinstance(payload, dict):
        return None, ["Ground truth must be a JSON object."]

    errors: list[str] = []
    for field in GROUND_TRUTH_REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"Missing required ground truth field: {field}.")

    task_completed = str(payload.get("task_completed", "")).strip()
    if task_completed not in TASK_COMPLETED_VALUES:
        errors.append(
            "task_completed must be one of: " + ", ".join(TASK_COMPLETED_VALUES) + "."
        )

    adjudicated_outcome = str(payload.get("adjudicated_outcome", "")).strip()
    if adjudicated_outcome not in VALID_OUTCOMES:
        errors.append(
            "adjudicated_outcome must be one of: " + ", ".join(VALID_OUTCOMES) + "."
        )

    confidence = str(payload.get("confidence", "")).strip()
    if confidence not in CONFIDENCE_VALUES:
        errors.append("confidence must be one of: " + ", ".join(CONFIDENCE_VALUES) + ".")

    reviewer = str(payload.get("reviewer") or "user").strip() or "user"
    if reviewer != "user":
        errors.append("reviewer must be user.")

    reviewed_at = str(payload.get("reviewed_at") or now_iso()).strip()
    if not reviewed_at:
        errors.append("reviewed_at must be a non-empty ISO8601 string.")

    result_gaps = normalized_text(payload.get("result_gaps"))
    process_gaps = normalized_text(payload.get("process_gaps"))
    missed_steps = normalized_text(payload.get("missed_steps"))
    notes = normalized_text(payload.get("notes"))

    if notes_need_trace_refs(notes):
        errors.append(
            "notes mentions process review/checkpoints but does not include trace_ref evidence. "
            "Inspect the trace_window/prompt_summary first, then write an agent verification "
            "conclusion with refs such as T009 or not_observed instead of copying user feedback verbatim."
        )

    if errors:
        return None, errors

    return {
        "reviewer": reviewer,
        "reviewed_at": reviewed_at,
        "task_completed": task_completed,
        "adjudicated_outcome": adjudicated_outcome,
        "result_gaps": result_gaps,
        "process_gaps": process_gaps,
        "missed_steps": missed_steps,
        "notes": notes,
        "confidence": confidence,
    }, []


def build_prompt_summary(
    *,
    target_skill: str,
    task_id: str,
    original_task: str,
    trace_outcome: str,
    collection_confidence: str,
    events: list[dict[str, Any]],
) -> dict[str, Any]:
    failed_events = [
        event
        for event in events
        if event.get("status") == "failure"
    ]
    return {
        "target_skill": target_skill,
        "task_id": task_id,
        "original_task": summarize_text(original_task),
        "trace_outcome": trace_outcome,
        "collection_confidence": collection_confidence,
        "event_count": len(events),
        "verification": verification_lines(events) or ["not_verified"],
        "known_failures_or_detours": [
            f"{event.get('trace_ref') or 'not_observed'}: "
            f"{event.get('tool_name') or event.get('event_type') or 'event'} -> "
            f"{event.get('output_summary') or event.get('status') or 'failure'}"
            for event in failed_events[:5]
        ]
        or ["none"],
        "key_steps": key_step_summaries(events),
        "process_review_guidance": PROCESS_REVIEW_GUIDANCE,
        "suggested_questions": SUGGESTED_QUESTIONS,
    }


def key_step_summaries(events: list[dict[str, Any]], limit: int = 12) -> list[str]:
    if not events:
        return ["not_observed"]

    selected_indexes: list[int] = []
    seen: set[int] = set()

    def add(index: int) -> None:
        if index not in seen and len(selected_indexes) < limit:
            seen.add(index)
            selected_indexes.append(index)

    for index, event in enumerate(events):
        if event.get("event_type") == "user_message":
            add(index)
            break

    scored_events = [
        (key_step_score(event), index)
        for index, event in enumerate(events)
        if index not in seen
    ]
    for score, index in sorted(scored_events, key=lambda item: (-item[0], item[1])):
        if score <= 0:
            continue
        add(index)

    for index in range(len(events)):
        add(index)
        if len(selected_indexes) >= limit:
            break

    return [format_step_summary(events[index]) for index in sorted(selected_indexes)]


def key_step_score(event: dict[str, Any]) -> int:
    event_type = str(event.get("event_type") or "")
    status = str(event.get("status") or "")
    text = " ".join(
        str(event.get(field) or "")
        for field in ("tool_name", "input_summary", "output_summary")
    ).casefold()

    score = 0
    if status == "failure":
        score += 100
    if event_type == "verification":
        score += 80
    if event_type in {"tool_call", "tool_output"}:
        score += 50
    if event_type == "agent_message":
        score += 15
    if is_command_or_structured_text(text):
        score += 20
    for keyword in GENERIC_STEP_CUES:
        if keyword in text:
            score += 8
    return score


def format_step_summary(event: dict[str, Any]) -> str:
    ref = event.get("trace_ref") or "not_observed"
    kind = event.get("event_type") or "event"
    tool = event.get("tool_name")
    label = f"{kind}:{tool}" if tool else kind
    detail = event.get("output_summary") or event.get("input_summary") or event.get("status")
    return f"{ref} {label}: {summarize_text(detail or 'observed')}"


def notes_need_trace_refs(notes: str) -> bool:
    if not notes or notes == "none":
        return False
    if not PROCESS_REVIEW_CUE_RE.search(notes):
        return False
    return not TRACE_REF_OR_NOT_OBSERVED_RE.search(notes)


def is_command_or_structured_text(text: str) -> bool:
    return any(token in text for token in ("{", "}", "[", "]", "--", ":", "/", "\\"))


def normalized_text(value: Any) -> str:
    if value is None:
        return "none"
    if isinstance(value, list):
        value = "; ".join(str(item) for item in value)
    text = summarize_text(str(value)).strip()
    return text or "none"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
