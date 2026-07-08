# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 157 (81.8%) | 188 (97.9%) | 182 (94.8%) |
| 部分命中 PARTIAL | 0 (0.0%) | 1 (0.5%) | 0 (0.0%) |
| 未命中 MISS | 35 (18.2%) | 3 (1.6%) | 10 (5.2%) |
| Recall@5 (FULL+PARTIAL) | 81.8% | 98.4% | 94.8% |
| Precision@1 (FULL) | 81.8% | 97.9% | 94.8% |
| MRR (平均倒数排名) | 0.599 | 0.816 | 0.807 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 75.0ms | 0.6ms | 22.7ms |
| P50 耗时 | 76.7ms | 0.4ms | 19.0ms |
| P95 耗时 | 103.3ms | 2.1ms | 47.3ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 80.0% | 95.0% | 95.0% |
| comparison | 93.3% | 100.0% | 100.0% |
| composition | 93.3% | 100.0% | 100.0% |
| constrained | 45.0% | 90.0% | 80.0% |
| cross_ecosystem | 93.3% | 100.0% | 93.3% |
| enumeration | 85.0% | 100.0% | 100.0% |
| how_to | 72.7% | 100.0% | 95.5% |
| performance_boundary | 87.5% | 100.0% | 100.0% |
| reverse_lookup | 81.2% | 100.0% | 87.5% |
| semantic_fuzzy | 93.8% | 100.0% | 100.0% |
| workflow | 88.2% | 100.0% | 94.1% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 0 | 192 | 19 |
| 10-100ms | 182 | 0 | 173 |
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
| 35 | enumeration | WebviewController有哪些方法 | MISS | FULL | FULL |
| 37 | enumeration | AnimateParam有哪些配置 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | FULL | FULL |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | MISS | FULL | MISS |
| 67 | semantic_fuzzy | 持久化数据丢失怎么办 | MISS | FULL | FULL |
| 81 | comparison | UIAbility和UIAbilityContext有什么区别 | MISS | FULL | FULL |
| 98 | composition | 做一个响应深色模式的页面 | MISS | FULL | FULL |
| 109 | cross_ecosystem | Android的Camera在鸿蒙对应什么 | FULL | FULL | MISS |
| 113 | cross_ecosystem | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL | FULL |
| 123 | workflow | 相机拍照的完整流程是什么 | MISS | FULL | FULL |
| 128 | workflow | Ability生命周期流程是什么 | MISS | FULL | FULL |
| 129 | workflow | 相机初始化流程是什么 | FULL | FULL | MISS |
| 136 | constrained | 蓝牙持续扫描电量消耗太快怎么办 | MISS | FULL | FULL |
| 138 | constrained | 通知权限没申请怎么办 | MISS | FULL | FULL |
| 139 | constrained | 数据库文件过大怎么办 | MISS | FULL | FULL |
| 141 | constrained | 相机权限被拒绝怎么办 | MISS | PARTIAL | MISS |
| 143 | constrained | 持久化数据超过2kb怎么办 | MISS | FULL | FULL |
| 144 | constrained | Environment参数不支持怎么办 | MISS | FULL | FULL |
| 145 | constrained | 后台任务申请权限怎么处理 | MISS | FULL | MISS |
| 146 | constrained | 相机权限被拒绝怎么处理 | MISS | MISS | MISS |
| 147 | constrained | WebView权限申请怎么处理 | MISS | FULL | FULL |
| 148 | constrained | Ability启动时参数传递限制 | MISS | FULL | FULL |
| 149 | constrained | 后台任务执行时间过长怎么办 | MISS | MISS | MISS |
| 163 | performance_boundary | PersistentStorage读写慢怎么办 | MISS | FULL | FULL |
| 170 | performance_boundary | 定时器执行延迟怎么办 | MISS | FULL | FULL |
| 171 | how_to | List组件怎么用 | MISS | FULL | FULL |
| 177 | how_to | 蓝牙BLE怎么扫描连接设备 | MISS | FULL | FULL |
| 179 | how_to | 关系型数据库RDB怎么用 | MISS | FULL | FULL |
| 183 | how_to | 相机拍照怎么实现 | FULL | FULL | MISS |
| 186 | how_to | 图片选择器怎么用 | MISS | FULL | FULL |
| 187 | how_to | 通知怎么发 | MISS | FULL | FULL |
| 188 | how_to | 数据库怎么创建 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 28 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 4 | HttpRequest的request方法参数 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 11 | ListScroller的API有哪些 | MISS | FULL |
| 24 | UIAbility的生命周期状态有哪些 | MISS | FULL |
| 35 | WebviewController有哪些方法 | MISS | FULL |
| 37 | AnimateParam有哪些配置 | MISS | FULL |
| 44 | 要发送通知用什么API | MISS | FULL |
| 67 | 持久化数据丢失怎么办 | MISS | FULL |
| 81 | UIAbility和UIAbilityContext有什么区别 | MISS | FULL |
| 98 | 做一个响应深色模式的页面 | MISS | FULL |
| 113 | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL |
| 123 | 相机拍照的完整流程是什么 | MISS | FULL |
| 128 | Ability生命周期流程是什么 | MISS | FULL |
| 136 | 蓝牙持续扫描电量消耗太快怎么办 | MISS | FULL |
| 138 | 通知权限没申请怎么办 | MISS | FULL |
| 139 | 数据库文件过大怎么办 | MISS | FULL |
| 143 | 持久化数据超过2kb怎么办 | MISS | FULL |
| 144 | Environment参数不支持怎么办 | MISS | FULL |
| 147 | WebView权限申请怎么处理 | MISS | FULL |
| 148 | Ability启动时参数传递限制 | MISS | FULL |
| 163 | PersistentStorage读写慢怎么办 | MISS | FULL |
| 170 | 定时器执行延迟怎么办 | MISS | FULL |
| 171 | List组件怎么用 | MISS | FULL |
| 177 | 蓝牙BLE怎么扫描连接设备 | MISS | FULL |
| 179 | 关系型数据库RDB怎么用 | MISS | FULL |
| 186 | 图片选择器怎么用 | MISS | FULL |
| 187 | 通知怎么发 | MISS | FULL |
| 188 | 数据库怎么创建 | MISS | FULL |