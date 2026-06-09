---
name: cangjie-trace2skill-evolution
description: "当需要治理 Skill 时使用此 Skill：与被治理 Skill 联用时，在目标 Skill 执行完成后采集 Trajectory Record；或读取一条或多条 Trajectory Record，按成功/失败轨迹分析、JSON patch、程序化冲突检测和层级合并进化 Skill。"
---

# 仓颉 Trace2Skill 轨迹进化

## 目的

把目标 Skill 的执行轨迹转化为可审计的 `Trajectory Record`，再从成功和失败轨迹中提取可迁移经验、生成局部补丁，并合并为无冲突的 Skill 修改建议或从零创建草案。

本 Skill 有两种模式：

- 模式 A：采集 Trajectory Record。与被治理 Skill 一起使用时，在目标 Skill 执行完成后自动总结本次执行轨迹，不修改文件。
- 模式 B：补丁提案与合并。读取一条或多条 `Trajectory Record`，生成 memory items、局部 JSON patch、consolidated patch 和审阅摘要；只有用户明确要求写入时才修改目标 Skill。

默认不追问用户补字段。无法从当前上下文、工具输出、文件产物或验证结果观察到的信息，写为 `unknown`、`not_observed` 或 `not_verified`。

## 模式 A：采集 Trajectory Record

在目标 Skill 执行完成后，从当前会话和可观察产物中生成轨迹记录。模式 A 是执行后的记录器，不是执行前表单。

### Stage 1 编排：Trajectory Collector

执行模式 A 时，直接切换为 `Trajectory Collector` 角色，并按以下约束生成记录：

- Role：作为已完成目标 Skill 执行的轨迹采集器。
- Context：只使用当前会话、目标 Skill、用户任务、可观察工具调用、产物、日志和验证结果。
- Task：基于可观察事实生成 `Trajectory Record`。
- Rules：不要询问用户补字段；缺失信息标为 `unknown`、`not_observed` 或 `not_verified`；不得编造事实；不得记录隐藏推理链。
- Output：严格输出符合本 Skill schema 的 `Trajectory Record`。

### 采集规则

- 自动识别 `target_skill`：优先使用本轮明确触发的被治理 Skill；无法唯一识别时写 `unknown`。
- 自动生成 `trace_id`：格式为 `<target_skill>-YYYYMMDD-HHMMSS-001`；同一秒内多条记录递增末尾序号。
- 自动生成 `task_id`：从用户原始任务主题提取稳定短名，避免包含敏感路径或大段文本。
- 只记录可复核事实：用户请求、公开决策依据、工具/命令、输入输出、文件产物、测试和错误日志。
- 不记录隐藏推理链；如需说明依据，只写可公开、可审计的简短 rationale。

### Outcome 判定

| outcome | 判定规则 |
| --- | --- |
| `success` | 任务完成，且测试、构建、lint、标准答案或用户验收中至少一种通过。 |
| `failure` | 有明确验证失败、错误结果、崩溃日志或产物不符合要求。 |
| `partial` | 有可用产物或部分目标完成，但仍有未完成项。 |
| `blocked` | 因缺权限、缺工具、环境不可用或必要信息缺失无法继续。 |
| `not_verified` | 看似完成，但没有可观察验证证据。 |

### 输出契约

```markdown
## Trajectory Record

- trace_id: <target_skill-YYYYMMDD-HHMMSS-001>
- target_skill: <被治理 Skill；未知写 unknown>
- task_id: <稳定短名>
- outcome: success | failure | partial | blocked | not_verified
- original_task: <用户原始任务>
- skill_used: <目标 Skill 与辅助 Skill；没有则写 none>

### Observable Steps

| step | action/tool | input/params | public rationale | observed result |
| --- | --- | --- | --- | --- |
| S1 | <工具或操作> | <参数摘要> | <公开依据；不可写隐藏推理链> | <可观察结果> |

### Artifacts

- <产物、报告、截图、日志、文件路径；没有则写 none>

### Verification

- <测试、构建、lint、标准答案对比、用户验收；没有则写 not_verified>

### Failure Or Detour

- <失败、绕路、回退、阻塞；没有则写 none>

### Transferable Observations

- <可迁移流程、防错点或待验证经验；没有则写 none>
```

## 模式 B：补丁提案与合并

模式 B 读取一条或多条 `Trajectory Record`，按“分组分流 -> Stage 2 角色分析 -> Stage 3 程序化预检 -> Merge Operator 合并 -> 程序化复检”的顺序执行。先按 `target_skill` 分组；不同目标 Skill 不得混合合并。每组内按 outcome 分流：

- `success` 进入 Success Analyst，提取可泛化成功模式。
- `failure` 进入 Error Analyst，诊断失败表面、行为根因和最小验证。
- `partial` 只提取已验证有效部分，默认 `pending`。
- `blocked` 只提取阻塞规避建议，默认 `pending`。
- `not_verified` 只能产生 `pending` 建议，不得直接进入 `accepted` patch。

默认只输出补丁建议。只有用户明确要求写入时，才编辑目标 Skill 文件。

### Stage 2：逐轨迹补丁提案

每条轨迹必须独立分析，不能提前读取其他轨迹的补丁来影响当前结论。

对 `success` 轨迹，切换为 `Success Analyst`：

- Role：作为成功模式分析师。
- Mission：从一条成功 `Trajectory Record` 中识别促成成功的可泛化行为。
- Requirements：覆盖有效行为；优先处理高频或适用面更广的模式；把罕见细节吸收到更通用规则中；避免任务特例化常量。
- Workflow：清理轨迹，只保留可复核行为、工具调用、产物和验证结果；识别通用成功模式；生成 `success` memory items 和局部 patch items。
- Output：输出符合 schema 的 `success` memory items 与 local JSON patch items。

对 `failure` 轨迹，切换为 `Error Analyst`：

- Role：作为失败分析师。
- Mission：基于失败轨迹、日志、产物和验证结果，诊断失败原因并提出可泛化 Skill 修改。
- Workflow：先理解失败表面，明确输出、日志、验证或产物哪里不符合要求；再追溯行为根因，定位导致失败的工具、命令、文件编辑、流程遗漏或判断错误；然后做最小修复验证；最后重新评估因果关系。
- Tool boundary：允许读取文件、检查日志、对比标准答案、运行非破坏性验证命令；默认不修改目标 Skill。
- Gate：若无法验证因果根因，相关 memory 和 patch 必须标为 `pending` 或 `rejected`，不得把未经验证的诊断升级为 `accepted` patch。
- Output：输出符合 schema 的 `failure` memory items 与 local JSON patch items。

最小修复验证应使用临时副本、dry-run、隔离产物或明确不会污染目标 Skill 的方式完成。不得把未经验证的失败归因写成硬性规则。

### Memory Item Schema

每个 memory item 是轨迹级可迁移经验，用于支撑 patch，不直接写入目标 Skill。

```json
{
  "id": "M-<trace_id>-001",
  "type": "success | failure",
  "content": "<一句话可迁移经验，建议不超过 80 中文字>",
  "condition": "<适用条件>",
  "boundary": "<不适用或需复核条件>",
  "source_trace": "<trace_id>",
  "evidence": "<可观察证据摘要>",
  "status": "accepted | pending | rejected"
}
```

状态规则：

- `accepted`：证据可复核，且验证或多轨迹支持足以进入合并候选。
- `pending`：有启发但缺少验证、根因不完整或只来自 `not_verified`/`partial`/`blocked`。
- `rejected`：与证据冲突、过度特例化、无法复现或会误导目标 Skill。

### Local Patch Item Schema

Stage 2 的局部补丁必须统一输出 JSON，便于 Stage 3 做程序化检查。

```json
{
  "patch_id": "P-<trace_id>-001",
  "source_trace": "<trace_id>",
  "analyst_type": "success | error",
  "memory_ids": ["M-<trace_id>-001"],
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

### Stage 3：程序化预检与层级合并

Stage 3 先做程序化预检，再把通过预检的 patch 交给 `Merge Operator`，最后做合并后程序化复检。Codex 单 Agent 默认 `B_merge = 8`；并行多 Agent 场景可使用 `32`。补丁较多时，分批合并后再合并批次结果。

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
- Bias：多条独立轨迹复现的模式优先保留，并抽象为稳定通用规则。
- Output：输出 consolidated JSON patch 和 Markdown review summary。

Merge Operator 必须遵守：

- 去重：相同或高度相似修改只保留最清晰、最可执行版本。
- 裁决冲突：证据更强、验证更完整、多轨迹复现的修改优先。
- 保留独特洞见：不同轨迹揭示的非冗余失败或成功模式应保留。
- 保持简洁：合并结果不应膨胀为轨迹摘要集合。
- 行级独立：合并后的编辑不得重叠同一行、同一标题块或同一 passage。
- 高频优先：多条独立轨迹复现的模式优先抽象为稳定通用规则。

LLM 合并后再次执行程序化检查，确认无重叠编辑、无 stale anchor、无断裂引用、无孤立 `references/*.md` 或孤立链接。

### Create/Link 原子对

`references/*.md` 与 `SKILL.md` 中的链接或加载说明必须同生同灭：

- 若 patch 新建 `references/*.md`，必须同时有 `link_reference` 在 `SKILL.md` 中加入对应链接或加载说明。
- 若合并时丢弃新建文件，必须同时丢弃链接。
- 若保留链接，必须保留对应文件。
- 原子对不完整时，该组编辑进入 `pending`，不得写入。

### Stage 3 输出

````markdown
## Consolidated Patch

### Decision Summary

- accepted: <数量和理由摘要>
- pending: <数量和阻塞原因>
- rejected: <数量和拒绝原因>
- stale/conflict: <程序化预检结果>

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

当目标 Skill 不存在时，模式 B 进入 creation branch：

- Stage 2 仍基于轨迹产生 memory items 和 patch items。
- Stage 3 不生成局部 diff，而是生成完整 `SKILL.md` 草案。
- 新 Skill 草案必须包含 frontmatter、适用场景、执行流程、验证方式和边界条件。
- creation branch 默认只输出草案；写入目录必须由用户明确要求。

## 写入与验证

只有用户明确要求写入时，才把 consolidated patch 应用到目标 Skill。写入时只应用 `accepted` 且通过合并后程序化检查的编辑。

写入后尽可能验证：

```powershell
skill-lint --path .agents\skills\<target-skill>
```

若新增或修改 eval，应再运行真实 agent eval；不可用时必须说明阻塞，不得用关键词检查冒充行为验证。

## 与 XSkill Rollout 的关系

`Trajectory Record` 不等同于 `cangjie-xskill-evolution` 的 `Rollout Summary`。v1 不自动转换。

需要混用时，可按轻量映射人工转换：

| Trajectory Record | Rollout Summary |
| --- | --- |
| `target_skill` | `target_skill` |
| `task_id` | `task_id` |
| `outcome` | `outcome` |
| `original_task` | `原始任务` |
| `observable_steps` | `步骤表` |
| `artifacts` / `verification` | `最终结果` |
| `failure_or_detour` | `失败、绕路与回退` |

## 最小检查清单

- 模式 A 不要求用户补字段，且缺失信息有显式标注。
- `outcome` 按判定表选择，未验证结果不得写成 `success`。
- 每个 memory item 字段完整，并被 patch 通过 `memory_ids` 正确引用。
- Stage 2 局部 patch 使用统一 JSON schema。
- Stage 3 已执行程序化预检和合并后检查。
- `create_file` 与 `link_reference` 原子对完整。
- 只有 `accepted` 且验证充分的知识进入目标 Skill 修改。
- 写入前有明确用户授权；写入后运行 `skill-lint` 或说明无法运行的原因。
