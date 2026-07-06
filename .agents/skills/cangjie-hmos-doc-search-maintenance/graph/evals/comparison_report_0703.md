# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 160 (83.3%) | 187 (97.4%) | 184 (95.8%) |
| 部分命中 PARTIAL | 0 (0.0%) | 1 (0.5%) | 0 (0.0%) |
| 未命中 MISS | 32 (16.7%) | 4 (2.1%) | 8 (4.2%) |
| Recall@5 (FULL+PARTIAL) | 83.3% | 97.9% | 95.8% |
| Precision@1 (FULL) | 83.3% | 97.4% | 95.8% |
| MRR (平均倒数排名) | 0.545 | 0.820 | 0.814 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 75.4ms | 0.5ms | 24.4ms |
| P50 耗时 | 78.0ms | 0.4ms | 22.2ms |
| P95 耗时 | 100.5ms | 1.6ms | 53.3ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 80.0% | 95.0% | 95.0% |
| comparison | 86.7% | 100.0% | 100.0% |
| composition | 93.3% | 100.0% | 100.0% |
| constrained | 40.0% | 90.0% | 80.0% |
| cross_ecosystem | 93.3% | 100.0% | 100.0% |
| enumeration | 90.0% | 100.0% | 100.0% |
| how_to | 90.9% | 100.0% | 100.0% |
| performance_boundary | 100.0% | 100.0% | 100.0% |
| reverse_lookup | 68.8% | 93.8% | 81.2% |
| semantic_fuzzy | 93.8% | 100.0% | 100.0% |
| workflow | 88.2% | 100.0% | 100.0% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 0 | 192 | 17 |
| 10-100ms | 182 | 0 | 175 |
| 100-500ms | 10 | 0 | 0 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 4 | api_lookup | HttpRequest的request方法参数 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | FULL |
| 11 | api_lookup | ListScroller的API有哪些 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 24 | enumeration | UIAbility的生命周期状态有哪些 | MISS | FULL | FULL |
| 31 | enumeration | UIAbility有哪些生命周期回调 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | FULL | MISS |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | FULL | FULL |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 51 | reverse_lookup | 要加载网页用什么组件 | MISS | FULL | FULL |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | MISS | MISS | MISS |
| 68 | semantic_fuzzy | Environment参数获取不到怎么办 | MISS | FULL | FULL |
| 81 | comparison | UIAbility和UIAbilityContext有什么区别 | MISS | FULL | FULL |
| 86 | comparison | WebView和WebviewController有什么区别 | MISS | FULL | FULL |
| 98 | composition | 做一个响应深色模式的页面 | MISS | FULL | FULL |
| 113 | cross_ecosystem | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL | FULL |
| 123 | workflow | 相机拍照的完整流程是什么 | MISS | FULL | FULL |
| 128 | workflow | Ability生命周期流程是什么 | MISS | FULL | FULL |
| 135 | constrained | 后台运行时怎么保持网络连接 | MISS | FULL | FULL |
| 138 | constrained | 通知权限没申请怎么办 | MISS | FULL | FULL |
| 141 | constrained | 相机权限被拒绝怎么办 | MISS | PARTIAL | MISS |
| 143 | constrained | 持久化数据超过2kb怎么办 | MISS | FULL | FULL |
| 144 | constrained | Environment参数不支持怎么办 | MISS | FULL | FULL |
| 145 | constrained | 后台任务申请权限怎么处理 | MISS | FULL | MISS |
| 146 | constrained | 相机权限被拒绝怎么处理 | MISS | MISS | MISS |
| 147 | constrained | WebView权限申请怎么处理 | MISS | FULL | FULL |
| 148 | constrained | Ability启动时参数传递限制 | MISS | FULL | FULL |
| 149 | constrained | 后台任务执行时间过长怎么办 | MISS | MISS | MISS |
| 150 | constrained | BLE广播包大小限制 | MISS | FULL | FULL |
| 152 | constrained | 数据库事务执行时间限制 | MISS | FULL | FULL |
| 181 | how_to | 后台任务怎么调度 | MISS | FULL | FULL |
| 188 | how_to | 数据库怎么创建 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 24 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 4 | HttpRequest的request方法参数 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 11 | ListScroller的API有哪些 | MISS | FULL |
| 24 | UIAbility的生命周期状态有哪些 | MISS | FULL |
| 31 | UIAbility有哪些生命周期回调 | MISS | FULL |
| 47 | 要查询数据库用什么类 | MISS | FULL |
| 51 | 要加载网页用什么组件 | MISS | FULL |
| 68 | Environment参数获取不到怎么办 | MISS | FULL |
| 81 | UIAbility和UIAbilityContext有什么区别 | MISS | FULL |
| 86 | WebView和WebviewController有什么区别 | MISS | FULL |
| 98 | 做一个响应深色模式的页面 | MISS | FULL |
| 113 | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL |
| 123 | 相机拍照的完整流程是什么 | MISS | FULL |
| 128 | Ability生命周期流程是什么 | MISS | FULL |
| 135 | 后台运行时怎么保持网络连接 | MISS | FULL |
| 138 | 通知权限没申请怎么办 | MISS | FULL |
| 143 | 持久化数据超过2kb怎么办 | MISS | FULL |
| 144 | Environment参数不支持怎么办 | MISS | FULL |
| 147 | WebView权限申请怎么处理 | MISS | FULL |
| 148 | Ability启动时参数传递限制 | MISS | FULL |
| 150 | BLE广播包大小限制 | MISS | FULL |
| 152 | 数据库事务执行时间限制 | MISS | FULL |
| 181 | 后台任务怎么调度 | MISS | FULL |
| 188 | 数据库怎么创建 | MISS | FULL |