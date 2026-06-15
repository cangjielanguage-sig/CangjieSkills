---
name: cangjie-skill-evolution
description: "当需要基于 cangjie-rollout-collector 生成的 Rollout Record、trace、ground truth 或 eval 结果，对已有仓颉 Agent Skill 做治理、演进、修复、抽象规则、生成 consolidated patch、沉淀或拒绝经验、从零起草 Skill 时使用此 Skill。它提供统一的 rollout 证据治理流程：读取证据、校验 ground truth、跨 rollout 对比、扫描目标 Skill 本体、增量去重、生成候选、抽象规则、编译补丁、执行 experience gate、合并写入与验证；只有用户明确要求写入时才修改目标 Skill。"
---

# 仓颉 Skill 自进化治理

本 Skill 是 rollout-based Skill 治理的唯一入口。采集和保存 rollout 交给 `cangjie-rollout-collector`；本 Skill 只处理已有 `Rollout Record`，并把证据筛选、跨 rollout 对比、目标本体扫描、规则抽象、补丁生成、经验准入、冲突检查和写入验证统一到一个流程中。

执行时只按下面的编号步骤推进。不要把历史方案暴露成多个入口、独立阶段或固定串联流程；相关能力已经合并到下面的具体步骤里。任何中间结果都不得直接写目标文件，最终只能产出一份 consolidated patch；只有用户明确授权写入时才应用。

## 1. 读取输入

输入可以是用户粘贴的 `Rollout Record` Markdown，也可以是用户指定的 rollout 文件。

未指定输入时，不假设固定 rollouts 路径。按顺序定位 Rollout Record：用户提供的 rollout 文件或目录；已有治理摘要、报告或 trace 中记录的 rollout 路径；当前工作区或已知 skills 根目录中发现的 `cangjie-rollout-collector` 的 `records/rollouts`。仍无法定位时，要求用户提供 rollout 路径，不得跨盘全局搜索或凭空生成记录。

可只读扫描目标 Skill 的既有治理摘要或 `reports/`，用于识别已处理 rollout、已应用 patch 和已拒绝候选。已有报告只用于增量过滤，不作为 accepted 候选的独立证据。

已处理且没有新证据的 rollout 不重复生成 patch；新候选与已应用内容重复时，优先标记为 `merge`、`stale` 或 `rejected`，不得追加冗余规则。

不得改写原始 rollout、证据文件、eval/report 文件或用户未授权修改的 Skill。

## 2. 校验 ground truth/yi* gate

读取每条 rollout 时先执行 ground truth/yi* gate：

- 若存在 `ground_truth_status: provided`、`outcome_source: ground_truth`、`adjudicated_outcome` 与 `### Ground Truth (yi*)`，使用 `adjudicated_outcome` 作为有效 outcome；`trace_outcome` 只作为审计和冲突说明。
- 若缺少任一 gate 字段或没有 `### Ground Truth (yi*)`，标记为 `invalid_rollout_schema` 并跳过；不得产生候选、memory、patch、`delta K` 或 `delta e`。
- 若 `trace_outcome` 与 `adjudicated_outcome` 冲突，必须写入治理摘要；当 ground truth `confidence: low` 或 trace 中有明确失败证据时，相关候选保持 `pending`。
- 单条 rollout 解析失败不得中断其他 rollout；缺失字段不得从上下文补全。

按有效 outcome 使用证据：

- `success`：可支撑稳定主流程、成功路径、补丁候选和验证建议。
- `partial`：只提取已验证有效部分，默认 `pending`。
- `failure`：用于失败根因、规避规则、过滤规则和补丁候选；不得单独支撑稳定主流程。
- `blocked`：视为 failure 子类，只记录阻塞条件和规避建议。
- `not_verified`：只产生 `pending`，不得进入 accepted 写入。

同时消费 Rollout Record 字段：

- `Transferable Observations.pattern`：可作为 `source: rollout` 候选输入；`pattern: none` 不生成候选，非空内容仍需通过 ground truth、边界和冲突检查。
- `Failure Or Detour`：作为失败根因、规避规则、validation gap 或 patch 候选证据，不得直接写成主流程。
- `used_experience`：用于判断既有 experience 是否有效、污染、错位或未被消费。
- `collection_confidence`：影响候选初始置信度；`low` 不支撑 accepted，`medium` 默认需要额外 rollout、验证或人工复核。

## 3. 按目标分组

先按 `target_skill` 分组，再按 `task_id` 分组，最后按有效 outcome 分流。

不同目标 Skill 的候选、patch、`delta K` 或 `delta e` 不得混合。每个目标 Skill 独立形成候选池、治理摘要和 consolidated patch。

## 4. 执行跨 rollout 对比

同一 `target_skill / task_id` 下存在多条有效 rollout 时，按 `success / partial / failure / blocked / not_verified` 对比。

只提炼可复核差异：成功路径、失败分叉、缺失验证、工具误用、经验是否被使用及其效果。对比结论必须绑定 rollout ID 与步骤证据，只能进入候选 `evidence`，不作为独立写入通道。

若发现零 rollout 或覆盖不足的功能盲区，只输出补采 rollout 或补充 eval 建议；不得主动合成测试任务并据此写入 Skill。

## 5. 扫描目标 Skill 本体

对每个目标 Skill 执行本体扫描，范围只包括目标 `SKILL.md` 和其中直接引用的 `references/*.md`；不做无限引用追踪。

扫描并生成 `source: target_audit` 候选：

- 主流程中出现一次性路径、样例数据、用户偏好、临时产物。
- 多处规则重复、互相矛盾，或触发条件过宽。
- `references/experiences.md` 中存在无触发条件、无边界、无来源证据或低复用价值的经验。
- reference 文件无入口、入口断链，或引用文件孤立。
- 本应进入 `SKILL.md` 的稳定规则被降级塞入 experience。
- 旧命令、旧工具、旧验证方式与当前 lint/eval 门禁不一致。

去腐化候选操作包括 `delete`、`merge`、`narrow`、`relocate`、`repair_link`。删除、迁移、收窄已有规则默认比新增更高风险；没有原文位置、腐化原因、证据来源和回归风险说明时，只能 `pending`。仅凭 target audit 可提出 consolidated patch，但涉及行为删除或收窄时必须建议 lint/eval 或人工复核。

## 6. 生成治理候选

先从有效 rollout 中生成候选，再判断每个候选需要哪些处理动作。每个候选先用 JSON 中间态表达，再转为 Markdown 建议或 patch。

生成候选时同步标记知识流向：

- `delta K`：稳定知识，应进入 `SKILL.md`、工具说明、validator、eval 或引用入口。
- `delta e`：上下文敏感经验，只能在通过 [experience gate](#experience-gate) 后进入 `references/experiences.md`。
- `none`：证据不足、边界不清、冲突、一次性或不值得沉淀，只保留在治理摘要。

```json
{
  "candidate_id": "C-001",
  "target_skill": "<skill name>",
  "task_id": "<task id>",
  "source": "rollout | target_audit | eval | user_feedback",
  "candidate_type": "rule | patch | validation | experience | deletion | creation",
  "problem_type": "main_flow_gap | tool_schema_gap | validation_gap | reference_gap | context_experience | evidence_gap",
  "corruption_type": "duplicate | conflict | one_off | overbroad | stale_reference | orphan_reference | experience_pollution | misplaced_experience | validation_gap | none",
  "content": "<可执行规则、补丁意图或经验内容>",
  "evidence": ["task_id/rollout_id#S1-S3"],
  "stream": "delta K | delta e | none",
  "actions": ["cross_rollout_critique", "abstract_rule", "compile_patch", "classify_stream", "experience_gate", "check_conflict"],
  "operation": "add | modify | merge | delete | narrow | relocate | repair_link | keep",
  "target": "SKILL.md | references/experiences.md | references/*.md | none",
  "status": "accepted | pending | rejected | stale | conflict",
  "reason": "<证据、边界、过滤和写入理由>"
}
```

`candidate_type` 表示候选产物形态，`corruption_type` 表示治理原因，最终写入、合并、删除或保留由 `operation` 决定。

状态规则：

- `accepted`：证据可复核，经过必要处理，并通过冲突、schema、边界和验证检查。
- `pending`：有启发但证据不足、根因不完整、仅来自 `partial` / `blocked` / `not_verified`，或缺少必要验证。
- `rejected`：与证据冲突、过度特例化、无法复现、低价值、会误导目标 Skill，或与用户要求冲突。
- `stale`：目标文件、锚点、旧内容或引用在当前文件中不可定位。
- `conflict`：多个候选修改同一文件同一行、同一标题块或同一 passage，且无法自动裁决。

## 7. 抽象主 Skill 规则

当候选暴露的是主流程缺口、工具使用规则缺口、验收规则缺口或可复用失败规避规则时，执行规则抽象。

抽象时保留动作意图、工具、关键参数、产物、错误和验证结果；删除硬编码路径、账号、样例数据、一次性任务描述和只适用于单次案例的内容。

分层写入时使用以下判断：

- `planning`：任务级流程、阶段顺序、分支选择、停止条件和最终验收。
- `functional`：某类子任务的稳定做法，例如检索、构建、转换、验证、诊断。
- `atomic`：单个工具、参数、文件格式、schema、失败模式或边界条件。

合并同目标、同输入输出、同工具集合和同失败边界的候选；拆分包含多个独立触发条件的过宽候选。

单条成功 rollout 支撑的主流程候选默认 `pending`，除非有独立验证或跨 rollout 复现。

## 8. 编译可落地 patch

当候选涉及具体文件修改时，编译为 local patch，并检查锚点、stale、冲突和引用完整性。

适用范围包括 `SKILL.md`、`references/*.md`、validator、eval、工具说明、经验入口或引用链接。

local patch schema：

```json
{
  "patch_id": "P-<rollout_id>-001",
  "source_rollout": "<rollout_id>",
  "target_file": "SKILL.md",
  "target_section": "<标题或 section>",
  "operation": "insert_after | replace | delete | create_file | link_reference",
  "anchor": "<精确锚点>",
  "old_content": "<replace/delete 时需要>",
  "new_content": "<新增或替换内容>",
  "verification": "<验证方式或 pending 原因>",
  "status": "accepted | pending | rejected | stale | conflict"
}
```

预检规则：

- `narrow`、`relocate`、`repair_link` 必须编译为明确的 `replace`、`insert_after`、`delete` 或 `link_reference` patch。
- `target_file` 不存在且操作不是 `create_file` 时，标为 `stale`。
- `anchor`、`target_section` 或 `old_content` 在当前文件中找不到时，标为 `stale`。
- 同一文件同一行、同一标题块或同一文本段被多个 patch 修改时，标为 `conflict`。
- `create_file` 与 `link_reference` 必须满足原子对规则：新建 `references/*.md` 时必须同步在 `SKILL.md` 加入口；丢弃文件时必须同步丢弃链接。

只把 `accepted` 且通过预检的 patch 交给统一合并。`pending`、`rejected`、`stale` 和 `conflict` 必须进入摘要，不得静默丢失。

<a id="experience-gate"></a>

## 9. 执行 experience gate

本节定义 `experience gate`：它不是单独文件或脚本，而是写入 `references/experiences.md` 之前必须执行的准入判断。

当候选满足任一条件时，必须经过 `experience gate`：

- 候选类型是 `experience`。
- 候选目标是 `references/experiences.md`。
- 候选不确定应进入 `SKILL.md` 还是经验库。
- 候选是上下文敏感动作提醒，可能不适合写成稳定主流程。
- 候选在第 6 步被初判为 `delta e`。

`experience gate` 只复核 `delta e` 是否允许写入经验库；它不得把应进入主 Skill 的 `delta K` 降级成经验。

`partial` / `blocked` / `not_verified` 可产生 pending 经验、验证建议或补采 rollout 建议，但默认不得 accepted 写入。

`delta e` 必须同时满足以下条件才能 accepted：

- 是上下文敏感、动作级提醒，不适合提升为无条件主流程。
- 有清晰触发条件、适用边界、失效条件和来源证据。
- 能在未来相似任务中减少重复错误或提醒关键判断。
- 不与用户要求、目标 `SKILL.md` 主流程或更强证据冲突。
- 证据不是只来自单次低置信、未验证、`partial` 或 `not_verified` rollout。
- 不是把本应修进 `SKILL.md` 的主流程缺陷降级成经验。

以下经验必须 `pending` 或 `rejected`：

- 绑定一次性路径、文件名、用户偏好、样例数据或临时产物。
- 只是原始 rollout 摘要，缺少可迁移触发条件。
- 会增加检索噪声、上下文负担，或让 agent 行为更犹豫。
- 与主流程、用户要求或更强证据冲突。

若有 accepted `delta e` 会创建或更新 `references/experiences.md`，必须同时检查目标 `SKILL.md` 是否有经验使用入口。若没有入口，生成配套 `delta K`，说明何时读取、如何筛选、如何改写和如何记录经验；不得只创建孤立经验文件。

经验条目格式：

```markdown
## <ID>

- 触发条件: <When/If/For 风格条件>
- 经验: <不超过 100 个中文字符或 64 个英文词>
- 适用边界: <何时适用，何时不适用>
- 来源 rollout: <task_id/rollout_id#步骤>
- 状态: accepted | pending | rejected
```

## 10. 合并候选池

所有候选进入统一候选池后，再执行去重、裁决、冲突检查和写入判断。

合并规则：

- 有限精炼：最多执行 2 轮去重、合并、拆分过宽候选和过滤低证据候选；不得扩展成独立迭代模式。
- 去重：相同或高度相似修改只保留最清晰、最可执行版本。
- 裁决：证据更强、验证更完整、多 rollout 复现的候选优先。
- 保留非冗余洞见：不同 rollout 揭示的独特失败或成功路径可以保留，但不得膨胀为 rollout 摘要集合。
- 行级独立：合并后的 patch 不得重叠同一行、同一标题块或同一 passage。
- 原子引用：`references/*.md` 与 `SKILL.md` 中的链接或加载说明必须同生同灭。
- 来源统一：`source=rollout` 与 `source=target_audit` 候选进入同一候选池；若新补丁与既有腐化内容重复，优先合并或替换，不追加冗余规则。

## 11. 生成 consolidated patch

只把 `accepted` 且通过合并检查的修改放入 consolidated patch。

consolidated patch 必须说明：

- 修改目标文件。
- 插入、替换、删除或创建的具体位置。
- 每个修改对应的候选 ID 和 rollout 证据。
- 未写入候选的状态与原因。
- 写入后需要运行的验证。

如果没有 accepted 候选，仍输出治理摘要，但 consolidated patch 标为 empty。

写入前必须确认 consolidated patch 可整体应用；若任一 accepted patch 在最终预检中失败，将相关候选标为 `stale` 或 `conflict`，中止写入并报告，不做部分写入。

## 12. 执行写入约束

- 用户只要求评估、建议或方案时，只输出治理建议，不改文件。
- 用户明确要求治理、更新、改进、修复或整合 Skill，且当前会话允许写入时，才修改目标 Skill。
- 无 ground truth 的 rollout 不支撑 accepted 候选。
- `partial` / `blocked` / `not_verified` 默认只能产生 `pending`。
- 没有 accepted `delta K` 时，不更新目标 `SKILL.md`。
- 没有 accepted `delta e` 时，不创建或更新 `references/experiences.md`。
- 不改写原始 rollout、证据文件或用户未授权目标 Skill。

## 13. 验证

写入后按顺序验证。将 `<target-skill-path>` 替换为目标 Skill 目录的绝对路径，将 `<target-skill-name>` 替换为目标 Skill 名称。

先检查工具是否存在：

```powershell
Get-Command skill-lint -ErrorAction SilentlyContinue
Get-Command skill-eval -ErrorAction SilentlyContinue
```

若 `skill-lint` 或 `skill-eval` 缺失，必须在治理摘要中写明缺少哪个工具，并提示用户从 [cjse](https://gitcode.com/cjse) 下载或安装后重试；不得假装已经完成对应验证。

基础结构校验：

```powershell
$env:PYTHONUTF8 = '1'
$skillCreatorHome = if ($env:CODEX_HOME) {
  Join-Path $env:CODEX_HOME 'skills\.system\skill-creator'
} else {
  Join-Path $HOME '.codex\skills\.system\skill-creator'
}
$quickValidate = Join-Path $skillCreatorHome 'scripts\quick_validate.py'
if (Test-Path $quickValidate) {
  python $quickValidate '<target-skill-path>'
} else {
  Write-Host "quick_validate.py is missing: $quickValidate"
}
```

若找不到 `quick_validate.py`，必须在治理摘要中写明阻塞原因，不得假装已完成基础结构校验。

lint 校验：

```powershell
New-Item -ItemType Directory -Force -Path 'reports\lint' | Out-Null
skill-lint --path '<target-skill-path>' --format text --severity-threshold warning
skill-lint --path '<target-skill-path>' --format json --out 'reports\lint\<target-skill-name>-skill-lint.json' --severity-threshold warning
```

`--severity-threshold warning` 表示 warning 也会让 lint 以失败状态退出，适合作为严格门禁；若只检查 blocking error，可省略该参数。

eval 校验：

```powershell
New-Item -ItemType Directory -Force -Path 'reports\eval' | Out-Null
if (Test-Path '<target-skill-path>\evals') {
  skill-eval --path '<target-skill-path>' --mode all --out 'reports\eval\<target-skill-name>-skill-eval.json' --timeout 1800 --progress
} else {
  Write-Host 'evals directory is missing; skip skill-eval.'
}
```

若目标 Skill 没有 `evals/`，跳过 `skill-eval` 并在摘要中说明 `evals directory is missing`。若新增或修改 eval，优先运行 `--mode all`；只改 discovery 触发时可运行 `--mode discovery`，只改正文规则时可运行 `--mode content`。

需要真实 agent runner 时使用：

```powershell
skill-eval --path '<target-skill-path>' --mode all --runner agent-command --agent-command '<agent command>' --out 'reports\eval\<target-skill-name>-agent-skill-eval.json' --timeout 1800 --progress --emit-trace
```

若真实 agent runner 不可用，说明阻塞原因，并至少保留 `quick_validate` 与 `skill-lint` 结果。

## 14. 输出治理摘要

每次治理结束都输出：

```markdown
## Skill Evolution 治理摘要

- target_skill: <名称>
- 使用 rollout: <数量与 ID>
- 跳过 rollout: <缺字段或无法解析的 ID 与原因>
- rollout fields consumed: transferable_observations <n>, failure_or_detour <n>, used_experience <n>, collection_confidence: high <n>, medium <n>, low <n>
- cross-rollout critique: compared <n> task groups, findings <n>
- incremental handling: skipped_processed <n>, duplicate_patch <n>, stale_existing <n>
- target audit: scanned <n>, corruption candidates <n>
- corruption types: duplicate <n>, conflict <n>, one_off <n>, stale_reference <n>, experience_pollution <n>
- ground truth: provided <n>, invalid_rollout_schema <n>, outcome_conflict <n>
- trace outcome 与 adjudicated outcome 冲突: <数量与摘要>
- 问题类型: <main_flow_gap/tool_schema_gap/validation_gap/reference_gap/context_experience/evidence_gap>
- 候选: accepted <n>, pending <n>, rejected <n>, stale <n>, conflict <n>
- 处理动作: cross_rollout_critique <n>, abstract_rule <n>, compile_patch <n>, classify_stream <n>, experience_gate <n>, check_conflict <n>
- delta K: add <n>, modify <n>, merge <n>, delete <n>, pending <n>, rejected <n>
- delta e: add <n>, modify <n>, merge <n>, delete <n>, pending <n>, rejected <n>
- de-corruption patch: delete <n>, merge <n>, narrow <n>, relocate <n>, repair_link <n>
- experience gate: <写入/不写入/需新增入口/拒写原因>
- consolidated patch: <数量、目标文件和操作摘要>
- expected impact: affected_rollouts <n>, expected_gap_reduction <summary>
- 未采纳原因: <pending/rejected/stale/conflict 的主要原因>
- 验证建议: <quick_validate、skill-lint、schema、eval、人工复核或最小复现>
```

## 最小检查清单

- 已确认 rollout 采集由 `cangjie-rollout-collector` 完成，本 Skill 只处理已有记录。
- 未指定输入时，已按用户输入、既有报告路径、当前工作区或已知 skills 根目录中的 collector 记录目录定位 rollout；无法定位时已要求用户提供路径。
- 已只读检查既有治理摘要或报告，已处理 rollout 未被重复生成 patch。
- 已消费 `Transferable Observations`、`Failure Or Detour`、`used_experience` 与 `collection_confidence`。
- 已按 `target_skill / task_id / outcome` 分组，未混合不同 Skill 的知识。
- 同一 `task_id` 的跨 rollout 对比只作为证据，不作为独立写入通道。
- 已扫描目标 `SKILL.md` 和直接引用的 `references/*.md`，并记录 target audit 候选。
- 每条有效 rollout 都通过 ground truth/yi* gate；未通过者已跳过并记录原因。
- `trace_outcome` 与 `adjudicated_outcome` 冲突已写入摘要。
- 每个候选都有 `source`、证据来源、候选类型、腐化类型、处理动作、目标位置、状态和理由。
- 规则抽象、patch 编译、经验准入和冲突检查都按候选需要执行，不作为独立入口暴露。
- experience 未被当作默认正收益；所有 `delta e` 已通过触发条件、边界、复用价值和冲突检查。
- `partial` / `blocked` / `not_verified` 只产生 pending 经验、验证建议或补采建议，默认未 accepted 写入。
- 删除、迁移、收窄已有内容已说明原文位置、腐化原因、证据来源和回归风险。
- consolidated patch 已通过 stale、conflict、引用原子对和行级重叠检查。
- 只有用户明确授权写入时才修改目标 Skill；写入后已运行验证或说明无法运行原因。
