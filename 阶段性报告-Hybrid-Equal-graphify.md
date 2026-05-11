# Cangjie HarmonyOS Skill 阶段性报告（Hybrid-Equal + graphify）

日期：2026-05-11

## 目标

本阶段目标是验证并落地一套更适合 code agent 开发鸿蒙/仓颉应用时使用的知识检索方案。原 V3 方案在精确 API、属性、示例和错误检索上可用，但在跨概念组合查询、规则表外新组件泛化、架构/依赖/跨文件线索上存在明显短板。因此本阶段采用 V3 与 graphify 平权互补的 Hybrid-Equal 方案。

## 已完成内容

### 1. 能力分发方案

已将 `cangjie-harmonyos-doc-search/SKILL.md` 更新为能力对齐分发协议：

- V3 负责明确 API、组件、属性、事件、装饰器、错误码、示例等精确检索。
- graphify KG 负责功能实现、跨概念组合、语义模糊、跨生态类比、依赖链和架构鸟瞰。
- fusion 层按 source path 去重，V3 精确事实优先，graphify 补充语义邻域。

### 2. graphify 知识图谱能力

已引入 `knowledge-graph-template`，并完成 HarmonyOS / Cangjie 文档图谱构建与查询改造：

- 新增 MCP stdio server，暴露 `query_graph`、`get_node`、`get_neighbors`、`get_community`、`god_nodes`、`graph_stats`、`shortest_path`。
- 默认优先加载 `data/merged/graph.json`，兼容旧 `graph_layered.json`。
- 增加中文自然语言 query expansion，覆盖列表、下拉刷新、网络请求、卡顿、WebView 双向通信等高频场景。
- traversal 起点改为多概念簇选择，避免组合查询只命中单一概念。
- LLM semantic cache 已按 `model + api_base + prompt_version + file hash` 隔离，避免换模型后误复用缓存。
- LLM 抽取失败会写入 `graphify-out/failures.jsonl`，运行缓存和反馈日志已加入忽略规则。

当前图谱规模：

| 图谱 | 节点 | 边 |
|---|---:|---:|
| merged | 6114 | 6388 |
| harmonyos | 6335 | 5921 |
| lang-features | 563 | 500 |
| std | 3555 | 3330 |
| stdx | 556 | 660 |
| tools | 86 | 73 |

### 3. V3 与 graphify 对齐

- 新增 `sync_v3_to_graph.py`，从 V3 index 生成 graphify seeds，用于对齐任务、API、别名和 source path。
- 新增 `high_value_tasks_ext.py`，将 V3 高价值任务从原有小集合扩展到更多应用开发场景。
- `build_index_v3.py` 已接入扩展任务，保持原 V3 主流程兼容。

### 4. 独立评测体系

新增三套独立评测集，避免继续只依赖 V3 自举 full eval：

- `eval_queries_real_session.jsonl`：真实/拟真实 agent session 查询。
- `eval_queries_composition.jsonl`：组合功能查询，包含概念簇覆盖要求。
- `eval_queries_paraphrase.jsonl`：同一意图的多表述改写稳健性评测。

新增 `run_ab_eval.py`，支持 V3、graphify、fusion 三组对比。

最新评测结果（limit=8）：

| 评测集 | V3 | graphify | fusion |
|---|---:|---:|---:|
| real_session | 10/30 = 0.3333 | 6/30 = 0.2000 | 13/30 = 0.4333 |
| composition | 4/30 = 0.1333 | 9/30 = 0.3000 | 11/30 = 0.3667 |
| paraphrase | 21/50 = 0.4200 | 22/50 = 0.4400 | 29/50 = 0.5800 |

组合概念覆盖率：

| 引擎 | composition_recall@concept |
|---|---:|
| V3 | 0.2139 |
| graphify | 0.1556 |
| fusion | 0.3167 |

结论：fusion 在三组评测中均优于单引擎，尤其在组合查询和 paraphrase 改写场景提升明显。但 real_session 召回仍只有 0.4333，说明图谱路径对齐、语义边质量、query expansion 仍有继续优化空间。

### 5. 构建与扩容链路

新增维护脚本：

- `env.example`：LLM 构建环境变量模板。
- `load_env.sh`：从本地 key 文件加载 ModelArts OpenAI-compatible 配置，key 不入库。
- `run_corpus_expansion.py`：支持 `auto`、`incremental`、`mixed`、`full-rebuild` 三种扩容模式，具备 dry-run、smoke-test、LLM 调用上限等护栏。

安全约束：

- `.gitignore` 已忽略 `LLM_API信息.txt`、`.env*`、`*api_key*`、`*api-key*`。
- graphify 构建缓存 `graphify-out/` 和查询日志 `knowledge-graph-template/data/feedback/*.jsonl` 不入库。
- 大图谱 JSON 已配置 Git LFS。

## 当前判断

1. Hybrid-Equal 方向成立：fusion 实测比 V3-only 和 graphify-only 更稳。
2. graphify 对组合查询有价值，但还需要继续提高 source path 对齐和语义边质量。
3. V3 仍适合作为精确 API/属性/错误/示例检索的事实源，不应被 graphify 完全替代。
4. 旧 `eval_queries_full.jsonl` 仍是 V3 自举回归门禁，不属于新独立评测主线；本阶段不建议把它的刷新作为核心成果提交。

## 后续建议

- 基于 AB 失败 case 补 query expansion 和 path normalization。
- 对 graphify 低召回 query 做 seed 注入和边质量补强。
- 将 `run_maintenance.py` 正式串起 V3 build、sync seeds、graphify update、AB gate。
- 将 `run_release_eval.py` 拆分为 V3 regression gate 和 semantic capability gate。
- 在真实 8K → 15K 文档扩容场景中演练 `run_corpus_expansion.py`。
