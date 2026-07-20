# 知识图谱评测指南

## 评测工具概览

| 脚本 | 用途 | 运行方式 |
|------|------|----------|
| `run_eval.py` | 主评测脚本（分类加权 + OR+累加双策略） | `python eval/run_eval.py` |
| `analyze_miss_detail.py` | MISS 查询逐条诊断（关键词、Top5 结果、期望路径） | `python eval/analyze_miss_detail.py` |
| `classify_miss_types.py` | MISS 类型分类（more_specific/sibling/partial/wrong） | `python eval/classify_miss_types.py` |
| `validate_keywords.py` | 关键词质量校验（泛化词、跨生态词、空核心词） | `python eval/validate_keywords.py` |

## 数据文件

| 文件 | 说明 |
|------|------|
| `datasets/eval_queries_comprehensive_deduped.jsonl` | 评测数据集（192 条查询，每条含 query/intent/category/acceptable_paths） |
| `keywords_v5_deduped.json` | 分类关键词映射（192 条，core/context/synonym 各含 en/zh） |

## 快速开始

### 1. 评测当前图谱

```bash
# 默认评测 data/doc/graph.json（分类加权搜索 + OR+累加搜索）
python eval/run_eval.py

# 指定图路径
python eval/run_eval.py --graph data/merged/graph.json --graph-dir data/merged

# 只跑一种搜索方法
python eval/run_eval.py --method categorized
python eval/run_eval.py --method or
```

输出：
- 控制台：FULL/PARTIAL/MISS 数量、Recall@5、各类别 R@5
- 文件：`eval/eval_report.md`（含详细分类数据 + MISS 详情）

### 2. 对比两个图谱版本

```bash
# 对比 LLM 增强前后
python eval/run_eval.py --before data/before_llm/graph.json --before-dir data/before_llm
```

报告会额外包含「增强前 vs 增强后」对比表。

### 3. MISS 查询诊断

```bash
# 逐条分析 MISS 查询（关键词配置 + Top5 结果 + 期望路径 + 对比分析）
python eval/analyze_miss_detail.py
```

输出：`eval/miss_analysis_detailed.md`

### 4. MISS 类型分类

```bash
# 将 MISS 分为 more_specific/sibling/same_namespace/partial/wrong 五类
python eval/classify_miss_types.py
```

输出：`eval/miss_type_classification.md`（含各类 MISS 数量 + 改进建议）

### 5. 关键词质量校验

```bash
# 检查关键词中是否有泛化词、跨生态词在 core、空 core 等问题
python eval/validate_keywords.py
```

输出：控制台（关键词频率统计 + 问题列表）

---

## 修改图谱后重新评测

当你修改了图谱（如重新 build、LLM 增强、调整提取逻辑）后：

```bash
# Step 1: 重新构建图谱
python cli.py build docs/ --enhance -o data/doc/graph.json

# Step 2: 运行评测
python eval/run_eval.py

# Step 3: 如果有 MISS，诊断原因
python eval/analyze_miss_detail.py
```

## 修改评测集后重新评测

当你修改了评测数据集或关键词后：

### 修改 acceptable_paths

评测数据集每条查询的 `acceptable_paths` 定义了命中标准。命中判定规则：返回结果的 `source_file` 与 `acceptable_paths` 中任一条**子串匹配**即算命中。

**设计原则**：
- 概览/指南级查询：`acceptable_paths` 应包含 overview 文档路径，**不仅限于 class_XXX**
- 具体 API 查询：同时包含具体 API 页面和所属模块 overview
- 对比/跨生态查询：包含两端的 overview 页面

```bash
# 修改数据集后直接评测
python eval/run_eval.py
```

### 修改关键词映射

关键词文件 `keywords_v5_deduped.json` 每条格式：

```json
{
  "1": {
    "query": "HttpRequest的timeout参数怎么设置",
    "intent": "HTTP超时配置",
    "category": "api_lookup",
    "core": {"zh": ["HTTP请求"], "en": ["HttpRequest"]},
    "context": {"zh": ["超时", "参数设置"], "en": ["timeout", "configuration"]},
    "synonym": {"zh": [], "en": []}
  }
}
```

修改后运行评测验证效果：

```bash
python eval/run_eval.py
```

---

## 命中判定规则

| 状态 | 定义 |
|------|------|
| **FULL** | 直接命中（Top5 的 direct_hits 中包含 acceptable_paths 任一条） |
| **PARTIAL** | 关联命中（related_hits 中包含，但 direct_hits 中不含） |
| **MISS** | 均未命中 |

匹配方式：`result_path == acceptable_path` 或 `acceptable_path in result_path` 或 `result_path in acceptable_path`（子串双向匹配）

---

## 评测报告格式

`eval/eval_report.md` 包含：

1. **总体指标**：FULL/PARTIAL/MISS 数量与比例、Recall@5、平均延迟
2. **各类别表现**：api_lookup/enumeration/reverse_lookup/semantic_fuzzy/comparison/cross_ecosystem/composition/constrained/performance_boundary/how_to/workflow 各类 R@5
3. **MISS 详情**：每条 MISS 查询的 ID、类别、查询内容、Top1 结果
4. **策略对比**（如果用 `--method both`）：分类加权 vs OR+累加的 R@5 和延迟对比