#!/usr/bin/env python3
"""Shared result handling for HarmonyOS Device Connector commands.

Some hdc releases report transport or device failures in stdout while returning
process exit code 0.  Callers must therefore check both channels.
"""

from __future__ import annotations

import re
from typing import Optional


_FAILURE_PATTERNS = (
    re.compile(r"^\s*\[(?:fail|failed|failure)\]", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*(?:fail|failed|failure)\s*[:：]", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*failed\s+to\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*error\s*[:：]", re.IGNORECASE | re.MULTILINE),
    re.compile(r"\bdevice\s+(?:not\s+found|not\s+founded|not\s+connected|offline)\b", re.IGNORECASE),
    re.compile(r"\b(?:no|cannot\s+find)\s+(?:connected\s+)?device(?:s)?\b", re.IGNORECASE),
    re.compile(r"\btarget\s+(?:not\s+found|offline|unauthorized)\b", re.IGNORECASE),
    re.compile(r"\bconnect(?:ion)?\s+(?:failed|failure|refused|reset)\b", re.IGNORECASE),
    re.compile(r"\bexecute\s+command\s+failed\b", re.IGNORECASE),
    re.compile(r"\bunknown\s+command\b", re.IGNORECASE),
    re.compile(r"\bmissing\s+parameter\b", re.IGNORECASE),
    re.compile(r"\bincorrect\s+(?:command|parameter|arguments?)\b", re.IGNORECASE),
)


def hdc_failure_reason(exit_code: int, output: str) -> Optional[str]:
    """Return a concise failure reason, including failures hidden by exit code 0."""
    text = (output or "").strip()
    if exit_code != 0:
        first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
        return f"exit code {exit_code}" + (f": {first_line}" if first_line else "")

    # Avoid false positives for normal phrases such as "No error".  Patterns are
    # deliberately narrower than a generic substring search for "error"/"fail".
    for pattern in _FAILURE_PATTERNS:
        match = pattern.search(text)
        if match:
            line = next(
                (line.strip() for line in text.splitlines() if match.group(0).lower() in line.lower()),
                match.group(0).strip(),
            )
            return f"hdc reported failure: {line}"
    return None


def hdc_command_ok(exit_code: int, output: str) -> bool:
    """Whether an hdc command succeeded by both process and textual semantics."""
    return hdc_failure_reason(exit_code, output) is None
