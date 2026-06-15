# Skill Evolution Governance: cangjie-testcase-xmind single-parameter hierarchy and interface type normalization

- target_skill: `cangjie-testcase-xmind`
- governance_skill: `cangjie-skill-evolution`
- generated_at: `2026-06-15`
- rollout_root: `.agents/skills/cangjie-rollout-collector/records/rollouts/cangjie-testcase-xmind`
- write_scope: target skill files only; original rollout records and output artifacts were not modified by this governance pass

## 1. Input And Gate

Read 4 rollout records and grouped them by `target_skill=cangjie-testcase-xmind`.
All 4 records passed the ground truth/yi* gate because each record contains `ground_truth_status: provided`, `outcome_source: ground_truth`, `adjudicated_outcome`, and `### Ground Truth (yi*)`.

| task_id | rollout_id | trace_outcome | adjudicated_outcome | gate | conflict | ground truth gap |
| --- | --- | --- | --- | --- | --- | --- |
| `ability_access_ctrl_testcase_xmind` | `cangjie-testcase-xmind-20260613-100839-001` | `partial` | `partial` | passed | no | `单参数测试` lacked per-parameter nodes and the `有效等价类 / 无效等价类 / 边界值 / 特殊值` discussion. |
| `abilitykit-error-observer-xmind` | `cangjie-testcase-xmind-20260613-105118-001` | `not_verified` | `partial` | passed | yes | `ErrorObserver.init` lacked `onUnhandledException` / `onException` parameter hierarchy and equivalence-class discussion. |
| `error_manager_testcase_xmind` | `cangjie-testcase-xmind-20260613-111744-001` | `not_verified` | `partial` | passed | yes | `测试覆盖` lacked concrete parameter nodes and equivalence-class discussion under `单参数测试`. |
| `error_manager_testcase_xmind` | `cangjie-testcase-xmind-20260615-161319-001` | `not_verified` | `partial` | passed | yes | Two gaps remained: single-parameter classification nodes were still missing, and `接口列表 -> 接口类型` used non-normalized values such as static function style labels instead of normalized values such as `类`, `实例属性`, `构造函数`, `订阅型API`, `枚举值`, and `硬件相关API`. |

Gate statistics:

- ground_truth provided: 4
- invalid_rollout_schema: 0
- trace/adjudicated outcome conflict: 3
- collection_confidence: high 4, medium 0, low 0
- `Transferable Observations` consumed: 4 sections read; all had `pattern: none`
- `Failure Or Detour` consumed: 4 sections read; 1 non-empty operational detour cluster in `cangjie-testcase-xmind-20260613-100839-001`
- `used_experience` consumed: 4 records; all observable steps had `used_experience: none`

## 2. Cross-Rollout Critique

Compared 3 task groups:

- `ability_access_ctrl_testcase_xmind`
- `abilitykit-error-observer-xmind`
- `error_manager_testcase_xmind`

Findings:

1. `单参数测试` hierarchy is a stable cross-rollout gap.
   Evidence appears in all 4 rollout records. The recurring failure pattern is that the generated mind map may validate, convert to `.xmind`, and pass basic `content.xml` spot checks while still flattening single-parameter testcases directly under `单参数测试`.

2. Validator coverage was insufficient.
   The existing validator checked fixed top-level coverage nodes, testcase field shape, and Pair-wise coverage, but did not reject a flat `单参数测试` structure or non-normalized `接口类型` values.

3. `接口类型` normalization is a newer high-confidence gap.
   It appears explicitly in `cangjie-testcase-xmind-20260615-161319-001`. Although it is supported by one rollout, the ground truth gives a clear normative vocabulary and the target audit confirmed there was no rule or validator gate for it.

4. Static `skill-eval` is not sufficient for this Skill's content behavior.
   Default static `skill-eval` checks the Skill text itself, while the historical passing reports and the current meaningful verification require `--runner agent-command` to exercise generated answers. This did not become a target Skill rule, but it is recorded as validation context.

## 3. Target Audit

Scanned target docs:

- `.agents/skills/cangjie-testcase-xmind/SKILL.md`
- `.agents/skills/cangjie-testcase-xmind/references/xmind-format.md`
- `.agents/skills/cangjie-testcase-xmind/references/pairwise.md`

Implementation and validation capability check:

- `.agents/skills/cangjie-testcase-xmind/scripts/common.py`
- `.agents/skills/cangjie-testcase-xmind/scripts/validate_testcase_xmind_json.py`
- `.agents/skills/cangjie-testcase-xmind/evals/content-basic.jsonl`

Audit findings:

- `SKILL.md` had a general JSON/Piar-wise workflow but did not force single-parameter hierarchy before Pair-wise.
- `references/xmind-format.md` documented single-parameter as a fixed node, but did not expand the required `参数名 -> 四类分类节点` tree.
- `SKILL.md` and `references/xmind-format.md` did not define a normalized `接口类型` vocabulary.
- `validate_testcase_xmind_json.py` had no single-parameter hierarchy validator and no interface type validator.
- Existing governance reports from 2026-06-13 already proposed single-parameter fixes, but the current target files did not fully encode the rule and gate, so the old finding was treated as stale/merge evidence rather than skipped.

Target audit statistics:

- scanned docs: 3
- implementation files inspected: 3
- corruption candidates: 3
- corruption types: duplicate 1, conflict 0, one_off 0, stale_reference 1, experience_pollution 0, validation_gap 2

## 4. Candidate Pool

```json
[
  {
    "candidate_id": "C-001",
    "target_skill": "cangjie-testcase-xmind",
    "task_id": "cross-task",
    "source": "rollout",
    "candidate_type": "rule",
    "problem_type": "main_flow_gap",
    "corruption_type": "validation_gap",
    "content": "For parameterized APIs, build 单参数测试 as 参数名 -> 有效等价类 / 无效等价类 / 边界值 / 特殊值 before Pair-wise cases.",
    "evidence": [
      "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#Ground Truth",
      "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#Ground Truth",
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260613-111744-001#Ground Truth",
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260615-161319-001#Ground Truth"
    ],
    "stream": "delta K",
    "actions": ["cross_rollout_critique", "abstract_rule", "compile_patch", "classify_stream", "check_conflict"],
    "operation": "modify",
    "target": "SKILL.md | references/xmind-format.md",
    "status": "accepted",
    "reason": "Repeated across four high-confidence partial rollouts and directly tied to user adjudicated output gaps."
  },
  {
    "candidate_id": "C-002",
    "target_skill": "cangjie-testcase-xmind",
    "task_id": "error_manager_testcase_xmind",
    "source": "rollout",
    "candidate_type": "rule",
    "problem_type": "main_flow_gap",
    "corruption_type": "none",
    "content": "接口类型 must use normalized vocabulary such as 类, 方法, 属性, 实例属性, 构造函数, 订阅型API, 枚举值, 硬件相关API, 类型; avoid implementation-detail labels such as 静态函数, 实例方法, 只读属性, 可读写属性.",
    "evidence": [
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260615-161319-001#Ground Truth"
    ],
    "stream": "delta K",
    "actions": ["abstract_rule", "compile_patch", "classify_stream", "check_conflict"],
    "operation": "modify",
    "target": "SKILL.md | references/xmind-format.md",
    "status": "accepted",
    "reason": "The ground truth provided explicit normalized values; target audit showed no existing rule; the change is low-risk and covered by a new eval."
  },
  {
    "candidate_id": "C-003",
    "target_skill": "cangjie-testcase-xmind",
    "task_id": "cross-task",
    "source": "target_audit",
    "candidate_type": "validation",
    "problem_type": "validation_gap",
    "corruption_type": "validation_gap",
    "content": "Add validator gates for single-parameter hierarchy and normalized interface type values.",
    "evidence": [
      "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#Ground Truth",
      "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#Ground Truth",
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260615-161319-001#Ground Truth"
    ],
    "stream": "delta K",
    "actions": ["abstract_rule", "compile_patch", "classify_stream", "check_conflict"],
    "operation": "modify",
    "target": "scripts/common.py | scripts/validate_testcase_xmind_json.py",
    "status": "accepted",
    "reason": "Without executable validation, generated JSON could keep passing while missing user-adjudicated hierarchy/type requirements."
  },
  {
    "candidate_id": "C-004",
    "target_skill": "cangjie-testcase-xmind",
    "task_id": "error_manager_testcase_xmind",
    "source": "eval",
    "candidate_type": "validation",
    "problem_type": "validation_gap",
    "corruption_type": "none",
    "content": "Add an eval that expects normalized interface type values and single-parameter hierarchy for a class/constructor/enum/property example.",
    "evidence": [
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260615-161319-001#Ground Truth"
    ],
    "stream": "delta K",
    "actions": ["compile_patch", "classify_stream", "check_conflict"],
    "operation": "add",
    "target": "evals/content-basic.jsonl",
    "status": "accepted",
    "reason": "Covers the newly observed interface type gap and confirms the single-parameter hierarchy remains active in true agent eval."
  },
  {
    "candidate_id": "C-005",
    "target_skill": "cangjie-testcase-xmind",
    "task_id": "ability_access_ctrl_testcase_xmind",
    "source": "rollout",
    "candidate_type": "experience",
    "problem_type": "context_experience",
    "corruption_type": "one_off",
    "content": "Set PowerShell pipeline and Python UTF-8 mode before piping Chinese JSON into Python.",
    "evidence": [
      "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#T029-T042"
    ],
    "stream": "delta e",
    "actions": ["experience_gate", "classify_stream", "check_conflict"],
    "operation": "keep",
    "target": "none",
    "status": "pending",
    "reason": "Useful local execution reminder but supported as an environment-specific detour in one rollout only; not written into the target skill."
  }
]
```

Candidate statistics:

- accepted: 4
- pending: 1
- rejected: 0
- stale: 0
- conflict: 0

## 5. Consolidated Patch

Applied patch set:

| patch_id | candidate | target_file | operation | summary |
| --- | --- | --- | --- | --- |
| `P-001` | `C-001` | `SKILL.md` | modify | Inserted workflow step requiring single-parameter coverage tree before Pair-wise. |
| `P-002` | `C-002` | `SKILL.md` | modify | Added JSON design rule requiring normalized `接口类型` vocabulary and avoiding labels such as `静态函数`, `实例方法`, `只读属性`, `可读写属性`. |
| `P-003` | `C-001/C-002` | `references/xmind-format.md` | modify | Expanded required tree and added `Single-Parameter Coverage` plus interface type vocabulary guidance. |
| `P-004` | `C-003` | `scripts/common.py` | modify | Added `SINGLE_PARAMETER_CATEGORIES` and `INTERFACE_TYPE_VALUES`. |
| `P-005` | `C-003` | `scripts/validate_testcase_xmind_json.py` | modify | Added `validate_interface_type`, `validate_single_parameter`, and helper checks for category/testcase shape. |
| `P-006` | `C-004` | `evals/content-basic.jsonl` | add | Added an eval case for `类`, `构造函数`, `枚举值`, `实例属性`, and parameter classification nodes. |

Modified files:

- `.agents/skills/cangjie-testcase-xmind/SKILL.md`
- `.agents/skills/cangjie-testcase-xmind/references/xmind-format.md`
- `.agents/skills/cangjie-testcase-xmind/scripts/common.py`
- `.agents/skills/cangjie-testcase-xmind/scripts/validate_testcase_xmind_json.py`
- `.agents/skills/cangjie-testcase-xmind/evals/content-basic.jsonl`

Not modified by this pass:

- rollout records under `.agents/skills/cangjie-rollout-collector/records/rollouts/`
- generated user artifacts under `outputs/`
- `references/experiences.md` was not created because there was no accepted `delta e`

## 6. Verification Results

Tool availability:

- `skill-lint.exe`: found
- `skill-eval.exe`: found
- `codex.ps1`: found
- `python -m skill_cli.eval_tools.codex_exec_agent_adapter`: importable

Verification commands and results:

```text
python -m py_compile .agents\skills\cangjie-testcase-xmind\scripts\common.py .agents\skills\cangjie-testcase-xmind\scripts\validate_testcase_xmind_json.py .agents\skills\cangjie-testcase-xmind\scripts\json_to_xmind.py .agents\skills\cangjie-testcase-xmind\scripts\generate_pairwise_cases.py
=> exit 0
```

```text
quick_validate.py .agents\skills\cangjie-testcase-xmind
=> Skill is valid!
```

Direct validator smoke tests:

```text
positive: parameterized API with 参数名 -> 有效等价类/无效等价类/边界值/特殊值
=> []

negative_single: testcase directly under 单参数测试
=> missing parameter nodes / extra parameter nodes / testcase must be under 参数名 -> 分类节点

negative_type: 接口类型 = 静态函数
=> must use normalized interface type value
```

Lint:

```text
skill-lint --path .agents\skills\cangjie-testcase-xmind --format text --severity-threshold warning
skill-lint --path .agents\skills\cangjie-testcase-xmind --format json --out reports\lint\cangjie-testcase-xmind-skill-lint.json --severity-threshold warning
=> OK 1 skill(s) checked, no issues found
=> status: passed
```

Static eval note:

```text
skill-eval --path .agents\skills\cangjie-testcase-xmind --mode all --out reports\eval\cangjie-testcase-xmind-skill-eval.json --timeout 1800 --progress
=> failed 2/4
```

Reason: default static eval checked the Skill text itself, so old content cases expecting one-off API names such as `bindEndpoint` and `configureCache` failed. This is not the meaningful runner for this Skill's content behavior.

True agent eval:

```text
skill-eval --path .agents\skills\cangjie-testcase-xmind --mode all --runner agent-command --agent-command "python -m skill_cli.eval_tools.codex_exec_agent_adapter" --out reports\eval\cangjie-testcase-xmind-agent-skill-eval.json --timeout 1800 --progress --emit-trace
=> status: passed
=> total 4, passed 4, failed 0
=> content_pass_rate 1.0
```

Reports produced:

- `reports/lint/cangjie-testcase-xmind-skill-lint.json`
- `reports/eval/cangjie-testcase-xmind-skill-eval.json`
- `reports/eval/cangjie-testcase-xmind-agent-skill-eval.json`

## 7. Skill Evolution 治理摘要

- target_skill: `cangjie-testcase-xmind`
- 使用 rollout: 4 (`cangjie-testcase-xmind-20260613-100839-001`, `cangjie-testcase-xmind-20260613-105118-001`, `cangjie-testcase-xmind-20260613-111744-001`, `cangjie-testcase-xmind-20260615-161319-001`)
- 跳过 rollout: 0
- rollout fields consumed: transferable_observations 4, failure_or_detour 4 sections / 1 non-empty, used_experience 4, collection_confidence: high 4, medium 0, low 0
- cross-rollout critique: compared 3 task groups, findings 4
- incremental handling: skipped_processed 0, duplicate_patch 1, stale_existing 1
- target audit: scanned 3 direct docs plus 3 implementation/eval files, corruption candidates 3
- corruption types: duplicate 1, conflict 0, one_off 1, stale_reference 1, experience_pollution 0, validation_gap 2
- ground truth: provided 4, invalid_rollout_schema 0, outcome_conflict 3
- trace outcome 与 adjudicated outcome 冲突: 3 (`20260613-105118`, `20260613-111744`, `20260615-161319` all had trace `not_verified` but ground truth `partial`)
- 问题类型: `main_flow_gap`, `validation_gap`, `reference_gap`, `context_experience`
- 候选: accepted 4, pending 1, rejected 0, stale 0, conflict 0
- 处理动作: cross_rollout_critique 1, abstract_rule 3, compile_patch 6, classify_stream 5, experience_gate 1, check_conflict 5
- delta K: add 1, modify 5, merge 1, delete 0, pending 0, rejected 0
- delta e: add 0, modify 0, merge 0, delete 0, pending 1, rejected 0
- de-corruption patch: delete 0, merge 1, narrow 0, relocate 0, repair_link 0
- experience gate: 不写入；UTF-8 pipe reminder remains pending because it is environment-specific and supported by only one rollout detour
- consolidated patch: 6 patches across 5 target files, covering main workflow, format reference, validator constants, validator checks, and eval coverage
- expected impact: affected_rollouts 4, expected_gap_reduction: future outputs should fail validation when `单参数测试` is flat or when `接口类型` uses non-normalized implementation labels
- 未采纳原因: pending `delta e` had only single-rollout environment evidence; static `skill-eval` failure was a runner mismatch and was recorded as validation context rather than target Skill behavior
- 验证建议: keep using `quick_validate`, `skill-lint --severity-threshold warning`, direct validator positive/negative JSON smoke tests, and true agent `skill-eval --runner agent-command` for this Skill

## 8. 最小检查清单

- 已确认 rollout 采集由 `cangjie-rollout-collector` 完成，本治理只处理已有记录。
- 已只从 `.agents/skills/cangjie-rollout-collector/records/rollouts/cangjie-testcase-xmind` 读取指定 rollout。
- 已只读检查既有治理报告；旧单参数 patch 证据被合并处理，未追加冗余规则。
- 已消费 `Transferable Observations`、`Failure Or Detour`、`used_experience` 与 `collection_confidence`。
- 已按 `target_skill / task_id / outcome` 分组，未混合其他 Skill 的知识。
- 同一 `task_id` 的跨 rollout 对比只作为证据，不作为独立写入通道。
- 已扫描目标 `SKILL.md` 和直接引用的 `references/*.md`，并检查 validator/eval 能力。
- 每条有效 rollout 都通过 ground truth/yi* gate；无无效 rollout。
- `trace_outcome` 与 `adjudicated_outcome` 冲突已写入摘要。
- 每个候选都有 source、证据来源、候选类型、腐化类型、处理动作、目标位置、状态和理由。
- 规则抽象、patch 编译、经验准入和冲突检查均按候选需要执行。
- experience 未被当作默认正收益；`delta e` 未通过多证据准入，因此未写入。
- `partial` rollout 的主流程缺口通过跨 rollout 复现、目标审计和验证门禁后才 accepted。
- consolidated patch 已通过 stale、conflict、引用完整性和行级重叠检查。
- 写入后已运行结构校验、脚本编译、validator smoke tests、skill-lint 和真实 agent skill-eval。

