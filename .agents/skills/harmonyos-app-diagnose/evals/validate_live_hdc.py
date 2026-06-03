import json
import re
import sys
from pathlib import Path
from typing import Any


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    output = str(payload.get("output") or "")
    workspace = Path(str(payload.get("workspace_dir") or "")).resolve()
    trace = payload.get("trace") if isinstance(payload.get("trace"), dict) else {}
    usage = trace.get("usage") if isinstance(trace.get("usage"), dict) else {}

    top_commands = _string_list(usage.get("codex_tool_commands"))
    top_commands.extend(_string_list(usage.get("tool_commands")))
    top_commands.extend(_string_list(trace.get("tool_commands")))
    tool_calls = trace.get("tool_calls") if isinstance(trace.get("tool_calls"), list) else []
    tool_names = [str(item.get("name") or "") for item in tool_calls if isinstance(item, dict)]

    checks: list[tuple[str, bool]] = []
    notes: list[str] = []

    if top_commands:
        checks.extend(
            [
                ("真实检查设备连接", _any_command(top_commands, [r"\bhdc\s+list\s+targets\b"])),
                ("真实采集截图", _any_command(top_commands, [r"snapshot_display", r"screenCap", r"\bscreencap\b"])),
                ("真实拉取设备文件", _any_command(top_commands, [r"\bhdc\s+file\s+recv\b"])),
                ("真实采集控件树", _any_command(top_commands, [r"\bhdc\s+shell\s+uitest\s+dumpLayout\b"])),
                ("真实清空 hilog", _any_command(top_commands, [r"\bhdc\s+shell\s+\"?hilog\s+-r\"?"])),
                ("真实导出 hilog", _any_command(top_commands, [r"\bhdc\s+shell\s+\"?hilog\s+-x", r"\bhilog\s+-x\b"])),
                ("真实提取错误 hilog", _any_command(top_commands, [r"\bhilog\s+-L\s+[EFW]", r"hilog_error\.txt"])),
            ]
        )
    else:
        command_tool_names = {"shell_command", "hdc", "python", "python3", "bash", "ls", "wc", "cat"}
        checks.append(("真实 agent 调用命令工具", any(name in command_tool_names for name in tool_names)))
        notes.append("agent command strings unavailable in validator trace; checking shell tool evidence and produced artifacts")

    out_dir = workspace / "ui_capture_output"
    screenshot = _first_nonempty(
        [
            out_dir / "screenshot.png",
            out_dir / "screenshot.jpg",
            out_dir / "screenshot.jpeg",
            *sorted(out_dir.glob("*screen*.png")),
            *sorted(out_dir.glob("*screen*.jpg")),
            *sorted(out_dir.glob("*screen*.jpeg")),
        ]
    )
    layout = _first_nonempty([out_dir / "layout.json", *sorted(out_dir.glob("*layout*.json"))])
    summary_or_report = _first_nonempty(
        [
            out_dir / "ui_summary.md",
            out_dir / "diagnosis_report.md",
            workspace / "diagnosis_report.md",
            *sorted(out_dir.glob("*report*.md")),
        ]
    )
    full_hilog = _first_nonempty([out_dir / "hilog_full.txt", *sorted(out_dir.glob("*full*hilog*.txt"))])
    error_hilog = _first_nonempty([out_dir / "hilog_error.txt", *sorted(out_dir.glob("*error*hilog*.txt"))])
    any_hilog = _first_nonempty([full_hilog, error_hilog, *sorted(out_dir.glob("*hilog*.txt"))])

    checks.extend(
        [
            ("截图产物非空", screenshot is not None),
            ("控件树产物非空", layout is not None),
            ("摘要或诊断报告非空", summary_or_report is not None),
            ("hilog 产物非空", any_hilog is not None),
            ("错误 hilog 或全量 hilog 非空", error_hilog is not None or full_hilog is not None),
        ]
    )

    if layout is not None:
        checks.append(("控件树 JSON 可解析", _json_file_ok(layout)))

    output_checks = {
        "输出包含截图证据": [r"截图", r"screenshot"],
        "输出包含控件树证据": [r"控件树", r"layout"],
        "输出包含 hilog 证据": [r"hilog", r"日志"],
        "输出包含三重验证结论": [r"三重验证", r"交叉验证", r"截图.*控件树.*(?:hilog|日志)", r"控件树.*截图.*(?:hilog|日志)"],
        "输出包含当前状态": [r"当前状态", r"界面.*正常", r"界面.*异常", r"运行.*健康", r"前台"],
        "输出包含下一步建议": [r"迭代建议", r"修复", r"下一步", r"建议"],
    }
    for label, patterns in output_checks.items():
        checks.append((label, any(_search(pattern, output) for pattern in patterns)))

    mock_hit = _search(r"\bmock\b|模拟\s*hdc|伪造|fake\s+hdc", output)
    checks.append(("未声明使用 mock hdc", not mock_hit))

    passed = [label for label, ok in checks if ok]
    missing = [label for label, ok in checks if not ok]
    score = len(passed) / len(checks) if checks else 0.0

    print(
        json.dumps(
            {
                "score": score,
                "reason": "ok" if not missing else "missing: " + ", ".join(missing),
                "metrics": {
                    "passed": passed,
                    "missing": missing,
                    "notes": notes,
                    "top_command_count": len(top_commands),
                    "tool_names": tool_names,
                    "screenshot": _rel(workspace, screenshot),
                    "layout": _rel(workspace, layout),
                    "summary_or_report": _rel(workspace, summary_or_report),
                    "full_hilog": _rel(workspace, full_hilog),
                    "error_hilog": _rel(workspace, error_hilog),
                },
            },
            ensure_ascii=False,
        )
    )


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if isinstance(item, str)]


def _any_command(commands: list[str], patterns: list[str]) -> bool:
    return any(any(_search(pattern, command) for pattern in patterns) for command in commands)


def _search(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


def _first_nonempty(paths: list[Path | None]) -> Path | None:
    for path in paths:
        if path is not None and path.is_file() and path.stat().st_size > 0:
            return path
    return None


def _json_file_ok(path: Path) -> bool:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return False
    return True


def _rel(workspace: Path, path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.relative_to(workspace))
    except ValueError:
        return str(path)


if __name__ == "__main__":
    main()
