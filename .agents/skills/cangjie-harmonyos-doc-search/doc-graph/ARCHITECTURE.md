# 仓颉鸿蒙知识图谱 — 系统架构文档

## 架构总览

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          CLI 入口 (cli.py)                              │
│  build-doc / build-code / build / build-subgraph / merge / search / ... │
└─────────────────────────────────┬───────────────────────────────┘
                                          │
          ┌───────────────────────────────┼───────────────────────────────┐
          │                               │                               │
          ▼                               ▼                               ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────────┐
│  阶段1: 确定性构建 │  │  阶段2: LLM增强   │  │       搜索与查询             │
│                  │  │   (可选)          │  │                              │
│  ┌───────────┐   │  │  ┌───────────┐   │  │  ┌───────────────────────┐  │
│  │ 文档提取  │   │  │  │ LLM Pipeline│  │  │  │ GraphSession          │  │
│  │ 1文件=1节点│   │  │  │ enhancer.py│   │  │  │ query.py              │  │
│  │ 正则+结构  │   │  │  │ pipeline.py│   │  │  │ ┌─────────┐ ┌────────┐│  │
│  └───────────┘   │  │  └───────────┘   │  │  │ │DocSearch │ │CodeSearch││  │
│  ┌───────────┐   │  │  urllib+thread   │  │  │ │Engine    │ │Engine   ││  │
│  │ 源码提取  │   │  │  分批读取原文     │  │  │ └─────────┘ └────────┘│  │
│  │ 1定义=1节点│   │  │  → Qwen3.6-plus  │  │  │ OR+累加打分   │  │
│  │ tree-sitter│   │  │  → 增强label_zh  │  │  │  倒排索引加速           │  │
│  │ 12语言AST  │   │  │  → 增强keywords  │  │  └───────────────────────┘  │
│  └───────────┘   │  │  → 增强description│  │                              │
│                  │  │  → 语义边(LLM)   │  │  ┌───────────────────────┐  │
│  ┌───────────┐   │  │                  │  │  │ GraphifyEngine         │  │
│  │ 图谱构建  │   │  │                  │  │  │ engines/               │  │
│  │ builders/ │   │  │                  │  │  │ 路径查找/邻居/统计      │  │
│  │ cluster   │   │  │                  │  │  └───────────────────────┘  │
│  │ validate  │   │  │                  │  │                              │
│  │ detect    │   │  │                  │  │                              │
│  │ cache     │   │  │                  │  │                              │
│  └───────────┘   │  │                  │  │                              │
└──────────────────┘  └──────────────────┘  └──────────────────────────────┘
          │                               │                               │
          ▼                               ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     输出与导出 (export/)                                │
│                 JSON / HTML / Report (Markdown)                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. 文档提取

### 入口
- **命令**: `python cli.py build-doc docs/ -o data/doc/graph.json`
- **核心文件**: `graph/doc/extractor.py` + `graph/doc/builder.py`

### 提取流程

```
docs/ 目录
  │
  ▼ detect_files() — 扫描 .md 文件
  │  分离 .overview.md (概览) 和 普通 .md (API/指南)
  │  排除顶层目录的 .overview.md 和 .abstract.md
  │
  ▼ 概览节点提取 — extract_overview_nodes()
  │  1. 从 .overview.md 提取: 目录名作为 label
  │  2. 从描述提取中英文关键词 (extract_overview_keywords)
  │     - 目录名 → 拆分驼峰/连字符/下划线 → 去 cj- 前缀 → 停词过滤
  │     - 描述文本 → @State/API名等技术术语
  │     - 中文连续字符 → 停词过滤
  │  3. 从"快速导航"提取 CONTAINS 边
  │  4. 基于目录结构自动建立 CONTAINS 边
  │  → 产出: DocNode(layer=1, is_god_node=True)
  │
  ▼ 普通文档提取 — extract_doc_node()
  │  1. is_pure_example() — 纯示例文件不建节点（去代码后中文<10且英文<5词）
  │  2. clean_filename() — 去哈希后缀/类型前缀/_Nmore后缀
  │  3. infer_layer() — L1=指南/概览, L2=API/错误码
  │  4. infer_category() — 按路径推断分类（harmonyos/std/stdx/lang/tools）
  │  5. build_namespace() — 从路径构建命名空间（cj-→去前缀，ohos→去前缀）
  │  6. detect_doc_type() — overview/api/guide/errorcode
  │  7. extract_label_zh() — 从 H1/H2 提取中文标题
  │  8. extract_description() — 从"功能:"或首段提取中英文描述
  │  9. extract_keywords() — 按文档类型提取中英文关键词（overview/api/guide/errorcode各有策略）
  │ 10. 提取 SEE_ALSO 边 — 从 Markdown 链接提取关联边
  │  → 产出: DocNode(layer=1或2)
  │
  ▼ 缓存机制 — cache.py
  │  check_semantic_cache(file_paths, root_dir) → (cached_nodes, cached_edges, cached_hyperedges, uncached_files)
  │  save_semantic_cache(new_nodes, new_edges, root) → 按文件哈希缓存
  │  save_cached(path, result, root) → SHA256+namespace 哈希 → JSON 缓存文件
  │
  ▼ build_doc_graph() — 组装所有节点和边
  │  → 返回 (nodes: dict[str, DocNode], neighbors: dict[str, list])
  │
  ▼ build_doc_nx_graph() → 转为 NetworkX Graph（委托 build_subgraph）
```

### DocNode 数据模型

| 字段 | 类型 | 说明 |
|------|------|------|
| id | str | `{category}_{namespace}_{doc_type}_{label}` |
| label | str | 清理后的文件名 |
| label_zh | str | 中文标题（H1/H2提取） |
| layer | int | 1=指南/概览, 2=API/错误码（文档图仅两层） |
| description_zh | str | 中文描述 |
| description_en | str | 英文描述 |
| keywords_zh | list[str] | 中文搜索关键词 |
| keywords_en | list[str] | 英文搜索关键词 |
| category | str | std/stdx/lang/harmonyos/tools |
| namespace | str | 从路径推导的命名空间 |
| source_file | str | 相对文件路径 |
| community_id | int | 社区检测后的社区编号 |
| degree | int | 邻居数量 |
| is_god_node | bool | 是否为核心节点（概览节点） |
| extra | dict | 预留扩展字段（当前未使用） |

---

## 2. 源码提取

### 入口
- **命令**: `python cli.py build-code src/ -o data/code/graph.json`
- **核心文件**: `graph/code/extractor.py` + `graph/code/builder.py`

### 提取流程

```
源码目录
  │
  ▼ collect_files() — 按扩展名收集源码文件
  │  支持 12 种语言: .cj/.py/.js/.jsx/.mjs/.ts/.tsx/.java/.c/.h/.cpp/.cc/.cxx/.hpp/.cs/.kt/.kts/.swift/.go/.rs
  │
  ▼ detect_language() — 根据文件扩展名匹配 LanguageConfig
  │  每种语言有独立的 tree-sitter 语法配置
  │  (class_types, function_types, import_types, call_types 等)
  │  每种语言有专属 import_handler（Python/JS/Java/C/仓颉各有不同解析逻辑）
  │  每种语言有专属 callee 提取逻辑（仓颉 fieldAccess/atomicVariable、Python attribute、JS member_expression 等）
  │
  ▼ _extract_ast() — tree-sitter AST 解析
  │  1. 加载对应语言的 tree-sitter 模块
  │  2. Parser 解析源码 → AST 树
  │  3. 递归 walk() AST:
  │     - import → import_handler() → USES 边
  │     - class/interface/enum/struct/extension → CodeNode(api_kind)
  │     - function/method → CodeNode("function")
  │     - 继承 → _extract_inheritance() → EXTENDS 边
  │  4. Call-graph pass: 遍历 function_bodies → _walk_calls() → USES 边
  │  5. 引用类型: keywords 字段 → USES 边
  │  6. 每个源码文件 → 1个 file 节点 (api_kind="file")
  │
  ▼ build_code_graph() — 组装
  │  → 返回 (nodes: dict[str, CodeNode], neighbors: dict[str, list])
  │
  ▼ build_code_nx_graph() → 转为 NetworkX Graph（委托 build_subgraph）
```

### CodeNode 数据模型

| 字段 | 类型 | 说明 |
|------|------|------|
| id | str | `{namespace}_{api_kind}_{name}` |
| label | str | 类名/函数名() |
| api_kind | str | class/interface/enum/struct/function/extension/file |
| category | str | std/stdx/lang/harmonyos/code |
| namespace | str | 从路径推导 |
| source_file | str | 源码文件路径 |
| parent_type | str | 父类名（继承） |
| methods | list[str] | 类方法列表 |
| enum_values | list[str] | 枚举值列表 |
| keywords | list[str] | 引用的类型名列表 |
| community_id | int | 社区编号 |
| degree | int | 邻居数量 |

---

## 3. 图谱构建与增强

### 构建流程

```
┌─────────────┐     ┌─────────────┐
│ Doc 提取结果 │     │ Code 提取结果 │
│ nodes+edges │     │ nodes+edges │
└──────┬──────┘     └──────┬──────┘
       │                    │
       ▼                    ▼
  build_subgraph() — 合并为 NetworkX Graph
       │
       ▼
  [可选] LLM 增强 — enhance_graph_from_files()
       │  1. 断点续传: 跳过已增强节点 (resume=True, 检查 llm_enhanced 标记)
       │  2. 分批: create_batches() (默认 max_chars=40000, 增强时默认 15000)
       │  3. 并发: ThreadPoolExecutor(max_workers=5)
       │  4. 调用: urllib.request → Qwen3.6-plus (3次重试, timeout=600s)
       │  5. 合并: merge_llm_results() → 增强现有节点属性
       │  6. 回写: 每批次完成后立即保存 JSON
       │  7. 超时: total_timeout 参数控制整个流程时间上限
       │
       ▼
  聚类 — cluster()
       │  算法: Leiden (graspologic) 或 Louvain (networkx, seed=42)
       │  过大社区自动拆分 (>25%节点数或 _MIN_SPLIT_SIZE=10)
       │  孤立节点单独成社区
       │  → assign_communities_to_nodes() → 写入 community_id 属性
       │
       ▼
分层标注 — annotate_layers()（仅文档图）
        │  文档图: L1=概念层(概览/指南), L2=API层(API/错误码)
        │  源码图 CodeNode 模型无 layer 字段，annotate_layers 会推断但不持久化
       │
       ▼
  保存 — save_graph()
       │  NetworkX → node_link_data JSON
       │  包含 input_tokens/output_tokens 元信息
       │
       ▼
  data/doc/graph.json 或 data/merged/graph.json
```

### 子图谱与合并

```
build-subgraph → data/subgraphs/{name}/graph.json
merge → 合并多个子图谱 → 基于label去重(deduplicate_by_label) → 重聚类 → data/merged/graph.json
```

### 边类型

| 边类型 | 所属图 | 来源 | 说明 |
|--------|--------|------|------|
| contains | 文档图 | 确定性 | 概览→子文档 |
| see_also | 文档图 | 确定性 | Markdown 链接关联 |
| extends | 源码图 | 确定性 | 类继承 |
| uses | 源码图 | 确定性 | import/调用关系 |
| method | 源码图 | 确定性 | 类→方法关系 |
| recommends_api | — | LLM (预留，未启用) | 推荐相关API |
| alternative_to | — | LLM (预留，未启用) | 替代方案 |
| typically_used_with | — | LLM (预留，未启用) | 常用组合 |
| semantically_similar_to | — | LLM (预留，未启用) | 语义相似 |

### Edge 数据模型

| 字段 | 类型 | 说明 |
|------|------|------|
| source | str | 源节点 ID |
| target | str | 目标节点 ID |
| relation | str | 边类型 (EdgeRelation enum) |
| source_file | str | 来源文件路径 |
| confidence | str | EXTRACTED / INFERRED / AMBIGUOUS |
| confidence_score | float | 置信度分数 (默认 1.0) |
| description | str | 边描述 |

---

## 4. 搜索与打分

### 搜索入口
- **命令**: `python cli.py search "关键词" --graph doc -b -k 5`
- **Python API**: `session = create_session(); result = session.search(query, top_k=5, graph="doc")`
- **核心文件**: `query.py` → `graph/doc/search.py` / `graph/code/search.py`

### 搜索流程

```
用户查询 (Agent 已提取的中英文关键词)
  │
  ▼ _parse_community_prefix() — 解析社区前缀 (如 "std.状态管理")
  │  支持前缀: std / stdx / lang / harmonyos / tools
  │
  ▼ 分词
  │  _tokenize_en() — 提取英文词: @[State] 或 [A-Za-z_][A-Za-z0-9_]* (保留@装饰器)
  │  _tokenize_zh() — 提取中文词: 连续中文字符 [\u4e00-\u9fff]+
  │
  ▼ 倒排索引过滤 — DocSearchEngine._build_inverted_index()
  │  label/label_zh/keywords_en/keywords_zh/description → term→node_id 映射
  │  仅对倒排索引命中的节点打分 (加速)
  │  如果命中节点超过50%候选 → 回退到全量扫描
  │  CodeSearchEngine 不使用倒排索引（直接遍历）
  │
  ▼ 打分 — score_node() [OR+累加策略]
  │  ┌──────────────────────────────────────────────┐
  │  │ 匹配层级          │ 单词得分  │ 说明          │
  │  │──────────────────│──────────│──────────────│
  │  │ label 精确匹配    │ 100      │ 完全匹配标签  │
  │  │ label_zh 精确匹配 │ 100      │ 中文标题精确  │
  │  │ label 包含匹配    │ 60       │ 标签包含关键词│
  │  │ label_zh 包含匹配 │ 60       │ 中文标题包含  │
  │  │ keyword 精确匹配  │ 40       │ 关键词完全匹配│
  │  │ keyword 包含匹配  │ 25       │ 关键词互相包含│
  │  │ description 匹配 │ 20       │ 描述文本包含  │
  │  └──────────────────────────────────────────────┤
  │  层级加权: score *= DOC_LAYER_WEIGHTS[layer]    │
  │  L1=2.5倍, L2=1.8倍                             │
  │  God节点加权: 概览类查询 1.2倍                    │
  │  → 每个关键词 OR 独立匹配，多关键词累加总分       │
  │  → 最佳匹配类型(best_match)记录                  │
  └──────────────────────────────────────────────────┘
│
   ▼ 排序 — 按总分降序
  │
  ▼ 直接命中 — 取 top_k 个
  │
  ▼ 关联推荐 — 邻居扩展
  │  对每个直接命中节点，取最多2个邻居
  │  关联分数 = 直接命中分数 * 0.5
  │  最多5个关联推荐，去重
  │
  ▼ SearchResult 组装
```

### 源码图打分

```
score_code_node() — OR+累加
  │  label 精确匹配  → +100
  │  label 包含匹配  → +60
  │  keywords 精确匹配 → +40
  │  keywords 包含匹配 → +25
  │  methods 匹配    → +25
  │  enum_values 匹配 → +25
  │  api_kind 过滤加权 → 查询包含kind关键词时 ×1.2
```

### 双图搜索

```
session.search(query, graph="auto|doc|code|both")
  │
  auto → 优先 doc 图
  doc  → DocSearchEngine.search()
  code → CodeSearchEngine.search()
  both → 双图搜索 → _merge_results() 按 source_file 去重合并
```

---

## 5. 返回结果格式

### SearchResult 模型

```python
@dataclass
class SearchResult:
    query: str                      # 查询字符串
    direct_hits: list[Hit]          # 直接命中结果
    related_hits: list[Hit]         # 关联推荐结果
    graph_used: str                 # "doc" | "code" | "both"
    latency_ms: float               # 搜索耗时(ms)
    
    # 兼容属性
    paths  → [h.source_file for all hits]
    nodes  → [dict形态的节点列表]
```

### Hit 模型

```python
@dataclass
class Hit:
    node_id: str                    # 节点ID
    label: str                      # 节点标签
    source_file: str                # 源文件路径
    score: float                    # 匹配分数
    match_type: str                 # "label"|"keyword"|"description"|"related"|"method"|"enum_value"
    related_from: str               # 关联来源节点标签(仅related)
    relation_type: str              # 关联边类型(仅related)
```

### Brief 模式输出 (Agent 默认)

```
=== 直接命中 (3) ===
[240.0] cj-scroll-swipe-list | harmonyos-6.0.2-15k/cj-scroll-swipe-list/xxx.md
[180.0] cj-state-rendering-lazyforeach | harmonyos-6.0.2-15k/cj-state-rendering-lazyforeach/xxx.md

=== 关联推荐 (2) ===
[120.0] cj-list-overview | harmonyos-6.0.2-15k/cj-list/xxx.md (来自 cj-scroll-swipe-list, contains)
```

### Full 模式输出

```
查询: List scroll performance LazyForEach 列表 滑动 卡顿
图谱: doc
耗时: 15.3ms
=== 直接命中 (3) ===
[240.0] cj-scroll-swipe-list | harmonyos-6.0.2-15k/cj-scroll-swipe-list/xxx.md
...
```

### JSON 输出

```json
{
  "query": "List scroll performance",
  "direct_hits": [
    {"node_id": "harmonyos_scroll_list", "label": "cj-scroll-swipe-list", "source_file": "...", "score": 240.0, "match_type": "keyword"}
  ],
  "related_hits": [
    {"node_id": "harmonyos_list_overview", "label": "cj-list-overview", "source_file": "...", "score": 120.0, "match_type": "related", "related_from": "cj-scroll-swipe-list", "relation_type": "contains"}
  ],
  "graph_used": "doc",
  "latency_ms": 15.3
}
```

---

## 6. 引擎插件架构

### GraphEngine 抽象基类

```
engines/base.py — GraphEngine (ABC)
  │  load(graph_path)           加载图谱 JSON
  │  find_path(a, b, depth)     最短路径查找
  │  explain_node(node_id)      节点详情
  │  get_neighbors(id, count)   邻居列表
  │  add_edge(src, tgt, ...)    添加边
  │  save(graph_path)           保存图谱
  │  name → str                 引擎名称
  │  stats → dict               统计信息
  │
  ▼ engines/registry.py — 注册表
  │  @register 装饰器 → 自动注册到 _registry
  │  get_engine(name) → 获取引擎类
  │  create_engine(name) → 创建引擎实例
  │
  ▼ engines/graphify_engine.py — GraphifyEngine 实现
  │  基于 NetworkX 图计算
  │  _resolve_node() → 模糊节点ID解析（支持 label/norm_label/id）
  │  shortest_path → nx.shortest_path
```

---

## 7. 文件检测与缓存

### detect 模块 (graph/builders/detect.py)

```
detect(root) → 扫描目录，分类文件类型
  │  classify_file() → FileType (CODE/DOCUMENT/PAPER/IMAGE/VIDEO)
  │  _is_sensitive() → 检测敏感文件(.env/.pem/.key 等)
  │  _looks_like_paper() → 论文信号检测(arxiv/doi/abstract 等)
  │  .graphifyignore → 类似 .gitignore 的排除机制
  │  大语料预警: <50k词可能不需要图谱, >500k词语义提取昂贵
  │  增量检测: detect_incremental() → 基于 mtime manifest.json

validate 模块 (graph/builders/validate.py)
  │  validate_extraction() → 校验提取 JSON schema
  │  REQUIRED_NODE_FIELDS: id/label/file_type/source_file
  │  REQUIRED_EDGE_FIELDS: source/target/relation/confidence/source_file
  │  VALID_FILE_TYPES: code/document/paper/image/rationale
  │  VALID_CONFIDENCES: EXTRACTED/INFERRED/AMBIGUOUS
```

### cache 模块 (graph/builders/cache.py)

```
file_hash(path, root, namespace) → SHA256(content + path + namespace)
  │  .md 文件 → 去 frontmatter 后计算哈希
  │  缓存目录: graphify-out/cache/
  │  
  │  check_semantic_cache(files, root) → (cached_nodes, cached_edges, cached_hyperedges, uncached_files)
  │  save_semantic_cache(nodes, edges, root) → 按 source_file 分组，逐文件缓存
  │  save_cached(path, result, root) → 写入 JSON 缓存文件
  │  load_cached(path, root) → 读取缓存
```

---

## 8. 分析与导出

### 分析模块 (analysis/analyze.py)

```
god_nodes(G, top_n) → 度最高的非文件/非概念节点
surprising_connections(G, communities, top_n) → 跨社区/跨文件边
  │  多源文件 → _cross_file_surprises()
  │  单源文件 → _cross_community_surprises()
suggest_questions(G, communities) → 基于图结构生成探索性问题
  │  ambiguous_edge / bridge_node / verify_inferred / isolated_nodes / low_cohesion
graph_diff(G_old, G_new) → 两版图谱差异对比（新增/删除节点和边）
```

### 导出模块 (export/)

```
export/json.py
  │  to_json(G, communities, output_path) → NetworkX → node_link_data JSON
  │  prune_dangling_edges(graph_data) → 删除引用不存在节点的边
  │  load_graph_json(path) → 加载 JSON 为 NetworkX 图
  │
export/html.py
  │  to_html(G, communities, output_path) → vis-network 交互式 HTML
  │  MAX_NODES_FOR_VIZ = 5000（超过时需 --max-nodes 裁剪后导出）
  │  vis-network forceAtlas2Based 物理引擎
  │  节点大小按度比例缩放，社区颜色映射
  │  CLI: python cli.py export --format html --max-nodes 5000
  │
export/report.py
  │  generate_report(G, communities, output_path) → Markdown 报告
  │  包含: god_nodes / surprising_connections / communities / suggest_questions
```

---

## 9. 项目目录结构

```
knowledge-graph-template/
├── cli.py                   # CLI 入口 (所有命令的调度中心)
├── query.py                 # 统一查询入口 (GraphSession)
├── core/
│   ├── models.py            # 数据模型 (DocNode/CodeNode/Edge/Hit/SearchResult)
│   ├── constants.py         # 共享常量 (社区名/层级权重[仅L1/L2]/停词表/颜色/默认路径)
│   └── README.md
├── graph/
│   ├── base_search.py       # 搜索基类 (分词/社区前缀解析/通用搜索流程)
│   ├── doc/
│   │   ├── extractor.py     # 文档提取器 (正则+结构分析, 概览关键词提取)
│   │   ├── builder.py       # 文档图构建器 (缓存+组装+NetworkX转换)
│   │   ├── search.py        # 文档搜索引擎 (OR+累加打分+倒排索引)
│   │   └── __init__.py
│   ├── code/
│   │   ├── extractor.py     # 源码提取器 (tree-sitter, 12语言, LanguageConfig)
│   │   ├── builder.py       # 源码图构建器 (组装+NetworkX转换)
│   │   ├── search.py        # 源码搜索引擎 (OR+累加打分+api_kind加权)
│   │   └── __init__.py
│   ├── llm/
│   │   ├── enhancer.py      # LLM增强核心 (urllib+thread, 分批/调用/合并/断点续传)
│   │   ├── pipeline.py      # LLM流水线编排 (ThreadPoolExecutor并发, 每批回写)
│   │   └── __init__.py
│   ├── builders/
│   │   ├── build.py         # 图谱操作 (合并/去重/聚类/分层/保存/加载)
│   │   ├── build_doc_graph.py  # 文档图构建(旧版, 引用 core.graph)
│   │   ├── cluster.py       # 社区检测 (Leiden/Louvain, 大社区拆分)
│   │   ├── validate.py      # 提取结果校验 (schema验证)
│   │   ├── detect.py        # 文件类型检测 (多类型/敏感文件/增量/论文信号)
│   │   ├── cache.py         # 文件提取缓存 (SHA256哈希, frontmatter去除)
│   │   └── __init__.py
│   └── __init__.py
├── engines/
│   ├── base.py              # 图谱引擎插件基类 (GraphEngine, NodeInfo, EdgeInfo)
│   ├── graphify_engine.py   # Graphify引擎实现 (NetworkX图计算, 模糊节点解析)
│   ├── registry.py          # 引擎注册表 (@register装饰器)
│   └── __init__.py
├── analysis/
│   ├── analyze.py           # 图分析 (核心节点/惊奇连接/建议问题/图谱差异)
│   ├── README.md
│   └── __init__.py
├── export/
│   ├── json.py              # JSON 导出 (node_link_data, dangling edge pruning)
│   ├── html.py              # HTML 可视化导出 (vis-network, 5000节点上限)
│   ├── report.py            # Markdown 报告导出
│   └── __init__.py
├── scripts/
│   ├── docs_statistics.py   # 文档统计脚本
│   ├── docs_statistics.json # 统计结果
│   └── .gitkeep
├── eval/                    # 评测与测试
│   ├── run_eval.py          # 搜索评测运行脚本
│   ├── verify_v7.py         # V7评测验证
│   ├── validate_keywords.py # 关键词质量验证
│   ├── extract_chunks.py    # 评测数据分块
│   ├── combine_chunks.py    # 分块合并
│   ├── check_data.py        # 数据质量检查
│   ├── keywords_v5_deduped.json  # 分类关键词映射
│   ├── keywords_v6_prompt.json   # V6关键词
│   ├── keywords_v7_prompt.json   # V7关键词
│   ├── chunk_v7_*.json           # V7评测数据分块
│   ├── chunk_v6_*.json           # V6评测数据分块
│   ├── eval_report.md            # 评测报告
│   ├── TEST_GUIDE.md             # 测试指南
│   └── datasets/
│       ├── eval_queries_comprehensive.jsonl
│       ├── eval_queries_comprehensive_deduped.jsonl
│       ├── eval_config.json
│       ├── chunk_1-4.json
│       ├── README.md
│       └── DESIGN_SPEC.md
├── docs/                    # 文档输入 (鸿蒙仓颉文档)
├── data/                    # 图谱输出
│   ├── doc/graph.json       # 文档图
│   ├── doc_oldPrompt/graph.json  # 旧提示词版本
│   ├── before_llm/graph.json   # LLM增强前备份
│   ├── code/graph.json      # 源码图（预留）
│   ├── merged/graph.json    # 合并图（预留）
│   └── subgraphs/*/graph.json  # 子图谱（预留）
├── .opencode/skills/keyword-extraction-guide.md  # 关键词提取指南
├── .gitattributes
├── ARCHITECTURE.md          # 本文档
├── BUILD_GUIDE.md           # 构建指南
└── SKILL.md                 # Agent 使用指南
```

---

## 10. 关键设计决策

| 决策 | 原因 |
|------|------|
| 1文件=1节点 (doc) | 文档是开发者的主要查找目标，保持粒度与文档对齐 |
| 1定义=1节点 (code) | 代码搜索需定位到具体API定义，而非整个文件 |
| 双图隔离 | doc/code 搜索逻辑和打分策略不同，隔离避免干扰 |
| OR+累加打分 | 多关键词意图需累积分数，OR保证单关键词也能命中 |
| 倒排索引 (doc only) | 文档图节点量大，纯关键词搜索无需遍历全图 |
| 层级加权 L1=2.5x (doc图) | 概览/指南文档是开发者的首选入口，提升优先级；文档图仅两层(L1/L2) |
| LLM 增强不建节点且不提边 | LLM只增强已有节点属性，不引入新节点或边（避免幻觉），LLM语义边为预留未启用 |
| 断点续传 | LLM调用成本高且可能中断，检查 llm_enhanced 标记跳过已完成 |
| 去路径/ID打分 | 移除建图知识干扰语义搜索，避免路径匹配虚假高分 |
| urllib+thread | 避免依赖 openai SDK，使用原生 urllib + threading 实现LLM调用 |
| 每批回写 | LLM流水线每完成一个批次立即保存，防止中断丢失已增强数据 |
| 模糊节点解析 | GraphifyEngine._resolve_node 支持按 label/norm_label/id 查找节点 |
| 大社区拆分 | 过大社区 (>25%节点) 降低搜索精度，自动拆分子社区 |
| frontmatter 去除 | 缓存哈希计算去除 .md 文件 frontmatter，避免无关内容影响缓存命中 |