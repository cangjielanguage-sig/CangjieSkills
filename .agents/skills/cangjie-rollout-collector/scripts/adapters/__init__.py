#!/usr/bin/env python3
"""Adapter dispatch for rollout collection."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from . import codex, generic, trae
from .base import unsupported_runtime
from collector_core import normalize_path


def collect_trace(
    runtime: str,
    workspace: Path,
    trace_file: Path | None = None,
    session_id: str | None = None,
) -> dict[str, Any]:
    normalized = runtime.lower().strip()
    if normalized == "codex":
        return codex.collect(workspace=workspace, trace_file=trace_file, session_id=session_id)
    if normalized == "generic":
        return generic.collect(workspace=workspace, trace_file=trace_file, session_id=session_id)
    if normalized == "trae":
        return trae.collect(workspace=workspace, trace_file=trace_file, session_id=session_id)
    return unsupported_runtime(normalized, normalize_path(workspace))
