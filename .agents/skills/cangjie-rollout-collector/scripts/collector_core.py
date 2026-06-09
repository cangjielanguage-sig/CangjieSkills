#!/usr/bin/env python3
"""Shared helpers for rollout trace collection."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_RECORD_ROOT = Path(".agents") / "skills" / "cangjie-rollout-collector" / "records" / "rollouts"
MAX_SUMMARY_CHARS = 1000
MOJIBAKE_REPAIR_ENCODINGS = ("gb18030", "gbk", "cp936")
COMMON_CJK_CHARS = set("的一是在不了有和人这中大为上个国用我以要他时来用们生到作地于出就分对成会可主发年动同工也能下过子说产种面而方后多定行学法所民得经十三之进着等部度家电力里如水化高自二理起小物现实加量都两体制机当使点从业本去把性好应开它合还因由其些然前外天政四日那社义事平形相全表间样与关各重新线内数正心反你明看原又么利比或但质气第向道命此变条只没结解问意建月公无系军很情者最立代想已通并提直题党程展五果料象员革位入常文总次品式活设及管特件长求老头基资边流路级少图山统接知较将组见计别她手角期根论运农指几九区强放决西被干做必战先回则任取据处队南给色光门即保治北造百规热领七海口东导器压志世金增争济阶油思术极交受联")


def normalize_path(path: Path) -> str:
    try:
        return str(path.expanduser().resolve(strict=False)).casefold()
    except Exception:
        return os.path.abspath(os.path.expanduser(str(path))).casefold()


def paths_related(candidate: str | None, workspace: str) -> bool:
    if not candidate:
        return False
    candidate_clean = candidate.rstrip("\\/")
    workspace_clean = workspace.rstrip("\\/")
    return (
        candidate_clean.startswith(workspace_clean + os.sep)
        or workspace_clean.startswith(candidate_clean + os.sep)
    )


def sanitize_path_part(value: str | None, fallback: str = "unknown") -> str:
    text = (value or "").strip()
    if not text:
        return fallback
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip(".-_")
    return text or fallback


def slugify_task_id(value: str | None, fallback: str = "unknown", max_length: int = 80) -> str:
    slug = sanitize_path_part((value or "").lower(), fallback=fallback)
    if len(slug) <= max_length:
        return slug
    return slug[:max_length].rstrip(".-_") or fallback


def make_rollout_id(target_skill: str, timestamp: datetime, sequence: int) -> str:
    target = sanitize_path_part(target_skill)
    return f"{target}-{timestamp:%Y%m%d-%H%M%S}-{sequence:03d}"


def allocate_rollout_path(
    workspace: Path,
    target_skill: str,
    task_id: str,
    rollout_id: str | None = None,
    now: datetime | None = None,
) -> tuple[str, Path]:
    timestamp = now or datetime.now()
    target_part = sanitize_path_part(target_skill)
    task_part = sanitize_path_part(task_id)
    record_dir = workspace / DEFAULT_RECORD_ROOT / target_part / task_part

    if rollout_id:
        candidate_id = sanitize_path_part(rollout_id)
        candidate_path = record_dir / f"{candidate_id}.md"
        if not candidate_path.exists():
            return candidate_id, candidate_path

    sequence = 1
    while True:
        candidate_id = make_rollout_id(target_part, timestamp, sequence)
        candidate_path = record_dir / f"{candidate_id}.md"
        if not candidate_path.exists():
            return candidate_id, candidate_path
        sequence += 1


def trace_event(
    runtime: str,
    session_id: str,
    source_path: str,
    timestamp: str | None,
    event_type: str,
    tool_name: str | None,
    status: str,
    input_summary: str,
    output_summary: str,
    evidence_ref: str,
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "runtime": runtime,
        "session_id": session_id,
        "source_path": source_path,
        "timestamp": timestamp,
        "event_type": event_type,
        "tool_name": tool_name or "",
        "status": status,
        "input_summary": input_summary,
        "output_summary": output_summary,
        "trace_ref": "",
        "evidence_ref": evidence_ref,
        "warnings": warnings or [],
    }


def assign_trace_refs(events: list[dict[str, Any]]) -> None:
    for index, event in enumerate(events, start=1):
        event["trace_ref"] = f"T{index:03d}"


def first_user_task(events: list[dict[str, Any]]) -> str:
    for event in events:
        if event.get("event_type") == "user_message" and event.get("input_summary"):
            return str(event["input_summary"])
    return "unknown"


def latest_task_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for index in range(len(events) - 1, -1, -1):
        if events[index].get("event_type") == "user_message":
            return events[index:]
    return events


def compact_source(runtime: str, session_id: str | None, source_path: str | None) -> str:
    if not source_path:
        return "not_observed"
    path = Path(source_path)
    if session_id:
        return f"{runtime} session {session_id} ({path.name})"
    return f"{runtime} ({path.name})"


def summarize_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return summarize_text(value)
    try:
        return summarize_text(json.dumps(value, ensure_ascii=False, sort_keys=True))
    except TypeError:
        return summarize_text(str(value))


def summarize_text(text: Any) -> str:
    if text is None:
        return ""
    rendered = normalize_text_encoding(redact(str(text))).replace("\r\n", "\n").strip()
    rendered = redact(rendered)
    if len(rendered) <= MAX_SUMMARY_CHARS:
        return rendered
    return rendered[:MAX_SUMMARY_CHARS].rstrip() + f"... <truncated {len(rendered) - MAX_SUMMARY_CHARS} chars>"


def normalize_text_encoding(text: str) -> str:
    """Repair common UTF-8-as-GBK mojibake when the conversion is clearly better."""
    if not text:
        return text

    best = text
    best_score = readability_score(text)
    for encoding in MOJIBAKE_REPAIR_ENCODINGS:
        for errors in ("strict", "ignore"):
            try:
                candidate = text.encode(encoding, errors=errors).decode("utf-8", errors=errors)
            except (UnicodeEncodeError, UnicodeDecodeError):
                continue
            if not candidate.strip():
                continue
            if len(candidate) < max(20, len(text) * 0.45):
                continue
            score = readability_score(candidate)
            if score > best_score + 8:
                best = candidate
                best_score = score
    return best


def looks_encoding_damaged(text: str | None) -> bool:
    if not text:
        return False
    metrics = text_quality_metrics(text)
    if metrics["private_use"] > 0 or metrics["replacement"] > 0:
        return True
    if metrics["repeated_question_marks"] >= 4:
        return True
    if metrics["cjk"] >= 24 and metrics["common_cjk"] / max(metrics["cjk"], 1) < 0.04:
        return True
    return False


def readability_score(text: str) -> float:
    metrics = text_quality_metrics(text)
    printable_ascii = metrics["ascii"] - metrics["control"]
    return (
        printable_ascii * 0.08
        + metrics["common_cjk"] * 2.5
        + metrics["cjk"] * 0.15
        - metrics["private_use"] * 30
        - metrics["replacement"] * 20
        - metrics["repeated_question_marks"] * 8
        - metrics["control"] * 20
    )


def text_quality_metrics(text: str) -> dict[str, int]:
    return {
        "ascii": sum(1 for ch in text if ord(ch) < 128),
        "control": sum(1 for ch in text if ord(ch) < 32 and ch not in "\n\r\t"),
        "cjk": sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff"),
        "common_cjk": sum(1 for ch in text if ch in COMMON_CJK_CHARS),
        "private_use": sum(1 for ch in text if "\ue000" <= ch <= "\uf8ff"),
        "replacement": text.count("\ufffd"),
        "repeated_question_marks": sum(len(match.group(0)) for match in re.finditer(r"\?{3,}", text)),
    }


def redact(text: str) -> str:
    patterns = [
        (r"(?i)(authorization\s*:\s*bearer\s+)[^\s\"']+", r"\1<redacted>"),
        (r"(?i)((?:api[_-]?key|token|password|secret)\s*[=:]\s*)[^\s,\"']+", r"\1<redacted>"),
        (r"sk-[A-Za-z0-9_-]{16,}", "<redacted-token>"),
    ]
    redacted = text
    for pattern, repl in patterns:
        redacted = re.sub(pattern, repl, redacted)
    return redacted
