# card — 卡片索引构建与评测

V3 结构化索引的构建、评测和维护分区。负责从原始文档语料构建 SQLite 搜索索引，通过评测验证索引质量，以及管理卡片相关的回归门禁。

## 目录结构

```
card/
├── builder/                  # 索引构建器
│   ├── build_index_v3.py     # V3 索引构建主脚本（rule/rule+llm 两种模式）
│   └── high_value_tasks_ext.py # 高价值任务卡片扩展定义
├── evals/                    # 评测数据集
│   ├── content-basic.jsonl   # 内容基础评测（2 条）
│   └── discovery.jsonl       # 发现能力评测（2 条）
├── records/                  # 评测结果和历史
│   ├── ab-15k-baseline.json  # AB 评测基线结果
│   ├── ab-15k-after-rule-llm.json # rule+llm 后的 AB 结果
│   ├── ab-15k-after-expansion.json # 语料扩充后的 AB 结果
│   ├── v3-regression-gate-15k-post-rule-llm.json # V3 回归门结果
│   ├── docs_manifest_15k.json # 文档指纹清单
│   ├── v3_seeds_15k.json / v3_seeds_15k_post_llm.json # 种子定义
│   ├── baselines/            # 历史基线
│   └── run-history/          # 运行历史
├── references/               # 参考文档
│   ├── workflow-overview.md  # 工作流程概述
│   ├── indexing-rules.md     # 索引规则说明
│   ├── llm-enrichment.md     # LLM 扩充说明
│   ├── troubleshooting.md   # 排障指南
│   └── evaluation-guide.md   # 评测门禁指南
└── scripts/                  # 维护和评测脚本
    ├── run_maintenance.py    # 全量维护流程（重建+评测+归档）
    ├── run_ab_eval.py        # V3/graphify/fusion AB 评测
    ├── eval_bench.py         # 评测基准脚本
    ├── run_semantic_capability_gate.py # 融合语义能力门禁
    ├── run_v3_regression_gate.py # V3 自举回归门禁
    ├── sync_v3_to_graph.py   # V3→graph 种子同步
    ├── run_corpus_expansion.py # 语料扩充流程
    ├── audit_api_coverage.py # API 覆盖审计
    ├── audit_coverage.py     # 通用覆盖审计
    ├── build_doc_manifest.py # 文档指纹清单生成
    ├── diff_doc_manifest.py  # 文档指纹对比
    ├── enrich_existing_index_appdev.py # 增量 AppDev 扩充
    ├── analyze_user_eval_failures.py # 评测失败分析
    ├── repair_llm_failure_cache.py # LLM 失败缓存修复
    └── load_env.sh           # 环境变量加载脚本
```

## 索引构建原理

### V3 索引模型

V3 将文档组织为四种卡片类型：

| 卡片类型 | 来源 | 说明 |
|----------|------|------|
| **task** | 硬编码 + LLM 生成 | 开发任务卡片（"如何做X"），约 100 个规则生成 |
| **api** | 硬编码高频 + LLM 扩充 | API 参考卡片，rule 模式约 40 个，rule+llm 约 4635 个 |
| **example** | LLM 生成 | 代码示例卡片 |
| **doc** | LLM 生成 | 通用文档卡片 |

### 两种构建模式

| 模式 | 说明 | 产出 | 耗时 |
|------|------|------|------|
| **rule** | 仅基于硬编码规则（HIGH_VALUE_TASKS + HIGH_VALUE_API_MAP） | ~40 API + 100 task | 数秒 |
| **rule+llm** | rule 基础 + LLM API 扩充（需要 OPENAI_API_KEY） | ~4635 API + 14824 doc | 数小时 |

### 构建流程

```
1. 文档发现     detect docs/ → 收集所有 Markdown 文件
2. 规则生成     HIGH_VALUE_TASKS/API_MAP → 基础卡片
3. LLM 扩充    调用 LLM API → 生成更多 API/example/doc 卡片（可选）
4. 别名生成    从卡片标题/关键词 → aliases.json
5. SQLite 构建  卡片数据 → search.db（FTS5 全文索引）
6. JSONL 输出   卡片数据 → tasks/apis/examples/docs.jsonl
```

## 使用方法

### 索引构建

```bash
# 规则模式（快速，不需要 LLM API）
python card/builder/build_index_v3.py --mode rule --index-dir doc-card/index

# rule+llm 模式（完整，需要 OPENAI_API_KEY）
python card/builder/build_index_v3.py --mode rule+llm --index-dir doc-card/index
```

### AB 评测

```bash
# 运行 V3/graphify/fusion 三引擎 AB 评测
python card/scripts/run_ab_eval.py --eval-dir fusion/evals --output ab_result.json

# 指定评测 split
python card/scripts/run_ab_eval.py --eval-dir fusion/evals --splits real_session,composition
```

### V3 回归门禁

```bash
# 自举回归测试（仅 V3 本地搜索）
python card/scripts/run_v3_regression_gate.py --index-dir doc-card/index --output-dir /tmp/v3-gate
```

### 全量维护

```bash
# 全量重建 + 评测 + 归档
python card/scripts/run_maintenance.py --mode rule+llm --publish-dir /tmp/publish

# 仅规则模式（快速验证）
python card/scripts/run_maintenance.py --mode rule --publish-dir /tmp/publish
```

### 种子同步

```bash
# 将 V3 高价值卡片同步到图谱种子节点
python card/scripts/sync_v3_to_graph.py --validate

# 仅同步（不验证）
python card/scripts/sync_v3_to_graph.py
```

### 覆盖审计

```bash
# API 覆盖审计
python card/scripts/audit_api_coverage.py --index-dir doc-card/index

# 通用覆盖审计
python card/scripts/audit_coverage.py --index-dir doc-card/index
```

## 评测结果参考

### AB 评测基线（15k 语料，limit=5）

| Split | V3 recall@5 | graphify recall@5 | fusion recall@5 |
|-------|------------|-------------------|----------------|
| real_session (15) | 0.67 | 0.40 | **0.80** |
| paraphrase (20) | 0.65 | 0.55 | **0.75** |
| composition (10) | 0.80 | 0.60 | **0.80** |

### 三引擎对比（192 条，limit=5）

card Recall@5 = 34.9%（结构化搜索覆盖有限）