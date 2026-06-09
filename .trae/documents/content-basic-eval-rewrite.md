# Plan: 改写 content-basic.jsonl eval 用例

## 目标

改写 `content-basic.jsonl`，使 eval 用例：

1. 贴近真实用户查询（组合场景、跨生态类比、模糊症状、构建报错等）
2. 评分有区分度：当前 Skill 得分约 0.5，优化后可达 0.8+

## 评分区分度设计原理

skill-eval 的 `answer_score = sum(匹配权重) / sum(总权重)`，通过 `pattern_weights` 可以为不同 pattern 设不同权重：

* **核心 pattern**（权重高）：Skill 必须正确回答的关键知识点，如搜索入口、关键词提取策略、引擎选择

* **过程 pattern**（权重中）：体现 Skill 工作流质量的中间步骤，如子意图拆分、core/context 分类、路径解析

* **细节 pattern**（权重低）：锦上添花的精确细节，如具体参数值、score 阈值、Windows 兼容提示

**当前 Skill 的典型问题**（导致 \~0.5 分）：

* 组合场景未拆分子意图，直接合并搜索

* 关键词提取不够精确（泛化词、缺少 context）

* 引擎选择不当（全部用 fusion，未按场景选 card/graph）

* 未说明路径解析规则（`docs/[source_file]`）

**优化后 Skill**（可达 0.8+）：

* 正确拆分子意图并分别搜索

* 精确提取 core/context/synonym

* 按场景选择引擎

* 说明路径解析和读取策略

## 用例设计（7 条）

### 用例 1：组合场景 — 蓝牙权限 + 网络权限 + WebView

```json
{"input":"我要写一个仓颉鸿蒙应用，需要申请蓝牙和网络权限，且需要在界面上放置能操控的web组件，我应该怎么做？","expected_patterns":["unified_search\\.py","子意图|拆分|分别搜索","权限|permission","WebView","--engine"],"pattern_weights":[3,2,2,2,1],"min_score":0.5}
```

* 核心(3)：搜索入口 `unified_search.py`

* 过程(2)：组合场景必须拆分子意图

* 过程(2)：提取权限相关关键词

* 过程(2)：识别 WebView 组件

* 细节(1)：提及引擎选择

* **区分度**：当前 Skill 可能只给合并搜索命令（缺"拆分"），得 \~0.5；优化后拆分子意图，得 \~0.8

### 用例 2：模糊症状 — 界面卡顿

```json
{"input":"我的鸿蒙仓颉应用列表滑动很卡，怎么优化？","expected_patterns":["unified_search\\.py","LazyForEach|懒加载","性能优化|卡顿","core.*=|关键词.*提取","fusion|card|graph"],"pattern_weights":[3,2,2,1,1],"min_score":0.5}
```

* 核心(3)：搜索入口

* 过程(2)：从"卡顿"反推 LazyForEach/懒加载（隐含意图提取）

* 过程(2)：添加性能优化关键词

* 细节(1)：说明关键词提取策略（core/context 分类）

* 细节(1)：提及引擎选择

* **区分度**：当前 Skill 可能只搜索"卡顿 优化"，缺 LazyForEach 隐含意图，得 \~0.5；优化后正确反推，得 \~0.8

### 用例 3：跨生态类比 — Android Activity

```json
{"input":"我之前写Android的，鸿蒙的Activity对应什么？页面跳转怎么写？","expected_patterns":["unified_search\\.py","UIAbility","Navigation|Router","Activity","synonym|跨生态"],"pattern_weights":[3,2,2,1,1],"min_score":0.5}
```

* 核心(3)：搜索入口

* 过程(2)：映射 Activity → UIAbility

* 过程(2)：识别页面跳转 → Navigation/Router

* 细节(1)：保留 Activity 作为 synonym

* 细节(1)：提及跨生态映射规则

* **区分度**：当前 Skill 可能只搜"Activity"，未映射到 UIAbility，得 \~0.5；优化后正确映射，得 \~0.8

### 用例 4：构建报错

```json
{"input":"仓颉构建报错：cannot convert an integer literal to type 'Enum-BarState'，怎么解决？","expected_patterns":["unified_search\\.py","BarState","--engine\\s+card","core.*BarState|关键词.*BarState","enum"],"pattern_weights":[3,2,2,1,1],"min_score":0.5}
```

* 核心(3)：搜索入口

* 过程(2)：提取 BarState 为 core 关键词（而非整段错误信息）

* 过程(2)：构建报错应选 card 引擎

* 细节(1)：说明关键词提取策略

* 细节(1)：enum 作为 context

* **区分度**：当前 Skill 可能把整段错误信息当关键词，且未选 card 引擎，得 \~0.5；优化后精确提取+选 card，得 \~0.8

### 用例 5：动画 + 图形交互

```json
{"input":"我需要写一个界面，界面上有图形，点击后图形会变化，变化有动画效果","expected_patterns":["unified_search\\.py","子意图|拆分|分别搜索","动画|animate|animation","点击|手势|gesture","图形|shape"],"pattern_weights":[3,2,2,1,1],"min_score":0.5}
```

* 核心(3)：搜索入口

* 过程(2)：组合场景拆分（动画 vs 手势交互 vs 图形绘制）

* 过程(2)：识别动画相关关键词

* 细节(1)：识别点击/手势交互

* 细节(1)：识别图形/Shape

* **区分度**：当前 Skill 可能合并搜索"图形 点击 动画"产生噪声，得 \~0.5；优化后拆分子意图，得 \~0.8

### 用例 6：摄像头调用

```json
{"input":"我要调用摄像头，应该怎么写","expected_patterns":["unified_search\\.py","camera|Camera","权限|permission","core.*camera|关键词.*camera","source_file|路径|docs"],"pattern_weights":[3,2,2,1,1],"min_score":0.5}
```

* 核心(3)：搜索入口

* 过程(2)：识别 camera 关键词

* 过程(2）：摄像头需要权限（隐含意图）

* 细节(1)：说明关键词分类

* 细节(1)：提及路径解析（docs/\[source\_file]）

* **区分度**：当前 Skill 可能只搜 camera 未提及权限，得 \~0.5；优化后补充隐含权限意图，得 \~0.8

### 用例 7：结果解读 + 读取策略

```json
{"input":"搜索结果里 score 是 350 的文档值得读吗？应该怎么读取原文？","expected_patterns":["unified_search\\.py","较相关|200.*400","source_file","docs/","Top.*1.*2|只读"],"pattern_weights":[2,2,2,2,2],"min_score":0.5}
```

* 核心(2)：score 200-400 为较相关

* 核心(2)：通过 source\_file 定位

* 核心(2)：路径前缀 docs/

* 核心(2)：只读 Top 1-2

* 核心(2)：搜索入口

* **区分度**：当前 Skill 可能只说"读取 source\_file"，未说明 score 阈值和读取限制，得 \~0.5；优化后完整说明，得 \~0.8

## 实施步骤

1. 备份当前 `content-basic.jsonl`（仅 1 条用例）
2. 写入新的 7 条用例到 `content-basic.jsonl`
3. 用 `skill-eval --mode content --runner agent-command` 跑一遍，记录基线分数
4. 根据基线结果微调 `pattern_weights` 或 `min_score`，确保区分度合理

