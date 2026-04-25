---
name: harmonyos-app-agent-development
description: "当用户要求开发、迭代、修复或验证 HarmonyOS/仓颉 App 时，作为 App Agent 自主开发总控 Skill 使用。它编排需求分析、项目初始化、文档检索、编码实现、构建验证、运行诊断和经验沉淀，适用于从零创建 App、实现功能、修复编译/运行问题、继续完善已有应用等场景。"
---

# HarmonyOS App Agent 自主开发总控

## 定位

本 Skill 是开发闭环的总入口，只负责调度和决策，不复制其他 Skill 的细节。

目标是在用户提出 App 开发任务后，让 Agent 自主完成：

1. 判断项目状态和任务类型
2. 拆解需求与验收标准
3. 查询仓颉/HarmonyOS 文档
4. 实现最小可用改动
5. 构建并根据日志修复
6. 构建成功后做运行诊断
7. 沉淀已验证经验

## 触发场景

- 用户要求“开发一个 HarmonyOS/仓颉 App”
- 用户要求实现页面、组件、路由、网络、存储、权限、WebView、ArkTS 互操作等功能
- 用户要求修复仓颉鸿蒙项目的构建错误、运行错误、白屏、崩溃或交互问题
- 用户要求继续完善已有 HarmonyOS 应用

不适用：

- 只问单个 API 或文档概念：直接使用 `cangjie-harmonyos-doc-search`
- 只做项目初始化：直接使用 `harmonyos-project-init`
- 只做构建：直接使用 `harmonyos-build`
- 只做运行诊断：直接使用 `harmonyos-app-diagnose`

## 自主开发流程

### 1. 入口路由

先判断用户输入属于哪条路径，避免简单问题过度规划，也避免大目标被当成单条检索 query：

| 路由 | 触发条件 | 处理方式 |
| --- | --- | --- |
| `direct_doc_search` | 用户明确问某个组件/API/属性/报错“怎么用/怎么查/为什么错” | 直接调用 `cangjie-harmonyos-doc-search`，必要时补 `api/example/doc` 模式 |
| `app_goal_planning` | 用户要求开发 App、页面、功能或较大迭代，但没有给出完整技术拆解 | 先做需求拆解和查询计划，再分批检索 |
| `build_diagnosis` | 构建失败、编译错误、依赖/类型/符号问题 | 读取日志，查 `Evolution.md`，再按错误关键词检索 |
| `runtime_diagnosis` | 白屏、崩溃、交互异常、权限拒绝、运行日志异常 | 构建通过后调用运行诊断，并用日志/截图/控件树反推查询 |

### 2. 判断项目状态

先检查当前目录或用户指定目录是否是 HarmonyOS 项目：

- 存在 `AppScope/`、`entry/`、`oh-package.json5`、`build-profile.json5`：按已有项目处理
- 不存在项目结构，且用户目标是新建 App：调用 `harmonyos-project-init`
- 项目路径不明确且无法从上下文判断：先向用户确认目标目录

### 3. 需求、验收与查询计划

需求较复杂时先调用 `harmonyos-requirements`，输出功能点、页面/组件拆分、系统能力依赖、验收标准。

轻量改动可直接执行，但仍要明确：

- 要改哪个页面或模块
- 用户可观察到的结果
- 是否需要构建或设备验证

当路由是 `app_goal_planning` 时，编码前必须产出查询计划：

```text
目标：<用户要开发的 App/页面/功能>
页面/模块：<页面或模块列表>
能力拆解：<UI、状态、网络、存储、权限、路由、媒体、互操作等>
查询计划：
- query: <要传给 search_v3.py 的自然语言查询>
  mode: <auto|task|api|example|doc>
  purpose: <这次查询要确认什么>
  capability: <能力分类>
验收点：<可构建、可运行、可观察的结果>
```

查询计划必须满足：

- 每个不确定能力至少有 1 条查询。
- 写代码前至少有 1 条示例类查询，复杂页面需要 `task + api + example` 组合。
- 不把用户大目标原样作为唯一 query，例如“开发聊天 App”必须拆成消息列表、输入发送、滚动、网络、状态、存储等子查询。
- 详细规划规则与常见 App 模板见 `references/query-planning.md`。

### 4. 文档检索门禁

写仓颉/HarmonyOS 代码前，遇到以下情况必须先查文档：

- 不确定组件、属性、事件、装饰器、生命周期、权限或系统 API
- 需要示例代码
- 需要处理编译错误、运行时报错、类型不匹配、模块找不到
- 涉及 WebView、路由、网络、文件、数据库、加密、ArkTS 互操作、stdx

默认使用：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "<query>" --json --limit 5
```

若当前工作目录就是 `CangjieSkills` 仓库根目录，可使用相对路径 `.agents/skills/cangjie-harmonyos-doc-search/search_v3.py`。若当前工作目录是用户 App 工程，必须使用已安装 Skill 的实际绝对路径，避免相对路径失效。

查询策略：

- 功能实现：优先使用查询计划中的子查询；轻量功能可用原始需求查 `auto` 或 `task`
- API/组件：使用 `--mode api`
- 代码写法：补查 `--mode example`
- 构建/运行错误：保留错误关键词、API 名、模块名重查
- Top5 不相关时，换组件名、API 名、英文关键词或错误码再查

不得只凭模型记忆臆造 HarmonyOS/仓颉 API。

### 5. 专项 Skill 分流

- 新建项目：`harmonyos-project-init`
- 构建与构建失败：`harmonyos-build`
- UI/运行时诊断：`harmonyos-app-diagnose`
- 已验证经验沉淀：`harmonyos-evolution`
- 仓颉与 ArkTS 互操作：`cangjie-arkts-interop`
- 仓颉语言语法：`cangjie-lang-features`
- 标准库：`cangjie-std`
- 扩展库 API：`cangjie-stdx`
- 鸿蒙 stdx 依赖配置：`harmonyos-stdx`

## 构建与修复闭环

实现后调用 `harmonyos-build`。

构建失败时按顺序处理：

1. 读取项目 `Evolution.md`，匹配已有已验证经验
2. 阅读 `build.log`，提取关键错误
3. 用错误关键词和涉及 API 调用 `cangjie-harmonyos-doc-search`
4. 做最小修复并重建
5. 最多连续 3 轮，仍失败则停止并输出阻塞原因、已尝试方案和需要用户补充的信息

只有 `BUILD SUCCESSFUL` 后，才允许把本次修复写入 `harmonyos-evolution`。

## 运行诊断

构建成功后：

- 有可用设备或模拟器：调用 `harmonyos-app-diagnose` 采集截图、控件树和 hilog
- 无设备：明确标记“构建已验证，运行未验证”
- 如果诊断发现崩溃、白屏、断言失败或关键 UI 缺失，返回编码阶段修复并重新构建

## 输出要求

最终回复必须包含：

- 完成的功能或修复
- 关键文档依据或检索结论
- 构建结果
- 运行诊断结果；没有设备时说明未验证原因
- 未完成项或风险
- 如写入 `Evolution.md`，说明沉淀条目标题

禁止输出未经验证的成功结论。

## 规划用例健康检查

维护本 Skill 时，可校验目标规划用例结构：

```bash
python <CangjieSkills>/.agents/skills/harmonyos-app-agent-development/scripts/validate_goal_planning_cases.py \
  --output /tmp/harmonyos-app-agent-goal-planning-health.json
```

用例位于 `evals/goal_planning_cases.jsonl`，用于覆盖“双通道路由”和“用户目标到查询计划”的设计质量；它不调用外部 LLM，也不替代 `cangjie-harmonyos-doc-search` 的检索评测。
