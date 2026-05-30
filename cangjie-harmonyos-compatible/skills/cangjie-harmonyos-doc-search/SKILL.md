---
name: cangjie-harmonyos-doc-search
description: "鸿蒙仓颉开发文档检索，适用于仓颉鸿蒙开发 API 用法、开发指南、跨平台迁移对应、语义模糊问题定位或组合场景方案检索。"
tags: [workflow, platform, search]
---

# 鸿蒙仓颉文档检索

职责是**索引定位**，Agent 责责**语义理解、关键词提取、读取原文、组织回答**。

## 适用场景

- 仓颉鸿蒙开发 API / 开发指南查询
- 跨生态类比（"Android RecyclerView 对应鸿蒙什么"）
- 组合场景方案（"带下拉刷新的网络列表页怎么做"）
- 语义模糊症状（"列表卡顿怎么优化"、"白屏怎么办"）
- 构建报错 / 错误码排查

## 工作流

```
用户查询 → 语义分析提取关键词 → 搜索 → 读取原文 → 组织回答
```

## 步骤 1：关键词提取

按 core/context/synonym 分类，合并为 `keywords_en` + `keywords_zh`，总数不超过 10 词。

- **core**（1-2词）：最高区分度术语（如 NavPathStack, @State），严禁泛化词（如 create, configuration）
- **context**（1-3词）：限定 core 侧面（如 pushPath, timeout），严禁泛化域类别词
- **synonym**（0-2词）：概念级联想（如 navigation, persistence），宁少勿多。**禁止主动添加其他生态术语**（如 RecyclerView、SwipeRefreshLayout），仅在用户明确提到跨生态类比时才加入

### 组合场景搜索策略

组合场景（"信息流App用什么组件"、"带下拉刷新的网络列表页"）应**严格按子意图分别搜索**，避免关键词合并后互相干扰产生噪声。每个子意图独立搜索后合并结果组织回答。

### 构建报错关键词策略

| 错误模式 | 提取关键词 |
|---------|-----------|
| "cannot convert X to type Y" | core=类型Y |
| "undeclared identifier 'Z'" | core=Z |
| "invalid named arguments prefix 'K:'" | core=目标函数名 |
| "extra argument given for parameter" | core=目标函数名 |
| "cannot access field 'F'" | core=F |

不将完整错误信息、宏展开代码、行号作为关键词。

详细规则（意图识别、跨生态映射、隐含意图、组合查询拆分）见 `SKILL_DETAIL.md`。

## 步骤 2：搜索

```bash
python unified_search.py "<query>" [options]
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `query` | — | 关键词合并后的查询串 |
| `--engine` | `fusion` | `fusion` / `card` / `graph` |
| `--json` | off | 输出 JSON |
| `--limit` | `5` | 直接命中数量上限 |

场景指引：**默认用 fusion**；精确 API/构建报错 → `card`；需要纯图遍历（neighbors/path/god-nodes/community）→ `graph`；其余一律 fusion。

`--engine graph` 可附加子命令：`--cmd neighbors <node>` / `path <s> <t>` / `god-nodes [n]` / `community <id>` / `explain <node>`。

详细调用示例见 `SKILL_DETAIL.md`。

## 步骤 3：结果解读

输出字段：`label`（主题名）、`source_file`（相对路径）、`score`（分数，≥400 高度相关、200-400 较相关、<100 疑似噪声）、`engine`（来源引擎）。

## 步骤 4：读取原文

### 路径解析

```
完整绝对路径 = [Skill目录]/docs/[source_file]
```

示例：
```
Skill 目录: "C:\CangjieSkills_3499\.agents\skills\cangjie-harmonyos-doc-search"
source_file: "harmonyos-6.0.2-15k/cj-scroll-swipe-list/List/.overview.md"
→ 完整绝对路径: "C:\CangjieSkills_3499\.agents\skills\cangjie-harmonyos-doc-search\docs\harmonyos-6.0.2-15k\cj-scroll-swipe-list\List\.overview.md"
```

### 读取策略（硬性约束）

1. **只读 Top 1-2** 直接命中的 `source_file`，若无所需内容，再查看后续文件
2. **overview.md 不含所需信息时**：根据其 Quick Navigation 段定位 1 个最相关子文件，总计仍不超过 2 个文件
3. **组合查询**：各子意图只取 Top1，不逐一全文阅读
4. **提取不粘贴**：从原文提取 API 签名、关键用法、注意事项，用自己的语言组织回答
5. **限制读取范围**：每个文件用 offset/limit 只读相关段落，不读全文

## 步骤 5：搜索失败与重试

| 原因 | 处理 |
|------|------|
| 关键词泛化 | 添加更具体术语 |
| 缺少原生态术语 | 跨生态查询添加 Android/iOS 术语 |
| 关键词过多/噪音 | 减少噪音词，聚焦 core |
| CLI 不可用 | 回退到 Glob/Grep，但仍遵守"只读 Top 1-2"限制 |

## 索引构建

首次使用或文档更新后，通过维护 Skill 构建卡片索引：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search-maintenance/builder/build_index_v3.py --mode rule
```

如需离线 LLM 语义增强：

```bash
python <CangjieSkills>/.agents/skills/cangjie-harmonyos-doc-search-maintenance/builder/build_index_v3.py --mode rule+llm
```

`rule+llm` 仅在构建阶段调用 OpenAI 兼容 API，查询运行时不要求用户配置任何外部模型参数。

构建产物写入 `doc-card/index/`：

- `manifest.json`
- `tasks.jsonl`
- `apis.jsonl`
- `examples.jsonl`
- `docs.jsonl`
- `aliases.json`
- `search.db`

日常检索仍使用顶层 `unified_search.py`，不直接调用构建脚本。

## 子技能

仅在需要深入理解引擎内部机制时参阅：
- **doc-card**：详见 `doc-card/SKILL.md`
- **doc-graph**：详见 `doc-graph/SKILL.md`

日常检索始终使用顶层 `unified_search.py`，无需直接调用子技能 CLI。
