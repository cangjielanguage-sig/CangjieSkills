# core/ — 核心功能模块

本目录包含知识图谱的核心功能：搜索、遍历、路由、分层、数据模型。

---

## 目录结构

```
core/
├── search.py          # 搜索算法（打分排序）
├── traversal.py       # 图遍历（BFS/DFS）
├── smart_router.py    # 智能路由器（三层路由策略）
├── router.py          # 基础路由器（关键词路由）
├── layer.py           # 分层标注（L1/L2/L3）
├── models.py          # 数据模型定义
└── __init__.py        # 模块导出
```

---

## 一、search.py — 搜索算法

### 功能

搜索 = **打分排序**（定位文档），不是图遍历。

从图谱中找到与查询最相关的节点，按分数排序返回。

### 实现原理

```python
class GraphSearch:
    def search_all(self, query: str, limit: int = 10) -> SearchResult:
        """
        全量搜索流程：
        
        1. 分词 → tokenize_query(query)
           例: "std.net 网络" → ['std', 'net', 'stdnet', '网络']
        
        2. 遍历节点 → 对每个节点计算匹配分数
        
        3. 分数计算 → score_node(query, node_data, tokens)
           - label 匹配: +10 分（精确匹配 +15）
           - source_file 匹配: +5 分（路径包含关键词）
           - 中文字符匹配: +3 分
           - overview/abstract 节点: ×1.5 加权
           - 高度节点（degree > 20）: ×1.3 加权
        
        4. 分层权重 → LAYER_WEIGHTS = {1: 1.5, 2: 2.0, 3: 0.2}
           概念层节点优先返回
        
        5. 排序 → sorted(nodes, key=score, reverse=True)
        
        6. 返回前 N 个结果
        """
```

### 关键参数

| 参数 | 默认值 | 说明 |
|------|:------:|------|
| `LAYER_WEIGHTS` | {1:1.5, 2:2.0, 3:0.2} | 分层权重，概念层优先 |
| `match_ratio` | 1 + matched/total | 匹配率加成 |
| `degree_threshold` | 20 | 高度节点加权阈值 |

### 使用示例

```python
from core.search import GraphSearch
from engines import GraphifyEngine

engine = GraphifyEngine()
engine.load('graph.json')
search = GraphSearch(engine)

# 全层搜索
result = search.search_all("List 组件", limit=10)

# 概念层搜索（L1）
result = search.search_concept("状态管理")

# API 层搜索（L1+L2）
result = search.search_api("Button onClick")

# 实现层搜索（L3）
result = search.search_impl("LazyForEach getData")
```

### 与 traversal.py 的区别

| 功能 | search.py | traversal.py |
|------|:---------:|:------------:|
| 目的 | 定位文档 | 发现关联 |
| 方法 | 打分排序 | BFS/DFS 图遍历 |
| 输入 | 查询关键词 | 查询关键词 + 起点 |
| 输出 | 排序节点列表 | 子图结构（节点+边） |
| 适用场景 | "List 组件在哪" | "List 和 Button 有什么关系" |

---

## 二、traversal.py — 图遍历

### 功能

图遍历 = **BFS/DFS 遍历**（发现关联关系）。

从一个起点出发，沿着边探索相关节点，返回子图结构。

### 实现原理

```python
def traverse(G: nx.Graph, query: str, mode: str = "bfs", depth: int = 3) -> TraverseResult:
    """
    图遍历流程：
    
    1. 分词 → tokenize_query(query)
    
    2. 找起点 → score_nodes(G, terms) → top 3 个匹配节点
    
    3. BFS 遍历（广度优先）
       - 从起点出发，逐层扩展
       - 每层收集所有邻居节点
       - visited, frontier = set(start_nodes), set(start_nodes)
       - for layer in range(depth):
           next_frontier = {所有未访问的邻居}
           visited.update(next_frontier)
           edges_seen.append(所有边)
    
    4. DFS 遍历（深度优先）
       - 从起点出发，深度探索一条路径
       - stack = [(node, depth)]
       - while stack:
           pop(node, d)
           if d > depth: continue
           visited.add(node)
           for neighbor in G.neighbors(node):
               if not visited:
                   stack.append((neighbor, d+1))
    
    5. 输出截断 → token_budget 控制（约 3 chars/token）
    
    6. 返回 TraverseResult(nodes, edges, subgraph_json)
    """
```

### BFS vs DFS

| 算法 | BFS（广度优先） | DFS（深度优先） |
|------|:---------------:|:---------------:|
| 策略 | 逐层扩展 | 深度探索 |
| 结果 | 广泛相关节点 | 深度关联路径 |
| 适用场景 | 发现相关概念 | 追踪依赖链 |
| 示例查询 | "List 相关概念" | "Button → onClick → 处理流程" |

### 核心分析函数

```python
def god_nodes(G: nx.Graph, top_n: int = 10) -> list[dict]:
    """
    核心节点 = 连接最多的节点。
    
    原理：
    1. degree = dict(G.degree())
    2. sorted_nodes = sorted(degree, reverse=True)
    3. 排除文件级 hub 节点（label == source_file.name）
    4. 排除方法 stub 节点（label.startswith('.') and label.endswith('()'))
    
    意义：
    - 代表知识图谱的核心抽象
    - 是用户应该首先了解的概念
    """

def surprising_connections(G: nx.Graph, top_n: int = 5) -> list[dict]:
    """
    惊奇连接 = 跨社区的边。
    
    原理：
    1. 遍历所有边
    2. 判断 (source_community != target_community)
    3. 排除结构性边（imports, contains, method）
    4. 按 confidence 排序（AMBIGUOUS > INFERRED > EXTRACTED）
    5. 去重（每个社区对只保留一条代表边）
    
    意义：
    - 发现非显而易见的关联
    - 揭示跨领域的知识连接
    """

def suggest_questions(G: nx.Graph, top_n: int = 7) -> list[dict]:
    """
    建议问题 = 基于图结构生成问题。
    
    原理：
    1. AMBIGUOUS 边 → "X 和 Y 的确切关系是什么？"
    2. 高 betweenness 节点 → "为什么 X 连接多个社区？"
    3. 多 INFERRED 边节点 → "X 的推断关系是否正确？"
    4. 孤立节点 → "X 如何与系统连接？"
    5. 低凝聚力社区 → "社区 X 是否需要拆分？"
    
    意义：
    - 帮助用户探索图谱
    - 发现知识盲区
    """
```

### 使用示例

```python
from core.traversal import traverse, traverse_text, god_nodes, surprising_connections

# BFS 遍历
result = traverse(G, "List", mode="bfs", depth=3)
print(traverse_text(result))

# DFS 遍历
result = traverse(G, "Button", mode="dfs", depth=6)

# 核心节点
nodes = god_nodes(G, top_n=10)

# 惊奇连接
surprises = surprising_connections(G, top_n=5)

# 建议问题
questions = suggest_questions(G, top_n=7)
```

---

## 三、smart_router.py — 智能路由器

### 功能

三层智能路由策略，将查询路由到最合适的图谱。

### 实现原理

```python
class SmartRouter:
    """
    三层路由策略：
    
    第一层：前缀匹配（最高优先级）
    ┌─────────────────────────────────────────────┐
    │ PREFIX_MAP = {                              │
    │     "std.": "std",                          │
    │     "stdx.": "stdx",                        │
    │     "harmonyos.": "harmonyos",              │
    │ }                                           │
    │                                             │
    │ 匹配规则：                                   │
    │ if "std.crypto" in query → route to "std"   │
    │                                             │
    │ 意义：                                       │
    │ 用户明确指定领域，直接路由                    │
    └─────────────────────────────────────────────┘
    
    第二层：域名权重匹配
    ┌─────────────────────────────────────────────┐
    │ DOMAIN_WEIGHTS = {                          │
    │     ("crypto", "stdx"): 5.0,  # stdx.crypto │
    │     ("cipher", "std"): 2.5,   # std.crypto  │
    │     ("net", "std"): 2.0,      # std.net     │
    │     ("http", "stdx"): 5.0,    # stdx.http   │
    │ }                                           │
    │                                             │
    │ 匹配规则：                                   │
    │ if domain in query → score += weight        │
    │ 选择得分最高的图谱                           │
    │                                             │
    │ 意义：                                       │
    │ 根据领域特征智能路由                         │
    │ 解决关键词冲突（cipher 在 std/stdx 都有）    │
    └─────────────────────────────────────────────┘
    
    第三层：关键词模糊匹配
    ┌─────────────────────────────────────────────┐
    │ KEYWORD_WEIGHTS = {                         │
    │     "socket": ("std", 2.5),                 │
    │     "http": ("stdx", 3.0),                  │
    │     "加密": ("stdx", 1.5),                   │
    │ }                                           │
    │                                             │
    │ 匹配规则：                                   │
    │ if keyword in query → score += weight       │
    │                                             │
    │ 意义：                                       │
    │ 兜底策略，处理模糊查询                       │
    └─────────────────────────────────────────────┘
    
    默认：merged（全量图谱）
    """
```

### 路由示例

| 查询 | 路由结果 | 原因 |
|------|:--------:|------|
| `std.crypto 加密` | std | 第一层：前缀 `std.` |
| `cipher` | std | 第二层：cipher → std 权重 2.5 |
| `crypto` | stdx | 第二层：crypto → stdx 权重 5.0 |
| `std.net 网络` | std | 第一层：前缀 `std.` |
| `http` | stdx | 第三层：关键词 http → stdx |
| `Button` | harmonyos | 第三层：关键词 Button → harmonyos |
| `状态管理` | merged | 无匹配，默认全量 |

### 使用示例

```python
from core.smart_router import SmartRouter

router = SmartRouter(merged_search, subgraph_searches)

# 路由查询
searcher, graph_name = router.route("std.crypto 加密")
print(f"路由到: {graph_name}")

# 搜索（自动路由）
result = router.search("List 组件", limit=10)
```

---

## 四、router.py — 基础路由器

### 功能

基于关键词的简单路由器，用于快速路由。

### 实现原理

```python
SUBGRAPH_KEYWORDS = {
    "harmonyos": ["uiability", "arkui", "list", "button", ...],
    "std": ["array", "hashmap", "file", "net", ...],
    "stdx": ["crypto", "http", "tls", ...],
    "lang-features": ["class", "struct", "closure", ...],
    "tools": ["cjpm", "lsp", "debug", ...],
}

def _classify(query: str) -> Optional[str]:
    """
    分类流程：
    
    1. tokens = tokenize_query(query)
    
    2. for graph, keywords in SUBGRAPH_KEYWORDS.items():
        score = sum(
            2 if keyword in query else
            1 if keyword.startswith(token) else
            0
            for keyword in keywords
            for token in tokens
        )
    
    3. threshold = 2
       if max_score < threshold: return None（使用 merged）
       else: return max_score graph
    """
```

### 与 smart_router.py 的区别

| 特性 | router.py | smart_router.py |
|------|:---------:|:---------------:|
| 路由层数 | 1 层 | 3 层 |
| 精度 | 中 | 高 |
| 性能 | 快 | 稍慢 |
| 适用场景 | 简单路由 | 复杂路由 |

---

## 五、layer.py — 分层标注

### 功能

为图谱节点标注层级（L1 概念层、L2 API 层、L3 实现层）。

### 实现原理

```python
def annotate_layer(node: dict) -> int:
    """
    分层规则：
    
    L1 概念层：
    ┌─────────────────────────────────────────────┐
    │ 规则：                                       │
    │ - source_file 包含 "guide/", "overview"     │
    │ - source_file 包含 "概述", "介绍", "概览"    │
    │ - node_type in ["package", "module"]        │
    │                                             │
    │ 典型节点：                                   │
    │ - "List 组件概述"                            │
    │ - "状态管理指南"                             │
    │ - "std.crypto Module"                       │
    │                                             │
    │ 意义：                                       │
    │ 代表概念和架构，适合架构探索                  │
    └─────────────────────────────────────────────┘
    
    L2 API 层：
    ┌─────────────────────────────────────────────┐
    │ 规则：                                       │
    │ - source_file 包含 "api/", "interface"      │
    │ - source_file 包含 "_package_", "_class_"  │
    │ - node_type in ["class", "function", "enum"]│
    │                                             │
    │ 典型节点：                                   │
    │ - "List Class"                              │
    │ - "Button onClick"                          │
    │ - "HashMap put()"                           │
    │                                             │
    │ 意义：                                       │
    │ 代表 API 定义，适合组件查找                  │
    └─────────────────────────────────────────────┘
    
    L3 实现层：
    ┌─────────────────────────────────────────────┐
    │ 规则：                                       │
    │ - source_file 包含 "src/", ".cj", ".py"     │
    │ - node_type in ["method", "variable", "line"]│
    │                                             │
    │ 典型节点：                                   │
    │ - "encrypt()"                               │
    │ - "getData()"                               │
    │ - "self.token"                              │
    │                                             │
    │ 意义：                                       │
    │ 代表具体实现，适合源码追溯                  │
    └─────────────────────────────────────────────┘
    
    默认：L3（实现层）
    """
```

### 分层权重

```python
LAYER_WEIGHTS = {
    1: 1.5,  # 概念层加权，优先返回
    2: 2.0,  # API 层最高权重
    3: 0.2,  # 实现层低权重
}
```

### 使用示例

```python
from core.layer import LayerAnnotator

annotator = LayerAnnotator()
annotator.annotate(G)

# 查看层级分布
counts = {1: 0, 2: 0, 3: 0}
for node, data in G.nodes(data=True):
    counts[data.get("layer", 3)] += 1
print(f"L1: {counts[1]}, L2: {counts[2]}, L3: {counts[3]}")
```

---

## 六、models.py — 数据模型

### 功能

定义核心数据结构，用于查询结果、反馈记录等。

### 数据模型

```python
@dataclass
class SearchResult:
    """搜索结果"""
    query: str                  # 查询字符串
    paths: list[str]            # 结果路径列表
    nodes: list[NodeInfo]       # 结果节点列表
    latency_ms: float           # 耗时（毫秒）
    graph_used: str             # 使用的图谱名称
    total_nodes: int            # 图谱总节点数
    total_edges: int            # 图谱总边数


@dataclass
class TraverseResult:
    """图遍历结果"""
    query: str                  # 查询字符串
    mode: str                   # bfs/dfs
    start_nodes: list[str]      # 起点节点
    depth: int                  # 遍历深度
    
    nodes: list[dict]           # 遍历到的节点
    edges: list[dict]           # 遍历到的边
    
    token_budget: int           # token 上限
    actual_tokens: int          # 实际 token 数
    subgraph_json: str          # 子图 JSON


@dataclass
class NodeInfo:
    """节点信息"""
    id: str                     # 节点 ID
    label: str                  # 节点标签
    source_file: str            # 来源文件
    source_location: str        # 来源位置
    layer: int                  # 层级（1/2/3）
    degree: int                 # 连接数
    community: int              # 社区 ID


@dataclass
class QueryRecord:
    """查询记录（用于反馈）"""
    query: str                  # 查询字符串
    timestamp: str              # 时间戳
    graph_used: str             # 使用的图谱
    layer_filter: list[int]     # 层级过滤
    result_count: int           # 结果数
    latency_ms: float           # 耗时
    top_paths: list[str]        # Top 结果
    satisfied: bool             # 是否满意


@dataclass
class FeedbackRecord:
    """反馈记录"""
    query: str                  # 查询字符串
    satisfied: bool             # 满意度
    timestamp: str              # 时间戳
    suggestion: str             # 建议
```

---

## 七、设计原则

### 1. 搜索 vs 遍历分离

```
搜索（search.py）      遍历（traversal.py）
    ↓                      ↓
打分排序              BFS/DFS 图遍历
    ↓                      ↓
定位文档              发现关联
    ↓                      ↓
"List 在哪"          "List 和 Button 有什么关系"
```

### 2. 分层优先级

```
L1 概念层 × 1.5  →  架构探索优先
L2 API 层 × 2.0  →  API 查找最高
L3 实现层 × 0.2  →  实现细节兜底
```

### 3. 三层路由策略

```
第一层：前缀匹配 → 最高优先级
第二层：域名权重 → 解决关键词冲突
第三层：关键词模糊 → 兜底
默认：merged → 全量图谱
```

---

## 八、性能指标

| 操作 | 延迟 P50 | 延迟 P95 |
|------|:--------:|:--------:|
| search（merged） | 160ms | 210ms |
| search（subgraph） | 50ms | 80ms |
| traverse（depth=3） | 30ms | 50ms |
| traverse（depth=6） | 80ms | 120ms |
| god_nodes | 20ms | 30ms |
| surprising_connections | 100ms | 150ms |

---

*最后更新: 2026-04-29*