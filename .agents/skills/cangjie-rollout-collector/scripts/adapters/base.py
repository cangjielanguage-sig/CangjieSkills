#!/usr/bin/env python3
"""Common adapter result helpers."""

from __future__ import annotations

from typing import Any


RECENT_CANDIDATE_LIMIT = 10


def unsupported_runtime(runtime: str, workspace: str | None) -> dict[str, Any]:
    return {
        "runtime": runtime,
        "status": "unsupported_runtime",
        "session_id": None,
        "source_path": None,
        "workspace": workspace,
        "collection_confidence": "low",
        "events": [],
        "warnings": [
            f"{runtime} adapter is reserved but not implemented. Provide a supported runtime or an explicit generic log file."
        ],
    }


def status_result(
    runtime: str,
    status: str,
    workspace: str | None,
    warnings: list[str],
    candidates: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    result = {
        "runtime": runtime,
        "status": status,
        "session_id": None,
        "source_path": None,
        "workspace": workspace,
        "collection_confidence": "low",
        "events": [],
        "warnings": warnings,
    }
    if candidates is not None:
        result["candidates"] = candidates
    return result


def ambiguous_result(
    runtime: str, workspace: str, candidates: list[dict[str, Any]]
) -> dict[str, Any]:
    return status_result(
        runtime=runtime,
        status="ambiguous_source",
        workspace=workspace,
        warnings=["Multiple possible trace sources matched; specify --trace-file or --session-id."],
        candidates=public_candidates(candidates),
    )


def public_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "session_id": c.get("session_id"),
            "source_path": str(c.get("source_path") or c.get("path")),
            "cwd": c.get("cwd"),
            "timestamp": c.get("timestamp"),
        }
        for c in sorted(candidates, key=lambda item: item.get("mtime", 0), reverse=True)[
            :RECENT_CANDIDATE_LIMIT
        ]
    ]
