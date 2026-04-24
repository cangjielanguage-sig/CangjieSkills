# Cangjie HarmonyOS Doc Search 持续迭代计划

## Summary

当前 V3 搜索已经从“文档路径/卡片定位”推进到“用户态 App 开发问题能否搜到可用入口”。现有约 814 条用户态评测集，覆盖 UI、路由、状态、权限、网络、WebView、媒体、相机、文件、数据库、定位、传感器、蓝牙、IPC、HUKS、ArkTS 互操作、日志、设备信息等场景。多套调参后评测集当前 `success@5 = 1.0`，严格盲测首跑 `success@5 = 0.875`，具备灰度发布基础。

下一阶段目标不是继续盲目扩测试集，而是补齐可持续机制：真实 query/失败收集、文档更新后的索引重建与测试集健康检查、候选测试集生成、发布评估流水线。

## Key Changes

### 1. 真实 query 与失败收集

为 `search_v3.py` 增加默认关闭的本地搜索事件日志：

```bash
DOC_SEARCH_LOG_PATH=/tmp/search-events.jsonl python search_v3.py "WebView loadUrl headers 怎么传" --json --limit 5
```

日志 JSONL 每行记录：

- `timestamp`
- `query`
- `mode`
- `understanding_mode`
- `index_dir`
- `index_manifest_generated_at`
- `limit`
- `latency_ms`
- `top_paths`
- `top_titles`
- `result_count`
- `error`

安全约束：

- 不记录 API key。
- 不记录环境变量。
- 不记录用户工程代码。
- 不记录完整文档正文。

新增 `record_search_feedback.py`，用于把真实失败显式登记为候选问题：

```bash
python record_search_feedback.py \
  --log /tmp/search-events.jsonl \
  --query "WebView loadUrl headers 怎么传" \
  --out /tmp/real_failed_queries.jsonl \
  --reason "top5_not_helpful"
```

新增 `analyze_search_logs.py`：

- 汇总高频 query。
- 汇总无结果 query。
- 汇总被人工标记失败的 query。
- 输出候选评测集 `eval_candidates_from_logs.jsonl`。
- 候选集不直接进入主门禁。

### 2. 文档更新后的索引与测试集维护

新增 `build_doc_manifest.py`：

```bash
python build_doc_manifest.py --output /tmp/doc_manifest_current.json
```

新增 `diff_doc_manifest.py`：

```bash
python diff_doc_manifest.py \
  --old /tmp/doc_manifest_old.json \
  --new /tmp/doc_manifest_current.json \
  --output /tmp/doc_diff.json
```

新增 `validate_eval_set.py`：

```bash
python validate_eval_set.py \
  --eval-set eval_queries_user_appdev.jsonl \
  --index-dir index \
  --doc-manifest /tmp/doc_manifest_current.json \
  --output /tmp/eval-health.json
```

检查：

- `acceptable_paths` 是否还能在当前文档或索引中找到。
- `must_contain` 是否可能过窄。
- query 是否重复。
- query 是否包含路径残片、自动模板味、`doc/task` 等非用户态词。
- 按 `capability/category/query_style/difficulty` 输出覆盖统计。
- 主评测集如出现阻塞级 `missing_path`，发布结论必须 blocked。

新增 `generate_eval_candidates_from_doc_diff.py`：

- 输入 `doc_diff.json` 和当前索引元数据。
- 只为新增或明显变化文档生成候选 query。
- 输出 `eval_queries_user_candidates.jsonl`。
- 候选 query 只进入候选池，不自动合并到主集。

### 3. 发布评估流水线

新增 `run_release_eval.py`：

```bash
PYTHONDONTWRITEBYTECODE=1 python run_release_eval.py \
  --output-dir /tmp/cangjie-doc-search-release-eval
```

默认不重建索引，只复用当前 `index/`。如需文档更新后重建：

```bash
PYTHONDONTWRITEBYTECODE=1 python run_release_eval.py \
  --rebuild-index \
  --output-dir /tmp/cangjie-doc-search-release-eval-rebuild
```

流程：

1. 生成当前文档 manifest 到输出目录。
2. 如传入 `--previous-doc-manifest`，生成文档 diff。
3. 如传入 `--rebuild-index`，执行 `build_index_v3.py --mode rule`。
4. 校验核心评测集健康状态。
5. 依次运行本地 V3 评测：
   - `eval_queries_user.jsonl`
   - `eval_queries_user_appdev.jsonl`
   - `eval_queries_user_appdev_next.jsonl`
   - `eval_queries_user_appdev_frozen.jsonl`
   - `eval_queries_user_appdev_batch2.jsonl`
   - `eval_queries_user_appdev_batch3.jsonl`
   - `eval_queries_user_appdev_blind.jsonl`
6. 每套评测后运行 `analyze_user_eval_failures.py`。
7. 汇总生成：
   - `release-summary.json`
   - `release-report.md`
   - `eval-health-summary.json`
   - 每套评测独立目录下的 `summary.json/details.jsonl/diff.md/failure-summary.json`

默认门禁：

- `eval_queries_user.jsonl`：`success@5 >= 0.98` 且 `error_rate = 0`
- `eval_queries_user_appdev*.jsonl`：`success@5 >= 0.95` 且 `error_rate = 0`
- 严格新盲测集：`success@5 >= 0.80`
- 主评测集有 `missing_path`：直接 `blocked`
- 候选集失败：只记录，不阻塞发布

发布报告结论必须是三选一：

- `pass`
- `gray_release`
- `blocked`

## Test Plan

基础编译检查：

```bash
cd /workspace/docs/CangjieSkills/.agents/skills/cangjie-harmonyos-doc-search

PYTHONDONTWRITEBYTECODE=1 python -m py_compile \
  search_v3.py \
  record_search_feedback.py \
  analyze_search_logs.py \
  build_doc_manifest.py \
  diff_doc_manifest.py \
  validate_eval_set.py \
  generate_eval_candidates_from_doc_diff.py \
  run_release_eval.py
```

搜索日志验证：

```bash
DOC_SEARCH_LOG_PATH=/tmp/search-events.jsonl \
PYTHONDONTWRITEBYTECODE=1 python search_v3.py "WebView loadUrl headers 怎么传" --json --limit 5
```

反馈收集验证：

```bash
PYTHONDONTWRITEBYTECODE=1 python record_search_feedback.py \
  --log /tmp/search-events.jsonl \
  --query "WebView loadUrl headers 怎么传" \
  --out /tmp/real_failed_queries.jsonl \
  --reason "top5_not_helpful"
```

文档 manifest 与测试集健康检查：

```bash
PYTHONDONTWRITEBYTECODE=1 python build_doc_manifest.py \
  --output /tmp/doc_manifest_current.json

PYTHONDONTWRITEBYTECODE=1 python validate_eval_set.py \
  --eval-set eval_queries_user.jsonl \
  --index-dir index \
  --doc-manifest /tmp/doc_manifest_current.json \
  --output /tmp/eval-health.json
```

发布评估验证：

```bash
PYTHONDONTWRITEBYTECODE=1 python run_release_eval.py \
  --output-dir /tmp/cangjie-doc-search-release-eval
```

验收：

- 所有新增脚本可编译。
- 默认不写搜索日志，设置 `DOC_SEARCH_LOG_PATH` 后才写。
- 搜索日志不包含敏感信息。
- 测试集健康检查能发现失效路径和重复 query。
- 发布报告能明确输出 `pass/gray_release/blocked`。
- 不触发 OpenViking 网络 AB，除非用户单独要求。

## Assumptions

- 第一版只做本地 JSONL 机制，不接入线上服务或数据库。
- 文档变化后必须重建索引，但测试集只做健康检查和局部补齐，不全量推倒重来。
- 真实失败 query 先进入候选池，人工或后续 agent 审核后再进入主评测集。
- 300 条 `eval_queries_sampled.jsonl` 继续保留为覆盖率/路径定位辅助诊断，不作为主发布结论。
- `eval_queries_user_appdev_blind.jsonl` 当前已被后续调参污染，不能继续当严格新盲测；后续需要生成时间戳化的新 blind 文件。
- 默认不使用外部 API key，不保存用户给过的 key。
- 不执行 `git commit`、`git push`、`git reset`。
