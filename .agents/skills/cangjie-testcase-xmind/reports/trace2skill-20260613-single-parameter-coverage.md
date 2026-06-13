# Trace2Skill Governance: cangjie-testcase-xmind Single-Parameter Coverage

- target_skill: `cangjie-testcase-xmind`
- governance_skill: `cangjie-trace2skill-evolution`
- generated_at: `2026-06-13`
- rollout_root: `.agents/skills/cangjie-rollout-collector/records/rollouts/cangjie-testcase-xmind`
- write_scope: target skill files only; rollout records were not modified
- user_authorization: user explicitly asked to fix and record detailed governance steps

## 1. Input And Ground Truth Gate

Read 3 rollout records and grouped them by `target_skill=cangjie-testcase-xmind`.
All records passed the required yi* gate because each had `ground_truth_status: provided`, `outcome_source: ground_truth`, `adjudicated_outcome`, and `### Ground Truth (yi*)`.

| task_id | rollout_id | trace_outcome | adjudicated_outcome | conflict | decision evidence |
| --- | --- | --- | --- | --- | --- |
| `ability_access_ctrl_testcase_xmind` | `cangjie-testcase-xmind-20260613-100839-001` | `partial` | `partial` | no | `单参数测试` did not create per-parameter nodes with `有效等价类`, `无效等价类`, `边界值`, and `特殊值`. |
| `abilitykit-error-observer-xmind` | `cangjie-testcase-xmind-20260613-105118-001` | `not_verified` | `partial` | yes | `ErrorObserver.init` lacked `onUnhandledException` / `onException` parameter hierarchy and equivalence-class discussion. |
| `error_manager_testcase_xmind` | `cangjie-testcase-xmind-20260613-111744-001` | `not_verified` | `partial` | yes | `测试覆盖` lacked concrete parameter nodes and equivalence-class discussion under `单参数测试`. |

Gate summary:

- ground_truth provided: 3
- invalid_rollout_schema: 0
- outcome_conflict: 2
- accepted evidence cluster: repeated high-confidence user adjudication of the same single-parameter hierarchy gap

## 2. Phase 1 Memory Items

```json
[
  {
    "id": "M-cangjie-testcase-xmind-20260613-100839-001-001",
    "type": "failure",
    "content": "参数化 API 的单参数测试必须按参数名展开四类分类节点。",
    "condition": "生成 testcase JSON 和 XMind 测试覆盖节点时",
    "boundary": "无参数 API 使用 不涉及 叶子",
    "source_rollout": "cangjie-testcase-xmind-20260613-100839-001",
    "evidence": "Ground Truth: context 等参数未展开有效等价类、无效等价类、边界值、特殊值。",
    "status": "accepted"
  },
  {
    "id": "M-cangjie-testcase-xmind-20260613-105118-001-001",
    "type": "failure",
    "content": "只抽查根节点和 Pair-wise 不足以证明单参数覆盖完整。",
    "condition": "XMind content.xml 抽查阶段",
    "boundary": "抽查不能替代 validator，但可作为产物 sanity check",
    "source_rollout": "cangjie-testcase-xmind-20260613-105118-001",
    "evidence": "Ground Truth: T026 only confirmed root/basic nodes and Pair-wise case; single-parameter parameter nodes were not observed.",
    "status": "accepted"
  },
  {
    "id": "M-cangjie-testcase-xmind-20260613-111744-001-001",
    "type": "failure",
    "content": "现有 schema 通过不代表单参数测试层级满足用户验收。",
    "condition": "validate_testcase_xmind_json.py 只校验固定节点、case shape 和 Pair-wise 时",
    "boundary": "需要配套单参数层级 gate 才能变成硬约束",
    "source_rollout": "cangjie-testcase-xmind-20260613-111744-001",
    "evidence": "Generated JSON/XMind passed validation and content.xml checks, but user adjudicated partial for missing 单参数测试 hierarchy.",
    "status": "accepted"
  }
]
```

## 3. Local Patch Items

```json
[
  {
    "patch_id": "P-100839-001",
    "source_rollout": "cangjie-testcase-xmind-20260613-100839-001",
    "analyst_type": "error",
    "memory_ids": ["M-cangjie-testcase-xmind-20260613-100839-001-001"],
    "target_file": "SKILL.md",
    "target_section": "Workflow / JSON Design Rules",
    "operation": "replace",
    "anchor": "Pair-wise workflow before validation",
    "new_content": "Generate 单参数测试 -> 参数名 -> 四类分类 before Pair-wise.",
    "status": "accepted"
  },
  {
    "patch_id": "P-105118-001",
    "source_rollout": "cangjie-testcase-xmind-20260613-105118-001",
    "analyst_type": "error",
    "memory_ids": ["M-cangjie-testcase-xmind-20260613-105118-001-001"],
    "target_file": "references/xmind-format.md",
    "target_section": "Required Tree / Single-Parameter Coverage",
    "operation": "insert_after",
    "anchor": "## Interface Details",
    "new_content": "Document required 单参数测试 parameter and category hierarchy.",
    "status": "accepted"
  },
  {
    "patch_id": "P-111744-001",
    "source_rollout": "cangjie-testcase-xmind-20260613-111744-001",
    "analyst_type": "error",
    "memory_ids": ["M-cangjie-testcase-xmind-20260613-111744-001-001"],
    "target_file": "scripts/validate_testcase_xmind_json.py",
    "target_section": "validate()",
    "operation": "insert_after",
    "anchor": "walk_testcases(coverage, f\"测试覆盖.{api}\", errors)",
    "new_content": "Add validate_single_parameter() gate.",
    "status": "accepted"
  }
]
```

Pending local observations:

- Windows PowerShell pipe UTF-8 guard remains pending. It was clearly observed in one rollout but is environmental, so it was not promoted into the target skill main workflow.
- User feedback being misread as a new modification request is rejected for this target skill; it belongs to rollout collection/session handling, not testcase XMind generation.

## 4. Programmatic Precheck

Checked anchors before writing:

- `SKILL.md`: Workflow step 2, Pair-wise step, `## JSON Design Rules`, `## Practical Defaults`
- `references/xmind-format.md`: `## Interface Details`, `## Testcase Nodes`
- `scripts/validate_testcase_xmind_json.py`: existing `validate()` flow and `walk_testcases(...)` call

Precheck result:

- stale: 0
- conflict: 0
- broken memory_ids: 0
- create/link atomic pairs: not applicable

## 5. Consolidated Patch Applied

Applied accepted changes only:

1. `SKILL.md`
   - Inserted a workflow step requiring `单参数测试 -> 参数名 -> 有效等价类 / 无效等价类 / 边界值 / 特殊值` before Pair-wise.
   - Added JSON design rules forbidding flat testcase objects directly under `单参数测试`.
   - Updated validator description and practical defaults.
2. `references/xmind-format.md`
   - Expanded the required tree under `单参数测试`.
   - Added `Single-Parameter Coverage` rules for parameterized and no-parameter APIs.
3. `scripts/validate_testcase_xmind_json.py`
   - Added `SINGLE_PARAMETER_CATEGORIES`.
   - Added `has_testcase_object()`, `extract_parameter_names()`, and `validate_single_parameter()`.
   - Wired `validate_single_parameter()` into `validate()` after testcase shape checking and before Pair-wise checking.

## 6. Verification

Static/script verification:

```text
python -m py_compile .agents\skills\cangjie-testcase-xmind\scripts\validate_testcase_xmind_json.py .agents\skills\cangjie-testcase-xmind\scripts\common.py
=> exit 0
```

Isolated in-memory validator checks:

```text
positive parameterized API with 单参数测试 -> p -> 有效等价类/无效等价类/边界值/特殊值
=> positive_errors []

negative flat 单参数测试 with testcase directly under 单参数测试
=> detected "missing parameter node p" and "unexpected node"

no-parameter API with 单参数测试: { "不涉及": "" }
=> no_param_errors []
```

Historical artifact regression:

```text
python -X utf8 ...validate_testcase_xmind_json.py outputs\testcase-xmind\ability_access_ctrl\ability_access_ctrl_testcase.json
=> expected failure; detects flat testcase objects under 单参数测试 and missing parameter nodes.

python -X utf8 ...validate_testcase_xmind_json.py outputs\testcase-xmind\error_manager\error_manager_testcase.json
=> expected failure; detects missing four category nodes under eventType/observer/observerId.

python -X utf8 ...validate_testcase_xmind_json.py outputs\testcase-xmind\error_observer\abilitykit_error_observer_testcase.json
=> Validation passed.
```

Skill lint:

```text
skill-lint --path .agents\skills\cangjie-testcase-xmind
=> passed; errors 0, warnings 0
```

## 7. Decision Summary

- accepted: 3 applied edits across `SKILL.md`, `references/xmind-format.md`, and `scripts/validate_testcase_xmind_json.py`.
- pending: 1 environmental UTF-8 pipe guard; not written to main rules.
- rejected: 1 process observation about user feedback handling; outside this skill boundary.
- stale/conflict: 0.
- ground truth: provided 3, invalid_rollout_schema 0, outcome_conflict 2.

## 8. Remaining Risk

- The new validator intentionally makes old flat `单参数测试` artifacts fail. This is expected and matches the user adjudicated rollout gaps.
- Real agent eval was not run in this pass; validation used py_compile, direct validator checks, historical artifact regression, and skill-lint.
