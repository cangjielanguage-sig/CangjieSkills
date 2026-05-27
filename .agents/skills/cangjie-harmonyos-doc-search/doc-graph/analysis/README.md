# analysis/ — 图谱分析模块

本目录包含图谱分析和洞察发现功能。

---

## 目录结构

```
analysis/
├── analyze.py    # 核心分析函数
├── metrics.py    # 图谱度量指标
└── __init__.py   # 模块导出
```

---

## 一、analyze.py — 核心分析函数

### 功能

发现图谱中的关键节点、意外连接、问题建议。

### 实现原理

```python
def god_nodes(G: nx.Graph, top_k: int = 20) -> list[tuple[str, dict, int]]:
    """
    发现关键节点（高连接度）：
    
    流程：
    ┌─────────────────────────────────────────────┐
    │ 1. 计算所有节点 degree                       │
    │    degrees = [(n, d, G.degree(n))          │
    │               for n, d in G.nodes(data=True)]│
    │                                             │
    │ 2. 排序                                     │
    │    degrees.sort(key=lambda x: x[2], reverse=True) │
    │                                             │
    │ 3. 返回 Top K                               │
    │    return degrees[:top_k]                   │
    │                                             │
    │ 意义：                                      │
    │ - 高 degree 节点 = 核心 API/概念            │
    │ - 常作为查询起点或中转点                    │
    │ - 可作为推荐入口                            │
    └─────────────────────────────────────────────┘
    """
```

```python
def surprising_connections(G: nx.Graph, top_k: int = 10) -> list[dict]:
    """
    发现意外连接（跨越社区）：
    
    流程：
    ┌─────────────────────────────────────────────┐
    │ 1. 获取社区分配                              │
    │    communities = {}                         │
    │    for node, data in G.nodes(data=True):   │
    │        cid = data.get("community", -1)     │
    │        communities[node] = cid              │
    │                                             │
    │ 2. 遍历所有边                                │
    │    surprises = []                           │
    │    for u, v, data in G.edges(data=True):   │
    │        if communities.get(u) != communities.get(v): │
    │            # 跨社区边                        │
    │            surprises.append({              │
    │                "source": u,                 │
    │                "target": v,                │
    │                "relation": data.get("relation"), │
    │                "source_community": communities[u], │
    │                "target_community": communities[v], │
    │            })                              │
    │                                             │
    │ 3. 排序（按节点 degree 乘积）               │
    │    surprises.sort(                         │
    │        key=lambda x: G.degree(x["source"]) * G.degree(x["target"]), │
    │        reverse=True                        │
    │    )                                       │
    │                                             │
    │ 4. 返回 Top K                               │
    │    return surprises[:top_k]                │
    │                                             │
    │ 意义：                                      │
    │ - 跨社区边 = 隐藏的关联                     │
    │ - 常对应业务逻辑或技术依赖                  │
    │ - 可作为知识补全建议                        │
    └─────────────────────────────────────────────┘
    """
```

```python
def suggest_questions(G: nx.Graph, top_k: int = 20) -> list[str]:
    """
    生成探索性问题：
    
    流程：
    ┌─────────────────────────────────────────────┐
    │ 1. 获取 god nodes                           │
    │    gods = god_nodes(G, top_k=50)           │
    │                                             │
    │ 2. 生成问题模板                              │
    │    templates = [                           │
    │        "如何使用 {label}？",                │
    │        "{label} 有哪些应用场景？",          │
    │        "{label} 和哪些模块相关？",          │
    │        "{label} 的最佳实践是什么？",        │
    │        "如何扩展 {label}？",                │
    │    ]                                       │
    │                                             │
    │ 3. 生成问题                                  │
    │    questions = []                          │
    │    for node_id, data, degree in gods:      │
    │        label = data.get("label", node_id)  │
    │        for tmpl in templates:              │
    │            questions.append(tmpl.format(label=label)) │
    │                                             │
    │ 4. 去重 + 截断                               │
    │    questions = list(dict.fromkeys(questions)) │
    │    return questions[:top_k]                │
    │                                             │
    │ 意义：                                      │
    │ - 引导用户探索关键概念                      │
    │ - 可作为 FAQ 或评测集种子                  │
    │ - 覆盖高价值 API                            │
    └─────────────────────────────────────────────┘
    """
```

### 使用示例

```python
from analysis.analyze import god_nodes, surprising_connections, suggest_questions
import networkx as nx

# 加载图谱
G = nx.node_link_graph(json.loads(Path("graph.json").read_text()))

# 发现关键节点
gods = god_nodes(G, top_k=20)
for node_id, data, degree in gods:
    print(f"{data.get('label', node_id)}: degree={degree}")

# 发现意外连接
surprises = surprising_connections(G, top_k=10)
for s in surprises:
    print(f"{s['source']} ({s['source_community']}) --[{s['relation']}]--> {s['target']} ({s['target_community']})")

# 生成问题
questions = suggest_questions(G, top_k=20)
for q in questions:
    print(f"- {q}")
```

---

## 二、metrics.py — 图谱度量指标

### 功能

计算图谱统计指标和质量指标。

### 实现原理

```python
def basic_stats(G: nx.Graph) -> dict:
    """
    基础统计：
    
    返回：
    {
        "nodes": 节点数,
        "edges": 边数,
        "density": 密度,
        "avg_degree": 平均度,
        "max_degree": 最大度,
        "isolates": 孤立节点数,
    }
    """
    
    stats = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": nx.density(G),
        "avg_degree": sum(dict(G.degree()).values()) / G.number_of_nodes(),
        "max_degree": max(dict(G.degree()).values()),
        "isolates": len(list(nx.isolates(G))),
    }
    return stats
```

```python
def layer_distribution(G: nx.Graph) -> dict[int, int]:
    """
    层级分布：
    
    返回：
    {
        1: L1 节点数,
        2: L2 节点数,
        3: L3 节点数,
    }
    """
    
    dist = {1: 0, 2: 0, 3: 0}
    for node, data in G.nodes(data=True):
        layer = data.get("layer", 3)
        dist[layer] = dist.get(layer, 0) + 1
    return dist
```

```python
def community_stats(G: nx.Graph) -> dict:
    """
    社区统计：
    
    返回：
    {
        "num_communities": 社区数,
        "largest_community": 最大社区节点数,
        "smallest_community": 最小社区节点数,
        "avg_community_size": 平均社区大小,
        "cohension_scores": {community_id: cohesion, ...},
    }
    """
    
    # 1. 统计社区
    communities = {}
    for node, data in G.nodes(data=True):
        cid = data.get("community", -1)
        communities[cid] = communities.get(cid, 0) + 1
    
    # 2. 计算凝聚力
    from builders.cluster import cohesion_score
    cohesion_scores = {}
    for cid, nodes in communities.items():
        cohesion_scores[cid] = cohesion_score(G, nodes)
    
    return {
        "num_communities": len(communities),
        "largest_community": max(communities.values()),
        "smallest_community": min(communities.values()),
        "avg_community_size": sum(communities.values()) / len(communities),
        "cohesion_scores": cohesion_scores,
    }
```

```python
def edge_confidence_distribution(G: nx.Graph) -> dict[str, int]:
    """
    边置信度分布：
    
    返回：
    {
        "EXTRACTED": 提取边数,
        "INFERRED": 推断边数,
        "AMBIGUOUS": 模糊边数,
    }
    """
    
    dist = {"EXTRACTED": 0, "INFERRED": 0, "AMBIGUOUS": 0}
    for u, v, data in G.edges(data=True):
        conf = data.get("confidence", "EXTRACTED")
        dist[conf] = dist.get(conf, 0) + 1
    return dist
```

### 使用示例

```python
from analysis.metrics import basic_stats, layer_distribution, community_stats, edge_confidence_distribution

# 基础统计
stats = basic_stats(G)
print(f"节点: {stats['nodes']}, 边: {stats['edges']}, 密度: {stats['density']:.4f}")

# 层级分布
layers = layer_distribution(G)
print(f"L1: {layers[1]}, L2: {layers[2]}, L3: {layers[3]}")

# 社区统计
comm_stats = community_stats(G)
print(f"社区数: {comm_stats['num_communities']}")
print(f"最大社区: {comm_stats['largest_community']} 节点")

# 边置信度分布
conf_dist = edge_confidence_distribution(G)
print(f"提取: {conf_dist['EXTRACTED']}, 推断: {conf_dist['INFERRED']}")
```

---

## 三、分析工作流

### 典型分析流程

```python
# 1. 加载图谱
from builders.build import load_graph
G = load_graph("data/merged/graph_layered.json")

# 2. 基础统计
from analysis.metrics import basic_stats, layer_distribution
stats = basic_stats(G)
layers = layer_distribution(G)

# 3. 发现关键节点
from analysis.analyze import god_nodes
gods = god_nodes(G, top_k=20)

# 4. 发现意外连接
from analysis.analyze import surprising_connections
surprises = surprising_connections(G, top_k=10)

# 5. 生成问题
from analysis.analyze import suggest_questions
questions = suggest_questions(G, top_k=30)

# 6. 导出报告
from export.report import generate_report
generate_report(G, output_dir="analysis-out")
```

### CLI 命令

```bash
# 发现关键节点
python cli.py god-nodes --top 20

# 发现意外连接
python cli.py surprises --top 10

# 生成问题
python cli.py questions --top 30

# 完整统计
python cli.py stats
```

---

## 四、分析结果应用

| 分析结果 | 应用场景 |
|---------|---------|
| god nodes | 推荐入口、文档首页、API 索引 |
| surprising connections | 知识补全、交叉引用、关联推荐 |
| suggest questions | FAQ 生成、评测集种子、用户引导 |
| community stats | 社区健康检查、聚类质量评估 |
| layer distribution | 分层质量检查、L1/L2/L3 比例优化 |
| edge confidence | 数据质量评估、推断边审核 |

---

## 五、性能指标

| 操作 | 48K 节点图谱 |
|------|:------------:|
| basic_stats | 50ms |
| layer_distribution | 100ms |
| community_stats | 200ms |
| god_nodes | 100ms |
| surprising_connections | 300ms |
| suggest_questions | 50ms |

---

*最后更新: 2026-04-29*