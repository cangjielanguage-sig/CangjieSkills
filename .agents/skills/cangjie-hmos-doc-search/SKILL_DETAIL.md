# 仓颉鸿蒙文档检索 — 详细参考

本文档包含低频使用的详细规则和示例，日常检索无需阅读，仅在需要深入理解时参阅。

## 1. 查询意图识别

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

## 2. 跨生态映射参考

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

## 3. 隐含意图提取

| 用户表述 | 隐含意图 | 应添加关键词 |
|---------|---------|------------|
| "卡顿" | 性能优化 | LazyForEach, 懒加载, 性能优化 |
| "白屏" | 路由/加载问题 | Router, Navigation, 页面加载 |
| "不刷新" | 状态管理 | @State, 状态管理, 响应式 |
| "崩溃" | 异常处理 | 异常, 错误处理, try-catch |
| "连不上" | 网络/权限 | 网络请求, 权限, HTTP |

## 4. 组合查询拆分

当 query 包含多个独立概念时（特征词：加、带、与、同时、和等），拆分为多个子意图：

```
Query: "带下拉刷新的网络列表页"
→ 子意图1: 列表组件 → "List 列表"
→ 子意图2: 下拉刷新 → "Refresh 下拉刷新"
→ 子意图3: 网络请求 → "HTTP 网络请求"
→ 各子意图独立搜索，各取 Top1，合并结果组织回答
```

## 5. CLI 调用示例

```bash
# 基础搜索（HarmonyOS API）
python cli.py search "Router pushUrl 路由 页面跳转" --graph doc --graph-path "data/doc/graph.json" -b -k 5

# 仓颉标准库搜索
python cli.py search "HashMap 键值对 put" --graph doc --graph-path "data/doc/graph_cj.json" -b -k 5

# JSON 输出（含分数、direct/related 分类）
python cli.py search "List LazyForEach 列表" --graph doc --graph-path "data/doc/graph.json" --json -k 5

# 构建报错搜索
python cli.py search "BarState enum Scroll" --graph doc --graph-path "data/doc/graph.json" --json -k 3

# 跨生态类比搜索
python cli.py search "RecyclerView 列表" --graph doc --graph-path "data/doc/graph.json" -b -k 5
```

## 6. 完整工作流示例

### 精确概念查询

```
用户: "Router.pushUrl的参数"
→ 意图=精确概念
→ 关键词: core=["Router"], context=["pushUrl"], synonym=["路由"]
→ 搜索: cli.py search "Router pushUrl 路由" --graph doc --graph-path "data/doc/graph.json" -b -k 5
→ Top 1: cj-arkui/.../class_Router.md (score=900+)
→ 读取原文 → 提取 API 签名和参数 → 组织回答
```

### 仓颉标准库查询

```
用户: "HashMap怎么存键值对"
→ 意图=精确概念
→ 关键词: core=["HashMap"], context=["键值对", "put"]
→ 搜索: cli.py search "HashMap 键值对 put" --graph doc --graph-path "data/doc/graph_cj.json" -b -k 5
→ Top 1: cj-std/collection/class_HashMap.md (score=747)
→ 读取原文 → 提取 put 方法签名 → 组织回答
```

### 跨生态类比查询

```
用户: "Android RecyclerView 对应鸿蒙什么"
→ 意图=跨生态类比
→ 关键词: core=["List"], synonym=["RecyclerView"]
→ 搜索: cli.py search "List LazyForEach RecyclerView 列表" --graph doc --graph-path "data/doc/graph.json" -b -k 5
→ Top 1: cj-arkui/cj-scroll-swipe-list.md (score=800+)
→ 读取原文 → 说明 List/LazyForEach 与 RecyclerView 的映射关系
```

### 构建错误排查

```
错误: "cannot convert an integer literal to type 'Enum-BarState'"
→ 关键词: core=["BarState"], context=["enum"]
→ 搜索: cli.py search "BarState enum Scroll" --graph doc --graph-path "data/doc/graph.json" --json -k 3
→ Top 1: enum_BarState.md (score=600+)
→ 读取原文 → 提取 BarState 枚举值 → 组织回答
```

### 语义模糊查询

```
用户: "列表滑动卡顿怎么优化"
→ 意图=模糊症状 → 隐含意图=性能优化
→ 关键词: core=["LazyForEach"], context=["性能优化", "懒加载"]
→ 搜索: cli.py search "LazyForEach 性能优化 懒加载" --graph doc --graph-path "data/doc/graph.json" -b -k 5
→ Top 1: cj-arkui/cj-state-rendering-lazyforeach/LazyForEach/.overview.md (score=1000+)
→ 读取 .overview.md → Quick Navigation 定位性能优化子文件 → 组织回答
```

## 7. 结果结构详解

graph 搜索返回 JSON 结构（`--json` 模式）：

```json
{
  "query": "搜索关键词",
  "engine": "doc",
  "latency_ms": 0.5,
  "direct_hits": [
    {"label": "HashMap", "source_file": "cj-std/collection/class_HashMap.md", "score": 747},
    {"label": "collection_hashmap", "source_file": "cj-kernel/.../collection_hashmap.md", "score": 625}
  ],
  "related_hits": [
    {"label": "collection", "source_file": "cj-std/collection/.overview.md", "score": 373.5, "related_from": "HashMap", "relation_type": "see_also"}
  ]
}
```

- **direct_hits**：关键词直接匹配节点（label/keywords/description），按分数降序
- **related_hits**：通过 SEE_ALSO 边推荐的相邻节点，分数为 direct 的约 50%，标记来源和关系类型
- **score**：5 层累加（label×100 + keywords_zh×60 + keywords_en×25 + description×20 + related×10）
