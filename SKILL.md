---
description: >
  CangjieSkills 是仓颉 HarmonyOS 应用开发的文档搜索引擎工具集。
  提供 card（结构化卡片检索）、graph（知识图谱语义检索）、fusion（双引擎融合）三种搜索引擎，
  支持 graph/card 的 LLM 全量节点增强与索引重建、192 条三引擎对比评测、噪声关键词过滤。
  当需要搜索仓颉/HarmonyOS API 文档、构建/重建搜索索引、增强图谱中文关键词、
  运行三引擎评测对比召回率、诊断搜索 MISS 原因、或配置 LLM API 端点时使用此 SKILL。
---

# CangjieSkills

> 仓颉 HarmonyOS 文档搜索引擎 — 构建 / 增强 / 搜索 / 评测 全流程工具集

## 项目概述

CangjieSkills 为仓颉 HarmonyOS 开发者提供**三种互补的文档搜索引擎**：

| 引擎 | 索引 | 搜索方式 | 返回内容 | 适用场景 |
|------|------|---------|---------|---------|
| **card** | SQLite FTS5 + JSONL（任务卡/API卡/示例卡/文档卡） | FTS5 BM25 + query_understanding + rerank | 任务卡（含推荐API+示例） | 精确 API/组件查询（"Router.pushUrl 参数"） |
| **graph** | 内存倒排索引（知识图谱节点+边） | 5-tier additive scoring × layer权重 | 文档路径列表 | 语义/自然语言搜索（"要实现懒加载用什么方案"） |
| **fusion** | card + graph 运行时编排 | fuse_results 融合排序 | 双引擎合并结果 | 综合查询（自动组合两者优势） |

**当前基线**（192 条评测，新语料文档，2026-07-03）：

| 引擎 | Recall@5 | MRR |
|------|:---:|:---:|
| card | 83.3% | 0.545 |
| graph | 97.9% | 0.820 |
| fusion | 95.8% | 0.814 |

## 目录结构速查

| 用途 | 路径 |
|------|------|
| **graph 图谱数据** | `.agents/skills/cangjie-hmos-doc-search/doc-graph/data/doc/graph.json` |
| **card 索引目录** | `.agents/skills/cangjie-hmos-doc-search/doc-card/index/` |
| graph 搜索 CLI | `.agents/skills/cangjie-hmos-doc-search/doc-graph/cli.py` |
| card 搜索 CLI | `.agents/skills/cangjie-hmos-doc-search/doc-card/search_v3.py` |
| fusion 搜索 CLI | `.agents/skills/cangjie-hmos-doc-search/unified_search.py` |
| graph 构建入口 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/builder/build_cli.py` |
| card 构建入口 | `.agents/skills/cangjie-hmos-doc-search-maintenance/card/builder/build_index_v3.py` |
| graph 评测脚本 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/evals/run_eval.py` |
| 评测数据集 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/evals/datasets/eval_queries_comprehensive_deduped.jsonl` |
| 关键词映射 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/evals/keywords_v7_prompt.json` |
| 源文档语料 | `.agents/skills/cangjie-hmos-doc-search/docs/harmonyos-6.0.2-15k/` |

## 环境变量

> ⚠️ **agent 执行规则**：在执行任何涉及 LLM API 调用的命令之前，**必须先向用户确认**以下三项，不可跳过：
>
> 1. 使用哪个模型端点（DeepSeek 官方 / GLM-5.2 自建 / 其他）
> 2. API Key 是什么
> 3. 并发数（推荐 DeepSeek 5、GLM-5.2 2-3）
>
> 确认后按下方表格设置对应的环境变量前缀。

### 各组件对应变量

| 组件 | 变量前缀 | 涉及命令 |
|------|---------|------|
| **graph enhance** | `DASHSCOPE_*` | `build_cli.py enhance-graph` |
| **card llm build** | `OPENAI_*` | `build_index_v3.py --mode rule+llm` |
| **全局必须** | `PYTHONIOENCODING=utf-8` | 所有 Python 命令（Windows 下中文输出必须） |

### 常用端点配置

| 端点 | API_BASE | 需设变量 | 并发建议 |
|------|---------|---------|:---:|
| DeepSeek 官方 | `https://api.deepseek.com/v1` | `API_BASE` / `API_KEY` / `MODEL="deepseek v4 pro"` | 5 |
| GLM-5.2 自建 | `http://113.46.219.251:8080/v1` | `API_BASE` / `API_KEY` / `MODEL="GLM-5.2"` | 2-3 |

### agent 确认对话模板

> 我将执行 **[graph enhance / card llm rebuild]**，需要调用 LLM API。
> 请确认：① 使用哪个端点？ ② API Key？ ③ 并发数？

### Graph enhance 完整示例

```powershell
$env:DASHSCOPE_API_KEY="sk-xxx"
$env:DASHSCOPE_API_BASE="https://api.deepseek.com/v1"
$env:DASHSCOPE_MODEL="deepseek-chat"
$env:PYTHONIOENCODING="utf-8"

cd .agents\skills\cangjie-hmos-doc-search-maintenance\graph\builder
python build_cli.py enhance-graph `
  --graph-dir "D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search\doc-graph\data" `
  --docs-dir  "D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search\docs\harmonyos-6.0.2-15k" `
  --max-workers 5
```

### Card llm build 完整示例

```powershell
$env:OPENAI_API_KEY="sk-xxx"
$env:OPENAI_BASE_URL="https://api.deepseek.com/v1"
$env:OPENAI_MODEL="deepseek-chat"
$env:PYTHONIOENCODING="utf-8"

cd .agents\skills\cangjie-hmos-doc-search-maintenance\card
python builder/build_index_v3.py --mode rule+llm `
  --docs-dir "D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search\docs" `
  --index-dir "<output_dir>" `
  --llm-card-types task,api,example,doc `
  --llm-concurrency 5
```

## Graph 构建 + LLM 节点增强

### 全量构建（build-doc → enhance-graph → post-filter 一键）

```powershell
cd .agents\skills\cangjie-hmos-doc-search-maintenance\graph\builder

# 仅构建图谱（不含增强）
python build_cli.py build-doc --docs-dir <path> --no-use-cache

# 仅增强已有图谱
python build_cli.py enhance-graph `
  --graph-dir <path_to_doc-graph/data> `
  --docs-dir <path_to_docs> `
  --max-workers 5

# 一键全流程（build-doc → enhance-graph → post-filter）
python build_cli.py build --docs-dir <path> --enhance --max-workers 5
```

### 参数

| 参数 | 说明 | 默认值 |
|------|------|:---:|
| `--docs-dir` | 文档语料目录 | 必填 |
| `--enhance` | 同时执行 LLM 增强 | 否 |
| `--max-workers` | 并发线程数 | 5 |
| `--no-use-cache` | 强制重建（改 extractor 后必须） | — |
| `--batch-limit N` | 限制增强批次数（测试用） | 无限制 |

### 验收标准

| 指标 | 目标 |
|------|:---:|
| nodes | ~3,700 |
| llm_enhanced | >95% |
| en_only | <5% |
| noise_en / noise_zh | 0 |
| 熔断 | 连续 50 批失败自动停止 |

### 注意事项

- **改 `extractor.py` 后**：必须清缓存（`docs/.../graphify-out/cache/`）或加 `--no-use-cache`，否则改动不生效
- **graph.json 格式**：`indent=2`，可直接用编辑器打开浏览
- **LLM 增强耗时**：约 1,000 文档/分钟（deepseek-chat 并发 5），~3,700 节点约 4-5 分钟

## Card 构建 + LLM 增强

### 构建命令

```powershell
cd .agents\skills\cangjie-hmos-doc-search-maintenance\card

# rule 模式（无 LLM，快速验证）
python builder/build_index_v3.py --mode rule `
  --docs-dir "D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search\docs" `
  --index-dir "<output_dir>"

# rule+llm 模式（需先确认 LLM 配置，见环境变量段）
python builder/build_index_v3.py --mode rule+llm `
  --docs-dir "D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search\docs" `
  --index-dir "<output_dir>" `
  --llm-card-types task,api,example,doc `
  --llm-concurrency 5 `
  --llm-cache-dir records/llm-cache
```

### 发布到生产

```powershell
Copy-Item -Recurse -Force <output_dir>\* `
  .agents\skills\cangjie-hmos-doc-search\doc-card\index\
```

### 验收标准

| 指标 | 新语料目标 |
|------|:---:|
| 总卡片数 | ~6,000 |
| llm_enriched | >95% |
| 构建耗时（rule+llm） | ~1h（deepseek-chat 并发 5） |
| 构建耗时（rule only） | ~5s |

### 注意事项

- Card builder 跳过 `.abstract.md` 文件（`discover_docs()` 已内置过滤）
- task 卡片的 `source_paths` 不再按字母排序，保留 `prefer_primary_doc` 自然序

## 搜索

### Graph 搜索（关键词/自然语言）

```powershell
cd .agents\skills\cangjie-hmos-doc-search\doc-graph
$env:PYTHONIOENCODING="utf-8"

cd D:\ZSY\CangjieSkills
# 关键词拼接并返回搜索词
python -c "
import json
with open(r'D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search-maintenance\graph\evals\keywords_v7_prompt.json', encoding='utf-8') as f:
    kw = json.load(f)
k = kw['6']  # 数字为评测数据集中的查询索引
print('en:', k['keywords_en'])
print('zh:', k['keywords_zh'])
print('search_q:', ' '.join(k['keywords_en'] + k['keywords_zh']))
"

# 基本搜索
python cli.py search "List 组件" --graph doc -k 5

# 查看节点详情
python cli.py explain "LazyForEach"

# 查看邻居
python cli.py neighbors "List" --limit 10

# 图谱统计
python cli.py stats
```

| 参数 | 说明 |
|------|------|
| `--graph doc` | 搜索文档图谱 |
| `-k N` | 返回条数 |
| `-b` / `--brief` | 简洁输出 |

### Card 搜索（API/组件精确查询）

```powershell
cd .agents\skills\cangjie-hmos-doc-search\doc-card
$env:PYTHONIOENCODING="utf-8"

cd D:\ZSY\CangjieSkills

# 关键词拼接并返回搜索词
python -c "
import json
with open(r'D:\ZSY\CangjieSkills\.agents\skills\cangjie-hmos-doc-search-maintenance\graph\evals\keywords_v7_prompt.json', encoding='utf-8') as f:
    kw = json.load(f)
k = kw['6']  # 数字为评测数据集中的查询索引
print('en:', k['keywords_en'])
print('zh:', k['keywords_zh'])
print('search_q:', ' '.join(k['keywords_en'] + k['keywords_zh']))
"

# 基本搜索
python search_v3.py "Router.pushUrl 参数" --mode auto --limit 5 --json

# 查看 top-5 最终检索路径（每卡 1 条最优路径 + 分数）
python search_v3.py "UIAbilityContext" --mode auto --limit 5 --json --paths
```

| 参数 | 说明 |
|------|------|
| `--mode auto` | 自动选择卡片类型 |
| `--limit N` | 返回条数 |
| `--json` | JSON 输出 |
| `--paths` | 追加 `top_paths` 字段（每卡 1 条最优路径 + 分数 + 卡片来源） |

### Fusion 搜索（双引擎融合）

```powershell
cd .agents\skills\cangjie-hmos-doc-search
python unified_search.py "要实现下拉刷新用什么组件" --json --limit 5
```

### 搜索所用数据集路径

| 用途 | 路径 |
|------|------|
| 评测数据集 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/evals/datasets/eval_queries_comprehensive_deduped.jsonl` |
| 关键词映射 | `.agents/skills/cangjie-hmos-doc-search-maintenance/graph/evals/keywords_v7_prompt.json` |
| 查询原始文本 | 评测数据集每条记录的 `query` 字段 |
| 查询搜索词 | `keywords_en + keywords_zh` 空格拼接（`keywords_v7_prompt.json`） |

### 三引擎完整检索输出查看命令

```powershell
$env:PYTHONIOENCODING="utf-8"

# === Card（结构化卡片检索 + top-5 最优路径） ===
cd .agents\skills\cangjie-hmos-doc-search\doc-card
python search_v3.py "List 组件 列表" --mode auto --limit 5 --json --paths

# === Graph（知识图谱语义检索 + JSON 输出） ===
cd .agents\skills\cangjie-hmos-doc-search\doc-graph
python cli.py search "List 组件 列表" --graph doc -k 5 --json

# === Fusion（双引擎融合 + top-5 最优路径） ===
cd .agents\skills\cangjie-hmos-doc-search
python unified_search.py "List 组件 列表" --json --limit 5
```

### 输出格式对照表（agent 读取指引）

| 引擎 | JSON 根字段 | agent 取路径字段 | agent 取来源字段 | score 字段 |
|------|------|------|------|:---:|
| **card** `--json --paths` | `{query, mode, understanding, tasks, apis, docs, paths, top_paths}` | `top_paths[].path` | `top_paths[].card` + `top_paths[].type` | `top_paths[].score` |
| **graph** `--json` | `{query, engine, graph_used, latency_ms, direct_hits, related_hits}` | `direct_hits[].source_file` | `direct_hits[].label` | `direct_hits[].score` |
| **fusion** `--json` | `{query, engine, direct_hits, related_hits, top_paths}` | `top_paths[].path`（优先）或 `direct_hits[].source_file` | `top_paths[].card` + `top_paths[].type`（优先）或 `direct_hits[].label` | `top_paths[].score` |

### `engine` 字段含义速查（fusion 输出）

| engine 值 | 含义 | agent 应如何处理 |
|------|------|------|
| `card+graph` | 同一文档被两个引擎都找到 | **最高优先级**，直接打开阅读 |
| `graph` | 仅图谱语义关联找到 | 次优先，验证相关性后阅读 |
| `card` | 仅卡片精确匹配找到 | 补充参考 |

### agent 决策优先级

```
agent 从三次检索（card / graph / fusion）获取结果后，按以下顺序决策：

1. 若结果含 top_paths 字段 → 直接按 score 排序取 top-3 → 读取 path 指向的文档
2. 若结果仅有 direct_hits → 取 engine="card+graph" 的（双引擎确认）→ 再取 engine="graph" 的
3. 若结果仅有 sections（card 未传 --paths 时）→ 遍历 tasks → apis → docs，取每个 item 的 paths[0]
4. 读取文档后，交叉验证文档内容是否与用户查询意图匹配
```

## 评测

### 三引擎 192 条全量评测

```powershell
cd .agents\skills\cangjie-hmos-doc-search-maintenance\graph\evals
$env:PYTHONIOENCODING="utf-8"

# 全量 192 条
python run_eval.py --limit 0 --output comparison_report.md

# 前 50 条（快速验证）
python run_eval.py --limit 50
```

### 评测指标

| 指标 | 含义 |
|------|------|
| Recall@5 | 前 5 个搜索结果（召回的路径）中是否有期望文档（card 与 graph 语义已对齐） |
| FULL | 直接命中（路径子串匹配 / 同目录匹配 / 包含或被包含期望路径） |
| PARTIAL | 关联命中（图邻居 / 相关推荐） |
| MISS | 未命中 |
| MRR | 平均倒数排名（第一个正确答案排第几） |

### 命中判定规则

1. **路径子串匹配**：返回路径与期望路径互为子串
2. **目录级匹配**：返回路径与期望路径在同一目录（`.overview.md` ⇄ `_2more.md` 等同目录文件视为命中）
3. 先检查直接命中 → 未命中则检查关联推荐

### 评测所用数据集

| 用途 | 路径 |
|------|------|
| 评测查询（192 条） | `graph/evals/datasets/eval_queries_comprehensive_deduped.jsonl` |
| 查询关键词 | `graph/evals/keywords_v7_prompt.json` |
| 评测报告输出 | `graph/evals/comparison_report_*.md` |

## 踩坑速查

| 现象 | 原因 | 解决 |
|------|------|------|
| graph enhance 全量 `unknown url type: 'xxx/chat/completions'` | `enhancer.py` 只读 `DASHSCOPE_*`，未设置该变量 | 设置 `$env:DASHSCOPE_API_BASE` 或检查 enhancer.py 版本 |
| card llm build 报 `缺少必要环境变量: OPENAI_BASE_URL, OPENAI_API_KEY` | card builder 读 `OPENAI_*`，不是 `DASHSCOPE_*` | 设置 `$env:OPENAI_API_KEY` 等 |
| 改 `extractor.py` 后 rebuild graph 无效果 | builder 使用缓存 `docs/.../graphify-out/cache/` | 清缓存或加 `--no-use-cache` |
| graph.json 单行打不开 | `json.dump` 未加 `indent` | 运行 `python -c "import json;f=open('...','r+');g=json.load(f);f.seek(0);json.dump(g,f,indent=2,ensure_ascii=False)"` |
| card 评测 Recall@5 异常低（<40%） | `check_hit` 缺少目录级匹配 / `card_paths[:5]` 截断 | 检查 `run_eval.py` 版本，确认目录匹配和 `collect_paths()` 就位 |
| PowerShell 中文乱码 | 未设 UTF-8 | `$env:PYTHONIOENCODING="utf-8"` |
| graph enhance 全量 429 限流 | 并发过高 | 降 `--max-workers 3` 或换 DeepSeek 端点 |