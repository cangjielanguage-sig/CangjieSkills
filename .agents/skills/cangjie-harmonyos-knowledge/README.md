# Cangjie HarmonyOS Knowledge

面向仓颉鸿蒙应用开发 Agent 的本地知识库。它把 HarmonyOS API 与开发指南预处理为 SQLite 检索索引，并随发布件提供完整的 256 维文档向量。系统不依赖 LLM，也不包含生成或重排序模型；可选的 `text-embedding-v4` 只用于把运行时自然语言查询转换为向量。

## 发布内容

```text
cangjie-harmonyos-knowledge/
├── SKILL.md                     # Agent 工作流
├── README.md                    # 技术、使用和维护说明
├── data/
│   ├── docs/                    # 权威 Markdown 语料
│   │   ├── API/
│   │   └── Guide/
│   └── index.sqlite             # 词法索引、结构化数据和 256 维向量
├── scripts/
│   ├── knowledge.py             # 唯一公开 CLI
│   ├── evaluate.py              # 检索评测
│   ├── run_tests.py             # 单元及在线测试入口
│   └── knowledge_core/          # 内部实现
├── tests/
│   ├── test_core.py
│   └── cases/                   # 标准、留出、语义、域外评测集
└── references/
    └── maintenance.md           # 发布维护清单
```

当前发布索引包含：

| 项目 | 数量 |
| --- | ---: |
| Markdown 文档 | 648 |
| 章节 | 12,324 |
| API 符号 | 6,271 |
| 代码示例 | 11,008 |
| 文档链接 | 10,234 |
| 256 维文档向量 | 12,324 |

## 快速使用

所有命令都可以从任意工作目录执行：

```powershell
python -B <skill-root>/scripts/knowledge.py doctor --strict
python -B <skill-root>/scripts/knowledge.py query "TextInput onChange" --top-k 3
python -B <skill-root>/scripts/knowledge.py symbol Button
python -B <skill-root>/scripts/knowledge.py read "docs/API/arkui-cj/cj-text-input-textinput.md#func-onchangestring---unit"
```

自然语言、跨语言或重度改写查询需要运行时查询向量：

```powershell
$env:DASHSCOPE_API_KEY = "<value>"
python -B <skill-root>/scripts/knowledge.py query "persist user settings across app launches" --top-k 3
```

未配置密钥、服务超时或响应无效时，查询自动退回符号、FTS 和结构化检索。精确 API 查询通常不会调用向量服务。离线退化路径不是语义模型：它适合符号和具体平台概念，但不承诺稳定理解重度改写的自然语言。

### CLI 能力

| 命令 | 用途 |
| --- | --- |
| `doctor --strict` | 检查语料映射、SQLite、FTS、链接和向量覆盖率 |
| `query` | 自适应检索 API、指南、错误码、权限和示例 |
| `symbol` | 精确查询 API 符号、签名、成员和示例 |
| `read` | 按 `path#anchor` 读取指定章节 |
| `versions` | 查看、逻辑删除或压缩文档版本 |
| `build` | 原子重建或增量更新索引 |
| `serve` | 启动本地 HTTP 服务与管理面板 |
| `mcp` | 启动 stdio MCP 服务 |

## 技术原理

```text
data/docs/*.md
       │
       ▼
确定性 Markdown 解析
       │
       ├── 文档、章节、锚点、面包屑
       ├── API 符号、签名、父子关系
       ├── 代码块、import、附近符号
       ├── 权限、SysCap、起始版本、错误码
       └── 内部链接
       │
       ▼
SQLite 结构化表 + unicode61 FTS + trigram FTS
       │
       ├── text-embedding-v4 文档向量（构建期）
       └── 链接关系和多版本元数据
       │
       ▼
data/index.sqlite
```

### Markdown 预处理

1. 递归读取 `data/docs/` 下的 Markdown，并以文件内容 SHA-256 标识版本。
2. 忽略代码围栏内的伪标题，按真实 Markdown 标题切分章节。
3. 生成与源文档兼容的稳定锚点、行号范围和标题面包屑。
4. 根据 `docs/API`、`docs/Guide` 及路径层级识别文档类型和 Kit。
5. 从 API 标题中确定性提取 `func`、`class`、`enum`、`prop` 等符号及签名。
6. 提取代码块、import、附近符号、普通链接和锚点链接。
7. 使用规则提取 `ohos.permission.*`、`SystemCapability.*`、起始版本和错误码，不调用模型推断。

### 词法与结构化索引

每个章节写入 `documents`、`sections`、`symbols`、`examples`、`links` 等结构化表，同时建立三类 FTS5 索引：

- `unicode61` 章节索引：适合英文标识符、中文词项和普通文本。
- `trigram` 章节索引：补充子串、CamelCase 和不完整 API 名称匹配。
- `unicode61` 示例索引：检索代码、import 和附近符号。

索引还保存权限、SysCap、版本、错误码、文档关系与多版本状态，因此精确 API 查询不依赖向量模型。

### 文档向量预处理

每个章节的向量输入由以下字段按顺序组成：

1. 文档标题。
2. Kit 名称。
3. 章节面包屑。
4. 章节标题。
5. 章节正文前 4,000 个字符。

构建器以 `batch_size = 10` 调用 `text-embedding-v4`，默认输出 256 维向量。返回结果必须满足：

- 输入与输出一一对应。
- 所有向量维度一致且等于请求维度。
- 所有数值有限。
- 每个发布章节都有匹配的 provider、model 和 dimension 向量。

向量以 float32 二进制写入 SQLite。缓存键包含服务地址、协议、模型、请求维度和输入文本哈希，避免跨模型或跨端点误用缓存。

发布构建使用临时 `index.building.sqlite`。只有解析、FTS、向量覆盖率和事务提交全部成功后才替换 `data/index.sqlite`；失败时保留上一版索引。

### 查询流程

```text
查询
 ├── 符号精确匹配
 ├── unicode61 / trigram FTS
 ├── 示例、数字、错误码和结构化意图
 └── 质量与覆盖率调整
          │
          ├── 高置信词法结果：直接返回
          └── 弱词法结果：查询向量 → 余弦相似度 → 语义结果
```

向量路径只在以下条件同时满足时启用：

- 配置模式允许查询向量。
- 查询向量服务可用。
- 发布索引包含匹配 provider/model/dimension 的向量。
- 词法最高分低于内部直达阈值。

长随机标识符、高置信域外主题、竞争技术生态、语料中不存在的显式技术标识符，以及低于 `min_similarity = 0.40` 的向量结果会被拒绝。域边界在词法和向量路径之前执行，防止“最近邻必然有结果”把无关问题伪装成鸿蒙答案。带 HarmonyOS/OpenHarmony/ArkUI/仓颉标记的对比或迁移问题不会被该边界拒绝。当前实现直接扫描匹配的 SQLite 向量并计算余弦相似度，没有 ANN、LLM 或 reranker。

运行时查询缓存默认位于：

```text
~/.cangjie/cache/cangjie-harmonyos-knowledge/vector_cache.sqlite
```

缓存不可写不会阻断检索，只会失去查询向量复用能力。使用 `--index-dir` 测试其他索引时，缓存跟随该测试索引目录，避免污染正式缓存。

## 配置

统一配置文件名为 `cangjie.skills.toml`。知识库的发布默认值为：

```toml
[knowledge]
version = "default"

[knowledge.embedding]
mode = "search"
api_format = "dashscope"
model = "text-embedding-v4"
base_url = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding"
api_key_env = "DASHSCOPE_API_KEY"
dimensions = 256
min_similarity = 0.40
batch_size = 10
timeout_seconds = 60.0
max_retries = 2
```

`mode` 的含义：

- `search`：默认模式；弱查询使用发布向量，失败时确定性降级。
- `off`：只使用确定性检索。
- `index`：严格构建文档向量；失败时不替换旧索引。
- `all`：严格构建并允许查询向量，主要用于维护。

完整的配置层级、默认值和降级策略见相邻 Skill 的 `cangjie-harmonyos-dev/references/configuration.md`。

## 维护

### 发布质量门

```powershell
python -B <skill-root>/scripts/knowledge.py doctor --strict
python -B <skill-root>/scripts/run_tests.py
python -B <skill-root>/scripts/evaluate.py --embedding-mode off --fail-under 1.00 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/holdout.json --embedding-mode off --fail-under 0.90 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/semantic.json --embedding-mode off --fail-under 0.40 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/ood.json --embedding-mode off --fail-under 1.00 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/agent_patterns.json --embedding-mode off --fail-under 1.00 --max-p95-ms 750
```

启用真实向量测试：

```powershell
$env:CANGJIE_KNOWLEDGE_RUN_LIVE_EMBEDDING = "1"
$env:DASHSCOPE_API_KEY = "<value>"
python -B <skill-root>/scripts/run_tests.py
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/semantic.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 0.95 --max-p95-ms 5000
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/ood.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 1.00 --max-p95-ms 5000
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/agent_patterns.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 1.00 --max-p95-ms 5000
```

五套评测数据的职责：

| 文件 | 目的 |
| --- | --- |
| `retrieval.json` | 稳定的 API 与常规任务回归 |
| `holdout.json` | 不参与别名和排序调优的独立留出集 |
| `semantic.json` | 跨语言和重度改写；离线只设诊断下限，在线向量门要求 95% |
| `ood.json` | 无关领域和竞争技术生态的拒答 |
| `agent_patterns.json` | Canvas、ForEach、`@Prop` 和 `@Builder bind` 等 Agent 高频编码合约 |

### 重建发布索引

```powershell
$env:DASHSCOPE_API_KEY = "<value>"
python -B <skill-root>/scripts/knowledge.py build --embedding-mode index
python -B <skill-root>/scripts/knowledge.py versions compact
python -B <skill-root>/scripts/knowledge.py doctor --strict
```

修改同一文档版本时可增加 `--incremental`；不同 SDK 文档必须使用新的 `--version`。完整发布清单见 [references/maintenance.md](references/maintenance.md)。

## 设计边界

- HarmonyOS、ArkUI、Kit、权限、SysCap 和平台错误属于本知识库。
- 仓颉语言、标准库、stdx API 和 cjpm 知识属于 `cangjie-coding`；鸿蒙 stdx 二进制下载与配置属于 `harmonyos-project-bootstrap`。
- ArkTS/仓颉互操作属于 `cangjie-arkts-interop`。
- 不把 API 密钥、查询缓存、临时索引或评测报告写入发布数据目录。
- 不使用 LLM、生成模型或 reranker 补全文档事实。
