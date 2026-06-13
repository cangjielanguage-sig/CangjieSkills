# XSkill Governance: cangjie-testcase-xmind Single-Parameter Coverage

- target_skill: `cangjie-testcase-xmind`
- governance_skill: `cangjie-xskill-evolution`
- generated_at: `2026-06-13`
- rollout_root: `.agents/skills/cangjie-rollout-collector/records/rollouts/cangjie-testcase-xmind`
- write_scope: target skill files only; rollout records were not modified

## 1. 输入与 Gate

读取 3 条 rollout，并按 `target_skill=cangjie-testcase-xmind` 分组。全部通过 ground truth/yi* gate。

| task_id | rollout_id | trace_outcome | adjudicated_outcome | gate | conflict | ground truth gap |
| --- | --- | --- | --- | --- | --- | --- |
| `ability_access_ctrl_testcase_xmind` | `cangjie-testcase-xmind-20260613-100839-001` | `partial` | `partial` | passed | no | `单参数测试` 未按每个参数建立参数节点，并展开有效等价类、无效等价类、边界值、特殊值 |
| `abilitykit-error-observer-xmind` | `cangjie-testcase-xmind-20260613-105118-001` | `not_verified` | `partial` | passed | yes | `ErrorObserver.init` 等接口下缺少 `onUnhandledException`、`onException` 参数节点与等价类讨论 |
| `error_manager_testcase_xmind` | `cangjie-testcase-xmind-20260613-111744-001` | `not_verified` | `partial` | passed | yes | `测试覆盖` 节点中的单参数测试缺失具体参数节点，以及有效等价类、无效等价类等讨论 |

Gate 统计：

- ground_truth provided: 3
- invalid_rollout_schema: 0
- trace/adjudicated conflict: 2

## 2. Cross-Rollout Critique

三条 rollout 都完成了 JSON 生成、校验、XMind 转换和 `content.xml` 抽检，但用户验收均裁定为 `partial`。共同问题不是固定 schema 或 Pair-wise，而是 `测试覆盖 -> {接口名} -> 单参数测试` 被写得过平，缺少 `参数名 -> 有效等价类 / 无效等价类 / 边界值 / 特殊值` 的层级。

现状检查：

- `SKILL.md` 只要求读取固定 schema、生成 Pair-wise、验证和转换，没有把单参数覆盖树作为 Pair-wise 之前的步骤。
- `references/xmind-format.md` 只在 `接口列表 -> 参数 -> 取值范围` 中要求四类取值节点，没有明确 `测试覆盖 -> 单参数测试` 的参数层级。
- `scripts/validate_testcase_xmind_json.py` 会检查固定节点、testcase shape 和 Pair-wise，不能发现单参数层级缺失。
- `references/experiences.md` 不存在；因此目标 Skill 也缺少经验消费入口。

## 3. Delta K

```json
[
  {
    "operation": "modify",
    "target_section": "SKILL.md / Workflow",
    "content": "在 Pair-wise 之前增加单参数覆盖树生成步骤。",
    "evidence": [
      "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#Ground Truth",
      "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#Ground Truth",
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260613-111744-001#Ground Truth"
    ],
    "status": "accepted",
    "reason": "三条 high-confidence partial 指向同一稳定缺口。"
  },
  {
    "operation": "modify",
    "target_section": "SKILL.md / JSON Design Rules",
    "content": "要求参数化 API 的 单参数测试 使用 参数名 -> 四类分类节点，禁止直接平铺 testcase。",
    "evidence": ["same as above"],
    "status": "accepted",
    "reason": "防止生成阶段再次漏掉用户裁定的核心层级。"
  },
  {
    "operation": "modify",
    "target_section": "references/xmind-format.md",
    "content": "展开 Required Tree 并新增 Single-Parameter Coverage 说明。",
    "evidence": ["same as above"],
    "status": "accepted",
    "reason": "将固定中文节点名和结构要求沉淀到格式参考。"
  },
  {
    "operation": "modify",
    "target_section": "scripts/validate_testcase_xmind_json.py",
    "content": "新增 validate_single_parameter，校验参数节点、四类分类节点和分类下 testcase/不涉及 叶子。",
    "evidence": ["same as above"],
    "status": "accepted",
    "reason": "把高频验收缺口转成可执行 gate。"
  },
  {
    "operation": "add",
    "target_section": "SKILL.md / Experience Use",
    "content": "新增经验消费入口，要求读取 accepted 经验、按上下文筛选、改写为任务动作提醒并记录 used_experience。",
    "evidence": ["cangjie-xskill-evolution rule"],
    "status": "accepted",
    "reason": "新增 accepted delta e 时必须配套经验使用入口。"
  }
]
```

## 4. Delta e

```json
[
  {
    "operation": "add",
    "id": "E-TESTCASE-XMIND-001",
    "experience": "转 XMind 前先抽检单参数测试是否按参数名展开四类分类节点。",
    "boundary": "适用于有参数 API；无参数或无具体取值时使用 不涉及 叶子。",
    "source": [
      "ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#Ground Truth",
      "abilitykit-error-observer-xmind/cangjie-testcase-xmind-20260613-105118-001#Ground Truth",
      "error_manager_testcase_xmind/cangjie-testcase-xmind-20260613-111744-001#Ground Truth"
    ],
    "status": "accepted",
    "reason": "跨 rollout 重复出现，且用户验收置信度高。"
  },
  {
    "operation": "add",
    "id": "E-TESTCASE-XMIND-002",
    "experience": "设置 PowerShell 和 Python 为 UTF-8，避免中文固定节点被写坏。",
    "boundary": "仅适用于 Windows PowerShell 管道；普通文件读取不需要。",
    "source": ["ability_access_ctrl_testcase_xmind/cangjie-testcase-xmind-20260613-100839-001#T029-T042"],
    "status": "pending",
    "reason": "只有单条 rollout 的环境绕路证据。"
  }
]
```

## 5. 写入步骤

1. 修改 `SKILL.md`：
   - 新增 `Experience Use` 入口。
   - 在 Workflow 中将单参数覆盖树放到 Pair-wise 前。
   - 在 JSON Design Rules 中要求参数层和四类分类节点。
   - 更新 validator 工具描述和 Practical Defaults。
2. 修改 `references/xmind-format.md`：
   - 在 Required Tree 展开 `单参数测试` 层级。
   - 新增 `Single-Parameter Coverage` 章节。
3. 修改 `scripts/validate_testcase_xmind_json.py`：
   - 新增 `SINGLE_PARAMETER_CATEGORIES`。
   - 新增 `extract_parameter_names`、`contains_testcase_object`、`validate_single_parameter`。
   - 在主 `validate()` 流程中调用单参数校验。
4. 新建 `references/experiences.md`：
   - 写入 accepted 的 `E-TESTCASE-XMIND-001`。
   - 保留 pending 的 Windows UTF-8 管道经验，避免提升为主流程。
5. 新建本报告，文件名前缀为 `xskill-`。

## 6. 治理摘要

- target_skill: `cangjie-testcase-xmind`
- 使用 rollout: 3
- 跳过 rollout: 0
- delta K: added 1, modified 4, merged 0, deleted 0, pending 0, rejected 0
- delta e: added 2, modified 0, merged 0, deleted 0, pending 1, rejected 0
- ground truth: provided 3, invalid_rollout_schema 0, conflict 2
- 写入位置: `SKILL.md`, `references/xmind-format.md`, `scripts/validate_testcase_xmind_json.py`, `references/experiences.md`
- 需新建文件: `references/experiences.md`, `reports/xskill-20260613-single-parameter-coverage.md`
- 经验入口: 已写入
- 未采纳原因: Windows UTF-8 管道经验仅作为 pending，不进入主流程
- 验证建议: `python -m py_compile`；用正例和反例 JSON 调用 `validate()`；必要时再跑真实历史产物回归

## 7. Verification Results

已执行的最小验证：

```text
python -m py_compile .agents\skills\cangjie-testcase-xmind\scripts\validate_testcase_xmind_json.py .agents\skills\cangjie-testcase-xmind\scripts\common.py
=> exit 0
```

```text
direct validate() positive case:
- parameterized API with 单参数测试 -> p -> 有效等价类/无效等价类/边界值/特殊值
=> positive_errors []
```

```text
direct validate() negative case:
- parameterized API with testcase object directly under 单参数测试
=> errors include "测试覆盖.foo.单参数测试: missing parameter node p"
```

```text
direct validate() no-parameter case:
- noParamApi with 单参数测试: { "不涉及": "" }
=> no_param_errors []
```

剩余风险：

- 尚未用历史真实 JSON 产物做全量回归；历史 partial 产物预期会被新单参数 gate 拦下。
- `E-TESTCASE-XMIND-002` 仍为 pending，不参与执行前经验筛选。
