# fusion — 融合发布门禁

V3（card）+ graphify（graph）融合搜索的发布门禁分区。负责融合 AB 评测、发布评估流水线、评测集管理和搜索反馈收集。

## 目录结构

```
fusion/
├── evals/                    # 评测数据集（全部 9 个核心评测集）
│   ├── eval_queries_user.jsonl           # 用户模式评测（75 条）
│   ├── eval_queries_app_agent_dev.jsonl  # 应用开发评测（32 条）
│   ├── eval_queries_user_appdev.jsonl    # 用户+开发综合（255 条）
│   ├── eval_queries_user_appdev_next.jsonl    # 下一代（100 条）
│   ├── eval_queries_user_appdev_frozen.jsonl  # 冻结集（80 条）
│   ├── eval_queries_user_appdev_batch2.jsonl  # 批次2（64 条）
│   ├── eval_queries_user_appdev_batch3.jsonl  # 批次3（160 条）
│   ├── eval_queries_user_appdev_blind.jsonl   # 闭集评测（80 条）
│   ├── eval_queries_user_appdev_blind_20260424.jsonl # 严格闭集（80 条）
│   ├── eval_queries_real_session.jsonl   # 真实会话评测（15 条）
│   ├── eval_queries_paraphrase.jsonl     # 改写评测（20 条）
│   ├── eval_queries_composition.jsonl    # 组合评测（10 条）
│   ├── eval_queries.jsonl                # 基础评测（71 条）
│   ├── eval_queries_sampled.jsonl        # 采样评测（300 条）
│   └── eval_queries_full.jsonl           # 全量评测（93486 条）
├── records/                  # 评测结果基线
│   ├── baselines/            # 基线记录
│   └── run-history/          # 运行历史
├── references/               # 参考文档
└── scripts/                  # 维护和评测脚本
    ├── run_maintenance.py    # 融合全量维护流程
    ├── run_ab_eval.py        # V3/graphify/fusion AB 评测
    ├── run_release_eval.py   # 发布评估流水线
    ├── validate_eval_set.py  # 评测集一致性验证
    ├── regenerate_15k_independent_evals.py   # 重建独立评测集
    ├── generate_appdev_eval_batch3_blind.py  # 生成 AppDev 扩展和闭集评测
    ├── generate_eval_candidates_from_doc_diff.py # 从文档差异生成评测候选
    ├── analyze_search_logs.py  # 搜索日志分析
    └── record_search_feedback.py # 搜索反馈记录
```

## 融合评测原理

### AB 评测设计

AB 评测同时测试三个搜索引擎在同一评测集上的表现：

- **V3（card）** — 结构化搜索，精确但覆盖有限
- **graphify（graph）** — 图谱搜索，语义泛化能力强
- **fusion** — V3 + graph 合并去重，理论上应该 >= 两者

门禁要求：**fusion >= V3 且 fusion >= graphify**（在每个 split 上）

### 评测 Split

| Split | 条数 | 设计目的 |
|-------|------|----------|
| real_session | 15 | 来自真实用户会话的查询 |
| paraphrase | 20 | 同一意图的不同表述变体 |
| composition | 10 | 需要组合多个概念的查询 |

### 发布评估流水线

`run_release_eval.py` 执行完整的发布评估流程：

```
1. 文档指纹清单    build_doc_manifest.py → 当前文档指纹
2. 文档差异检测    diff_doc_manifest.py → 与上次发布的差异（可选）
3. 索引重建        build_index_v3.py → rule 模式重建（可选）
4. 评测集验证      validate_eval_set.py → 检查评测集完整性
5. 逐评测集评估    ab_test_openviking_vs_v3.py → 搜索评分
6. 失败分析        analyze_user_eval_failures.py → 归类失败原因
7. 门禁判定        success@5 >= threshold → pass/gray_release/blocked
```

### 发布门禁阈值

| 评测集 | 通过阈值 |
|--------|----------|
| eval_queries_user.jsonl | success@5 >= 0.98 |
| eval_queries_app_agent_dev.jsonl | success@5 >= 0.98 |
| eval_queries_user_appdev*.jsonl | success@5 >= 0.95 |
| eval_queries_user_appdev_blind_20260424.jsonl | success@5 >= 0.80 |

### 发布状态判定

- **pass** — 所有门禁通过
- **gray_release** — 门禁通过但 blind 评测 success@5 < 0.95
- **blocked** — 任一门禁失败或评测健康检查有 blocking 级问题

## 使用方法

### AB 评测

```bash
# 运行融合 AB 评测（默认使用 fusion/evals 中的 split）
python fusion/scripts/run_ab_eval.py --output ab_result.json

# 指定评测目录和 split
python fusion/scripts/run_ab_eval.py --eval-dir fusion/evals --splits real_session,composition
```

### 发布评估

```bash
# 完整发布评估流水线
python fusion/scripts/run_release_eval.py --output-dir /tmp/release-eval

# 重建索引后评估
python fusion/scripts/run_release_eval.py --output-dir /tmp/release-eval --rebuild-index
```

### 全量维护

```bash
# 融合全量维护（V3重建 + 图重建 + AB评测 + 种子同步）
python fusion/scripts/run_maintenance.py --mode rule+llm --publish-dir /tmp/publish
```

### 评测集管理

```bash
# 验证评测集完整性
python fusion/scripts/validate_eval_set.py --eval-set fusion/evals/eval_queries_user.jsonl

# 重建独立评测集（real_session/composition/paraphrase）
python fusion/scripts/regenerate_15k_independent_evals.py

# 生成 AppDev 扩展评测集
python fusion/scripts/generate_appdev_eval_batch3_blind.py

# 从文档差异生成评测候选
python fusion/scripts/generate_eval_candidates_from_doc_diff.py --old-manifest old.json --new-manifest new.json
```

### 搜索反馈

```bash
# 记录搜索反馈
python fusion/scripts/record_search_feedback.py --query "List性能" --result_paths "path1,path2" --hit true

# 分析搜索日志
python fusion/scripts/analyze_search_logs.py --log-dir /tmp/search-logs
```

## 评测结果参考

### AB 评测（15k 语料，limit=5）

| Split | V3 recall@5 | graphify recall@5 | fusion recall@5 | 门禁 |
|-------|------------|-------------------|----------------|------|
| real_session (15) | 0.67 | 0.40 | **0.73** | pass |
| paraphrase (20) | 0.65 | 0.55 | **0.75** | pass |
| composition (10) | 0.80 | 0.50 | **0.80** | pass |

fusion >= V3 和 fusion >= graphify 在 real_session 和 composition split 上通过。