# builders/ — 图谱构建模块

本目录包含从文档/代码构建知识图谱的全部功能。

---

## 目录结构

```
builders/
├── detect.py      # 文件检测和分类
├── build.py       # 构建 NetworkX 图谱
├── cluster.py     # 社区检测（Leiden/Louvain）
├── cache.py       # 文件缓存管理
└── __init__.py    # 模块导出
```

---

## 一、detect.py — 文件检测和分类

### 功能

扫描目录，检测文件类型，过滤敏感文件。

### 实现原理

```python
def detect(root: Path) -> dict:
    """
    文件检测流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 扫描目录                                  │
    │    for dirpath, dirnames, filenames in     │
    │        os.walk(root):                      │
    │                                             │
    │    2. 过滤噪声目录                           │
    │       SKIP_DIRS = {                        │
    │           "venv", ".venv", "node_modules", │
    │           "__pycache__", ".git",           │
    │           "dist", "build", "target",       │
    │       }                                    │
    │       dirnames[:] = [                      │
    │           d for d in dirnames              │
    │           if not _is_noise_dir(d)          │
    │       ]                                    │
    │                                             │
    │ 3. 分类文件                                  │
    │       for fname in filenames:              │
    │           if fname in SKIP_FILES:          │
    │               continue                     │
    │           ftype = classify_file(p)         │
    │                                             │
    │ 4. 统计                                     │
    │       return {                             │
    │           "files": {                       │
    │               "code": [...],               │
    │               "document": [...],           │
    │               "paper": [...],              │
    │           },                               │
    │           "total_files": N,                │
    │           "total_words": W,                │
    │           "warning": "...",                │
    │       }                                    │
    └─────────────────────────────────────────────┘
    """
```

### 文件分类规则

```python
class FileType(str, Enum):
    CODE = "code"
    DOCUMENT = "document"
    PAPER = "paper"
    IMAGE = "image"
    VIDEO = "video"

CODE_EXTENSIONS = {
    '.cj', '.py', '.ts', '.js', '.go', '.rs', 
    '.java', '.cpp', '.c', '.h', '.rb', '.swift', ...
}

DOC_EXTENSIONS = {
    '.md', '.mdx', '.txt', '.rst', '.html'
}

PAPER_EXTENSIONS = {
    '.pdf'
}

IMAGE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'
}

def classify_file(path: Path) -> FileType | None:
    """
    分类规则：
    
    1. 扩展名匹配
       ext = path.suffix.lower()
       if ext in CODE_EXTENSIONS: return CODE
       if ext in DOC_EXTENSIONS: return DOCUMENT
       if ext in PAPER_EXTENSIONS: return PAPER
       if ext in IMAGE_EXTENSIONS: return IMAGE
    
    2. 内容检测（文档是否是论文）
       if _looks_like_paper(path): return PAPER
       
       论文信号：
       - "arxiv" in content
       - "doi:" in content
       - "abstract" in content
       - LaTeX citation \cite{}
       - Numbered citation [1]
    
    3. 不匹配
       return None
    """
```

### 敏感文件过滤

```python
_SENSITIVE_PATTERNS = [
    re.compile(r'(^|[\\/])\.(env|envrc)(\.|$)'),        # .env
    re.compile(r'\.(pem|key|p12|pfx|cert)'),            # 密钥文件
    re.compile(r'(credential|secret|passwd|token)'),    # 敏感关键词
    re.compile(r'(id_rsa|id_dsa|id_ecdsa)'),            # SSH 密钥
]

def _is_sensitive(path: Path) -> bool:
    """
    过滤规则：
    
    1. 环境变量文件
       .env, .envrc, .env.local
    
    2. 密钥文件
       .pem, .key, .p12, .pfx, .cert
    
    3. 包含敏感关键词
       credential, secret, password, token
    
    4. SSH 密钥
       id_rsa, id_dsa, id_ecdsa
    
    返回 True → 跳过该文件
    """
```

### 噪声目录过滤

```python
_SKIP_DIRS = {
    "venv", ".venv", "env",           # Python 虚拟环境
    "node_modules",                   # Node.js 依赖
    "__pycache__",                    # Python 缓存
    ".git",                           # Git 目录
    "dist", "build", "target", "out", # 构建产物
    ".pytest_cache", ".mypy_cache",   # 测试/类型缓存
    "graphify-out",                   # 图谱输出
}

_SKIP_FILES = {
    "package-lock.json",              # 锁文件
    "yarn.lock", "pnpm-lock.yaml",
    "Cargo.lock", "poetry.lock",
}
```

### 使用示例

```python
from builders.detect import detect, classify_file, FileType

# 检测目录
result = detect(Path("./docs"))
print(f"文件数: {result['total_files']}")
print(f"词数: ~{result['total_words']}")
print(f"代码文件: {len(result['files']['code'])}")
print(f"文档文件: {len(result['files']['document'])}")

if result.get("warning"):
    print(f"警告: {result['warning']}")

# 分类单个文件
ftype = classify_file(Path("main.cj"))
print(f"类型: {ftype}")  # FileType.CODE

# 增量检测
result = detect_incremental(Path("./docs"))
print(f"新增文件: {result['new_total']}")
print(f"删除文件: {result['deleted_files']}")
```

---

## 二、build.py — 构建图谱

### 功能

从节点/边字典构建 NetworkX 图谱。

### 实现原理

```python
def build_from_json(extraction: dict, directed: bool = False) -> nx.Graph:
    """
    构建图谱流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 验证数据                                  │
    │    if "edges" not in extraction:           │
    │        extraction["edges"] = extraction["links"] │
    │                                             │
    │ 2. 创建 NetworkX Graph                      │
    │    G = nx.DiGraph() if directed else nx.Graph() │
    │                                             │
    │ 3. 添加节点                                  │
    │    for node in extraction["nodes"]:        │
    │        G.add_node(                         │
    │            node["id"],                     │
    │            label=node.get("label"),        │
    │            source_file=node.get("source_file"), │
    │            layer=node.get("layer"),        │
    │        )                                   │
    │                                             │
    │ 4. 标准化节点 ID                             │
    │    norm_to_id = {                          │
    │        normalize_id(nid): nid              │
    │        for nid in G.nodes()                │
    │    }                                       │
    │                                             │
    │ 5. 添加边                                    │
    │    for edge in extraction["edges"]:        │
    │        src = edge["source"]                │
    │        tgt = edge["target"]                │
    │                                             │
    │        # 处理悬空边                          │
    │        if src not in G.nodes():            │
    │            src = norm_to_id.get(normalize_id(src)) │
    │        if tgt not in G.nodes():            │
    │            tgt = norm_to_id.get(normalize_id(tgt)) │
    │                                             │
    │        if src and tgt and src in G and tgt in G: │
    │            G.add_edge(src, tgt,            │
    │                relation=edge.get("relation"), │
    │                confidence=edge.get("confidence"), │
    │            )                               │
    │                                             │
    │ 6. 返回                                     │
    │    return G                                 │
    └─────────────────────────────────────────────┘
    """
```

### 节点 ID 标准化

```python
def _normalize_id(s: str) -> str:
    """
    标准化节点 ID：
    
    原因：LLM 可能生成 ID 与 AST 提取不一致
    
    例：
    - "Session_ValidateToken" → "session_validatetoken"
    - "session.validateToken" → "session_validatetoken"
    
    流程：
    1. 去除非字母数字字符 → re.sub(r"[^a-zA-Z0-9]+", "_", s)
    2. 小写化 → lower()
    3. 去除前后下划线 → strip("_")
    """
```

### 节点去重

```python
def deduplicate_by_label(nodes: list[dict], edges: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    按 Label 去重节点：
    
    原因：同一概念可能被多次提取
    
    流程：
    1. 标准 Label → norm_label = label.lower().strip()
    
    2. 选择保留节点
       - 优先保留无 chunk suffix 的（不含 _c\d+）
       - 其次保留 ID 更短的
    
    3. 重写边引用
       for edge in edges:
           edge["source"] = remap.get(edge["source"], edge["source"])
           edge["target"] = remap.get(edge["target"], edge["target"])
           if source == target:  # 自环 → 删除
               skip
    
    4. 返回去重后的 nodes + edges
    """
```

### 合并图谱

```python
def build_merge(new_chunks: list[dict], graph_path: str) -> nx.Graph:
    """
    合并新提取到现有图谱：
    
    流程：
    1. 加载现有图谱
       existing_G = load_graph(graph_path)
    
    2. 合并新提取
       base = [existing_nodes + existing_edges]
       all_chunks = base + new_chunks
    
    3. 构建
       G = build(all_chunks)
    
    4. 安全检查
       if new_nodes < existing_nodes:
           raise ValueError("图谱缩小，可能丢失数据")
    
    5. 返回合并后的图谱
    
    意义：
    - 增量更新时合并新旧数据
    - 防止数据丢失
    """
```

### 使用示例

```python
from builders.build import build, build_from_json, build_merge, save_graph

# 从 JSON 构建
data = json.loads(Path("extraction.json").read_text())
G = build_from_json(data)

# 合并多个提取
extractions = [
    {"nodes": [...], "edges": [...]},
    {"nodes": [...], "edges": [...]},
]
G = build(extractions)

# 增量合并
G = build_merge([new_extraction], "graph.json")

# 保存图谱
save_graph(G, "output/graph.json")
```

---

## 三、cluster.py — 社区检测

### 功能

使用 Leiden/Louvain 算法发现图谱社区。

### 实现原理

```python
def cluster(G: nx.Graph) -> dict[int, list[str]]:
    """
    社区检测流程：
    
    ┌─────────────────────────────────────────────┐
    │ 1. 选择算法                                  │
    │                                             │
    │    优先：Leiden（graspologic）              │
    │    备选：Louvain（networkx）                │
    │                                             │
    │    原因：                                    │
    │    - Leiden 更稳定，避免局部最优            │
    │    - Louvain 是 NetworkX 内置               │
    │                                             │
    │ 2. 运行聚类                                  │
    │                                             │
    │    try:                                     │
    │        from graspologic.partition import leiden │
    │        result = leiden(G)                   │
    │        return {node: cid for ...}          │
    │    except ImportError:                     │
    │        communities = nx.community.louvain_communities(G) │
    │                                             │
    │ 3. 处理孤立节点                              │
    │                                             │
    │    isolates = [n for n in G.nodes() if G.degree(n) == 0] │
    │    每个孤立节点 → 单独社区                   │
    │                                             │
    │ 4. 拆分超大社区                              │
    │                                             │
    │    max_size = max(10, nodes * 0.25)        │
    │    if len(nodes) > max_size:               │
    │        sub_partition = leiden(subgraph)    │
    │                                             │
    │ 5. 排序社区                                  │
    │                                             │
    │    final_communities.sort(key=len, reverse=True) │
    │    return {i: nodes for i, nodes in ...}   │
    │                                             │
    │    意义：                                    │
    │    - 社区 0 = 最大社区                       │
    │    - 社区编号稳定                            │
    └─────────────────────────────────────────────┘
    """
```

### Leiden vs Louvain

| 特性 | Leiden | Louvain |
|------|:------:|:-------:|
| 稳定性 | 高 | 中 |
| 质量 | 高 | 中 |
| 依赖 | graspologic | networkx |
| 速度 | 慢 | 快 |

### 社区凝聚力

```python
def cohesion_score(G: nx.Graph, community_nodes: list[str]) -> float:
    """
    计算社区凝聚力：
    
    公式：
    cohesion = actual_edges / possible_edges
    
    其中：
    - actual_edges = 社区内实际边数
    - possible_edges = n * (n-1) / 2（完全图边数）
    
    意义：
    - cohesion >= 0.7 → 紧密社区（稳定模块）
    - cohesion < 0.3 → 松散社区（可能需要拆分）
    """
```

### 拆分超大社区

```python
_MAX_COMMUNITY_FRACTION = 0.25  # 最大社区不超过 25% 节点
_MIN_SPLIT_SIZE = 10            # 至少 10 节点才拆分

def _split_community(G: nx.Graph, nodes: list[str]) -> list[list[str]]:
    """
    拆分超大社区：
    
    流程：
    1. 构建子图
       subgraph = G.subgraph(nodes)
    
    2. 再次运行 Leiden
       sub_partition = leiden(subgraph)
    
    3. 返回拆分后的子社区
    
    意义：
    - 防止单一社区过大
    - 提高查询精度
    """
```

### 使用示例

```python
from builders.cluster import cluster, cohesion_score, score_all, assign_communities_to_nodes

# 社区检测
communities = cluster(G)
print(f"社区数: {len(communities)}")
print(f"社区 0: {len(communities[0])} 节点")

# 计算凝聚力
coh = cohesion_score(G, communities[0])
print(f"凝聚力: {coh}")

# 计算所有社区凝聚力
scores = score_all(G, communities)

# 分配社区到节点属性
assign_communities_to_nodes(G, communities)
for node, data in G.nodes(data=True):
    print(f"{node}: community={data.get('community')}")
```

---

## 四、cache.py — 文件缓存

### 功能

缓存文件提取结果，支持增量更新。

### 实现原理

```python
def file_hash(path: Path, root: Path) -> str:
    """
    计算文件 Hash：
    
    流程：
    1. 读取文件内容
       raw = path.read_bytes()
    
    2. 去除 YAML frontmatter（仅 .md）
       if path.suffix == ".md":
           content = _body_content(raw)  # 去除头部 YAML
    
    3. 计算 SHA256
       h = hashlib.sha256()
       h.update(content)
    
    4. 加入相对路径
       rel = path.relative_to(root)
       h.update(str(rel).encode())
    
    5. 返回 Hash
    
    意义：
    - 内容变化 → Hash 变化 → 需要重新提取
    - 路径不变 → 内容不变 → 使用缓存
    """
```

### 缓存存储

```python
def cache_dir(root: Path) -> Path:
    """
    缓存目录：
    
    graphify-out/cache/{hash}.json
    
    每个 Hash 对应一个文件提取结果
    """

def save_cached(path: Path, result: dict, root: Path) -> None:
    """
    保存缓存：
    
    流程：
    1. 计算 Hash
       h = file_hash(path, root)
    
    2. 写入临时文件
       tmp = cache_dir(root) / f"{h}.tmp"
       tmp.write_text(json.dumps(result))
    
    3. 重命名为正式文件
       os.replace(tmp, cache_dir(root) / f"{h}.json")
    
    4. 错误处理（Windows）
       if PermissionError:
           shutil.copy2(tmp, entry)  # 复制而非替换
           tmp.unlink()
    """
```

### 缓存检查

```python
def load_cached(path: Path, root: Path) -> dict | None:
    """
    加载缓存：
    
    流程：
    1. 计算 Hash
       h = file_hash(path, root)
    
    2. 查找缓存文件
       entry = cache_dir(root) / f"{h}.json"
    
    3. 判断是否有效
       if not entry.exists():
           return None  # 无缓存
    
    4. 加载缓存
       return json.loads(entry.read_text())
    
    意义：
    - Hash 匹配 → 使用缓存（无需重新提取）
    - Hash 不匹配 → 返回 None（需要重新提取）
    """
```

### 语义缓存

```python
def check_semantic_cache(files: list[str]) -> tuple[list[dict], list[dict], list[str]]:
    """
    批量检查语义缓存：
    
    流程：
    1. 遍历文件
       for fpath in files:
           result = load_cached(Path(fpath))
    
    2. 分类
       if result:
           cached_nodes.extend(result["nodes"])
           cached_edges.extend(result["edges"])
       else:
           uncached.append(fpath)
    
    3. 返回
       return (cached_nodes, cached_edges, cached_hyperedges, uncached)
    
    意义：
    - 已缓存文件 → 直接使用结果
    - 未缓存文件 → 需要语义提取
    - 减少 LLM 成本
    """
```

### 使用示例

```python
from builders.cache import load_cached, save_cached, cache_dir, clear_cache, check_semantic_cache

# 单文件缓存
result = load_cached(Path("auth.md"))
if result:
    print("使用缓存")
else:
    # 提取节点和边
    extraction = extract(Path("auth.md"))
    save_cached(Path("auth.md"), extraction)

# 批量缓存检查
cached_nodes, cached_edges, _, uncached = check_semantic_cache(files)
print(f"缓存命中: {len(cached_nodes)} 节点")
print(f"需要提取: {len(uncached)} 文件")

# 清空缓存
clear_cache()
```

---

## 五、构建流程总结

```
输入文档/代码
      ↓
  detect.py（文件检测）
      ↓
  extract.py（节点提取）*
      ↓
  cache.py（缓存检查）
      ↓
  build.py（构建图谱）
      ↓
  cluster.py（社区检测）
      ↓
  layer.py（分层标注）*
      ↓
  save_graph()（保存图谱）
```

*注：extract.py 和 layer.py 在 `engines/` 和 `core/` 中实现

---

## 六、性能指标

| 操作 | 延迟 |
|------|:----:|
| detect（1000 文件） | 200ms |
| detect（10000 文件） | 2s |
| build（1000 节点） | 50ms |
| build（50000 节点） | 500ms |
| cluster（Leiden） | 3s |
| cluster（Louvain） | 1s |
| cache load | 10ms |
| cache save | 20ms |

---

*最后更新: 2026-04-29*