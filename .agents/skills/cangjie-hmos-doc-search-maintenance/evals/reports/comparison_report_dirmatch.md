# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 97 (50.5%) | 159 (82.8%) | 148 (77.1%) |
| 部分命中 PARTIAL | 0 (0.0%) | 18 (9.4%) | 10 (5.2%) |
| 未命中 MISS | 95 (49.5%) | 15 (7.8%) | 34 (17.7%) |
| Recall@5 (FULL+PARTIAL) | 50.5% | 92.2% | 82.3% |
| Precision@1 (FULL) | 50.5% | 82.8% | 77.1% |
| MRR (平均倒数排名) | 0.243 | 0.423 | 0.396 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 164.3ms | 1.5ms | 164.2ms |
| P50 耗时 | 161.2ms | 1.2ms | 163.4ms |
| P95 耗时 | 275.4ms | 4.1ms | 265.8ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 80.0% | 95.0% | 95.0% |
| comparison | 66.7% | 86.7% | 80.0% |
| composition | 60.0% | 93.3% | 86.7% |
| constrained | 40.0% | 75.0% | 65.0% |
| cross_ecosystem | 53.3% | 86.7% | 86.7% |
| enumeration | 45.0% | 100.0% | 95.0% |
| how_to | 50.0% | 95.5% | 77.3% |
| performance_boundary | 43.8% | 100.0% | 81.2% |
| reverse_lookup | 31.2% | 87.5% | 62.5% |
| semantic_fuzzy | 31.2% | 93.8% | 87.5% |
| workflow | 52.9% | 100.0% | 88.2% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 0 | 192 | 0 |
| 10-100ms | 27 | 0 | 28 |
| 100-500ms | 164 | 0 | 164 |
| 500ms-1s | 1 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 20 | api_lookup | geometryTransition的参数有哪些 | MISS | FULL | FULL |
| 21 | enumeration | Timer定时器的配置参数有哪些 | MISS | FULL | FULL |
| 24 | enumeration | UIAbility的生命周期状态有哪些 | MISS | FULL | MISS |
| 28 | enumeration | NotificationRequest有哪些属性 | MISS | FULL | FULL |
| 29 | enumeration | NotificationSlot有哪些配置 | MISS | FULL | FULL |
| 30 | enumeration | Want的属性有哪些 | MISS | FULL | FULL |
| 32 | enumeration | ErrorManager有哪些方法 | MISS | FULL | FULL |
| 33 | enumeration | CameraManager有哪些方法 | MISS | FULL | FULL |
| 34 | enumeration | CameraInput有哪些事件 | MISS | FULL | FULL |
| 36 | enumeration | WebCookieManager有哪些方法 | MISS | FULL | FULL |
| 37 | enumeration | AnimateParam有哪些配置 | MISS | FULL | FULL |
| 40 | enumeration | PersistentStorage有哪些限制 | MISS | FULL | FULL |
| 42 | reverse_lookup | 要实现懒加载用什么方案 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | MISS | MISS |
| 45 | reverse_lookup | 要取消通知用什么方法 | MISS | FULL | MISS |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | MISS | MISS |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | PARTIAL | MISS |
| 50 | reverse_lookup | 要获取相机列表用什么方法 | MISS | FULL | FULL |
| 52 | reverse_lookup | 要设置Cookie用什么API | MISS | FULL | MISS |
| 53 | reverse_lookup | 要实现页面转场用什么API | MISS | FULL | FULL |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | MISS | FULL | PARTIAL |
| 55 | reverse_lookup | 要持久化状态用什么组件 | MISS | FULL | FULL |
| 56 | reverse_lookup | 要获取设备环境参数用什么API | MISS | FULL | MISS |
| 57 | semantic_fuzzy | 列表滑动卡顿怎么优化 | MISS | FULL | FULL |
| 58 | semantic_fuzzy | 为什么状态改了界面不更新 | MISS | FULL | FULL |
| 62 | semantic_fuzzy | 数据库查询结果为空怎么办 | MISS | MISS | MISS |
| 63 | semantic_fuzzy | 图片解码失败怎么办 | MISS | FULL | FULL |
| 64 | semantic_fuzzy | 相机拍照失败怎么处理 | MISS | FULL | FULL |
| 66 | semantic_fuzzy | 转场动画效果不对怎么办 | MISS | FULL | FULL |
| 67 | semantic_fuzzy | 持久化数据丢失怎么办 | MISS | FULL | FULL |
| 68 | semantic_fuzzy | Environment参数获取不到怎么办 | MISS | FULL | MISS |
| 69 | semantic_fuzzy | Ability启动失败怎么排查 | MISS | PARTIAL | PARTIAL |
| 70 | semantic_fuzzy | Ability生命周期回调不执行怎么办 | MISS | FULL | FULL |
| 72 | semantic_fuzzy | 相机无法打开怎么办 | MISS | FULL | FULL |
| 73 | comparison | List和LazyForEach有什么区别 | MISS | FULL | FULL |
| 76 | comparison | AES和RSA加密有什么区别 | FULL | MISS | MISS |
| 77 | comparison | NotificationRequest和NotificationCon | MISS | FULL | FULL |
| 79 | comparison | ImageSource和PixelMap有什么区别 | MISS | FULL | MISS |
| 80 | comparison | PhotoSession和VideoSession有什么区别 | MISS | MISS | MISS |
| 83 | comparison | geometryTransition和sharedTransition | MISS | FULL | PARTIAL |
| 89 | composition | 做一个带虚拟滚动的大数据表格 | MISS | PARTIAL | MISS |
| 91 | composition | 做一个带下拉刷新的网络列表页 | FULL | MISS | FULL |
| 92 | composition | 做一个带图片的通知 | MISS | FULL | FULL |
| 93 | composition | 做一个带进度条的通知 | MISS | FULL | FULL |
| 97 | composition | 做一个持久化的用户设置页 | MISS | FULL | MISS |
| 99 | composition | 做一个带相机的页面 | MISS | PARTIAL | PARTIAL |
| 101 | composition | 做一个带通知的下载任务 | MISS | FULL | FULL |
| 103 | cross_ecosystem | Android的RecyclerView在鸿蒙对应什么 | MISS | PARTIAL | PARTIAL |
| 105 | cross_ecosystem | RN的FlatList对应鸿蒙什么组件 | MISS | MISS | MISS |
| 107 | cross_ecosystem | Android的Notification在鸿蒙对应什么 | MISS | MISS | MISS |
| 109 | cross_ecosystem | Android的Camera在鸿蒙对应什么 | MISS | FULL | FULL |
| 112 | cross_ecosystem | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL | FULL |
| 113 | cross_ecosystem | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL | FULL |
| 115 | cross_ecosystem | Android的Intent在鸿蒙对应什么 | MISS | FULL | FULL |
| 121 | workflow | 通知发布的完整流程是什么 | MISS | FULL | FULL |
| 123 | workflow | 相机拍照的完整流程是什么 | MISS | FULL | FULL |
| 125 | workflow | 页面转场的配置流程是什么 | MISS | FULL | MISS |
| 126 | workflow | 持久化存储的配置流程是什么 | MISS | FULL | FULL |
| 129 | workflow | 相机初始化流程是什么 | MISS | FULL | FULL |
| 132 | workflow | BLE GATT连接流程 | MISS | FULL | FULL |
| 133 | workflow | ImageSource解码流程 | MISS | FULL | FULL |
| 134 | workflow | ImagePacker编码流程 | MISS | FULL | MISS |
| 135 | constrained | 后台运行时怎么保持网络连接 | MISS | PARTIAL | PARTIAL |
| 137 | constrained | 弱网环境下请求超时怎么处理 | MISS | FULL | FULL |
| 138 | constrained | 通知权限没申请怎么办 | MISS | PARTIAL | PARTIAL |
| 140 | constrained | 图片内存占用过大怎么办 | MISS | MISS | MISS |
| 141 | constrained | 相机权限被拒绝怎么办 | MISS | MISS | MISS |
| 142 | constrained | 动画在弱设备上卡顿怎么办 | FULL | FULL | MISS |
| 143 | constrained | 持久化数据超过2kb怎么办 | MISS | FULL | FULL |
| 144 | constrained | Environment参数不支持怎么办 | MISS | FULL | MISS |
| 145 | constrained | 后台任务申请权限怎么处理 | MISS | MISS | MISS |
| 146 | constrained | 相机权限被拒绝怎么处理 | MISS | MISS | MISS |
| 149 | constrained | 后台任务执行时间过长怎么办 | MISS | MISS | MISS |
| 153 | constrained | 图片解码内存限制 | MISS | FULL | FULL |
| 154 | constrained | 相机预览帧率限制 | MISS | FULL | FULL |
| 155 | performance_boundary | 一万条数据的列表渲染卡顿怎么办 | MISS | FULL | MISS |
| 156 | performance_boundary | 快速滑动列表时内存飙升怎么办 | MISS | FULL | FULL |
| 158 | performance_boundary | 大量图片加载内存溢出怎么办 | MISS | FULL | FULL |
| 160 | performance_boundary | 相机预览卡顿怎么办 | MISS | FULL | FULL |
| 162 | performance_boundary | 页面转场内存占用过大 | MISS | FULL | PARTIAL |
| 163 | performance_boundary | PersistentStorage读写慢怎么办 | MISS | FULL | FULL |
| 164 | performance_boundary | 大量Ability启动性能问题 | MISS | FULL | MISS |
| 166 | performance_boundary | 相机录像内存飙升怎么办 | MISS | FULL | MISS |
| 170 | performance_boundary | 定时器执行延迟怎么办 | MISS | FULL | FULL |
| 178 | how_to | Timer定时器怎么用 | MISS | FULL | FULL |
| 180 | how_to | UIAbility怎么创建和启动 | MISS | FULL | MISS |
| 181 | how_to | 后台任务怎么调度 | MISS | PARTIAL | MISS |
| 182 | how_to | 定位服务怎么获取位置 | MISS | FULL | FULL |
| 183 | how_to | 相机拍照怎么实现 | MISS | FULL | MISS |
| 184 | how_to | 图片处理怎么实现 | MISS | FULL | MISS |
| 185 | how_to | 动画效果怎么实现 | MISS | MISS | MISS |
| 186 | how_to | 图片选择器怎么用 | MISS | FULL | FULL |
| 187 | how_to | 通知怎么发 | MISS | PARTIAL | PARTIAL |
| 189 | how_to | 图片怎么解码 | MISS | FULL | FULL |
| 191 | how_to | PersistentStorage怎么配置 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 55 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 20 | geometryTransition的参数有哪些 | MISS | FULL |
| 21 | Timer定时器的配置参数有哪些 | MISS | FULL |
| 28 | NotificationRequest有哪些属性 | MISS | FULL |
| 29 | NotificationSlot有哪些配置 | MISS | FULL |
| 30 | Want的属性有哪些 | MISS | FULL |
| 32 | ErrorManager有哪些方法 | MISS | FULL |
| 33 | CameraManager有哪些方法 | MISS | FULL |
| 34 | CameraInput有哪些事件 | MISS | FULL |
| 36 | WebCookieManager有哪些方法 | MISS | FULL |
| 37 | AnimateParam有哪些配置 | MISS | FULL |
| 40 | PersistentStorage有哪些限制 | MISS | FULL |
| 42 | 要实现懒加载用什么方案 | MISS | FULL |
| 50 | 要获取相机列表用什么方法 | MISS | FULL |
| 53 | 要实现页面转场用什么API | MISS | FULL |
| 55 | 要持久化状态用什么组件 | MISS | FULL |
| 57 | 列表滑动卡顿怎么优化 | MISS | FULL |
| 58 | 为什么状态改了界面不更新 | MISS | FULL |
| 63 | 图片解码失败怎么办 | MISS | FULL |
| 64 | 相机拍照失败怎么处理 | MISS | FULL |
| 66 | 转场动画效果不对怎么办 | MISS | FULL |
| 67 | 持久化数据丢失怎么办 | MISS | FULL |
| 70 | Ability生命周期回调不执行怎么办 | MISS | FULL |
| 72 | 相机无法打开怎么办 | MISS | FULL |
| 73 | List和LazyForEach有什么区别 | MISS | FULL |
| 77 | NotificationRequest和NotificationContent有 | MISS | FULL |
| 91 | 做一个带下拉刷新的网络列表页 | FULL | MISS |
| 92 | 做一个带图片的通知 | MISS | FULL |
| 93 | 做一个带进度条的通知 | MISS | FULL |
| 101 | 做一个带通知的下载任务 | MISS | FULL |
| 109 | Android的Camera在鸿蒙对应什么 | MISS | FULL |
| 112 | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL |
| 113 | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL |
| 115 | Android的Intent在鸿蒙对应什么 | MISS | FULL |
| 121 | 通知发布的完整流程是什么 | MISS | FULL |
| 123 | 相机拍照的完整流程是什么 | MISS | FULL |
| 126 | 持久化存储的配置流程是什么 | MISS | FULL |
| 129 | 相机初始化流程是什么 | MISS | FULL |
| 132 | BLE GATT连接流程 | MISS | FULL |
| 133 | ImageSource解码流程 | MISS | FULL |
| 137 | 弱网环境下请求超时怎么处理 | MISS | FULL |
| 143 | 持久化数据超过2kb怎么办 | MISS | FULL |
| 153 | 图片解码内存限制 | MISS | FULL |
| 154 | 相机预览帧率限制 | MISS | FULL |
| 156 | 快速滑动列表时内存飙升怎么办 | MISS | FULL |
| 158 | 大量图片加载内存溢出怎么办 | MISS | FULL |
| 160 | 相机预览卡顿怎么办 | MISS | FULL |
| 163 | PersistentStorage读写慢怎么办 | MISS | FULL |
| 170 | 定时器执行延迟怎么办 | MISS | FULL |
| 178 | Timer定时器怎么用 | MISS | FULL |
| 182 | 定位服务怎么获取位置 | MISS | FULL |
| 186 | 图片选择器怎么用 | MISS | FULL |
| 189 | 图片怎么解码 | MISS | FULL |
| 191 | PersistentStorage怎么配置 | MISS | FULL |