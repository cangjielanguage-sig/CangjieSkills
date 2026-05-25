---
name: cangjie-harmonyos-doc-search-maintenance
description: "维护 cangjie-harmonyos-doc-search 的文档更新、索引/卡片重建、LLM 离线增强、候选 query 生成、评测集健康检查、严格 blind 轮换和发布门禁流程。适用于文档路径或内容变化后重新生成检索索引、测试素材并判断 pass/gray_release/blocked。"
tags: [workflow, evaluation, maintenance, platform]
---

# cangjie-harmonyos-doc-search-maintenance

## 适用场景

在以下情况使用本 Skill：

- `cangjie-harmonyos-doc-search` 的文档路径或正文内容更新
- 需要重建 `rule` 或 `rule+llm` 索引/卡片
- 需要基于文档 diff 生成候选 query 或新严格 blind 集
- 需要检查主评测集是否因文档变化失效
- 需要运行发布门禁并输出 `pass / gray_release / blocked`
- 需要收集真实搜索日志、失败反馈并沉淀候选评测素材

不适用：

- 在线回答普通用户的 HarmonyOS/Cangjie API 用法问题。此类问题使用 `cangjie-harmonyos-doc-search`。
- 未经评测直接替换正式 `index/`。
- 自动把候选 query 合并进主门禁。

## 标准流程

文档更新后优先执行这一条可复用链路：

```bash
cd .agents/skills/cangjie-harmonyos-doc-search

PYTHONDONTWRITEBYTECODE=1 python scripts/build_doc_manifest.py \
  --output /tmp/doc_manifest_current.json

PYTHONDONTWRITEBYTECODE=1 python scripts/diff_doc_manifest.py \
  --old /tmp/doc_manifest_old.json \
  --new /tmp/doc_manifest_current.json \
  --output /tmp/doc_diff.json

PYTHONDONTWRITEBYTECODE=1 python build_index_v3.py \
  --mode rule \
  --index-dir /tmp/cangjie-index-rule

PYTHONDONTWRITEBYTECODE=1 python scripts/generate_eval_candidates_from_doc_diff.py \
  --doc-diff /tmp/doc_diff.json \
  --index-dir /tmp/cangjie-index-rule \
  --output /tmp/eval_candidates_from_doc_diff.jsonl

PYTHONDONTWRITEBYTECODE=1 python scripts/run_release_eval.py \
  --index-dir /tmp/cangjie-index-rule \
  --output-dir /tmp/cangjie-release-eval
```

发布结论以 `scripts/run_release_eval.py` 输出为准。报告必须包含 `release-summary.json`、`release-report.md` 和各评测集的 `eval-health.json / summary.json / details.jsonl / failure-summary.json`。

## LLM 卡片重建

`rule+llm` 是离线构建能力，只在维护阶段调用 OpenAI 兼容 API；用户查询运行时不调用外部 LLM。

```bash
OPENAI_BASE_URL="..." \
OPENAI_API_KEY="..." \
OPENAI_MODEL="..." \
OPENAI_TEMPERATURE="0" \
PYTHONDONTWRITEBYTECODE=1 python build_index_v3.py \
  --mode rule+llm \
  --index-dir /tmp/cangjie-index-llm \
  --llm-card-types task,api,example,doc \
  --llm-concurrency 24 \
  --llm-cache-dir /tmp/cangjie-llm-cache
```

约束：

- 默认先写临时索引目录，不直接覆盖正式 `index/`。
- 发布前必须跑 `scripts/run_release_eval.py --index-dir /tmp/cangjie-index-llm`。
- `llm.failed > 0` 或任一卡片类型未完成增强时，不允许发布 `rule+llm` 索引。
- 需要详细约束时读取 `references/llm-enrichment.md`。

## 测试集与候选集规则

- 主评测集只接受审核后的 query。
- `scripts/generate_eval_candidates_from_doc_diff.py` 和 `scripts/analyze_search_logs.py` 产物只能进入候选池。
- `scripts/validate_eval_set.py` 出现 `missing_path` 时发布必须 blocked。
- 候选集失败不阻塞发布，但必须记录。
- 已经用于调参的 blind 集降级为回归集，不再作为严格盲测。

## 严格 Blind 轮换

生成新的时间戳 blind 集：

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/generate_appdev_eval_batch3_blind.py \
  --strict-blind-out evals/eval_queries_user_appdev_blind_YYYYMMDD.jsonl \
  --strict-source strict-blind-YYYYMMDD
```

首跑后立即记录结果，作为严格 blind 首次基线。若后续根据该 blind 调整搜索规则或索引，它就只能作为回归集；下一次发布前需要生成新的时间戳 blind。

## 真实 Query 闭环

默认不写日志。需要收集本地搜索事件时：

```bash
DOC_SEARCH_LOG_PATH=/tmp/search-events.jsonl \
PYTHONDONTWRITEBYTECODE=1 python search_v3.py "WebView loadUrl headers 怎么传" --json --limit 5

PYTHONDONTWRITEBYTECODE=1 python scripts/record_search_feedback.py \
  --log /tmp/search-events.jsonl \
  --query "WebView loadUrl headers 怎么传" \
  --out /tmp/real_failed_queries.jsonl \
  --reason "top5_not_helpful"

PYTHONDONTWRITEBYTECODE=1 python scripts/analyze_search_logs.py \
  --log /tmp/search-events.jsonl \
  --feedback /tmp/real_failed_queries.jsonl \
  --output-dir /tmp/search-log-analysis
```

日志不得包含 API key、环境变量、用户工程代码或完整文档正文。

## 当前基线

已验证基线：

- 全量发布评估：7 套评测集，合计 814 条，`release status = pass`
- 全量评测：所有套件 `success@5 = 1.0`、`error_rate = 0.0`
- 健康检查：所有套件 `blocking = false`、`issue_counts = {}`
- 严格 blind：`evals/eval_queries_user_appdev_blind_20260424.jsonl`，80 条，首跑 `success@1 = 0.875`、`success@5 = 1.0`

## 参考资料

- 流程总览：`references/workflow-overview.md`
- 索引与卡片规则：`references/indexing-rules.md`
- LLM 补全约束：`references/llm-enrichment.md`
- 评测说明：`references/evaluation-guide.md`
- 故障排查：`references/troubleshooting.md`
