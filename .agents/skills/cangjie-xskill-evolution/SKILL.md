---
name: cangjie-xskill-evolution
description: "当需要基于双流框架治理已有仓颉 Skill 时使用此 Skill：读取 cangjie-rollout-collector 生成的一个或多个 Rollout Record，按 target_skill 与 task_id 分组生成技能流 delta K 和经验流 delta e，输出治理建议；用户明确要求写入时更新目标 Skill。"
---

# 仓颉 XSkill 双流进化

## 目的

使用双流思想治理已有仓颉 Skill：技能流沉淀稳定任务级流程，经验流沉淀上下文敏感的动作级建议。本 Skill 处理文本 rollout、工具调用、失败/回退和可迁移知识。采集和保存 rollout 使用 `cangjie-rollout-collector`，本 Skill 不执行采集持久化。

本 Skill 的职责是双流治理：

- 读取一条或多条 `Rollout Record`（默认从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 查找），生成 `delta K` 与 `delta e`，输出治理建议；只有用户明确要求写入时才修改目标 Skill。

## 治理 Skill

输入可以是粘贴的 `Rollout Record` Markdown，也可以是用户指定的 rollout 文件。未指定输入时，优先读取 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 下与用户指定 `target_skill` / `task_id` 匹配的 Markdown。先按 `target_skill` 分组，分别执行治理流程并分别输出审计摘要；每个 `target_skill` 组内再按 `task_id` 分组做跨 rollout 分析，禁止把不同 Skill 的 `delta K` 或 `delta e` 混在一起。

读取 `Rollout Record` 时必须先执行 ground truth/yi* gate：

- 若存在 `ground_truth_status: provided`、`outcome_source: ground_truth`、`adjudicated_outcome` 与 `### Ground Truth (yi*)`，后续分组和双流治理使用 `adjudicated_outcome` 作为有效 outcome；`trace_outcome` 只作为冲突审计证据。
- 若缺少 `ground_truth_status: provided`、缺少 `outcome_source: ground_truth`、缺少 `adjudicated_outcome` 或没有 `### Ground Truth (yi*)`，标记为 `invalid_rollout_schema`；该 rollout 必须跳过并写入摘要，不得产生 `delta K` / `delta e`，也不得写入目标 Skill 或经验库。
- 若 `trace_outcome` 与 `adjudicated_outcome` 冲突，治理摘要必须列出冲突；当 ground truth `confidence: low` 或 trace 中有明确失败证据时，相关 `delta K` / `delta e` 保持 `pending`。

读取 rollout 时先做容错检查：

- 缺少必含字段时，不从上下文补全；标记为 `invalid_rollout_schema` 并跳过。
- 缺少字段时，在治理输出中列出缺失字段并跳过该条 rollout。
- 单条 rollout 格式错误不得中断其他 rollout 的治理。

### 多 Rollout 分组规则

以下规则按有效 outcome（优先 `adjudicated_outcome`）执行。

- 同一 `task_id` 有 2 条及以上 rollout，且包含不同 `outcome` 时，执行完整 cross-rollout critique。
- 只有 `success`：提取候选有效流程，默认标为 `pending`，除非另有独立验证。
- 只有 `failure`：只提取规避型经验或防错候选，不写入稳定主流程。
- `partial`：提取有效部分，标注未完成步骤和不达标结果，整体默认 `pending`。
- `blocked`：视为 failure 子类，只提取阻塞规避经验，不提取流程候选。
- `not_verified`：只产生 `pending` 建议，不得直接进入 `accepted` 的 `delta K` 或 `delta e`。

## 技能流：生成并治理 Delta K

技能流处理任务级稳定知识，最终落位是目标 Skill 的 `SKILL.md`。先使用 JSON 操作中间态，再转成 Markdown 修改建议或写入结果。

### 1. Generate Raw Skill

参照 `GENERATE RAW SKILL PROMPT` 的思想，从 rollout 中提取原始技能片段：

- 从成功模式提取有效工作流、工具顺序和验收动作。
- 从失败、绕路、回退中提取防错补丁。
- 将具体路径、文件名、项目名、样例数据替换为占位符。
- 只保留可执行知识：步骤、工具模板、边界、验证方法。

输出 `delta K` 操作中间态：

```json
[
  {
    "operation": "add | modify | merge | delete",
    "target_section": "SKILL.md 中的目标章节或 new",
    "content": "拟新增或改写的稳定技能内容",
    "evidence": ["task_id/rollout_id#S2-S4"],
    "status": "accepted | pending | rejected",
    "reason": "证据与治理理由"
  }
]
```

操作含义：

- `add`：新增稳定流程、规则或工具模板。
- `modify`：改写现有步骤、边界或验收规则。
- `merge`：合并重叠流程或重复章节。
- `delete`：删除被反证、冗余或过具体内容。

### 2. Merge Skill

参照 `MERGE SKILL PROMPT` 的思想合并 `delta K`：

- 更准确的新内容改写旧内容。
- 冗余或过具体内容删除。
- 互补内容合并成更通用规则。
- 真正不同的流程保留为变体，但同一节内最多保留少量必要变体。
- 保留可复用工具模板，删除一次性案例叙述。

### 3. Skill Manage

参照 `SKILL MANAGE PROMPT` 的思想治理目标 `SKILL.md`：

- 稳定知识进入主文件；上下文敏感建议不得写成无条件规则。
- 若更新后单节超过约 2000 中文字、正文明显膨胀或出现重复流程，先合并、泛化、删冗余，不直接追加。
- 主文件只保留高频、稳定、可执行、可验证的内容。

稳定知识进入目标 `SKILL.md` 必须同时满足：

- 证据可追溯到具体 rollout。
- 不绑定具体路径、文件名、样例数据或一次性任务。
- 有跨 rollout 对比支持，或有独立验证支撑。
- 能写成可执行步骤、工具模板、失败规避或验收规则。

不满足条件但有价值的内容标为 `pending`；被反证、太具体或低价值的内容标为 `rejected`。

## 经验流：生成并治理 Delta e

经验流处理动作级、上下文敏感知识，最终建议落位是目标 Skill 的 `references/experiences.md`。先使用 JSON 操作中间态，再转成结构化 Markdown 经验条目。

### 1. Cross Rollout Critique

参照 `CROSS ROLLOUT CRITIQUE` 的思想，对同一 `task_id` 的 rollout 做对比：

- 找出成功 rollout 中存在、失败 rollout 中缺失的关键决策。
- 找出失败、partial、blocked rollout 的错误选择、缺失验证或阻塞条件。
- 判断已有经验是否被使用、是否无效、是否需要改写。
- 提取行动级建议，而不是抽象原则。

输出 `delta e` 操作中间态：

```json
[
  {
    "operation": "add | modify | merge | delete",
    "id": "E001 或已有经验 ID",
    "experience": "触发条件开头的短经验",
    "boundary": "适用边界或失效条件",
    "source": ["task_id/rollout_id#S3"],
    "status": "accepted | pending | rejected",
    "reason": "证据与治理理由"
  }
]
```

### 2. Merge Experience

参照 `MERGE PROMPT` 的思想合并经验：

- 触发条件属于同一类场景、动作方向一致、无实质矛盾时合并。
- 合并后保留所有重要信息点，但删除重复表达。
- 有冲突时保持 separate 或 `pending`，并说明冲突。
- 每条经验不超过 100 个中文字符或 64 个英文词；超长必须压缩或拆分。

### 3. Experience Manage

参照 `EXPERIENCE MANAGE PROMPT` 的思想治理经验库：

- `add`：新增未覆盖的上下文敏感经验。
- `modify`：让已有经验更准确、更清晰或更可执行。
- `merge`：合并重复或高度重叠经验。
- `delete`：删除被反证、低价值或只适用一次性场景的经验。
- 只在明确冗余或低质量时删除，保留经验多样性。

经验最终 Markdown 格式：

```markdown
## <ID>

- 触发条件: <When/If/For 风格条件>
- 经验: <不超过 100 个中文字符或 64 个英文词>
- 适用边界: <何时适用，何时不适用>
- 来源 rollout: <task_id/rollout_id#步骤>
- 状态: accepted | pending | rejected
```

经验 ID 默认使用目标 Skill 缩写加自增序号，例如 `E-HMOS-BUILD-001`；无法确定缩写时使用 `E001`。目标 Skill 没有 `references/experiences.md` 时，在治理建议中标注“需新建”；只有用户明确要求写入时才创建文件。

## 经验使用入口治理

治理过程中只要有 `accepted` 的 `delta e` 会新增或更新 `references/experiences.md`，就必须同时检查目标 `SKILL.md` 是否说明如何消费经验。

- 若目标 `SKILL.md` 已有等价说明，保持不变，并在治理摘要中写明“经验入口已存在”。
- 若目标 `SKILL.md` 没有说明，或只创建了 `references/experiences.md` 但未说明如何使用，生成一个配套 `delta K` 的 `add` 或 `modify` 操作，写入目标 `SKILL.md` 的合适位置。
- 该配套 `delta K` 只声明读取、筛选、改写和记录经验的方法，不把具体经验提升为稳定主流程。

目标 `SKILL.md` 的经验使用入口应包含：

- 执行前若存在 `references/experiences.md`，按当前任务会经过的工作流阶段匹配经验；优先使用目标 Skill 已有步骤、章节、检查清单或工具阶段。
- 若目标 Skill 没有明确阶段，退化为 `准备 / 执行 / 验证 / 失败恢复`。
- 只读取状态为 `accepted` 的经验；按触发条件、适用边界和当前上下文筛选，通常最多选用 3 条。
- 经验必须改写为当前任务下的具体动作提醒，不得原样套用。
- 若经验与用户要求或目标 `SKILL.md` 主流程冲突，以用户要求和主流程为准。
- 执行后在 rollout 的“已用经验”字段记录经验 ID、使用阶段和效果。

## 写入与拒写规则

- 用户只要求“总结 rollout”或“保存 rollout”时，交给 `cangjie-rollout-collector`；本 Skill 不执行采集持久化。
- 用户要求“评审”“建议”或“给出治理方案”时，只输出治理建议，不修改文件。
- 用户明确要求“治理”“更新”“改进目标 Skill”且当前会话允许写入时，才修改目标 Skill。
- 原始 rollout、证据文件和用户未授权修改的 Skill 不得改写。
- 没有通过 ground truth/yi* gate 的 rollout 不得支撑 `delta K` 或 `delta e` 生成，也不得写入。
- 没有 `accepted` 的 `delta K` 时，不更新目标 `SKILL.md`。
- 没有 `accepted` 的 `delta e` 时，不创建或更新 `references/experiences.md`。
- 有 `accepted` 的 `delta e` 时，若目标 `SKILL.md` 缺少经验使用入口，必须把入口作为配套 `delta K` 建议或写入；否则不得只创建孤立的 `references/experiences.md`。

## 治理摘要

每次治理结束都输出摘要：

```markdown
## 治理摘要

- target_skill: <名称>
- 使用 rollout: <数量与 ID>
- 跳过 rollout: <缺字段或无法解析的 ID 与原因>
- delta K: added <n>, modified <n>, merged <n>, deleted <n>, pending <n>, rejected <n>
- delta e: added <n>, modified <n>, merged <n>, deleted <n>, pending <n>, rejected <n>
- ground truth: provided <n>, invalid_rollout_schema <n>, conflict <n>
- 建议写入位置: <SKILL.md / references/experiences.md / 无>
- 需新建文件: <路径或无>
- 经验入口: <已存在 / 建议新增 / 已写入 / 不需要，附理由>
- 未采纳原因: <pending/rejected 的主要原因>
- 验证建议: <最小验证、lint、eval 或人工复核>
```

## 最小检查清单

- 已按 `target_skill` 分组，未混合不同 Skill 的知识。
- 采集 rollout 已交给 `cangjie-rollout-collector`；本 Skill 只处理已有 `Rollout Record`。
- 未指定输入时，只从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 自动查找 rollout。
- 每条有效 rollout 都有 `task_id`、`rollout_id`、`target_skill`、`outcome`、`outcome_source: ground_truth`、`ground_truth_status: provided`、`adjudicated_outcome` 和 `### Ground Truth (yi*)`；不满足者已记录缺失并跳过。
- 已执行 ground truth/yi* gate；不满足 gate 的 rollout 已标记为 `invalid_rollout_schema` 并跳过，未产生 `delta K` 或 `delta e`。
- `trace_outcome` 与 `adjudicated_outcome` 冲突已写入治理摘要，低置信度或有明确失败证据的冲突未进入 `accepted`。
- 每个 `delta K` 和 `delta e` 都可追溯到具体 rollout。
- `delta K` 与 `delta e` 都先以 JSON 操作中间态表达，再转成 Markdown 落位。
- `partial` 与 `blocked` 已按降级规则处理。
- 经验符合长度限制、ID 规则和合并判据。
- 稳定规则与上下文经验没有混写。
- 若有 accepted `delta e`，已检查目标 `SKILL.md` 是否包含经验加载、阶段匹配、上下文改写和 rollout 记录规则。
- 输出了治理摘要。
