# rule+llm 补全约束

`rule+llm` 使用 OpenAI 兼容 API 在离线构建阶段补全卡片语义字段。用户查询运行时只读取本地索引，不调用外部 LLM。

## 环境变量

必填：

- `OPENAI_BASE_URL`
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

推荐：

- `OPENAI_TEMPERATURE=0`
- `OPENAI_TIMEOUT=60`
- `OPENAI_MAX_RETRIES=1` 到 `3`

## 推荐命令

```bash
OPENAI_BASE_URL="..." \
OPENAI_API_KEY="..." \
OPENAI_MODEL="..." \
OPENAI_TEMPERATURE="0" \
PYTHONDONTWRITEBYTECODE=1 python .agents/skills/cangjie-hmos-doc-search-maintenance/builder/build_index_v3.py \
  --mode rule+llm \
  --index-dir /tmp/cangjie-index-llm \
  --llm-card-types task,api,example,doc \
  --llm-concurrency 24 \
  --llm-cache-dir /tmp/cangjie-llm-cache
```

## 补全原则

- 只能基于给定 evidence 摘取和归纳。
- 不允许臆造不存在的 API、路径、约束或示例。
- 不允许修改身份字段，例如 `source_paths`、原始标题、方法名、签名、card id。
- 证据不足时保守输出，并标记 `needs_review=true`。
- 输出必须是结构化 JSON。
- 推荐使用缓存，避免文档未变时重复消耗 token。

## 发布门禁

- 先写临时索引目录，不直接覆盖默认 `index/`。
- `manifest.llm.failed` 必须为 `0`。
- 选择增强的 card type 必须完成对应全量增强。
- 必须使用 `scripts/run_release_eval.py --index-dir 临时索引目录` 通过发布评估。
- 通过后才允许人工决定是否替换正式 `index/`。
