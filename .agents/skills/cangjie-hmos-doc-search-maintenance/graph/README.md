# graph — 知识图谱构建与评测

文档知识图谱的构建、评测和维护分区。负责从 Markdown 文件提取语义节点和边、构建 NetworkX 图、通过 LLM 增强关键词、以及三引擎对比评测。

## 目录结构

```
graph/
├── builder/                  # 图谱构建器
│   ├── build_cli.py          # 构建命令行入口（build-doc/build-code/merge/enhance/build）
│   ├── builders/             # 通用构建工具
│   │   ├── build.py          # 图操作（构建/合并/保存/去重/标注）
│   │   ├── cache.py          # SHA 内容缓存
│   │   ├── cluster.py        # 社区检测（NetworkX 聚类）
│   │   ├── detect.py         # 文件发现和类型分类
│   │   └── validate.py       # 提取结果验证
│   ├── doc/                  # 文档图提取和构建
│   │   ├── extractor.py      # 文档节点提取器（1文件=1节点）
│   │   └── builder.py        # 文档图构建器（NetworkX）
│   ├── code/                 # 代码图提取和构建
│   │   ├── extractor.py      # 代码节点提取器（tree-sitter AST）
│   │   └── builder.py        # 代码图构建器
│   └── llm/                  # LLM 语义增强
│   │   ├── enhancer.py       # LLM 关键词增强器
│   │   └── pipeline.py       # LLM 增强流水线（并发处理）
├── evals/                    # 评测数据和脚本
│   ├── run_eval.py           # 三引擎对比评测（card/graph/fusion）
│   ├── datasets/             # 评测数据集
│   │   ├── eval_queries_comprehensive_deduped.jsonl # 192 条去重评测集
│   │   ├── eval_queries_comprehensive.jsonl # 228 条完整评测集
│   │   ├── eval_config.json  # 评测配置
│   │   └── README.md / DESIGN_SPEC.md # 设计文档
│   ├── keywords_v7_prompt.json # 关键词提取 prompt
│   ├── comparison_report.md  # 对比评测报告
│   ├── eval_report.md        # 评测报告
│   ├── TEST_GUIDE.md         # 测试指南
│   └── *.py                  # 辅助分析脚本（check_data/classify_miss_types 等）
├── records/                  # 评测结果
│   ├── docs_statistics.json  # 文档语料统计
│   ├── baselines/            # 历史基线
│   └── run-history/          # 运行历史
├── references/               # 参考文档
│   ├── ARCHITECTURE.md       # 图系统架构说明
│   └── BUILD_GUIDE.md        # 构建指南
└── scripts/                  # 入口脚本
    ├── build_doc_graph.py    # 文档图构建入口
    ├── build_code_graph.py   # 代码图构建入口
    ├── validate_graph_data.py # 图数据验证
    ├── docs_statistics.py    # 语料统计
    └── run_graph_release_eval.py # 图谱发布评测入口
```

## 图谱构建原理

### 文档图构建流程

```
1. 文件发现      detect(docs/) → 收集所有 .md 文件
2. 节点提取      extract_doc_node() → 每个文件生成一个 DocNode
   - 双语标签（label_zh/label_en）
   - 双语关键词（keywords_zh/keywords_en）
   - 层级推断（concept/howto/reference/example）
   - 社区推断（从 category 字段）
   - 命名空间构建（从目录结构）
3. 边提取        文件间关系 → Edge（contains/depends_on/related_to）
4. 图构建        build_doc_nx_graph() → NetworkX DiGraph
5. 社区聚类      cluster() → NetworkX community detection
6. LLM 增强      enhance() → LLM 补充关键词（可选）
7. 导出保存      save_graph() → graph.json
```

### 节点 ID 格式

节点 ID = 文件的相对路径（不含顶层目录），如 `cj-scroll-swipe-list/List/.overview.md`

### 边关系类型

| 关系 | 说明 | 来源 |
|------|------|------|
| `contains` | 包含关系（目录→子文件） | 目录结构推断 |
| `depends_on` | 依赖关系 | 目录结构推断 |
| `related_to` | 语义关联 | 目录同级推断 |
| `llm_semantic_*` | LLM 语义关系 | LLM 增强生成 |

### 自动检测 docs 子目录

当 `docs/` 目录没有顶层 .md 文件且只有一个包含 .md 的子目录时，自动使用该子目录作为 `root_dir`，确保节点 ID 格式与原始图谱一致。

## 使用方法

### 图谱构建

```bash
# 构建文档图（最常用）
python graph/builder/build_cli.py build-doc --docs-dir docs/harmonyos-6.0.2-15k --output doc-graph/data/doc/graph.json

# 快捷脚本
python graph/scripts/build_doc_graph.py

# 构建代码图
python graph/scripts/build_code_graph.py

# 全量构建（doc + code + merge + enhance）
python graph/builder/build_cli.py build --docs-dir docs/harmonyos-6.0.2-15k
```

### LLM 增强

```bash
# 增强已有图谱的关键词
python graph/builder/build_cli.py enhance-graph --graph-dir doc-graph/data --docs-dir docs/harmonyos-6.0.2-15k

# 需要设置环境变量
export DASHSCOPE_API_KEY=...
export DASHSCOPE_API_BASE=...
export DASHSCOPE_MODEL=qwen3.6-plus  # 可选，默认 qwen3.6-plus
```

### 图数据验证

```bash
# 验证 graph.json 的完整性
python graph/scripts/validate_graph_data.py
```

### 语料统计

```bash
# 统计文档语料的字数分布
python graph/scripts/docs_statistics.py
```

### 三引擎对比评测

```bash
# 运行 card/graph/fusion 三引擎对比
python graph/scripts/run_graph_release_eval.py --output report.md

# 只测前 50 条
python graph/scripts/run_graph_release_eval.py --limit 50
```

## 评测结果参考

### 三引擎对比（192 条评测集）

| 指标 | card | graph | fusion |
|------|-----:|------:|-------:|
| Recall@5 | 34.9% | **97.4%** | 90.6% |
| MRR | 0.133 | **0.700** | 0.696 |
| Avg latency | 149.3ms | **2.9ms** | 165.7ms |
| FULL hits | 67 | 178 | 165 |
| MISS | 125 | 5 | 18 |

Graph 搜索质量远超 card（97.4% vs 34.9%），延迟极低（2.9ms vs 149.3ms）。