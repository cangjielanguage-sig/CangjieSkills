---
name: cangjie-trace2skill-evolution
description: "当需要治理 Skill 时使用此 Skill：读取 cangjie-rollout-collector 生成的一条或多条 Rollout Record，按成功/失败 rollout 分析、JSON patch、程序化冲突检测和层级合并进化 Skill。"
---

# 仓颉 Trace2Skill Rollout 进化

## 目的

读取可审计的 `Rollout Record`，再从成功和失败 rollout 中提取可迁移经验、生成局部补丁，并合并为无冲突的 Skill 修改建议或从零创建草案。采集和保存 rollout 使用 `cangjie-rollout-collector`，本 Skill 不执行采集持久化。

本 Skill 的职责是补丁提案与合并：

- 读取一条或多条 `Rollout Record`（默认从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 查找），生成 memory items、局部 JSON patch、consolidated patch 和审阅摘要；只有用户明确要求写入时才修改目标 Skill。

## 补丁提案与合并

读取一条或多条 `Rollout Record`。输入可以是粘贴文本或用户指定文件；未指定输入时，优先读取 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 下与用户指定 `target_skill` / `task_id` 匹配的 Markdown。按“分组分流 -> 阶段 1 角色分析 -> 阶段 2 程序化预检 -> Merge Operator 合并 -> 程序化复检”的顺序执行。先按 `target_skill` 分组；不同目标 Skill 不得混合合并。

读取 `Rollout Record` 时必须先执行 ground truth/yi* gate：

- 若存在 `ground_truth_status: provided`、`outcome_source: ground_truth`、`adjudicated_outcome` 与 `### Ground Truth (yi*)`，按 `adjudicated_outcome` 分流；`trace_outcome` 只作为审计和冲突说明。
- 若缺少 `ground_truth_status: provided`、缺少 `outcome_source: ground_truth`、缺少 `adjudicated_outcome` 或没有 `### Ground Truth (yi*)`，标记为 `invalid_rollout_schema`；该 rollout 必须跳过并写入 Decision Summary，不得产生 memory/patch，也不得进入 consolidated accepted patch。
- 若 `trace_outcome` 与 `adjudicated_outcome` 冲突，Decision Summary 必须列出冲突；当 ground truth `confidence: low` 或 trace 中有明确失败证据时，相关 memory/patch 保持 `pending`。

每组内按有效 outcome（优先 `adjudicated_outcome`）分流：

- `success` 进入 Success Analyst，提取可泛化成功模式。
- `failure` 进入 Error Analyst，诊断失败表面、行为根因和最小验证。
- `partial` 只提取已验证有效部分，默认 `pending`。
- `blocked` 只提取阻塞规避建议，默认 `pending`。
- `not_verified` 只能产生 `pending` 建议，不得直接进入 `accepted` patch。

默认只输出补丁建议。只有用户明确要求写入时，才编辑目标 Skill 文件。

### 阶段 1：逐 Rollout 补丁提案

每条 rollout 必须独立分析，不能提前读取其他 rollout 的补丁来影响当前结论。

对 `success` rollout，切换为 `Success Analyst`：

- Role：作为成功模式分析师。
- Mission：从一条成功 `Rollout Record` 中识别促成成功的可泛化行为。
- Requirements：覆盖有效行为；优先处理高频或适用面更广的模式；把罕见细节吸收到更通用规则中；避免任务特例化常量。
- Workflow：清理 rollout，只保留可复核行为、工具调用、产物和验证结果；识别通用成功模式；生成 `success` memory items 和局部 patch items。
- Output：输出符合 schema 的 `success` memory items 与 local JSON patch items。

对 `failure` rollout，切换为 `Error Analyst`：

- Role：作为失败分析师。
- Mission：基于失败 rollout、日志、产物和验证结果，诊断失败原因并提出可泛化 Skill 修改。
- Workflow：先理解失败表面，明确输出、日志、验证或产物哪里不符合要求；再追溯行为根因，定位导致失败的工具、命令、文件编辑、流程遗漏或判断错误；然后做最小修复验证；最后重新评估因果关系。
- Tool boundary：允许读取文件、检查日志、对比标准答案、运行非破坏性验证命令；默认不修改目标 Skill。
- Gate：若无法验证因果根因，相关 memory 和 patch 必须标为 `pending` 或 `rejected`，不得把未经验证的诊断升级为 `accepted` patch。
- Output：输出符合 schema 的 `failure` memory items 与 local JSON patch items。

最小修复验证应使用临时副本、dry-run、隔离产物或明确不会污染目标 Skill 的方式完成。不得把未经验证的失败归因写成硬性规则。

### Memory Item Schema

每个 memory item 是 rollout 级可迁移经验，用于支撑 patch，不直接写入目标 Skill。

```json
{
  "id": "M-<rollout_id>-001",
  "type": "success | failure",
  "content": "<一句话可迁移经验，建议不超过 80 中文字>",
  "condition": "<适用条件>",
  "boundary": "<不适用或需复核条件>",
  "source_rollout": "<rollout_id>",
  "evidence": "<可观察证据摘要>",
  "status": "accepted | pending | rejected"
}
```

状态规则：

- `accepted`：证据可复核，且验证或多 rollout 支持足以进入合并候选。
- `pending`：有启发但缺少验证、根因不完整或只来自 `not_verified`/`partial`/`blocked`。
- `rejected`：与证据冲突、过度特例化、无法复现或会误导目标 Skill。

### Local Patch Item Schema

阶段 1 的局部补丁必须统一输出 JSON，便于阶段 2 做程序化检查。

```json
{
  "patch_id": "P-<rollout_id>-001",
  "source_rollout": "<rollout_id>",
  "analyst_type": "success | error",
  "memory_ids": ["M-<rollout_id>-001"],
  "target_file": "SKILL.md",
  "target_section": "<目标标题或 section；创建文件时可为 null>",
  "operation": "insert_after | replace | delete | create_file | link_reference",
  "anchor": "<精确锚点、标题或行范围>",
  "old_content": "<replace/delete 时需要；其他操作可为 null>",
  "new_content": "<新增或替换内容>",
  "evidence": "<支持该修改的证据>",
  "boundary": "<不适用或需人工复核条件>",
  "verification": "<验证方式或 pending 原因>",
  "status": "accepted | pending | rejected"
}
```

`memory_ids` 必须引用同批次已定义的 memory item。引用不存在时，该 patch 进入 `pending`。

### 阶段 2：程序化预检与层级合并

阶段 2 先做程序化预检，再把通过预检的 patch 交给 `Merge Operator`，最后做合并后程序化复检。Codex 单 Agent 默认 `B_merge = 8`；并行多 Agent 场景可使用 `32`。补丁较多时，分批合并后再合并批次结果。

LLM 合并前先执行程序化冲突预检：

- `target_file` 不存在，且操作不是 `create_file` 时，标为 `stale`。
- `anchor`、`target_section` 或 `old_content` 在当前文件中找不到时，标为 `stale`。
- 同一文件同一行、同一标题块或同一文本段被多个 patch 修改时，标为 `conflict`。
- `memory_ids` 引用缺失时，标为 `pending`。
- `create_file` 与 `link_reference` 必须满足原子对规则。

只把 `accepted` 且通过预检的 patch 交给合并算子。`pending`、`rejected`、`stale`、`conflict` 需要进入决策摘要，不得静默丢失。

对通过预检的 patch，切换为 `Merge Operator`：

- Role：作为 Skill edit coordinator。
- Inputs：只接收通过程序化预检的 local patch items。
- Rules：去重；裁决冲突；保留独特洞见；保持编辑简洁；保持行级独立；成对处理 `create_file` 与 `link_reference`。
- Bias：多条独立 rollout 复现的模式优先保留，并抽象为稳定通用规则。
- Output：输出 consolidated JSON patch 和 Markdown review summary。

Merge Operator 必须遵守：

- 去重：相同或高度相似修改只保留最清晰、最可执行版本。
- 裁决冲突：证据更强、验证更完整、多 rollout 复现的修改优先。
- 保留独特洞见：不同 rollout 揭示的非冗余失败或成功模式应保留。
- 保持简洁：合并结果不应膨胀为 rollout 摘要集合。
- 行级独立：合并后的编辑不得重叠同一行、同一标题块或同一 passage。
- 高频优先：多条独立 rollout 复现的模式优先抽象为稳定通用规则。

LLM 合并后再次执行程序化检查，确认无重叠编辑、无 stale anchor、无断裂引用、无孤立 `references/*.md` 或孤立链接。

### Create/Link 原子对

`references/*.md` 与 `SKILL.md` 中的链接或加载说明必须同生同灭：

- 若 patch 新建 `references/*.md`，必须同时有 `link_reference` 在 `SKILL.md` 中加入对应链接或加载说明。
- 若合并时丢弃新建文件，必须同时丢弃链接。
- 若保留链接，必须保留对应文件。
- 原子对不完整时，该组编辑进入 `pending`，不得写入。

### 阶段 2 输出

````markdown
## Consolidated Patch

### Decision Summary

- accepted: <数量和理由摘要>
- pending: <数量和阻塞原因>
- rejected: <数量和拒绝原因>
- stale/conflict: <程序化预检结果>
- ground truth: provided <n>, invalid_rollout_schema <n>, outcome_conflict <n>

### Consolidated JSON Patch

```json
[
  {
    "patch_id": "CP-001",
    "source_patches": ["P-..."],
    "target_file": "SKILL.md",
    "operation": "insert_after",
    "anchor": "<目标锚点>",
    "new_content": "<合并后的内容>",
    "verification": "<写入后验证方式>"
  }
]
```

### Markdown Review

- <给人类审阅的修改摘要、风险和验证建议>
````

### 从零创建分支

当目标 Skill 不存在时，进入 creation branch：

- 阶段 1 仍基于 rollout 产生 memory items 和 patch items。
- 阶段 2 不生成局部 diff，而是生成完整 `SKILL.md` 草案。
- 新 Skill 草案必须包含 frontmatter、适用场景、执行流程、验证方式和边界条件。
- creation branch 默认只输出草案；写入目录必须由用户明确要求。

## 写入与验证

只有用户明确要求写入时，才把 consolidated patch 应用到目标 Skill。写入时只应用 `accepted` 且通过合并后程序化检查的编辑。

缺少 ground truth/yi* 的 rollout 必须作为 `invalid_rollout_schema` 跳过，不得产生 memory/patch。存在未消解 outcome 冲突时，低置信度 ground truth 或 trace 中有明确失败证据的冲突项只能保留在 pending 决策摘要中。

写入后尽可能验证：

```powershell
skill-lint --path .agents\skills\<target-skill>
```

若新增或修改 eval，应再运行真实 agent eval；不可用时必须说明阻塞，不得用关键词检查冒充行为验证。

## 最小检查清单

- 采集 rollout 已交给 `cangjie-rollout-collector`；本 Skill 只处理已有 `Rollout Record`。
- 未指定输入时，只从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 自动查找 rollout。
- `outcome` 按判定表选择，未验证结果不得写成 `success`。
- 已执行 ground truth/yi* gate；不满足 gate 的 rollout 已标记为 `invalid_rollout_schema` 并跳过，未产生 memory/patch。
- `trace_outcome` 与 `adjudicated_outcome` 冲突已写入 Decision Summary，低置信度或有明确失败证据的冲突 patch 未进入 consolidated accepted patch。
- 每个 memory item 字段完整，并被 patch 通过 `memory_ids` 正确引用。
- 阶段 1 局部 patch 使用统一 JSON schema。
- 阶段 2 已执行程序化预检和合并后检查。
- `create_file` 与 `link_reference` 原子对完整。
- 只有 `accepted` 且验证充分的知识进入目标 Skill 修改。
- 写入前有明确用户授权；写入后运行 `skill-lint` 或说明无法运行的原因。
