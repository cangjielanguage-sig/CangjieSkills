# 知识图谱架构图

## 整体架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                           用户/Agent                                 │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  用户有文档/代码项目，需要构建图谱指导仓颉 App 开发           │   │
│  │                                                               │   │
│  │  Trigger: /build-graph                                        │   │
│  │                                                               │   │
│  │  使用方式：                                                   │   │
│  │    方案 A（小项目）：单图谱构建                               │   │
│  │    方案 B（大项目）：子图谱构建 → 合并                        │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
            │
            │
            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         核心模块层                                   │
│                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   query.py  │  │    cli.py   │  │  builders/  │  │   export/   │ │
│  │  查询引擎   │  │  CLI入口    │  │  构建器     │  │  导出器     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘ │
│         │                │                │                │        │
│         │                │                │                │        │
│         ▼                ▼                ▼                ▼        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   core/     │  │  analysis/  │  │  engines/   │  │  feedback/  │ │
│  │  遍历/路由  │  │  分析器     │  │  图引擎     │  │  反馈系统   │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
            │
            │
            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         数据层                                       │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  用户图谱 (knowledge-graph-template/data/)                    │   │
│  │                                                               │   │
│  │  ├── subgraphs/                 子图谱目录                   │   │
│  │  │   ├── api/graph.json                                      │   │
│  │  │   ├── core/graph.json                                     │   │
│  │  │   ├── ui/graph.json                                       │   │
│  │  │   └── examples/graph.json                                 │   │
│  │  │                                                           │   │
│  │  ├── merged/graph.json          合并后的图谱                 │   │
│  │  ├── GRAPH_REPORT.md            分析报告                     │   │
│  │  └── feedback/queries.jsonl     查询反馈日志                 │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 子图谱构建与合并流程

```
用户项目文档/代码（大项目）
       │
       ├── docs/api/     API文档
       ├── docs/core/    核心代码
       ├── docs/ui/      UI文档
       └── docs/examples/ 示例代码
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  子图谱构建（并行）                                  │
│                                                                      │
│  build-subgraph docs/api --name api                                 │
│  build-subgraph docs/core --name core                               │
│  build-subgraph docs/ui --name ui                                   │
│  build-subgraph docs/examples --name examples                       │
│                                                                      │
│  输出：                                                              │
│  ├── data/subgraphs/api/graph.json                                  │
│  ├── data/subgraphs/core/graph.json                                 │
│  ├── data/subgraphs/ui/graph.json                                   │
│  └── data/subgraphs/examples/graph.json                             │
└─────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  子图谱合并                                          │
│                                                                      │
│  merge \                                                             │
│    data/subgraphs/api/graph.json \                                   │
│    data/subgraphs/core/graph.json \                                  │
│    data/subgraphs/ui/graph.json \                                    │
│    data/subgraphs/examples/graph.json \                              │
│    --output data/merged/graph.json                                   │
│                                                                      │
│  合并步骤：                                                          │
│  ├── 1. 加载所有子图谱                                               │
│  ├── 2. 合并节点和边                                                 │
│  ├── 3. 去重（基于 label）                                          │
│  ├── 4. 重新聚类（Leiden）                                          │
│  └── 5. 标注层级（L1/L2/L3）                                        │
│                                                                      │
│  输出：                                                              │
│  └── data/merged/graph.json                                         │
└─────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  查询合并图谱                                        │
│                                                                      │
│  python cli.py search "概念" --graph data/merged/graph.json         │
│                                                                      │
│  或使用 Python API：                                                 │
│  session.load_graph("data/merged/graph.json")                       │
│  session.search("概念")                                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 模块调用关系

### 构建流程

```
用户文档/代码
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                    builders/ 模块                        │
│                                                         │
│  detect.py ──► 文件检测分类                              │
│       │                                                 │
│       ▼                                                 │
│  extract_ast.py ──► AST 提取 (tree-sitter)              │
│       │       │                                         │
│       │       ▼                                         │
│       │  extract_semantic.py ──► 简化语义提取           │
│       │       │                                         │
│       │       ▼                                         │
│       │  extract_semantic_llm.py ──► LLM 语义提取       │
│       │       (需要 OPENAI_API_KEY)                     │
│       │                                                 │
│       ▼                                                 │
│  validate.py ──► 验证 extraction JSON                   │
│       │                                                 │
│       ▼                                                 │
│  build.py ──► 构建 NetworkX 图                          │
│       │       (from_extraction_dict)                    │
│       │                                                 │
│       ▼                                                 │
│  cluster.py ──► Leiden/Louvain 聚类                     │
│       │       (assign_communities_to_nodes)             │
│       │                                                 │
│       ▼                                                 │
│  分层标注 (layer: 1/2/3)                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                    export/ 模块                          │
│                                                         │
│  json.py ──► 导出 graph.json                            │
│  report.py ──► 生成 GRAPH_REPORT.md                     │
│  html.py ──► 导出 HTML 可视化 (小图谱)                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
  graph.json + GRAPH_REPORT.md
```

### 查询流程

```
Agent 查询请求
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                    query.py 模块                         │
│                                                         │
│  create_session()                                       │
│       │                                                 │
│       ▼                                                 │
│  GraphSession                                           │
│       │                                                 │
│       └──► load_graph("data/my-graph.json")             │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                    查询执行                              │
│                                                         │
│  search(query)                                          │
│       │                                                 │
│       ├──► score_nodes() (打分排序)                     │
│       │     core/traversal.py                           │
│       │                                                 │
│       ├──► traverse() (BFS/DFS)                         │
│       │     core/traversal.py                           │
│       │                                                 │
│       ├──► find_path() (路径查询)                       │
│       │     NetworkX shortest_path                      │
│       │                                                 │
│       └──► explain() (节点详情)                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                    analysis/ 模块                        │
│                                                         │
│  god_nodes() ──► 核心节点 (degree top-N)                │
│  surprises() ──► 惊奇连接 (跨社区边)                    │
│  questions() ──► 建议问题                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
  返回结果给 Agent
```

### 反馈优化流程

```
Agent 查询结果
      │
      ├──► 标记满意度
      │     session.mark_satisfied(query, True/False)
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                  feedback/ 模块                          │
│                                                         │
│  feedback.py                                            │
│       │                                                 │
│       ├──► log_query() (记录查询)                       │
│       │     queries.jsonl                               │
│       │                                                 │
│       ├──► track_failed() (失败查询追踪)                │
│       │                                                 │
│       └──► get_missed_queries() (未命中查询)            │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│                  自动优化                                │
│                                                         │
│  session.optimize()                                     │
│       │                                                 │
│       ├──► 学习别名 (从失败查询)                        │
│       │                                                 │
│       ├──► 推断新边 (从共现查询)                        │
│       │                                                 │
│       └──► 调整权重 (从满意度标记)                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
      │
      ▼
  更新 graph.json
```

---

## CLI 命令流向

```
cli.py
   │
   ├──► build <path> ──► builders/ ──► graph.json
   │
   ├──► search <query> ──► query.py ──► score_nodes()
   │
   ├──► traverse <query> ──► query.py ──► bfs_traverse() / dfs_traverse()
   │
   ├──► path <A> <B> ──► query.py ──► find_path()
   │
   ├──► explain <node> ──► query.py ──► explain()
   │
   ├──► god-nodes ──► analysis/analyze.py
   │
   ├──► surprises ──► analysis/analyze.py
   │
   ├──► questions ──► analysis/analyze.py
   │
   ├──► stats ──► query.py ──► get_stats()
   │
   ├──► export ──► export/{json,html,report}.py
   │
   └──► optimize ──► feedback/feedback.py
```

---

## 与其他 Skills 的协作

```
┌─────────────────────────────────────────────────────────────────┐
│                     Skills 协作关系                              │
│                                                                 │
│  harmonyos-project-init (创建项目)                              │
│       │                                                         │
│       ├──► harmonyos-requirements (需求分析)                   │
│       │                                                         │
│       ├──► knowledge-graph-template (构建项目图谱)             │
│       │     │                                                   │
│       │     ├─► 理解项目结构                                    │
│       │     ├─► 发现模块关联                                    │
│       │     └─► 定位 API 实现                                   │
│       │                                                         │
│       ├──► harmonyos-build (构建)                              │
│       │                                                         │
│       ├──► harmonyos-app-diagnose (诊断)                       │
│       │                                                         │
│       └──► harmonyos-evolution (经验沉淀)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 数据流向

```
用户项目文档/代码
       │
       ├── docs/api/
       ├── docs/guide/
       ├── docs/src/
       └── docs/examples/
       │
       ▼
 builders/ (构建器)
       │
       ├──► detect.py (文件检测)
       ├──► extract_ast.py (AST提取)
       ├──► extract_semantic.py (语义提取)
       ├──► build.py (NetworkX构建)
       ├──► cluster.py (聚类)
       └──► validate.py (验证)
       │
       ▼
 data/
       │
       ├── my-graph.json
       ├── GRAPH_REPORT.md
       └── feedback/queries.jsonl
       │
       ▼
 query.py (查询引擎)
       │
       ├──► search (打分排序)
       ├──► traverse (BFS/DFS)
       ├──► find_path (路径查询)
       └──► explain (节点详情)
       │
       ▼
 Agent (理解项目结构，指导仓颉 App 开发)
```

---

## 关键设计

### 1. 三层图谱结构

图谱按重要度分层，帮助 Agent 快速定位：

| 层级 | 名称 | 内容 | 权重 |
|------|------|------|------|
| **L1** | 概念层 | 文档、指南、概述 | ×1.5 |
| **L2** | API 层 | 类、接口、组件定义 | ×2.0 |
| **L3** | 实现层 | 函数、属性、测试代码 | ×0.2 |

**查询策略**：
- `search_concept()` → L1（快速定位文档）
- `search_api()` → L1+L2（定位 API）
- `search_impl()` → L3（深入实现）

### 2. 智能路由（多图谱场景）

当用户构建多个图谱时，智能路由选择：

```python
# query.py
class GraphSession:
    def load_graph(self, path: str):
        self._engine.load(path)

    def search(self, query: str):
        # 直接在加载的图谱中搜索
        return self._engine.search(query)
```

### 3. 反馈优化闭环

```
查询 → 结果 → 标记满意度 → 日志 → 分析 → 优化 → 更新图谱
```

**自动学习**：
1. 失败查询 → 学习别名
2. 共现查询 → 推断新边
3. 满意度标记 → 调整权重

---

## 性能指标

| 操作 | 延迟 | 说明 |
|------|------|------|
| search (L1+L2) | ~100ms | 打分排序 |
| traverse (depth=3) | ~150ms | BFS/DFS |
| find_path | ~50ms | NetworkX shortest_path |
| explain | ~10ms | 单节点查询 |
| build (AST) | 视文件数而定 | tree-sitter解析 |

---

## 文件清单

```
knowledge-graph-template/
├── cli.py              # CLI入口 (627行)
├── query.py            # 查询引擎 (282行)
├── SKILL.md            # Skill文档 (用户构建场景)
├── README.md           # 快速开始
│
├── docs/               # 用户文档目录 (空白)
│   └── .gitkeep
│
├── data/               # 图谱输出目录 (空白)
│   └── feedback/
│
├── builders/           # 构建器
│   ├── extract_ast.py          # AST提取 (3516行, 30+语言)
│   ├── extract_semantic.py     # 简化语义 (168行)
│   ├── extract_semantic_llm.py # LLM语义 (426行)
│   ├── build.py                # NetworkX构建 (231行)
│   ├── cluster.py              # Leiden聚类 (108行)
│   ├── detect.py               # 文件检测 (352行)
│   ├── validate.py             # 验证
│   └── security.py             # 安全
│
├── analysis/           # 分析器
│   └── analyze.py              # God nodes等 (368行)
│
├── export/             # 导出器
│   ├── json.py                 # JSON导出 (79行)
│   ├── html.py                 # HTML可视化 (165行)
│   └── report.py               # 分析报告 (87行)
│
├── core/               # 核心模块
│   ├── traversal.py            # BFS/DFS (272行)
│   └── smart_router.py         # 智能路由
│
├── engines/            # 图引擎
│   └── graphify_engine.py      # NetworkX实现
│
├── feedback/           # 反馈系统
│   └── feedback.py             # 查询日志
│
└── scripts/            # 辅助脚本
    ├── rebuild_index.py
    └── analyze_feedback.py
```

---

## 总结

1. **核心能力**
   - 构建：AST + 语义提取 → NetworkX 图
   - 查询：分层搜索 → 图遍历
   - 分析：God nodes、Surprises、Questions
   - 优化：反馈闭环 → 自动学习

2. **Agent 使用流程**
   ```
   用户放入文档/代码 → 构建图谱 → Agent查询 → 理解项目结构
   ```

3. **指导仓颉 App 开发**
   - 理解项目模块结构
   - 发现组件/API 关联
   - 定位实现代码
   - 查询依赖路径