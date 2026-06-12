#!/usr/bin/env python3
"""Trae trace adapter.

Supported sources:
- Trae CLI sessions under %LOCALAPPDATA%/trae-cli/sessions/<session_id>/.
- Trae CN renderer logs under %APPDATA%/Trae CN/logs/**/renderer.log.
"""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from adapters.base import ambiguous_result, public_candidates, status_result
from collector_core import (
    assign_trace_refs,
    normalize_path,
    paths_related,
    summarize_text,
    summarize_value,
    trace_event,
)


VALIDATION_COMMAND_RE = re.compile(
    r"(?i)\b(skill-lint|py_compile|pytest|unittest|cargo\s+test|go\s+test|npm\s+(?:run\s+)?test|pnpm\s+test|yarn\s+test|lint|build|cjpm\s+build|validate|validator)\b"
)
LOG_PREFIX_RE = re.compile(r"^(?P<timestamp>\S+)\s+\[(?P<level>[^\]]+)\]\s+(?P<body>.*)$")
SEND_CHAT_RE = re.compile(r"\[sendChatMessage\]\s+sessionId=(?P<session>[A-Za-z0-9_-]+)")
TOOL_EVENT_RE = re.compile(r"event:\s*(?P<event>[A-Za-z0-9_]+)\s*;\s*params:\s*(?P<json>\{.*\}|undefined)\s*$")
RUN_COMMAND_RE = re.compile(
    r"\[tooling\]\s+(?P<call>[0-9a-fA-F-]+)\s+runCommandInTerminal\s+blocking=(?P<blocking>\w+)\s+(?P<json>\[.*\])\s*$"
)
COMMAND_RESULT_RE = re.compile(
    r"\[tooling\]\s+(?P<call>[0-9a-fA-F-]+)\s+commandId:(?P<command_id>[0-9a-fA-F-]+)\s+result:\s+exitCode=(?P<exit>[-\w]+)\s+commandResult=\s+(?P<json>\[.*\])\s*$"
)
TERMINAL_TRACE_RE = re.compile(r"\[ToolingTerminalTrace\]toolcall_run_command_tracing\s+(?P<json>\{.*\})\s*$")
PARSE_INPUTS_RE = re.compile(r"\[parseInputs\]\s+parsing completed,\s+inputString:\s+(?P<text>.*)$")
SESSION_ID_RE = re.compile(
    r'(?:"(?:chatSessionId|session_id|sessionId)"\s*:\s*"(?P<json>[A-Za-z0-9_-]+)"|sessionId=(?P<plain>[A-Za-z0-9_-]+))'
)
MAX_RENDERER_EVENTS = 250
MAX_DISCOVERY_BYTES = 8_000_000


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    workspace_norm = normalize_path(workspace)

    if trace_file:
        selected = trace_file.expanduser().resolve(strict=False)
        if not selected.exists():
            return status_result(
                runtime="trae",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"Trace file does not exist: {selected}"],
            )
        return parse_explicit_source(selected, workspace_norm, session_id)

    candidates = discover_candidates(workspace_norm)
    if not candidates:
        return status_result(
            runtime="trae",
            status="not_found",
            workspace=workspace_norm,
            warnings=[
                "No Trae trace matched the workspace. Checked Trae CLI sessions and Trae CN renderer logs."
            ],
        )

    if session_id:
        exact = [
            c
            for c in candidates
            if c.get("session_id") == session_id or session_id in str(c.get("source_path") or c.get("path"))
        ]
        if len(exact) == 1:
            return parse_candidate(exact[0], workspace_norm, session_id)
        if len(exact) > 1:
            return ambiguous_result("trae", workspace_norm, exact)
        return status_result(
            runtime="trae",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No Trae trace matched session id: {session_id}"],
            candidates=public_candidates(candidates),
        )

    exact_workspace = [c for c in candidates if c.get("cwd_norm") == workspace_norm]
    if exact_workspace:
        return parse_candidate(newest_candidate(exact_workspace), workspace_norm, None)

    approximate = [c for c in candidates if paths_related(c.get("cwd_norm"), workspace_norm)]
    if len(approximate) == 1:
        parsed = parse_candidate(approximate[0], workspace_norm, None)
        parsed["collection_confidence"] = "medium"
        parsed["warnings"].append(
            "Selected an approximate Trae workspace match; verify trace_source before saving."
        )
        return parsed
    if len(approximate) > 1:
        return ambiguous_result("trae", workspace_norm, approximate)

    return status_result(
        runtime="trae",
        status="not_found",
        workspace=workspace_norm,
        warnings=["Trae traces were found, but none matched the requested workspace."],
        candidates=public_candidates(candidates),
    )


def parse_explicit_source(
    source: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    if source.is_dir():
        if (source / "events.jsonl").exists() or (source / "traces.jsonl").exists():
            return parse_cli_session(source, workspace_norm, session_id)
        renderer_logs = sorted(source.glob("**/renderer.log"), key=lambda p: p.stat().st_mtime, reverse=True)
        if len(renderer_logs) == 1:
            return parse_renderer_log(renderer_logs[0], workspace_norm, session_id)
        if len(renderer_logs) > 1:
            return ambiguous_result(
                "trae",
                workspace_norm,
                [
                    {
                        "path": p,
                        "source_path": str(p),
                        "mtime": p.stat().st_mtime,
                        "session_id": session_id,
                        "cwd": None,
                        "timestamp": None,
                    }
                    for p in renderer_logs
                ],
            )
        return status_result(
            runtime="trae",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Directory does not contain a supported Trae trace source: {source}"],
        )

    lower_name = source.name.lower()
    if lower_name in {"events.jsonl", "traces.jsonl", "session.json", "session.log"}:
        return parse_cli_session(source.parent, workspace_norm, session_id)
    if lower_name == "renderer.log":
        return parse_renderer_log(source, workspace_norm, session_id)

    sniffed = sniff_jsonl_kind(source)
    if sniffed in {"cli_events", "cli_traces"}:
        return parse_cli_files(
            events_path=source if sniffed == "cli_events" else None,
            traces_path=source if sniffed == "cli_traces" else None,
            session_path=source.parent / "session.json",
            workspace_norm=workspace_norm,
            session_id=session_id,
        )
    return parse_renderer_log(source, workspace_norm, session_id)


def parse_candidate(
    candidate: dict[str, Any], workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    kind = candidate.get("kind")
    path = Path(candidate.get("path") or candidate.get("source_path") or "")
    selected_session = session_id or candidate.get("session_id")
    if kind == "cli":
        return parse_cli_session(path if path.is_dir() else path.parent, workspace_norm, selected_session)
    if kind == "renderer":
        return parse_renderer_log(path, workspace_norm, selected_session)
    return parse_explicit_source(path, workspace_norm, selected_session)


def discover_candidates(workspace_norm: str) -> list[dict[str, Any]]:
    candidates = []
    candidates.extend(discover_cli_candidates())
    candidates.extend(discover_renderer_candidates(workspace_norm))
    candidates.sort(key=lambda c: c.get("mtime", 0), reverse=True)
    return candidates


def discover_cli_candidates() -> list[dict[str, Any]]:
    root = Path(os.environ.get("LOCALAPPDATA", "")) / "trae-cli" / "sessions"
    if not root.exists():
        return []

    candidates: list[dict[str, Any]] = []
    for session_dir in root.iterdir():
        if not session_dir.is_dir():
            continue
        events_path = session_dir / "events.jsonl"
        traces_path = session_dir / "traces.jsonl"
        session_path = session_dir / "session.json"
        if not events_path.exists() and not traces_path.exists():
            continue
        session = read_cli_session_meta(session_path)
        source_path = events_path if events_path.exists() else traces_path
        cwd = session.get("cwd")
        candidates.append(
            {
                "kind": "cli",
                "path": session_dir,
                "source_path": str(source_path),
                "mtime": max_existing_mtime([events_path, traces_path, session_path]),
                "session_id": session.get("id") or session_dir.name,
                "cwd": cwd,
                "cwd_norm": normalize_path(Path(cwd)) if cwd else None,
                "timestamp": session.get("updated_at") or session.get("created_at"),
            }
        )
    return candidates


def discover_renderer_candidates(workspace_norm: str) -> list[dict[str, Any]]:
    root = Path(os.environ.get("APPDATA", "")) / "Trae CN" / "logs"
    if not root.exists():
        return []

    candidates: list[dict[str, Any]] = []
    for path in root.glob("**/renderer.log"):
        if path.stat().st_size <= 0 or path.stat().st_size > MAX_DISCOVERY_BYTES:
            continue
        match = scan_renderer_workspace_match(path, workspace_norm)
        if not match:
            continue
        candidates.append(
            {
                "kind": "renderer",
                "path": path,
                "source_path": str(path),
                "mtime": path.stat().st_mtime,
                "session_id": match.get("session_id"),
                "cwd": match.get("cwd"),
                "cwd_norm": workspace_norm,
                "timestamp": match.get("timestamp"),
            }
        )
    return candidates


def scan_renderer_workspace_match(path: Path, workspace_norm: str) -> dict[str, Any] | None:
    needles = workspace_needles(workspace_norm)
    session_ids: Counter[str] = Counter()
    last_timestamp = None
    matched = False
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                folded = line.casefold()
                if not any(needle in folded for needle in needles):
                    continue
                matched = True
                timestamp, _level, _body = split_log_line(line)
                last_timestamp = timestamp or last_timestamp
                for found in SESSION_ID_RE.finditer(line):
                    session = found.group("json") or found.group("plain")
                    if session:
                        session_ids[session] += 1
    except OSError:
        return None
    if not matched:
        return None
    session_id = session_ids.most_common(1)[0][0] if session_ids else None
    return {"session_id": session_id, "cwd": workspace_norm, "timestamp": last_timestamp}


def parse_cli_session(
    session_dir: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    return parse_cli_files(
        events_path=session_dir / "events.jsonl" if (session_dir / "events.jsonl").exists() else None,
        traces_path=session_dir / "traces.jsonl" if (session_dir / "traces.jsonl").exists() else None,
        session_path=session_dir / "session.json",
        workspace_norm=workspace_norm,
        session_id=session_id,
    )


def parse_cli_files(
    *,
    events_path: Path | None,
    traces_path: Path | None,
    session_path: Path,
    workspace_norm: str,
    session_id: str | None,
) -> dict[str, Any]:
    session = read_cli_session_meta(session_path)
    actual_session_id = session_id or session.get("id") or session_path.parent.name
    source_path = str(events_path or traces_path or session_path)
    warnings: list[str] = []

    events: list[dict[str, Any]] = []
    if events_path and events_path.exists():
        parsed_events, parse_warnings = parse_cli_events_file(events_path, actual_session_id)
        events.extend(parsed_events)
        warnings.extend(parse_warnings)
    if traces_path and traces_path.exists():
        parsed_traces, parse_warnings = parse_cli_traces_file(
            traces_path,
            actual_session_id,
            skip_user_prompt=any(e.get("event_type") == "user_message" for e in events),
        )
        events.extend(parsed_traces)
        warnings.extend(parse_warnings)

    events = dedupe_events(events)
    events.sort(key=event_sort_key)
    assign_trace_refs(events)

    cwd = session.get("cwd")
    cwd_norm = normalize_path(Path(cwd)) if cwd else None
    if cwd_norm and cwd_norm != workspace_norm:
        warnings.append("Trae CLI session cwd does not match requested workspace.")

    return {
        "runtime": "trae",
        "status": "ok",
        "session_id": actual_session_id,
        "source_path": source_path,
        "workspace": workspace_norm,
        "collection_confidence": "high" if cwd_norm == workspace_norm and events_path else "medium",
        "session": {
            "id": actual_session_id,
            "timestamp": session.get("updated_at") or session.get("created_at"),
            "cwd": cwd,
        },
        "events": events,
        "warnings": warnings,
    }


def parse_cli_events_file(path: Path, session_id: str) -> tuple[list[dict[str, Any]], list[str]]:
    records, warnings = read_jsonl(path)
    source_path = str(path)
    events: list[dict[str, Any]] = []

    for item in records:
        record = item["record"]
        line_no = item["line_no"]
        timestamp = record.get("created_at") or record.get("updated_at")

        message = nested_get(record, ("message", "message"))
        if isinstance(message, dict):
            event = cli_message_event(message, session_id, source_path, timestamp, line_no)
            if event:
                events.append(event)
            continue

        tool_call = first_dict(record, ("tool_call", "toolCall", "function_call"))
        if tool_call:
            events.append(cli_tool_call_event(tool_call, session_id, source_path, timestamp, line_no))
            continue

        tool_result = first_dict(record, ("tool_result", "toolResult", "function_call_output"))
        if tool_result:
            events.append(cli_tool_result_event(tool_result, session_id, source_path, timestamp, line_no))
            continue

        agent_end = record.get("agent_end")
        if isinstance(agent_end, dict):
            error = agent_end.get("error_message") or agent_end.get("error")
            events.append(
                trace_event(
                    runtime="trae",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type="task_complete",
                    tool_name=None,
                    status="failure" if error else "observed",
                    input_summary="",
                    output_summary=summarize_text(error or agent_end.get("message") or "agent_end"),
                    evidence_ref=line_ref(session_id, line_no),
                )
            )

    return events, warnings


def parse_cli_traces_file(
    path: Path, session_id: str, *, skip_user_prompt: bool
) -> tuple[list[dict[str, Any]], list[str]]:
    records, warnings = read_jsonl(path)
    source_path = str(path)
    events: list[dict[str, Any]] = []

    for item in records:
        span = item["record"]
        line_no = item["line_no"]
        tags = tags_to_dict(span.get("tags"))
        category = str(tags.get("span.category") or span.get("operationName") or "")
        timestamp = timestamp_from_span(span)
        evidence = span_ref(session_id, span, line_no)

        if category == "user.prompt":
            if skip_user_prompt:
                continue
            prompt = tags.get("prompt.summary") or first_log_field(span, "telemetry.prompt")
            if prompt:
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session_id,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="user_message",
                        tool_name=None,
                        status="observed",
                        input_summary=summarize_text(prompt),
                        output_summary="",
                        evidence_ref=evidence,
                    )
                )
        elif category in {"query.do", "agent.call"}:
            error = tags.get("error") or first_log_field(span, "exception.message") or first_log_field(
                span, "telemetry.error.message"
            )
            if error:
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session_id,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="task_complete",
                        tool_name=None,
                        status="failure",
                        input_summary=summarize_text(tags.get("prompt.summary") or ""),
                        output_summary=summarize_text(error),
                        evidence_ref=evidence,
                    )
                )
        elif category == "cmd.root":
            command_name = first_log_field(span, "telemetry.command.name")
            if command_name:
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session_id,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="tool_call",
                        tool_name="trae-cli",
                        status="observed",
                        input_summary=summarize_text(command_name),
                        output_summary="command_request observed",
                        evidence_ref=evidence,
                    )
                )

    return events, warnings


def parse_renderer_log(
    path: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    source_path = str(path)
    warnings: list[str] = ["Trae renderer log parsing is semi-structured; verify key evidence before saving."]
    events: list[dict[str, Any]] = []
    pending_commands: dict[str, dict[str, Any]] = {}
    command_events_by_tool_id: dict[str, dict[str, Any]] = {}
    shown_tools: set[str] = set()
    workspace_seen = False

    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line_no, raw_line in enumerate(handle, start=1):
                timestamp, level, body = split_log_line(raw_line)
                if workspace_matches(raw_line, workspace_norm):
                    workspace_seen = True
                if session_id and not renderer_line_matches_session(raw_line, session_id):
                    continue

                parsed = parse_renderer_line(
                    body=body,
                    timestamp=timestamp,
                    level=level,
                    line_no=line_no,
                    source_path=source_path,
                    default_session_id=session_id,
                    pending_commands=pending_commands,
                    command_events_by_tool_id=command_events_by_tool_id,
                    shown_tools=shown_tools,
                )
                events.extend(parsed)
                if len(events) >= MAX_RENDERER_EVENTS:
                    warnings.append(f"Stopped after {MAX_RENDERER_EVENTS} Trae renderer events.")
                    break
    except OSError as exc:
        return status_result(
            runtime="trae",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Could not read Trae renderer log {path}: {exc}"],
        )

    events = dedupe_events(events)
    events.sort(key=event_sort_key)
    assign_trace_refs(events)
    confidence = "medium" if workspace_seen else "low"
    if not workspace_seen:
        warnings.append("Renderer log did not contain the requested workspace path.")

    return {
        "runtime": "trae",
        "status": "ok",
        "session_id": session_id or infer_session_id(events) or "trae-renderer",
        "source_path": source_path,
        "workspace": workspace_norm,
        "collection_confidence": confidence,
        "events": events,
        "warnings": warnings,
    }


def parse_renderer_line(
    *,
    body: str,
    timestamp: str | None,
    level: str,
    line_no: int,
    source_path: str,
    default_session_id: str | None,
    pending_commands: dict[str, dict[str, Any]],
    command_events_by_tool_id: dict[str, dict[str, Any]],
    shown_tools: set[str],
) -> list[dict[str, Any]]:
    session = default_session_id or first_session_id(body) or "trae-renderer"
    evidence = file_line_ref(source_path, line_no)
    events: list[dict[str, Any]] = []

    parse_inputs = PARSE_INPUTS_RE.search(body)
    if parse_inputs:
        if default_session_id and default_session_id not in body:
            return events
        text = parse_logged_string(parse_inputs.group("text"))
        if text:
            events.append(
                trace_event(
                    runtime="trae",
                    session_id=session,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type="user_message",
                    tool_name=None,
                    status="observed",
                    input_summary=summarize_text(text),
                    output_summary="",
                    evidence_ref=evidence,
                )
            )
        return events

    send_chat = SEND_CHAT_RE.search(body)
    if send_chat:
        session = send_chat.group("session")
        events.append(
            trace_event(
                runtime="trae",
                session_id=session,
                source_path=source_path,
                timestamp=timestamp,
                event_type="user_message",
                tool_name=None,
                status="observed",
                input_summary=f"Trae chat request submitted for session {session}",
                output_summary="",
                evidence_ref=evidence,
            )
        )
        return events

    tool_event = TOOL_EVENT_RE.search(body)
    if tool_event:
        event_name = tool_event.group("event")
        payload = loads_json(tool_event.group("json"))
        if isinstance(payload, dict):
            if event_name == "code_comp_trigger":
                session = str(payload.get("session_id") or default_session_id or session)
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="user_message",
                        tool_name=None,
                        status="observed",
                        input_summary=summarize_value(public_chat_trigger_payload(payload)),
                        output_summary="",
                        evidence_ref=evidence,
                    )
                )
                return events
            tool_id = str(payload.get("tool_id") or payload.get("block_id") or "")
            tool_type = str(payload.get("tool_type") or payload.get("block_type") or event_name)
            session = str(payload.get("session_id") or default_session_id or session)
            if event_name in {"tool_call_show", "file_tool_show", "run_script_show"} and tool_id not in shown_tools:
                shown_tools.add(tool_id)
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="patch" if is_patch_tool(tool_type) else "tool_call",
                        tool_name=tool_type,
                        status="pending",
                        input_summary=summarize_value(public_tool_payload(payload)),
                        output_summary=f"{event_name} observed",
                        evidence_ref=evidence,
                    )
                )
            elif event_name.endswith("_success") and tool_id:
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type="patch" if is_patch_tool(tool_type) else "tool_output",
                        tool_name=tool_type,
                        status="success",
                        input_summary=summarize_value(public_tool_payload(payload)),
                        output_summary=f"{event_name} observed",
                        evidence_ref=evidence,
                    )
                )
        return events

    run_command = RUN_COMMAND_RE.search(body)
    if run_command:
        payload = loads_json(run_command.group("json"))
        if isinstance(payload, list) and payload:
            command_payload = payload[0]
            if isinstance(command_payload, dict):
                call_id = str(command_payload.get("callId") or run_command.group("call"))
                tool_call_id = str(command_payload.get("toolCallId") or call_id)
                command = str(command_payload.get("command") or "")
                session = str(command_payload.get("chatSessionId") or default_session_id or session)
                event = trace_event(
                    runtime="trae",
                    session_id=session,
                    source_path=source_path,
                    timestamp=timestamp,
                    event_type=classify_command_event(command),
                    tool_name="run_command",
                    status="pending",
                    input_summary=summarize_value(public_command_payload(command_payload)),
                    output_summary="runCommandInTerminal invoked",
                    evidence_ref=evidence,
                    warnings=["command result not observed"],
                )
                pending_commands[call_id] = event
                command_events_by_tool_id[tool_call_id] = event
                events.append(event)
        return events

    result = COMMAND_RESULT_RE.search(body)
    if result:
        payload = loads_json(result.group("json"))
        if isinstance(payload, list) and payload:
            result_payload = payload[0]
            if isinstance(result_payload, dict):
                call_id = result.group("call")
                tool_call_id = str(result_payload.get("serverCallId") or "")
                event = pending_commands.get(call_id) or command_events_by_tool_id.get(tool_call_id)
                command = str(result_payload.get("command") or "")
                exit_code = result_payload.get("exitCode", result.group("exit"))
                status = "success" if str(exit_code) == "0" else "failure"
                output = summarize_command_result(result_payload)
                if event:
                    event["status"] = status
                    event["output_summary"] = output
                    event["evidence_ref"] = append_evidence_ref(event.get("evidence_ref"), evidence)
                    event["warnings"] = []
                else:
                    session = str(result_payload.get("chatSessionId") or default_session_id or session)
                    events.append(
                        trace_event(
                            runtime="trae",
                            session_id=session,
                            source_path=source_path,
                            timestamp=timestamp,
                            event_type=classify_command_event(command),
                            tool_name="run_command",
                            status=status,
                            input_summary=summarize_value(
                                {"command": command, "toolCallId": tool_call_id or None}
                            ),
                            output_summary=output,
                            evidence_ref=evidence,
                        )
                    )
        return events

    terminal_trace = TERMINAL_TRACE_RE.search(body)
    if terminal_trace:
        payload = loads_json(terminal_trace.group("json"))
        if isinstance(payload, dict):
            categories = payload.get("categories") if isinstance(payload.get("categories"), dict) else {}
            tool_call_id = str(categories.get("tool_call_key") or "")
            event = command_events_by_tool_id.get(tool_call_id)
            exit_code = categories.get("exitCode")
            if event and event.get("status") == "pending":
                event["status"] = terminal_trace_status(categories)
                event["output_summary"] = summarize_value(
                    {
                        "exitCode": exit_code,
                        "last_stage": categories.get("last_stage"),
                        "duration_ms": nested_get(payload, ("metrics", "total_duration")),
                    }
                )
                event["evidence_ref"] = append_evidence_ref(event.get("evidence_ref"), evidence)
                if event["status"] != "pending":
                    event["warnings"] = []
            elif not event:
                command = str(categories.get("command") or "")
                session = str(categories.get("chat_session_id") or default_session_id or session)
                events.append(
                    trace_event(
                        runtime="trae",
                        session_id=session,
                        source_path=source_path,
                        timestamp=timestamp,
                        event_type=classify_command_event(command),
                        tool_name="run_command",
                        status=terminal_trace_status(categories),
                        input_summary=summarize_value({"command": command, "toolCallId": tool_call_id or None}),
                        output_summary=summarize_value(
                            {
                                "exitCode": exit_code,
                                "last_stage": categories.get("last_stage"),
                                "duration_ms": nested_get(payload, ("metrics", "total_duration")),
                            }
                        ),
                        evidence_ref=evidence,
                    )
                )
        return events

    return events


def cli_message_event(
    message: dict[str, Any], session_id: str, source_path: str, timestamp: str | None, line_no: int
) -> dict[str, Any] | None:
    role = str(message.get("role") or "").lower()
    content = message.get("content")
    extra = message.get("extra") if isinstance(message.get("extra"), dict) else {}
    text = content_to_text(content)
    if is_hidden_or_context_message(text, extra):
        return None
    if role == "user":
        return trace_event(
            runtime="trae",
            session_id=session_id,
            source_path=source_path,
            timestamp=timestamp,
            event_type="user_message",
            tool_name=None,
            status="observed",
            input_summary=summarize_text(text),
            output_summary="",
            evidence_ref=line_ref(session_id, line_no),
        )
    if role in {"assistant", "agent"}:
        return trace_event(
            runtime="trae",
            session_id=session_id,
            source_path=source_path,
            timestamp=timestamp,
            event_type="agent_message",
            tool_name=None,
            status="observed",
            input_summary="",
            output_summary=summarize_text(text),
            evidence_ref=line_ref(session_id, line_no),
        )
    return None


def cli_tool_call_event(
    tool_call: dict[str, Any], session_id: str, source_path: str, timestamp: str | None, line_no: int
) -> dict[str, Any]:
    tool_name = str(
        tool_call.get("name")
        or tool_call.get("tool_name")
        or tool_call.get("function")
        or tool_call.get("type")
        or "tool_call"
    )
    args = (
        tool_call.get("arguments")
        or tool_call.get("args")
        or tool_call.get("input")
        or tool_call.get("params")
    )
    command = command_from_value(args)
    return trace_event(
        runtime="trae",
        session_id=session_id,
        source_path=source_path,
        timestamp=timestamp,
        event_type=classify_command_event(command) if command else "tool_call",
        tool_name=tool_name,
        status="pending",
        input_summary=summarize_value(args),
        output_summary="tool_call observed",
        evidence_ref=line_ref(session_id, line_no),
        warnings=["tool output not observed"],
    )


def cli_tool_result_event(
    tool_result: dict[str, Any], session_id: str, source_path: str, timestamp: str | None, line_no: int
) -> dict[str, Any]:
    output = tool_result.get("output") or tool_result.get("content") or tool_result.get("result")
    status = str(tool_result.get("status") or "")
    if not status:
        status = "failure" if tool_result.get("error") else "observed"
    return trace_event(
        runtime="trae",
        session_id=session_id,
        source_path=source_path,
        timestamp=timestamp,
        event_type="tool_output",
        tool_name=str(tool_result.get("name") or tool_result.get("tool_name") or "tool_result"),
        status=status,
        input_summary="",
        output_summary=summarize_value(output or tool_result.get("error")),
        evidence_ref=line_ref(session_id, line_no),
    )


def read_cli_session_meta(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    return {
        "id": payload.get("id"),
        "created_at": payload.get("created_at"),
        "updated_at": payload.get("updated_at"),
        "cwd": metadata.get("cwd") or payload.get("cwd"),
        "model_name": metadata.get("model_name"),
        "title": metadata.get("title"),
    }


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    warnings: list[str] = []
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line_no, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    records.append({"line_no": line_no, "record": json.loads(line)})
                except json.JSONDecodeError as exc:
                    warnings.append(f"Skipped invalid JSON line {line_no}: {exc}")
    except OSError as exc:
        warnings.append(f"Could not read {path}: {exc}")
    return records, warnings


def sniff_jsonl_kind(path: Path) -> str | None:
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line in handle:
                if not line.strip():
                    continue
                payload = json.loads(line)
                if isinstance(payload, dict):
                    if "traceID" in payload and "spanID" in payload:
                        return "cli_traces"
                    if any(key in payload for key in ("message", "agent_start", "agent_end", "state_update")):
                        return "cli_events"
                return None
    except (OSError, json.JSONDecodeError):
        return None
    return None


def split_log_line(line: str) -> tuple[str | None, str, str]:
    match = LOG_PREFIX_RE.match(line.rstrip("\n"))
    if not match:
        return None, "info", line.strip()
    return match.group("timestamp"), match.group("level"), match.group("body")


def renderer_line_matches_session(line: str, session_id: str) -> bool:
    return session_id in line


def first_session_id(text: str) -> str | None:
    match = SESSION_ID_RE.search(text)
    if not match:
        return None
    return match.group("json") or match.group("plain")


def workspace_needles(workspace_norm: str) -> list[str]:
    slash = workspace_norm.replace("\\", "/")
    escaped = workspace_norm.replace("\\", "\\\\")
    escaped_slash = slash.replace("/", "\\/")
    return [workspace_norm, slash, escaped, escaped_slash]


def workspace_matches(text: str, workspace_norm: str) -> bool:
    folded = text.casefold()
    return any(needle in folded for needle in workspace_needles(workspace_norm))


def loads_json(raw: str) -> Any:
    if raw == "undefined":
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def parse_logged_string(raw: str) -> str:
    text = raw.strip()
    if not text:
        return ""
    if text.startswith('"'):
        try:
            return str(json.loads(text))
        except json.JSONDecodeError:
            return text.strip('"')
    return text


def public_tool_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        key: payload.get(key)
        for key in ("session_id", "message_id", "tool_type", "tool_id", "block_type", "block_id")
        if payload.get(key) not in {None, ""}
    }


def public_chat_trigger_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        key: payload.get(key)
        for key in (
            "session_id",
            "message_id",
            "agent_name",
            "agent_id",
            "agent_type",
            "chat_type",
            "command_type",
            "trigger_mode",
            "slash_skill_count",
            "workspace_folders",
            "file_count",
            "has_context",
        )
        if is_present(payload.get(key))
    }


def public_command_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        key: payload.get(key)
        for key in (
            "toolCallId",
            "command",
            "args",
            "execEnv",
            "blocking",
            "chatSessionId",
            "targetFolderPath",
            "workspaceFolders",
            "sessionType",
            "callId",
        )
        if is_present(payload.get(key))
    }


def summarize_command_result(payload: dict[str, Any]) -> str:
    summary = {
        "exit_code": payload.get("exitCode"),
        "command": payload.get("command"),
    }
    logs = payload.get("logs")
    if isinstance(logs, list) and logs:
        summary["output"] = summarize_text("\n".join(str(item) for item in logs))
    elif payload.get("error"):
        summary["error"] = payload.get("error")
    return summarize_value(summary)


def is_present(value: Any) -> bool:
    return value is not None and value != "" and value != []


def append_evidence_ref(current: Any, new_ref: str) -> str:
    current_text = str(current or "").strip()
    if not current_text:
        return new_ref
    if new_ref in current_text:
        return current_text
    return f"{current_text}; {new_ref}"


def terminal_trace_status(categories: dict[str, Any]) -> str:
    exit_code = str(categories.get("exitCode") or "")
    if exit_code == "0":
        return "success"
    if exit_code and exit_code != "undefined":
        return "failure"
    if str(categories.get("error") or "") not in {"", "0", "false", "False"}:
        return "failure"
    if categories.get("last_stage") == "command_finished":
        return "observed"
    return "pending"


def classify_command_event(command: str | None) -> str:
    return "verification" if command and VALIDATION_COMMAND_RE.search(command) else "tool_call"


def is_patch_tool(tool_type: str) -> bool:
    return tool_type.lower() in {
        "write",
        "edit",
        "multiedit",
        "applypatch",
        "deletefile",
        "edit_file_search_replace",
    }


def content_to_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)
    return str(content)


def is_hidden_or_context_message(text: str, extra: dict[str, Any]) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped.startswith("<system-reminder>") or "<context name=" in stripped:
        return True
    if extra.get("is_additional_context_input") is True:
        return True
    if extra and extra.get("is_original_user_input") is False:
        return True
    return False


def first_dict(record: dict[str, Any], keys: tuple[str, ...]) -> dict[str, Any] | None:
    for key in keys:
        value = record.get(key)
        if isinstance(value, dict):
            return value
    return None


def nested_get(payload: Any, keys: tuple[str, ...]) -> Any:
    current = payload
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def command_from_value(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("command") or value.get("cmd") or "")
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return value
        if isinstance(parsed, dict):
            return str(parsed.get("command") or parsed.get("cmd") or value)
        return value
    return ""


def tags_to_dict(tags: Any) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if not isinstance(tags, list):
        return result
    for item in tags:
        if not isinstance(item, dict):
            continue
        key = item.get("key")
        if key:
            result[str(key)] = item.get("value")
    return result


def first_log_field(span: dict[str, Any], field_name: str) -> Any:
    for log in span.get("logs") or []:
        fields = log.get("fields") if isinstance(log, dict) else None
        if not isinstance(fields, list):
            continue
        for field in fields:
            if isinstance(field, dict) and field.get("key") == field_name:
                return field.get("value")
    return None


def timestamp_from_span(span: dict[str, Any]) -> str | None:
    raw = span.get("startTime")
    if raw is None:
        return None
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return None
    if value > 10_000_000_000_000:
        seconds = value / 1_000_000
    elif value > 10_000_000_000:
        seconds = value / 1_000
    else:
        seconds = value
    try:
        return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()
    except (OSError, OverflowError, ValueError):
        return None


def dedupe_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduped: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for event in events:
        key = (
            event.get("event_type"),
            event.get("tool_name"),
            event.get("input_summary"),
            event.get("output_summary"),
            event.get("evidence_ref"),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(event)
    return deduped


def event_sort_key(event: dict[str, Any]) -> tuple[str, str]:
    return (str(event.get("timestamp") or ""), str(event.get("evidence_ref") or ""))


def infer_session_id(events: list[dict[str, Any]]) -> str | None:
    counts = Counter(str(event.get("session_id") or "") for event in events if event.get("session_id"))
    return counts.most_common(1)[0][0] if counts else None


def newest_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return sorted(candidates, key=lambda c: c.get("mtime", 0), reverse=True)[0]


def max_existing_mtime(paths: list[Path]) -> float:
    mtimes = [path.stat().st_mtime for path in paths if path.exists()]
    return max(mtimes) if mtimes else 0


def line_ref(session_id: str, line_no: int) -> str:
    return f"trae-session:{session_id}#line:{line_no}"


def span_ref(session_id: str, span: dict[str, Any], line_no: int) -> str:
    return f"trae-session:{session_id}#span:{span.get('spanID') or line_no}"


def file_line_ref(source_path: str, line_no: int) -> str:
    return f"file:{source_path}#line:{line_no}"
