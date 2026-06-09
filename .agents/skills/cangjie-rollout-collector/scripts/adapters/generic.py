#!/usr/bin/env python3
"""Generic explicit-log adapter."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from adapters.base import status_result
from collector_core import assign_trace_refs, normalize_path, summarize_text, trace_event


MAX_GENERIC_EVENTS = 80


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    workspace_norm = normalize_path(workspace)
    if not trace_file:
        return status_result(
            runtime="generic",
            status="not_found",
            workspace=workspace_norm,
            warnings=["Generic adapter requires an explicit --trace-file log, JSONL, or Markdown file."],
        )

    selected = trace_file.expanduser()
    if not selected.exists():
        return status_result(
            runtime="generic",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Trace file does not exist: {selected}"],
        )

    events: list[dict[str, Any]] = []
    warnings = ["Generic adapter performs weak line-based parsing; verify the Rollout Record manually."]
    try:
        with selected.open("r", encoding="utf-8", errors="replace") as handle:
            for line_no, line in enumerate(handle, start=1):
                text = line.strip()
                if not text:
                    continue
                events.append(
                    trace_event(
                        runtime="generic",
                        session_id=session_id or "generic",
                        source_path=str(selected),
                        timestamp=None,
                        event_type="tool_output",
                        tool_name="generic_log",
                        status="observed",
                        input_summary="",
                        output_summary=summarize_text(text),
                        evidence_ref=f"file:{selected}#line:{line_no}",
                    )
                )
                if len(events) >= MAX_GENERIC_EVENTS:
                    warnings.append(f"Stopped after {MAX_GENERIC_EVENTS} non-empty log lines.")
                    break
    except Exception as exc:
        return status_result(
            runtime="generic",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Could not read trace file {selected}: {exc}"],
        )

    assign_trace_refs(events)
    return {
        "runtime": "generic",
        "status": "ok",
        "session_id": session_id or "generic",
        "source_path": str(selected),
        "workspace": workspace_norm,
        "collection_confidence": "medium" if events else "low",
        "events": events,
        "warnings": warnings,
    }
