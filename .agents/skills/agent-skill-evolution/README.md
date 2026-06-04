# Agent Skill Evolution 使用说明

`agent-skill-evolution` 用来把日常开发 Skill 时产生的失败记录、成功记录、rollout、工具调用、视觉观察、用户反馈和测试结果，转化为可执行、可验证的 Skill 改进。

它适合在一个 Skill 已经写完并经过测试后使用。你先把测试过程中的失败情形、成功情形和相关证据保存下来，再让 evolution 根据证据修复或扩展目标 Skill。

## 一句话流程

写 Skill -> 测试 Skill 行为 -> 记录失败和成功证据 -> 调用 evolution 分析证据 -> evolution 修改 Skill、references 或 evals -> 运行 lint 和 eval 验证。

## 什么时候使用

使用 evolution 的典型场景：

- 一个 Skill 写完后，测试中发现若干失败情形，例如 `missing-readback-validation`、`unsupported-tool-flag`。
- 一个 Skill 在某些任务中表现正确，例如 `schema-first-valid-report`、`help-guided-parameter-fix`，希望把成功经验沉淀为稳定流程。
- 同一个任务尝试了多条执行路径，需要比较不同 rollout 的差异。
- 工具调用参数、命令、schema 或失败模式需要写进 Skill。
- UI、网页、鸿蒙界面等任务中有截图、控件树、视觉状态或操作结果，需要区分稳定流程和上下文经验。
- 技能库中存在过宽 Skill、重复 Skill、依赖不清或能力缺口，需要拆分、合并或治理。

不适合使用 evolution 的场景：

- 只修复 `skill-lint` 报错或 warning。此时应使用 `skill-lint-fix`。
- 只是查询某个 API、修普通业务代码、排构建错误。此时应使用对应领域 Skill。
- 没有任何可复核证据。此时只能形成 `pending` 建议，不能直接写成最终规则。

## 推荐目录结构

建议把每次测试证据放在目标 Skill 目录下的 `evidence/evolution/` 中，按日期和任务命名。

示例：

```text
.agents/
  skills/
    my-skill/
      SKILL.md
      evals/
      references/
      evidence/
        evolution/
          2026-06-05-basic-behavior/
            case.md
            failures/
              missing-readback-validation.md
              unsupported-tool-flag.md
            successes/
              schema-first-valid-report.md
              help-guided-parameter-fix.md
            rollouts/
              direct-generation.md
              validation-first.md
            tools/
              command-log.md
              schema.md
            visual/
              screenshot-before.png
              screenshot-after.png
              control-tree.json
            feedback.md
            test-results.md
```

如果证据不属于某个单独 Skill，而是用于治理整个技能库，可以放在技能库根目录：

```text
.agents/
  skills/
    evidence/
      evolution/
        2026-06-05-library-governance/
          topology.md
          duplicate-skills.md
          missing-capabilities.md
          test-results.md
```

## 如何记录失败情形

每个失败情形建议单独写成一个文件，例如 `failures/missing-readback-validation.md`。

模板：

```markdown
# missing-readback-validation 失败情形

## 目标

这次测试希望 Skill 完成什么任务。

## 输入

用户请求、文件、命令、页面状态或其他初始条件。

## 实际行为

Agent 做了什么，调用了哪些工具，输出了什么。

## 失败结果

哪里失败了，例如遗漏步骤、调用错工具、参数错误、没有验证、误判界面状态。

## 证据

日志、命令输出、截图、控件树、测试结果或人工复核结论。

## 期望行为

下次遇到类似场景时，Skill 应该如何处理。
```

失败情形最有价值的部分是“为什么失败”和“下次应该增加什么防错动作”。evolution 会优先从失败记录中提取防错规则。

## 如何记录成功情形

每个成功情形也建议单独写成一个文件，例如 `successes/schema-first-valid-report.md`。

模板：

```markdown
# schema-first-valid-report 成功情形

## 目标

这次测试希望 Skill 完成什么任务。

## 输入

用户请求、文件、命令、页面状态或其他初始条件。

## 成功路径

Agent 按什么顺序完成任务，使用了哪些工具，关键判断是什么。

## 成功结果

最终产物、测试通过结果、用户确认或人工复核结论。

## 可迁移经验

哪些步骤可以沉淀为稳定流程，哪些只适合当前场景。

## 证据

日志、命令输出、截图、控件树、测试结果或人工复核结论。
```

成功情形最有价值的部分是“可迁移流程”。evolution 会从成功记录中提炼稳定做法。

## 如何记录 rollout

`rollout` 是同一个任务的一次完整尝试路径。多个 rollout 可以帮助 evolution 比较不同路径，区分稳定流程和上下文经验。

示例：

```text
rollouts/
  r1-direct-click.md
  r2-check-control-tree-first.md
  r3-read-log-first.md
```

每个 rollout 建议记录：

- 初始状态。
- 执行动作顺序。
- 工具调用和关键参数。
- 观察到的页面、文件、日志或视觉状态。
- 最终结果。
- 这条路径成功或失败的原因。

如果是 UI 或多模态任务，建议同时保存截图、控件树和操作结果。

## 调用 evolution 的方式

### 只分析，不修改文件

当你还不确定应该如何改 Skill 时，先使用分析评审模式。

示例请求：

```text
请使用 agent-skill-evolution 分析 .agents/skills/my-skill。
执行分析评审模式，不修改文件。
证据目录是 .agents/skills/my-skill/evidence/evolution/2026-06-05-basic-behavior。
其中 failures/missing-readback-validation.md、failures/unsupported-tool-flag.md 是失败情形，successes/schema-first-valid-report.md、successes/help-guided-parameter-fix.md 是成功情形。
请输出路线决策、候选知识单元、accepted/pending/rejected 决策和具体修改建议。
```

### 实际修复目标 Skill

当证据已经清楚，并且希望直接改进 Skill 时，使用实际修改模式。

示例请求：

```text
请使用 agent-skill-evolution 实际改进 .agents/skills/my-skill。
证据目录是 .agents/skills/my-skill/evidence/evolution/2026-06-05-basic-behavior。
失败情形包括 missing-readback-validation、unsupported-tool-flag，成功情形包括 schema-first-valid-report、help-guided-parameter-fix。
请先选择主路线和增强模块，再把 accepted 知识写入合适位置。
修改后运行 skill-lint 和必要 eval，并报告验证结果。
```

### 治理整个技能库

当目标不是单个 Skill，而是多个 Skill 的拆分、合并或依赖治理时：

```text
请使用 agent-skill-evolution 治理 .agents/skills 技能库。
证据目录是 .agents/skills/evidence/evolution/2026-06-05-library-governance。
目标是识别过宽 Skill、重复 Skill 和能力缺口。
请使用 SkillX 作为主路线，必要时叠加 Trace2Skill 或 XSkill。
请给出并实施拓扑变更、跨 Skill 依赖和独立 eval。
```

## evolution 会如何选择路线

evolution 每次只选择一个主路线，其余路线只能作为增强模块。

### Trace2Skill

当核心证据是成功轨迹和失败轨迹时使用。

适合：

- 从 `schema-first-valid-report`、`help-guided-parameter-fix` 这类成功情形提炼稳定流程。
- 从 `missing-readback-validation`、`unsupported-tool-flag` 这类失败情形提炼防错规则。
- 修复单个 Skill 的行为缺陷。

产物通常是：

- 逐轨迹知识单元。
- 冲突裁决。
- 合并后的稳定规则。
- 更新后的 `SKILL.md` 或 `references/`。

### SkillX

当核心问题是技能结构、工具编排或技能库治理时使用。

适合：

- 一个 Skill 太宽，需要拆成多个 Skill。
- 多个 Skill 语义重复，需要合并。
- 工具参数、命令、schema 和失败模式需要系统整理。
- 技能库存在能力缺口。

产物通常是：

- 规划层、功能层、原子层结构。
- 拆分或合并决策。
- 跨 Skill 输入、输出和依赖。
- 独立 discovery eval 和 behavior eval。

### XSkill

当核心证据是多个 rollout、视觉观察或上下文敏感动作时使用。

适合：

- 多个 UI rollout 得到不同结果。
- 截图、控件树、视觉状态影响下一步动作。
- 某个经验只在特定页面状态下有效。

产物通常是：

- 稳定技能流，写入 `SKILL.md`。
- 上下文经验流，写入 `references/experiences.md`。
- 经验加载和适配规则。

## 知识应该放在哪里

evolution 会根据知识稳定性和用途决定放置位置。

```text
SKILL.md
  高频、稳定、已验证的规则和主流程。

references/
  较长案例、工具矩阵、依赖说明、背景知识。

references/experiences.md
  已验证但依赖上下文的经验，例如某种 UI 遮罩状态下的动作建议。

evals/
  只放验证用例，不放规则正文，也不放经验正文。

待验证清单
  证据不足、冲突未裁决或还没有验证方法的 pending 知识。
```

只有 `accepted` 知识可以写入最终产物。`pending` 和 `rejected` 只能出现在决策摘要或待验证清单中，不能被写成硬性规则。

## 修改后的验证

实际修改模式下，evolution 应对所有受影响 Skill 运行验证。

常用命令：

```powershell
$target = ".agents\skills\<skill-name>"
$skillName = Split-Path -Leaf (Resolve-Path -LiteralPath $target)
New-Item -ItemType Directory -Force -Path "reports\lint","reports\eval" | Out-Null

skill-lint --path $target --format json --out "reports\lint\$skillName.json"
skill-eval --path $target --mode all --runner agent-command --agent-command "python -m skill_cli.eval_tools.codex_exec_agent_adapter" --emit-trace --timeout 600 --progress --out "reports\eval\$skillName.json"
```

如果新增或修改了 `evals/`，真实 agent eval 是最终验收要求。真实 agent eval 不可用时，必须明确说明阻塞，不能只用非真实 agent 验证代替。

## 日常使用建议

1. 每次测试 Skill 时，至少记录一个失败情形或一个成功情形。
2. 失败记录要写清楚实际行为、失败结果和期望行为。
3. 成功记录要写清楚成功路径和可迁移经验。
4. 涉及工具时，保存命令、参数、schema、`--help` 输出或实际调用结果。
5. 涉及 UI 或视觉状态时，保存截图、控件树和操作前后状态。
6. 每次调用 evolution 前，明确是分析评审模式还是实际修改模式。
7. 不要把未经验证的想法直接写进 `SKILL.md`，先标为 `pending`。
8. 修改后必须保存验证报告，方便下次继续 evolution。

## 一次完整示例

假设你开发了 `.agents/skills/json-report`，测试后发现：

- `missing-readback-validation`：生成 JSON 后没有读回校验，导致空字段没有被发现。
- `unsupported-tool-flag`：工具参数写错，误用了不存在的 `--target`。
- `schema-first-valid-report`：先读取 schema，再生成报告，再校验必需字段，可以稳定成功。
- `help-guided-parameter-fix`：失败后读取命令 `--help`，能正确修正参数。

先保存证据：

```text
.agents/skills/json-report/evidence/evolution/2026-06-05-json-report/
  failures/missing-readback-validation.md
  failures/unsupported-tool-flag.md
  successes/schema-first-valid-report.md
  successes/help-guided-parameter-fix.md
  tools/report-tool-help.md
  test-results.md
```

然后请求：

```text
请使用 agent-skill-evolution 实际改进 .agents/skills/json-report。
证据目录是 .agents/skills/json-report/evidence/evolution/2026-06-05-json-report。
失败情形包括 missing-readback-validation、unsupported-tool-flag，成功情形包括 schema-first-valid-report、help-guided-parameter-fix。
请选择主路线，生成知识单元，只把 accepted 知识写入目标产物，并运行验证。
```

预期 evolution 会做的事情：

1. 选择 `Trace2Skill` 作为主路线，因为核心证据是成功和失败轨迹。
2. 如果工具参数问题较重，叠加 `SkillX` 作为增强模块。
3. 从 `missing-readback-validation` 提炼“写入结构化文件后必须读回校验”的防错规则。
4. 从 `unsupported-tool-flag` 提炼“工具参数必须通过 schema、`--help` 或实际命令验证”的工具规则。
5. 从 `schema-first-valid-report`、`help-guided-parameter-fix` 提炼稳定流程。
6. 将稳定规则写入 `SKILL.md` 或 `references/`。
7. 保留证据文件不变。
8. 运行 lint 和 eval，输出报告路径。

## 最终交付应包含什么

一次 evolution 完成后，最终摘要应说明：

- 使用的主路线和增强模块。
- 目标形态是单 Skill 还是技能库。
- accepted、pending、rejected 知识决策。
- 修改了哪些文件。
- 是否产生技能拆分、合并或跨 Skill 依赖。
- 是否产生 `references/experiences.md` 经验流。
- 运行了哪些验证。
- 报告保存在哪里。
- 是否存在阻塞。
