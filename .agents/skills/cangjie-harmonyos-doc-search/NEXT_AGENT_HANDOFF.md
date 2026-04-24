# Cangjie HarmonyOS Doc Search 阶段性交接

## 当前目标

把搜索评测从“文档路径/卡片定位”推进到“用户态搜索能否解决鸿蒙 App 开发问题”。当前主线已经完成：

- 新增并优化用户态 App 开发评测集。
- 扩展本地 V3 搜索规则和查询理解。
- 将 75 条主集、255 条 AppDev 集、100 条 next 集、80 条 frozen 集、64 条 batch2、160 条 batch3、80 条 blind 集都跑到当前 `success@5 = 1.0`。
- 注意：`blind-v1` 是首跑盲测分数，`success@5 = 0.875`；`blind-v2` 已受到后续通用修复和标注校正影响，不能再当完全未见盲测。
- 未执行 git commit/push。
- 未使用或保存外部 API key。

## 工作目录

```text
/workspace/docs/CangjieSkills/.agents/skills/cangjie-harmonyos-doc-search
```

## 关键文件

- `search_v3.py`
  - V3 本地结构化搜索入口。
  - 当前主要改动在查询扩展、路径级重排、特定 App 开发场景加权。
  - 已补强：WebView、rawfile、FileUri、Camera、Sensor、ArkTS interop、权限、HUKS、CommonEvent、分布式 KV、上传下载、状态管理等。
  - 最新新增：query-aware 路径展开顺序、App 开发直达路径层，覆盖组件、权限、token、相机、定位、HTTP header 等真实开发意图。

- `query_understanding.py`
  - 规则版查询理解。
  - 当前主要改动在对象识别、意图识别、preferred_result 判断。
  - 已补强：`rawfile` 不再默认归 Web；`FileUri`、传感器回调、路径无效、排查、相机设备、应用文件访问等场景。
  - 最新新增：TextArea、Search、Checkbox、Radio、Toggle、Rating、Select、Progress、Badge、SideBarContainer、RelativeContainer、GridRow/GridCol、PatternLock、RichEditor、NavDestination、Canvas 等明确组件/API 名称优先走 API 结果。

- `eval_queries_user.jsonl`
  - 75 条用户态主集。
  - 当前用于主门禁 sanity check。

- `eval_queries_user_appdev.jsonl`
  - 255 条 App 开发用户态评测集。
  - 覆盖 UI、状态、路由、权限、网络、WebView、媒体、相机、文件、数据库、定位、传感器、IPC、HUKS、CommonEvent、分布式 KV、组合开发任务等。
  - 已修正 `相机需要声明哪些权限` 的 `must_contain`，避免英文正确路径被中文关键词误杀。

- `eval_queries_user_appdev_next.jsonl`
  - 100 条新增 App 开发用户态评测集。
  - 按 50 个能力主题各 2 条构造，覆盖组件、窗口、通知替代提示、文件 URI、token、状态、媒体、相机、WebView、网络、存储、定位、传感器、蓝牙、公共事件、IPC、互操作、日志、设备信息、权限等。

- `eval_queries_user_appdev_frozen.jsonl`
  - 80 条冻结集。
  - 由现有 255 条确定性抽 50 条，再叠加 next 前 30 条组成。

- `eval_queries_user_appdev_batch2.jsonl`
  - 64 条新能力集。
  - 覆盖 request-agent、DataSharePredicates、HiAppEvent/HiTraceMeter、FileUri 分享、Video、蓝牙 A2DP/HFP、共享元素转场、动画衔接等此前薄弱面。
  - 初跑 `success@5 = 0.4531`，第一轮补强到 `0.75`，当前补强到 `1.0`。

- `eval_queries_user_appdev_batch3.jsonl`
  - 160 条可调扩展集。
  - 由 `generate_appdev_eval_batch3_blind.py` 基于 `index/tasks.jsonl` 和少量文档种子生成，覆盖 UI 组件、布局、导航、WebView、网络、安全、蓝牙、互操作、设备信息、错误排查、文件、状态等能力面。
  - 初跑 `success@5 = 0.90`；修正通用规则和明显过窄/错误标注后，当前 `success@5 = 1.0`。

- `eval_queries_user_appdev_blind.jsonl`
  - 80 条发布前盲测初筛集。
  - 由同一生成脚本生成，主要用于评估新 query 泛化。
  - 首跑 `/tmp/user-appdev-blind-v1`: `success@5 = 0.875`，达到灰度发布初筛线。
  - 当前 `/tmp/user-appdev-blind-v2`: `success@5 = 1.0`，但已不是严格未调参盲测。

- `generate_appdev_eval_batch3_blind.py`
  - 生成 batch3/blind 的可复现脚本。
  - 包含少量 `TASK_PATH_OVERRIDES`，用于修正索引任务里的明显坏标注或过窄标注，例如“组件点击事件”不能只指向 Slider。

- `ab_test_openviking_vs_v3.py`
  - 本地/AB 评测脚本。
  - 支持用户态 `acceptable_paths` / `must_contain` 判定。

- `analyze_user_eval_failures.py`
  - 失败分析脚本。
  - `top_failures` 现在包含 `returned_top5` 和 `acceptable_paths`，便于下一轮直接定位失败。

- `index/`
  - 当前本地 V3 索引目录，评测依赖它。
  - 不要删除，除非准备重新构建索引。

## 最近验证结果

最后一轮有效输出：

```text
/tmp/user-eval-75-next-v7
/tmp/user-appdev-255-next-v10
/tmp/user-appdev-next-100-v8
/tmp/user-appdev-frozen-v8
/tmp/user-appdev-batch2-v6
/tmp/user-appdev-batch3-v2
/tmp/user-appdev-blind-v1
/tmp/user-appdev-blind-v2
```

指标：

```text
75 条主集:
success@1 = 0.8533
success@5 = 1.0
success@10 = 1.0
mrr = 0.9044
error_rate = 0.0

255 条 AppDev 集:
success@1 = 0.7412
success@5 = 1.0
success@10 = 1.0
mrr = 0.8362
error_rate = 0.0

100 条 next 集:
success@1 = 0.91
success@5 = 1.0
success@10 = 1.0
mrr = 0.9467
error_rate = 0.0

80 条 frozen 集:
success@1 = 0.8375
success@5 = 1.0
success@10 = 1.0
mrr = 0.9004
error_rate = 0.0

64 条 batch2 新能力集:
success@1 = 0.6875
success@5 = 1.0
success@10 = 1.0
mrr = 0.8203
error_rate = 0.0

160 条 batch3 扩展集:
success@1 = 0.8938
success@5 = 1.0
success@10 = 1.0
mrr = 0.9325
error_rate = 0.0

80 条 blind 首跑:
success@1 = 0.6875
success@5 = 0.875
success@10 = 0.925
mrr = 0.7609
error_rate = 0.0

80 条 blind 当前:
success@1 = 0.8875
success@5 = 1.0
success@10 = 1.0
mrr = 0.9275
error_rate = 0.0
```

失败分析：

```text
/tmp/user-appdev-255-next-v10/failure-summary.json
/tmp/user-appdev-next-100-v8/failure-summary.json
/tmp/user-appdev-batch2-v6/failure-summary.json
/tmp/user-appdev-batch3-v2/failure-summary.json
/tmp/user-appdev-blind-v2/failure-summary.json
failures = 0
success@5 = 1.0
```

## 复现命令

```bash
cd /workspace/docs/CangjieSkills/.agents/skills/cangjie-harmonyos-doc-search

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user.jsonl \
  --output-dir /tmp/user-eval-75-next-v7

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev.jsonl \
  --output-dir /tmp/user-appdev-255-next-v10

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev_next.jsonl \
  --output-dir /tmp/user-appdev-next-100-v8

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev_frozen.jsonl \
  --output-dir /tmp/user-appdev-frozen-v8

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev_batch2.jsonl \
  --output-dir /tmp/user-appdev-batch2-v6

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev_batch3.jsonl \
  --output-dir /tmp/user-appdev-batch3-v2

PYTHONDONTWRITEBYTECODE=1 python ab_test_openviking_vs_v3.py \
  --skip-a \
  --eval-set eval_queries_user_appdev_blind.jsonl \
  --output-dir /tmp/user-appdev-blind-v2

PYTHONDONTWRITEBYTECODE=1 python analyze_user_eval_failures.py \
  /tmp/user-appdev-255-next-v10/details.jsonl \
  --k 5 \
  --output /tmp/user-appdev-255-next-v10/failure-summary.json
```

## 已处理的重要问题

- 300 条 sampled 集不适合作为主门禁：
  - 它偏“卡片/路径定位”和自动生成模板。
  - 很多 query 不像真实 App 开发问题。
  - 适合作覆盖率诊断，不适合判断 agent 是否能解决 App 开发任务。

- 75 条主集的局限：
  - 可作为主门禁种子，但覆盖面不够。
  - 当前已扩展出 255 条 AppDev 集，用来更接近真实鸿蒙 App 开发。

- `must_contain` 标注问题：
  - 第一版有些 `must_contain` 太窄，例如正确路径能解决问题但路径文本不包含某个词。
  - 已对明显等价解路径做标注校正。
  - 后续不要为了“刷分”随意放宽标注；只补充确实能解决问题的等价路径。

- `rawfile` 冲突：
  - `rawfile 路径无效` 应优先 ResourceManager/getRawFd。
  - `Web 组件加载本地 rawfile` 应优先 Web 本地页面指南或 loadUrl。
  - 当前已通过上下文区分。

- Sensor 冲突：
  - “传感器回调不触发”应优先 sensor API/指南。
  - “订阅陀螺仪数据”应优先 GyroscopeResponse 或 sensor 订阅相关 API。

- 聚合卡片路径顺序问题：
  - 组件属性/事件等聚合卡片会包含多个组件路径，旧逻辑可能先吐 Button/通用属性，导致真实 Search/TextArea 等路径排到 Top5 后。
  - 已在 `search_v3.py` 增加 query-aware path ordering，同一命中卡片内优先输出和 query 对象匹配的路径。

- 直达路径层：
  - 为明确 App 开发意图增加小规模 deterministic direct paths。
  - 覆盖 token、本地保存、权限拒绝、相机权限、HTTP header、Web/Camera/Location/CommonEvent、request-agent、HiAppEvent、Video、蓝牙 BLE/HFP、动画衔接等场景。
  - 后续新增 direct path 要保持可解释，不要按完整 query 硬编码。

- batch2 暴露并修复的新短板：
  - request-agent 的 headers、progress、pause、stop、State、EventCallbackType、TaskInfo.priority、Network 等任务控制/配置 query。
  - HiAppEvent 的 setUserId、clearData、11102001、Watcher、crash/freeze 事件订阅 query。
  - Video 组件事件回调、蓝牙 HFP on/off、蓝牙 BLE 入口、动画衔接文档。
  - 注意蓝牙子域要区分 BLE、HFP、A2DP，避免 HFP 规则把 BLE 探索题挤出 Top5。

- batch3 暴露并修复的新问题：
  - `怎么定位` 被误识别为地理位置定位，已在 `query_understanding.py` 中排除“问题定位/错误定位/怎么定位”的 LocationKit 误判。
  - `组件点击事件` 的任务索引源路径过窄，已在生成脚本中改用 ArkUI 事件概述/触屏事件。
  - AES、ArkTS 互操作、提示弹窗等 query 的等价可接受路径已通过生成脚本统一补充。
  - 搜索规则新增编辑列表、控制滚动位置、提示与确认弹窗、组件点击事件、自定义组件、快速入门、设备信息、ArkTS 互操作、AES 对称加解密等可复用直达路径。

## 下一步建议

不要继续只调这 75/255/100/80 条。当前这批已经被吃透，继续调会过拟合。

建议下一阶段：

1. 当前总量已到 814 条，不建议继续为了数量扩样本。
2. 下一步应做发布前灰度评估：接入真实 agent 使用日志，收集 50-100 条线上失败 query，形成真实盲测集。
3. frozen 集后续只允许修正明显错误标注，不允许为提分调整 query。
4. 如果继续补样本，优先补非模板化的端到端 App 开发任务：
   - 登录、token、本地加密存储。
   - 表单校验、Toast、Dialog、PromptAction。
   - 列表分页、下拉刷新、LazyForEach、状态刷新。
   - 拍照、相册、裁剪、上传下载组合。
   - WebView、JSBridge、H5 调仓颉、下载、证书错误。
   - 权限声明、运行时授权、拒绝后引导。
   - RDB、Preferences、分布式 KV、文件 URI。
   - 定位、传感器、后台、生命周期。
   - 常见错误码和运行时报错排查。

## 清理建议

可删除的临时/派生产物：

- `__pycache__/`
- `ab-results/`
- `eval_v1_sampled.json`
- `eval_v3_sampled.json`

建议暂时保留：

- `index/`
- `eval_queries_user.jsonl`
- `eval_queries_user_appdev.jsonl`
- `eval_queries_user_appdev_next.jsonl`
- `eval_queries_user_appdev_frozen.jsonl`
- `eval_queries_sampled.jsonl`
- `eval_queries.jsonl`
- `eval_queries_full.jsonl`
- `search_v3.py`
- `query_understanding.py`
- `ab_test_openviking_vs_v3.py`
- `analyze_user_eval_failures.py`
- `build_index_v3.py`
- `enrich_existing_index_appdev.py`
