---
name: cangjie-skillx-layered-refinement
description: "当需要从 Rollout Record 对已有 Agent Skill 做 SkillX 分层抽取与精炼时使用此 Skill：读取 cangjie-rollout-collector 生成的记录，执行 planning / functional / atomic 三层技能抽取，并按 merge/decompose、general filter、tool schema filter 与 add/modify/keep 治理目标 Skill。"
---

# 仓颉 SkillX 分层抽取与精炼

本 Skill 负责 SkillX 的三层抽取与迭代精炼；`cangjie-xskill-evolution` 负责 XSkill 技能流/经验流治理。不要混用二者：需要 planning / functional / atomic 分层、技能合并过滤和 add/modify/keep 更新时使用本 Skill；需要把稳定技能流与上下文敏感经验流分离时使用 `cangjie-xskill-evolution`。


## 职责边界

- 采集 rollout 使用 `cangjie-rollout-collector` 生成并集中保存 `Rollout Record`；本 Skill 不执行采集或持久化。
- 本 Skill 负责分层抽取与精炼：读取一个或多个 `Rollout Record`（默认从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 查找），按 Tool Summary -> Plan Extract -> Functional/Atomic Extract -> Merge/Decompose -> General Filter -> Tool Schema Filter -> Update 执行治理；只有用户明确要求写入时才修改目标 Skill。

## 输入与分组

输入可以是粘贴的 `Rollout Record` Markdown，也可以是用户指定的 rollout 文件。未指定输入时，优先读取 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 下与用户指定 `target_skill` / `task_id` 匹配的 Markdown。先按 `target_skill` 分组，再按 `task_id` 分组；禁止把不同目标 Skill 的候选技能混合精炼。

读取 `Rollout Record` 时必须先执行 ground truth/yi* gate：

- 若存在 `ground_truth_status: provided`、`outcome_source: ground_truth`、`adjudicated_outcome` 与 `### Ground Truth (yi*)`，治理使用 `adjudicated_outcome` 作为有效 outcome；`trace_outcome` 只作为审计参考。
- 若缺少 `ground_truth_status: provided`、缺少 `outcome_source: ground_truth`、缺少 `adjudicated_outcome` 或没有 `### Ground Truth (yi*)`，标记为 `invalid_rollout_schema`；该 rollout 必须跳过并写入摘要，不得产生候选、不得进入治理或写入目标 Skill。
- 若 `trace_outcome` 与 `adjudicated_outcome` 冲突，治理摘要必须列出冲突；当 ground truth `confidence: low` 或 trace 中有明确失败证据时，相关候选保持 `pending`。

读取 rollout 时执行容错：

- 缺少必含字段时，不从上下文补全；标记为 `invalid_rollout_schema` 并跳过。
- 缺少 `task_id`、`rollout_id`、`target_skill` 或 `outcome` 时，跳过该条并在摘要中说明。
- 单条 rollout 格式错误不得中断其他 rollout。

按有效 outcome（优先 `adjudicated_outcome`）使用证据：

- `success`：作为 planning / functional / atomic 抽取的主要来源。
- `partial`：只抽取已验证有效片段，默认标为 `pending`。
- `failure`：只用于失败模式、过滤、防错或 rejected/pending 判断，不进入稳定主流程。
- `blocked`：作为 failure 子类处理，只记录阻塞条件和规避提示。
- `not_verified`：只产生 `pending` 候选，不得直接进入稳定主流程。

## 候选 JSON 契约

每个候选技能必须先以 JSON 中间态表达，再转为 Markdown 建议或写入内容。

```json
{
  "level": "planning | functional | atomic",
  "name": "候选技能名称",
  "document": "输入、输出、使用说明、约束和注意事项",
  "content": "可复用步骤、工具调用模式或工具使用示例",
  "tools": ["涉及的工具名或命令"],
  "source_rollouts": ["task_id/rollout_id#S1-S3"],
  "operation": "add | modify | keep",
  "status": "accepted | pending | rejected",
  "target_placement": "目标 SKILL.md 章节或 new",
  "reason": "证据、过滤和更新理由",
  "metadata": {
    "cluster_id": "C001 或 unclustered",
    "extraction_epoch": "E1 或迭代轮次",
    "similarity_basis": "embedding | llm | manual",
    "source_steps": ["S1", "S2"]
  }
}
```

只允许 `accepted` 候选进入目标 Skill。`pending` 和 `rejected` 只能保留在治理摘要中。

## 阶段 1：Tool Summary

对每个步骤的环境反馈做事实压缩，尤其当反馈冗长、重复或超过约 1500 tokens 时。

- 只总结环境反馈相对于动作意图传达了什么。
- 保留与动作目标紧密相关的关键值、状态、错误码、路径、工具名和参数。
- 删除无关日志、重复输出和噪声。
- 不引入推测；无法确认时写“未观察到”。
- 输出用于后续抽取的紧凑步骤事实，而不是最终 Skill 内容。

## 阶段 2：Plan Extract

从成功 rollout 的关键路径中抽取 planning skills。planning skill 描述任务拆解、步骤顺序、依赖、分支和停止条件。

执行规则：

- 将 rollout 压缩为高层步骤，而不是逐个复述工具调用。
- 合并同一目标下的连续动作。
- 排除能力探索、调试、失败调用、回退和试错步骤。
- 保留关键 API、工具或命令名称，确保其他 agent 能复用。
- 若多个成功 rollout 展示同一任务结构，合并为更通用的 planning skill。

planning 候选的 `content` 使用有序步骤；每步写自然语言子目标和关键工具。

## 阶段 3：Functional Extract

按每个 planning step 抽取 functional skills。functional skill 是完成一个子任务的可复用宏操作，必须包含多步处理或有意义的工具组合。

执行规则：

- 每次只围绕一个具体 planning step 抽取。
- 产出 `name`、`document`、`content`、`tools`。
- `name` 使用通用名称，不绑定一次性任务、用户、路径或样例数据。
- `document` 明确 Parameters、Outputs、Notes。
- `content` 写可复用的工具调用模式和步骤，不写函数式 `return` 风格，不导入额外 Python 包。
- 如果已有 Skill 能覆盖该子任务，使用 `modify` 或 `keep`，不要重复 `add`。
- 如果候选只是单个 API 的薄封装，标为 `rejected` 或降级为 atomic 候选。

## 阶段 4：Atomic Extract

按单个工具抽取 atomic skills。atomic skill 是工具 schema 的执行型补充，用于记录单工具的参数模式、约束、组合示例和失败模式。

执行规则：

- 每次只围绕一个具体工具抽取。
- `name` 默认使用工具名或工具能力名。
- `document` 描述工具功能、关键参数、输出类型、约束和注意事项。
- `content` 给出可复用使用示例，可包含与其他工具的组合，但中心必须仍是该工具。
- 从真实调用中提炼常见参数配置、前置条件、后置验证和失败模式。
- 若目标 Skill 已充分说明该工具，使用 `keep`；只有缺少关键约束或失败模式时使用 `modify`。

## 阶段 5：Merge/Decompose

先聚类相似候选，再合并重复能力或拆分过宽候选。

聚类规则：

- 首选语义嵌入聚类；使用 DBSCAN 与 cosine similarity >= 0.90，等价 cosine distance `eps=0.10`。
- 无嵌入模型时，退化为 LLM 判断候选是否同名、同目标、同工具集合、同输入输出和同失败边界；将 `metadata.similarity_basis` 标为 `llm`。
- 每个候选必须写入 `metadata.cluster_id`；无法聚类时使用 `unclustered`。
- 每个迭代轮次写入 `metadata.extraction_epoch`。

合并规则：

- 名称不同但功能、输入输出和工具模式相同的候选合并。
- 新内容更准确时改写旧内容；互补内容合成更通用的 Notes 或步骤。
- 删除硬编码路径、账号、样例数据、一次性任务描述。
- 对包含多个独立触发条件或多个维护边界的候选执行拆分。
- 拆分出新 Skill 只有在用户明确要求创建时才写入；否则在摘要中提出建议。

## 阶段 6：General Filter

对 merge/decompose 后的候选做通用质量过滤。

过滤为 `rejected` 的情形：

- 绑定具体路径、账号、样例 ID、一次性任务或临时文件。
- 只是调用一个已有 Skill 或单个底层工具，没有额外逻辑。
- 引入额外 Python 包、安装步骤或目标 Skill 不需要的运行依赖。
- 使用函数式实现风格，像代码库函数而不是 agent 可执行技能说明。
- 缺少明确输入、输出、约束或使用说明。
- 与已有 Skill 高度重复但没有改进点。

可保留为 `pending` 的情形：

- 只有单条成功 rollout 支持，缺少跨 rollout 或独立验证。
- 证据来自 partial/failure，但有潜在防错价值。
- 工具 schema 暂不可验证。

## 阶段 7：Tool Schema Filter

对涉及工具调用的 functional 和 atomic 候选执行 schema 校验。

检查项：

- 工具名真实存在，未发明 API、命令或参数。
- 必需参数完整，类型、格式、枚举和取值范围符合 schema。
- 不包含 schema 不支持的参数。
- 多个工具调用的顺序不违反依赖关系。
- 注释或步骤说明与工具实际能力一致。
- 若 schema 不可获得，标为 `pending`，并写明所需验证来源。

只有 schema 校验通过或有等价可执行验证的候选才能标为 `accepted`。

## 阶段 8：Update

对目标 Skill 执行 `add | modify | keep` 决策。

- `add`：目标 Skill 缺少该稳定能力，且候选已通过 merge/filter/schema 验证。
- `modify`：目标 Skill 已有相关内容，但缺少关键输入输出、工具约束、失败模式或步骤顺序。
- `keep`：目标 Skill 已覆盖该能力，或候选没有带来可观察行为改进。

写入规则：

- 用户只要求评估、建议或方案时，只输出治理建议，不改文件。
- 用户明确要求更新、改进或治理目标 Skill，且当前会话允许写入时，才修改目标 Skill。
- 不改写原始 rollout、证据文件或未授权 Skill。
- 没有通过 ground truth/yi* gate 的 rollout 不得支撑候选生成或写入。
- 只写入 `accepted` 内容；`pending` 和 `rejected` 放入摘要。
- 目标 `SKILL.md` 只保留高频、稳定、可执行、可验证的流程和规则。

## 治理摘要

每次治理结束都输出：

```markdown
## SkillX 治理摘要

- target_skill: <名称>
- 使用 rollout: <数量与 ID>
- 跳过 rollout: <缺字段或无法解析的 ID 与原因>
- extraction_epoch: <本轮迭代 ID>
- ground truth: provided <n>, invalid_rollout_schema <n>, conflict <n>
- planning candidates: accepted <n>, pending <n>, rejected <n>
- functional candidates: accepted <n>, pending <n>, rejected <n>
- atomic candidates: accepted <n>, pending <n>, rejected <n>
- clusters: <cluster_id 列表与合并/拆分结果>
- update decisions: add <n>, modify <n>, keep <n>
- 建议写入位置: <SKILL.md 章节或无>
- 建议新建 Skill: <名称与理由；无则写无>
- 未采纳原因: <pending/rejected 的主要原因>
- 验证建议: <schema、lint、eval、人工复核或最小复现>
```

## 最小检查清单

- 采集 rollout 已交给 `cangjie-rollout-collector`；本 Skill 只处理已有 `Rollout Record`。
- 未指定输入时，只从 `.agents/skills/cangjie-rollout-collector/records/rollouts/` 自动查找 rollout。
- 治理阶段顺序是 summary -> plan -> functional/atomic -> merge/decompose -> general filter -> tool schema filter -> update。
- 每条有效 rollout 都有 `task_id`、`rollout_id`、`target_skill`、`outcome`、`outcome_source: ground_truth`、`ground_truth_status: provided`、`adjudicated_outcome` 和 `### Ground Truth (yi*)`。
- 已执行 ground truth/yi* gate；不满足 gate 的 rollout 已标记为 `invalid_rollout_schema` 并跳过，未产生候选。
- `trace_outcome` 与 `adjudicated_outcome` 冲突已写入治理摘要，低置信度或有明确失败证据的冲突候选未标为 `accepted`。
- 每个候选 JSON 都包含 `metadata.cluster_id` 和 `metadata.extraction_epoch`。
- 成功 rollout 才能支撑稳定主流程；失败、blocked、partial 只参与防错、过滤或 pending/rejected 判断。
- 每个候选都可追溯到具体 rollout 与步骤。
- `accepted` 候选已经通过通用质量过滤和工具 schema 校验，或写明等价验证。
