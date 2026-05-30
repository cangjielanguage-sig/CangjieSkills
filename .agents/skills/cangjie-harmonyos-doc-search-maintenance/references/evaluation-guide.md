# 发布评测说明

当前发布评测以本地 V3 为准，不默认触发远端 OpenViking AB。

## 默认评测集

- `evals/search/eval_queries_user.jsonl`
- `evals/search/eval_queries_app_agent_dev.jsonl`
- `evals/search/eval_queries_user_appdev.jsonl`
- `evals/search/eval_queries_user_appdev_next.jsonl`
- `evals/search/eval_queries_user_appdev_frozen.jsonl`
- `evals/search/eval_queries_user_appdev_batch2.jsonl`
- `evals/search/eval_queries_user_appdev_batch3.jsonl`
- `evals/search/eval_queries_user_appdev_blind.jsonl`

可额外传入新的严格 blind，例如 `evals/search/eval_queries_user_appdev_blind_20260424.jsonl`。

## 核心指标

- `success@1`：Top1 命中率。
- `success@5`：Top5 命中率，是当前主门禁指标。
- `success@10`：Top10 命中率。
- `mrr`：命中排序质量。
- `error_rate`：评测执行错误率。
- `latency_p50_ms / latency_p95_ms`：本地检索延迟。

## 门禁

- `evals/search/eval_queries_user.jsonl`：`success@5 >= 0.98` 且 `error_rate = 0`。
- `evals/search/eval_queries_app_agent_dev.jsonl`：`success@5 >= 0.98` 且 `error_rate = 0`。
- `evals/search/eval_queries_user_appdev*.jsonl`：`success@5 >= 0.95` 且 `error_rate = 0`。
- 严格新 blind：`success@5 >= 0.80` 且 `error_rate = 0`。
- 健康检查有阻塞级 `missing_path`：直接 blocked。

## 输出物

`scripts/run_release_eval.py` 输出：

- `release-summary.json`：机器可读发布结论。
- `release-report.md`：人类可读报告。
- `eval-health-summary.json`：各评测集健康检查汇总。
- 每套评测目录下的 `summary.json / details.jsonl / failure-summary.json / eval-health.json`。

## 失败分析

若有失败，读取对应目录的 `failure-summary.json`。优先区分：

- 搜索未返回可接受路径。
- 可接受路径命中但 `must_contain` 未满足。
- 评测标注路径失效。
- query 本身不符合用户态表达。
