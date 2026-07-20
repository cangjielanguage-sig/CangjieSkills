# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (192 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 192 | 192 | 192 |
| 完全命中 FULL | 65 (33.9%) | 182 (94.8%) | 171 (89.1%) |
| 部分命中 PARTIAL | 0 (0.0%) | 4 (2.1%) | 4 (2.1%) |
| 未命中 MISS | 127 (66.1%) | 6 (3.1%) | 17 (8.9%) |
| Recall@5 (FULL+PARTIAL) | 33.9% | 96.9% | 91.1% |
| Precision@1 (FULL) | 33.9% | 94.8% | 89.1% |
| MRR (平均倒数排名) | 0.176 | 0.700 | 0.684 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 42.4ms | 1.1ms | 54.9ms |
| P50 耗时 | 33.8ms | 0.8ms | 49.5ms |
| P95 耗时 | 117.8ms | 3.2ms | 121.0ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 15.0% | 95.0% | 85.0% |
| comparison | 46.7% | 93.3% | 93.3% |
| composition | 40.0% | 100.0% | 100.0% |
| constrained | 45.0% | 85.0% | 75.0% |
| cross_ecosystem | 33.3% | 100.0% | 93.3% |
| enumeration | 15.0% | 100.0% | 90.0% |
| how_to | 27.3% | 100.0% | 95.5% |
| performance_boundary | 25.0% | 100.0% | 100.0% |
| reverse_lookup | 25.0% | 93.8% | 75.0% |
| semantic_fuzzy | 56.2% | 100.0% | 100.0% |
| workflow | 52.9% | 100.0% | 100.0% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 11 | 192 | 10 |
| 10-100ms | 167 | 0 | 161 |
| 100-500ms | 14 | 0 | 21 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 2 | api_lookup | DeviceInfo获取设备信息的具体API | MISS | FULL | FULL |
| 4 | api_lookup | HttpRequest的request方法参数 | MISS | FULL | FULL |
| 5 | api_lookup | Router.pushUrl的参数 | MISS | FULL | MISS |
| 6 | api_lookup | Router.back的用法 | MISS | FULL | FULL |
| 7 | api_lookup | Router.replaceUrl的参数 | MISS | FULL | MISS |
| 8 | api_lookup | Router.getState怎么用 | MISS | FULL | FULL |
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | FULL |
| 11 | api_lookup | ListScroller的API有哪些 | MISS | FULL | FULL |
| 12 | api_lookup | SwiperController的API有哪些 | MISS | FULL | FULL |
| 13 | api_lookup | RefreshParams的配置参数 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 16 | api_lookup | HttpResponseCache的创建方法 | MISS | FULL | FULL |
| 17 | api_lookup | MultiFormData的属性 | MISS | FULL | FULL |
| 18 | api_lookup | ClientCert的配置方法 | MISS | FULL | FULL |
| 19 | api_lookup | PerformanceTiming的属性 | MISS | FULL | FULL |
| 20 | api_lookup | geometryTransition的参数有哪些 | MISS | FULL | FULL |
| 21 | enumeration | Timer定时器的配置参数有哪些 | MISS | FULL | FULL |
| 22 | enumeration | AppStorage有哪些方法 | MISS | PARTIAL | PARTIAL |
| 23 | enumeration | Swiper有哪些回调事件 | MISS | FULL | FULL |
| 24 | enumeration | UIAbility的生命周期状态有哪些 | MISS | FULL | FULL |
| 27 | enumeration | ResponseCode有哪些状态码 | MISS | FULL | FULL |
| 29 | enumeration | NotificationSlot有哪些配置 | MISS | FULL | FULL |
| 30 | enumeration | Want的属性有哪些 | MISS | FULL | FULL |
| 31 | enumeration | UIAbility有哪些生命周期回调 | MISS | FULL | FULL |
| 32 | enumeration | ErrorManager有哪些方法 | MISS | FULL | FULL |
| 33 | enumeration | CameraManager有哪些方法 | MISS | FULL | FULL |
| 34 | enumeration | CameraInput有哪些事件 | MISS | FULL | FULL |
| 35 | enumeration | WebviewController有哪些方法 | MISS | FULL | FULL |
| 36 | enumeration | WebCookieManager有哪些方法 | MISS | FULL | FULL |
| 37 | enumeration | AnimateParam有哪些配置 | MISS | FULL | MISS |
| 38 | enumeration | TransitionEffect有哪些类型 | MISS | FULL | FULL |
| 39 | enumeration | Environment有哪些内置参数 | MISS | FULL | FULL |
| 40 | enumeration | PersistentStorage有哪些限制 | MISS | FULL | MISS |
| 41 | reverse_lookup | 要实现下拉刷新用什么组件 | MISS | FULL | FULL |
| 42 | reverse_lookup | 要实现懒加载用什么方案 | MISS | FULL | FULL |
| 43 | reverse_lookup | 要实现轮播用什么组件 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | FULL | MISS |
| 45 | reverse_lookup | 要取消通知用什么方法 | MISS | FULL | FULL |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | PARTIAL | PARTIAL |
| 48 | reverse_lookup | 要实现页面跳转用什么方法 | MISS | FULL | MISS |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 50 | reverse_lookup | 要获取相机列表用什么方法 | MISS | FULL | FULL |
| 52 | reverse_lookup | 要设置Cookie用什么API | MISS | FULL | FULL |
| 54 | reverse_lookup | 要实现共享元素转场用什么方法 | FULL | MISS | MISS |
| 55 | reverse_lookup | 要持久化状态用什么组件 | MISS | FULL | FULL |
| 56 | reverse_lookup | 要获取设备环境参数用什么API | MISS | FULL | FULL |
| 57 | semantic_fuzzy | 列表滑动卡顿怎么优化 | MISS | FULL | FULL |
| 63 | semantic_fuzzy | 图片解码失败怎么办 | MISS | FULL | FULL |
| 65 | semantic_fuzzy | 动画执行后界面不更新怎么办 | MISS | FULL | FULL |
| 67 | semantic_fuzzy | 持久化数据丢失怎么办 | MISS | FULL | FULL |
| 68 | semantic_fuzzy | Environment参数获取不到怎么办 | MISS | FULL | FULL |
| 69 | semantic_fuzzy | Ability启动失败怎么排查 | MISS | FULL | FULL |
| 70 | semantic_fuzzy | Ability生命周期回调不执行怎么办 | MISS | FULL | FULL |
| 73 | comparison | List和LazyForEach有什么区别 | MISS | FULL | FULL |
| 75 | comparison | AppStorage和LocalStorage有什么不同 | MISS | FULL | FULL |
| 79 | comparison | ImageSource和PixelMap有什么区别 | MISS | FULL | FULL |
| 80 | comparison | PhotoSession和VideoSession有什么区别 | MISS | MISS | MISS |
| 81 | comparison | UIAbility和UIAbilityContext有什么区别 | MISS | FULL | FULL |
| 83 | comparison | geometryTransition和sharedTransition | MISS | FULL | FULL |
| 84 | comparison | PersistentStorage和AppStorage有什么区别 | MISS | FULL | FULL |
| 85 | comparison | Environment和AppStorage有什么区别 | MISS | FULL | FULL |
| 88 | composition | 做一个带下拉刷新的列表页 | MISS | FULL | FULL |
| 89 | composition | 做一个带虚拟滚动的大数据表格 | MISS | FULL | FULL |
| 91 | composition | 做一个带下拉刷新的网络列表页 | MISS | FULL | FULL |
| 95 | composition | 做一个带动画的列表删除 | MISS | FULL | FULL |
| 96 | composition | 做一个带转场的页面跳转 | MISS | FULL | PARTIAL |
| 97 | composition | 做一个持久化的用户设置页 | MISS | FULL | FULL |
| 98 | composition | 做一个响应深色模式的页面 | MISS | FULL | FULL |
| 99 | composition | 做一个带相机的页面 | MISS | FULL | FULL |
| 101 | composition | 做一个带通知的下载任务 | MISS | FULL | FULL |
| 103 | cross_ecosystem | Android的RecyclerView在鸿蒙对应什么 | MISS | FULL | FULL |
| 104 | cross_ecosystem | React的useState对应鸿蒙什么 | MISS | FULL | FULL |
| 105 | cross_ecosystem | RN的FlatList对应鸿蒙什么组件 | MISS | FULL | FULL |
| 106 | cross_ecosystem | 鸿蒙版SwipeRefreshLayout怎么写 | MISS | FULL | FULL |
| 107 | cross_ecosystem | Android的Notification在鸿蒙对应什么 | MISS | FULL | MISS |
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
| 135 | constrained | 后台运行时怎么保持网络连接 | MISS | FULL | FULL |
| 138 | constrained | 通知权限没申请怎么办 | MISS | FULL | FULL |
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
| 155 | performance_boundary | 一万条数据的列表渲染卡顿怎么办 | MISS | FULL | FULL |
| 156 | performance_boundary | 快速滑动列表时内存飙升怎么办 | MISS | FULL | FULL |
| 158 | performance_boundary | 大量图片加载内存溢出怎么办 | MISS | FULL | FULL |
| 159 | performance_boundary | 数据库查询太慢怎么办 | MISS | FULL | FULL |
| 160 | performance_boundary | 相机预览卡顿怎么办 | MISS | FULL | FULL |
| 162 | performance_boundary | 页面转场内存占用过大 | MISS | FULL | FULL |
| 163 | performance_boundary | PersistentStorage读写慢怎么办 | MISS | FULL | FULL |
| 164 | performance_boundary | 大量Ability启动性能问题 | MISS | FULL | FULL |
| 165 | performance_boundary | WebView内存占用过大怎么办 | MISS | FULL | FULL |
| 166 | performance_boundary | 相机录像内存飙升怎么办 | MISS | FULL | FULL |
| 169 | performance_boundary | HTTP缓存过多怎么办 | MISS | FULL | FULL |
| 170 | performance_boundary | 定时器执行延迟怎么办 | MISS | FULL | FULL |
| 171 | how_to | List组件怎么用 | MISS | FULL | FULL |
| 174 | how_to | 页面跳转怎么做 | MISS | FULL | FULL |
| 175 | how_to | Swiper轮播怎么用 | MISS | FULL | FULL |
| 176 | how_to | Grid网格布局怎么用 | MISS | FULL | FULL |
| 178 | how_to | Timer定时器怎么用 | MISS | FULL | FULL |
| 180 | how_to | UIAbility怎么创建和启动 | MISS | FULL | FULL |
| 181 | how_to | 后台任务怎么调度 | MISS | FULL | FULL |
| 182 | how_to | 定位服务怎么获取位置 | MISS | FULL | FULL |
| 184 | how_to | 图片处理怎么实现 | MISS | FULL | FULL |
| 185 | how_to | 动画效果怎么实现 | MISS | FULL | FULL |
| 186 | how_to | 图片选择器怎么用 | MISS | FULL | FULL |
| 187 | how_to | 通知怎么发 | MISS | FULL | FULL |
| 189 | how_to | 图片怎么解码 | MISS | FULL | FULL |
| 190 | how_to | 显式动画怎么用 | MISS | FULL | FULL |
| 191 | how_to | PersistentStorage怎么配置 | MISS | FULL | MISS |
| 192 | how_to | Environment怎么获取参数 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 108 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 2 | DeviceInfo获取设备信息的具体API | MISS | FULL |
| 4 | HttpRequest的request方法参数 | MISS | FULL |
| 6 | Router.back的用法 | MISS | FULL |
| 8 | Router.getState怎么用 | MISS | FULL |
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 11 | ListScroller的API有哪些 | MISS | FULL |
| 12 | SwiperController的API有哪些 | MISS | FULL |
| 13 | RefreshParams的配置参数 | MISS | FULL |
| 16 | HttpResponseCache的创建方法 | MISS | FULL |
| 17 | MultiFormData的属性 | MISS | FULL |
| 18 | ClientCert的配置方法 | MISS | FULL |
| 19 | PerformanceTiming的属性 | MISS | FULL |
| 20 | geometryTransition的参数有哪些 | MISS | FULL |
| 21 | Timer定时器的配置参数有哪些 | MISS | FULL |
| 23 | Swiper有哪些回调事件 | MISS | FULL |
| 24 | UIAbility的生命周期状态有哪些 | MISS | FULL |
| 27 | ResponseCode有哪些状态码 | MISS | FULL |
| 29 | NotificationSlot有哪些配置 | MISS | FULL |
| 30 | Want的属性有哪些 | MISS | FULL |
| 31 | UIAbility有哪些生命周期回调 | MISS | FULL |
| 32 | ErrorManager有哪些方法 | MISS | FULL |
| 33 | CameraManager有哪些方法 | MISS | FULL |
| 34 | CameraInput有哪些事件 | MISS | FULL |
| 35 | WebviewController有哪些方法 | MISS | FULL |
| 36 | WebCookieManager有哪些方法 | MISS | FULL |
| 38 | TransitionEffect有哪些类型 | MISS | FULL |
| 39 | Environment有哪些内置参数 | MISS | FULL |
| 41 | 要实现下拉刷新用什么组件 | MISS | FULL |
| 42 | 要实现懒加载用什么方案 | MISS | FULL |
| 43 | 要实现轮播用什么组件 | MISS | FULL |
| 45 | 要取消通知用什么方法 | MISS | FULL |
| 50 | 要获取相机列表用什么方法 | MISS | FULL |
| 52 | 要设置Cookie用什么API | MISS | FULL |
| 55 | 要持久化状态用什么组件 | MISS | FULL |
| 56 | 要获取设备环境参数用什么API | MISS | FULL |
| 57 | 列表滑动卡顿怎么优化 | MISS | FULL |
| 63 | 图片解码失败怎么办 | MISS | FULL |
| 65 | 动画执行后界面不更新怎么办 | MISS | FULL |
| 67 | 持久化数据丢失怎么办 | MISS | FULL |
| 68 | Environment参数获取不到怎么办 | MISS | FULL |
| 69 | Ability启动失败怎么排查 | MISS | FULL |
| 70 | Ability生命周期回调不执行怎么办 | MISS | FULL |
| 73 | List和LazyForEach有什么区别 | MISS | FULL |
| 75 | AppStorage和LocalStorage有什么不同 | MISS | FULL |
| 79 | ImageSource和PixelMap有什么区别 | MISS | FULL |
| 81 | UIAbility和UIAbilityContext有什么区别 | MISS | FULL |
| 83 | geometryTransition和sharedTransition有什么区别 | MISS | FULL |
| 84 | PersistentStorage和AppStorage有什么区别 | MISS | FULL |
| 85 | Environment和AppStorage有什么区别 | MISS | FULL |
| 88 | 做一个带下拉刷新的列表页 | MISS | FULL |
| 89 | 做一个带虚拟滚动的大数据表格 | MISS | FULL |
| 91 | 做一个带下拉刷新的网络列表页 | MISS | FULL |
| 95 | 做一个带动画的列表删除 | MISS | FULL |
| 97 | 做一个持久化的用户设置页 | MISS | FULL |
| 98 | 做一个响应深色模式的页面 | MISS | FULL |
| 99 | 做一个带相机的页面 | MISS | FULL |
| 101 | 做一个带通知的下载任务 | MISS | FULL |
| 103 | Android的RecyclerView在鸿蒙对应什么 | MISS | FULL |
| 104 | React的useState对应鸿蒙什么 | MISS | FULL |
| 105 | RN的FlatList对应鸿蒙什么组件 | MISS | FULL |
| 106 | 鸿蒙版SwipeRefreshLayout怎么写 | MISS | FULL |
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
| 135 | 后台运行时怎么保持网络连接 | MISS | FULL |
| 138 | 通知权限没申请怎么办 | MISS | FULL |
| 140 | 图片内存占用过大怎么办 | MISS | FULL |
| 142 | 动画在弱设备上卡顿怎么办 | MISS | FULL |
| 144 | Environment参数不支持怎么办 | MISS | FULL |
| 153 | 图片解码内存限制 | MISS | FULL |
| 155 | 一万条数据的列表渲染卡顿怎么办 | MISS | FULL |
| 156 | 快速滑动列表时内存飙升怎么办 | MISS | FULL |
| 158 | 大量图片加载内存溢出怎么办 | MISS | FULL |
| 159 | 数据库查询太慢怎么办 | MISS | FULL |
| 160 | 相机预览卡顿怎么办 | MISS | FULL |
| 162 | 页面转场内存占用过大 | MISS | FULL |
| 163 | PersistentStorage读写慢怎么办 | MISS | FULL |
| 164 | 大量Ability启动性能问题 | MISS | FULL |
| 165 | WebView内存占用过大怎么办 | MISS | FULL |
| 166 | 相机录像内存飙升怎么办 | MISS | FULL |
| 169 | HTTP缓存过多怎么办 | MISS | FULL |
| 170 | 定时器执行延迟怎么办 | MISS | FULL |
| 171 | List组件怎么用 | MISS | FULL |
| 174 | 页面跳转怎么做 | MISS | FULL |
| 175 | Swiper轮播怎么用 | MISS | FULL |
| 176 | Grid网格布局怎么用 | MISS | FULL |
| 178 | Timer定时器怎么用 | MISS | FULL |
| 180 | UIAbility怎么创建和启动 | MISS | FULL |
| 181 | 后台任务怎么调度 | MISS | FULL |
| 182 | 定位服务怎么获取位置 | MISS | FULL |
| 184 | 图片处理怎么实现 | MISS | FULL |
| 185 | 动画效果怎么实现 | MISS | FULL |
| 186 | 图片选择器怎么用 | MISS | FULL |
| 187 | 通知怎么发 | MISS | FULL |
| 189 | 图片怎么解码 | MISS | FULL |
| 190 | 显式动画怎么用 | MISS | FULL |
| 192 | Environment怎么获取参数 | MISS | FULL |