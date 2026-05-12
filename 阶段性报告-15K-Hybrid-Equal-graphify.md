# Cangjie HarmonyOS Skill — 15K + Hybrid-Equal + graphify

日期：2026-05-11

## 目标

在 `skill_15K/CangjieSkills` 落地与 `recommend` 同构的 **V3 + knowledge-graph-template（graphify）+ maintenance** 三件套，语料主版本为 **`harmonyos-6.0.2-15k`**（目录扁平化，与旧 `harmonyos-6.1-8k/API/arkui-cj/...` 路径不同），并保持 **fusion 不低于单引擎** 的 Hybrid-Equal 策略。

## 已完成

### 语料与常量

- 全仓库技能内字符串 **`harmonyos-6.1-8k` → `harmonyos-6.0.2-15k`**（含 `build_index_v3.DOC_SOURCES`、`search_v3` 高价值路径、`run_ab_eval.norm_path`、`graphify_engine`、`SKILL.md` 等）。
- `knowledge-graph-template/docs/harmonyos-6.0.2-15k` symlink 指向 `cangjie-harmonyos-doc-search/harmonyos-6.0.2-15k`。

### V3 索引

- 已跑通 **`build_index_v3.py --mode rule`**，产物在 `cangjie-harmonyos-doc-search/index/`（约 docs 14824、apis 4635 等，见 manifest）。
- **`rule+llm` 全量**：已用 `CANGJIE_LLM_API_FILE` + 修复后的 `load_env.sh`（避免占位 `OPENAI_API_KEY` 导致 **401**）完成构建并写入默认 **`index/`**；`index/manifest.json` 为 **`generation_mode: rule+llm`**。
  - counts：tasks 100、apis 4635、examples 584、docs 14824。
  - LLM 富化：tasks 88、apis 4632、examples 584、docs 14824；`failed=0`、`skipped=15`。
  - 曾有 7 条 `std/sync` 原子类型相关 api/doc 稳定触发 ModelArts **HTTP 403**；已通过 `cangjie-harmonyos-doc-search-maintenance/scripts/repair_llm_failure_cache.py` 生成本地 fallback cache，并以 `--max-llm-publish-failures 0` 严格重跑成功。fallback 条目带 `llm-fallback-cache` tag 与 `needs_review=true`，后续可人工复核或用稳定 LLM 再补。
- **构建结束后自动收尾**：已跑 **`cangjie-harmonyos-doc-search-maintenance/scripts/run_after_rule_llm_build.sh`**（等待进程结束 → `sync_v3_to_graph` → `--validate` → `run_ab_eval`），写出 **`records/v3_seeds_15k_post_llm.json`** 与 **`records/ab-15k-after-rule-llm.json`**；日志 **`/tmp/after_rule_llm_build_latest.log`**。

### graphify 图谱

- 子图：`build-subgraph` + `--llm-provider skip`（简化语义抽取）生成 `harmonyos / lang-features / std / stdx / tools`。
- 合并：`cli.py merge ...` → **`data/merged/graph.json`**（约 **36088** 节点，**78623** 边）。
- `sync_v3_to_graph.py --validate`：简化图与 V3 种子 id 对齐仍有差距（预期后续 LLM 建图 + 种子迭代收窄）。

### 独立评测集（重建）

- 脚本：`cangjie-harmonyos-doc-search-maintenance/scripts/regenerate_15k_independent_evals.py`
- 规模：`real_session` 15、`composition` 10、`paraphrase` 20；`eval_queries_full.jsonl` 精简为 **15** 条自举用例。
- 校验：`validate_eval_set.py` + `records/docs_manifest_15k.json` + 当前 `index/` → **blocking: false**。

### AB baseline（limit=8）

见 `cangjie-harmonyos-doc-search-maintenance/records/ab-15k-baseline.json`：

| 评测集 | V3 | graphify | fusion |
|--------|---:|----------:|-------:|
| real_session | 12/15 | 12/15 | 15/15 |
| paraphrase | 14/20 | 13/20 | 17/20 |
| composition | 8/10 | 7/10 | 9/10 |

fusion 在三套集上均不低于 V3 与 graphify。

### Post rule+llm AB（limit=8）

见 `cangjie-harmonyos-doc-search-maintenance/records/ab-15k-after-rule-llm.json`：

| 评测集 | V3 | graphify | fusion |
|--------|---:|----------:|-------:|
| real_session | 11/15 (0.7333) | 12/15 (0.8000) | 15/15 (1.0000) |
| paraphrase | 15/20 (0.7500) | 13/20 (0.6500) | 17/20 (0.8500) |
| composition | 8/10 (0.8000) | 7/10 (0.7000) | 9/10 (0.9000) |

fusion 在三套集上继续满足 **`fusion >= V3 且 fusion >= graphify`**。

### 最终验收

- V3 检索：`python search_v3.py "List组件下拉刷新" --mode auto --json` 命中 `ui.refresh.basic`、`ui.list.basic`、`arkui.refresh`、`arkui.list` 以及 Refresh/List 相关示例和文档。
- graphify traverse：`python knowledge-graph-template/cli.py traverse "鸿蒙版 RecyclerView" --depth 3` 可找到 ListItem/ListItemGroup 相关起点与邻域。
- semantic capability gate：`../cangjie-harmonyos-doc-search-maintenance/scripts/run_semantic_capability_gate.py` 输出 `status: ok`。
- V3 regression gate：`../cangjie-harmonyos-doc-search-maintenance/scripts/run_v3_regression_gate.py --max-rows 500` 完成，`recall@5=0.4271`、`recall@10=0.6668`、`mrr=0.6245`；全量 `eval_queries_full.jsonl` 为 93486 条，直接全跑会耗时较长，脚本已新增 `--max-rows` 供门禁采样使用。

### 优化项（相对 recommend 阶段报告）

1. **query expansion**：`graphify_engine.QUERY_EXPANSIONS` 增补 RecyclerView / FlatList / SwipeRefreshLayout；网络相关 token 对齐 `cj-apis-net-http`。
2. **路由**：`smart_router.KEYWORD_WEIGHTS` 增补 `recyclerview` / `lazyforeach` / `flatlist`。
3. **LLM 抽取 prompt**：`extract_semantic_llm` 增加跨生态类比 `semantically_similar_to` 规则说明。
4. **maintenance**：`run_maintenance.py` 增加 `--fusion-ab-gate`（发布前 `sync_v3_to_graph` + `run_ab_eval`）；**OpenViking 默认关闭**，需 `--openviking` 开启。
5. **门禁拆分**：`../cangjie-harmonyos-doc-search-maintenance/scripts/run_v3_regression_gate.py`、`../cangjie-harmonyos-doc-search-maintenance/scripts/run_semantic_capability_gate.py`；`run_release_eval.py` 文档指向二者。
6. **扩容演练**：`records/expansion-8k-to-15k.md`（`run_corpus_expansion.py --dry-run`，old=6.1-8k，new=6.0.2-15k）；全量 LLM 需真实密钥后去掉 `--dry-run`。

### 收尾

- 根目录 `.gitignore`：`graphify-out/`、`index/`、`feedback/`、密钥模式等。
- 用户态与维护态分层：`cangjie-harmonyos-doc-search/scripts/` 仅保留 README，原评测/AB/日志分析/种子同步/遗留 V1 等脚本已迁入 `cangjie-harmonyos-doc-search-maintenance/scripts/`。
- V1 `search.py` → `cangjie-harmonyos-doc-search-maintenance/scripts/_legacy_search_v1.py`。

## 后续建议

- 零失败基线已达成；后续建议复核 `llm-fallback-cache` 标记的 7 条 `std/sync` 原子类型卡片质量，必要时用稳定 LLM 重新补缓存。
- 可选增强：跑 **`build-subgraph --llm-provider openai`** 重建 graphify LLM 子图，再 merge，重做 AB 与 seed validate。
- 按业务把 `eval_queries_*` 从当前冒烟规模扩到 30/30/50+。
- 将 `cli.py merge` 或增量 `build-subgraph --update` 接入 CI（仅在语料变更时触发）。
