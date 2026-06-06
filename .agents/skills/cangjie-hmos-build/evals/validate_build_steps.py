import json
import re
import sys
from pathlib import Path


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    case_id = str(payload.get("case_id") or "")
    output = str(payload.get("output") or "")
    workspace_dir = Path(str(payload.get("workspace_dir") or "")).resolve()

    checks = {
        "success-build-executes-script": validate_success,
        "failure-uses-evolution-then-reruns": validate_evolution_failure,
        "startup-path-missing-checks-constants": validate_path_missing,
        "insufficient-log-asks-user-devEco": validate_insufficient_log,
    }.get(case_id)

    if checks is None:
        finish([f"unknown case_id: {case_id}"], {"case_id": case_id})
        return

    passed, failed, metrics = checks(workspace_dir, output)
    score = len(passed) / (len(passed) + len(failed)) if passed or failed else 0.0
    print(
        json.dumps(
            {
                "score": score,
                "reason": "ok" if not failed else "missing: " + ", ".join(failed),
                "metrics": {
                    "case_id": case_id,
                    "passed": passed,
                    "failed": failed,
                    **metrics,
                },
            },
            ensure_ascii=False,
        )
    )


def validate_success(workspace: Path, output: str) -> tuple[list[str], list[str], dict[str, object]]:
    log = read_text(workspace / "build.log")
    invocations = read_jsonl(workspace / "build.invocations.jsonl")
    hap = workspace / "dist" / "entry-default.hap"

    checks = [
        ("执行 build.py", bool(invocations)),
        ("生成 build.log", log is not None),
        ("构建三阶段顺序正确", contains_in_order(log or "", ["ohpm install", "SyncCangjieResource", "assembleHap"])),
        ("日志判定 BUILD SUCCESSFUL", "BUILD SUCCESSFUL" in (log or "")),
        ("生成模拟 HAP 产物", hap.is_file()),
        ("回复引用 build.log", search(r"build\.log|构建日志", output)),
        ("回复基于成功日志判定", search(r"BUILD SUCCESSFUL|构建成功|成功", output)),
        ("回复包含成功沉淀要求", search(r"Evolution\.md|cangjie-hmos-evolution|沉淀", output)),
    ]
    passed, failed = split_checks(checks)
    return passed, failed, {
        "invocation_count": len(invocations),
        "build_log_chars": len(log or ""),
        "hap_exists": hap.is_file(),
    }


def validate_evolution_failure(workspace: Path, output: str) -> tuple[list[str], list[str], dict[str, object]]:
    final_log = read_text(workspace / "build.log")
    attempts = read_text(workspace / "build.attempts.log") or ""
    invocations = read_jsonl(workspace / "build.invocations.jsonl")
    fixed = read_text(workspace / "config" / "fixed.txt")

    checks = [
        ("先执行构建并产生失败日志", len(invocations) >= 1 and "EVC001" in attempts),
        ("命中 Evolution.md 记录后修复", fixed is not None and "resource mapping synced" in fixed),
        ("修复后重新执行构建", len(invocations) >= 2),
        ("失败后重建最终成功", "EVC001" in attempts and "BUILD SUCCESSFUL" in attempts and "BUILD SUCCESSFUL" in (final_log or "")),
        ("回复说明读取或依据 build.log", search(r"build\.log|构建日志|日志", output)),
        ("回复说明 Evolution.md 命中", search(r"Evolution\.md|已有记录|历史记录|经验记录", output)),
        ("回复说明 EVC001 根因或修复", search(r"EVC001|resource mapping|资源映射|generated resource", output)),
        ("回复说明已重建验证", search(r"重建|重新.*构建|再次.*构建|rerun|验证", output)),
    ]
    passed, failed = split_checks(checks)
    return passed, failed, {
        "invocation_count": len(invocations),
        "fixed_file": fixed is not None,
        "attempt_log_chars": len(attempts),
    }


def validate_path_missing(workspace: Path, output: str) -> tuple[list[str], list[str], dict[str, object]]:
    log = read_text(workspace / "build.log") or ""
    invocations = read_jsonl(workspace / "build.invocations.jsonl")

    checks = [
        ("执行 build.py", bool(invocations)),
        ("未误判构建成功", "BUILD SUCCESSFUL" not in log and not search(r"构建成功|BUILD SUCCESSFUL", output)),
        ("回复包含路径不存在报错", search(r"路径不存在|不存在|DevEco Studio|Cangjie SDK", output)),
        ("回复要求检查 build.py 顶部常量", search(r"build\.py.*顶部|顶部.*常量|DEVECO_HOME|DEVECO_HOME_WINDOWS|DEVECO_HOME_LINUX|DEVECO_HOME_MACOS", output)),
        ("未编造业务代码修复", not search(r"entry/src|修改.*业务代码|业务代码.*修改|修改.*页面|修改.*组件", output)),
    ]
    passed, failed = split_checks(checks)
    return passed, failed, {
        "invocation_count": len(invocations),
        "build_log_chars": len(log),
    }


def validate_insufficient_log(workspace: Path, output: str) -> tuple[list[str], list[str], dict[str, object]]:
    log = read_text(workspace / "build.log") or ""
    invocations = read_jsonl(workspace / "build.invocations.jsonl")
    fix_marker = workspace / "config" / "fixed.txt"

    checks = [
        ("执行 build.py", bool(invocations)),
        ("生成泛化失败 build.log", "NO_ACTIONABLE_DIAGNOSTIC" in log),
        ("未误判构建成功", "BUILD SUCCESSFUL" not in log and not search(r"构建成功|BUILD SUCCESSFUL", output)),
        ("回复说明日志信息不足", search(r"日志.*不足|信息不足|无法定位|无法判断|缺少.*报错|insufficient|cannot locate|not enough", output)),
        ("请求用户在 DevEco Studio 重建", search(r"DevEco Studio.*重建|DevEco.*重新.*构建|在.*DevEco|rebuild.*DevEco|DevEco.*rebuild", output)),
        ("请求用户提供完整报错或日志", search(r"提供.*报错|提供.*日志|完整.*错误|完整.*日志|provide.*(?:error|log)|complete.*(?:error|log)", output)),
        ("未擅自创建修复文件", not fix_marker.exists()),
    ]
    passed, failed = split_checks(checks)
    return passed, failed, {
        "invocation_count": len(invocations),
        "build_log_chars": len(log),
        "fix_marker_exists": fix_marker.exists(),
    }


def split_checks(checks: list[tuple[str, bool]]) -> tuple[list[str], list[str]]:
    passed = [label for label, ok in checks if ok]
    failed = [label for label, ok in checks if not ok]
    return passed, failed


def read_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def read_jsonl(path: Path) -> list[dict[str, object]]:
    text = read_text(path)
    if not text:
        return []
    rows = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(item, dict):
            rows.append(item)
    return rows


def contains_in_order(text: str, needles: list[str]) -> bool:
    index = -1
    for needle in needles:
        next_index = text.find(needle, index + 1)
        if next_index == -1:
            return False
        index = next_index
    return True


def search(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


def finish(failures: list[str], metrics: dict[str, object]) -> None:
    print(
        json.dumps(
            {
                "score": 0.0,
                "reason": "; ".join(failures),
                "metrics": metrics,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
