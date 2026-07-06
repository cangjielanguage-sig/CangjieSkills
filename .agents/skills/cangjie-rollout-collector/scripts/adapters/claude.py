#!/usr/bin/env python3
"""Claude Code trace adapter."""

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
    r"(?i)\b(skill-lint|py_compile|pytest|unittest|cargo\s+test|go\s+test|npm\s+(?:run\s+)?test|pnpm\s+test|yarn\s+test|lint|build|cjpm\s+build|validate|validator)\b"
)
FILE_DUMP_COMMAND_RE = re.compile(r"(?i)\b(get-content|gc|type|cat)\b")
PATCH_TOOL_NAMES = {"Edit", "MultiEdit", "Write", "NotebookEdit"}
SKIPPED_RECORD_TYPES = {"queue-operation", "last-prompt", "attachment", "summary"}
SKIPPED_CONTENT_TYPES = {"thinking"}
DISCOVERY_META_LINE_LIMIT = 80


def collect(
    workspace: Path, trace_file: Path | None = None, session_id: str | None = None
) -> dict[str, Any]:
    workspace_norm = normalize_path(workspace)

    if trace_file:
        selected = trace_file.expanduser().resolve(strict=False)
        if not selected.exists():
            return status_result(
                runtime="claude",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"Trace file does not exist: {selected}"],
            )
        return parse_explicit_source(selected, workspace_norm, session_id)

    candidates = discover_candidates()
    if not candidates:
        return status_result(
            runtime="claude",
            status="not_found",
            workspace=workspace_norm,
            warnings=["No Claude Code JSONL transcripts found under ~/.claude/projects."],
        )

    if session_id:
        exact = [
            c
            for c in candidates
            if c.get("session_id") == session_id or session_id in Path(c["path"]).stem
        ]
        if len(exact) == 1:
            return parse_claude_file(exact[0]["path"], workspace_norm)
        if len(exact) > 1:
            return ambiguous_result("claude", workspace_norm, exact)
        return status_result(
            runtime="claude",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"No Claude session matched session id: {session_id}"],
            candidates=public_candidates(candidates),
        )

    exact_workspace = [c for c in candidates if c.get("cwd_norm") == workspace_norm]
    if exact_workspace:
        return parse_claude_file(newest_candidate(exact_workspace)["path"], workspace_norm)

    approximate = [c for c in candidates if paths_related(c.get("cwd_norm"), workspace_norm)]
    if len(approximate) == 1:
        parsed = parse_claude_file(approximate[0]["path"], workspace_norm)
        parsed["collection_confidence"] = "medium"
        parsed["warnings"].append(
            "Selected an approximate Claude cwd match; verify trace_source before saving."
        )
        return parsed
    if len(approximate) > 1:
        return ambiguous_result("claude", workspace_norm, approximate)

    return status_result(
        runtime="claude",
        status="not_found",
        workspace=workspace_norm,
        warnings=["Claude transcripts were found, but none matched the requested workspace."],
        candidates=public_candidates(candidates),
    )


def parse_explicit_source(
    source: Path, workspace_norm: str, session_id: str | None
) -> dict[str, Any]:
    if source.is_dir():
        files = sorted(source.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            return status_result(
                runtime="claude",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"Directory does not contain Claude JSONL transcripts: {source}"],
            )
        if session_id:
            matches = [p for p in files if session_id in p.stem]
            if not matches:
                matches = [
                    p
                    for p in files
                    if read_session_meta(p).get("session_id") == session_id
                ]
            if len(matches) == 1:
                return parse_claude_file(matches[0], workspace_norm)
            if len(matches) > 1:
                return ambiguous_result(
                    "claude", workspace_norm, [candidate_from_path(p) for p in matches]
                )
            return status_result(
                runtime="claude",
                status="not_found",
                workspace=workspace_norm,
                warnings=[f"No Claude transcript in {source} matched session id: {session_id}"],
                candidates=public_candidates([candidate_from_path(p) for p in files]),
            )
        parsed = parse_claude_file(files[0], workspace_norm)
        if len(files) > 1:
            parsed["warnings"].append(
                "Explicit Claude transcript directory contained multiple JSONL files; selected the newest."
            )
        return parsed

    if source.suffix.lower() != ".jsonl":
        return status_result(
            runtime="claude",
            status="not_found",
            workspace=workspace_norm,
            warnings=[f"Claude adapter expects a .jsonl transcript or transcript directory: {source}"],
        )
    return parse_claude_file(source, workspace_norm)


def discover_candidates() -> list[dict[str, Any]]:
    root = Path.home() / ".claude" / "projects"
    if not root.exists():
        return []

    candidates: list[dict[str, Any]] = []
    for path in root.glob("*/*.jsonl"):
        if not path.is_file():
            continue
        candidates.append(candidate_from_path(path))
    candidates.sort(key=lambda c: c.get("mtime", 0), reverse=True)
    return candidates


def candidate_from_path(path: Path) -> dict[str, Any]:
    meta = read_session_meta(path)
    cwd = meta.get("cwd")
    return {
        "path": path,
        "source_path": str(path),
        "mtime": path.stat().st_mtime,
        "session_id": meta.get("session_id") or path.stem,
        "cwd": cwd,
        "cwd_norm": normalize_path(Path(cwd)) if cwd else None,
        "timestamp": meta.get("timestamp"),
    }


def read_session_meta(path: Path) -> dict[str, Any]:
    meta: dict[str, Any] = {"session_id": path.stem, "cwd": None, "timestamp": None}
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line_no, line in enumerate(handle, start=1):
                if line_no > DISCOVERY_META_LINE_LIMIT:
                    break
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    if record.get("sessionId"):
                        meta["session_id"] = record.get("sessionId")
                    if record.get("cwd"):
                        meta["cwd"] = record.get("cwd")
                    if record.get("timestamp"):
                        meta["timestamp"] = record.get("timestamp")
                    if meta.get("session_id") and meta.get("cwd"):
                        break
    except OSError:
        pass
    return meta


def parse_claude_file(path: Path, workspace_norm: str) -> dict[str, Any]:
    records, parse_warnings = read_jsonl(path)
    session = extract_session(records, path)
    session_id = str(session.get("id") or path.stem)
    source_path = str(path)

    events: list[dict[str, Any]] = []
    tool_calls: dict[str, dict[str, Any]] = {}
    tool_results: dict[str, dict[str, Any]] = {}
    warnings = list(parse_warnings)

    for item in records:
        record = item["record"]
        if should_skip_record(record):
            continue

        record_type = str(record.get("type") or "")
        message = record.get("message") if isinstance(record.get("message"), dict) else {}
        content = content_items(message.get("content"))
        timestamp = record.get("timestamp")
        line_no = item["line_no"]

        if record_type == "user":
            text_parts: list[str] = []
            for block in content:
                block_type = str(block.get("type") or "")
                if block_type == "tool_result":
                    result = tool_result_from_block(block, record, line_no, timestamp)
                    if result.get("tool_use_id"):
                        tool_results[str(result["tool_use_id"])] = result
                    continue
                if block_type == "text":
                    text = block_text(block)
                    if text:
                        text_parts.append(text)
            if text_parts:
                events.append(
                    ordered_event(
                        trace_event(
                            runtime="claude",
                            session_id=session_id,
                            source_path=source_path,
                            timestamp=timestamp,
                            event_type="user_message",
                            tool_name=None,
                            status="observed",
                            input_summary=summarize_text("\n".join(text_parts)),
                            output_summary="",
                            evidence_ref=line_ref(session_id, line_no),
                        ),
                        line_no,
                    )
                )
        elif record_type == "assistant":
            text_parts = []
            for block in content:
                block_type = str(block.get("type") or "")
                if block_type in SKIPPED_CONTENT_TYPES:
                    continue
                if block_type == "tool_use":
                    call_id = str(block.get("id") or f"line-{line_no}")
                    tool_calls[call_id] = {
                        "timestamp": timestamp,
                        "line_no": line_no,
                        "name": str(block.get("name") or "tool_call"),
                        "input": block.get("input"),
                    }
                    continue
                if block_type == "text":
                    text = block_text(block)
                    if text:
                        text_parts.append(text)
            if text_parts:
                events.append(
                    ordered_event(
                        trace_event(
                            runtime="claude",
                            session_id=session_id,
                            source_path=source_path,
                            timestamp=timestamp,
                            event_type="agent_message",
                            tool_name=None,
                            status="observed",
                            input_summary="",
                            output_summary=summarize_text("\n".join(text_parts)),
                            evidence_ref=line_ref(session_id, line_no),
                        ),
                        line_no,
                    )
                )

    events.extend(build_tool_events(session_id, source_path, tool_calls, tool_results))
    events.extend(build_unmatched_result_events(session_id, source_path, tool_calls, tool_results))
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

    cwd_norm = session.get("cwd_norm")
    if cwd_norm and cwd_norm != workspace_norm:
        warnings.append("Claude session cwd does not match requested workspace.")

    return {
        "runtime": "claude",
        "status": "ok",
        "session_id": session_id,
        "source_path": source_path,
        "workspace": workspace_norm,
        "collection_confidence": "high" if cwd_norm == workspace_norm else "medium",
        "session": {
            "id": session_id,
            "timestamp": session.get("timestamp"),
            "cwd": session.get("cwd"),
            "version": session.get("version"),
        },
        "events": events,
        "warnings": warnings,
    }


def build_tool_events(
    session_id: str,
    source_path: str,
    calls: dict[str, dict[str, Any]],
    results: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for call_id, call in calls.items():
        result = results.get(call_id)
        tool_name = str(call.get("name") or "tool_call")
        event_type = classify_tool_event(tool_name, call.get("input"))
        status = infer_tool_status(tool_name, result)
        events.append(
            ordered_event(
                trace_event(
                    runtime="claude",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=call.get("timestamp"),
                    event_type=event_type,
                    tool_name=tool_name,
                    status=status,
                    input_summary=summarize_value(call.get("input")),
                    output_summary=summarize_tool_result(tool_name, call.get("input"), result),
                    evidence_ref=tool_ref(session_id, call_id),
                    warnings=[] if result else ["tool output not observed"],
                ),
                int(call.get("line_no") or 0),
            )
        )
    return events


def build_unmatched_result_events(
    session_id: str,
    source_path: str,
    calls: dict[str, dict[str, Any]],
    results: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for call_id, result in results.items():
        if call_id in calls:
            continue
        events.append(
            ordered_event(
                trace_event(
                    runtime="claude",
                    session_id=session_id,
                    source_path=source_path,
                    timestamp=result.get("timestamp"),
                    event_type="tool_output",
                    tool_name="unknown",
                    status="failure" if result_is_failure(result) else "observed",
                    input_summary="",
                    output_summary=summarize_tool_result("unknown", None, result),
                    evidence_ref=tool_ref(session_id, call_id),
                    warnings=["tool input not observed"],
                ),
                int(result.get("line_no") or 0),
            )
        )
    return events


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    warnings: list[str] = []
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line_no, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError as exc:
                    warnings.append(f"Skipped invalid JSON line {line_no}: {exc}")
                    continue
                if isinstance(payload, dict):
                    records.append({"line_no": line_no, "record": payload})
    except OSError as exc:
        warnings.append(f"Could not read trace file {path}: {exc}")
    return records, warnings


def extract_session(records: list[dict[str, Any]], path: Path) -> dict[str, Any]:
    session_id = path.stem
    timestamp = None
    cwd = None
    version = None
    for item in records:
        record = item["record"]
        if record.get("sessionId"):
            session_id = str(record.get("sessionId"))
        if record.get("timestamp"):
            timestamp = timestamp or record.get("timestamp")
        if record.get("cwd"):
            cwd = str(record.get("cwd"))
        if record.get("version"):
            version = str(record.get("version"))
        if session_id and cwd and version:
            break
    return {
        "id": session_id,
        "timestamp": timestamp,
        "cwd": cwd,
        "cwd_norm": normalize_path(Path(cwd)) if cwd else None,
        "version": version,
    }


def should_skip_record(record: dict[str, Any]) -> bool:
    record_type = str(record.get("type") or "")
    if record_type in SKIPPED_RECORD_TYPES:
        return True
    if record.get("isSidechain") is True:
        return True
    if record_type not in {"user", "assistant"}:
        return True
    return not isinstance(record.get("message"), dict)


def content_items(content: Any) -> list[dict[str, Any]]:
    if content is None:
        return []
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    if isinstance(content, dict):
        return [content]
    if isinstance(content, list):
        return [item for item in content if isinstance(item, dict)]
    return [{"type": "text", "text": str(content)}]


def block_text(block: dict[str, Any]) -> str:
    return str(block.get("text") or block.get("content") or "").strip()


def tool_result_from_block(
    block: dict[str, Any], record: dict[str, Any], line_no: int, timestamp: str | None
) -> dict[str, Any]:
    return {
        "tool_use_id": block.get("tool_use_id"),
        "timestamp": timestamp,
        "line_no": line_no,
        "content": block.get("content"),
        "is_error": block.get("is_error"),
        "tool_use_result": record.get("toolUseResult")
        if isinstance(record.get("toolUseResult"), dict)
        else None,
    }


def classify_tool_event(tool_name: str, tool_input: Any) -> str:
    if tool_name in PATCH_TOOL_NAMES:
        return "patch"
    if tool_name == "Bash" and VALIDATION_COMMAND_RE.search(command_from_input(tool_input)):
        return "verification"
    return "tool_call"


def infer_tool_status(tool_name: str, result: dict[str, Any] | None) -> str:
    if result is None:
        return "pending"
    if result_is_failure(result):
        return "failure"
    if tool_name in PATCH_TOOL_NAMES or tool_name == "Bash":
        return "success"
    return "observed"


def result_is_failure(result: dict[str, Any] | None) -> bool:
    if not result:
        return False
    if result.get("is_error") is True:
        return True
    payload = result.get("tool_use_result")
    if isinstance(payload, dict):
        if payload.get("interrupted") is True:
            return True
        error = payload.get("error") or payload.get("errorMessage")
        if error:
            return True
    return False


def summarize_tool_result(
    tool_name: str, tool_input: Any, result: dict[str, Any] | None
) -> str:
    if result is None:
        return "tool output not observed"
    payload = result.get("tool_use_result")
    content = result.get("content")

    if tool_name == "Bash":
        return summarize_bash_result(tool_input, payload, content)
    if tool_name == "Read":
        return summarize_structured_result(payload, content, omit_content=True) or (
            "read result observed; content omitted"
        )
    if tool_name in PATCH_TOOL_NAMES:
        return summarize_structured_result(payload, content, omit_content=True) or "patch result observed"
    return summarize_structured_result(payload, content, omit_content=False) or summarize_value(content)


def summarize_bash_result(tool_input: Any, payload: Any, content: Any) -> str:
    command = command_from_input(tool_input)
    payload = payload if isinstance(payload, dict) else {}
    stdout = str(payload.get("stdout") or "")
    stderr = str(payload.get("stderr") or "")
    if not stdout and not stderr and isinstance(content, str):
        stdout = content

    parts: list[str] = []
    if payload.get("interrupted") is True:
        parts.append("interrupted=true")
    if stdout.strip():
        stdout_summary = summarize_text(normalize_text_encoding(stdout))
        if command_prints_file_content(command, stdout):
            parts.append("stdout omitted: command printed file content; input_summary keeps command/path")
        elif looks_encoding_damaged(stdout_summary):
            parts.append("stdout omitted: output appears encoding-damaged; use evidence_ref for raw trace")
        else:
            parts.append("stdout=" + stdout_summary)
    if stderr.strip():
        parts.append("stderr=" + summarize_text(stderr))
    if not parts:
        parts.append("bash result observed")
    return "; ".join(parts)


def summarize_structured_result(payload: Any, content: Any, *, omit_content: bool) -> str:
    parts: list[str] = []
    if isinstance(payload, dict):
        public_payload = {}
        for key, value in payload.items():
            if omit_content and key in {"content", "stdout", "stderr"}:
                continue
            public_payload[key] = value
        if public_payload:
            parts.append(summarize_value(public_payload))
        if omit_content and any(key in payload for key in ("content", "stdout", "stderr")):
            parts.append("large content omitted; input_summary keeps tool target")
    if content and not omit_content:
        parts.append(summarize_value(content))
    return " | ".join(part for part in parts if part)


def command_from_input(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("command") or "")
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return value
        if isinstance(parsed, dict):
            return str(parsed.get("command") or value)
        return value
    return ""


def command_prints_file_content(command: str, output: str) -> bool:
    if not FILE_DUMP_COMMAND_RE.search(command or ""):
        return False
    if ".md" in command.lower() or ".txt" in command.lower() or ".json" in command.lower():
        return True
    sample = output[:500]
    return sample.startswith("---") or "\n#" in sample or "\n##" in sample


def ordered_event(event: dict[str, Any], line_no: int) -> dict[str, Any]:
    event["_order"] = line_no
    return event


def newest_candidate(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return sorted(candidates, key=lambda c: c.get("mtime", 0), reverse=True)[0]


def line_ref(session_id: str, line_no: int) -> str:
    return f"claude-session:{session_id}#line:{line_no}"


def tool_ref(session_id: str, tool_use_id: str) -> str:
    return f"claude-session:{session_id}#tool:{tool_use_id}"
