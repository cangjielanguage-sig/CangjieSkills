# 索引与卡片规则

`build_index_v3.py` 支持两种模式：

- `rule`
- `rule+llm`

共同约束：

- 运行时检索不调用 LLM
- 结构化产物统一落在 `index/` 风格目录中
- 产物至少包含：
  - `manifest.json`
  - `tasks.jsonl`
  - `apis.jsonl`
  - `examples.jsonl`
  - `docs.jsonl`
  - `aliases.json`
  - `search.db`

卡片分层：

- `task card`
- `api card`
- `example card`
- `doc card`

`rule` 负责：

- 路径
- 标题
- 文档类型提示
- 候选归类
- 基础索引落库

`rule+llm` 负责：

- `summary`
- `user_queries`
- `semantic_aliases`
- `intent_types`
- `primary_objects`
- `when_to_use`
- `when_not_to_use`
- `problem_signals`
- `tags`
- `needs_review`
- `confidence`

禁止项：

- 运行时查询依赖 LLM
- 在没有证据的情况下编造 API 或场景
- 修改卡片主键
- 覆盖 API/doc 的原始标题、方法名、签名、`source_paths` 等身份字段

评测产物：

- 每次构建会生成 `evals/search/eval_queries_full.jsonl`
- 每张 `task/api/example/doc` 至少生成多类 query
- 分类至少包含 `exact / natural / semi-structured / error-driven / exploration`
