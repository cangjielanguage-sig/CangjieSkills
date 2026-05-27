# 鸿蒙仓颉文档检索 — 详细参考

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
→ 子意图1: 列表组件 (List, 列表)
→ 子意图2: 下拉刷新 (Refresh, 下拉刷新)
→ 子意图3: 网络请求 (HTTP, 网络请求)
→ 合并搜索: "List Refresh HTTP 列表 下拉刷新 网络请求"
```

## 5. CLI 调用示例

```bash
# 默认搜索
python unified_search.py "Router pushUrl 路由 页面跳转 参数" --json --limit 5

# 精确 API 查找
python unified_search.py "List" --engine card --json --limit 5

# 语义模糊/组合场景
python unified_search.py "卡顿优化" --engine graph --json --limit 5

# 构建报错
python unified_search.py "BarState enum Scroll" --engine card --json --limit 3

# 图遍历
python unified_search.py "" --engine graph --cmd neighbors List
python unified_search.py "" --engine graph --cmd path UIAbility WindowStage
python unified_search.py "" --engine graph --cmd god-nodes 10
```

## 6. 完整工作流示例

### 精确概念查询

```
用户: "Router.pushUrl的参数"
→ 意图=精确概念
→ 关键词: core=["Router"], context=["pushUrl"], synonym=["路由"]
→ 合并: "Router pushUrl 路由 参数"
→ CLI: unified_search.py "Router pushUrl 路由 参数" --json --limit 5
→ 读取 Top 1 source_file → 提取 API 签名和参数 → 组织回答
```

### 跨生态类比查询

```
用户: "Android RecyclerView 对应鸿蒙什么"
→ 意图=跨生态类比
→ 关键词: core=["List"], synonym=["RecyclerView"]
→ 合并: "List LazyForEach RecyclerView 列表"
→ CLI: unified_search.py "List LazyForEach RecyclerView 列表" --json
→ 读取 Top 1 → 说明映射关系
```

### 构建错误排查

```
错误: "cannot convert an integer literal to type 'Enum-BarState'"
→ 关键词: core=["BarState"], context=["enum"]
→ CLI: unified_search.py "BarState enum Scroll" --engine card --json --limit 3
→ 读取 Top 1 → 提取 BarState 枚举值 → 组织回答
```

## 7. 子技能内部机制

- **doc-card**（卡片检索）：详见 `doc-card/SKILL.md` — V3 搜索 CLI、索引构建、评分规则、卡类型详解
- **doc-graph**（知识图谱检索）：详见 `doc-graph/SKILL.md` — 图谱 CLI、图遍历命令、语义分析提示词、跨生态映射

日常检索始终使用顶层 `unified_search.py`，无需直接调用子技能 CLI。