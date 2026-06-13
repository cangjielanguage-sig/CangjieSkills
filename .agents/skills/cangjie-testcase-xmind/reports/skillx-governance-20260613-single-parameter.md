# SkillX Governance: cangjie-testcase-xmind 单参数覆盖治理

- target_skill: `cangjie-testcase-xmind`
- extraction_epoch: `E1`
- generated_at: `2026-06-13`
- governance_skill: `cangjie-skillx-layered-refinement`
- rollout_root: `.agents/skills/cangjie-rollout-collector/records/rollouts/cangjie-testcase-xmind`
- update_scope: target skill files only; original rollout records were not modified
- follow_up_adjustment: per user request, ignore `evals/content-basic.jsonl`; remove the validator executable gate and fixture files from this pass

## 1. 输入分组与 Gate

读取目标 skill 目录下的 3 条 rollout record，按 `target_skill=cangjie-testcase-xmind` 分组后进入 yi* gate。

| task_id | rollout_id | gate | trace_outcome | adjudicated_outcome | conflict | ground truth gap |
| --- | --- | --- | --- | --- | --- | --- |
| `ability_access_ctrl_testcase_xmind` | `cangjie-testcase-xmind-20260613-100839-001` | passed | `partial` | `partial` | no | `单参数测试` 未按每个参数建立参数节点，并展开有效等价类、无效等价类、边界值、特殊值 |
| `abilitykit-error-observer-xmind` | `cangjie-testcase-xmind-20260613-105118-001` | passed | `not_verified` | `partial` | yes | `ErrorObserver.init` 等接口下缺少 `onUnhandledException`、`onException` 参数节点与等价类讨论 |
| `error_manager_testcase_xmind` | `cangjie-testcase-xmind-20260613-111744-001` | passed | `not_verified` | `partial` | yes | `测试覆盖` 节点中的单参数测试缺失具体参数节点，以及有效等价类、无效等价类等讨论 |

Gate 结果：

- provided ground truth: 3
- invalid_rollout_schema: 0
- trace/adjudicated conflict: 2
- usable evidence: repeated high-confidence partial gaps; used for failure-prevention and validator strengthening

## 2. Tool Summary

对每条 rollout 的可复用事实做压缩：

1. 所有任务都按当前 skill 流程生成 JSON，再运行 `scripts/validate_testcase_xmind_json.py`，最后转换为 `.xmind` 并抽查 `content.xml`。
2. 校验器能够检查固定节点、testcase shape 和 Pair-wise 覆盖，但没有检查 `单参数测试` 的参数节点与四类分类节点。
3. 用户裁定结果均为 `partial`，共同原因不是转换失败，而是内容结构缺失：`测试覆盖 -> {接口名} -> 单参数测试` 被写成过平的 testcase 列表，或没有展开参数维度。
4. 现有 `references/xmind-format.md` 已要求 `接口列表 -> 参数 -> 取值范围` 使用 `有效等价类 / 无效等价类 / 边界值 / 特殊值`，但没有把同样的层级明确要求到 `测试覆盖 -> 单参数测试`。
5. Per follow-up instruction, `evals/content-basic.jsonl` is ignored in this pass and is not used as governance evidence or validation input.

## 3. Plan Extract

候选 planning skill：

```json
{
  "level": "planning",
  "name": "生成参数化 API 测试脑图时先完成单参数覆盖树",
  "document": "输入为结构化 API 信息和参数取值范围；输出为符合固定 XMind schema 的 testcase JSON。约束：先生成单参数测试层级，再生成 Pair-wise 多参数组合，最后统一校验和转换。",
  "content": "1. 读取接口列表、参数、返回值、异常和权限信息。2. 为每个参数化 API 建立 单参数测试 -> 参数名 -> 有效等价类/无效等价类/边界值/特殊值。3. 每个适用分类下写 concrete testcase 对象；无适用值时使用 不涉及 叶子。4. 再按 Pair-wise 规则生成 多参数组合。5. 运行 validate_testcase_xmind_json.py，只有通过后才转换为 .xmind。",
  "tools": ["scripts/validate_testcase_xmind_json.py", "scripts/generate_pairwise_cases.py", "scripts/json_to_xmind.py"],
  "source_rollouts": [
    "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#S50-S56",
    "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#S20-S26",
    "error_manager_testcase_xmind/cangjie-testcase-xmind-20260613-111744-001#S25-S28"
  ],
  "operation": "modify",
  "status": "accepted",
  "target_placement": "SKILL.md Workflow / JSON Design Rules / Practical Defaults",
  "reason": "三条 high-confidence ground truth 都指出同一结构缺口；该修改将已验证缺口前移为生成步骤和设计规则。",
  "metadata": {
    "cluster_id": "C001",
    "extraction_epoch": "E1",
    "similarity_basis": "llm",
    "source_steps": ["S20", "S25", "S50"]
  }
}
```

## 4. Functional Extract

候选 functional skill：

```json
{
  "level": "functional",
  "name": "校验单参数测试层级",
  "document": "Parameters: full testcase JSON. Outputs: validation errors when 单参数测试 is flat, misses parameter nodes, misses category nodes, or contains categories without testcase objects. Notes: no extra dependency; reuse existing validator style.",
  "content": "1. 从 接口列表.{api}.参数 提取参数名。2. 无参数 API 要求 测试覆盖.{api}.单参数测试 为 不涉及。3. 有参数 API 要求 单参数测试 是对象，且包含每个参数名。4. 每个参数节点必须包含 有效等价类、无效等价类、边界值、特殊值。5. 每个分类必须包含 testcase object 或合法 不涉及 叶子。6. 将错误合并到现有 validate() 错误列表。",
  "tools": ["scripts/validate_testcase_xmind_json.py"],
  "source_rollouts": [
    "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#Ground Truth",
    "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#Ground Truth",
    "error_manager_testcase_xmind/cangjie-testcase-xmind-20260613-111744-001#Ground Truth"
  ],
  "operation": "modify",
  "status": "pending",
  "target_placement": "deferred",
  "reason": "现有 validator 未覆盖用户裁定的共同缺口；但用户要求先去掉脚本新增内容和 fixture，因此该 executable gate 暂缓。",
  "metadata": {
    "cluster_id": "C001",
    "extraction_epoch": "E1",
    "similarity_basis": "llm",
    "source_steps": ["Ground Truth"]
  }
}
```

## 5. Atomic Extract

候选 atomic skill：

```json
{
  "level": "atomic",
  "name": "validate_testcase_xmind_json.py single-parameter gate",
  "document": "Tool validates testcase JSON. New parameter pattern: no new CLI flags; same json_file argument. Output remains Validation passed or Validation failed with path-specific errors.",
  "content": "Use python -X utf8 scripts/validate_testcase_xmind_json.py path/to/testcase.json during verification when Chinese stderr readability matters on Windows.",
  "tools": ["python", "scripts/validate_testcase_xmind_json.py"],
  "source_rollouts": ["ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#T029-T050"],
  "operation": "modify",
  "status": "pending",
  "target_placement": "deferred",
  "reason": "The existing CLI is stable, but executable validator changes are deferred per follow-up instruction.",
  "metadata": {
    "cluster_id": "C001",
    "extraction_epoch": "E1",
    "similarity_basis": "llm",
    "source_steps": ["T029", "T050"]
  }
}
```

Pending observation:

```json
{
  "level": "atomic",
  "name": "Windows PowerShell Python pipe UTF-8 guard",
  "document": "Use UTF-8 console or python -X utf8 when piping Chinese source into Python on Windows.",
  "content": "This is useful for local execution reliability, but it is not central to testcase XMind generation and was observed strongly in only one rollout.",
  "tools": ["powershell", "python -X utf8"],
  "source_rollouts": ["ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#T029-T042"],
  "operation": "keep",
  "status": "pending",
  "target_placement": "none",
  "reason": "Single-rollout operational detour; not written into target skill main rules.",
  "metadata": {
    "cluster_id": "C002",
    "extraction_epoch": "E1",
    "similarity_basis": "llm",
    "source_steps": ["T029", "T042"]
  }
}
```

## 6. Merge / Decompose

Cluster `C001` merged three rollout gaps into one target capability:

- symptom: generated XMind can validate and convert while still missing parameter-level single-parameter coverage;
- stable correction: require `单参数测试 -> 参数名 -> 四类分类 -> testcase`;
- implementation split:
  - instruction-level modification in `SKILL.md`;
  - schema reference modification in `references/xmind-format.md`;
  - executable validation modification in `scripts/validate_testcase_xmind_json.py` was considered but deferred;
  - positive and negative JSON fixtures were considered but removed per follow-up instruction.

Cluster `C002` was kept pending and not written because it is a Windows execution detour rather than a high-frequency testcase-design rule.

## 7. General Filter

Accepted content passed these filters:

1. Not tied to a specific AbilityKit document path, API name, or one-off artifact.
2. Improves an existing target skill behavior rather than creating a new skill.
3. Uses existing Python standard library and existing scripts only.
4. Keeps agent-facing instructions executable and concise.
5. Keeps executable validator and fixture changes out of this pass per follow-up instruction.

Rejected content:

- none

Pending content:

- UTF-8 pipe guard remains out of the target skill because evidence is narrower and the behavior is environmental.

## 8. Tool Schema Filter

Checked tools and commands:

- `python -m py_compile .agents/skills/cangjie-testcase-xmind/scripts/validate_testcase_xmind_json.py`
Deferred tools and commands:

- `scripts/validate_testcase_xmind_json.py` single-parameter hierarchy gate
- positive and negative JSON fixture validation

All tools are existing local commands/scripts. No new package, CLI flag, or external dependency was introduced.

## 9. Update Steps

Actual modification steps:

1. Updated `SKILL.md` workflow:
   - inserted single-parameter coverage before Pair-wise generation;
   - changed validation/conversion step numbers;
   - added parameter-centric `单参数测试` rule;
   - updated testcase naming guidance;
   - updated validator tool description.
2. Updated `references/xmind-format.md`:
   - expanded required tree under `单参数测试`;
   - added `Single-Parameter Coverage` section;
   - specified four mandatory category nodes and `不涉及` leaf behavior.
3. Deferred `scripts/validate_testcase_xmind_json.py` executable gate:
   - the proposed single-parameter hierarchy validator was removed from the script per follow-up instruction;
   - the script currently remains scoped to schema consistency, testcase shape, and Pair-wise coverage.
4. Removed proposed fixture files:
   - `evals/fixtures/single-param-valid.json`
   - `evals/fixtures/single-param-missing-coverage.json`
5. Kept `evals/content-basic.jsonl` out of this governance pass.

## 10. Verification Results

Commands and observed results:

```text
python -m py_compile .agents\skills\cangjie-testcase-xmind\scripts\validate_testcase_xmind_json.py
=> exit 0
```

```text
Fixture validation was removed from the pass per follow-up instruction.

## 11. SkillX 治理摘要

- target_skill: `cangjie-testcase-xmind`
- 使用 rollout: 3 (`ability_access_ctrl_testcase_xmind`, `abilitykit-error-observer-xmind`, `error_manager_testcase_xmind`)
- 跳过 rollout: 0
- extraction_epoch: `E1`
- ground truth: provided 3, invalid_rollout_schema 0, conflict 2
- planning candidates: accepted 1, pending 0, rejected 0
- functional candidates: accepted 0, pending 1, rejected 0
- atomic candidates: accepted 0, pending 2, rejected 0
- clusters: `C001` merged single-parameter coverage hierarchy; `C002` pending UTF-8 execution detour
- update decisions: add 0, modify 2 existing files, deferred 2
- 建议写入位置: already applied to `SKILL.md`, `references/xmind-format.md`; deferred for `scripts/validate_testcase_xmind_json.py` and `evals/fixtures/`
- 建议新建 Skill: 无
- 未采纳原因: UTF-8 pipe guard is environment-specific and only supported by one rollout detour
- 验证建议: after the user re-enables executable validation, add positive/negative validator fixtures and run them separately from `evals/content-basic.jsonl`
