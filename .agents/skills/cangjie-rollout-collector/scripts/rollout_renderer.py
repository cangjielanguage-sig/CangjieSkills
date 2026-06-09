#!/usr/bin/env python3
"""Render normalized trace data as a Rollout Record."""

from __future__ import annotations

from typing import Any

from collector_core import looks_encoding_damaged, normalize_text_encoding
from outcome import verification_lines


MAX_FIELD_CHARS = 500
MAX_CELL_CHARS = 360


def render_rollout(record: dict[str, Any], events: list[dict[str, Any]]) -> str:
    warnings = record.get("warnings") or []
    source_path = record.get("source_path")
    rollout_path = record.get("rollout_path")

    lines = [
        "## Rollout Record",
        "",
        f"- rollout_id: {record['rollout_id']}",
        f"- target_skill: {record['target_skill']}",
        f"- task_id: {record['task_id']}",
        f"- outcome: {record['outcome']}",
        f"- trace_runtime: {record['trace_runtime']}",
        f"- trace_source: {metadata_value(record['trace_source'])}",
        f"- collection_confidence: {record['collection_confidence']}",
        f"- original_task: {metadata_value(record['original_task'])}",
        f"- key_constraints: {metadata_value(record.get('key_constraints') or 'none')}",
        f"- skill_used: {metadata_value(record.get('skill_used') or record['target_skill'])}",
        f"- summary: {metadata_value(record['summary'])}",
        "",
        "### Observable Steps",
        "",
        "| step | trace_ref | action/tool | input/params | public rationale | observed result | used_experience |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    if events:
        for index, event in enumerate(events, start=1):
            lines.append(render_step(index, event))
    else:
        lines.append("| S1 | not_observed | none | none | no structured trace was available | not_observed | none |")

    lines.extend(
        [
            "",
            "### Trace Evidence Map",
            "",
            "| trace_ref | event_type | tool/status | evidence_ref | summary |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    if events:
        for event in events:
            lines.append(render_evidence(event))
    else:
        lines.append("| not_observed | none | none | not_observed | no structured evidence |")

    lines.extend(["", "### Artifacts", ""])
    if source_path:
        lines.append(f"- trace file: {source_path}")
    if rollout_path:
        lines.append(f"- rollout record: {rollout_path}")
    if not source_path and not rollout_path:
        lines.append("- none")

    lines.extend(["", "### Verification", ""])
    verifications = verification_lines(events)
    if verifications:
        for item in verifications:
            lines.append(f"- {md_text(item)}")
    else:
        lines.append("- not_verified")

    lines.extend(["", "### Failure Or Detour", ""])
    detours = failure_or_detour(events, warnings)
    if detours:
        for item in detours:
            lines.append(f"- {md_text(item)}")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "### Transferable Observations",
            "",
            "- pattern: none",
            "  generality: low",
            "  source_steps: not_observed",
            "",
        ]
    )
    return "\n".join(lines)


def render_step(index: int, event: dict[str, Any]) -> str:
    action = event.get("event_type") or "event"
    tool = event.get("tool_name")
    if tool:
        action = f"{action}:{tool}"
    observed = event.get("output_summary") or event.get("status") or "observed"
    return (
        f"| S{index} | {cell(event.get('trace_ref') or 'not_observed')} | {cell(action)} | "
        f"{cell(event.get('input_summary') or 'none')} | trace event | {cell(observed)} | none |"
    )


def render_evidence(event: dict[str, Any]) -> str:
    tool_status = "/".join(
        part
        for part in [str(event.get("tool_name") or ""), str(event.get("status") or "")]
        if part
    )
    summary = event.get("output_summary") or event.get("input_summary") or event.get("status") or "observed"
    return (
        f"| {cell(event.get('trace_ref') or 'not_observed')} | {cell(event.get('event_type') or 'event')} | "
        f"{cell(tool_status or 'observed')} | {cell(event.get('evidence_ref') or 'not_observed')} | {cell(summary)} |"
    )


def failure_or_detour(events: list[dict[str, Any]], warnings: list[str]) -> list[str]:
    items: list[str] = []
    for warning in warnings:
        items.append(f"warning: {warning}")
    for event in events:
        if event.get("status") == "failure":
            ref = event.get("trace_ref") or "not_observed"
            tool = event.get("tool_name") or event.get("event_type") or "event"
            summary = event.get("output_summary") or event.get("input_summary") or "failure observed"
            items.append(f"{ref}: {tool} failed; {summary}")
    return items


def cell(value: Any) -> str:
    return compact_text(value, MAX_CELL_CHARS).replace("|", "\\|").replace("\n", "<br>")


def metadata_value(value: Any) -> str:
    return compact_text(value, MAX_FIELD_CHARS).replace("\n", " / ")


def compact_text(value: Any, max_chars: int) -> str:
    text = md_text(value)
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + f"... <truncated {len(text) - max_chars} chars>"


def md_text(value: Any) -> str:
    text = "" if value is None else normalize_text_encoding(str(value))
    if looks_encoding_damaged(text):
        return "[encoding-damaged text omitted; see Trace Evidence Map]"
    return text.strip() or "none"
