---
name: harmonyos-ui-inspect
description: "构建成功后，采集设备上的应用 UI 截图与控件树，分析界面状态并给出迭代建议。当需要验证构建产物的界面表现、排查 UI 缺陷、或评估是否需要进一步开发时使用此 Skill。"
---

# HarmonyOS UI 分析反馈 Skill

## 目的

在应用**构建成功**并安装到设备后，自动采集界面截图和控件树，**结合源码分析自动生成交互场景并执行真实验证**，分析 UI 状态，给出可操作的迭代建议。

## 前置条件

- 构建已通过（`BUILD SUCCESSFUL`）
- 设备已通过 USB 连接且 `hdc` 可用（`hdc list targets` 有输出），**或**本地模拟器已启动（DevEco Studio Emulator）
- 应用已安装或有可用的 `.hap` 文件

## 工作流程

### Step 0 — 确认设备连接与端口

```powershell
hdc list targets
```

输出示例：
```
127.0.0.1:5555        # 模拟器（取冒号后的数字作为 --emulator 参数）
0123456789ABCDEF      # USB 物理设备（无需 --emulator 参数）
```

- 如果输出含 `127.0.0.1:<port>`，记下端口号，后续 `--emulator <port>` 使用。
- 如果输出是设备 SN（无冒号），说明是 USB 物理设备，无需 `--emulator` 参数。
- 如果输出为空或 `Empty`，模拟器/设备未连接，请先启动。

### Step 1 — 采集 UI 状态

运行辅助脚本采集截图 + 控件树：

```powershell
# 在鸿蒙项目目录下运行（自动检测 bundle/ability）
cd <鸿蒙项目目录>
python "<skills_dir>/harmonyos-ui-inspect/ui_capture.py" --out ./ui_capture_output

# 本地模拟器
python "<skills_dir>/harmonyos-ui-inspect/ui_capture.py" --emulator 5555 --out ./ui_capture_output

# 手动指定项目目录（在任意位置运行）
python "<skills_dir>/harmonyos-ui-inspect/ui_capture.py" --project <项目路径> --out ./ui_capture_output

# 推荐：显式指定 --hap，确保设备上一定是最新安装包（避免“启动失败/采集到桌面”）
python "<skills_dir>/harmonyos-ui-inspect/ui_capture.py" --emulator 5555 \
  --hap "entry/build/default/outputs/default/entry-default-unsigned.hap" \
  --out ./ui_capture_output
```

#### 常见问题：未成功启动应用 / 采集到桌面（SceneBoard）

现象（满足任一即可判定）：

- `screenshot.png` 显示的是桌面/系统页面，而不是目标应用界面
- `layout.json` 里几乎找不到目标 `bundleName`（或过滤后窗口数为 0）
- 脚本输出显示已执行 `aa start`，但界面仍停留在桌面

优先按下面顺序处理（从最常见原因开始）：

1) 确认应用已安装到设备/模拟器

- 直接用脚本安装（推荐）：运行时加 `--hap <path-to-hap>`
- 或手动安装：

```powershell
hdc -t 127.0.0.1:5555 install -r "entry/build/default/outputs/default/entry-default-unsigned.hap"
```

2) 再次显式启动目标 Ability（避免启动到其他窗口）

```powershell
hdc -t 127.0.0.1:5555 shell aa start -b <bundleName> -a <abilityName>
```

3) 检查项目是否错误配置为“桌面/home”能力

- 如果 `entry/src/main/module.json5` 的 `EntryAbility.skills` 包含 `entity.system.home` / `action.system.home`，设备可能会把应用当桌面启动，导致采集一直抓到桌面。
- 解决：移除上述 home skill 后重新构建、重新安装 hap。

4) 用控件树快速自检是否抓到了目标应用

- 看 `layout.json` 中是否出现 `bundleName: <你的包名>`
- 或看脚本输出：过滤后窗口数应为 >= 1（示例：`已过滤控件树，仅保留 <bundle> 的 1 个窗口`）

**参数说明：**

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--project` | 自动向上搜索 | 鸿蒙项目目录（含 `AppScope/`），脚本从中读取 bundle/ability |
| `--bundle` | 自动检测 | 应用包名（从 `AppScope/app.json5` 读取） |
| `--ability` | 自动检测 | 启动 Ability（从 `entry/src/main/module.json5` 读取） |
| `--hap` | 无 | 指定 hap 路径则自动安装 |
| `--no-launch` | 否 | 应用已在前台时跳过启动 |
| `--wait` | `3` | 启动后等待加载秒数 |
| `--emulator` | 无 | 模拟器端口或地址（如 `5555` 或 `127.0.0.1:5555`），自动执行 `hdc tconn` |
| `--scenario` | 无 | 交互场景配置 JSON 文件路径，指定后自动执行交互→二次采集→差异报告 |

> 如脚本不可用，可手动执行等价 hdc 命令：
> ```powershell
> hdc shell aa start -a EntryAbility -b com.example.openvk330
> Start-Sleep 3
> hdc shell snapshot_display -f /data/local/tmp/screen.png
> hdc file recv /data/local/tmp/screen.png ./screenshot.png
> hdc shell uitest dumpLayout -p /data/local/tmp/layout.json
> hdc file recv /data/local/tmp/layout.json ./layout.json
> ```

### Step 2 — 读取采集结果（截图 + 控件树双验证）

依次读取 `ui_capture_output/` 下的三个文件：

1. **`screenshot.png`** — 截图提供**视觉表现**：颜色、布局、留白、文字渲染效果
2. **`layout.json`** — 控件树提供**结构事实**：控件是否存在、属性值、层级关系
3. **`ui_summary.md`** — 结构化摘要：类型分布、尺寸间距量化数据、可交互统计

> **双验证原则**：每个结论必须同时有截图和控件树的证据支撑。两者矛盾时以控件树为准（截图可能有渲染延迟）。

### Step 2.5 — 自动生成交互场景（源码 + 控件树驱动）

基于 Step 2 的采集结果和项目源码，**自动生成**交互场景 JSON。此步骤是 AI 的核心推理环节，不依赖外部模板文件。

#### 2.5.1 扫描源码交互绑定

在 `entry/src/` 下搜索 `.cj` 源文件，提取事件绑定与状态变量：

| 源码模式 | 含义 | 生成的场景动作 |
|----------|------|---------------|
| `.onClick(...)` | 点击事件 | `click` |
| `.onLongPress(...)` | 长按事件 | `long_click` |
| `.onChange(...)` / `.onTextChange(...)` | 值变化 | `input` + 断言 `text_changed` |
| `.onSwipe(...)` / `Scroll` / `List`+`ForEach` | 滑动 | `swipe` / `fling` |
| `Navigator` / `router.push` / `pushUrl` | 页面跳转 | `click` + 断言 `page_changed` |
| `@State var xxx` | 状态变量 | 追踪绑定的 UI 控件作为断言目标 |

**关键**：事件回调中修改了哪些 `@State` 变量 → 这些变量绑定的 UI 控件 = 断言检查目标。

#### 2.5.2 分析控件树可交互节点

从 `layout.json` 提取：

- `clickable: true` → 候选点击目标
- `scrollable: true` → 候选滑动目标
- TextInput 类型 → 候选输入目标
- 记录每个控件的 `key`、`text`、`type`、`bounds`

#### 2.5.3 交叉匹配与场景组装

1. **匹配**：源码事件绑定 → 控件树找到对应节点且交互属性为 true → 确认可测试
2. **定位优先级**：`key` > `text` > `type+index` > 坐标
3. **步骤编排**：按业务流程自然顺序；关键状态转换处插 `snapshot`；操作间插 `wait`（点击 0.5-1s，跳转 2-3s）
4. **断言设计**：`@State` 变化 → `text_changed`/`text_equals`；跳转 → `page_changed`+`exists`；出现/消失 → `exists`/`not_exists`
5. **避坑**：操作回到初始状态（A→B→A）时用中间 `snapshot` 验证，而非首尾 `page_changed`

#### 2.5.4 输出场景文件

在项目目录下生成 `auto_scenario.json`：

- 覆盖核心业务路径，忽略纯装饰控件
- 一个场景聚焦一个流程，复杂应用拆多文件
- `name`/`description` 准确描述测试意图

### Step 3 — 执行交互验证

将 Step 2.5 生成的场景传入 `--scenario` 执行：

```powershell
python "<skills_dir>/harmonyos-ui-inspect/ui_capture.py" \
  --emulator 5555 --scenario ./auto_scenario.json --out ./ui_capture_output
```

**场景 JSON 格式**（支持 `//` 注释）：

```json
{
  "name": "计数器点击测试",
  "description": "验证点击按钮后计数器是否正确递增",
  "steps": [
    {"action": "click", "target": {"text": "点击计数"}},
    {"action": "wait", "seconds": 1},
    {"action": "click", "target": {"text": "点击计数"}},
    {"action": "click", "target": {"text": "点击计数"}}
  ],
  "assertions": [
    {"type": "text_equals", "target": {"key": "counter_display"}, "expected": "3", "message": "点击3次后计数器应为3"},
    {"type": "page_changed", "message": "界面应有变化"}
  ]
}
```

**支持的交互动作 (`steps[].action`)**：

| 动作 | 参数 | 说明 |
|------|------|------|
| `click` | `target` | 模拟单击（自动在控件树中定位目标中心点） |
| `double_click` | `target` | 模拟双击 |
| `long_click` | `target`, `duration`(ms) | 模拟长按 |
| `input` | `target`, `text` | 点击目标输入框后输入文本 |
| `swipe` | `direction`(up/down/left/right) 或 `from`+`to` | 模拟滑动手势 |
| `fling` | `direction` 或 `from`+`to`, `stepLen`, `speed` | 模拟快速滑动 |
| `back` | 无 | 模拟返回键 |
| `home` | 无 | 模拟 Home 键 |
| `wait` | `seconds` | 等待指定秒数 |
| `snapshot` | `label` | 在中间步骤额外采集一次截图+控件树 |

**目标定位 (`target`) 方式**（按优先级）：

| 方式 | 示例 | 说明 |
|------|------|------|
| 坐标 | `{"x": 540, "y": 1200}` | 直接指定屏幕坐标 |
| key | `{"key": "btn_submit"}` | 精确匹配控件 key 属性 |
| text | `{"text": "提交"}` | 精确匹配或包含匹配 text |
| type+index | `{"type": "Button", "index": 0}` | 按类型+序号定位（默认第0个） |
| hint | `{"hint": "请输入用户名"}` | 匹配 hint 文本 |

**支持的断言 (`assertions[].type`)**：

| 类型 | 参数 | 说明 |
|------|------|------|
| `exists` | `target` | 交互后目标控件应存在 |
| `not_exists` | `target` | 交互后目标控件应消失 |
| `text_changed` | `target` | 目标控件 text 应与交互前不同 |
| `text_equals` | `target`, `expected` | 目标控件 text 应等于指定值 |
| `clickable` | `target`, `expected`(bool) | 目标控件 clickable 状态 |
| `count_changed` | `target`(需含 type) | 指定类型控件数量应变化 |
| `page_changed` | 无 | 界面整体应有变化 |

每个断言可附带 `message` 描述预期行为。

**执行流程**：
1. 基线采集（截图+控件树） → `ui_capture_output/screenshot.png` + `layout.json`
2. 逐步执行交互（每步前重新 dump 控件树以精确定位）
3. 交互后二次采集 → `ui_capture_output/after/screenshot.png` + `layout.json`
4. 差异对比 → `ui_capture_output/diff.json`（新增/删除/属性变化/文本变化/数量变化）
5. 断言检查 → 逐条评估通过/失败
6. 生成报告 → `ui_capture_output/interaction_report.md`

**读取结果**（按顺序）：

1. `screenshot.png` — 交互前基线
2. `after/screenshot.png` — 交互后截图
3. `interaction_report.md` — 步骤执行 + 差异摘要 + 断言结果
4. `diff.json` — 结构化差异数据
5. `snapshot_<label>/` — 中间快照（如有）

### Step 4 — 分析与诊断

基于采集数据，从以下维度逐项检查：

**🔍 控件完整性**
- 页面是否加载成功（非白屏/空页面）
- 关键控件是否存在（对照源码中的 UI 组件）
- 文本内容是否正确渲染（非空、非占位符）

**🎯 交互可用性**
- 按钮/输入框是否可点击（`clickable: true`）
- 列表是否可滚动（`scrollable: true`）
- 控件是否有 `key` 标识（利于自动化测试定位）
- **[交互验证]** 若提供了 `--scenario`，检查 `interaction_report.md` 中的断言结果，确认交互是否真正生效

**📐 布局合理性**
- 重叠、溢出、截断检查
- 控件层级深度 > 10 需关注
- 大片留白（>1/4 屏幕高度无内容区域），结合 `ui_summary.md` 间距分析定位

**🎨 视觉审美**（基于 `ui_summary.md` + 截图）
- 字体层次：正文 ≥14fp、标题 ≥18fp，信息层级分明
- 间距一致：同级元素间距差异不超 2 倍
- 控件尺寸：可点击 ≥48×48vp，同类尺寸一致
- 颜色语义：同状态同颜色，不同状态颜色不混淆

**⚡ 数据与业务逻辑**
- 列表非空态；状态变量正确反映
- 源码有 onClick 则控件应 `clickable: true`；有导航则控件可交互
- 控件树文本/数值与源码初始状态一致
- **[交互验证]** `diff.json` 变化与源码预期一致；断言失败 = 高优先级问题

### Step 5 — 输出迭代建议

按以下格式输出分析结论：

```markdown
## UI 反馈分析报告

### 当前状态
<一句话描述界面当前表现>

### 交互验证结果（如有）
**断言通过率**: X/Y
- ✅ <通过的断言>
- ❌ <失败的断言> → 原因 + 修复建议

### 发现的问题
1. [严重程度: 高/中/低] <问题描述> → 建议修复方式
2. ...

### 迭代建议
- [ ] <具体可执行的开发任务>
- [ ] ...

### 无需改动
<确认正常的部分，避免过度修改>
```

## 核心原则

1. **双验证**：截图 + 控件树双重证据，矛盾时以控件树为准
2. **只基于数据**：控件树中没有的信息不下结论
3. **聚焦可操作项**：只输出有明确修复方向的问题
4. **不过度设计**：界面正常则明确说“无需改动”
5. **源码驱动场景**：交互场景从源码事件绑定 + 控件树可交互节点交叉分析得出，不凭空猜测
6. **真实交互优先**：优先用 `--scenario` 真实操作验证，而非仅凭静态属性推测
7. **可重复验证**：场景 JSON 可版本化、可复用，支持回归验证
