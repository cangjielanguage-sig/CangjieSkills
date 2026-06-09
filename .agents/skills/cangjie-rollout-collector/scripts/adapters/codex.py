#!/usr/bin/env python3
"""Codex trace adapter."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from adapters.base import ambiguous_result, public_candidates, status_result
from collector_core import (
    assign_trace_refs,
    looks_encoding_damaged,
    normalize_path,
    normalize_text_encoding,
    paths_related,
    summarize_text,
    summarize_value,
    trace_event,
)


VALIDATION_COMMAND_RE = re.compile(
    r"(?i)\b(skill-lint|py_compile|pytest|unittest|cargo\s+test|go\s+test|npm\s+(?:run\s+)?test|pnpm\s+test|yarn\s+test|lint|build|cjpm\s+build)\b"
)
FILE_DUMP_COMMAND_RE = re.compile(r"(?i)\b(get-content|gc|type|cat)\b")


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    workspace_norm = normalize_path(workspace)

    if trace_file:
        selected = trace_file.expanduser()
        if not selected.exists():
            return status_result(
                runtime="codex",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"Trace file does not exist: {selected}"],
            )
        parsed = parse_codex_file(selected, workspace_norm)
        parsed_cwd = parsed.get("session", {}).get("cwd")
        if parsed_cwd and normalize_path(Path(parsed_cwd)) != workspace_norm:
            parsed["warnings"].append(
                "Explicit trace file cwd does not match workspace; using explicit trace file anyway."
            )
        return parsed

    candidates = discover_candidates()
    if not candidates:
        return status_result(
            runtime="codex",
            status="not_found",
            workspace=workspace_norm,
            warnings=["No Codex rollout JSONL files found under ~/.codex/sessions."],
        )

    if session_id:
        exact = [c for c in candidates if c.get("session_id") == session_id]
        if not exact:
            exact = [c for c in candidates if session_id in c["path"].name]
        if len(exact) == 1:
            return parse_codex_file(exact[0]["path"], workspace_norm)
        if len(exact) > 1:
            return ambiguous_result("codex", workspace_norm, exact)
        return status_result(
            runtime="codex",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No Codex session matched session id: {session_id}"],
            candidates=public_candidates(candidates),
        )

    exact_workspace = [c for c in candidates if c.get("cwd_norm") == workspace_norm]
    if exact_workspace:
        selected = newest_candidate(exact_workspace)
        return parse_codex_file(selected["path"], workspace_norm)

    approximate = [c for c in candidates if paths_related(c.get("cwd_norm"), workspace_norm)]
    if len(approximate) == 1:
        parsed = parse_codex_file(approximate[0]["path"], workspace_norm)
        parsed["warnings"].append(
            "Selected an approximate cwd match; verify trace_source before using as high-confidence evidence."
        )
        parsed["collection_confidence"] = "medium"
        return parsed
    if len(approximate) > 1:
        return ambiguous_result("codex", workspace_norm, approximate)

    return status_result(
        runtime="codex",
        status="not_found",
        workspace=workspace_norm,
        warnings=["No Codex session cwd matched the requested workspace."],
        candidates=public_candidates(candidates),
    )


def discover_candidates() -> list[dict[str, Any]]:
    root = Path.home() / ".codex" / "sessions"
    if not root.exists():
        return []

    candidates: list[dict[str, Any]] = []
    for path in root.glob("**/rollout-*.jsonl"):
        meta, warnings = read_session_meta(path)
        candidates.append(
            {
                "path": path,
                "source_path": str(path),
                "mtime": path.stat().st_mtime,
                "session_id": meta.get("id"),
                "cwd": meta.get("cwd"),
                "cwd_norm": normalize_path(Path(meta["cwd"])) if meta.get("cwd") else None,
                "timestamp": meta.get("timestamp"),
                "warnings": warnings,
            }
        )
    candidates.sort(key=lambda c: c["mtime"], reverse=True)
    return candidates


def read_session_meta(path: Path) -> tuple[dict[str, Any], list[str]]:
    warnings: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                record = json.loads(line)
                if record.get("type") == "session_meta":
                    payload = record.get("payload") or {}
                    return {
                        "id": payload.get("id"),
                        "timestamp": payload.get("timestamp") or record.get("timestamp"),
                        "cwd": payload.get("cwd"),
                    }, warnings
    except Exception as exc:  # pragma: no cover - defensive for corrupt logs.
        warnings.append(f"Could not read session metadata from {path}: {exc}")
    return {}, warnings


def parse_codex_file(path: Path, workspace_norm: str) -> dict[str, Any]:
    records, parse_warnings = read_jsonl(path)
    session = extract_session(records)
    session_id = session.get("id") or "unknown"
    source_path = str(path)

    message_events: list[dict[str, Any]] = []
    task_events: list[dict[str, Any]] = []
    function_calls: dict[str, dict[str, Any]] = {}
    function_outputs: dict[str, dict[str, Any]] = {}
    custom_calls: dict[str, dict[str, Any]] = {}
    custom_outputs: dict[str, dict[str, Any]] = {}
    patch_ends: dict[str, dict[str, Any]] = {}
    warnings = list(parse_warnings)

    for item in records:
        record = item["record"]
        payload = record.get("payload") or {}
        event_type = payload.get("type") or record.get("type")
        line_no = item["line_no"]
        timestamp = record.get("timestamp") or payload.get("timestamp")

        if event_type in {
            "reasoning",
            "turn_context",
            "context_compacted",
            "compacted",
            "token_count",
            "session_meta",
        }:
            continue

        if event_type == "user_message":
            message_events.append(
                trace_event(
                    runtime="codex",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type="user_message",
                    tool_name=None,
                    status="observed",
                    input_summary=summarize_text(payload.get("message") or payload.get("text") or ""),
                    output_summary="",
                    evidence_ref=line_ref(session_id, line_no),
                )
            )
        elif event_type == "agent_message":
            message_events.append(
                trace_event(
                    runtime="codex",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type="agent_message",
                    tool_name=None,
                    status="observed",
                    input_summary="",
                    output_summary=summarize_text(payload.get("message") or payload.get("text") or ""),
                    evidence_ref=line_ref(session_id, line_no),
                )
            )
        elif event_type == "function_call":
            call_id = payload.get("call_id") or f"line-{line_no}"
            function_calls[call_id] = {
                "timestamp": timestamp,
                "line_no": line_no,
                "name": payload.get("name") or "unknown",
                "arguments": parse_json_field(payload.get("arguments")),
            }
        elif event_type == "function_call_output":
            call_id = payload.get("call_id") or f"line-{line_no}"
            function_outputs[call_id] = {
                "timestamp": timestamp,
                "line_no": line_no,
                "output": payload.get("output") or "",
            }
        elif event_type == "custom_tool_call":
            call_id = payload.get("call_id") or f"line-{line_no}"
            custom_calls[call_id] = {
                "timestamp": timestamp,
                "line_no": line_no,
                "name": payload.get("name") or "custom_tool",
                "input": payload.get("input"),
                "status": payload.get("status"),
            }
        elif event_type == "custom_tool_call_output":
            call_id = payload.get("call_id") or f"line-{line_no}"
            custom_outputs[call_id] = {
                "timestamp": timestamp,
                "line_no": line_no,
                "output": payload.get("output") or "",
            }
        elif event_type == "patch_apply_end":
            call_id = payload.get("call_id") or f"line-{line_no}"
            patch_ends[call_id] = {
                "timestamp": timestamp,
                "line_no": line_no,
                "success": payload.get("success"),
                "stdout": payload.get("stdout") or "",
                "stderr": payload.get("stderr") or "",
                "changes": payload.get("changes"),
                "status": payload.get("status"),
            }
        elif event_type == "task_complete":
            task_events.append(
                trace_event(
                    runtime="codex",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type="task_complete",
                    tool_name=None,
                    status="observed",
                    input_summary="",
                    output_summary=summarize_text(
                        payload.get("message") or payload.get("status") or "task_complete"
                    ),
                    evidence_ref=line_ref(session_id, line_no),
                )
            )

    events: list[dict[str, Any]] = []
    events.extend(message_events)
    events.extend(build_function_events(session_id, source_path, function_calls, function_outputs))
    events.extend(build_custom_events(session_id, source_path, custom_calls, custom_outputs, patch_ends))
    events.extend(build_patch_events(session_id, source_path, custom_calls, patch_ends))
    events.extend(task_events)
    events.sort(key=lambda e: (e.get("timestamp") or "", e.get("evidence_ref") or ""))
    assign_trace_refs(events)

    if session.get("cwd_norm") and session["cwd_norm"] != workspace_norm:
        warnings.append("Session cwd does not match requested workspace.")

    return {
        "runtime": "codex",
        "status": "ok",
        "session_id": session_id,
        "source_path": source_path,
        "workspace": workspace_norm,
        "collection_confidence": "high" if session.get("cwd_norm") == workspace_norm else "medium",
        "session": {
            "id": session.get("id"),
            "timestamp": session.get("timestamp"),
            "cwd": session.get("cwd"),
        },
        "events": events,
        "warnings": warnings,
    }


def build_function_events(
    session_id: str,
    source_path: str,
    calls: dict[str, dict[str, Any]],
    outputs: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    events = []
    for call_id, call in calls.items():
        output = outputs.get(call_id)
        output_text = output.get("output", "") if output else ""
        status = infer_output_status(output_text) if output else "pending"
        event_type = classify_function_event(call.get("name"), call.get("arguments"))
        events.append(
            trace_event(
                runtime="codex",
                session_id=session_id,
                source_path=source_path,
                timestamp=call.get("timestamp"),
                event_type=event_type,
                tool_name=call.get("name"),
                status=status,
                input_summary=summarize_value(call.get("arguments")),
                output_summary=summarize_tool_output(call.get("name"), call.get("arguments"), output_text),
                evidence_ref=call_ref(session_id, call_id),
                warnings=[] if output else ["tool output not observed"],
            )
        )
    for call_id, output in outputs.items():
        if call_id in calls:
            continue
        output_text = output.get("output") or ""
        events.append(
            trace_event(
                runtime="codex",
                session_id=session_id,
                source_path=source_path,
                timestamp=output.get("timestamp"),
                event_type="tool_output",
                tool_name="unknown",
                status=infer_output_status(output_text),
                input_summary="",
                output_summary=summarize_tool_output("unknown", None, output_text),
                evidence_ref=call_ref(session_id, call_id),
                warnings=["tool input not observed"],
            )
        )
    return events


def build_custom_events(
    session_id: str,
    source_path: str,
    calls: dict[str, dict[str, Any]],
    outputs: dict[str, dict[str, Any]],
    patch_ends: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    events = []
    for call_id, call in calls.items():
        if call_id in patch_ends:
            continue
        output = outputs.get(call_id)
        output_text = output.get("output", "") if output else ""
        status = call.get("status") or ("observed" if output else "pending")
        events.append(
            trace_event(
                runtime="codex",
                session_id=session_id,
                source_path=source_path,
                timestamp=call.get("timestamp"),
                event_type="tool_call",
                tool_name=call.get("name") or "custom_tool",
                status=status,
                input_summary=summarize_value(call.get("input")),
                output_summary=summarize_tool_output(call.get("name"), call.get("input"), output_text),
                evidence_ref=call_ref(session_id, call_id),
                warnings=[] if output else ["custom tool output not observed"],
            )
        )
    return events


def build_patch_events(
    session_id: str,
    source_path: str,
    custom_calls: dict[str, dict[str, Any]],
    patch_ends: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    events = []
    for call_id, patch in patch_ends.items():
        custom_call = custom_calls.get(call_id, {})
        success = patch.get("success")
        if success is True:
            status = "success"
        elif success is False:
            status = "failure"
        else:
            status = patch.get("status") or "observed"
        events.append(
            trace_event(
                runtime="codex",
                session_id=session_id,
                source_path=source_path,
                timestamp=patch.get("timestamp"),
                event_type="patch",
                tool_name=custom_call.get("name") or "apply_patch",
                status=status,
                input_summary=summarize_value(custom_call.get("input")),
                output_summary=summarize_patch(patch),
                evidence_ref=call_ref(session_id, call_id),
            )
        )
    return events


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    warnings: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    records.append({"line_no": line_no, "record": json.loads(line)})
                except json.JSONDecodeError as exc:
                    warnings.append(f"Skipped invalid JSON line {line_no}: {exc}")
    except Exception as exc:
        warnings.append(f"Could not read trace file {path}: {exc}")
    return records, warnings


def extract_session(records: list[dict[str, Any]]) -> dict[str, Any]:
    for item in records:
        record = item["record"]
        if record.get("type") == "session_meta":
            payload = record.get("payload") or {}
            cwd = payload.get("cwd")
            return {
                "id": payload.get("id"),
                "timestamp": payload.get("timestamp") or record.get("timestamp"),
                "cwd": cwd,
                "cwd_norm": normalize_path(Path(cwd)) if cwd else None,
            }
    return {"id": None, "timestamp": None, "cwd": None, "cwd_norm": None}


def newest_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return sorted(candidates, key=lambda c: c["mtime"], reverse=True)[0]


def parse_json_field(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def summarize_patch(patch: dict[str, Any]) -> str:
    parts = []
    changes = patch.get("changes")
    if changes:
        parts.append("changes=" + summarize_value(changes))
    if patch.get("stdout"):
        parts.append("stdout=" + summarize_text(patch.get("stdout")))
    if patch.get("stderr"):
        parts.append("stderr=" + summarize_text(patch.get("stderr")))
    if not parts:
        parts.append("patch_apply_end observed")
    return " | ".join(parts)


def summarize_tool_output(tool_name: str | None, arguments: Any, output_text: str) -> str:
    if tool_name == "shell_command":
        return summarize_shell_output(arguments, output_text)
    return summarize_text(output_text)


def summarize_shell_output(arguments: Any, output_text: str) -> str:
    text = normalize_text_encoding(output_text or "").replace("\r\n", "\n")
    header, body = split_shell_output(text)
    parts = shell_header_parts(header)
    command = shell_command_text(arguments)

    if not body.strip():
        return "; ".join(parts) if parts else summarize_text(text)

    body_summary = summarize_text(body)
    if command_prints_file_content(command, body):
        parts.append("stdout omitted: command printed file content; input_summary keeps command/path")
    elif looks_encoding_damaged(body_summary):
        parts.append("stdout omitted: output appears encoding-damaged; use evidence_ref for raw trace")
    else:
        parts.append("output: " + body_summary)

    return "; ".join(parts) if parts else summarize_text(text)


def split_shell_output(output_text: str) -> tuple[str, str]:
    marker = "\nOutput:\n"
    if marker in output_text:
        header, body = output_text.split(marker, 1)
        return header.strip(), body.strip()
    return output_text.strip(), ""


def shell_header_parts(header: str) -> list[str]:
    parts: list[str] = []
    exit_match = re.search(r"Exit code:\s*(-?\d+)", header)
    if exit_match:
        parts.append(f"exit_code={exit_match.group(1)}")
    wall_match = re.search(r"Wall time:\s*([^\n]+)", header)
    if wall_match:
        parts.append(f"wall_time={wall_match.group(1).strip()}")
    total_match = re.search(r"Total output lines:\s*(\d+)", header)
    if total_match:
        parts.append(f"total_output_lines={total_match.group(1)}")
    return parts


def shell_command_text(arguments: Any) -> str:
    if isinstance(arguments, dict):
        return str(arguments.get("command") or "")
    if isinstance(arguments, str):
        try:
            parsed = json.loads(arguments)
            if isinstance(parsed, dict):
                return str(parsed.get("command") or arguments)
        except json.JSONDecodeError:
            pass
        return arguments
    return ""


def command_prints_file_content(command: str, body: str) -> bool:
    if not FILE_DUMP_COMMAND_RE.search(command or ""):
        return False
    if ".md" in command.lower() or ".txt" in command.lower() or ".json" in command.lower():
        return True
    sample = body[:500]
    return sample.startswith("---") or "\n#" in sample or "\n##" in sample


def infer_output_status(output: str) -> str:
    match = re.search(r"Exit code:\s*(-?\d+)", output or "")
    if match:
        return "success" if match.group(1) == "0" else "failure"
    lowered = (output or "").lower()
    if "error" in lowered or "failed" in lowered:
        return "failure"
    return "observed"


def classify_function_event(name: str | None, arguments: Any) -> str:
    if name != "shell_command":
        return "tool_call"
    command = ""
    if isinstance(arguments, dict):
        command = str(arguments.get("command") or "")
    elif isinstance(arguments, str):
        command = arguments
    return "verification" if VALIDATION_COMMAND_RE.search(command) else "tool_call"


def line_ref(session_id: str, line_no: int) -> str:
    return f"session:{session_id}#line:{line_no}"


def call_ref(session_id: str, call_id: str) -> str:
    return f"session:{session_id}#call:{call_id}"
