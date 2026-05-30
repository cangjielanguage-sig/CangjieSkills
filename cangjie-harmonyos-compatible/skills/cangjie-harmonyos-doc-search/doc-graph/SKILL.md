---
description: "仓颉鸿蒙开发文档知识图谱检索，适用于查询仓颉鸿蒙开发API用法、开发指南、跨平台迁移对应、语义模糊问题定位或组合场景方案检索。"
name: doc-graph
tags: [reference, platform, search]
version: "1.0.0"
---

# 鸿蒙仓颉文档知识图谱检索

## 适用场景

在以下情况应优先使用本 Skill：

- 仓颉鸿蒙开发 API / 开发指南查询（组件用法、状态管理、生命周期、网络请求等）
- 跨生态类比查询（"Android RecyclerView 对应鸿蒙什么"）
- 组合场景方案检索（"带下拉刷新的网络列表页怎么做"）
- 语义模糊问题定位（"列表卡顿怎么优化"、"白屏怎么办"）

## 概述

本 Skill 提供基于 HarmonyOS 6.0.2 仓颉开发文档构建的知识图谱（`data/doc/graph.json`），用于快速定位仓颉鸿蒙开发文档路径。图谱职责是**索引定位**，Agent 职责是**语义理解、关键词提取、读取原文、组织回答**。

核心工作流：

```
用户查询 → 语义分析提取关键词 → CLI 搜索图谱 → 读取 source_file → 组织回答
```

## 快速流程

1. 分析用户查询意图，按 core/context/synonym 提取关键词并合并为 keywords_en/keywords_zh
2. 调用 CLI 搜索图谱，获取 `source_file` 路径列表
3. 读取路径对应的原文文档
4. 从原文提取详情组织回答

## 步骤 1：语义分析与关键词提取

### 1.1 查询意图识别

根据用户 query 特征识别类型：

| 查询类型 | 特征词/模式 | 关键词策略 |
|---------|------------|-----------|
| 精确概念 | 明确 API/组件名 | 直接提取 API 名 |
| 模糊症状 | 卡顿、白屏、不生效 | 从症状反推核心概念 |
| 组合场景 | 加、带、与、同时 | 拆分子意图，分别搜索 |
| 跨生态类比 | RecyclerView、FlatList、对应 | 映射鸿蒙等价物 + 原术语 |
| 对比查询 | 区别、对比、vs | 双侧关键词分别搜索 |
| 替代方案 | 除了、还有什么 | 核心概念 + 替代类词 |
| 错误排查 | 报错、异常 | 错误信息 + 相关组件 |
| 条件约束 | 在…时、后台 | 条件词 + 核心概念 |

### 1.2 语义分析提示词

在提取关键词前，Agent 应在内部使用以下提示词框架对用户 query 进行语义分析（无需输出 JSON 给用户，仅用于指导关键词提取）：

```
你是一个鸿蒙/仓颉开发文档的检索助手。用户提出了以下查询：

「{用户原始query}」

请从开发者视角分析此查询，执行以下任务：

1. 意图识别：判断查询属于以下哪种类型——精确概念、模糊症状、组合场景、跨生态类比、对比查询、替代方案、错误排查、条件约束。

2. 关键词提取（按以下严格规范）：

   a) core（核心词）——定位目标节点的核心锚点：
      - 从query中提取的最精确、最独特的标识符
      - 通常是API类名/方法名（如 HttpRequest, Router, CameraManager）
      - 严禁添加泛化概念词（如 create, parameters, timeout, configuration, list等普通动词/名词）
      - 每条1-2词，第1个词必须是query中最具区分度的术语
      - 跨生态类比时 Core 必须是鸿蒙等价术语

   b) context（上下文词）——限定core的具体侧面：
      - 必须是限定性技术术语：具体方法名、参数名、操作类型
        （如 pushUrl, once, getCameraList, timeout, destroyInstance）
      - 严禁泛化域类别词（如 HTTP request, network, multimedia, device management）
      - 来源：query中明确提到的子概念，或从core可直接推断的限定性术语
      - 每条1-3词

   c) synonym（联想词）——为Agent预留的推理联想空间：
      - 概念级联想优先（推荐）：如 persistence, HTTP client, background task,
        page navigation, data storage — 容易在文档描述中出现，有助于发现相关内容
      - 实现级联想谨慎（限每条最多1个）：如 OkHttp, URLSession, SharedPreferences
        — 是其他平台的具体实现名，在鸿蒙文档中不存在，仅当与鸿蒙概念高度对应时保留1个作为联想线索
      - 宁少勿多，0-2词即可，不确定就留空
      - 跨生态类比时 Synonym 包含原生态术语

3. 词形与禁止规则：

   a) 词形规范：
      - 单词优先：timeout > "request timeout"；camera > "camera manager"
      - 驼峰/API名保持原样：HttpRequest, pushUrl, geometryTransition
      - 小写概念词用单词：persistence, navigation, storage
      - 多词短语拆为单词分放不同类别："OkHttp timeout" → OkHttp(synonym) + timeout(context)
      - 单个关键词不超过3个词

   b) 长度约束：
      - core.en/zh:     1-2词（第1词必须是最高区分度术语）
      - context.en/zh:  1-3词（每个词必须是限定性术语）
      - synonym.en/zh:  0-2词（概念级联想优先，留空也合理）
      - 整条所有关键词总数不超过10个词

   c) 禁止项：
      - 泛化域类别词作 core/context（network, device, management, configuration）
      - 多词短语作关键词（"OkHttp timeout", "network timeout"）
      - 日常疑问词（怎么, 什么, 如何）
      - core中混入普通动词/名词（create, get, set, list, start）→ 放 context
      - 内部实现细节（ohos.request, cj-app-file, func_startBLEScan, 模块包名）

4. 内部输出格式（按此 JSON 结构组织，不展示给用户）：
{
  "intent_type": "意图类型",
  "core_en": ["核心英文关键词"],
  "core_zh": ["核心中文关键词"],
  "context_en": ["上下文英文关键词"],
  "context_zh": ["上下文中文关键词"],
  "synonym_en": ["联想英文关键词"],
  "synonym_zh": ["联想中文关键词"],
  "keywords_en": ["合并去重后的所有英文关键词"],
  "keywords_zh": ["合并去重后的所有中文关键词"]
}

其中 keywords_en = core_en + context_en + synonym_en 合并去重（保持原序）；
     keywords_zh = core_zh + context_zh + synonym_zh 合并去重（保持原序）。
```

### 1.3 跨生态映射参考

当用户提到其他平台术语时，Core 必须是鸿蒙等价物，Synonym 包含原生态术语：

| 其他生态术语 | 鸿蒙等价物 | Core | Synonym |
|-------------|----------|------|---------|
| RecyclerView / FlatList | List, LazyForEach | List | RecyclerView, FlatList |
| SwipeRefreshLayout | Refresh | Refresh | SwipeRefreshLayout |
| Toast | PromptAction | PromptAction | Toast |
| WebView | WebView | WebView | — |
| Navigation (Android) | Navigation, Router | Navigation | Intent |
| SharedPreferences | PersistentStorage | PersistentStorage | SharedPreferences |
| Activity | UIAbility | UIAbility | Activity |
| LiveData | @State | @State | LiveData |
| ViewModel | 状态管理 | 状态管理 | ViewModel |

### 1.4 隐含意图提取

| 用户表述 | 隐含意图 | 应添加关键词 |
|---------|---------|------------|
| "卡顿" | 性能优化 | LazyForEach, 懒加载, 性能优化 |
| "白屏" | 路由/加载问题 | Router, Navigation, 页面加载 |
| "不刷新" | 状态管理 | @State, 状态管理, 响应式 |
| "崩溃" | 异常处理 | 异常, 错误处理, try-catch |
| "连不上" | 网络/权限 | 网络请求, 权限, HTTP |

### 1.5 组合查询拆分

当 query 包含多个独立概念时（特征词：加、带、与、同时、和等），拆分为多个子意图：

```
Query: "带下拉刷新的网络列表页"
→ 子意图1: 列表组件 (List)
→ 子意图2: 下拉刷新 (Refresh)
→ 子意图3: 网络请求 (HTTP)

Query: "文件下载加进度条显示"
→ 子意图1: 文件下载 (download)
→ 子意图2: 进度条显示 (Progress)
```

## 步骤 2：搜索图谱

**工作目录**：所有 CLI 命令需在 `cangjie-harmonyos-doc-search/doc-graph/` 目录下执行，以确保能找到 `cli.py` 和 `data/doc/graph.json`。

关键词提取完成后，将 keywords_en 和 keywords_zh 合并为一个查询串进行 OR+累加搜索。

**调用方式**：

```bash
python cli.py search "关键词1 关键词2 关键词3 ..." --graph doc -b -k 5
```

**参数说明**：

| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| 查询串 | MUST | — | 空格分隔的中英文关键词（keywords_en + keywords_zh 合并） |
| `--graph` | SHOULD | auto | 选择图谱：doc（文档图）、code（源码图）、both（双图并行） |
| `-b` | SHOULD | — | Brief 模式，仅返回 label + source_file + score，节省 Token |
| `-k` | MAY | 5 | 直接命中返回数量 |

**示例**：

```bash
# 精确概念搜索
python cli.py search "Router pushUrl 路由 页面跳转" --graph doc -b -k 5

# 跨生态搜索
python cli.py search "List RecyclerView 列表 长列表 懒加载" --graph doc -b -k 5

# 双图并行
python cli.py search "HTTP 网络请求 request" --graph both -b
```

**组合查询时**：对每个子意图分别调用，再融合结果：

```bash
python cli.py search "List 列表 列表组件" --graph doc -b -k 3
python cli.py search "Refresh 下拉刷新 刷新" --graph doc -b -k 3
python cli.py search "HTTP request 网络请求" --graph doc -b -k 3
```

### 2.1 辅助 CLI 命令

| 命令 | 用途 | 示例 |
|------|------|------|
| `stats` | 查看图谱统计（节点数、边数） | `python cli.py stats` |
| `graphs` | 列出可用图谱 | `python cli.py graphs` |
| `explain` | 查看节点完整属性 | `python cli.py explain "节点ID"` |
| `neighbors` | 查看节点关联 | `python cli.py neighbors "List"` |
| `path` | 查找两节点间路径 | `python cli.py path "UIAbility" "WindowStage"` |

## 步骤 3：结果解读

CLI 搜索输出格式：

```
=== 直接命中 (N) ===
[分数] label | source_file

=== 关联推荐 (M) ===
[分数] label | source_file (来自 source_label, relation_type)
```

### 3.1 输出字段含义

| 字段 | 说明 | Agent 用途 |
|------|------|-----------|
| `score` | 匹配分数，越高越相关 | 优先读取高分文档 |
| `label` | 文档主题名 | 判断相关性 |
| `source_file` | 文档相对路径 | **必须拼接为完整路径后读取**（见步骤4.1） |
| `match_type` | 匹配类型：label/keyword/description | 判断命中质量 |
| `related_from` | 关联来源节点 | 理解关联推荐来源 |
| `relation_type` | 边类型：CONTAINS/see_also/recommends_api/typically_used_with | 理解关联语义 |

### 3.2 匹配类型优先级

label 精确匹配 > keyword 精确匹配 > label 包含匹配 > keyword 包含匹配 > description 匹配

- **label** 命中：文档主题直接对应查询核心概念，优先读取
- **keyword** 命中：文档关键词包含查询词，次优先读取
- **description** 命中：语义兜底，相关性较弱
- **related** 命中：关联推荐，从直接命中节点扩展的相关文档

### 3.3 分数参考

| 分数范围 | 相关性 | 建议 |
|---------|--------|------|
| ≥ 400 | 高度相关 | 必须读取 |
| 200-400 | 较相关 | 推荐读取 |
| 100-200 | 弱相关 | 可选读取 |
| < 100 | 疑似噪声 | 跳过或重试 |

## 步骤 4：读取原文并组织回答

### 4.1 文档路径解析

搜索返回的 `source_file` 是相对路径，基准目录为**`cangjie-harmonyos-doc-search/docs/`**。

按以下公式拼接完整绝对路径：

```
完整绝对路径 = [cangjie-harmonyos-doc-search绝对路径] + "/docs/" + source_file
```

**示例**：
```
Skill 绝对路径: "C:\CangjieSkills_3499\.agents\skills\cangjie-harmonyos-doc-search"
source_file:    "harmonyos-6.0.2-15k/ui/components/List/.overview.md"
→ 完整绝对路径: "C:\CangjieSkills_3499\.agents\skills\cangjie-harmonyos-doc-search\docs\harmonyos-6.0.2-15k\ui\components\List\.overview.md"
```

**注意**：
- 使用 Read 工具读取该绝对路径的文件内容

### 4.2 读取策略

1. 优先读取 Top1-2 直接命中的 `source_file`
2. 从 Top1 直接命中节点取 Top1-2 关联推荐的 `source_file`
3. 组合查询：各子意图取 Top1 + 关联 Top1

### 4.3 文档内容提取要点

从原文中提取：

- **API 名称和签名**：回答"怎么调用"
- **参数说明**：回答"参数是什么"
- **使用示例**：回答"怎么用"
- **注意事项/限制**：回答"有什么限制"
- **替代方案**：回答"还有什么方法"

### 4.4 回答组织规范

- 列出每个 `source_file` 的相关性说明
- 组合查询标注各结果对应哪个子意图
- 跨生态查询说明映射关系（如 RecyclerView → List + LazyForEach）
- 搜索无结果时分析原因并建议调整关键词

## 步骤 5：搜索失败与重试

### 5.1 未命中分析

| 原因 | 处理方式 |
|------|---------|
| 关键词过于泛化 | 添加更具体的术语（Router → Router.pushUrl） |
| 缺少原生态术语 | 跨生态查询添加 Android/iOS 术语到 Synonym |
| 意图识别错误 | 重新分析用户真实需求 |
| 关键词过多/噪音 | 减少噪音词，聚焦核心关键词 |

### 5.2 重试流程

1. 第一次搜索结果不理想 → 分析未命中原因
2. 调整关键词（增删改） → 重新搜索
3. 仍无结果 → 检查 `data/doc/graph.json` 是否存在相关文档域

### 5.3 CLI 执行失败兜底

如果 CLI 命令执行失败（Python 环境问题、图谱文件损坏等），按以下降级策略处理：

1. 检查 `python cli.py stats` 是否可执行，确认图谱是否正常加载
2. 若 CLI 完全不可用，回退到直接搜索 `docs/` 目录：
   - 使用 Glob 工具按关键词匹配文件名
   - 使用 Grep 工具在文档内容中搜索关键词
3. 若仍无法定位，尝试使用 `cangjie-harmonyos-doc-search` 顶层 Skill（`../SKILL.md`）作为备选

### 5.4 图谱不可用时的处理

如果 `data/` 目录下没有对应领域的图谱数据（如 `data/doc/graph.json` 缺失或为空），按以下流程处理：

1. 检查图谱是否存在：

```bash
python cli.py stats
```

2. 若图谱缺失或领域覆盖不足，参阅 `BUILD_GUIDE.md` 重新构建图谱：

```bash
python cli.py build-doc ../docs/harmonyos-6.0.2-15k --enhance
```

构建完成后重新执行搜索流程。

## 完整工作流示例

### 精确概念查询

```
用户: "Router.pushUrl的参数"
→ 意图: 精确概念
→ 关键词: core_en=["Router"], core_zh=["路由", "页面跳转"],
           context_en=["pushUrl"], context_zh=["参数"]
→ keywords: en=["Router","pushUrl"], zh=["路由","页面跳转","参数"]
→ CLI: python cli.py search "Router pushUrl 路由 页面跳转 参数" --graph doc -b
→ 返回 source_file: "arkui\router\pushUrl\.overview.md"
→ 拼接绝对路径: [cangjie-harmonyos-doc-search绝对路径]\doc-graph\docs\harmonyos-6.0.2-15k\arkui\router\pushUrl\.overview.md
→ Read 读取原文 → 组织回答
```

### 跨生态类比查询

```
用户: "Android RecyclerView 对应鸿蒙什么"
→ 意图: 跨生态类比
→ 关键词: core_en=["List","LazyForEach"], core_zh=["列表","长列表"],
           synonym_en=["RecyclerView","FlatList"], synonym_zh=["懒加载"]
→ keywords: en=["List","LazyForEach","RecyclerView","FlatList"], zh=["列表","长列表","懒加载"]
→ CLI: python cli.py search "List LazyForEach RecyclerView FlatList 列表 长列表 懒加载" --graph doc -b
→ 返回 source_file: "ui\components\List\.overview.md"
→ 拼接绝对路径: [cangjie-harmonyos-doc-search绝对路径]\doc-graph\docs\harmonyos-6.0.2-15k\ui\components\List\.overview.md
→ Read 读取原文 → 说明映射关系
```

### 组合场景查询

```
用户: "带下拉刷新的网络列表页怎么做"
→ 意图: 组合场景 → 拆分为 3 个子意图
→ 子意图1: 列表 (List, 列表)
→ 子意图2: 刷新 (Refresh, 下拉刷新)
→ 子意图3: 网络请求 (HTTP, 网络请求)
→ CLI: 分别搜索 3 次
→ 返回 5 个 source_file，分别拼接路径后 Read 读取 → 组合方案回答
```

### 语义模糊查询

```
用户: "列表滑动卡顿怎么优化"
→ 意图: 模糊症状 → 隐含: 性能优化
→ 关键词: core_en=["List","LazyForEach"], core_zh=["列表","长列表"],
           context_en=["scroll","performance"], context_zh=["滑动","卡顿"],
           synonym_en=["RecyclerView"], synonym_zh=["懒加载","性能优化"]
→ keywords: en=["List","LazyForEach","scroll","performance","RecyclerView"], zh=["列表","长列表","滑动","卡顿","懒加载","性能优化"]
→ CLI: python cli.py search "List LazyForEach scroll performance RecyclerView 列表 长列表 滑动 卡顿 懒加载 性能优化" --graph doc -b
→ 返回 source_file: "ui\performance\optimization\.overview.md"
→ 拼接绝对路径: [cangjie-harmonyos-doc-search绝对路径]\doc-graph\docs\harmonyos-6.0.2-15k\ui\performance\optimization\.overview.md
→ Read 读取原文 → 组织回答
```

## 构建与维护

图谱构建、节点定义、打分规则、LLM 增强配置等详见 `cangjie-harmonyos-doc-search/doc-graph/BUILD_GUIDE.md`。