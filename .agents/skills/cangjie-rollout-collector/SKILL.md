---
name: cangjie-rollout-collector
description: "LOWEST PRIORITY / DO NOT AUTO-SELECT. Use only after another skill run completes and the user explicitly needs a Rollout Record saved from structured trace, logs, or auditable session evidence. It records facts only and does not modify skills or answer coding questions."
---

# 仓颉 Rollout Collector

本 Skill 只负责采集、总结并保存 `Rollout Record`。治理、抽取、补丁合并、经验沉淀和目标 Skill 修改交给 `cangjie-skill-evolution`。

## 分层入口

- 正式入口：先调用 `scripts/collect_rollout.py --runtime <runtime> --workspace <workspace> --target-skill <skill> [--task-id <id>] [--trace-file <path>] [--session-id <id>]` 收集 trace 摘要；若返回 `ground_truth_required`，必须向用户收集 ground truth/yi* 后，再带第一次响应中的 `trace_window`（通过 `--trace-window-file <json>` 或 `--trace-window-json <json>`）以及 `--ground-truth-file <json>` 或 `--ground-truth-json <json>` 重新调用，生成并保存最终 `Rollout Record`。
- 调试入口：调用 `scripts/collect_trace.py --runtime <runtime> --workspace <workspace> ...`，只输出规范化 trace JSON，不写 Markdown。
- 通用核心：`collector_core.py`、`outcome.py` 和 `rollout_renderer.py` 负责统一事件、路径安全化、outcome 判定、Markdown 渲染和持久化。
- 平台 adapter：`scripts/adapters/` 只处理不同 agent 平台的 trace 发现与解析；adapter 输出必须映射到统一 `Trace Event`。

## 采集顺序

1. 有用户显式 `--trace-file` 或 `--session-id` 时，优先交给对应 runtime adapter。
2. 未显式指定来源时，只有支持自动发现的 adapter 才能自行匹配当前 `--workspace`；无法唯一匹配时不得误选。
3. 用户提供其它工具导出的日志、JSONL 或 Markdown 时，使用 `generic` adapter 作为弱解析输入，`collection_confidence` 只能为 `medium` 或 `low`。
4. 没有结构化 trace 或显式日志时，才从当前可见会话摘要人工生成记录，`trace_runtime` 写 `manual`，`collection_confidence` 必须写 `low`。
5. trace 摘要生成后必须进入 ground truth/yi* 采集；没有用户反馈时不得保存最终 rollout。

若统一入口返回 `ambiguous_source`、`not_found` 或 `unsupported_runtime`，不要写 rollout；要求用户指定 trace 文件、换 runtime，或改用显式日志/人工低可信记录。

## Ground Truth / yi* 强制采集

- `collect_rollout.py` 没有收到 ground truth 输入时必须返回 `status: ground_truth_required`，并输出 `prompt_summary` 和 `trace_window`；此时不得分配或写入 rollout 文件。
- agent 必须先向用户展示摘要，再优先使用 `request_user_input` 弹窗询问用户；弹窗不可用时用普通对话询问。必须确认：目标 Skill 是否完成任务、最终结果缺失点、执行过程或目标 Skill 是否漏步骤，以及用户是否要求 agent 回看 trace 确认某些过程考察点。返回 `ground_truth_required` 后不得直接结束，也不得把后续用户反馈当作新的 `original_task` 收集。
- 当用户反馈包含“覆盖/考察/请确认过程”等要求时，agent 必须先基于 `trace_window`、`prompt_summary.key_steps` 和 Trace Evidence Map 回看证据，再生成 ground truth JSON；不得把用户反馈原封不动写入 `notes`。
- 用户反馈写成 JSON 后传给 `--ground-truth-file` 或 `--ground-truth-json`，同时必须把第一次响应中的 `trace_window` 通过 `--trace-window-file` 或 `--trace-window-json` 传回；在 PowerShell 等容易剥离内联 JSON 引号的 shell 中优先使用文件形式。ground truth 必需字段为 `task_completed`、`adjudicated_outcome`、`result_gaps`、`process_gaps`、`missed_steps`、`notes`、`confidence`；`reviewer` 固定为 `user`，`reviewed_at` 可由脚本补入 ISO8601 时间。
- ground truth 字段语义固定：`result_gaps` 只写最终结果缺失，结果正确则写 `none`；`process_gaps` 只写未确认、漏做或错做的过程点，全部确认则写 `none`；`missed_steps` 只写目标 Skill 该覆盖但未覆盖的步骤，没有则写 `none`；`notes` 写 agent 的过程核验结论，并带可复核 `trace_ref`（例如 `T009-T012`），不要写成用户原话。
- 如果 `notes` 提到确认、覆盖、考察、回看、步骤或证据等过程核验点但没有 `trace_ref` 或 `not_observed` 证据，统一入口会返回 `status: invalid_ground_truth`，不得保存 rollout。
- `task_completed` 只能是 `yes | partial | no | blocked | unknown`；`adjudicated_outcome` 只能是 `success | partial | failure | blocked | not_verified`；`confidence` 只能是 `high | medium | low`。
- 若 ground truth 缺字段或枚举非法，统一入口返回 `status: invalid_ground_truth`，不得保存 rollout。
- 若已提供 ground truth 但缺少 `trace_window`，统一入口返回 `status: trace_window_required`，不得保存 rollout；若 `trace_window` 无法解析、来源不匹配或证据锚点找不到，返回 `status: invalid_trace_window`，不得保存 rollout。
- `Rollout Record` 必须双轨保留 outcome：`trace_outcome` 记录自动推断，`adjudicated_outcome` 记录用户 yi*，顶层 `outcome` 等于 `adjudicated_outcome`，`outcome_source` 写 `ground_truth`，`ground_truth_status` 写 `provided`。
- 若 `trace_outcome` 与 `adjudicated_outcome` 冲突，不在采集阶段消解；后续治理 Skill 必须在摘要中列出冲突，并以用户 yi* 作为优先证据。

## Adapter 边界

- 内置 adapter：Codex。读取 UTF-8 JSONL，自动发现路径为 `~/.codex/sessions/**/rollout-*.jsonl`，按 `session_meta.cwd` 匹配当前工作区，解析公开的消息、工具调用、工具输出、patch 结果和任务完成事件。
- 内置 adapter：Trae。读取 Trae CLI 结构化 session（Windows 默认路径 `%LOCALAPPDATA%/trae-cli/sessions/<session_id>/events.jsonl` 与 `traces.jsonl`）以及 Trae CN renderer 可审计日志（Windows 默认路径 `%APPDATA%/Trae CN/logs/**/renderer.log`）；自动发现时只按 `session.json.metadata.cwd` 或 renderer 日志中的 `targetFolderPath`/`workspaceFolders` 精确匹配当前 `--workspace`，显式 `--trace-file` 可传入 session 目录、`events.jsonl`、`traces.jsonl` 或 `renderer.log`。Trae adapter 只解析原始用户输入、公开助手消息、工具展示、文件工具、命令调用、命令结果和终端 trace，不采集 `system-reminder`、`prompt.last_context`、`system_reminders` 等隐藏/上下文状态。
- 通用 adapter：generic。只在用户显式提供可读日志、JSONL 或 Markdown 文件时做弱解析；不要自动扫描任意工具目录。
- 只采集公开可审计事件：用户请求、公开响应、工具调用、工具输出、patch 结果、产物路径、日志和验证命令。
- 禁止采集或复述 `reasoning`、system/developer 指令、`base_instructions`、隐藏上下文和不可公开推理链。

统一 `Trace Event` 字段为：

```json
{
  "runtime": "<runtime>",
  "session_id": "<session id or generic>",
  "source_path": "<trace or log file>",
  "timestamp": "<event time or null>",
  "event_type": "user_message | agent_message | tool_call | tool_output | patch | verification | task_complete",
  "tool_name": "<tool name or empty>",
  "status": "success | failure | observed | pending",
  "input_summary": "<public input summary>",
  "output_summary": "<public output summary>",
  "trace_ref": "T001",
  "evidence_ref": "<raw audit anchor>",
  "warnings": []
}
```

`trace_ref` 是 `Rollout Record` 主表使用的短引用，按事件顺序编号为 `T001`、`T002`。`evidence_ref` 是回到原始 trace/log 的审计锚点，可能较长，只能放在 `Trace Evidence Map` 中，不要直接写进 `Observable Steps`。

## Rollout 生成规则

- `target_skill` 必须来自用户请求、明确触发的目标 Skill，或 `--target-skill` 参数；无法确定时写 `unknown`。
- `collect_trace.py` 可输出整条 session；`collect_rollout.py` 首次摘要时选择当前任务事件并生成稳定 `trace_window`，最终保存时必须按该 `trace_window` 截取同一段事件，避免用户验收反馈或后续任务污染当前 rollout。
- `task_id` 优先使用用户显式值；否则从用户原始任务主题生成稳定短名，避免包含敏感路径或大段文本。
- `rollout_id` 格式为 `<target_skill>-YYYYMMDD-HHMMSS-001`；若目标文件已存在，递增末尾序号并同步正文。
- `Observable Steps.trace_ref` 只写短引用，如 `T001`、`T002-T004` 或 `not_observed`。
- `Trace Evidence Map` 维护短 `trace_ref` 到原始 `evidence_ref` 的映射，保证主表可读且证据可追溯。
- 只记录可复核事实：用户请求、公开决策依据、工具/命令、输入输出摘要、文件产物、测试、错误日志和交付结果。
- 工具 stdout/stderr 只写可读摘要；若输出疑似编码损坏、终端错码或只是文件正文 dump，主表写省略原因，原始证据只通过 `evidence_ref` 回溯。
- 缺失信息写 `unknown`、`not_observed` 或 `not_verified`；不得编造事实。

## Outcome 判定

| outcome | 判定规则 |
| --- | --- |
| `success` | 任务完成，且 trace 或显式证据中有测试、构建、lint、标准答案或用户验收至少一种通过。 |
| `partial` | 有可用产物或部分目标完成，但仍有未完成项。 |
| `failure` | 有明确验证失败、错误结果、崩溃日志或产物不符合要求。 |
| `blocked` | 因缺权限、缺工具、环境不可用或必要信息缺失无法继续。 |
| `not_verified` | 看似完成，但没有可观察验证证据；没有验证证据时不得写成 `success`。 |

trace 自动判定只能写入 `trace_outcome`。最终顶层 `outcome` 必须来自用户 ground truth 的 `adjudicated_outcome`；缺少 ground truth 时不得保存 rollout。

`collection_confidence` 判定：

- `high`：内置结构化 adapter 与当前工作区精确匹配，且关键步骤有 `evidence_ref`。
- `medium`：显式 trace 或日志可关联任务，但来源为弱解析、工作区近似匹配或部分步骤缺证据。
- `low`：仅来自当前会话摘要、不可结构化日志或人工回忆式整理。

## Rollout Record 模板

```markdown
## Rollout Record

- rollout_id: <target_skill-YYYYMMDD-HHMMSS-001>
- target_skill: <被治理 Skill 名称>
- task_id: <同一任务多次执行时保持一致；未知则从任务主题生成稳定短名>
- outcome: success | partial | failure | blocked | not_verified
- trace_outcome: success | partial | failure | blocked | not_verified
- adjudicated_outcome: success | partial | failure | blocked | not_verified
- outcome_source: ground_truth
- ground_truth_status: provided
- trace_runtime: codex | trae | generic | manual
- trace_source: <trace 文件、session id、日志路径或 not_observed>
- collection_confidence: high | medium | low
- original_task: <用户原始任务>
- key_constraints: <用户要求、环境限制、禁止事项；没有则写 none>
- skill_used: <目标 Skill 与辅助 Skill；没有则写 none>
- summary: <交付物、验证结果和未完成项的一句话摘要>

### Observable Steps

| step | trace_ref | action/tool | input/params | public rationale | observed result | used_experience |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | <T001、T002-T004 或 not_observed> | <操作或工具调用> | <参数、文件、输入或 none> | <公开依据；不可写隐藏推理链> | <观察到的结果> | <经验 ID、使用阶段和效果；没有则写 none> |

### Trace Evidence Map

| trace_ref | event_type | tool/status | evidence_ref | summary |
| --- | --- | --- | --- | --- |
| T001 | <Trace Event.event_type> | <tool_name/status> | <原始审计锚点> | <可公开摘要> |

### Artifacts

- <产物、报告、截图、日志、文件路径；没有则写 none>

### Verification

- <测试、构建、lint、标准答案对比、用户验收；没有则写 not_verified>

### Ground Truth (yi*)

- reviewer: user
- reviewed_at: <ISO8601>
- task_completed: yes | partial | no | blocked | unknown
- adjudicated_outcome: success | partial | failure | blocked | not_verified
- result_gaps: <none 或用户列出的结果缺失>
- process_gaps: <none 或 agent 漏掉/错做的步骤>
- missed_steps: <none 或目标 Skill 未覆盖步骤>
- notes: <agent 基于 trace_ref 的过程核验结论；没有则写 none>
- confidence: high | medium | low

### Failure Or Detour

- <记录探索、调试、错误、backtracking、blocked 原因及影响；没有则写 none>

### Transferable Observations

- pattern: <可复用流程、工具模式、失败规避或验收规则；没有则写 none>
  generality: high | medium | low
  source_steps: <如 S2-S4；优先标注关键路径步骤>
```

## 持久化规则

- 保存根目录固定为 `.agents/skills/cangjie-rollout-collector/records/rollouts/`。
- 保存路径固定为 `.agents/skills/cangjie-rollout-collector/records/rollouts/<target_skill>/<task_id>/<rollout_id>.md`。
- `target_skill`、`task_id` 和 `rollout_id` 只能用于文件路径时保留字母、数字、点、下划线和连字符；空格、斜杠、反斜杠、冒号和其他不安全字符替换为 `-`；无法确定时使用 `unknown`。
- 若目录不存在，先创建目录；用 UTF-8 写入完整 `Rollout Record` Markdown。
- 最终响应中说明保存路径。保存 rollout 不等于写入治理结果；不得修改目标 Skill 或其他治理产物。

## 最小检查清单

- 已优先尝试统一 collector 入口；失败时已记录 fallback 原因和 `collection_confidence`。
- 已输出统一的 `Rollout Record`。
- 每个可观察步骤都有短 `trace_ref` 或显式 `not_observed`，主表没有长审计锚点。
- 主表没有展开疑似编码损坏的 stdout/stderr；如需追溯，已通过 `Trace Evidence Map.evidence_ref` 保留原始锚点。
- `Trace Evidence Map` 已保留短 `trace_ref` 到原始 `evidence_ref` 的映射。
- `outcome` 按判定表选择，未验证结果不得写成 `success`。
- 未提供 ground truth 时统一入口只返回 `ground_truth_required`，没有写入 rollout 文件。
- `ground_truth_required` 响应已包含 `trace_window`；最终保存前已复用同一个 `trace_window`，且 `original_task` 与首次摘要一致。
- 若用户反馈要求确认过程考察点，最终保存前已回看 `prompt_summary.key_steps`/Trace Evidence Map，并把核验结论写入 `notes`，带 `trace_ref` 或 `not_observed`；没有把用户反馈原文直接写入 `notes`。
- `result_gaps`、`process_gaps`、`missed_steps` 已按字段语义拆开：结果缺失、过程问题、目标 Skill 漏覆盖分别记录，全部确认则写 `none`。
- 已提供 ground truth 但缺少或无法匹配 `trace_window` 时，统一入口只返回 `trace_window_required` 或 `invalid_trace_window`，没有写入 rollout 文件。
- `Rollout Record` 已包含 `trace_outcome`、`adjudicated_outcome`、`outcome_source: ground_truth`、`ground_truth_status: provided` 和 `### Ground Truth (yi*)`。
- `outcome` 等于 `adjudicated_outcome`；trace 自动判断只保留在 `trace_outcome`。
- 缺失信息已显式标注为 `unknown`、`not_observed` 或 `not_verified`。
- 记录只包含可复核事实，没有隐藏推理链。
- 记录已保存到集中目录 `.agents/skills/cangjie-rollout-collector/records/rollouts/`。
- 最终响应说明了保存路径，且没有修改目标 Skill。
