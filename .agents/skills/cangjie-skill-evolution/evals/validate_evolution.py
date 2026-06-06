#!/usr/bin/env python3
"""Validate the unified Trace2Skill, SkillX, and XSkill evolution workflow."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


ROUTE_DECISION_FIELDS = ["主路线", "增强模块", "选择理由", "目标形态", "必需产物"]
COMMON_KNOWLEDGE_FIELDS = [
    "知识单元",
    "单元类型",
    "触发条件",
    "做法",
    "证据来源",
    "例外/边界",
    "放置位置",
    "验证方式",
    "验证状态",
    "预期行为变化",
]
EXPERIENCE_FIELDS = [
    "观察状态",
    "动作",
    "结果",
    "适用上下文",
    "适配规则",
    "失效条件",
    "提升条件",
]


def main() -> int:
    payload = _payload()
    workspace = Path(str(payload.get("workspace_dir") or ".")).resolve()
    skill_dir = Path(str(payload.get("skill_dir") or ".")).resolve()
    trace = payload.get("trace") if isinstance(payload.get("trace"), dict) else {}
    runner = str(trace.get("runner") or "")
    case_id = str(payload.get("case_id") or "")

    if runner == "static":
        checks, metrics = _validate_static(skill_dir)
        success_reason = "static three-route orchestration checks passed"
    else:
        validators: dict[str, Callable[[Path, Path, dict[str, Any], dict[str, Any]], tuple[dict[str, bool], dict[str, Any]]]] = {
            "evolve-demo-skill-from-evidence": _validate_trace2skill,
            "organize-single-skill-with-skillx": _validate_skillx_single,
            "govern-skill-library-with-skillx": _validate_skillx_library,
            "separate-ui-skill-and-experience-with-xskill": _validate_xskill_ui,
        }
        validator = validators.get(case_id)
        if validator is None:
            return _emit(0.0, f"unknown real-eval case_id: {case_id}", {"case_id": case_id})
        checks, metrics = validator(workspace, skill_dir, payload, trace)
        success_reason = f"{case_id} checks passed"

    missing = [name for name, passed in checks.items() if not passed]
    reason = success_reason if not missing else "failed checks: " + ", ".join(missing)
    return _emit(1.0 if not missing else 0.0, reason, {**checks, **metrics, "missing": missing})


def _validate_static(skill_dir: Path) -> tuple[dict[str, bool], dict[str, Any]]:
    text = _read(skill_dir / "SKILL.md")
    paper = _read(skill_dir / "references" / "paper-synthesis.md")
    content_real_path = skill_dir / "evals" / "content-real.jsonl"
    discovery_path = skill_dir / "evals" / "discovery.jsonl"
    checks = {
        "version_is_1_2_0": 'version: "1.2.0"' in text,
        "has_execution_modes": "分析评审模式" in text and "实际修改模式" in text,
        "has_route_decision_contract": all(field in text for field in ROUTE_DECISION_FIELDS),
        "has_one_primary_route_policy": "只选择一个主路线" in text and "不得无差别运行全部机制" in text,
        "has_six_stage_contract": all(text.count(marker) >= 6 for marker in ["- 输入：", "- 必须动作：", "- 输出产物：", "- 完成条件：", "- 停止条件："]),
        "has_common_knowledge_contract": all(field in text for field in COMMON_KNOWLEDGE_FIELDS),
        "has_skill_and_tool_contracts": all(marker in text for marker in ["层级", "规划层", "功能层", "原子层", "工具 schema", "参数约束", "失败模式", "实际验证结果"]),
        "has_experience_contract": all(field in text for field in EXPERIENCE_FIELDS),
        "has_trace2skill_main_behavior": "为每条轨迹独立生成局部知识单元" in text and "再集中" in text,
        "has_skillx_main_behavior": "语义聚类" in text and "拆分" in text and "合并" in text and "能力缺口" in text,
        "has_xskill_main_behavior": "跨路径 critique" in text and "技能流" in text and "经验流" in text,
        "has_experience_storage_gate": "`references/experiences.md`" in text and "不得存入 `evals/`" in text,
        "has_experience_adaptation_gate": "依据当前上下文重写后应用" in text and "多个场景重复验证后" in text,
        "accepted_only_gate": "只有 `accepted` 知识单元可以进入目标产物" in text,
        "routes_lint_only": "`cangjie-skill-lint-fix`" in text,
        "paper_has_primary_sources": all(arxiv_id in paper for arxiv_id in ["2603.25158", "2604.04804", "2603.12056"]),
        "paper_uses_xskill_name": "XSkill" in paper and "XSKILL" not in paper,
        "paper_has_route_matrix": "主路线与增强模块矩阵" in paper and "迭代精炼" in paper and "探索扩展" in paper,
        "real_inputs_avoid_hardcoded_commands": _content_real_inputs_avoid_hardcoded_commands(content_real_path),
        "content_real_has_one_case_per_route": _content_real_has_one_case_per_route(content_real_path),
        "discovery_has_single_case": _jsonl_count(discovery_path) == 1,
        "content_basic_removed": not (skill_dir / "evals" / "content-basic.jsonl").exists(),
        "no_root_scripts_dir": not (skill_dir / "scripts").exists(),
    }
    return checks, {
        "route_decision_field_count": sum(field in text for field in ROUTE_DECISION_FIELDS),
        "knowledge_field_count": sum(field in text for field in COMMON_KNOWLEDGE_FIELDS),
        "experience_field_count": sum(field in text for field in EXPERIENCE_FIELDS),
        "content_real_case_count": _jsonl_count(content_real_path),
        "discovery_case_count": _jsonl_count(discovery_path),
    }


def _validate_trace2skill(
    workspace: Path, skill_dir: Path, payload: dict[str, Any], trace: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    demo_dir = workspace / ".agents" / "skills" / "demo"
    skill_text = _read(demo_dir / "SKILL.md")
    output = str(payload.get("output") or "")
    commands = _commands(trace)
    lint = _run_lint(demo_dir, workspace)
    report = _read_json(workspace / "reports" / "lint" / "demo.json")
    text_for_behavior = skill_text + "\n" + output
    has_validation_action = _has_validation_action(text_for_behavior)

    checks = {
        "selected_trace2skill_primary": _contains_all(output, ["主路线", "Trace2Skill"]),
        "reported_per_trace_candidates": _contains_all(output, ["T-S1", "T-F1"]),
        "agent_read_all_evidence": _commands_contain(commands, "success-trace.md", "failure-trace.md", "user-suggestion.md"),
        "agent_ran_skill_lint": "skill-lint" in commands,
        "direct_delivery_rule_removed": "写完 JSON 文件后直接交付" not in skill_text,
        "has_readback_rule": _search(r"(读回|重新读取|再次读取|read.?back)", skill_text),
        "has_validation_action": has_validation_action,
        "accepted_readback_behavior_written": _search(r"(读回|read.?back)", skill_text)
        and has_validation_action
        and "accepted" in output.lower(),
        "accepted_knowledge_written": "accepted" in output.lower() and _search(r"(读回|read.?back)", skill_text),
        "agent_avoided_static_eval": _agent_avoided_static_eval(commands),
        "cache_suggestion_not_promoted": _cache_suggestion_not_promoted(skill_text),
        "pending_or_rejected_reported": _search(r"pending|rejected", output),
        "fixture_evidence_unchanged": _fixture_subtree_unchanged(skill_dir, workspace, "evolve-demo-skill", "evidence"),
        "existing_eval_unchanged": _fixture_file_unchanged(
            skill_dir, workspace, "evolve-demo-skill", ".agents/skills/demo/evals/content-basic.jsonl"
        ),
        "lint_report_generated": _lint_report_passed(report),
        "validator_lint_passed": lint["passed"],
    }
    return checks, _metrics(commands, lint, {"knowledge_fields": sum(field in skill_text for field in COMMON_KNOWLEDGE_FIELDS)})


def _validate_skillx_single(
    workspace: Path, skill_dir: Path, payload: dict[str, Any], trace: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    target = workspace / ".agents" / "skills" / "report-pipeline"
    skill_text = _read(target / "SKILL.md")
    output = str(payload.get("output") or "")
    commands = _commands(trace)
    lint = _run_lint(target, workspace)
    report = _read_json(workspace / "reports" / "lint" / "report-pipeline.json")
    skill_names = _skill_names(workspace / ".agents" / "skills")

    checks = {
        "selected_skillx_primary": "SkillX" in output and _search(r"路线", output),
        "kept_single_skill_shape": _search(r"单(?:个)?\s*Skill", output) and skill_names == ["report-pipeline"],
        "agent_read_skillx_evidence": _commands_contain(commands, "workflow-trace.md", "tool-schema.md"),
        "agent_validated_tool_help": "report_tool.py --help" in commands,
        "agent_ran_skill_lint": "skill-lint" in commands,
        "agent_avoided_static_eval": _agent_avoided_static_eval(commands),
        "has_three_layers": all(marker in skill_text for marker in ["规划层", "功能层", "原子层"]),
        "has_correct_tool_schema": all(flag in skill_text for flag in ["--input", "--output", "--format"]),
        "unsupported_target_not_used_as_valid_command": "--target" not in skill_text
        or _search(r"(不支持|禁止|失败|无效|错误|不要使用|unsupported|invalid).{0,50}--target|--target.{0,50}(不支持|禁止|失败|无效|错误|不要使用|unsupported|invalid)", skill_text),
        "records_single_skill_reason": _search(r"(单 Skill|不拆分|无需拆分|不应拆分)", skill_text + output),
        "fixture_evidence_unchanged": _fixture_subtree_unchanged(skill_dir, workspace, "skillx-single", "evidence"),
        "fixture_tool_unchanged": _fixture_subtree_unchanged(skill_dir, workspace, "skillx-single", "tools"),
        "existing_evals_unchanged": _fixture_subtree_unchanged(
            skill_dir, workspace, "skillx-single", ".agents/skills/report-pipeline/evals"
        ),
        "lint_report_generated": _lint_report_passed(report),
        "validator_lint_passed": lint["passed"],
    }
    return checks, _metrics(commands, lint, {"skill_names": skill_names})


def _validate_skillx_library(
    workspace: Path, skill_dir: Path, payload: dict[str, Any], trace: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    skills_root = workspace / ".agents" / "skills"
    build_dir = skills_root / "release-build"
    inspect_dir = skills_root / "release-inspect"
    build_text = _read(build_dir / "SKILL.md")
    inspect_text = _read(inspect_dir / "SKILL.md")
    inspect_discovery = _read(inspect_dir / "evals" / "discovery.jsonl")
    output = str(payload.get("output") or "")
    commands = _commands(trace)
    lint = _run_lint(skills_root, workspace)
    reports_dir = workspace / "reports" / "lint"
    skill_names = _skill_names(skills_root)

    checks = {
        "selected_skillx_library_primary": _contains_all(output, ["SkillX", "技能库"]) and _search(r"路线", output),
        "agent_read_topology_evidence": "topology-evidence.md" in commands,
        "agent_ran_skill_lint": "skill-lint" in commands,
        "agent_avoided_static_eval": _agent_avoided_static_eval(commands),
        "obsolete_ops_suite_removed": not (skills_root / "ops-suite").exists(),
        "result_has_exact_skill_topology": skill_names == ["release-build", "release-inspect"],
        "merged_build_knowledge": "dist/manifest.json" in build_text,
        "created_independent_inspect_skill": _created_independent_inspect_skill(inspect_dir, inspect_text),
        "records_cross_skill_dependency": "release-build" in inspect_text and "dist/manifest.json" in inspect_text,
        "inspect_has_independent_discovery_eval": '"release-inspect"' in inspect_discovery,
        "inspect_has_content_eval": (inspect_dir / "evals" / "content-basic.jsonl").is_file(),
        "build_evals_preserved": (build_dir / "evals" / "discovery.jsonl").is_file()
        and (build_dir / "evals" / "content-basic.jsonl").is_file(),
        "fixture_evidence_unchanged": _fixture_subtree_unchanged(skill_dir, workspace, "skillx-library", "evidence"),
        "lint_report_generated": _all_lint_reports_passed(
            reports_dir,
            ["release-build.json", "release-inspect.json"],
        ),
        "validator_lint_passed": lint["passed"],
    }
    return checks, _metrics(commands, lint, {"skill_names": skill_names})


def _validate_xskill_ui(
    workspace: Path, skill_dir: Path, payload: dict[str, Any], trace: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    target = workspace / ".agents" / "skills" / "ui-button-diagnose"
    skill_text = _read(target / "SKILL.md")
    experiences = _read(target / "references" / "experiences.md")
    eval_text = "\n".join(_read(path) for path in (target / "evals").glob("*.jsonl"))
    output = str(payload.get("output") or "")
    commands = _commands(trace)
    lint = _run_lint(target, workspace)
    report = _read_json(workspace / "reports" / "lint" / "ui-button-diagnose.json")

    checks = {
        "selected_xskill_primary": _contains_all(output, ["主路线", "XSkill"]),
        "reported_skill_and_experience_flows": _contains_all(output, ["技能流", "经验流"]),
        "agent_read_all_multimodal_evidence": _read_all_multimodal_evidence(commands),
        "agent_ran_skill_lint": "skill-lint" in commands,
        "agent_avoided_static_eval": _agent_avoided_static_eval(commands),
        "stable_flow_uses_multimodal_observation": _search(r"截图|screenshot", skill_text)
        and _search(r"控件树|control tree", skill_text)
        and _search(r"前后|before.{0,20}after|重新观察|再次观察", skill_text),
        "skill_loads_and_adapts_experience": _skill_loads_and_adapts_experience(skill_text, output),
        "experience_file_has_complete_contract": _experience_contract_complete(experiences, output),
        "experience_is_verified_and_contextual": "accepted" in experiences
        and _search(r"overlay|遮罩", experiences)
        and _search(r"enabled|启用", experiences),
        "overlay_action_not_promoted_to_main_skill": not _search(
            r"(?m)^\s*(?:\d+\.|[-*])\s*(?:(?:必须|总是|每次|先|直接)\s*)?(?:关闭|解除|移除|dismiss).{0,50}(?:遮罩|overlay)",
            skill_text,
        ),
        "experience_not_stored_in_evals": not _search(r"overlay|遮罩", eval_text),
        "experience_not_unconditional": not _search(r"always|总是|每次都", experiences),
        "fixture_evidence_unchanged": _fixture_subtree_unchanged(skill_dir, workspace, "xskill-ui", "evidence"),
        "lint_report_generated": _lint_report_passed(report),
        "validator_lint_passed": lint["passed"],
    }
    return checks, _metrics(commands, lint, {"experience_chars": len(experiences)})


def _commands(trace: dict[str, Any]) -> str:
    usage = trace.get("usage") if isinstance(trace.get("usage"), dict) else {}
    values = usage.get("codex_tool_commands")
    if not isinstance(values, list):
        return ""
    return "\n".join(str(value) for value in values).lower()


def _commands_contain(commands: str, *names: str) -> bool:
    return all(name.lower() in commands for name in names)


def _agent_avoided_static_eval(commands: str) -> bool:
    return not _search(r"--runner\s+static|runner\s+static|\.static\.json|-static\.json", commands)


def _created_independent_inspect_skill(inspect_dir: Path, inspect_text: str) -> bool:
    if not inspect_dir.is_dir():
        return False
    has_inspection_capability = _search(r"检查|巡检|inspect|audit|verify|validate", inspect_text)
    has_artifact_context = _search(r"发布产物|artifact|dist/manifest\.json|manifest", inspect_text)
    return has_inspection_capability and has_artifact_context


def _cache_suggestion_not_promoted(skill_text: str) -> bool:
    for match in re.finditer(r"delete all caches|删除全部缓存|删除所有缓存|删(?:除|掉).{0,8}缓存", skill_text, flags=re.IGNORECASE):
        start = max(0, match.start() - 80)
        end = min(len(skill_text), match.end() + 80)
        context = skill_text[start:end]
        if _search(r"不要|不得|禁止|不能|不应|未验证|缺少证据|pending|rejected|without evidence|unverified|do not", context):
            continue
        return False
    return True


def _skill_loads_and_adapts_experience(skill_text: str, output: str) -> bool:
    names_experience_stream = _search(r"references/experiences\.md|experiences\.md|经验流|经验库|经验文件", skill_text)
    says_when_to_load = _search(r"读取|加载|查阅|检索|按需|何时|when to (?:read|load|retrieve)", skill_text)
    says_contextual_adaptation = _search(r"当前.{0,20}(?:上下文|状态|截图|控件树)|上下文.{0,30}(?:适配|重写|改写)|适配|重写|改写|adapt", skill_text)
    artifact_passed = names_experience_stream and says_when_to_load and says_contextual_adaptation
    output_confirms = _contains_all(output, ["references/experiences.md"]) and _search(
        r"经验读取时机|读取.*经验|加载.*经验|当前上下文.*适配|按当前上下文适配|context.*adapt",
        output,
    )
    return artifact_passed or output_confirms


def _experience_contract_complete(experiences: str, output: str) -> bool:
    field_groups = [
        ["知识单元", "knowledge unit", "unit"],
        ["单元类型", "unit type", "type"],
        ["证据来源", "evidence source", "evidence"],
        ["验证状态", "validation status", "status", "accepted"],
        ["观察状态", "observed state", "observation", "state"],
        ["动作", "action"],
        ["结果", "outcome", "result"],
        ["适用上下文", "applicable context", "context"],
        ["适配规则", "adaptation rule", "adapt", "rewrite"],
        ["失效条件", "invalid", "失效", "failure", "stop condition"],
        ["提升条件", "promotion", "promote", "提升"],
    ]
    lowered = experiences.lower()
    hits = sum(1 for group in field_groups if any(marker.lower() in lowered for marker in group))
    if hits == len(field_groups):
        return True
    minimum_artifact = (
        "accepted" in lowered
        and _search(r"overlay|遮罩", experiences)
        and _search(r"enabled|启用|可用", experiences)
        and hits >= 8
    )
    output_confirms = _search(r"完整.*accepted.*经验单元|accepted.*经验单元", output)
    return minimum_artifact and output_confirms


def _has_validation_action(text: str) -> bool:
    subject = r"(关键字段|必需字段|必填|required|items|非空|格式|key|键)"
    action = r"(验证|校验|确认|检查|check|validate|parse|解析)"
    return _search(subject + r".{0,80}" + action, text) or _search(action + r".{0,80}" + subject, text)


def _read_all_multimodal_evidence(commands: str) -> bool:
    read_text_evidence = _commands_contain(commands, "rollout-clear.md", "rollout-overlay.md", "feedback.md")
    read_json_evidence = _commands_contain(commands, "control-tree-clear.json", "control-tree-overlay.json") or (
        "evidence" in commands and "*.json" in commands and "get-content" in commands
    )
    read_svg_evidence = _commands_contain(commands, "screenshot-clear.svg", "screenshot-overlay.svg") or (
        "evidence" in commands and "*.svg" in commands and "get-content" in commands
    )
    return read_text_evidence and read_json_evidence and read_svg_evidence


def _content_real_inputs_avoid_hardcoded_commands(path: Path) -> bool:
    blocked_patterns = [
        r"\bNew-Item\b",
        r"skill-lint\s+--path",
        r"--format\s+json\s+--out",
        r"python\s+tools[/\\]report_tool\.py\s+--help",
    ]
    rows = _read_jsonl(path)
    if not rows:
        return False
    for row in rows:
        text = str(row.get("input") or "")
        if any(_search(pattern, text) for pattern in blocked_patterns):
            return False
    return True


def _content_real_has_one_case_per_route(path: Path) -> bool:
    expected_ids = [
        "evolve-demo-skill-from-evidence",
        "govern-skill-library-with-skillx",
        "separate-ui-skill-and-experience-with-xskill",
    ]
    rows = _read_jsonl(path)
    return [str(row.get("id") or "") for row in rows] == expected_ids


def _jsonl_count(path: Path) -> int:
    return len(_read_jsonl(path))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return rows
    for line in lines:
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            return []
        if not isinstance(value, dict):
            return []
        rows.append(value)
    return rows


def _skill_names(root: Path) -> list[str]:
    if not root.is_dir():
        return []
    return sorted(path.name for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())


def _run_lint(target: Path, workspace: Path) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            ["skill-lint", "--path", str(target), "--format", "json"],
            cwd=workspace,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"passed": False, "output": str(exc)}

    output = (proc.stdout or "") + "\n" + (proc.stderr or "")
    try:
        report = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        report = {}
    return {"passed": proc.returncode == 0 and _lint_report_passed(report), "output": output}


def _fixture_file_unchanged(skill_dir: Path, workspace: Path, fixture_name: str, relative: str) -> bool:
    source = skill_dir / "fixtures" / fixture_name / relative
    target = workspace / relative
    return source.is_file() and target.is_file() and source.read_bytes() == target.read_bytes()


def _fixture_subtree_unchanged(skill_dir: Path, workspace: Path, fixture_name: str, relative: str) -> bool:
    source_root = skill_dir / "fixtures" / fixture_name / relative
    target_root = workspace / relative
    if not source_root.is_dir() or not target_root.is_dir():
        return False
    source_files = sorted(path.relative_to(source_root) for path in source_root.rglob("*") if path.is_file())
    target_files = sorted(path.relative_to(target_root) for path in target_root.rglob("*") if path.is_file())
    if source_files != target_files:
        return False
    return all((source_root / relative_path).read_bytes() == (target_root / relative_path).read_bytes() for relative_path in source_files)


def _lint_report_passed(report: Any) -> bool:
    if not isinstance(report, dict):
        return False
    summary = report.get("summary") if isinstance(report.get("summary"), dict) else {}
    return summary.get("errors") == 0 and summary.get("warnings") == 0


def _all_lint_reports_passed(root: Path, names: list[str]) -> bool:
    return all(_lint_report_passed(_read_json(root / name)) for name in names)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _payload() -> dict[str, Any]:
    try:
        value = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        value = {}
    return value if isinstance(value, dict) else {}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _search(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


def _contains_all(text: str, markers: list[str]) -> bool:
    lowered = text.lower()
    return all(marker.lower() in lowered for marker in markers)


def _metrics(commands: str, lint: dict[str, Any], extra: dict[str, Any]) -> dict[str, Any]:
    return {
        "commands_tail": commands[-2500:],
        "lint_tail": str(lint.get("output") or "")[-1500:],
        **extra,
    }


def _emit(score: float, reason: str, metrics: dict[str, Any]) -> int:
    print(json.dumps({"score": score, "reason": reason, "metrics": metrics}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
