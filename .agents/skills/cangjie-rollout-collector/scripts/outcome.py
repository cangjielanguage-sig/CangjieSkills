#!/usr/bin/env python3
"""Outcome classification for Rollout Records."""

from __future__ import annotations

import re
from typing import Any


SUCCESS_EVIDENCE_RE = re.compile(
    r"(?i)\b(pass(?:ed|es)?|0 errors?|0 failures?|success(?:ful)?|succeeded|ok|green)\b"
)


def determine_outcome(events: list[dict[str, Any]]) -> str:
    verification_events = [e for e in events if e.get("event_type") == "verification"]
    if any(e.get("status") == "failure" for e in verification_events):
        return "failure"
    if any(is_successful_verification(e) for e in verification_events):
        return "success"
    if any(e.get("status") == "failure" for e in events):
        return "partial"
    if events:
        return "not_verified"
    return "not_verified"


def is_successful_verification(event: dict[str, Any]) -> bool:
    if event.get("event_type") != "verification":
        return False
    if event.get("status") == "success":
        return True
    text = f"{event.get('input_summary', '')}\n{event.get('output_summary', '')}"
    return bool(SUCCESS_EVIDENCE_RE.search(text))


def verification_lines(events: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for event in events:
        if event.get("event_type") != "verification":
            continue
        ref = event.get("trace_ref") or "not_observed"
        tool = event.get("tool_name") or "verification"
        status = event.get("status") or "observed"
        summary = event.get("output_summary") or event.get("input_summary") or status
        lines.append(f"{ref}: {tool} -> {status}; {summary}")
    return lines
