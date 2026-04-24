---
name: cangjie-harmonyos-doc-search
description: "鸿蒙仓颉应用开发本地检索技能，提供任务卡、API 卡、示例卡、文档卡四层结构化搜索，适用于 UI/API/框架机制/状态管理/构建报错日志知识检索，并保留旧版入口用于 AB 测试。"
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

默认入口仍然是本地结构化检索 `search_v3.py`。`search_v2.py` 仅作为兼容入口保留。旧版 `search.py` 保留用于 AB 测试或效果回归。

## AB 入口

V3 默认入口：

```bash
python .agents/skills/cangjie-harmonyos-doc-search/search_v3.py "我想写一个滑动列表"
python .agents/skills/cangjie-harmonyos-doc-search/search_v3.py "List" --mode api
python .agents/skills/cangjie-harmonyos-doc-search/search_v3.py "滚动事件示例" --mode example --json
```

V1 保留入口：

```bash
python .agents/skills/cangjie-harmonyos-doc-search/search.py "Stack组件用法"
```

旧版说明见 `SKILL.v1.md`。

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
python .agents/skills/cangjie-harmonyos-doc-search/build_index_v3.py --mode rule
```

如需更高质量的离线卡片补全，可使用：

```bash
python .agents/skills/cangjie-harmonyos-doc-search/build_index_v3.py --mode rule+llm
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
python .agents/skills/cangjie-harmonyos-doc-search-maintenance/scripts/run_maintenance.py \
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
- V1 与 V3 并行存在，做 AB 对比时请显式调用对应脚本
- 用户态在线查询优先复用当前 agent 的理解能力，然后再调用本地检索
- 若后续平台提供内部模型调用接口，再考虑把在线理解下沉为程序化能力；当前版本先按 skill 指令流执行
- 文档更新后如需按固定流程重建、评测、留档，请使用 `cangjie-harmonyos-doc-search-maintenance`
