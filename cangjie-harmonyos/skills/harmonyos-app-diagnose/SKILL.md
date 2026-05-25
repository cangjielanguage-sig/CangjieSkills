---
name: harmonyos-app-diagnose
description: "构建成功后，采集设备上的应用 UI 截图与控件树，抓取 hilog 运行日志，分析界面状态与运行时异常并给出迭代建议。当需要验证构建产物的界面表现、排查 UI 缺陷、诊断应用崩溃/ANR/运行时错误、或评估是否需要进一步开发时使用此 Skill。"
---

# HarmonyOS 应用运行诊断 Skill

## 目的

构建成功后，通过 UI 采集（截图 + 控件树）、hilog 日志抓取、源码驱动的交互验证，输出可落地的诊断与迭代建议。

## 适用场景

- 验证界面表现、排查 UI 缺陷或交互问题
- 应用崩溃（Crash）、白屏、闪退、ANR
- 抓取运行日志定位业务逻辑错误或异常堆栈

## 前置条件

- 构建已通过（`BUILD SUCCESSFUL`）
- `hdc list targets` 有可用设备（模拟器或真机）
- 应用已安装，或有 `.hap` 文件

## 诊断流程

### 步骤 1：确认设备连接

```powershell
hdc list targets
```

- 输出含 `127.0.0.1:<port>` → 模拟器，后续传 `--emulator <port>`
- 输出为设备 SN → USB 设备，不传 `--emulator`
- 输出为空 → 先启动模拟器或连接设备

### 步骤 2：采集 UI 状态

```powershell
cd <鸿蒙项目目录>

# 推荐：指定 --hap 确保安装最新包
python "<skills_dir>/harmonyos-app-diagnose/ui_capture.py" --emulator 5555 \
  --hap "entry/build/default/outputs/default/entry-default-unsigned.hap" \
  --out ./ui_capture_output
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--project` | 自动向上搜索 | 鸿蒙项目目录（含 `AppScope/`） |
| `--bundle` | 自动检测 | 应用包名 |
| `--ability` | 自动检测 | 启动 Ability |
| `--hap` | 无 | 指定后自动安装 |
| `--no-launch` | 否 | 应用已在前台时跳过启动 |
| `--wait` | `3` | 启动后等待秒数 |
| `--emulator` | 无 | 模拟器端口（如 `5555`），自动 `hdc tconn` |
| `--scenario` | 无 | 场景 JSON，执行交互后二次采集 |

脚本不可用时手动采集：

```powershell
hdc shell aa start -a EntryAbility -b <bundleName>
Start-Sleep 3
hdc shell snapshot_display -f /data/local/tmp/screen.png
hdc file recv /data/local/tmp/screen.png ./screenshot.png
hdc shell uitest dumpLayout -p /data/local/tmp/layout.json
hdc file recv /data/local/tmp/layout.json ./layout.json
```

采集产物（`ui_capture_output/`）：
- `screenshot.png` — 视觉表现
- `layout.json` — 控件树（结构事实）
- `ui_summary.md` — 统计摘要

### 步骤 3：自动生成并执行交互场景

扫描 `entry/src/` 的 `.cj` 文件，与控件树交叉匹配，生成 `auto_scenario.json`：

| 源码模式 | 场景动作 |
|----------|----------|
| `.onClick(...)` | `click` |
| `.onLongPress(...)` | `long_click` |
| `.onChange(...)` / `.onTextChange(...)` | `input` + `text_changed` |
| `.onSwipe(...)` / `Scroll` / `List` + `ForEach` | `swipe` / `fling` |
| `Navigator` / `router.push` / `pushUrl` | `click` + `page_changed` |
| `@State var xxx` | 找到绑定 UI 作为断言目标 |

生成规则：
- 定位优先级：`key` > `text` > `type+index` > 坐标
- 操作间插入 `wait`（点击 0.5-1s，跳转 2-3s），关键转换点插 `snapshot`
- 追踪回调修改的 `@State`，将绑定控件作为断言目标

执行：

```powershell
python "<skills_dir>/harmonyos-app-diagnose/ui_capture.py" \
  --emulator 5555 --scenario ./auto_scenario.json --out ./ui_capture_output
```

**场景 JSON 示例**：

```json
{
  "name": "计数器点击测试",
  "steps": [
    {"action": "click", "target": {"text": "点击计数"}},
    {"action": "wait", "seconds": 1},
    {"action": "click", "target": {"text": "点击计数"}}
  ],
  "assertions": [
    {"type": "text_equals", "target": {"key": "counter_display"}, "expected": "2"},
    {"type": "page_changed", "message": "界面应有变化"}
  ]
}
```

**支持的动作**：`click`、`double_click`、`long_click`（`duration` ms）、`input`（`text`）、`swipe`/`fling`（`direction` 或 `from`+`to`）、`back`、`home`、`wait`（`seconds`）、`snapshot`（`label`）

**目标定位**：坐标 `{x,y}` > `key` > `text` > `type+index` > `hint`

**支持的断言**：`exists`、`not_exists`、`text_changed`、`text_equals`（`expected`）、`clickable`（`expected`）、`count_changed`（`type`）、`page_changed`

**执行产物**：
- `ui_capture_output/screenshot.png` + `layout.json` — 基线
- `ui_capture_output/after/screenshot.png` + `layout.json` — 交互后
- `ui_capture_output/diff.json` — 差异数据
- `ui_capture_output/interaction_report.md` — 执行报告
- `ui_capture_output/snapshot_<label>/` — 中间快照

### 步骤 4：hilog 日志采集

以下情况**必须**采集日志：崩溃/闪退/白屏/ANR、断言失败、截图异常但控件树正常、业务逻辑不符预期。

**推荐采集流程**：

```powershell
hdc shell hilog -r                                          # 1. 清空旧日志
hdc shell aa start -a <abilityName> -b <bundleName>         # 2. 启动应用
Start-Sleep 5                                                # 3. 等待/复现
hdc shell hilog -x > ./ui_capture_output/hilog_full.txt     # 4. 导出全量日志
hdc shell "hilog -L E" > ./ui_capture_output/hilog_error.txt # 5. 提取错误
```

**常用过滤**：

```powershell
# 按包名过滤
hdc shell hilog | Select-String "<bundleName>" > ./hilog_app.txt
# 按标签过滤（AceAbility / JsApp / ArkCompiler）
hdc shell "hilog -T AceAbility" > ./hilog_ace.txt
# 按级别：-L E（ERROR+FATAL）、-L F（仅FATAL）、-L W（WARN及以上）
```

**崩溃模式速查表**：

| 关键词 | 含义 | 排查方向 |
|--------|------|----------|
| `Signal:11(SIGSEGV)` / `Signal:6(SIGABRT)` | 原生崩溃 | 堆栈函数名→源码行 |
| `Cannot read property` / `is not callable` | ArkTS 运行时错误 | 错误消息 + 调用栈 |
| `NullPointerException` / `nullptr` | 空引用 | 变量初始化时序、生命周期 |
| `ANR` / `Application Not Responding` | 主线程阻塞 | 耗时操作异步化 |
| `OutOfMemoryError` / `OOM` | 内存溢出 | 大图 / 缓存泄漏 / 循环引用 |
| `Permission denied` | 权限不足 | `module.json5` 添加 `requestPermissions` |
| `module is not installed` | 未安装 | 重装 hap、确认包名 |
| `Ability not found` | Ability 解析失败 | `module.json5` abilities 配置 |
| `libark_jsruntime` / `ark_` 崩溃 | ArkCompiler 层 | 互操作类型不匹配 / FFI |

**日志分析原则**：
1. 先 FATAL/ERROR 后 WARN，优先致命问题
2. 关注崩溃前 0.5-2 秒日志（往往含根因）
3. 堆栈截断时用 `hilog -G 2M` 增大缓冲区重采
4. 建议清空→操作→采集至少 2 次确认
5. 日志 + 控件树 + 截图交叉验证

### 步骤 5：分析与诊断

按以下维度输出结论：

| 维度 | 关注点 |
|------|--------|
| 控件完整性 | 是否白屏、关键控件是否存在、文本是否有效 |
| 交互可用性 | `clickable`/`scrollable` 状态、断言是否通过 |
| 布局合理性 | 重叠/溢出/截断、层级深度 >10、大片留白 >1/4 屏高 |
| 视觉审美 | 正文 >=14fp、标题 >=18fp、可点击尺寸 >=48x48vp |
| 运行时健康 | hilog ERROR/FATAL、崩溃堆栈→源码位置、权限/资源错误 |
| 数据与业务 | 状态变量与 UI 一致性、`diff.json` 是否符合预期、日志业务异常 |

### 步骤 6：输出诊断报告

```markdown
## 应用运行诊断报告

### 当前状态
<一句话概述界面表现和运行健康度>

### 运行日志摘要（如有）
- 级别分布: FATAL: X, ERROR: Y, WARN: Z
- 关键发现: <崩溃/错误摘要及源码位置>

### 交互验证结果（如有）
断言通过率: X/Y
- ✅ / ❌ <断言描述> → 修复建议

### 发现的问题
1. [高/中/低] <描述> → 修复方式

### 迭代建议
- [ ] <具体开发任务>

### 无需改动
<确认正常的部分>
```

## 常见问题排查

截图是桌面 / 控件树无目标 bundleName / `aa start` 后仍在桌面：

1. 确认已安装（传 `--hap` 或 `hdc install -r`）
2. 显式启动：`hdc shell aa start -b <bundleName> -a <abilityName>`
3. 检查 `module.json5` 中 skills 是否误含 `entity.system.home`
4. 控件树确认目标 `bundleName` 出现且过滤后窗口数 >= 1

## 核心原则

1. **三重验证**：截图 + 控件树 + hilog，冲突时以控件树和日志为准
2. **只基于数据**：控件树和日志中没有的信息不下结论
3. **崩溃优先**：FATAL/ERROR 优先于 UI 细节
4. **聚焦可执行**：每个问题给出明确修复方向
5. **源码驱动场景**：事件绑定与可交互节点交叉得出，不凭空猜测
6. **不过度设计**：正常且无异常时标注"无需改动"
