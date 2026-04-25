---
name: cangjie-harmonyos-doc-search
description: "鸿蒙仓颉应用开发本地检索技能，提供任务卡、API 卡、示例卡、文档卡四层结构化搜索，适用于 UI/API/框架机制/状态管理/构建报错日志知识检索。"
tags: [workflow, platform]
---

# 仓颉鸿蒙文档检索 Skill（V3 默认）

## 定位

这个 Skill 负责把鸿蒙仓颉开发问题或构建报错日志线索收敛成四类检索对象：

- 任务卡：回答“我要实现什么功能”
- API 卡：回答“应该用哪个组件或接口”
- 示例卡：回答“代码怎么写”
- 文档卡：回答“原始文档、概览、排错信号和探索性线索在哪里”

用户态默认执行方式不是“直接硬搜”，而是：

1. 当前 agent 先理解用户问题属于功能/API/示例/排错哪一类
2. 再选择合适的本地检索模式调用 `search_v3.py`
3. 最后结合任务卡、API 卡、示例卡组织回答

默认入口是本地结构化检索 `search_v3.py`。历史 V1 入口已移除；如需与 OpenViking 做效果对比，使用 `scripts/ab_test_openviking_vs_v3.py`。

## 使用入口

默认查询：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "我想写一个滑动列表"
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "List" --mode api
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "滚动事件示例" --mode example --json
```

AB 对比和发布评估脚本位于 `scripts/`，评测集位于 `evals/`。
若当前工作目录就是 `CangjieSkills` 仓库根目录，可把 `<CangjieSkills>/` 替换为相对路径空前缀。

## 用户态在线使用规范

用户真正使用本 Skill 时，遵循下面这条固定流程：

1. 先由当前对话中的 agent 做语义理解，不要求用户提供任何 `url`、`key` 或模型配置
2. 若判断是功能诉求，优先调用 `search_v3.py --mode task` 或默认 `--mode auto`
3. 若判断是属性、事件、组件、装饰器、接口问题，优先调用 `search_v3.py --mode api`
4. 若用户明确要代码写法、demo、示例，补一次 `search_v3.py --mode example`
5. 若是排错问题，先看任务卡，再补相关 API 卡
6. 最终回答必须以本地索引命中的文档结果为依据，不直接凭模型记忆回答

这意味着：

- 用户态在线理解复用的是当前 agent 的理解能力
- 用户态查询不依赖单独配置 OpenAI 兼容 API
- `url/key` 只属于开发者维护索引时的离线能力，不属于最终用户使用门槛

## V3 使用规范

1. 用户是功能诉求时，优先 `--mode task`，或直接用默认 `--mode auto`
2. 用户明确问组件、属性、事件、装饰器时，优先 `--mode api`
3. 准备生成代码前，至少补一次 `--mode example`
4. 命中多个候选时，先读任务卡和示例卡，再下钻 API 明细

## 索引构建

首次使用 V3 前，需要先构建本地索引：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/build_index_v3.py --mode rule
```

如需更高质量的离线卡片补全，可使用：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/build_index_v3.py --mode rule+llm
```

`rule+llm` 仅在构建阶段调用 OpenAI 兼容 API，查询运行时不要求用户配置任何外部模型参数。

构建产物写入 `index/`：

- `manifest.json`
- `tasks.jsonl`
- `apis.jsonl`
- `examples.jsonl`
- `docs.jsonl`
- `aliases.json`
- `search.db`

当前索引覆盖来源包括 `harmonyos-6.1-8k`、`lang-features`、`std`、`stdx`、`tools`。

文档更新后的准确性优先复跑流程：

```bash
OPENAI_BASE_URL="https://api.modelarts-maas.com/openai/v1" \
OPENAI_API_KEY="your-key" \
OPENAI_MODEL="deepseek-v3.2" \
OPENAI_TEMPERATURE="0" \
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search-maintenance/scripts/run_maintenance.py \
  --llm-card-types task,api,example,doc \
  --llm-concurrency 24
```

该维护流程会先写入时间戳临时目录，完成全量增强、评测门禁和覆盖审计后才同步到默认 `index/`。用户态查询仍只使用本地索引，不调用外部 LLM。

## 检索模式

- `auto`：自动判定任务/API/示例
- `task`：优先返回任务卡，并补相关 API、示例
- `api`：优先返回 API 卡，并补相关任务、示例
- `example`：优先返回示例卡，并补相关 API、任务
- `doc`：优先返回文档卡，并补相关任务、API、示例

## 首批覆盖重点

V3 第一批重点覆盖高频 UI 场景：

- `List`
- `Scroll`
- `Refresh`
- `LazyForEach`
- `ListItem`
- `ListItemGroup`
- 基础滑动列表、分组列表、编辑列表、控制滚动位置、下拉刷新、嵌套滚动

## 注意事项

- V3 不依赖远端 OpenViking 服务
- `index/` 缺失时，直接提示执行 `build_index_v3.py`
- OpenViking 只作为 `scripts/ab_test_openviking_vs_v3.py` 中的对照组，不作为默认入口
- 用户态在线查询优先复用当前 agent 的理解能力，然后再调用本地检索
- 若后续平台提供内部模型调用接口，再考虑把在线理解下沉为程序化能力；当前版本先按 skill 指令流执行
- 文档更新后如需按固定流程重建、评测、留档，请使用 `cangjie-harmonyos-doc-search-maintenance`

## App Agent 自主开发调用协议

当 Agent 正在开发 HarmonyOS/仓颉 App 时，以下情况必须先调用本 Skill：

- 不确定组件、API、权限、生命周期、路由、WebView、网络、存储、文件、数据库、ArkTS 互操作或 stdx 的用法
- 需要示例代码、参数说明、返回值说明或 import/module 线索
- 遇到构建错误、运行时报错、API 找不到、类型不匹配、权限拒绝、白屏、崩溃等问题
- 用户提出 App 功能目标，但实现路径不确定

调用要求：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "<query>" --json --limit 5
```

- 功能实现类问题优先使用默认 `auto`，必要时补 `--mode task`
- API、组件、属性、事件、装饰器问题使用 `--mode api`
- 写代码前至少补一次 `--mode example`
- 排错问题保留错误关键词、API 名、组件名、模块名或错误码
- Top5 不相关时换 query 重查，不允许只凭模型记忆编造 API

App Agent 只依赖 `--json` 输出中的稳定字段：

- `query`：原始查询
- `mode`：检索模式
- `understanding`：意图、对象、标识符和后续模式建议
- `tasks`：功能实现线索
- `apis`：组件/API/接口线索
- `examples`：代码示例线索
- `docs`：原始文档和参考说明
- `paths`：可继续读取的文档路径

编码前必须基于命中的 `tasks/apis/examples/docs/paths` 确认 API 名、import、参数、返回值、权限配置和示例写法。
