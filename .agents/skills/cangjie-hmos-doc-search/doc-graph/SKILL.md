---
description: "仓颉鸿蒙开发文档知识图谱检索，适用于查询仓颉鸿蒙开发API用法、开发指南、跨平台迁移对应、语义模糊问题定位或组合场景方案检索。"
name: doc-graph
tags: [reference, platform, search]
version: "1.0.0"
---

# 鸿蒙仓颉文档知识图谱检索

本 Skill 仅提供**搜索运行时**（cli.py search/neighbors/path/explain/god-nodes/stats 等），图谱构建与评测由 `cangjie-hmos-doc-search-maintenance/graph/` 负责。

## 适用场景

- 仓颉鸿蒙开发 API / 开发指南查询
- 跨生态类比（"Android RecyclerView 对应鸿蒙什么"）
- 组合场景方案（"带下拉刷新的网络列表页怎么做"）
- 语义模糊症状（"列表卡顿怎么优化"、"白屏怎么办"）

## 工作流

```
用户查询 → 语义分析提取关键词 → CLI 搜索图谱 → 读取 source_file → 组织回答
```

## 步骤 1：关键词提取

按 core/context/synonym 分类，合并为 keywords_en + keywords_zh，总数不超过 10 词。

- **core**（1-2词）：最高区分度术语，严禁泛化词
- **context**（1-3词）：限定 core 侧面，严禁泛化域类别词
- **synonym**（0-2词）：概念级联想，宁少勿多

### 组合查询拆分

当 query 包含多个独立概念时（特征词：加、带、与、同时、和等），拆分为多个子意图分别搜索：

```
"带下拉刷新的网络列表页" → List / Refresh / HTTP 分别搜索
```

### 跨生态映射

当用户提到其他平台术语时，Core 必须是鸿蒙等价物，Synonym 包含原生态术语：

| 其他生态术语 | 鸿蒙等价物 | Core | Synonym |
|-------------|----------|------|---------|
| RecyclerView / FlatList | List, LazyForEach | List | RecyclerView, FlatList |
| SwipeRefreshLayout | Refresh | Refresh | SwipeRefreshLayout |
| Toast | PromptAction | PromptAction | Toast |
| SharedPreferences | PersistentStorage | PersistentStorage | SharedPreferences |
| Activity | UIAbility | UIActivity | Activity |
| LiveData | @State | @State | LiveData |

## 步骤 2：搜索图谱

```bash
python cli.py search "关键词1 关键词2 关键词3 ..." --graph doc -b -k 5
```

| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| 查询串 | MUST | — | 空格分隔的中英文关键词 |
| `--graph` | SHOULD | auto | doc / code / both |
| `-b` | SHOULD | — | Brief 模式，仅返回 label + source_file + score |
| `-k` | MAY | 5 | 直接命中返回数量 |

组合查询时对每个子意图分别调用，再融合结果。

### 辅助 CLI 命令

| 命令 | 用途 | 示例 |
|------|------|------|
| `neighbors` | 查看节点关联 | `python cli.py neighbors "List"` |
| `path` | 查找两节点间路径 | `python cli.py path "UIAbility" "WindowStage"` |
| `god-nodes` | 领域核心 API | `python cli.py god-nodes --top-n 10` |
| `explain` | 查看节点完整属性 | `python cli.py explain "节点ID"` |
| `stats` | 图谱统计 | `python cli.py stats` |
| `graphs` | 列出可用图谱 | `python cli.py graphs` |

## 步骤 3：结果解读

输出格式：

```
=== 直接命中 (N) ===
[分数] label | source_file

=== 关联推荐 (M) ===
[分数] label | source_file (来自 source_label, relation_type)
```

| 字段 | 说明 |
|------|------|
| `score` | ≥400 高度相关、200-400 较相关、<100 疑似噪声 |
| `label` | 文档主题名 |
| `source_file` | 文档相对路径（须拼接完整路径后读取） |
| `match_type` | label/keyword/description，label > keyword > description |
| `relation_type` | CONTAINS/see_also/recommends_api/typically_used_with |

## 步骤 4：读取原文

### 路径解析

```
完整绝对路径 = [cangjie-hmos-doc-search绝对路径]/docs/[source_file]
```

示例：
```
Skill 路径: "C:\CangjieSkills_3499\.agents\skills\cangjie-hmos-doc-search"
source_file: "harmonyos-6.0.2-15k/ui/components/List/.overview.md"
→ 完整路径: "C:\CangjieSkills_3499\.agents\skills\cangjie-hmos-doc-search\docs\harmonyos-6.0.2-15k\ui\components\List\.overview.md"
```

### 读取策略

1. 优先读取 Top1-2 直接命中的 source_file
2. 从 Top1 直接命中节点取 Top1-2 关联推荐的 source_file
3. 组合查询：各子意图取 Top1 + 关联 Top1
4. 提取不粘贴：从原文提取关键信息，用自己的语言组织回答

## 步骤 5：搜索失败与重试

| 原因 | 处理 |
|------|------|
| 关键词过于泛化 | 添加更具体的术语 |
| 缺少原生态术语 | 跨生态查询添加 Android/iOS 术语 |
| 关键词过多/噪音 | 减少噪音词，聚焦核心 |
| CLI 不可用 | 回退到 Glob/Grep 搜索 docs/ 目录 |

## 与 doc-card 的关系

本 Skill 与 `doc-card`（卡片检索）平权并存，按 query 类型分发。日常检索通过顶层 `unified_search.py --engine fusion` 自动融合 card + graph 结果。

精确命中优先 doc-card，语义/组合/跨生态优先 doc-graph。矛盾时 API 名/签名/参数以 doc-card 为单一事实源，doc-graph 只提供关联线索。