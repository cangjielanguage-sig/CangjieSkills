---
name: cangjie-hmos-doc-search
description: "仓颉鸿蒙开发文档检索。当需要查询 HarmonyOS API 用法、仓颉标准库 API、开发指南、跨平台迁移对应、语义模糊问题定位时使用。通过知识图谱语义检索定位文档，agent 读取原文后组织回答。"
---

# 仓颉鸿蒙文档检索

通过知识图谱语义检索定位文档路径，agent 读取原文后组织回答。

## 适用场景

- HarmonyOS API / 开发指南查询（"Router.pushUrl 参数"）
- 仓颉标准库 / 扩展库 API 查询（"HashMap 怎么用"）
- 跨生态类比（"Android RecyclerView 对应鸿蒙什么"）
- 语义模糊问题（"列表卡顿怎么优化"、"白屏怎么办"）
- 构建报错 / 错误码排查

## 工作流

用户提问 → 提取关键词 → graph 搜索 → 读取原文 → 组织回答

## 步骤 1：提取关键词

从用户提问中提取搜索关键词，合并为空格分隔的查询串，3-8 词。

- **核心词**（1-2 词）：API 名或概念名（如 NavPathStack, HashMap），禁用泛化词（如 create, configuration, 使用, 方法, 怎么, 参数）
- **上下文词**（1-3 词）：限定核心词侧面（如 pushPath, timeout, 键值对）
- **同义词**（0-2 词）：概念级联想（如 navigation, persistence），宁少勿多。禁止主动添加其他生态术语，仅在用户明确提到跨生态类比时才加入

### 组合场景搜索策略

组合场景（"带下拉刷新的网络列表页怎么做"）应**按子意图分别搜索**，避免关键词合并后互相干扰。每个子意图独立搜索后合并结果组织回答。

### 构建报错关键词策略

| 错误模式 | 提取关键词 |
|---------|-----------|
| "cannot convert X to type Y" | 核心词=类型 Y |
| "undeclared identifier 'Z'" | 核心词=Z |
| "invalid named arguments prefix 'K:'" | 核心词=目标函数名 |
| "extra argument given for parameter" | 核心词=目标函数名 |
| "cannot access field 'F'" | 核心词=F |

不将完整错误信息、宏展开代码、行号作为关键词。

## 步骤 2：搜索

```bash
cd [Skill目录]/doc-graph
python cli.py search "关键词1 关键词2 关键词3" --graph doc --graph-path "data/doc/graph.json" --json -k 5
```

HarmonyOS API 搜索：`--graph-path "data/doc/graph.json"`
仓颉标准库搜索：`--graph-path "data/doc/graph_cj.json"`

agent 推荐使用 `--json` 输出，解析 `direct_hits[].source_file` 获取文档路径。

| 参数 | 说明 |
|------|------|
| `--graph doc` | 搜索文档图谱（必选） |
| `--graph-path` | 图谱文件路径（默认 data/doc/graph.json，cangjie 用 data/doc/graph_cj.json） |
| `--json` | JSON 输出（含分数、direct/related 分类，**agent 推荐**） |
| `-b` | 简洁文本输出（仅 label + 路径，非 JSON 场景备用） |
| `-k N` | 返回 N 条 |

### 结果结构

搜索返回两类结果：

- **direct_hits**（直接命中）：关键词匹配节点 label/keywords/description，分数高，**优先读取**
- **related_hits**（关联推荐）：通过 SEE_ALSO 边推荐的相邻节点，分数较低，作为补充

### 分数解读

| 分数范围 | 含义 | 处理 |
|---------|------|------|
| ≥ 400 | 高度相关 | 直接读取原文 |
| 200-400 | 较相关 | 可参考 |
| < 100 | 疑似噪声 | 忽略 |

## 步骤 3：读取原文

搜索返回的 `source_file` 是相对路径，需要拼接完整路径后读取：

**HarmonyOS 文档**（graph.json 返回）：
```
完整路径 = [Skill目录]/docs/harmonyos-6.0.2-15k/[source_file]
示例：source_file = "cj-arkui/cj-scroll-swipe-list.md"
     → docs/harmonyos-6.0.2-15k/cj-arkui/cj-scroll-swipe-list.md
```

**仓颉标准库/扩展库/内核文档**（graph_cj.json 返回）：
```
完整路径 = [skills目录]/cangjie-docs/[source_file]
示例：source_file = "cj-std/collection/class_HashMap.md"
     → ../../cangjie-docs/cj-std/collection/class_HashMap.md
```

### 读取策略

1. **只读 Top 1-2** 直接命中的 `source_file`，若无所需内容，再查看后续文件
2. **`.overview.md` 不含所需信息时**：根据其 Quick Navigation 段定位 1 个最相关子文件，总计仍不超过 2 个文件
3. **组合查询**：各子意图只取 Top1，不逐一全文阅读
4. **提取不粘贴**：从原文提取 API 签名、关键用法、注意事项，用自己的语言组织回答
5. **限制读取范围**：每个文件用 offset/limit 只读相关段落，不读全文

## 搜索失败与重试

| 失败模式 | 判断依据 | 处理 |
|---------|---------|------|
| 关键词泛化 | Top-1 score < 100 | 添加更具体的 API 名或类型名重新搜索 |
| 缺少生态术语 | 跨生态查询全部 MISS | 添加 Android/iOS 对应术语重新搜索 |
| 关键词过多/噪声 | Top-5 score 全部接近且偏低 | 减至 3-5 个核心词重新搜索 |
| 搜索结果无关 | Top-1 路径与查询意图不符 | 换关键词角度重新搜索 |
| CLI 不可用 | 命令报错或超时 | 回退到 Glob/Grep 搜索 `docs/` 目录，仍遵守"只读 Top 1-2"限制 |

重试时每次只调整 1-2 个关键词，不要一次性全部替换。
