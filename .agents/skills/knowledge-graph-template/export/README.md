# export/ — 导出模块

本目录包含图谱导出和可视化功能。

---

## 目录结构

```
export/
├── json.py       # JSON 导出（标准格式）
├── html.py       # HTML 可视化（vis.js）
├── report.py     # GRAPH_REPORT.md 生成
└── __init__.py   # 模块导出
```

---

## 一、json.py — JSON 导出

### 功能

将 NetworkX 图谱导出为标准 JSON 格式。

### 实现原理

```python
def save_graph(G: nx.Graph, output_path: str) -> None:
    """
    导出 JSON 流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 提取节点                                  │
    │    nodes = []                               │
    │    for node_id, data in G.nodes(data=True): │
    │        nodes.append({                       │
    │            "id": node_id,                   │
    │            "label": data.get("label"),      │
    │            "source_file": data.get("source_file"), │
    │            "source_location": data.get("source_location"), │
    │            "layer": data.get("layer"),      │
    │            "community": data.get("community"), │
    │            "degree": G.degree(node_id),     │
    │        })                                   │
    │                                             │
    │ 2. 提取边                                    │
    │    links = []                               │
    │    for u, v, data in G.edges(data=True):    │
    │        links.append({                       │
    │            "source": u,                     │
    │            "target": v,                     │
    │            "relation": data.get("relation"), │
    │            "confidence": data.get("confidence"), │
    │        })                                   │
    │                                             │
    │ 3. 构造 JSON                                 │
    │    graph_json = {                           │
    │        "nodes": nodes,                      │
    │        "links": links,                      │
    │        "metadata": {                        │
    │            "node_count": len(nodes),        │
    │            "edge_count": len(links),        │
    │            "export_time": datetime.now().isoformat(), │
    │        }                                    │
    │    }                                        │
    │                                             │
    │ 4. 写入文件                                  │
    │    Path(output_path).write_text(           │
    │        json.dumps(graph_json, ensure_ascii=False, indent=2) │
    │    )                                        │
    └─────────────────────────────────────────────┘
    """
```

### JSON 格式规范

```json
{
  "nodes": [
    {
      "id": "std.collection.HashMap",
      "label": "HashMap",
      "source_file": "docs/std/collection.md",
      "source_location": "docs/std/collection.md:45",
      "layer": 2,
      "community": 5,
      "degree": 42
    }
  ],
  "links": [
    {
      "source": "std.collection.HashMap",
      "target": "std.collection.Map",
      "relation": "implements",
      "confidence": "EXTRACTED"
    }
  ],
  "metadata": {
    "node_count": 48587,
    "edge_count": 131342,
    "export_time": "2026-04-29T10:30:00"
  }
}
```

### 使用示例

```python
from export.json import save_graph, load_graph
import networkx as nx

# 导出图谱
save_graph(G, "output/graph.json")

# 加载图谱
G = load_graph("output/graph.json")
print(f"节点数: {G.number_of_nodes()}")
```

---

## 二、html.py — HTML 可视化

### 功能

生成交互式 HTML 可视化（vis.js）。

### 实现原理

```python
def export_html(G: nx.Graph, output_path: str, max_nodes: int = 1000) -> None:
    """
    导出 HTML 流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 节点数量限制                              │
    │    if G.number_of_nodes() > max_nodes:     │
    │        G = _sample_graph(G, max_nodes)    │
    │                                             │
    │ 2. 生成 vis.js 数据                         │
    │    nodes = []                               │
    │    for node_id, data in G.nodes(data=True): │
    │        nodes.append({                      │
    │            "id": node_id,                  │
    │            "label": data.get("label", node_id), │
    │            "group": data.get("community", 0), │
    │            "value": G.degree(node_id),     │
    │            "title": _tooltip(data),        │
    │        })                                   │
    │                                             │
    │ 3. 生成 HTML 模板                           │
    │    html = f'''                              │
    │    <!DOCTYPE html>                          │
    │    <html>                                   │
    │    <head>                                   │
    │        <title>Knowledge Graph</title>      │
    │        <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script> │
    │    </head>                                  │
    │    <body>                                   │
    │        <div id="network"></div>            │
    │        <script>                             │
    │            var nodes = new vis.DataSet({nodes_json}); │
    │            var edges = new vis.DataSet({edges_json}); │
    │            var network = new vis.Network( │
    │                document.getElementById('network'), │
    │                {{nodes, edges}},           │
    │                {{physics: {{stabilization: true}}}} │
    │            );                              │
    │        </script>                            │
    │    </body>                                  │
    │    </html>                                  │
    │    '''                                      │
    │                                             │
    │ 4. 写入文件                                  │
    │    Path(output_path).write_text(html)      │
    └─────────────────────────────────────────────┘
    """
```

### 节点采样策略

```python
def _sample_graph(G: nx.Graph, max_nodes: int) -> nx.Graph:
    """
    采样策略：
    
    1. 优先保留高 degree 节点（god nodes）
    2. 优先保留 L1/L2 层节点（概念/API）
    3. 保持社区代表性
    
    流程：
    - 按 degree 排序
    - 按 layer 加权（L1=3x, L2=2x, L3=1x）
    - 选择 Top max_nodes
    - 保留这些节点之间的边
    """
```

### 可视化特性

| 特性 | 实现 |
|------|------|
| 节点大小 | 按 degree 缩放 |
| 节点颜色 | 按社区分组 |
| 节点提示 | 显示完整信息 |
| 边样式 | 实线（EXTRACTED）/ 虚线（INFERRED） |
| 物理模拟 | 力导向布局 |

### 使用示例

```python
from export.html import export_html

# 导出 HTML（限制 1000 节点）
export_html(G, "output/graph.html", max_nodes=1000)

# 导出完整图谱（48K 节点可能卡顿）
export_html(G, "output/graph_full.html", max_nodes=50000)
```

---

## 三、report.py — GRAPH_REPORT.md 生成

### 功能

生成图谱分析报告（Markdown 格式）。

### 实现原理

```python
def generate_report(G: nx.Graph, output_dir: str) -> str:
    """
    生成报告流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 基础统计                                  │
    │    stats = basic_stats(G)                    │
    │    layers = layer_distribution(G)          │
    │                                             │
    │ 2. 分析                                      │
    │    gods = god_nodes(G, top_k=20)           │
    │    surprises = surprising_connections(G, top_k=10) │
    │    questions = suggest_questions(G, top_k=30) │
    │                                             │
    │ 3. 生成 Markdown                            │
    │    md = f'''                                │
    │    # 知识图谱分析报告                         │
    │                                             │
    │    ## 1. 基础统计                            │
    │    - 节点数: {stats['nodes']}               │
    │    - 边数: {stats['edges']}                 │
    │    - 密度: {stats['density']:.4f}          │
    │    - 平均度: {stats['avg_degree']:.2f}      │
    │    - 孤立节点: {stats['isolates']}          │
    │                                             │
    │    ## 2. 层级分布                            │
    │    - L1（概念层）: {layers[1]} 节点         │
    │    - L2（API 层）: {layers[2]} 节点         │
    │    - L3（实现层）: {layers[3]} 节点         │
    │                                             │
    │    ## 3. 关键节点（Top 20）                  │
    │    | 节点 | 标签 | 连接数 |                 │
    │    |------|------|--------|                │
    │    ...                                       │
    │                                             │
    │    ## 4. 意外连接（Top 10）                  │
    │    | 源节点 → 目标节点 | 关系 | 社区 |     │
    │    |---------------------|------|------|   │
    │    ...                                       │
    │                                             │
    │    ## 5. 探索性问题                          │
    │    - 如何使用 {label}？                     │
    │    - {label} 有哪些应用场景？               │
    │    ...                                       │
    │    '''                                       │
    │                                             │
    │ 4. 写入文件                                  │
    │    report_path = Path(output_dir) / "GRAPH_REPORT.md" │
    │    report_path.write_text(md)               │
    │                                             │
    │ 5. 返回路径                                  │
    │    return str(report_path)                  │
    └─────────────────────────────────────────────┘
    """
```

### 报告内容结构

```markdown
# 知识图谱分析报告

## 1. 基础统计
- 节点数: 48,587
- 边数: 131,342
- 密度: 0.0001
- 平均度: 5.4
- 孤立节点: 123

## 2. 层级分布
- L1（概念层）: 1,410 节点 (2.9%)
- L2（API 层）: 2,374 节点 (4.9%)
- L3（实现层）: 44,803 节点 (92.2%)

## 3. 关键节点（Top 20）
| 节点 | 标签 | 连接数 |
|------|------|--------|
| std.collection.HashMap | HashMap | 142 |
| std.net.HttpClient | HttpClient | 98 |
| ... | ... | ... |

## 4. 意外连接（Top 10）
| 源节点 → 目标节点 | 关系 | 社区 |
|-------------------|------|------|
| UIAbility → HttpClient | uses | 3 → 7 |
| ... | ... | ... |

## 5. 探索性问题
- 如何使用 HashMap？
- HashMap 有哪些应用场景？
- HashMap 和哪些模块相关？
...
```

### 使用示例

```python
from export.report import generate_report

# 生成报告
report_path = generate_report(G, "analysis-out")
print(f"报告已生成: {report_path}")
```

---

## 四、导出工作流

### 典型导出流程

```python
# 1. 加载图谱
from builders.build import load_graph
G = load_graph("data/merged/graph_layered.json")

# 2. 导出 JSON
from export.json import save_graph
save_graph(G, "output/graph.json")

# 3. 导出 HTML
from export.html import export_html
export_html(G, "output/graph.html", max_nodes=1000)

# 4. 生成报告
from export.report import generate_report
generate_report(G, "output")
```

### CLI 命令

```bash
# 导出 JSON
python cli.py export json --output output/graph.json

# 导出 HTML
python cli.py export html --output output/graph.html --max-nodes 1000

# 生成报告
python cli.py export report --output output/
```

---

## 五、导出格式对比

| 格式 | 用途 | 大小 | 可读性 |
|------|------|:----:|:------:|
| JSON | 数据交换、加载图谱 | 大 | 中 |
| HTML | 浏览器可视化 | 大 | 高 |
| GRAPH_REPORT.md | 文本报告 | 小 | 高 |

---

## 六、性能指标

| 操作 | 48K 节点图谱 |
|------|:------------:|
| save_graph（JSON） | 500ms |
| load_graph（JSON） | 300ms |
| export_html（1000 节点） | 200ms |
| generate_report | 500ms |

---

*最后更新: 2026-04-29*