#!/usr/bin/env python3
"""OpenCode trace adapter.

Supported sources:
- OpenCode SQLite data store at ~/.local/share/opencode/opencode.db.
- JSON emitted by `opencode export [sessionID]` or `opencode export --sanitize`.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
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
    r"(?i)\b(skill-lint|py_compile|pytest|unittest|cargo\s+test|go\s+test|npm\s+(?:run\s+)?test|pnpm\s+test|yarn\s+test|lint|build|cjpm\s+build|validate|validator)\b"
)
FILE_DUMP_COMMAND_RE = re.compile(r"(?i)\b(get-content|gc|type|cat)\b")
PATCH_TOOL_NAMES = {"edit", "write", "patch", "apply_patch", "multiedit"}
OMIT_OUTPUT_TOOLS = {"read", "skill", "write", "edit", "patch"}
SKIPPED_PART_TYPES = {"reasoning", "step-start", "step-finish", "file"}
MAX_EXPLICIT_JSON_FILES = 10


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    workspace_norm = normalize_path(workspace)

    if trace_file:
        selected = trace_file.expanduser().resolve(strict=False)
        if not selected.exists():
            return status_result(
                runtime="opencode",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"Trace file does not exist: {selected}"],
            )
        return parse_explicit_source(selected, workspace_norm, session_id)

    candidates = discover_candidates()
    if not candidates:
        roots = ", ".join(str(path) for path in opencode_data_roots())
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No OpenCode database sessions found. Checked: {roots}"],
        )

    if session_id:
        exact = [
            c
            for c in candidates
            if c.get("session_id") == session_id or session_id in str(c.get("session_id") or "")
        ]
        if len(exact) == 1:
            return parse_db_session(Path(exact[0]["path"]), exact[0]["session_id"], workspace_norm)
        if len(exact) > 1:
            return ambiguous_result("opencode", workspace_norm, exact)
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No OpenCode session matched session id: {session_id}"],
            candidates=public_candidates(candidates),
        )

    exact_workspace = [c for c in candidates if c.get("cwd_norm") == workspace_norm]
    if exact_workspace:
        selected = newest_candidate(exact_workspace)
        return parse_db_session(Path(selected["path"]), selected["session_id"], workspace_norm)

    approximate = [c for c in candidates if paths_related(c.get("cwd_norm"), workspace_norm)]
    if len(approximate) == 1:
        parsed = parse_db_session(Path(approximate[0]["path"]), approximate[0]["session_id"], workspace_norm)
        parsed["collection_confidence"] = "medium"
        parsed["warnings"].append(
            "Selected an approximate OpenCode workspace match; verify trace_source before saving."
        )
        return parsed
    if len(approximate) > 1:
        return ambiguous_result("opencode", workspace_norm, approximate)

    return status_result(
        runtime="opencode",
        status="not_found",
        workspace=workspace_norm,
        warnings=["OpenCode sessions were found, but none matched the requested workspace."],
        candidates=public_candidates(candidates),
    )


def parse_explicit_source(
    source: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    if source.is_dir():
        db_path = source / "opencode.db"
        if db_path.exists():
            return select_db_session(db_path, workspace_norm, session_id)

        json_files = sorted(source.glob("*.json"), key=lambda path: path.stat().st_mtime, reverse=True)
        if session_id:
            matches = [path for path in json_files if session_id in path.stem]
            if len(matches) == 1:
                return parse_export_file(matches[0], workspace_norm)
            if len(matches) > 1:
                return ambiguous_result(
                    "opencode",
                    workspace_norm,
                    [candidate_from_export_file(path) for path in matches],
                )
        if len(json_files) == 1:
            return parse_export_file(json_files[0], workspace_norm)
        if len(json_files) > 1:
            return ambiguous_result(
                "opencode",
                workspace_norm,
                [candidate_from_export_file(path) for path in json_files[:MAX_EXPLICIT_JSON_FILES]],
            )
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Directory does not contain opencode.db or an OpenCode export JSON file: {source}"],
        )

    if source.name == "opencode.db" or source.suffix.lower() in {".db", ".sqlite", ".sqlite3"}:
        return select_db_session(source, workspace_norm, session_id)

    return parse_export_file(source, workspace_norm)


def discover_candidates() -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    seen: set[str] = set()
    for root in opencode_data_roots():
        db_path = root / "opencode.db"
        db_key = normalize_path(db_path)
        if db_key in seen or not db_path.exists():
            continue
        seen.add(db_key)
        candidates.extend(discover_db_candidates(db_path))
    candidates.sort(key=lambda c: c.get("mtime", 0), reverse=True)
    return candidates


def opencode_data_roots() -> list[Path]:
    roots: list[Path] = []
    for env_name in ("OPENCODE_DATA_DIR",):
        value = os.environ.get(env_name)
        if value:
            roots.append(Path(value).expanduser())

    xdg_data_home = os.environ.get("XDG_DATA_HOME")
    if xdg_data_home:
        roots.append(Path(xdg_data_home).expanduser() / "opencode")

    roots.append(Path.home() / ".local" / "share" / "opencode")

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        roots.append(Path(local_app_data).expanduser() / "opencode")

    deduped: list[Path] = []
    seen: set[str] = set()
    for root in roots:
        key = normalize_path(root)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(root)
    return deduped


def discover_db_candidates(db_path: Path) -> list[dict[str, Any]]:
    try:
        with open_db(db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                """
                select
                  s.id,
                  s.project_id,
                  s.directory,
                  s.path,
                  s.title,
                  s.version,
                  s.agent,
                  s.time_created,
                  s.time_updated,
                  p.worktree
                from session s
                left join project p on p.id = s.project_id
                order by s.time_updated desc
                """
            ).fetchall()
    except sqlite3.Error:
        return []

    return [candidate_from_session_row(db_path, row) for row in rows]


def select_db_session(
    db_path: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    candidates = discover_db_candidates(db_path)
    if not candidates:
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No OpenCode sessions found in database: {db_path}"],
        )

    if session_id:
        exact = [
            c
            for c in candidates
            if c.get("session_id") == session_id or session_id in str(c.get("session_id") or "")
        ]
        if len(exact) == 1:
            return parse_db_session(db_path, exact[0]["session_id"], workspace_norm)
        if len(exact) > 1:
            return ambiguous_result("opencode", workspace_norm, exact)
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No OpenCode session in {db_path} matched session id: {session_id}"],
            candidates=public_candidates(candidates),
        )

    exact_workspace = [c for c in candidates if c.get("cwd_norm") == workspace_norm]
    if exact_workspace:
        selected = newest_candidate(exact_workspace)
        return parse_db_session(db_path, selected["session_id"], workspace_norm)

    approximate = [c for c in candidates if paths_related(c.get("cwd_norm"), workspace_norm)]
    if len(approximate) == 1:
        parsed = parse_db_session(db_path, approximate[0]["session_id"], workspace_norm)
        parsed["collection_confidence"] = "medium"
        parsed["warnings"].append(
            "Selected an approximate OpenCode workspace match from explicit database; verify trace_source."
        )
        return parsed
    if len(approximate) > 1:
        return ambiguous_result("opencode", workspace_norm, approximate)

    return status_result(
        runtime="opencode",
        status="not_found",
        workspace=workspace_norm,
        warnings=["OpenCode database was readable, but no session matched the requested workspace."],
        candidates=public_candidates(candidates),
    )


def parse_db_session(db_path: Path, session_id: str, workspace_norm: str) -> dict[str, Any]:
    try:
        with open_db(db_path) as conn:
            conn.row_factory = sqlite3.Row
            session_row = conn.execute(
                """
                select
                  s.id,
                  s.project_id,
                  s.slug,
                  s.directory,
                  s.path,
                  s.title,
                  s.version,
                  s.agent,
                  s.model,
                  s.time_created,
                  s.time_updated,
                  p.worktree
                from session s
                left join project p on p.id = s.project_id
                where s.id = ?
                """,
                (session_id,),
            ).fetchone()
            if not session_row:
                return status_result(
                    runtime="opencode",
                    status="not_found",
                    workspace=workspace_norm,
                    warnings=[f"OpenCode session not found: {session_id}"],
                )
            messages = load_db_messages(conn, session_id)
    except sqlite3.Error as exc:
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Could not read OpenCode database {db_path}: {exc}"],
        )

    info = session_info_from_db_row(session_row)
    parsed = parse_session_payload(
        info=info,
        messages=messages,
        source_path=str(db_path),
        workspace_norm=workspace_norm,
        explicit_export=False,
    )
    return parsed


def load_db_messages(conn: sqlite3.Connection, session_id: str) -> list[dict[str, Any]]:
    message_rows = conn.execute(
        """
        select id, session_id, time_created, time_updated, data
        from message
        where session_id = ?
        order by time_created, id
        """,
        (session_id,),
    ).fetchall()
    part_rows = conn.execute(
        """
        select id, session_id, message_id, time_created, time_updated, data
        from part
        where session_id = ?
        order by time_created, id
        """,
        (session_id,),
    ).fetchall()

    parts_by_message: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in part_rows:
        payload = loads_json_object(row["data"])
        if not payload:
            continue
        payload["id"] = row["id"]
        payload["sessionID"] = row["session_id"]
        payload["messageID"] = row["message_id"]
        payload["_time_created"] = row["time_created"]
        payload["_time_updated"] = row["time_updated"]
        parts_by_message[row["message_id"]].append(payload)

    messages: list[dict[str, Any]] = []
    for row in message_rows:
        info = loads_json_object(row["data"])
        if not info:
            continue
        info["id"] = row["id"]
        info["sessionID"] = row["session_id"]
        info["_time_created"] = row["time_created"]
        info["_time_updated"] = row["time_updated"]
        messages.append(
            {
                "info": info,
                "parts": parts_by_message.get(row["id"], []),
            }
        )
    return messages


def parse_export_file(path: Path, workspace_norm: str) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8-sig", errors="replace")
        payload = loads_export_payload(raw)
    except OSError as exc:
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Could not read OpenCode export file {path}: {exc}"],
        )

    if not isinstance(payload, dict):
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"OpenCode export file is not a JSON object: {path}"],
        )

    info = payload.get("info") if isinstance(payload.get("info"), dict) else {}
    messages = payload.get("messages") if isinstance(payload.get("messages"), list) else []
    if not info or not messages:
        return status_result(
            runtime="opencode",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"OpenCode export JSON must contain info and messages: {path}"],
        )

    return parse_session_payload(
        info=info,
        messages=[message for message in messages if isinstance(message, dict)],
        source_path=str(path),
        workspace_norm=workspace_norm,
        explicit_export=True,
    )


def parse_session_payload(
    *,
    info: dict[str, Any],
    messages: list[dict[str, Any]],
    source_path: str,
    workspace_norm: str,
    explicit_export: bool,
) -> dict[str, Any]:
    session_id = str(info.get("id") or "unknown")
    cwd = session_cwd(info)
    cwd_norm = normalize_path(Path(cwd)) if cwd and not is_redacted(cwd) else None
    warnings: list[str] = []
    if cwd_norm and cwd_norm != workspace_norm:
        warnings.append("OpenCode session directory does not match requested workspace.")
    if explicit_export:
        warnings.append("OpenCode export JSON was provided explicitly; verify it was generated with the intended session.")

    events: list[dict[str, Any]] = []
    order = 0
    for message in messages:
        msg_info = message.get("info") if isinstance(message.get("info"), dict) else {}
        if not msg_info:
            msg_info = message
        parts = message.get("parts") if isinstance(message.get("parts"), list) else []
        role = str(msg_info.get("role") or "").lower()
        message_id = str(msg_info.get("id") or f"message-{order}")

        if role == "user":
            text = user_message_text(parts)
            if text:
                order += 1
                events.append(
                    ordered_event(
                        trace_event(
                            runtime="opencode",
                            session_id=session_id,
                            source_path=source_path,
                            timestamp=timestamp_from_message(msg_info),
                            event_type="user_message",
                            tool_name=None,
                            status="observed",
                            input_summary=summarize_text(text),
                            output_summary="",
                            evidence_ref=message_ref(session_id, message_id),
                        ),
                        order,
                    )
                )
            continue

        if role != "assistant":
            continue

        for part in parts:
            if not isinstance(part, dict):
                continue
            part_type = str(part.get("type") or "")
            if part_type in SKIPPED_PART_TYPES:
                continue
            order += 1
            event = event_from_assistant_part(
                part=part,
                msg_info=msg_info,
                session_id=session_id,
                source_path=source_path,
                order=order,
            )
            if event:
                events.append(event)

    events.sort(
        key=lambda event: (
            str(event.get("timestamp") or ""),
            int(event.get("_order") or 0),
            str(event.get("evidence_ref") or ""),
        )
    )
    for event in events:
        event.pop("_order", None)
    assign_trace_refs(events)

    if explicit_export:
        confidence = "high" if cwd_norm == workspace_norm else "medium"
    else:
        confidence = "high" if cwd_norm == workspace_norm else "medium"

    return {
        "runtime": "opencode",
        "status": "ok",
        "session_id": session_id,
        "source_path": source_path,
        "workspace": workspace_norm,
        "collection_confidence": confidence,
        "session": {
            "id": session_id,
            "timestamp": timestamp_from_ms(nested_get(info, ("time", "updated")) or info.get("time_updated")),
            "cwd": cwd,
            "title": info.get("title"),
            "version": info.get("version"),
            "agent": info.get("agent"),
        },
        "events": events,
        "warnings": warnings,
    }


def event_from_assistant_part(
    *,
    part: dict[str, Any],
    msg_info: dict[str, Any],
    session_id: str,
    source_path: str,
    order: int,
) -> dict[str, Any] | None:
    part_type = str(part.get("type") or "")
    part_id = str(part.get("id") or f"part-{order}")
    timestamp = timestamp_from_part(part, msg_info)

    if part_type == "text":
        text = str(part.get("text") or "")
        if not text.strip():
            return None
        return ordered_event(
            trace_event(
                runtime="opencode",
                session_id=session_id,
                source_path=source_path,
                timestamp=timestamp,
                event_type="agent_message",
                tool_name=None,
                status="observed",
                input_summary="",
                output_summary=summarize_text(text),
                evidence_ref=part_ref(session_id, part_id),
            ),
            order,
        )

    if part_type == "tool":
        tool_name = str(part.get("tool") or "tool_call")
        state = part.get("state") if isinstance(part.get("state"), dict) else {}
        tool_input = state.get("input")
        return ordered_event(
            trace_event(
                runtime="opencode",
                session_id=session_id,
                source_path=source_path,
                timestamp=timestamp,
                event_type=classify_tool_event(tool_name, tool_input),
                tool_name=tool_name,
                status=tool_status(tool_name, state),
                input_summary=summarize_value(public_tool_input(tool_name, tool_input)),
                output_summary=summarize_tool_state(tool_name, tool_input, state),
                evidence_ref=part_ref(session_id, part_id),
                warnings=[] if state.get("status") else ["tool state status not observed"],
            ),
            order,
        )

    if part_type == "patch":
        return ordered_event(
            trace_event(
                runtime="opencode",
                session_id=session_id,
                source_path=source_path,
                timestamp=timestamp,
                event_type="patch",
                tool_name="patch",
                status="observed",
                input_summary=summarize_value(public_patch_part(part)),
                output_summary="patch part observed",
                evidence_ref=part_ref(session_id, part_id),
            ),
            order,
        )

    return None


def user_message_text(parts: list[Any]) -> str:
    text_parts: list[str] = []
    for part in parts:
        if not isinstance(part, dict):
            continue
        if str(part.get("type") or "") != "text":
            continue
        text = str(part.get("text") or "").strip()
        if text:
            text_parts.append(text)
    return "\n".join(text_parts)


def classify_tool_event(tool_name: str, tool_input: Any) -> str:
    normalized = tool_name.lower()
    if normalized in PATCH_TOOL_NAMES:
        return "patch"
    if normalized == "bash" and VALIDATION_COMMAND_RE.search(command_from_input(tool_input)):
        return "verification"
    return "tool_call"


def tool_status(tool_name: str, state: dict[str, Any]) -> str:
    status = str(state.get("status") or "").lower()
    if status in {"error", "failed", "failure"}:
        return "failure"
    if status in {"pending", "queued", "running"}:
        return "pending"
    if status == "completed" and tool_name.lower() in PATCH_TOOL_NAMES | {"bash"}:
        return "success"
    if status == "completed":
        return "observed"
    if state.get("error"):
        return "failure"
    return "observed"


def summarize_tool_state(tool_name: str, tool_input: Any, state: dict[str, Any]) -> str:
    normalized = tool_name.lower()
    if not state:
        return "tool state not observed"
    if state.get("error"):
        return summarize_value(state.get("error"))
    output = state.get("output")
    metadata = state.get("metadata") if isinstance(state.get("metadata"), dict) else None

    if normalized == "bash":
        return summarize_bash_output(tool_input, output)
    if normalized in OMIT_OUTPUT_TOOLS:
        return summarize_omitted_tool_result(normalized, tool_input, state)

    if output not in {None, ""}:
        return summarize_text(output)
    if metadata:
        return "metadata=" + summarize_value(metadata)
    if state.get("title"):
        return summarize_text(state.get("title"))
    return f"tool status={state.get('status') or 'observed'}"


def summarize_bash_output(tool_input: Any, output: Any) -> str:
    command = command_from_input(tool_input)
    text = normalize_text_encoding(str(output or ""))
    if not text.strip():
        return "bash output not observed"
    summary = summarize_text(text)
    if command_prints_file_content(command, text):
        return "stdout omitted: command printed file content; input_summary keeps command/path"
    if looks_encoding_damaged(summary):
        return "stdout omitted: output appears encoding-damaged; use evidence_ref for raw trace"
    return "output: " + summary


def summarize_omitted_tool_result(
    tool_name: str, tool_input: Any, state: dict[str, Any]
) -> str:
    parts: list[str] = [f"status={state.get('status') or 'observed'}"]
    if state.get("title"):
        parts.append("title=" + summarize_text(state.get("title")))
    metadata = state.get("metadata") if isinstance(state.get("metadata"), dict) else None
    if metadata:
        parts.append("metadata=" + summarize_value(metadata))
    if state.get("output") not in {None, ""}:
        parts.append("large content omitted; input_summary keeps tool target")
    return "; ".join(parts)


def public_tool_input(tool_name: str, value: Any) -> Any:
    normalized = tool_name.lower()
    if not isinstance(value, dict):
        return value

    if normalized == "bash":
        return {
            key: value.get(key)
            for key in ("command", "description")
            if value.get(key) not in {None, ""}
        }

    if normalized in {"read", "write", "edit", "patch"}:
        return {
            key: summarize_public_input_value(key, item)
            for key, item in value.items()
            if key not in {"content", "oldString", "newString", "patch", "diff"}
        } | {
            key: "<omitted>"
            for key in ("content", "oldString", "newString", "patch", "diff")
            if key in value
        }

    if normalized == "task":
        return {
            key: summarize_public_input_value(key, item)
            for key, item in value.items()
            if key in {"description", "subagent_type", "agent", "mode"}
        } or {"description": summarize_text(value.get("description") or value.get("prompt") or "")}

    return {
        key: summarize_public_input_value(key, item)
        for key, item in value.items()
        if key not in {"content"}
    }


def summarize_public_input_value(key: str, value: Any) -> Any:
    if isinstance(value, str) and (key.lower() in {"prompt", "query"} or len(value) > 500):
        return summarize_text(value)
    return value


def public_patch_part(part: dict[str, Any]) -> dict[str, Any]:
    return {
        key: part.get(key)
        for key in ("id", "sessionID", "messageID", "files", "path", "status")
        if part.get(key) not in {None, ""}
    }


def command_from_input(value: Any) -> str:
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


def command_prints_file_content(command: str, output: str) -> bool:
    if not FILE_DUMP_COMMAND_RE.search(command or ""):
        return False
    if any(ext in command.lower() for ext in (".md", ".txt", ".json", ".cj", ".py")):
        return True
    sample = output[:500]
    return sample.startswith("---") or "\n#" in sample or "\n##" in sample


def session_info_from_db_row(row: sqlite3.Row) -> dict[str, Any]:
    model = loads_json_object(row["model"]) if row["model"] else row["model"]
    return {
        "id": row["id"],
        "slug": row["slug"],
        "projectID": row["project_id"],
        "directory": row["directory"] or row["worktree"],
        "path": row["path"],
        "title": row["title"],
        "agent": row["agent"],
        "model": model,
        "version": row["version"],
        "time": {
            "created": row["time_created"],
            "updated": row["time_updated"],
        },
        "time_created": row["time_created"],
        "time_updated": row["time_updated"],
    }


def candidate_from_session_row(db_path: Path, row: sqlite3.Row) -> dict[str, Any]:
    cwd = row["directory"] or row["worktree"] or row["path"]
    updated = row["time_updated"] or row["time_created"] or 0
    return {
        "path": db_path,
        "source_path": str(db_path),
        "mtime": updated / 1000 if isinstance(updated, int) else db_path.stat().st_mtime,
        "session_id": row["id"],
        "cwd": cwd,
        "cwd_norm": normalize_path(Path(cwd)) if cwd else None,
        "timestamp": timestamp_from_ms(updated),
        "title": row["title"],
    }


def candidate_from_export_file(path: Path) -> dict[str, Any]:
    return {
        "path": path,
        "source_path": str(path),
        "mtime": path.stat().st_mtime,
        "session_id": path.stem,
        "cwd": None,
        "timestamp": None,
    }


def open_db(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)


def loads_json_object(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        return {}
    try:
        payload = json.loads(value)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def loads_export_payload(raw: str) -> Any:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            return json.loads(raw[start : end + 1])
        except json.JSONDecodeError:
            return None


def session_cwd(info: dict[str, Any]) -> str | None:
    path = info.get("path") if isinstance(info.get("path"), dict) else None
    return (
        as_non_empty_str(info.get("directory"))
        or as_non_empty_str(path.get("cwd") if path else None)
        or as_non_empty_str(path.get("root") if path else None)
    )


def timestamp_from_message(info: dict[str, Any]) -> str | None:
    return timestamp_from_ms(nested_get(info, ("time", "created")) or info.get("_time_created"))


def timestamp_from_part(part: dict[str, Any], msg_info: dict[str, Any]) -> str | None:
    return timestamp_from_ms(
        nested_get(part, ("time", "start"))
        or part.get("_time_created")
        or nested_get(msg_info, ("time", "created"))
        or msg_info.get("_time_created")
    )


def timestamp_from_ms(value: Any) -> str | None:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    if number <= 0:
        return None
    seconds = number / 1000 if number > 10_000_000_000 else number
    try:
        return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()
    except (OSError, OverflowError, ValueError):
        return None


def nested_get(payload: Any, keys: tuple[str, ...]) -> Any:
    current = payload
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def as_non_empty_str(value: Any) -> str | None:
    text = str(value or "").strip()
    return text or None


def is_redacted(value: str) -> bool:
    return value.startswith("[redacted:")


def ordered_event(event: dict[str, Any], order: int) -> dict[str, Any]:
    event["_order"] = order
    return event


def newest_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return sorted(candidates, key=lambda c: c.get("mtime", 0), reverse=True)[0]


def message_ref(session_id: str, message_id: str) -> str:
    return f"opencode-session:{session_id}#message:{message_id}"


def part_ref(session_id: str, part_id: str) -> str:
    return f"opencode-session:{session_id}#part:{part_id}"
