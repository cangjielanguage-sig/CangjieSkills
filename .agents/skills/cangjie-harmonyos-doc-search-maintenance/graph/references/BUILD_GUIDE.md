# 知识图谱构建指南

本文档描述知识图谱的构建流程、节点定义、搜索策略和工程规范。当 `data/doc/graph.json` 缺失或领域覆盖不足时，Agent 应参考本指南重建图谱。

## 双图架构

| 图谱 | 文件 | 节点粒度 | 提取方式 | 用途 |
|------|------|---------|---------|------|
| **文档图** | `data/doc/graph.json` | 1文件=1节点 | 正则+结构分析 | 用法查询、指南、教程 |
| **源码图** | `data/code/graph.json` | 1定义=1节点 | tree-sitter AST（12语言） | 源码查询、继承关系、API定义 |

### 源码图支持的语言

| 扩展名 | 语言 | 提取内容 |
|--------|------|---------|
| `.cj` | 仓颉 | class/struct/enum/function/继承/调用/导入 |
| `.py` | Python | class/function/继承/调用/导入 |
| `.js/.jsx/.mjs` | JavaScript | class/function/调用/导入 |
| `.ts/.tsx` | TypeScript | class/function/调用/导入 |
| `.java` | Java | class/interface/method/继承/调用/导入 |
| `.c/.h` | C | function/调用/导入 |
| `.cpp/.cc/.cxx/.hpp` | C++ | class/function/调用/导入 |
| `.cs` | C# | class/interface/method/继承/调用/导入 |
| `.kt/.kts` | Kotlin | class/object/function/调用/导入 |
| `.swift` | Swift | class/protocol/function/继承/调用/导入 |
| `.go` | Go | function/调用/导入 |
| `.rs` | Rust | struct/enum/trait/function/调用/导入 |

## 构建流程

### 两阶段管线

```
阶段1：确定性构建（doc + code AST）
    ↓
阶段2：LLM 信息增强（可选，只增强搜索元数据，不建节点）
```

### CLI 构建命令

```bash
# 构建文档图（1文件=1节点）
python cli.py build-doc docs/harmonyos-6.0.2-15k -o data/doc/graph.json

# 构建文档图 + LLM增强
python cli.py build-doc docs/harmonyos-6.0.2-15k -o data/doc/graph.json --enhance

# 构建源码图（1定义=1节点，多语言 AST）
python cli.py build-code docs/stdx/net/http -o data/code/graph.json

# 完整构建（编排 doc + code + 可选 LLM 增强）
python cli.py build docs/ -o data/graph.json
python cli.py build docs/ --enhance -o data/graph.json

# 仅重新聚类（不重新提取）
python cli.py build docs/ --cluster-only -o data/full/graph.json

# 构建子图谱
python cli.py build-subgraph docs/harmonyos --name harmonyos
python cli.py build-subgraph docs/harmonyos --name harmonyos --enhance

# 合并子图谱
python cli.py merge data/subgraphs/*/graph.json --output data/merged/graph.json
python cli.py merge graph1.json graph2.json --output merged.json --no-deduplicate --no-recluster

# 对已有图谱做 LLM 增强
python cli.py enhance-graph data/merged/graph.json --docs-dir docs/

# LLM 增强高级选项
python cli.py enhance-graph data/doc/graph.json --docs-dir docs/ \
    --batch-chars 15000 \
    --batch-limit 5 \
    --total-timeout 21600 \
    --no-resume \
    -o data/doc/graph_enhanced.json
```

### LLM 增强配置

LLM 增强位于 `graph/llm/enhancer.py` 和 `graph/llm/pipeline.py`，用于提取高质量搜索元数据：

- 提取中英文关键词（5-10个）
- 生成简洁描述
- 从用户搜索视角提取核心内容

技术实现：
- 使用 `urllib.request` 直接调用 DashScope API（Qwen3.6-plus）
- `ThreadPoolExecutor(max_workers=5)` 并发处理
- 每批次完成后立即保存（防止中断丢失）
- 3次重试机制（retry with 2s sleep）
- 单次请求超时 600s
- 支持 `total_timeout` 全流程超时控制

提示词核心规则：
1. 关键词必须反映文档独有内容
2. 从用户视角提取开发者实际搜索的词
3. 避免过于泛化的词（HarmonyOS、API、使用等）
4. 严格控制在5-10个关键词
5. 问题解决类关键词（卡顿、不刷新）仅在文档确实覆盖时才加入

### 缓存机制

构建过程使用文件内容哈希缓存（SHA256），避免重复提取：

- `.md` 文件计算哈希时去除 frontmatter
- 缓存目录: `graphify-out/cache/`
- `build_doc_graph()` 自动启用缓存（`use_cache=True`）
- 缓存命中文件直接复用提取结果
- 新提取结果按 source_file 分组写入缓存

## 节点定义

### 文档节点

```python
@dataclass
class DocNode:
    id: str = ""                    # "harmonyos_list_doc"
    label: str = ""                 # "List"
    label_zh: str = ""              # "列表组件"
    layer: int = 1                  # 1=指南, 2=API
    description_zh: str = ""        # 中文描述
    description_en: str = ""        # 英文描述
    keywords_zh: list[str] = []     # 中文关键词（仅搜索词）
    keywords_en: list[str] = []     # 英文关键词（仅搜索词）
    category: str = ""              # "std" | "stdx" | "lang" | "harmonyos" | "tools"
    namespace: str = ""             # 命名空间（用于 ID 生成和边构建）
    source_file: str = ""           # 相对路径 → Agent 读取原文
    community_id: int = -1          # 社区检测后的社区编号
    degree: int = 0                 # 邻居数量
    is_god_node: bool = False       # 是否为核心节点（概览节点）
    extra: dict = field(default_factory=dict)  # 预留扩展字段（当前未使用）
```

### 源码节点

```python
@dataclass
class CodeNode:
    id: str = ""
    label: str = ""                 # "Client"
    api_kind: str = ""              # "class" | "interface" | "enum" | "function" | "struct" | "extension" | "file"
    category: str = ""              # "std" | "stdx" | "lang" | "harmonyos" | "code"
    namespace: str = ""             # 命名空间（用于 ID 生成）
    source_file: str = ""
    parent_type: str = ""           # 父类/接口名
    methods: list[str] = []         # 方法列表
    enum_values: list[str] = []     # 枚举值
    keywords: list[str] = []        # 引用类型名
    community_id: int = -1          # 社区编号
    degree: int = 0                 # 邻居数量
```

### 边模型

```python
class EdgeRelation(Enum):
    # 确定性边（文档图）
    CONTAINS = "contains"           # 概览→子文档
    SEE_ALSO = "see_also"           # Markdown 链接关联
    # 确定性边（源码图）
    EXTENDS = "extends"             # 类继承
    USES = "uses"                   # import/调用关系
    # LLM 语义边（预留，当前未启用）
    RECOMMENDS_API = "recommends_api"
    ALTERNATIVE_TO = "alternative_to"
    TYPICALLY_USED_WITH = "typically_used_with"
    SEMANTICALLY_SIMILAR_TO = "semantically_similar_to"

@dataclass
class Edge:
    source: str = ""
    target: str = ""
    relation: str = ""
    source_file: str = ""
    confidence: str = "EXTRACTED"     # EXTRACTED | INFERRED | AMBIGUOUS
    confidence_score: float = 1.0
    description: str = ""
```

## 搜索打分规则

### 策略 A：OR + 累加打分

#### 文档图

| 匹配类型 | 单关键词分值 | 说明 |
|---------|------------|------|
| label 精确匹配 | +100 | 文档主题就是这个词 |
| label_zh 精确匹配 | +100 | 中文精确匹配 |
| label 包含匹配 | +60 | 文档主题包含该词 |
| label_zh 包含匹配 | +60 | 同上 |
| keywords 精确匹配 | +40 | 文档明确将此词列为关键词 |
| keywords 包含匹配 | +25 | 关键词包含该词 |
| description 匹配 | +20 | 描述中提到该词（语义兜底） |

最终分数 × 层权重（L1指南×2.5, L2 API×1.8）

God节点加权：概览类查询（含"有哪些"、"概览"、"功能"、"overview"）×1.2

#### 源码图

| 匹配类型 | 单关键词分值 | 说明 |
|---------|------------|------|
| label 精确匹配 | +100 | API 名称精确匹配 |
| label 包含匹配 | +60 | API 名称包含该词 |
| keywords 精确匹配 | +40 | 引用类型精确匹配 |
| keywords 包含匹配 | +25 | 引用类型部分匹配 |
| methods 匹配 | +25 | 方法名匹配 |
| enum_values 匹配 | +25 | 枚举值匹配 |

api_kind 过滤加权：查询中包含 class/interface/enum 等关键词时，匹配 api_kind 的节点 ×1.2

### 关联推荐选取

| 优先级 | 选取规则 | 示例 |
|--------|---------|------|
| P0 | 语义边优先 | List → LazyForEach（recommends_api） |
| P1 | 结构边次之 | List Overview → List 组件属性（CONTAINS） |
| P2 | 度小的优先 | 优先返回具体组件，而非"概述" |

默认：每个直接命中取 top2 邻居，关联节点总计不超过 **5 个**。
关联分数 = 直接命中分数 × 0.5

### 倒排索引优化

DocSearchEngine 构建倒排索引加速搜索：

- 索引范围: label / label_zh / keywords_en / keywords_zh / description 的分词结果
- 搜索时先查倒排索引获取候选节点 ID，再对候选节点打分
- 如果命中节点超过 50% 候选节点 → 回退到全量扫描
- CodeSearchEngine 不使用倒排索引（直接遍历所有节点）

## CLI 命令速查

| 命令 | 说明 | 示例 |
|------|------|------|
| `build-doc` | 构建文档图（1文件=1节点） | `build-doc docs/ -o data/doc/graph.json` |
| `build-doc --enhance` | 构建文档图 + LLM增强 | `build-doc docs/ --enhance -o data/doc/graph.json` |
| `build-code` | 构建源码图（多语言 AST） | `build-code src/ -o data/code/graph.json` |
| `build` | 完整构建（doc + code + 可选 LLM 增强） | `build docs/ --enhance` |
| `build --cluster-only` | 仅重新聚类 | `build docs/ --cluster-only` |
| `build-subgraph` | 构建子图谱 | `build-subgraph docs/api --name api` |
| `merge` | 合并子图谱 | `merge graph1.json graph2.json -o merged.json` |
| `enhance-graph` | LLM 增强已有图谱 | `enhance-graph graph.json --docs-dir docs/` |
| `search` | OR+累加搜索 | `search "概念" --graph doc -b` |
| `path` | 路径查询 | `path "A" "B"` |
| `explain` | 解释节点 | `explain "API"` |
| `neighbors` | 邻居节点 | `neighbors "节点"` |
| `god-nodes` | 核心节点 | `god-nodes --top-n 10` |
| `surprises` | 惊奇连接 | `surprises --top-n 5` |
| `stats` | 统计 | `stats` |
| `graphs` | 列出可用图谱 | `graphs` |
| `export` | 导出图谱 | `export --format html --max-nodes 5000` |

## 目录结构

```
knowledge-graph-template/
├── cli.py                      # CLI 入口（编排构建/搜索）
├── SKILL.md                    # Agent 使用指南（搜索流程）
├── ARCHITECTURE.md             # 系统架构文档
├── BUILD_GUIDE.md              # 本文档（构建指南）
├── query.py                    # 统一查询入口 (GraphSession)
│
├── core/                       # 核心数据模型
│   ├── __init__.py
│   ├── models.py               # DocNode / CodeNode / Edge / Hit / SearchResult
│   ├── constants.py            # 常量定义 (DOC_LAYER_WEIGHTS/CODE_KIND_MAP/COMMUNITIES)
│   └── README.md
│
├── graph/                      # 图谱构建与搜索管线
│   ├── __init__.py
│   ├── base_search.py          # 搜索基类 (分词/社区前缀解析/通用搜索流程)
│   ├── builders/               # 图操作：合并/去重/聚类/分层/保存/加载/缓存/检测/校验
│   ├── doc/                    # 文档图管线（提取/构建/搜索）
│   ├── code/                   # 源码图管线（AST提取/构建/搜索）
│   └── llm/                    # LLM 信息增强 (urllib+thread并发/分批/断点续传)
│
├── engines/                    # 图计算引擎插件
│   ├── base.py                 # GraphEngine 抽象基类
│   ├── graphify_engine.py      # NetworkX 图计算实现
│   ├── registry.py             # @register 引擎注册表
│   └── __init__.py
│
├── export/                     # 导出工具（JSON/HTML/Report）
│   ├── json.py                 # JSON导出 + dangling edge pruning
│   ├── html.py                 # vis-network交互式HTML (5000节点上限)
│   ├── report.py               # Markdown报告 (god_nodes/surprises/questions)
│   └── __init__.py
│
├── analysis/                   # 分析工具
│   ├── analyze.py              # god_nodes/surprising_connections/suggest_questions/graph_diff
│   ├── README.md
│   └── __init__.py
│
├── eval/                       # 评测与测试
│   ├── run_eval.py             # 搜索评测运行脚本
│   ├── verify_v7.py            # V7评测验证
│   ├── validate_keywords.py    # 关键词质量验证
│   ├── keywords_v5_deduped.json    # 分类关键词配置
│   ├── keywords_v6_prompt.json     # V6关键词
│   ├── keywords_v7_prompt.json     # V7关键词
│   ├── eval_report.md              # 评测报告
│   └── TEST_GUIDE.md               # 测试指南
│   └── datasets/
│       ├── eval_queries_comprehensive.jsonl
│       ├── eval_queries_comprehensive_deduped.jsonl
│       ├── eval_config.json
│       ├── DESIGN_SPEC.md
│       └── README.md
│
├── data/                       # 图谱数据文件
│   ├── doc/graph.json              # 文档图谱（增强后）
│   ├── doc_oldPrompt/graph.json    # 旧提示词版本图谱
│   ├── before_llm/graph.json       # 增强前图谱备份
│   └── code/graph.json             # 源码图谱（预留）
│
├── docs/                       # 文档输入（鸿蒙仓颉文档）
│   ├── harmonyos-6.0.2-15k/    # 鸿蒙文档目录
│   └── .gitkeep
│
├── scripts/                    # 辅助脚本
│   ├── docs_statistics.py      # 文档统计
│   └── docs_statistics.json    # 统计结果
│
└── .opencode/skills/           # opencode skill 配置
    └── keyword-extraction-guide.md
```

## 评测与优化

### 评测流程

```bash
# 搜索评测
python eval/run_eval.py

# 关键词验证
python eval/validate_keywords.py

# V7 评测验证
python eval/verify_v7.py

# 数据质量检查
python eval/check_data.py
```

### 关键词提取优化

关键词提取位于 `graph/llm/enhancer.py`，通过 `EXTRACTION_PROMPT` 控制提取质量。

核心优化点：
1. 从用户搜索视角提取关键词
2. 聚焦文档核心内容（API名、方法名、关键特性）
3. 避免泛化词（HarmonyOS、API、使用）
4. 严格控制数量（5-10个）
5. 问题解决类关键词仅在文档确实覆盖时才加入
6. source_file 必须与输入路径精确匹配

### 提取缓存优化

缓存机制（`graph/builders/cache.py`）避免重复提取：

- 文件内容 SHA256 哈希（.md 文件去除 frontmatter）
- 缓存目录: `graphify-out/cache/`
- 支持命名空间（model + api_base + prompt_version）
- 增量构建: 仅处理新增/变更文件

## 图谱导出

### 导出命令

```bash
# 导出 JSON（默认，无节点数限制）
python cli.py export --format json --graph data/doc/graph.json

# 导出 HTML（vis-network 交互式可视化）
# 注意：超过 5000 节点时需使用 --max-nodes 裁剪
python cli.py export --format html --graph data/doc/graph.json --max-nodes 5000

# 导出 Markdown 报告
python cli.py export --format report --graph data/doc/graph.json

# 同时导出所有格式
python cli.py export --format all --graph data/doc/graph.json --max-nodes 5000

# 指定输出目录
python cli.py export --format html --graph data/doc/graph.json --max-nodes 3000 --output-dir output/
```

### `--max-nodes` 参数

HTML 导出使用 vis-network 力导向布局，节点过多会导致浏览器交互严重卡顿。当图谱节点数超过 vis-network 性能阈值时：

- **不设 `--max-nodes`**：如果节点超过 5000，HTML 导出会报错拒绝
- **设 `--max-nodes N`**：导出前裁剪图谱，只保留度最高的 N 个节点（及其之间的边），确保可视化流畅

当前文档图约 7008 节点，建议设 `--max-nodes 5000` 以获得流畅的浏览器体验。

### 导出格式说明

| 格式 | 输出文件 | 说明 |
|------|---------|------|
| JSON | graph_export.json | NetworkX node_link_data 格式，完整数据 |
| HTML | graph.html | vis-network 交互式可视化，节点大小按度缩放，社区颜色映射 |
| Report | GRAPH_REPORT.md | Markdown 报告（核心节点/惊奇连接/社区概览） |