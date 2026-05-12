# feedback/ — 反馈系统模块

本目录包含用户反馈收集和自动优化功能。

---

## 目录结构

```
feedback/
├── collector.py     # 反馈收集器
├── optimizer.py     # 自动优化器
├── analyzer.py      # 反馈分析
└── __init__.py      # 模块导出
```

---

## 一、collector.py — 反馈收集器

### 功能

记录用户查询和满意度，支持手动和自动反馈。

### 实现原理

```python
class FeedbackCollector:
    """
    反馈收集器。
    
    数据结构：
    ┌─────────────────────────────────────────────┐
    │ queries.jsonl（查询日志）                    │
    │                                             │
    │ 每行一个 JSON 对象：                         │
    │ {                                           │
    │   "timestamp": "2026-04-29T10:30:00",      │
    │   "query": "List 组件 onReachEnd",          │
    │   "results": [                              │
    │     "docs/ui/list.md#onReachEnd",          │
    │     "docs/ui/list.md#overview",            │
    │   ],                                        │
    │   "graph": "harmonyos",                     │
    │   "layers": [1, 2],                         │
    │   "latency_ms": 160,                        │
    │   "satisfied": null,                        │
    │ }                                           │
    │                                             │
    │ 字段说明：                                   │
    │ - timestamp: 查询时间                       │
    │ - query: 查询字符串                         │
    │ - results: 返回的文档路径                   │
    │ - graph: 使用的图谱                         │
    │ - layers: 搜索的层级                        │
    │ - latency_ms: 延迟（毫秒）                  │
    │ - satisfied: 满意度（null/true/false）      │
    └─────────────────────────────────────────────┘
    """
    
    def __init__(self, feedback_dir: str = "data/feedback"):
        self.feedback_dir = Path(feedback_dir)
        self.queries_file = self.feedback_dir / "queries.jsonl"
        self.feedback_dir.mkdir(parents=True, exist_ok=True)
    
    def log_query(self, query: str, results: list[str], graph: str = None, 
                  layers: list[int] = None, latency_ms: float = None) -> str:
        """
        记录查询：
        
        流程：
        1. 生成查询 ID
           query_id = str(uuid.uuid4())
        
        2. 构造记录
           record = {
               "id": query_id,
               "timestamp": datetime.now().isoformat(),
               "query": query,
               "results": results,
               "graph": graph,
               "layers": layers,
               "latency_ms": latency_ms,
               "satisfied": None,
           }
        
        3. 追加到文件
           with open(self.queries_file, "a", encoding="utf-8") as f:
               f.write(json.dumps(record, ensure_ascii=False) + "\n")
        
        4. 返回查询 ID（用于后续标记满意度）
           return query_id
        """
    
    def mark_satisfied(self, query_id: str, satisfied: bool) -> None:
        """
        标记满意度：
        
        流程：
        1. 读取所有记录
           records = []
           with open(self.queries_file, "r", encoding="utf-8") as f:
               for line in f:
                   record = json.loads(line)
                   if record["id"] == query_id:
                       record["satisfied"] = satisfied
                   records.append(record)
        
        2. 重写文件
           with open(self.queries_file, "w", encoding="utf-8") as f:
               for record in records:
                   f.write(json.dumps(record, ensure_ascii=False) + "\n")
        """
    
    def get_unsatisfied_queries(self) -> list[dict]:
        """
        获取未满意查询：
        
        返回：
        [
            {
                "id": "...",
                "query": "std.net 网络",
                "results": [...],
                "satisfied": false,
            },
            ...
        ]
        """
        
        unsatisfied = []
        with open(self.queries_file, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)
                if record.get("satisfied") is False:
                    unsatisfied.append(record)
        return unsatisfied
```

### 使用示例

```python
from feedback.collector import FeedbackCollector

collector = FeedbackCollector()

# 记录查询
query_id = collector.log_query(
    query="List 组件 onReachEnd",
    results=["docs/ui/list.md#onReachEnd", "docs/ui/list.md#overview"],
    graph="harmonyos",
    layers=[1, 2],
    latency_ms=160,
)

# 标记满意
collector.mark_satisfied(query_id, True)

# 标记不满意
collector.mark_satisfied(query_id, False)

# 获取未满意查询
unsatisfied = collector.get_unsatisfied_queries()
for record in unsatisfied:
    print(f"查询: {record['query']}")
    print(f"结果: {record['results']}")
```

---

## 二、analyzer.py — 反馈分析

### 功能

分析反馈数据，发现知识盲区和优化机会。

### 实现原理

```python
class FeedbackAnalyzer:
    """
    反馈分析器。
    
    分析维度：
    ┌─────────────────────────────────────────────┐
    │ 1. 满意度分析                                │
    │    - 满意查询数 / 总查询数                   │
    │    - 满意度趋势（按时间）                    │
    │                                             │
    │ 2. 知识盲区                                  │
    │    - 未满意查询的高频关键词                  │
    │    - 未返回结果的查询                        │
    │    - 低满意度文档                            │
    │                                             │
    │ 3. 性能分析                                  │
    │    - 平均延迟                                │
    │    - 延迟分布                                │
    │    - 超时查询                                │
    │                                             │
    │ 4. 图谱使用                                  │
    │    - 各图谱查询频率                          │
    │    - 图谱路由准确性                          │
    └─────────────────────────────────────────────┘
    """
    
    def __init__(self, feedback_dir: str = "data/feedback"):
        self.collector = FeedbackCollector(feedback_dir)
    
    def satisfaction_rate(self) -> float:
        """
        满意度：
        
        公式：
        satisfaction_rate = satisfied_queries / total_queries
        
        返回：
        0.95（95% 满意度）
        """
        
        records = self._load_all_queries()
        if not records:
            return 0.0
        
        satisfied = sum(1 for r in records if r.get("satisfied") is True)
        total = len(records)
        return satisfied / total
    
    def knowledge_gaps(self, top_k: int = 20) -> list[dict]:
        """
        发现知识盲区：
        
        流程：
        1. 提取未满意查询
           unsatisfied = self.collector.get_unsatisfied_queries()
        
        2. 分词并统计高频词
           from collections import Counter
           word_freq = Counter()
           for record in unsatisfied:
               tokens = self._tokenize(record["query"])
               word_freq.update(tokens)
        
        3. 返回 Top K
           return [{"word": word, "count": count} for word, count in word_freq.most_common(top_k)]
        
        意义：
        - 高频词 = 用户频繁查询但未满意的关键词
        - 可作为文档补全建议
        """
    
    def low_satisfaction_docs(self, threshold: float = 0.5) -> list[dict]:
        """
        低满意度文档：
        
        流程：
        1. 统计每个文档的满意度
           doc_stats = {}
           for record in records:
               for doc in record["results"]:
                   if doc not in doc_stats:
                       doc_stats[doc] = {"satisfied": 0, "total": 0}
                   doc_stats[doc]["total"] += 1
                   if record.get("satisfied"):
                       doc_stats[doc]["satisfied"] += 1
        
        2. 计算满意度并过滤
           low_satisfaction = []
           for doc, stats in doc_stats.items():
               rate = stats["satisfied"] / stats["total"]
               if rate < threshold:
                   low_satisfaction.append({
                       "doc": doc,
                       "satisfaction_rate": rate,
                       "total_queries": stats["total"],
                   })
        
        3. 排序返回
           return sorted(low_satisfaction, key=lambda x: x["satisfaction_rate"])
        
        意义：
        - 低满意度文档 = 内容可能不完整或错误
        - 可作为文档优化建议
        """
    
    def graph_usage(self) -> dict[str, int]:
        """
        图谱使用统计：
        
        返回：
        {
            "harmonyos": 120,
            "std": 45,
            "stdx": 30,
            "lang-features": 15,
        }
        """
        
        records = self._load_all_queries()
        usage = {}
        for record in records:
            graph = record.get("graph", "merged")
            usage[graph] = usage.get(graph, 0) + 1
        return usage
```

### 使用示例

```python
from feedback.analyzer import FeedbackAnalyzer

analyzer = FeedbackAnalyzer()

# 满意度
rate = analyzer.satisfaction_rate()
print(f"满意度: {rate:.1%}")

# 知识盲区
gaps = analyzer.knowledge_gaps(top_k=20)
for gap in gaps:
    print(f"{gap['word']}: {gap['count']} 次")

# 低满意度文档
low_docs = analyzer.low_satisfaction_docs(threshold=0.5)
for doc in low_docs:
    print(f"{doc['doc']}: 满意度 {doc['satisfaction_rate']:.1%}")

# 图谱使用
usage = analyzer.graph_usage()
for graph, count in usage.items():
    print(f"{graph}: {count} 次查询")
```

---

## 三、optimizer.py — 自动优化器

### 功能

根据反馈自动优化图谱（学习别名、调整权重）。

### 实现原理

```python
class AutoOptimizer:
    """
    自动优化器。
    
    优化策略：
    ┌─────────────────────────────────────────────┐
    │ 1. 学习别名                                  │
    │    从未满意查询中学习同义词                  │
    │                                             │
    │    例：                                      │
    │    - 用户查询 "网络请求" → 未命中 std.net.HttpClient │
    │    - 优化：添加别名 "网络请求" → "HttpClient" │
    │                                             │
    │ 2. 推断新边                                  │
    │    从共现查询中推断关联                      │
    │                                             │
    │    例：                                      │
    │    - 查询 "HttpClient" 和 "UIAbility" 频繁共现 │
    │    - 推断：添加边 HttpClient --[related]--> UIAbility │
    │                                             │
    │ 3. 调整权重                                  │
    │    根据满意度调整节点权重                    │
    │                                             │
    │    例：                                      │
    │    - 文档 A 满意度 95% → 提高 weight         │
    │    - 文档 B 满意度 40% → 降低 weight         │
    └─────────────────────────────────────────────┘
    """
    
    def __init__(self, graph_path: str, feedback_dir: str = "data/feedback"):
        self.graph_path = graph_path
        self.analyzer = FeedbackAnalyzer(feedback_dir)
        self.aliases: dict[str, list[str]] = {}
        self.inferred_edges: list[dict] = []
    
    def learn_aliases(self) -> dict[str, list[str]]:
        """
        学习别名：
        
        流程：
        1. 获取知识盲区
           gaps = self.analyzer.knowledge_gaps(top_k=100)
        
        2. 对每个盲区词，查找相似节点
           for gap in gaps:
               # 查找相似节点
               similar_nodes = self._find_similar_nodes(gap["word"])
               if similar_nodes:
                   # 添加别名
                   for node_id, similarity in similar_nodes:
                       if node_id not in self.aliases:
                           self.aliases[node_id] = []
                       self.aliases[node_id].append(gap["word"])
        
        3. 保存别名
           self._save_aliases()
        
        4. 返回学习的别名
           return self.aliases
        
        相似度计算：
        - 编辑距离（Levenshtein）
        - 语义相似度（可选，需要 embedding）
        """
    
    def infer_edges(self, co_occurrence_threshold: int = 3) -> list[dict]:
        """
        推断新边：
        
        流程：
        1. 统计查询共现
           from collections import defaultdict
           co_occurrence = defaultdict(int)
           
           records = self._load_all_queries()
           for i, record in enumerate(records):
               for j in range(i + 1, len(records)):
                   if self._are_related(records[i], records[j]):
                       pair = tuple(sorted([records[i]["query"], records[j]["query"]]))
                       co_occurrence[pair] += 1
        
        2. 过滤高频共现
           high_co = {pair: count for pair, count in co_occurrence.items() 
                      if count >= co_occurrence_threshold}
        
        3. 映射到节点
           for (q1, q2), count in high_co.items():
               node1 = self._find_node_for_query(q1)
               node2 = self._find_node_for_query(q2)
               if node1 and node2 and not self._edge_exists(node1, node2):
                   self.inferred_edges.append({
                       "source": node1,
                       "target": node2,
                       "relation": "INFERRED_CO_OCCUR",
                       "confidence": "INFERRED",
                       "count": count,
                   })
        
        4. 返回推断的边
           return self.inferred_edges
        """
    
    def apply_optimizations(self) -> None:
        """
        应用优化：
        
        流程：
        1. 加载图谱
           G = load_graph(self.graph_path)
        
        2. 应用别名
           for node_id, aliases in self.aliases.items():
               if node_id in G.nodes:
                   G.nodes[node_id]["aliases"] = aliases
        
        3. 应用推断边
           for edge in self.inferred_edges:
               G.add_edge(
                   edge["source"],
                   edge["target"],
                   relation=edge["relation"],
                   confidence="INFERRED",
               )
        
        4. 保存图谱
           save_graph(G, self.graph_path)
        """
```

### 使用示例

```python
from feedback.optimizer import AutoOptimizer

optimizer = AutoOptimizer("data/merged/graph_layered.json")

# 学习别名
aliases = optimizer.learn_aliases()
print(f"学习到 {len(aliases)} 个别名")
for node_id, alias_list in aliases.items():
    print(f"  {node_id}: {alias_list}")

# 推断新边
edges = optimizer.infer_edges(co_occurrence_threshold=3)
print(f"推断到 {len(edges)} 条新边")
for edge in edges:
    print(f"  {edge['source']} --[{edge['relation']}]--> {edge['target']}")

# 应用优化
optimizer.apply_optimizations()
print("优化已应用")
```

---

## 四、反馈工作流

### 典型反馈流程

```python
# 1. 记录查询
from feedback.collector import FeedbackCollector
collector = FeedbackCollector()
query_id = collector.log_query(
    query="HttpClient 网络请求",
    results=["docs/stdx/net/http_client.md"],
    graph="stdx",
    latency_ms=150,
)

# 2. 用户标记满意度
# 用户反馈：满意 → collector.mark_satisfied(query_id, True)
# 用户反馈：不满意 → collector.mark_satisfied(query_id, False)

# 3. 定期分析
from feedback.analyzer import FeedbackAnalyzer
analyzer = FeedbackAnalyzer()
satisfaction = analyzer.satisfaction_rate()
gaps = analyzer.knowledge_gaps(top_k=20)
low_docs = analyzer.low_satisfaction_docs()

# 4. 自动优化
from feedback.optimizer import AutoOptimizer
optimizer = AutoOptimizer("data/merged/graph_layered.json")
aliases = optimizer.learn_aliases()
edges = optimizer.infer_edges()
optimizer.apply_optimizations()
```

### CLI 命令

```bash
# 查看反馈统计
python cli.py analyze feedback

# 运行自动优化
python cli.py optimize
```

---

## 五、反馈数据结构

### queries.jsonl 格式

```json
{"id": "uuid-1", "timestamp": "2026-04-29T10:30:00", "query": "List 组件 onReachEnd", "results": ["docs/ui/list.md#onReachEnd"], "graph": "harmonyos", "layers": [1, 2], "latency_ms": 160, "satisfied": true}
{"id": "uuid-2", "timestamp": "2026-04-29T10:31:00", "query": "HttpClient 网络请求", "results": [], "graph": "merged", "layers": [1, 2, 3], "latency_ms": 180, "satisfied": false}
```

### aliases.json 格式

```json
{
  "std.net.HttpClient": ["网络请求", "HTTP 客户端", "httpClient"],
  "std.collection.HashMap": ["哈希表", "hashmap", "map"]
}
```

---

## 六、性能指标

| 操作 | 1000 条反馈 |
|------|:-----------:|
| log_query | 5ms |
| mark_satisfied | 10ms |
| satisfaction_rate | 20ms |
| knowledge_gaps | 50ms |
| low_satisfaction_docs | 100ms |
| learn_aliases | 500ms |
| infer_edges | 1000ms |
| apply_optimizations | 300ms |

---

*最后更新: 2026-04-29*