---
name: cangjie-hmos-doc-search-maintenance
description: "维护 cangjie-hmos-doc-search 的文档更新、索引/卡片重建、图谱构建与 LLM 离线增强、三引擎评测、发布门禁流程。支持 OpenAI 兼容 LLM 端点（GLM-5.2/DashScope 等）。适用于文档变化后重建检索索引/图谱数据、跑 enhance-graph 补全中文关键词、三引擎评测对比、发布门禁判定 pass/gray_release/blocked。"
tags: [workflow, evaluation, maintenance, platform]
---

# cangjie-hmos-doc-search-maintenance

## 目录结构

```
cangjie-hmos-doc-search-maintenance/
├── card/                    # 卡片索引（doc-card）构建与评测
│   ├── builder/             # build_index_v3.py, high_value_tasks_ext.py
│   ├── evals/               # content-basic.jsonl, discovery.jsonl
│   ├── records/             # run-history/, baselines/, changelog, seeds
│   ├── references/          # workflow-overview.md, indexing-rules.md, llm-enrichment.md, ...
│   └── scripts/             # run_maintenance.py, run_ab_eval.py, eval_bench.py, ...
├── graph/                   # 知识图谱（doc-graph）构建与评测
│   ├── builder/             # doc/extractor+builder, code/extractor+builder, llm/enhancer+pipeline, builders/
│   ├── evals/               # run_eval.py, datasets/, keywords_v7_prompt.json
│   ├── records/             # docs_statistics.json, baselines/, run-history/
│   ├── references/          # BUILD_GUIDE.md, ARCHITECTURE.md
│   └── scripts/             # build_doc_graph.py, build_code_graph.py, validate_graph_data.py, ...
├── fusion/                  # 融合发布门禁（V3 + doc-graph fusion AB）
│   ├── evals/               # 15 JSONL 评测集（real_session, paraphrase, composition, ...）
│   ├── records/             # run-history/, baselines/, changelog.md
│   ├── references/          # (空，card references 覆盖大部分)
│   └── scripts/             # run_maintenance.py, run_ab_eval.py, run_release_eval.py, ...
└── SKILL.md
```

## 与 doc-search 的关系

`cangjie-hmos-doc-search` 是用户面向的搜索运行时（仅搜索，不构建），包含：
- `doc-card/search_v3.py` — 卡片索引搜索
- `doc-graph/cli.py` — 知识图谱搜索 CLI（search/path/explain/neighbors/god-nodes/surprises/stats/export）
- `doc-graph/query.py` — GraphSession，双图搜索引擎
- `unified_search.py` — fusion 入口，编排 card + graph

maintenance 负责：
- card 端：重建索引（rule / rule+llm），评测卡片搜索质量
- graph 端：构建图谱数据（doc/code/merged graph.json），评测图搜索质量
- fusion 端：AB 门禁确保 fusion 召回不低于单引擎

构建产物写入 doc-search 运行时目录：
- card → `cangjie-hmos-doc-search/doc-card/index/`
- graph → `cangjie-hmos-doc-search/doc-graph/data/`

## 适用场景

在以下情况使用本 Skill：

- `cangjie-hmos-doc-search` 的文档路径或正文内容更新
- 需要重建 `rule` 或 `rule+llm` 索引/卡片 → `card/scripts/run_maintenance.py`
- 需要重建知识图谱数据 → `graph/builder/build_cli.py` 或 `graph/scripts/build_doc_graph.py`
- 需要基于文档 diff 生成候选 query 或新严格 blind 集
- 需要检查主评测集是否因文档变化失效
- 需要运行发布门禁并输出 `pass / gray_release / blocked` → `fusion/scripts/run_maintenance.py`
- 需要收集真实搜索日志、失败反馈并沉淀候选评测素材

不适用：

- 在线回答普通用户的 HarmonyOS/Cangjie API 用法问题。此类问题使用 `cangjie-hmos-doc-search`。
- 未经评测直接替换正式 `index/` 或 `data/`。
- 自动把候选 query 合并进主门禁。

## card 分区 — 卡片索引维护

### 标准流程

```bash
cd .agents/skills/cangjie-hmos-doc-search-maintenance

PYTHONDONTWRITEBYTECODE=1 python card/scripts/build_doc_manifest.py \
  --output /tmp/doc_manifest_current.json

PYTHONDONTWRITEBYTECODE=1 python card/scripts/diff_doc_manifest.py \
  --old /tmp/doc_manifest_old.json \
  --new /tmp/doc_manifest_current.json \
  --output /tmp/doc_diff.json

PYTHONDONTWRITEBYTECODE=1 python card/builder/build_index_v3.py \
  --mode rule \
  --docs-dir <docs_corpus_dir> \
  --index-dir /tmp/cangjie-index-rule

PYTHONDONTWRITEBYTECODE=1 python card/scripts/run_release_eval.py \
  --index-dir /tmp/cangjie-index-rule \
  --output-dir /tmp/cangjie-release-eval
```

### LLM 卡片重建

`rule+llm` 是离线构建能力，只在维护阶段调用 OpenAI 兼容 API。

```bash
OPENAI_BASE_URL="..." \
OPENAI_API_KEY="..." \
OPENAI_MODEL="..." \
OPENAI_TEMPERATURE="0" \
PYTHONDONTWRITEBYTECODE=1 python card/builder/build_index_v3.py \
  --mode rule+llm \
  --docs-dir <docs_corpus_dir> \
  --index-dir /tmp/cangjie-index-llm \
  --llm-card-types task,api,example,doc \
  --llm-concurrency 24 \
  --llm-cache-dir /tmp/cangjie-llm-cache
```

约束：

- 默认先写临时索引目录，不直接覆盖正式 `index/`。
- 发布前必须跑 `card/scripts/run_release_eval.py --index-dir /tmp/cangjie-index-llm`。
- `llm.failed > 0` 或任一卡片类型未完成增强时，不允许发布 `rule+llm` 索引。
- 需要详细约束时读取 `card/references/llm-enrichment.md`。

## graph 分区 — 知识图谱维护

### 构建图谱

```bash
PYTHONDONTWRITEBYTECODE=1 python graph/builder/build_cli.py build \
  --docs-dir <docs_corpus_dir> \
  [--code-dir <code_corpus_dir>] \
  --graph-dir cangjie-hmos-doc-search/doc-graph/data

# 单步构建
PYTHONDONTWRITEBYTECODE=1 python graph/builder/build_cli.py build-doc \
  --docs-dir <docs_corpus_dir>

PYTHONDONTWRITEBYTECODE=1 python graph/builder/build_cli.py build-code \
  --code-dir <code_corpus_dir>

PYTHONDONTWRITEBYTECODE=1 python graph/builder/build_cli.py merge --graph-dir <graph_dir>

# LLM 增强（可选）— 补全中文关键词，en-only 从 9336→417
# 支持任何 OpenAI 兼容 LLM 端点（不限于 DashScope），env 变量名保持 DASHSCOPE_* 是历史命名
# 合并策略保护 API 名不被覆盖（ClientCert/Grid 等保留）、keywords 增量去重合并
DASHSCOPE_API_KEY="..." \
DASHSCOPE_API_BASE="..." \
DASHSCOPE_MODEL="GLM-5.2" \
PYTHONDONTWRITEBYTECODE=1 python graph/builder/build_cli.py enhance-graph \
  --graph-dir <graph_dir> \
  --docs-dir <docs_corpus_dir>
```

### 评测图谱搜索

```bash
PYTHONDONTWRITEBYTECODE=1 python graph/evals/run_eval.py --limit 50
PYTHONDONTWRITEBYTECODE=1 python graph/scripts/run_graph_release_eval.py
```

### 验证图谱数据

```bash
PYTHONDONTWRITEBYTECODE=1 python graph/scripts/validate_graph_data.py
```

## fusion 分区 — 融合发布门禁

### Fusion AB 门禁

`fusion/scripts/run_maintenance.py` 支持 `--fusion-ab-gate`：在发布候选 `index/` 前执行 `sync_v3_to_graph` + `run_ab_eval`（`real_session` / `paraphrase` / `composition`），要求 **fusion 召回不低于 V3 与 doc-graph**。

```bash
PYTHONDONTWRITEBYTECODE=1 python fusion/scripts/run_maintenance.py \
  --fusion-ab-gate \
  [--openviking] \
  --note "重建 reason"
```

### 独立 AB 评测

```bash
PYTHONDONTWRITEBYTECODE=1 python fusion/scripts/run_ab_eval.py \
  --eval-dir fusion/evals \
  --index-dir cangjie-hmos-doc-search/doc-card/index \
  --graph-dir cangjie-hmos-doc-search/doc-graph/data \
  --splits real_session,paraphrase,composition \
  --limit 5
```

## 测试集与候选集规则

- 主评测集只接受审核后的 query。
- `card/scripts/generate_eval_candidates_from_doc_diff.py` 和 `card/scripts/analyze_search_logs.py` 产物只能进入候选池。
- `card/scripts/validate_eval_set.py` 出现 `missing_path` 时发布必须 blocked。
- 候选集失败不阻塞发布，但必须记录。
- 已经用于调参的 blind 集降级为回归集，不再作为严格盲测。

## 严格 Blind 轮换

生成新的时间戳 blind 集：

```bash
PYTHONDONTWRITEBYTECODE=1 python card/scripts/generate_appdev_eval_batch3_blind.py \
  --strict-blind-out card/evals/eval_queries_user_appdev_blind_YYYYMMDD.jsonl \
  --strict-source strict-blind-YYYYMMDD
```

首跑后立即记录结果，作为严格 blind 首次基线。

## 真实 Query 闭环

```bash
DOC_SEARCH_LOG_PATH=/tmp/search-events.jsonl \
PYTHONDONTWRITEBYTECODE=1 python search_v3.py "WebView loadUrl headers 怎么传" --json --limit 5

PYTHONDONTWRITEBYTECODE=1 python card/scripts/record_search_feedback.py \
  --log /tmp/search-events.jsonl \
  --query "WebView loadUrl headers 怎么传" \
  --out /tmp/real_failed_queries.jsonl \
  --reason "top5_not_helpful"

PYTHONDONTWRITEBYTECODE=1 python card/scripts/analyze_search_logs.py \
  --log /tmp/search-events.jsonl \
  --feedback /tmp/real_failed_queries.jsonl \
  --output-dir /tmp/search-log-analysis
```

日志不得包含 API key、环境变量、用户工程代码或完整文档正文。

## 当前基线

### card 单引擎旧基线

全量发布评估（card-only，未含 graph/fusion）：
- 7 套评测集，合计 814 条，`release status = pass`
- 所有套件 `success@5 = 1.0`、`error_rate = 0.0`
- 健康检查：所有套件 `blocking = false`、`issue_counts = {}`
- 严格 blind：`fusion/evals/eval_queries_user_appdev_blind_20260424.jsonl`，80 条，首跑 `success@1 = 0.875`、`success@5 = 1.0`

> 此基线仅覆盖 card 单引擎，不含 graph/fusion 评测。

### 三引擎评测基线（0629，192 条全量）

评测集：`graph/evals/datasets/eval_queries_comprehensive_deduped.jsonl`（192 条去重集）

| 指标 | card | graph | fusion |
|---|---:|---:|---:|
| Recall@5 | 34.9% | **91.7%** | 77.6% |
| MRR | 0.133 | 0.460 | 0.422 |
| 平均耗时 | 69.6ms | **1.7ms** | 66.5ms |

已知问题：fusion 77.6% < graph 91.7%，根因是 `unified_search.fuse_results` 中 card 路径挤占 graph 命中位。50 条子集上 fusion=78% vs graph=96%。属独立优化点。

图谱数据状态：11,661 nodes / 17,154 links / 11,107 llm_enhanced / 417 en-only。

## 参考资料

card 分区：
- 流程总览：`card/references/workflow-overview.md`
- 索引与卡片规则：`card/references/indexing-rules.md`
- LLM 补全约束：`card/references/llm-enrichment.md`
- 评测说明：`card/references/evaluation-guide.md`
- 故障排查：`card/references/troubleshooting.md`

graph 分区：
- 构建指南：`graph/references/BUILD_GUIDE.md`
- 架构说明：`graph/references/ARCHITECTURE.md`