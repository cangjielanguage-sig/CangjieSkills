#!/usr/bin/env python3
"""Analyze HarmonyOS/Cangjie build logs and summarize actionable failures."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
FAILED_TASK_RE = re.compile(r"Failed\s+(:[^\s.]+)")
FILE_LOC_RE = re.compile(r"==>\s+(.+?):(\d+):(\d+):")


@dataclass
class Finding:
    code: str
    severity: str
    title: str
    evidence: str
    suggestion: str


def clean_text(raw: str) -> str:
    return ANSI_RE.sub("", raw).replace("\ufeff", "").replace("\r\n", "\n").replace("\r", "\n")


def first_error_block(lines: list[str]) -> list[str]:
    start = None
    for i, line in enumerate(lines):
        lower = line.lower()
        if "error:" in lower or "error code:" in lower or "failed :" in lower:
            start = i
            break
    if start is None:
        return []

    end = min(len(lines), start + 80)
    for i in range(start + 1, min(len(lines), start + 120)):
        lower = lines[i].lower()
        if "try the following" in lower or "* try:" in lower or "> hvigor error: build failed" in lower:
            end = i
            break
    return lines[start:end]


def collect_locations(lines: list[str]) -> list[dict[str, object]]:
    locations = []
    for line in lines:
        match = FILE_LOC_RE.search(line)
        if match:
            locations.append({
                "file": match.group(1),
                "line": int(match.group(2)),
                "column": int(match.group(3)),
            })
    return locations


def detect_findings(text: str) -> list[Finding]:
    lower = text.lower()
    findings: list[Finding] = []

    def add(code: str, title: str, evidence: str, suggestion: str, severity: str = "error") -> None:
        findings.append(Finding(code, severity, title, evidence, suggestion))

    if "datamodelexception: this data is not datamodelstring" in lower or "depmodel::loaddepincrementalcache" in lower:
        add(
            "cjpm_incremental_cache",
            "cjpm incremental dependency cache is likely corrupted or incompatible",
            "DataModelException / DepModel::loadDepIncrementalCache",
            "Use build_recovery.py --retry to clean project-local Hvigor/Cangjie intermediates. If it repeats, try [profile.build] incremental = false.",
        )

    if "expected type name after ':'" in lower:
        add(
            "arkts_object_literal_in_cangjie",
            "ArkTS-style object literal was used in Cangjie ArkUI code",
            "expected type name after ':'",
            "Replace calls such as .margin({left: 20}) with Cangjie named parameters and units, for example .margin(left: 20.vp).",
        )

    if "'trim' is not a member" in lower or '"trim" is not a member' in lower:
        add(
            "string_trim_missing",
            "Cangjie String does not provide JS/ArkTS trim() in this environment",
            "trim is not a member of String",
            "Check Cangjie String docs. Use trimAscii() for ASCII whitespace when appropriate.",
        )

    if "'length' is not a member" in lower and "observedarraylist" in lower:
        add(
            "observed_array_list_length",
            "ObservedArrayList uses size, not length",
            "length is not a member of ObservedArrayList",
            "Replace .length with .size.",
        )

    if "'add' is not a member" in lower and "observedarraylist" in lower:
        add(
            "observed_array_list_add",
            "ObservedArrayList appends with append(), not add()",
            "add is not a member of ObservedArrayList",
            "Replace .add(value) with .append(value).",
        )

    if "only ui component syntax can be written here" in lower:
        add(
            "arkts_builder_non_ui_statement",
            "ArkTS @Builder body contains a non-UI statement",
            "Only UI component syntax can be written here",
            "Move local declarations or calculations out of the @Builder body; pass the value as a parameter or call a side-effect-free helper inline.",
        )

    if "no signingconfigs" in lower:
        add(
            "missing_signing_config",
            "Signing config is missing but unsigned local build may still be usable",
            "No signingConfigs profile is configured",
            "Treat as non-blocking for local unsigned HAP validation unless the task requires signed release output.",
            severity="warning",
        )

    failed_markers = ("build failed", "failed :", "error code:", "tools execution failed", "invalid options")
    if "build successful" in lower and not any(marker in lower for marker in failed_markers) and not any(f.severity == "error" for f in findings):
        add(
            "build_successful",
            "Build completed successfully",
            "BUILD SUCCESSFUL",
            "Proceed to runtime/UI validation when the task changes behavior.",
            severity="info",
        )

    return findings


def analyze(log_path: Path) -> dict[str, object]:
    raw = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
    text = clean_text(raw)
    lines = text.splitlines()
    failed_tasks = []
    for line in lines:
        match = FAILED_TASK_RE.search(line)
        if match and match.group(1) not in failed_tasks:
            failed_tasks.append(match.group(1))

    block = first_error_block(lines)
    findings = detect_findings(text)
    return {
        "log": str(log_path),
        "exists": log_path.exists(),
        "failed_tasks": failed_tasks,
        "locations": collect_locations(lines),
        "first_error_block": block,
        "findings": [asdict(f) for f in findings],
    }


def render_text(result: dict[str, object]) -> str:
    lines = ["# Build Log Analysis", ""]
    lines.append(f"- log: `{result['log']}`")
    lines.append(f"- exists: {result['exists']}")
    failed_tasks = result.get("failed_tasks") or []
    lines.append(f"- failed_tasks: {', '.join(failed_tasks) if failed_tasks else 'none detected'}")

    locations = result.get("locations") or []
    if locations:
        lines.extend(["", "## Locations"])
        for loc in locations[:10]:
            lines.append(f"- `{loc['file']}:{loc['line']}:{loc['column']}`")

    findings = result.get("findings") or []
    if findings:
        lines.extend(["", "## Findings"])
        for item in findings:
            lines.append(f"- [{item['severity']}] `{item['code']}`: {item['title']}")
            lines.append(f"  evidence: {item['evidence']}")
            lines.append(f"  suggestion: {item['suggestion']}")

    block = result.get("first_error_block") or []
    if block:
        lines.extend(["", "## First Error Block", "", "```text"])
        lines.extend(block[:80])
        lines.append("```")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".", help="Project root containing build.log.")
    parser.add_argument("--log", default=None, help="Explicit build log path.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    project = Path(args.project_root).expanduser().resolve()
    log_path = Path(args.log).expanduser().resolve() if args.log else project / "build.log"
    result = analyze(log_path)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
