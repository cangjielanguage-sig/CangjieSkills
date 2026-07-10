# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 110 (57.3%) | 182 (94.8%) | 172 (89.6%) |
| 部分命中 PARTIAL | 0 (0.0%) | 4 (2.1%) | 4 (2.1%) |
| 未命中 MISS | 82 (42.7%) | 6 (3.1%) | 16 (8.3%) |
| Recall@5 (FULL+PARTIAL) | 57.3% | 96.9% | 91.7% |
| Precision@1 (FULL) | 57.3% | 94.8% | 89.6% |
| MRR (平均倒数排名) | 0.198 | 0.698 | 0.684 |
| 平均直接命中数 | 19.6 | 5.0 | 6.0 |
| 平均搜索耗时 | 25.0ms | 0.6ms | 24.2ms |
| P50 耗时 | 22.8ms | 0.4ms | 21.9ms |
| P95 耗时 | 53.9ms | 1.7ms | 52.8ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 55.0% | 95.0% | 85.0% |
| comparison | 66.7% | 93.3% | 93.3% |
| composition | 80.0% | 100.0% | 100.0% |
| constrained | 55.0% | 85.0% | 75.0% |
| cross_ecosystem | 53.3% | 100.0% | 100.0% |
| enumeration | 50.0% | 100.0% | 90.0% |
| how_to | 50.0% | 100.0% | 95.5% |
| performance_boundary | 62.5% | 100.0% | 100.0% |
| reverse_lookup | 37.5% | 93.8% | 81.2% |
| semantic_fuzzy | 75.0% | 100.0% | 93.8% |
| workflow | 52.9% | 100.0% | 100.0% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 16 | 192 | 19 |
| 10-100ms | 176 | 0 | 173 |
| 100-500ms | 0 | 0 | 0 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 2 | api_lookup | DeviceInfo获取设备信息的具体API | MISS | FULL | FULL |
| 5 | api_lookup | Router.pushUrl的参数 | FULL | FULL | MISS |
| 7 | api_lookup | Router.replaceUrl的参数 | FULL | FULL | MISS |
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | FULL |
| 11 | api_lookup | ListScroller的API有哪些 | MISS | FULL | FULL |
| 12 | api_lookup | SwiperController的API有哪些 | MISS | FULL | FULL |
| 13 | api_lookup | RefreshParams的配置参数 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 16 | api_lookup | HttpResponseCache的创建方法 | MISS | FULL | FULL |
| 20 | api_lookup | geometryTransition的参数有哪些 | MISS | FULL | FULL |
| 21 | enumeration | Timer定时器的配置参数有哪些 | MISS | FULL | FULL |
| 22 | enumeration | AppStorage有哪些方法 | MISS | PARTIAL | PARTIAL |
| 23 | enumeration | Swiper有哪些回调事件 | MISS | FULL | FULL |
| 29 | enumeration | NotificationSlot有哪些配置 | MISS | FULL | FULL |
| 30 | enumeration | Want的属性有哪些 | MISS | FULL | FULL |
| 31 | enumeration | UIAbility有哪些生命周期回调 | MISS | FULL | FULL |
| 32 | enumeration | ErrorManager有哪些方法 | MISS | FULL | FULL |
| 37 | enumeration | AnimateParam有哪些配置 | MISS | FULL | MISS |
| 38 | enumeration | TransitionEffect有哪些类型 | MISS | FULL | FULL |
| 40 | enumeration | PersistentStorage有哪些限制 | MISS | FULL | MISS |
| 41 | reverse_lookup | 要实现下拉刷新用什么组件 | MISS | FULL | FULL |
| 42 | reverse_lookup | 要实现懒加载用什么方案 | MISS | FULL | FULL |
| 43 | reverse_lookup | 要实现轮播用什么组件 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | FULL | FULL |
| 45 | reverse_lookup | 要取消通知用什么方法 | MISS | FULL | FULL |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | PARTIAL | PARTIAL |
| 48 | reverse_lookup | 要实现页面跳转用什么方法 | FULL | FULL | MISS |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 52 | reverse_lookup | 要设置Cookie用什么API | MISS | FULL | FULL |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | FULL | MISS | MISS |
| 55 | reverse_lookup | 要持久化状态用什么组件 | MISS | FULL | FULL |
| 56 | reverse_lookup | 要获取设备环境参数用什么API | MISS | FULL | FULL |
| 58 | semantic_fuzzy | 为什么状态改了界面不更新 | FULL | FULL | MISS |
| 67 | semantic_fuzzy | 持久化数据丢失怎么办 | MISS | FULL | FULL |
| 68 | semantic_fuzzy | Environment参数获取不到怎么办 | MISS | FULL | FULL |
| 69 | semantic_fuzzy | Ability启动失败怎么排查 | MISS | FULL | FULL |
| 70 | semantic_fuzzy | Ability生命周期回调不执行怎么办 | MISS | FULL | FULL |
| 75 | comparison | AppStorage和LocalStorage有什么不同 | MISS | FULL | FULL |
| 79 | comparison | ImageSource和PixelMap有什么区别 | MISS | FULL | FULL |
| 80 | comparison | PhotoSession和VideoSession有什么区别 | FULL | MISS | MISS |
| 81 | comparison | UIAbility和UIAbilityContext有什么区别 | MISS | FULL | FULL |
| 83 | comparison | geometryTransition和sharedTransition | MISS | FULL | FULL |
| 84 | comparison | PersistentStorage和AppStorage有什么区别 | MISS | FULL | FULL |
| 88 | composition | 做一个带下拉刷新的列表页 | MISS | FULL | FULL |
| 98 | composition | 做一个响应深色模式的页面 | MISS | FULL | FULL |
| 101 | composition | 做一个带通知的下载任务 | MISS | FULL | FULL |
| 106 | cross_ecosystem | 鸿蒙版SwipeRefreshLayout怎么写 | MISS | FULL | FULL |
| 107 | cross_ecosystem | Android的Notification在鸿蒙对应什么 | MISS | FULL | FULL |
| 110 | cross_ecosystem | iOS的UIView动画在鸿蒙对应什么 | MISS | FULL | FULL |
| 111 | cross_ecosystem | React的Context在鸿蒙对应什么 | MISS | FULL | FULL |
| 112 | cross_ecosystem | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL | FULL |
| 113 | cross_ecosystem | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL | FULL |
| 115 | cross_ecosystem | Android的Intent在鸿蒙对应什么 | MISS | FULL | FULL |
| 119 | workflow | UIAbility启动流程是什么 | MISS | FULL | FULL |
| 121 | workflow | 通知发布的完整流程是什么 | MISS | FULL | FULL |
| 124 | workflow | 显式动画的执行流程是什么 | MISS | FULL | FULL |
| 126 | workflow | 持久化存储的配置流程是什么 | MISS | FULL | FULL |
| 127 | workflow | Ability启动流程是什么 | MISS | FULL | FULL |
| 128 | workflow | Ability生命周期流程是什么 | MISS | FULL | FULL |
| 133 | workflow | ImageSource解码流程 | MISS | FULL | FULL |
| 134 | workflow | ImagePacker编码流程 | MISS | FULL | FULL |
| 140 | constrained | 图片内存占用过大怎么办 | MISS | FULL | FULL |
| 141 | constrained | 相机权限被拒绝怎么办 | FULL | PARTIAL | MISS |
| 142 | constrained | 动画在弱设备上卡顿怎么办 | MISS | FULL | FULL |
| 143 | constrained | 持久化数据超过2kb怎么办 | MISS | PARTIAL | PARTIAL |
| 144 | constrained | Environment参数不支持怎么办 | MISS | FULL | FULL |
| 145 | constrained | 后台任务申请权限怎么处理 | MISS | FULL | MISS |
| 146 | constrained | 相机权限被拒绝怎么处理 | MISS | MISS | MISS |
| 148 | constrained | Ability启动时参数传递限制 | MISS | MISS | MISS |
| 149 | constrained | 后台任务执行时间过长怎么办 | MISS | MISS | MISS |
| 153 | constrained | 图片解码内存限制 | MISS | FULL | FULL |
| 156 | performance_boundary | 快速滑动列表时内存飙升怎么办 | MISS | FULL | FULL |
| 158 | performance_boundary | 大量图片加载内存溢出怎么办 | MISS | FULL | FULL |
| 163 | performance_boundary | PersistentStorage读写慢怎么办 | MISS | FULL | FULL |
| 164 | performance_boundary | 大量Ability启动性能问题 | MISS | FULL | FULL |
| 166 | performance_boundary | 相机录像内存飙升怎么办 | MISS | FULL | FULL |
| 170 | performance_boundary | 定时器执行延迟怎么办 | MISS | FULL | FULL |
| 175 | how_to | Swiper轮播怎么用 | MISS | FULL | FULL |
| 178 | how_to | Timer定时器怎么用 | MISS | FULL | FULL |
| 180 | how_to | UIAbility怎么创建和启动 | MISS | FULL | FULL |
| 182 | how_to | 定位服务怎么获取位置 | MISS | FULL | FULL |
| 184 | how_to | 图片处理怎么实现 | MISS | FULL | FULL |
| 185 | how_to | 动画效果怎么实现 | MISS | FULL | FULL |
| 186 | how_to | 图片选择器怎么用 | MISS | FULL | FULL |
| 187 | how_to | 通知怎么发 | MISS | FULL | FULL |
| 190 | how_to | 显式动画怎么用 | MISS | FULL | FULL |
| 191 | how_to | PersistentStorage怎么配置 | MISS | FULL | MISS |
| 192 | how_to | Environment怎么获取参数 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 70 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 2 | DeviceInfo获取设备信息的具体API | MISS | FULL |
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 11 | ListScroller的API有哪些 | MISS | FULL |
| 12 | SwiperController的API有哪些 | MISS | FULL |
| 13 | RefreshParams的配置参数 | MISS | FULL |
| 16 | HttpResponseCache的创建方法 | MISS | FULL |
| 20 | geometryTransition的参数有哪些 | MISS | FULL |
| 21 | Timer定时器的配置参数有哪些 | MISS | FULL |
| 23 | Swiper有哪些回调事件 | MISS | FULL |
| 29 | NotificationSlot有哪些配置 | MISS | FULL |
| 30 | Want的属性有哪些 | MISS | FULL |
| 31 | UIAbility有哪些生命周期回调 | MISS | FULL |
| 32 | ErrorManager有哪些方法 | MISS | FULL |
| 38 | TransitionEffect有哪些类型 | MISS | FULL |
| 41 | 要实现下拉刷新用什么组件 | MISS | FULL |
| 42 | 要实现懒加载用什么方案 | MISS | FULL |
| 43 | 要实现轮播用什么组件 | MISS | FULL |
| 44 | 要发送通知用什么API | MISS | FULL |
| 45 | 要取消通知用什么方法 | MISS | FULL |
| 52 | 要设置Cookie用什么API | MISS | FULL |
| 55 | 要持久化状态用什么组件 | MISS | FULL |
| 56 | 要获取设备环境参数用什么API | MISS | FULL |
| 67 | 持久化数据丢失怎么办 | MISS | FULL |
| 68 | Environment参数获取不到怎么办 | MISS | FULL |
| 69 | Ability启动失败怎么排查 | MISS | FULL |
| 70 | Ability生命周期回调不执行怎么办 | MISS | FULL |
| 75 | AppStorage和LocalStorage有什么不同 | MISS | FULL |
| 79 | ImageSource和PixelMap有什么区别 | MISS | FULL |
| 81 | UIAbility和UIAbilityContext有什么区别 | MISS | FULL |
| 83 | geometryTransition和sharedTransition有什么区别 | MISS | FULL |
| 84 | PersistentStorage和AppStorage有什么区别 | MISS | FULL |
| 88 | 做一个带下拉刷新的列表页 | MISS | FULL |
| 98 | 做一个响应深色模式的页面 | MISS | FULL |
| 101 | 做一个带通知的下载任务 | MISS | FULL |
| 106 | 鸿蒙版SwipeRefreshLayout怎么写 | MISS | FULL |
| 107 | Android的Notification在鸿蒙对应什么 | MISS | FULL |
| 110 | iOS的UIView动画在鸿蒙对应什么 | MISS | FULL |
| 111 | React的Context在鸿蒙对应什么 | MISS | FULL |
| 112 | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL |
| 113 | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL |
| 115 | Android的Intent在鸿蒙对应什么 | MISS | FULL |
| 119 | UIAbility启动流程是什么 | MISS | FULL |
| 121 | 通知发布的完整流程是什么 | MISS | FULL |
| 124 | 显式动画的执行流程是什么 | MISS | FULL |
| 126 | 持久化存储的配置流程是什么 | MISS | FULL |
| 127 | Ability启动流程是什么 | MISS | FULL |
| 128 | Ability生命周期流程是什么 | MISS | FULL |
| 133 | ImageSource解码流程 | MISS | FULL |
| 134 | ImagePacker编码流程 | MISS | FULL |
| 140 | 图片内存占用过大怎么办 | MISS | FULL |
| 142 | 动画在弱设备上卡顿怎么办 | MISS | FULL |
| 144 | Environment参数不支持怎么办 | MISS | FULL |
| 153 | 图片解码内存限制 | MISS | FULL |
| 156 | 快速滑动列表时内存飙升怎么办 | MISS | FULL |
| 158 | 大量图片加载内存溢出怎么办 | MISS | FULL |
| 163 | PersistentStorage读写慢怎么办 | MISS | FULL |
| 164 | 大量Ability启动性能问题 | MISS | FULL |
| 166 | 相机录像内存飙升怎么办 | MISS | FULL |
| 170 | 定时器执行延迟怎么办 | MISS | FULL |
| 175 | Swiper轮播怎么用 | MISS | FULL |
| 178 | Timer定时器怎么用 | MISS | FULL |
| 180 | UIAbility怎么创建和启动 | MISS | FULL |
| 182 | 定位服务怎么获取位置 | MISS | FULL |
| 184 | 图片处理怎么实现 | MISS | FULL |
| 185 | 动画效果怎么实现 | MISS | FULL |
| 186 | 图片选择器怎么用 | MISS | FULL |
| 187 | 通知怎么发 | MISS | FULL |
| 190 | 显式动画怎么用 | MISS | FULL |
| 192 | Environment怎么获取参数 | MISS | FULL |