# OpenViking vs V3 多维评测报告

**评测日期**: 2026-04-29
**评测数据**: 1,077 条（去重后）
**评测维度**: category、capability、query_style、difficulty

---

## 一、评测集概况

### 1.1 评测集来源

| 评测集 | 条目数 | 定位 | 特点 |
|--------|--------|------|------|
| eval_queries.jsonl | 71 | 早期种子集 | 仅有 category 标注 |
| eval_queries_user.jsonl | 75 | 主门禁集 | 完整多维标注 |
| eval_queries_user_appdev.jsonl | 255 | 应用开发扩展集 | 多批次合并 |
| eval_queries_user_appdev_batch2.jsonl | 64 | 第二批补丁 | 应用开发场景 |
| eval_queries_user_appdev_batch3.jsonl | 160 | 第三批 | 从索引元数据生成 |
| eval_queries_user_appdev_next.jsonl | 100 | 增量集 | 持续扩展 |
| eval_queries_user_appdev_frozen.jsonl | 80 | 冻结基准集 | 回归对比 |
| eval_queries_user_appdev_blind.jsonl | 80 | 盲测集 | 发布门禁 |
| eval_queries_user_appdev_blind_20260424.jsonl | 80 | 严格盲测集 | 最新快照 |
| eval_queries_app_agent_dev.jsonl | 32 | App Agent 场景 | 目标规划评测 |
| eval_queries_sampled.jsonl | 300 | 分层抽样子集 | 全量集代表性子集 |

**总计**: 1,297 条 → 去重后 **1,077 条**

### 1.2 维度分布

#### 按 category（查询类别）

| 类别 | 条目数 | 占比 | 说明 |
|------|--------|------|------|
| error-driven | 289 | 26.8% | **错误排查型**：用户遇到错误或异常，需要查找解决方案 |
| how_to | 279 | 25.9% | **操作指南型**：用户想学习如何实现某个功能 |
| exploration | 124 | 11.5% | **探索型**：用户不确定具体需求，需要浏览相关文档 |
| api_lookup | 110 | 10.2% | **API 查找型**：用户明确要查找某个 API 或组件 |
| exact | 90 | 8.4% | **精确查询型**：用户输入精确的 API 名称或关键词 |
| semi-structured | 77 | 7.1% | **半结构化型**：用户输入包含结构化信息（如"Column 的 alignItems"） |
| natural | 76 | 7.1% | **自然语言型**：用户用自然语言描述需求 |
| app_agent_dev | 32 | 3.0% | **App Agent 开发型**：高层目标拆解为查询计划 |

#### 按 capability（能力域）

| 能力域 | 条目数 | 说明 |
|--------|--------|------|
| unknown | 371 | 未标注能力域 |
| arkui_component | 208 | ArkUI 组件（Button、List、Column 等） |
| troubleshooting | 48 | 故障排查 |
| ability | 40 | 应用能力（Ability、ServiceAbility 等） |
| webview | 38 | WebView 组件 |
| network | 35 | 网络请求（HTTP、WebSocket 等） |
| resource_file | 33 | 资源文件管理 |
| storage | 30 | 数据存储（Preferences、数据库等） |
| security | 28 | 安全与权限 |
| diagnostics | 24 | 诊断工具 |
| media | 24 | 多媒体（音视频播放、录制） |
| file_transfer | 24 | 文件传输 |
| arkui_state | 21 | ArkUI 状态管理 |
| interop | 17 | 仓颉与 ArkTS 互操作 |
| device_info | 16 | 设备信息 |
| bluetooth | 15 | 蓝牙 |
| camera | 14 | 相机 |
| permission | 13 | 权限管理 |
| location | 13 | 定位服务 |
| general | 12 | 通用功能 |
| ipc | 9 | 进程间通信 |
| window_display | 9 | 窗口与显示 |
| common_event | 8 | 公共事件 |
| sensor | 7 | 传感器 |
| distributed_storage | 6 | 分布式存储 |
| websocket | 6 | WebSocket |
| telephony | 3 | 电话服务 |
| graphics | 2 | 图形渲染 |
| hilog | 2 | 日志系统 |
| navigation | 1 | 导航 |

#### 按 query_style（查询风格）

| 风格 | 条目数 | 说明 |
|------|--------|------|
| unknown | 371 | 未标注风格 |
| how_to | 261 | 操作类：如何实现某功能 |
| debug | 224 | 调试类：排查错误或异常 |
| exact_api | 116 | 精确 API 类：直接查询 API 名称 |
| explore | 58 | 探索类：浏览相关文档 |
| integration | 42 | 集成类：多个功能组合使用 |
| task | 4 | 任务类：完成特定任务 |
| api_lookup | 1 | API 查找类 |

#### 按 difficulty（难度等级）

| 难度 | 条目数 | 说明 |
|------|--------|------|
| normal | 393 | 普通难度：单一功能查询 |
| compound | 310 | 复合难度：涉及多个功能或场景 |
| basic | 3 | 基础难度：最基础的查询 |
| unknown | 371 | 未标注难度 |

---

## 二、多维评测结果

### 2.1 整体对比

| 指标 | OpenViking | V3 | 提升幅度 | 胜者 |
|------|------------|-----|----------|------|
| **success@1** | 48.9% | 65.9% | +34.8% | V3 |
| **success@5** | 73.4% | 80.2% | +9.3% | V3 |
| **success@10** | 80.9% | 81.4% | +0.6% | V3 |
| **MRR** | 0.592 | 0.715 | +20.8% | V3 |
| **延迟 p50** | 239ms | 315ms | -24.1% | OpenViking |
| **延迟 p95** | 1231ms | 413ms | -66.4% | V3 |

**结论**: V3 在检索效果上全面领先，OpenViking 在 p50 延迟上有优势但 p95 延迟波动大。

### 2.2 按 category 维度

| 类别 | OpenViking success@5 | V3 success@5 | 提升 | 胜者 |
|------|---------------------|--------------|------|------|
| **how_to** | 78.5% | 100% | +27.4% | V3 |
| **api_lookup** | 77.3% | 100% | +29.4% | V3 |
| **app_agent_dev** | 81.3% | 100% | +23.0% | V3 |
| **error-driven** | 66.4% | 82.7% | +24.5% | V3 |
| **exploration** | 54.0% | 63.7% | +18.0% | V3 |
| **exact** | 75.6% | 53.3% | -29.5% | OpenViking |
| **natural** | 86.8% | 54.0% | -37.8% | OpenViking |
| **semi-structured** | 87.0% | 46.8% | -46.2% | OpenViking |

**分析**:
- **V3 优势场景**: 任务型查询（how_to、api_lookup、app_agent_dev）和错误排查（error-driven）
- **OpenViking 优势场景**: 精确查询（exact）、自然语言（natural）、半结构化（semi-structured）

### 2.3 按 capability 维度（重点能力域）

| 能力域 | OpenViking success@5 | V3 success@5 | 提升 | 胜者 |
|--------|---------------------|--------------|------|------|
| arkui_component | 86.1% | 100% | +16.1% | V3 |
| troubleshooting | 25.0% | 100% | +300% | V3 |
| interop | 23.5% | 100% | +325% | V3 |
| network | 60.0% | 100% | +66.7% | V3 |
| bluetooth | 60.0% | 100% | +66.7% | V3 |
| security | 75.0% | 100% | +33.3% | V3 |
| webview | 81.6% | 100% | +22.5% | V3 |
| media | 91.7% | 100% | +9.0% | V3 |
| storage | 73.3% | 100% | +36.4% | V3 |
| location | 46.2% | 100% | +116.7% | V3 |
| ability | 80.0% | 100% | +25.0% | V3 |
| camera | 92.9% | 100% | +7.7% | V3 |
| device_info | 100% | 100% | 0% | 平局 |
| diagnostics | 79.2% | 100% | +26.3% | V3 |

**分析**:
- **V3 提升最大的能力域**: troubleshooting (+300%)、interop (+325%)、location (+116.7%)
- **V3 所有能力域都达到 100% success@5**（除 unknown 外）

### 2.4 按 query_style 维度

| 风格 | OpenViking success@5 | V3 success@5 | 提升 | 胜者 |
|------|---------------------|--------------|------|------|
| how_to | 77.8% | 100% | +28.5% | V3 |
| debug | 71.0% | 100% | +40.8% | V3 |
| exact_api | 77.6% | 100% | +28.9% | V3 |
| explore | 75.9% | 100% | +31.8% | V3 |
| integration | 78.6% | 100% | +27.2% | V3 |
| task | 100% | 100% | 0% | 平局 |

**分析**:
- **V3 在所有查询风格上都达到 100% success@5**
- **debug 风格提升最大**: +40.8%

### 2.5 按 difficulty 维度

| 难度 | OpenViking success@5 | V3 success@5 | 提升 | 胜者 |
|------|---------------------|--------------|------|------|
| basic | 66.7% | 100% | +50.0% | V3 |
| normal | 78.1% | 100% | +28.0% | V3 |
| compound | 72.6% | 100% | +37.7% | V3 |

**分析**:
- **V3 在所有难度等级上都达到 100% success@5**
- **基础难度提升最大**: +50.0%

---

## 三、评测集科学性审视

### 3.1 优点

#### ✅ 多维度覆盖设计
评测集沿 5 个正交维度标注（category、capability、query_style、difficulty），支持按维度切片分析，便于定位薄弱环节。

#### ✅ Ground Truth 设计合理
每条 query 都有明确的 `acceptable_paths`（多个可接受路径），部分还有 `must_contain` 关键词约束，属于文档检索领域的标准做法。

#### ✅ Blind 测试机制
专门维护了 frozen 集和多个日期的 strict-blind 集，防止过拟合，确保评测结果可信。

#### ✅ 数据闭环机制
通过 `record_search_feedback.py` 和 `analyze_search_logs.py` 可将线上真实搜索反馈自动转化为候选评测用例，实现评测集的持续扩充。

#### ✅ 评测集健康检查
`validate_eval_set.py` 可自动检测失效路径（stale_path / missing_path）、弱 query、重复 query、must_contain 可能过严等问题，并区分阻塞级和非阻塞级问题。

#### ✅ 抽样策略科学
`sample_eval.py` 实现了按 category x card_type 分层抽样，确保子集代表性。

### 3.2 可改进之处

#### ⚠️ unknown 标注过多
- **category**: 无 unknown（已全部标注）
- **capability**: 371 条 unknown（34.4%）
- **query_style**: 371 条 unknown（34.4%）
- **difficulty**: 371 条 unknown（34.4%）

**影响**: 约 1/3 的数据无法按 capability、query_style、difficulty 维度分析，降低了多维评测的代表性。

**建议**: 补充标注这些维度，或在评测报告中明确说明 unknown 数据的影响。

#### ⚠️ 维度分布不均衡

**category 维度**:
- error-driven (26.8%) 和 how_to (25.9%) 占比过高
- natural (7.1%) 和 semi-structured (7.1%) 占比偏低

**capability 维度**:
- arkui_component (208 条) 占比过高
- 多个能力域只有个位数样本（telephony: 3, graphics: 2, hilog: 2, navigation: 1）

**影响**: 样本量过小的能力域评测结果统计意义有限。

**建议**: 对小样本能力域进行扩充，或在评测报告中注明置信度。

#### ⚠️ 评测集之间存在重复
合并前 1,297 条，去重后 1,077 条，说明有 **220 条重复**（17%）。

**影响**: 重复数据会放大某些 query 的权重，影响评测结果的客观性。

**建议**: 在评测流程中加入自动去重步骤。

#### ⚠️ 维护集和 Agent 集样本量极小
- `content-basic.jsonl`: 2 条
- `discovery.jsonl`: 2 条
- `goal_planning_cases.jsonl`: 8 条

**影响**: 统计意义有限，更像是冒烟测试而非严格评测。

**建议**: 扩充样本量至至少 30 条以上。

#### ⚠️ 缺乏端到端评测
当前评测体系聚焦于文档检索（信息检索层面），没有覆盖"拿到文档后能否正确编码实现"的端到端能力评测。

**建议**: 增加端到端评测维度，验证检索到的文档是否能有效指导编码。

#### ⚠️ Ground Truth 粒度问题
`acceptable_paths` 中多条路径被视为等价正确，但实际上有些路径比其他更精确（如具体 API 页 vs 概览页），未区分路径的精确度等级。

**建议**: 引入路径精确度权重，区分"完全匹配"、"相关匹配"、"模糊匹配"。

### 3.3 科学性评分

| 维度 | 评分 | 说明 |
|------|------|------|
| 多维度覆盖 | ⭐⭐⭐⭐⭐ | 5 个正交维度，支持细粒度分析 |
| Ground Truth 设计 | ⭐⭐⭐⭐ | 多路径 + must_contain，但缺乏精确度权重 |
| 样本量 | ⭐⭐⭐ | 总量充足，但部分维度分布不均 |
| 标注完整性 | ⭐⭐⭐ | unknown 占比过高（34.4%） |
| 防过拟合机制 | ⭐⭐⭐⭐⭐ | blind 集 + frozen 集 |
| 数据闭环 | ⭐⭐⭐⭐ | 有反馈采集和日志分析机制 |
| 健康检查 | ⭐⭐⭐⭐⭐ | 完整的校验工具链 |

**总体评分**: ⭐⭐⭐⭐ (4/5)

---

## 四、结论与建议

### 4.1 方案对比结论

| 维度 | OpenViking | V3 | 推荐 |
|------|------------|-----|------|
| **整体效果** | success@5 = 73.4% | success@5 = 80.2% | V3 |
| **任务型查询** | 77-81% | 100% | V3 |
| **错误排查** | 66.4% | 82.7% | V3 |
| **精确查询** | 75.6% | 53.3% | OpenViking |
| **自然语言** | 86.8% | 54.0% | OpenViking |
| **延迟稳定性** | p95 = 1231ms | p95 = 413ms | V3 |
| **部署复杂度** | 需要远端服务 | 本地运行 | V3 |

### 4.2 推荐策略

1. **生产环境**: 使用 **V3 方案**，覆盖大部分场景
2. **特定场景优化**: 针对 exact、natural、semi-structured 场景，可考虑引入 OpenViking 作为补充
3. **混合方案**: 实现智能路由，根据查询类型自动选择最优方案

### 4.3 评测集改进建议

1. **补充 unknown 标注**: 将 371 条 unknown 数据补充 capability、query_style、difficulty 标注
2. **均衡维度分布**: 扩充小样本能力域（telephony、graphics、hilog、navigation）
3. **引入精确度权重**: 区分不同路径的匹配精确度
4. **增加端到端评测**: 验证检索到的文档是否能有效指导编码
5. **自动去重**: 在评测流程中加入自动去重步骤
6. **扩充维护集和 Agent 集**: 样本量至少 30 条以上

---

## 五、附录

### 5.1 评测工具链

| 工具 | 路径 | 功能 |
|------|------|------|
| `ab_test_openviking_vs_v3.py` | scripts/ | AB 评测主脚本 |
| `run_multidim_ab_test.py` | scripts/ | 多维评测合并脚本 |
| `eval_bench.py` | scripts/ | 基础评测执行引擎 |
| `run_release_eval.py` | scripts/ | 发布评测流水线 |
| `validate_eval_set.py` | scripts/ | 评测集健康度校验 |
| `sample_eval.py` | scripts/ | 分层抽样工具 |
| `analyze_user_eval_failures.py` | scripts/ | 失败分析工具 |

### 5.2 评测结果文件

- **合并评测集**: `scripts/ab-results-multidim/eval_queries_merged.jsonl`
- **维度统计**: `scripts/ab-results-multidim/dimension_stats.json`
- **AB 测试结果**: `scripts/ab-results-multidim/summary.json`
- **详细对比**: `scripts/ab-results-multidim/diff.md`

### 5.3 发布门禁标准

| 评测集 | success@5 门禁 | error_rate 门禁 |
|--------|----------------|-----------------|
| eval_queries_user.jsonl | >= 0.98 | = 0 |
| eval_queries_app_agent_dev.jsonl | >= 0.98 | = 0 |
| eval_queries_user_appdev*.jsonl | >= 0.95 | = 0 |
| 严格 blind 集 | >= 0.80 | = 0 |

---

**报告生成时间**: 2026-04-29
**评测数据版本**: 20260429
**评测工具版本**: ab_test_openviking_vs_v3.py (latest)
