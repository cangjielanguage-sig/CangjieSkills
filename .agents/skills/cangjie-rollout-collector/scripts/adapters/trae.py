#!/usr/bin/env python3
"""Reserved Trae adapter."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from adapters.base import unsupported_runtime
from collector_core import normalize_path


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    return unsupported_runtime("trae", normalize_path(workspace))
