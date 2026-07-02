# 三引擎搜索对比评测报告

**测试集**: eval_queries_comprehensive_deduped.jsonl (50 条)
**评测引擎**: card / graph / fusion
**计时范围**: 仅纯搜索（不含 query understanding）

## 1. 总体对比

| 指标 | card | graph | fusion |
|------|------|-------|--------|
| 总查询数 | 50 | 50 | 50 |
| 完全命中 FULL | 18 (36.0%) | 45 (90.0%) | 36 (72.0%) |
| 部分命中 PARTIAL | 0 (0.0%) | 3 (6.0%) | 3 (6.0%) |
| 未命中 MISS | 32 (64.0%) | 2 (4.0%) | 11 (22.0%) |
| Recall@5 (FULL+PARTIAL) | 36.0% | 96.0% | 78.0% |
| Precision@1 (FULL) | 36.0% | 90.0% | 72.0% |
| MRR (平均倒数排名) | 0.121 | 0.578 | 0.531 |
| 平均直接命中数 | 5.0 | 5.0 | 6.0 |
| 平均搜索耗时 | 52.3ms | 1.3ms | 54.7ms |
| P50 耗时 | 46.6ms | 1.0ms | 48.9ms |
| P95 耗时 | 114.5ms | 4.8ms | 109.9ms |

## 2. 各类别 Recall@5 对比

| 类别 | card | graph | fusion |
|------|------|-------|--------|
| api_lookup | 50.0% | 95.0% | 85.0% |
| enumeration | 25.0% | 100.0% | 80.0% |
| reverse_lookup | 30.0% | 90.0% | 60.0% |

## 3. 搜索耗时分布

| 范围 | card | graph | fusion |
|------|------|-------|--------|
| <10ms | 6 | 50 | 7 |
| 10-100ms | 40 | 0 | 36 |
| 100-500ms | 4 | 0 | 7 |
| 500ms-1s | 0 | 0 | 0 |
| >1s | 0 | 0 | 0 |

## 4. MISS 查询对比

| ID | 类别 | 查询 | card | graph | fusion |
|---:|------|------|------|-------|--------|
| 1 | api_lookup | HttpRequest的timeout参数怎么设置 | MISS | PARTIAL | PARTIAL |
| 2 | api_lookup | DeviceInfo获取设备信息的具体API | MISS | FULL | FULL |
| 6 | api_lookup | Router.back的用法 | FULL | FULL | MISS |
| 7 | api_lookup | Router.replaceUrl的参数 | FULL | FULL | MISS |
| 9 | api_lookup | UIAbilityContext的API有哪些 | MISS | FULL | FULL |
| 10 | api_lookup | Timer.once的参数 | MISS | FULL | FULL |
| 12 | api_lookup | SwiperController的API有哪些 | MISS | FULL | FULL |
| 14 | api_lookup | Duration的构造方法 | MISS | MISS | MISS |
| 16 | api_lookup | HttpResponseCache的创建方法 | MISS | FULL | FULL |
| 17 | api_lookup | MultiFormData的属性 | MISS | FULL | FULL |
| 18 | api_lookup | ClientCert的配置方法 | MISS | FULL | FULL |
| 20 | api_lookup | geometryTransition的参数有哪些 | MISS | FULL | FULL |
| 21 | enumeration | Timer定时器的配置参数有哪些 | MISS | FULL | MISS |
| 22 | enumeration | AppStorage有哪些方法 | MISS | FULL | FULL |
| 23 | enumeration | Swiper有哪些回调事件 | MISS | FULL | FULL |
| 24 | enumeration | UIAbility的生命周期状态有哪些 | MISS | FULL | MISS |
| 27 | enumeration | ResponseCode有哪些状态码 | MISS | FULL | FULL |
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
| 42 | reverse_lookup | 要实现懒加载用什么方案 | MISS | FULL | MISS |
| 43 | reverse_lookup | 要实现轮播用什么组件 | MISS | FULL | FULL |
| 44 | reverse_lookup | 要发送通知用什么API | MISS | MISS | MISS |
| 45 | reverse_lookup | 要取消通知用什么方法 | MISS | FULL | MISS |
| 47 | reverse_lookup | 要查询数据库用什么类 | MISS | FULL | FULL |
| 49 | reverse_lookup | 要启动另一个Ability用什么API | MISS | FULL | MISS |
| 50 | reverse_lookup | 要获取相机列表用什么方法 | MISS | FULL | FULL |

## 5. Fusion 补救命中（fusion=FULL 但 card 或 graph = MISS）

共 22 条：

| ID | 查询 | card | graph |
|---:|------|------|-------|
| 2 | DeviceInfo获取设备信息的具体API | MISS | FULL |
| 9 | UIAbilityContext的API有哪些 | MISS | FULL |
| 10 | Timer.once的参数 | MISS | FULL |
| 12 | SwiperController的API有哪些 | MISS | FULL |
| 16 | HttpResponseCache的创建方法 | MISS | FULL |
| 17 | MultiFormData的属性 | MISS | FULL |
| 18 | ClientCert的配置方法 | MISS | FULL |
| 20 | geometryTransition的参数有哪些 | MISS | FULL |
| 22 | AppStorage有哪些方法 | MISS | FULL |
| 23 | Swiper有哪些回调事件 | MISS | FULL |
| 27 | ResponseCode有哪些状态码 | MISS | FULL |
| 29 | NotificationSlot有哪些配置 | MISS | FULL |
| 30 | Want的属性有哪些 | MISS | FULL |
| 31 | UIAbility有哪些生命周期回调 | MISS | FULL |
| 32 | ErrorManager有哪些方法 | MISS | FULL |
| 33 | CameraManager有哪些方法 | MISS | FULL |
| 34 | CameraInput有哪些事件 | MISS | FULL |
| 36 | WebCookieManager有哪些方法 | MISS | FULL |
| 37 | AnimateParam有哪些配置 | MISS | FULL |
| 43 | 要实现轮播用什么组件 | MISS | FULL |
| 47 | 要查询数据库用什么类 | MISS | FULL |
| 50 | 要获取相机列表用什么方法 | MISS | FULL |