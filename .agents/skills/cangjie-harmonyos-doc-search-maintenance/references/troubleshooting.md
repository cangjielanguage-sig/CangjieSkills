# 常见问题排查

## release status 是 blocked

优先看 `release-summary.json` 中每个 eval set 的 `reasons`。

- `eval_health_blocking`：读取对应 `eval-health.json`，通常是 `missing_path`。
- `success@5_below_*`：读取对应 `failure-summary.json` 和 `details.jsonl`。
- `error_rate_non_zero`：先定位搜索执行异常，不要调评测标注。

## 健康检查出现 missing_path

这通常说明文档路径变化或索引未覆盖旧路径。

处理顺序：

1. 用 `doc_diff.json` 确认路径是否被删除、移动或改名。
2. 用新索引确认是否存在等价新路径。
3. 如果文档确实迁移，更新评测集 `acceptable_paths`。
4. 如果文档仍存在但索引缺失，先修索引构建。

`missing_path` 是阻塞级问题，不允许忽略后发布。

## success@5 下降

优先区分三类原因：

- 文档/路径变化导致可接受路径失效。
- 索引或卡片重建导致候选召回下降。
- 搜索重排或 query understanding 规则退化。

排查文件：

- `failure-summary.json`
- `details.jsonl`
- `eval-health.json`
- `index/manifest.json`

## 候选 query 很多但质量不稳定

`scripts/generate_eval_candidates_from_doc_diff.py` 和 `scripts/analyze_search_logs.py` 只产出候选池。进入主门禁前必须审核：

- query 是否像真实用户问题。
- 是否包含路径残片、内部模板词或自动生成味。
- `acceptable_paths` 是否足够宽但不失真。
- `must_contain` 是否必要。

## strict blind 首跑不理想

不要立刻调参污染 blind。

先判断：

- 是否是候选生成质量问题。
- 是否存在明显错误标注。
- 是否暴露真实能力缺口。

如果基于该 blind 调整了搜索或索引，它就降级为回归集。下一次发布前需要重新生成新的时间戳 blind。

## rule+llm 直接失败

检查：

- `OPENAI_BASE_URL`
- `OPENAI_API_KEY`
- `OPENAI_MODEL`
- 网络是否允许访问 OpenAI 兼容接口

建议使用 `--llm-cache-dir`，中断后复跑可以复用已成功卡片。

## search_v3.py 提示索引不完整

确认索引目录存在：

- `manifest.json`
- `tasks.jsonl`
- `apis.jsonl`
- `examples.jsonl`
- `docs.jsonl`
- `aliases.json`
- `search.db`
