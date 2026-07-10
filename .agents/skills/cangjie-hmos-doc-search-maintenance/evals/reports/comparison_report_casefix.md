# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 63 (32.8%) | 158 (82.3%) | 131 (68.2%) |
| 部分命中 PARTIAL | 0 (0.0%) | 17 (8.9%) | 17 (8.9%) |
| 未命中 MISS | 129 (67.2%) | 17 (8.9%) | 44 (22.9%) |
| Recall@5 (FULL+PARTIAL) | 32.8% | 91.1% | 77.1% |
| Precision@1 (FULL) | 32.8% | 82.3% | 68.2% |
| MRR (平均倒数排名) | 0.125 | 0.466 | 0.427 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 20.2ms | 1.7ms | 20.9ms |
| P50 耗时 | 16.6ms | 1.3ms | 16.8ms |
| P95 耗时 | 40.6ms | 4.7ms | 47.3ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 40.0% | 95.0% | 80.0% |
| comparison | 46.7% | 86.7% | 73.3% |
| composition | 46.7% | 100.0% | 93.3% |
| constrained | 25.0% | 75.0% | 65.0% |
| cross_ecosystem | 40.0% | 93.3% | 93.3% |
| enumeration | 30.0% | 100.0% | 80.0% |
| how_to | 27.3% | 81.8% | 63.6% |
| performance_boundary | 18.8% | 93.8% | 75.0% |
| reverse_lookup | 18.8% | 87.5% | 68.8% |
| semantic_fuzzy | 31.2% | 93.8% | 81.2% |
| workflow | 41.2% | 100.0% | 82.4% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 35 | 192 | 33 |
| 10-100ms | 157 | 0 | 159 |
| 100-500ms | 0 | 0 | 0 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 5 | api_lookup | Router.pushUrl的参数 | MISS | PARTIAL | PARTIAL |
| 6 | api_lookup | Router.back的用法 | MISS | FULL | MISS |
| 7 | api_lookup | Router.replaceUrl的参数 | MISS | FULL | MISS |
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | MISS |
| 12 | api_lookup | SwiperController的API有哪些 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 16 | api_lookup | HttpResponseCache的创建方法 | MISS | FULL | FULL |
| 17 | api_lookup | MultiFormData的属性 | MISS | FULL | FULL |
| 18 | api_lookup | ClientCert的配置方法 | MISS | FULL | FULL |
| 19 | api_lookup | PerformanceTiming的属性 | MISS | FULL | FULL |
| 20 | api_lookup | geometryTransition的参数有哪些 | MISS | FULL | FULL |
| 21 | enumeration | Timer定时器的配置参数有哪些 | MISS | FULL | MISS |
| 22 | enumeration | AppStorage有哪些方法 | MISS | FULL | FULL |
| 23 | enumeration | Swiper有哪些回调事件 | MISS | FULL | FULL |
| 24 | enumeration | UIAbility的生命周期状态有哪些 | MISS | FULL | MISS |
| 29 | enumeration | NotificationSlot有哪些配置 | MISS | FULL | FULL |
| 30 | enumeration | Want的属性有哪些 | MISS | FULL | FULL |
| 31 | enumeration | UIAbility有哪些生命周期回调 | MISS | FULL | FULL |
| 32 | enumeration | ErrorManager有哪些方法 | MISS | FULL | FULL |
| 33 | enumeration | CameraManager有哪些方法 | MISS | FULL | FULL |
| 34 | enumeration | CameraInput有哪些事件 | MISS | FULL | FULL |
| 36 | enumeration | WebCookieManager有哪些方法 | MISS | FULL | FULL |
| 37 | enumeration | AnimateParam有哪些配置 | MISS | FULL | FULL |
| 38 | enumeration | TransitionEffect有哪些类型 | MISS | FULL | MISS |
| 40 | enumeration | PersistentStorage有哪些限制 | MISS | FULL | MISS |
| 42 | reverse_lookup | 要实现懒加载用什么方案 | MISS | FULL | FULL |
| 43 | reverse_lookup | 要实现轮播用什么组件 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | MISS | MISS |
| 45 | reverse_lookup | 要取消通知用什么方法 | MISS | FULL | MISS |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | FULL | FULL |
| 48 | reverse_lookup | 要实现页面跳转用什么方法 | MISS | PARTIAL | PARTIAL |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 50 | reverse_lookup | 要获取相机列表用什么方法 | MISS | FULL | FULL |
| 52 | reverse_lookup | 要设置Cookie用什么API | MISS | MISS | MISS |
| 53 | reverse_lookup | 要实现页面转场用什么API | MISS | FULL | FULL |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | MISS | FULL | PARTIAL |
| 55 | reverse_lookup | 要持久化状态用什么组件 | MISS | FULL | FULL |
| 56 | reverse_lookup | 要获取设备环境参数用什么API | MISS | FULL | MISS |
| 57 | semantic_fuzzy | 列表滑动卡顿怎么优化 | MISS | FULL | FULL |
| 59 | semantic_fuzzy | 页面切换有白屏怎么办 | MISS | FULL | FULL |
| 62 | semantic_fuzzy | 数据库查询结果为空怎么办 | MISS | MISS | MISS |
| 63 | semantic_fuzzy | 图片解码失败怎么办 | MISS | FULL | FULL |
| 64 | semantic_fuzzy | 相机拍照失败怎么处理 | MISS | FULL | FULL |
| 65 | semantic_fuzzy | 动画执行后界面不更新怎么办 | MISS | FULL | MISS |
| 66 | semantic_fuzzy | 转场动画效果不对怎么办 | MISS | FULL | FULL |
| 67 | semantic_fuzzy | 持久化数据丢失怎么办 | MISS | FULL | MISS |
| 69 | semantic_fuzzy | Ability启动失败怎么排查 | MISS | PARTIAL | PARTIAL |
| 70 | semantic_fuzzy | Ability生命周期回调不执行怎么办 | MISS | FULL | FULL |
| 72 | semantic_fuzzy | 相机无法打开怎么办 | MISS | FULL | FULL |
| 73 | comparison | List和LazyForEach有什么区别 | MISS | FULL | PARTIAL |
| 76 | comparison | AES和RSA加密有什么区别 | MISS | MISS | MISS |
| 79 | comparison | ImageSource和PixelMap有什么区别 | MISS | FULL | MISS |
| 80 | comparison | PhotoSession和VideoSession有什么区别 | MISS | MISS | MISS |
| 81 | comparison | UIAbility和UIAbilityContext有什么区别 | MISS | FULL | FULL |
| 82 | comparison | animateTo和animation有什么区别 | MISS | FULL | MISS |
| 83 | comparison | geometryTransition和sharedTransition | MISS | FULL | PARTIAL |
| 84 | comparison | PersistentStorage和AppStorage有什么区别 | MISS | FULL | FULL |
| 89 | composition | 做一个带虚拟滚动的大数据表格 | MISS | FULL | FULL |
| 92 | composition | 做一个带图片的通知 | MISS | FULL | PARTIAL |
| 93 | composition | 做一个带进度条的通知 | MISS | FULL | FULL |
| 95 | composition | 做一个带动画的列表删除 | MISS | FULL | FULL |
| 96 | composition | 做一个带转场的页面跳转 | MISS | FULL | FULL |
| 97 | composition | 做一个持久化的用户设置页 | MISS | PARTIAL | PARTIAL |
| 99 | composition | 做一个带相机的页面 | MISS | PARTIAL | MISS |
| 101 | composition | 做一个带通知的下载任务 | MISS | FULL | FULL |
| 103 | cross_ecosystem | Android的RecyclerView在鸿蒙对应什么 | MISS | FULL | FULL |
| 105 | cross_ecosystem | RN的FlatList对应鸿蒙什么组件 | MISS | FULL | FULL |
| 107 | cross_ecosystem | Android的Notification在鸿蒙对应什么 | MISS | MISS | MISS |
| 109 | cross_ecosystem | Android的Camera在鸿蒙对应什么 | MISS | FULL | FULL |
| 110 | cross_ecosystem | iOS的UIView动画在鸿蒙对应什么 | MISS | FULL | FULL |
| 112 | cross_ecosystem | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL | FULL |
| 113 | cross_ecosystem | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL | FULL |
| 114 | cross_ecosystem | Android的Activity在鸿蒙对应什么 | MISS | FULL | FULL |
| 116 | cross_ecosystem | iOS的UIViewController在鸿蒙对应什么 | MISS | FULL | FULL |
| 119 | workflow | UIAbility启动流程是什么 | MISS | FULL | PARTIAL |
| 123 | workflow | 相机拍照的完整流程是什么 | MISS | FULL | FULL |
| 124 | workflow | 显式动画的执行流程是什么 | MISS | FULL | FULL |
| 125 | workflow | 页面转场的配置流程是什么 | MISS | FULL | MISS |
| 126 | workflow | 持久化存储的配置流程是什么 | MISS | FULL | MISS |
| 127 | workflow | Ability启动流程是什么 | MISS | PARTIAL | PARTIAL |
| 129 | workflow | 相机初始化流程是什么 | MISS | FULL | FULL |
| 132 | workflow | BLE GATT连接流程 | MISS | FULL | FULL |
| 133 | workflow | ImageSource解码流程 | MISS | FULL | MISS |
| 134 | workflow | ImagePacker编码流程 | MISS | FULL | FULL |
| 135 | constrained | 后台运行时怎么保持网络连接 | MISS | PARTIAL | PARTIAL |
| 137 | constrained | 弱网环境下请求超时怎么处理 | MISS | FULL | MISS |
| 138 | constrained | 通知权限没申请怎么办 | MISS | PARTIAL | PARTIAL |
| 140 | constrained | 图片内存占用过大怎么办 | MISS | MISS | MISS |
| 141 | constrained | 相机权限被拒绝怎么办 | MISS | MISS | MISS |
| 142 | constrained | 动画在弱设备上卡顿怎么办 | MISS | FULL | FULL |
| 143 | constrained | 持久化数据超过2kb怎么办 | MISS | FULL | MISS |
| 145 | constrained | 后台任务申请权限怎么处理 | MISS | MISS | MISS |
| 146 | constrained | 相机权限被拒绝怎么处理 | MISS | MISS | MISS |
| 148 | constrained | Ability启动时参数传递限制 | MISS | FULL | FULL |
| 149 | constrained | 后台任务执行时间过长怎么办 | MISS | MISS | MISS |
| 151 | constrained | HTTP请求并发限制 | MISS | PARTIAL | PARTIAL |
| 152 | constrained | 数据库事务执行时间限制 | MISS | FULL | FULL |
| 153 | constrained | 图片解码内存限制 | MISS | FULL | FULL |
| 154 | constrained | 相机预览帧率限制 | MISS | FULL | FULL |
| 155 | performance_boundary | 一万条数据的列表渲染卡顿怎么办 | MISS | FULL | MISS |
| 156 | performance_boundary | 快速滑动列表时内存飙升怎么办 | MISS | FULL | MISS |
| 157 | performance_boundary | WebView加载大页面白屏怎么办 | MISS | FULL | FULL |
| 158 | performance_boundary | 大量图片加载内存溢出怎么办 | MISS | FULL | FULL |
| 160 | performance_boundary | 相机预览卡顿怎么办 | MISS | FULL | FULL |
| 161 | performance_boundary | 大量动画同时执行性能问题 | MISS | FULL | FULL |
| 162 | performance_boundary | 页面转场内存占用过大 | MISS | PARTIAL | PARTIAL |
| 163 | performance_boundary | PersistentStorage读写慢怎么办 | MISS | FULL | MISS |
| 164 | performance_boundary | 大量Ability启动性能问题 | MISS | PARTIAL | PARTIAL |
| 165 | performance_boundary | WebView内存占用过大怎么办 | MISS | FULL | PARTIAL |
| 166 | performance_boundary | 相机录像内存飙升怎么办 | MISS | MISS | MISS |
| 169 | performance_boundary | HTTP缓存过多怎么办 | MISS | FULL | FULL |
| 170 | performance_boundary | 定时器执行延迟怎么办 | MISS | FULL | FULL |
| 171 | how_to | List组件怎么用 | MISS | FULL | MISS |
| 174 | how_to | 页面跳转怎么做 | MISS | FULL | MISS |
| 175 | how_to | Swiper轮播怎么用 | MISS | FULL | FULL |
| 176 | how_to | Grid网格布局怎么用 | MISS | MISS | MISS |
| 178 | how_to | Timer定时器怎么用 | MISS | FULL | MISS |
| 180 | how_to | UIAbility怎么创建和启动 | MISS | FULL | FULL |
| 181 | how_to | 后台任务怎么调度 | MISS | MISS | MISS |
| 182 | how_to | 定位服务怎么获取位置 | MISS | FULL | FULL |
| 183 | how_to | 相机拍照怎么实现 | MISS | FULL | FULL |
| 184 | how_to | 图片处理怎么实现 | MISS | FULL | FULL |
| 185 | how_to | 动画效果怎么实现 | MISS | MISS | MISS |
| 186 | how_to | 图片选择器怎么用 | MISS | FULL | FULL |
| 187 | how_to | 通知怎么发 | MISS | MISS | MISS |
| 189 | how_to | 图片怎么解码 | MISS | FULL | FULL |
| 190 | how_to | 显式动画怎么用 | MISS | FULL | FULL |
| 191 | how_to | PersistentStorage怎么配置 | MISS | FULL | MISS |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 69 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |
| 12 | SwiperController的API有哪些 | MISS | FULL |
| 16 | HttpResponseCache的创建方法 | MISS | FULL |
| 17 | MultiFormData的属性 | MISS | FULL |
| 18 | ClientCert的配置方法 | MISS | FULL |
| 19 | PerformanceTiming的属性 | MISS | FULL |
| 20 | geometryTransition的参数有哪些 | MISS | FULL |
| 22 | AppStorage有哪些方法 | MISS | FULL |
| 23 | Swiper有哪些回调事件 | MISS | FULL |
| 29 | NotificationSlot有哪些配置 | MISS | FULL |
| 30 | Want的属性有哪些 | MISS | FULL |
| 31 | UIAbility有哪些生命周期回调 | MISS | FULL |
| 32 | ErrorManager有哪些方法 | MISS | FULL |
| 33 | CameraManager有哪些方法 | MISS | FULL |
| 34 | CameraInput有哪些事件 | MISS | FULL |
| 36 | WebCookieManager有哪些方法 | MISS | FULL |
| 37 | AnimateParam有哪些配置 | MISS | FULL |
| 42 | 要实现懒加载用什么方案 | MISS | FULL |
| 43 | 要实现轮播用什么组件 | MISS | FULL |
| 47 | 要查询数据库用什么类 | MISS | FULL |
| 50 | 要获取相机列表用什么方法 | MISS | FULL |
| 53 | 要实现页面转场用什么API | MISS | FULL |
| 55 | 要持久化状态用什么组件 | MISS | FULL |
| 57 | 列表滑动卡顿怎么优化 | MISS | FULL |
| 59 | 页面切换有白屏怎么办 | MISS | FULL |
| 63 | 图片解码失败怎么办 | MISS | FULL |
| 64 | 相机拍照失败怎么处理 | MISS | FULL |
| 66 | 转场动画效果不对怎么办 | MISS | FULL |
| 70 | Ability生命周期回调不执行怎么办 | MISS | FULL |
| 72 | 相机无法打开怎么办 | MISS | FULL |
| 81 | UIAbility和UIAbilityContext有什么区别 | MISS | FULL |
| 84 | PersistentStorage和AppStorage有什么区别 | MISS | FULL |
| 89 | 做一个带虚拟滚动的大数据表格 | MISS | FULL |
| 93 | 做一个带进度条的通知 | MISS | FULL |
| 95 | 做一个带动画的列表删除 | MISS | FULL |
| 96 | 做一个带转场的页面跳转 | MISS | FULL |
| 101 | 做一个带通知的下载任务 | MISS | FULL |
| 103 | Android的RecyclerView在鸿蒙对应什么 | MISS | FULL |
| 105 | RN的FlatList对应鸿蒙什么组件 | MISS | FULL |
| 109 | Android的Camera在鸿蒙对应什么 | MISS | FULL |
| 110 | iOS的UIView动画在鸿蒙对应什么 | MISS | FULL |
| 112 | Flutter的Hero动画在鸿蒙对应什么 | MISS | FULL |
| 113 | Android的SharedPreferences在鸿蒙对应什么 | MISS | FULL |
| 114 | Android的Activity在鸿蒙对应什么 | MISS | FULL |
| 116 | iOS的UIViewController在鸿蒙对应什么 | MISS | FULL |
| 123 | 相机拍照的完整流程是什么 | MISS | FULL |
| 124 | 显式动画的执行流程是什么 | MISS | FULL |
| 129 | 相机初始化流程是什么 | MISS | FULL |
| 132 | BLE GATT连接流程 | MISS | FULL |
| 134 | ImagePacker编码流程 | MISS | FULL |
| 142 | 动画在弱设备上卡顿怎么办 | MISS | FULL |
| 148 | Ability启动时参数传递限制 | MISS | FULL |
| 152 | 数据库事务执行时间限制 | MISS | FULL |
| 153 | 图片解码内存限制 | MISS | FULL |
| 154 | 相机预览帧率限制 | MISS | FULL |
| 157 | WebView加载大页面白屏怎么办 | MISS | FULL |
| 158 | 大量图片加载内存溢出怎么办 | MISS | FULL |
| 160 | 相机预览卡顿怎么办 | MISS | FULL |
| 161 | 大量动画同时执行性能问题 | MISS | FULL |
| 169 | HTTP缓存过多怎么办 | MISS | FULL |
| 170 | 定时器执行延迟怎么办 | MISS | FULL |
| 175 | Swiper轮播怎么用 | MISS | FULL |
| 180 | UIAbility怎么创建和启动 | MISS | FULL |
| 182 | 定位服务怎么获取位置 | MISS | FULL |
| 183 | 相机拍照怎么实现 | MISS | FULL |
| 184 | 图片处理怎么实现 | MISS | FULL |
| 186 | 图片选择器怎么用 | MISS | FULL |
| 189 | 图片怎么解码 | MISS | FULL |
| 190 | 显式动画怎么用 | MISS | FULL |