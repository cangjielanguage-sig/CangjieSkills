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

默认入口是本地结构化检索 `search_v3.py`。历史 V1 与 AB/评测/构建辅助脚本均已迁至 `../cangjie-harmonyos-doc-search-maintenance/scripts/`，用户态不调用这些维护脚本。

## 使用入口

默认查询：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "我想写一个滑动列表"
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "List" --mode api
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "滚动事件示例" --mode example --json
```

AB 对比和发布评估脚本位于 `../cangjie-harmonyos-doc-search-maintenance/scripts/`，评测集位于本 skill 的 `evals/`。
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

当前索引覆盖来源包括 `harmonyos-6.0.2-15k`、`lang-features`、`std`、`stdx`、`tools`。

文档更新后的准确性优先复跑流程（推荐用密钥文件，避免 shell 里残留 `OPENAI_API_KEY=占位符` 导致 401）：

```bash
export CANGJIE_LLM_API_FILE="/path/to/LLM_API信息.txt"   # 见 maintenance/scripts/load_env.sh 支持的格式
unset OPENAI_API_KEY
source <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search-maintenance/scripts/load_env.sh

OPENAI_BASE_URL="https://api.modelarts-maas.com/openai/v1" \
OPENAI_MODEL="deepseek-v3.2" \
OPENAI_TEMPERATURE="0" \
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search-maintenance/scripts/run_maintenance.py \
  --llm-card-types task,api,example,doc \
  --llm-concurrency 24 \
  --fusion-ab-gate
```

- `--fusion-ab-gate`：发布前对候选索引跑 `run_ab_eval`（V3 / graphify / fusion），要求 fusion 召回不低于单引擎；并导出 `v3_seeds.json` 供图谱对齐。
- OpenViking 远端对照默认关闭；需要时显式传 `--openviking`。
- 独立评测集重建：`../cangjie-harmonyos-doc-search-maintenance/scripts/regenerate_15k_independent_evals.py`；校验：`../cangjie-harmonyos-doc-search-maintenance/scripts/validate_eval_set.py`。
- 拆分门禁：`../cangjie-harmonyos-doc-search-maintenance/scripts/run_v3_regression_gate.py`（`eval_queries_full` 自举）、`../cangjie-harmonyos-doc-search-maintenance/scripts/run_semantic_capability_gate.py`（fusion 三套独立集）。

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
- OpenViking 只作为 `../cangjie-harmonyos-doc-search-maintenance/scripts/ab_test_openviking_vs_v3.py` 中的对照组，不作为默认入口
- 用户态在线查询优先复用当前 agent 的理解能力，然后再调用本地检索
- 若后续平台提供内部模型调用接口，再考虑把在线理解下沉为程序化能力；当前版本先按 skill 指令流执行
- 文档更新后如需按固定流程重建、评测、留档，请使用 `cangjie-harmonyos-doc-search-maintenance`

## App Agent 自主开发调用协议

当 Agent 正在开发 HarmonyOS/仓颉 App 时，以下情况必须先调用本 Skill 或搭档的 `knowledge-graph-template`：

- 不确定组件、API、权限、生命周期、路由、WebView、网络、存储、文件、数据库、ArkTS 互操作或 stdx 的用法
- 需要示例代码、参数说明、返回值说明或 import/module 线索
- 遇到构建错误、运行时报错、API 找不到、类型不匹配、权限拒绝、白屏、崩溃等问题
- 用户提出 App 功能目标，但实现路径不确定

本 Skill 与 `knowledge-graph-template`（下称 graphify KG）**平权并存**，按 query 类型分发。两条引擎共享同一套文档源（harmonyos-6.0.2-15k / lang-features / std / stdx / tools），agent 侧融合结果即可。

### 能力对齐分发表

| Query 特征 | 首选引擎 | 具体调用 |
|---|---|---|
| 明确 API / 组件 / 装饰器名 | V3 | `search_v3.py "<q>" --mode api --json --limit 5` |
| 属性 / 事件 / 枚举值穷举 | V3 | `search_v3.py "<q>" --mode api` |
| 错误码 / 错误信息 / 构建日志关键字 | V3 | `search_v3.py "<q>" --mode auto` |
| 写代码前找示例 | V3 | `search_v3.py "<q>" --mode example` |
| 功能实现类（"做一个 X"）| V3 默认 + graphify 组合 | V3 `--mode task` + graphify `query_graph` |
| 跨概念组合（"带下拉刷新的网络列表页"）| graphify | MCP `query_graph` + `get_neighbors` |
| 语义模糊描述（"卡顿"/"响应式失效"）| graphify | MCP `query_graph`（LLM 语义边） |
| 跨生态类比（"鸿蒙版 RecyclerView"）| graphify | MCP `query_graph` + `god_nodes` |
| "A 和 B 怎么配合" / 依赖链 | graphify | MCP `shortest_path` + `get_neighbors` |
| "这个领域的核心 API" | graphify | MCP `god_nodes` |
| 架构鸟瞰 / 社区洞察 | graphify | MCP `get_community` |

### V3 调用（精确检索）

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search/search_v3.py "<query>" --json --limit 5
```

- 功能实现类问题优先 `auto`，必要时补 `--mode task`
- API / 属性 / 装饰器问题使用 `--mode api`
- 写代码前至少补一次 `--mode example`
- 排错问题保留错误关键词、API 名、组件名、模块名或错误码
- Top5 不相关时换 query 重查或切图谱，不允许只凭模型记忆编造 API

`--json` 稳定字段：`query` / `mode` / `understanding` / `tasks` / `apis` / `examples` / `docs` / `paths`。

### graphify KG 调用（语义 / 组合 / 架构）

通过 MCP 调用（参见 `knowledge-graph-template/MCP_USAGE.md`），7 个工具：

- `query_graph(query, limit, graph?)` —— 语义搜索，跨概念关联首选
- `get_neighbors(node, depth, limit)` —— 典型搭档 / 邻域展开
- `shortest_path(source, target, max_depth)` —— 关联链（限同子图）
- `god_nodes(top_n)` —— 领域核心 API
- `get_community(community_id)` —— 功能领域聚簇
- `get_node(node)` —— 节点详情
- `graph_stats()` —— 规模统计

若 MCP 未接入，可 subprocess 兜底：
```bash
python <CangjieSkills>/.agents/skills/knowledge-graph-template/cli.py traverse "<query>" --depth 3
python <CangjieSkills>/.agents/skills/knowledge-graph-template/cli.py god-nodes --top-n 10
```

### 结果融合规则

当两条引擎同时被调用时：

1. **精确命中优先**：V3 返回的 `paths`（匹配 `HIGH_VALUE_API_MAP` 的）排在 graphify 之前
2. **按 `source_file` / `source_paths` 去重**：同一文档不重复
3. **graphify 补充邻域**：V3 没覆盖的相关概念从 graphify `get_neighbors` 拉进来作为"扩展阅读"
4. **矛盾时以 V3 为准**：API 名、签名、参数类型这类事实性信息以 V3 卡片为单一事实源，graphify 只提供关联线索

编码前必须基于命中的 `tasks/apis/examples/docs/paths` 确认 API 名、import、参数、返回值、权限配置和示例写法。
