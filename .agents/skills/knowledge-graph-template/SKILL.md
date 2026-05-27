---
name: knowledge-graph-template
description: "鸿蒙仓颉知识图谱，基于 graphify v7 构建。与 cangjie-harmonyos-doc-search 平权：V3 负责精确 API/属性/错误码/穷举检索，本 Skill 负责语义/组合/架构/跨生态类比/邻域推理。共享同一套文档源（harmonyos-6.0.2-15k / lang-features / std / stdx / tools），通过 MCP 暴露 7 个工具给 code agent。"
trigger: /build-graph
---

# 鸿蒙仓颉知识图谱 Skill（与 V3 平权）

## 定位

本 Skill 与 `cangjie-harmonyos-doc-search`（下称 V3）**平权并存**，各自擅长不同 query 类型：

| Query 特征 | 用 V3 | 用本 Skill |
|---|---|---|
| 明确 API / 组件名 / 属性 / 事件 | ✓ | |
| 错误码 / 错误信息 | ✓ | |
| 穷举式（"有哪些属性"）| ✓ | |
| 跨概念组合（"带下拉刷新的网络列表页"）| | ✓ |
| 语义模糊（"卡顿"/"响应式失效"）| | ✓ |
| 跨生态类比（"鸿蒙版 RecyclerView"）| | ✓ |
| "A 和 B 怎么配合" / 依赖链 | | ✓ |
| 领域核心 API / 架构鸟瞰 | | ✓ |

Agent 按 query 特征分发，两引擎结果融合见 `cangjie-harmonyos-doc-search/SKILL.md` 的"结果融合规则"一节。

## 对 Agent 暴露：MCP 7 工具

接入方式见 `MCP_USAGE.md`。七个工具：

- `query_graph` —— 语义/关键词搜索图谱节点
- `get_node` —— 节点详情（community / layer / source_file）
- `get_neighbors` —— 邻居遍历（典型搭档）
- `get_community` —— 社区（一个功能领域的全部节点）
- `god_nodes` —— 度中心性 top N（领域核心）
- `graph_stats` —— 规模统计
- `shortest_path` —— 两节点最短路径

共享数据源：`docs/{harmonyos-6.0.2-15k,lang-features,std,stdx,tools}` 是指向 `cangjie-harmonyos-doc-search/` 同名目录的 symlink，不需要二次拷贝。

## 对开发者暴露：/build-graph（用户自带语料）

以下内容是 graphify v7 模板原有功能，供你用自己的文档/代码构建独立图谱。**主用途是定制化扩展，不是维护线上 agent 路径**——线上路径由上文的 MCP 工具驱动。

将你自己的文档和代码转化为三层知识图谱，用于指导仓颉 App 开发。

**一句话定位**：让 AI 理解你的项目结构，发现你不知道的关联。

---

## 快速开始

### 1. 放入你的资料

```bash
# 将文档放入 docs/
cp your_docs/*.md docs/
cp your_code/*.cj docs/
cp your_examples/* docs/

# 或创建子目录
mkdir docs/api docs/guide docs/examples
```

**支持格式**：
- 文档：`.md`, `.txt`, `.rst`
- 代码：`.cj`, `.py`, `.js`, `.ts`, `.java`, `.go`, `.rs`, `.c`, `.cpp`
- 配置：`.json`, `.yaml`, `.toml`

### 2. 构建图谱

```bash
# 全量构建
python cli.py build docs/ --output data/my-graph.json

# 查看构建报告
python cli.py export --graph data/my-graph.json --format report
```

**构建输出**：
- `data/my-graph.json` — 图谱数据
- `data/GRAPH_REPORT.md` — 分析报告（核心节点、惊奇连接、建议问题）

### 3. 查询图谱

```bash
# 搜索
python cli.py search "你的概念" --limit 5

# 图遍历（发现关联）
python cli.py traverse "你的概念" --depth 3

# 路径查询
python cli.py path "概念A" "概念B"

# 解释节点
python cli.py explain "某个API"

# 核心节点
python cli.py god-nodes --top-n 10
```

---

## Python API（Agent 编程接口）

### 基础搜索

```python
from query import create_session

# 加载你的图谱
session = create_session()
session.load_graph("data/my-graph.json")

# 搜索（定位文档）
result = session.search("你的概念", limit=10)
for path in result.paths:
    print(f"  {path}")

# 图遍历（发现关联）
traverse_result = session.traverse("你的概念", mode="bfs", depth=3)
print(f"找到 {len(traverse_result.nodes)} 个节点")

# 路径查询
path = session.find_path("概念A", "概念B")
for node in path:
    print(f"  {node.label}")

# 核心节点（God Nodes）— 连接最多的概念
god_nodes = session.god_nodes(top_n=10)
for n in god_nodes:
    print(f"{n['label']}: {n['degree']} 条连接")

# 惊奇连接— 跨社区的关联
surprises = session.surprises(top_n=5)
for s in surprises:
    print(f"{s['source']} ↔ {s['target']}")

# 建议问题 — 图谱能回答的问题
questions = session.suggest_questions(top_n=7)
for q in questions:
    print(f"{q['question']}")
```

### LLM语义增强搜索

**Agent 使用知识图谱搜索时，应先进行语义理解，生成更好的搜索输入。**

```python
from query_llm import create_llm_session

# 创建LLM增强会话
session = create_llm_session(enable_enhancement=True)

# 搜索（自动改写query）
result = session.search("怎么做一个列表页面")
# 内部流程：原始query → 预定义规则改写 → KG搜索

print(f"原始query: {result.original_query}")
print(f"改写query: {result.enhanced_query}")
print(f"结果: {len(result.paths)} 条路径")
```

**Agent 搜索流程**：

```
用户问题 → Agent语义理解 → 改写query → KG关键词匹配 → 返回文档路径
```

**改写规则**（Agent 内置预定义规则）：

1. **添加路径关键片段**：如 `cj-scroll-swipe-list`、`cj-apis-net-http`
2. **添加核心概念**：如 `List`、`Refresh`、`Navigation`
3. **添加Kit名称**：如 `NetworkKit`、`CryptoArchitectureKit`
4. **去除冗余词**：如 "怎么"、"如何"、"实现"
5. **保留核心概念**：用空格分隔关键词

---

## 子图谱构建与合并

当项目规模较大时，建议先构建子图谱，再合并：

### 1. 构建子图谱

```bash
# 按模块构建子图谱
python cli.py build-subgraph docs/api --name api
python cli.py build-subgraph docs/core --name core
python cli.py build-subgraph docs/ui --name ui
python cli.py build-subgraph docs/examples --name examples
```

**子图谱输出**：
- `data/subgraphs/api/graph.json`
- `data/subgraphs/core/graph.json`
- `data/subgraphs/ui/graph.json`
- `data/subgraphs/examples/graph.json`

### 2. 合并子图谱

```bash
# 合并所有子图谱
python cli.py merge \
  data/subgraphs/api/graph.json \
  data/subgraphs/core/graph.json \
  data/subgraphs/ui/graph.json \
  data/subgraphs/examples/graph.json \
  --output data/merged/graph.json
```

**合并参数**：
| 参数 | 说明 |
|------|------|
| `--no-deduplicate` | 不去重（保留所有节点） |
| `--no-recluster` | 不重新聚类（保留原社区） |
| `--directed` | 生成有向图 |

### 3. Python API

```python
from builders import merge_graphs

# 合并多个图谱
G = merge_graphs(
    ["data/subgraphs/api/graph.json", "data/subgraphs/core/graph.json"],
    "data/merged/graph.json",
    deduplicate=True,
    recluster=True,
)

print(f"合并图谱: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")
```

---

## 三层图谱结构

图谱按重要度分层，帮助 Agent 快速定位：

| 层级 | 名称 | 内容 | 权重 |
|------|------|------|------|
| **L1** | 概念层 | 文档、指南、概述 | ×1.5 |
| **L2** | API 层 | 类、接口、组件定义 | ×2.0 |
| **L3** | 实现层 | 函数、属性、测试代码 | ×0.2 |

**查询策略**：
- `search_concept()` — 只搜索 L1（快速定位文档）
- `search_api()` — 搜索 L1+L2（定位 API）
- `search_impl()` — 搜索 L3（深入实现）

---

## 构建模式

### AST 模式（默认）

基于 tree-sitter 解析代码，提取结构信息（无 API 成本）：

```bash
python cli.py build docs/ --output data/graph.json
```

**支持语言**：30+（仓颉、Python、JS、TS、Java、Go、Rust、C/C++ 等）

### 语义模式（需要 OPENAI_API_KEY）

LLM 提取概念、rationale、跨文档关联：

```bash
export OPENAI_API_KEY=sk-xxx
python cli.py build docs/ --mode deep --output data/graph.json
```

**提取内容**：
- 概念节点（概念、rationale）
- 超边（跨文档关联）
- 语义边（rationale-driven）

---

## 图谱分析

构建完成后，查看分析报告：

```bash
python cli.py export --graph data/my-graph.json --format report
```

**报告内容**：

1. **核心节点（God Nodes）**：连接最多的概念
   - 代表项目核心概念
   - Agent 应优先理解这些节点

2. **惊奇连接**：跨社区的边
   - 发现隐式关联
   - Agent 可从这里探索新方向

3. **建议问题**：图谱能回答的问题
   - 代表图谱覆盖范围
   - Agent 可据此判断查询成功率

---

## 与仓颉 App 开发结合

### 场景：开发仓颉鸿蒙应用

1. **放入项目资料**
   ```bash
   mkdir docs/my-app
   cp AppScope/**/*.md docs/my-app/
   cp entry/**/*.cj docs/my-app/
   cp examples/**/*.md docs/my-app/
   ```

2. **构建图谱**
   ```bash
   python cli.py build docs/my-app --output data/my-app-graph.json
   ```

3. **Agent 查询**
   ```python
   session = create_session()
   session.load_graph("data/my-app-graph.json")

   # 理解项目结构
   god_nodes = session.god_nodes(top_n=10)

   # 发现模块关联
   surprises = session.surprises(top_n=5)

   # 查询 API 用法
   result = session.search_api("Component")

   # 查找依赖路径
   path = session.find_path("UIAbility", "MyComponent")
   ```

---

## CLI 命令速查

| 命令 | 说明 | 示例 |
|------|------|------|
| `build` | 构建图谱 | `build docs/ --output graph.json` |
| `build-subgraph` | 构建子图谱 | `build-subgraph docs/api --name api` |
| `merge` | 合并子图谱 | `merge graph1.json graph2.json --output merged.json` |
| `search` | 搜索 | `search "概念" --limit 5` |
| `traverse` | 图遍历 | `traverse "概念" --depth 3 --dfs` |
| `path` | 路径查询 | `path "A" "B"` |
| `explain` | 解释节点 | `explain "API"` |
| `neighbors` | 邻居节点 | `neighbors "节点"` |
| `god-nodes` | 核心节点 | `god-nodes --top-n 10` |
| `surprises` | 惊奇连接 | `surprises --top-n 5` |
| `questions` | 建议问题 | `questions --top-n 7` |
| `stats` | 统计 | `stats` |
| `export` | 导出 | `export --format report` |

---

## 目录结构

```
knowledge-graph-template/
├── cli.py              # CLI 入口
├── query.py            # 查询引擎
├── query_llm.py        # LLM增强搜索
├── SKILL.md            # 本文档
├── README.md           # 快速开始
│
├── docs/               # 你的文档/代码（放入这里）
│   └── .gitkeep
│
├── data/               # 图谱输出
│   ├── my-graph.json   # 构建产物
│   ├── GRAPH_REPORT.md # 分析报告
│   └── feedback/       # 查询反馈
│
├── builders/           # 构建器
│   ├── extract_ast.py          # AST 提取（30+ 语言）
│   ├── extract_semantic.py     # 语义提取（简化版）
│   ├── extract_semantic_llm.py # LLM 语义提取
│   ├── build.py                # 构建 NetworkX 图
│   ├── cluster.py              # Leiden 聚类
│   ├── detect.py               # 文件检测
│   ├── validate.py             # 验证
│   ├── security.py             # 安全
│   ├── query_enhancer.py       # Query改写规则
│   └── v3_rules_adapter.py     # V3规则适配器
│
├── analysis/           # 分析器
│   └── analyze.py      # God nodes、surprises、questions
│
├── export/             # 导出器
│   ├── json.py         # JSON 导出
│   ├── html.py         # HTML 可视化
│   └── report.py       # 分析报告
│
├── core/               # 核心模块
│   ├── traversal.py    # BFS/DFS 遍历
│   └── smart_router.py # 智能路由
│
├── engines/            # 图引擎
│   └── graphify_engine.py  # NetworkX 实现
│
├── feedback/           # 反馈系统
│   └── feedback.py     # 查询日志、优化建议
│
└── scripts/            # 辅助脚本
    └── rebuild_index.py    # 重建索引
```

---

## 最佳实践

1. **分层放入资料**
   - `docs/api/` — API 文档
   - `docs/guide/` — 开发指南
   - `docs/examples/` — 示例代码
   - `docs/src/` — 源代码

2. **定期更新图谱**
   ```bash
   # 文档变化后
   python cli.py build docs/ --update
   ```

3. **标记查询满意度**
   ```python
   session.mark_satisfied("某个查询", True)  # 满意
   session.mark_satisfied("某个查询", False) # 不满意
   ```

4. **执行自动优化**
   ```python
   report = session.optimize()
   # 新增边、别名、权重调整
   ```

---

## 依赖安装

```bash
pip install tree-sitter-python networkx leidenalg

# 如需更多语言支持
pip install tree-sitter-javascript tree-sitter-typescript
pip install tree-sitter-java tree-sitter-go
pip install tree-sitter-rust tree-sitter-c tree-sitter-cpp
```