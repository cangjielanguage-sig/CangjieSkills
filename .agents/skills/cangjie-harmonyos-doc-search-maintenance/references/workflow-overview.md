# doc-search 维护流程总览

本流程服务于 `cangjie-harmonyos-doc-search` 的持续维护。目标是让文档路径或内容变化后，可以可重复地完成索引重建、候选素材生成、评测健康检查和发布判断。

## 核心链路

1. 生成当前文档 manifest：记录每个文档的路径、标题、大小和 sha256。
2. 对比新旧 manifest：识别新增、删除、变更和疑似重命名文档。
3. 重建索引/卡片：使用 `build_index_v3.py --mode rule` 或 `--mode rule+llm`。
4. 生成候选 query：基于 `doc_diff.json` 或真实搜索日志生成候选池。
5. 校验评测集健康：检查路径是否失效、query 是否重复、覆盖分布是否异常。
6. 运行发布评估：执行本地 V3 评测和失败分析。
7. 输出发布结论：只能是 `pass`、`gray_release` 或 `blocked`。

## 主要脚本

- `scripts/build_doc_manifest.py`：输入文档目录，输出 `doc_manifest_current.json`。
- `scripts/diff_doc_manifest.py`：输入旧/新 manifest，输出 `doc_diff.json`。
- `build_index_v3.py`：输入文档目录，输出 `tasks/apis/examples/docs/aliases/search.db/manifest`。
- `scripts/generate_eval_candidates_from_doc_diff.py`：输入文档 diff 和索引，输出候选评测 JSONL。
- `../cangjie-harmonyos-doc-search-maintenance/scripts/validate_eval_set.py`：输入评测集、索引和 manifest，输出 `eval-health.json`。
- `scripts/run_release_eval.py`：输入索引和评测集，输出 release 报告。
- `scripts/generate_appdev_eval_batch3_blind.py --strict-blind-out`：生成时间戳严格 blind 集。

## 发布规则

- 主评测集有 `missing_path`：发布 blocked。
- 主评测集 `error_rate > 0`：发布 blocked。
- 主评测集未达到 success@5 阈值：发布 blocked 或 gray_release，按 `scripts/run_release_eval.py` 结果判断。
- 候选集失败只记录，不阻塞发布。
- 新 strict blind 首跑结果应归档为基线；后续调参后该 blind 降级为回归集。

## LLM 与旧维护脚本

`scripts/run_maintenance.py` 是历史 rule/rule+llm/OpenViking AB 流程入口，可用于需要同时沉淀旧 baselines/run-history 的场景。当前发布判断优先使用 `cangjie-harmonyos-doc-search-maintenance/scripts/run_release_eval.py`。
