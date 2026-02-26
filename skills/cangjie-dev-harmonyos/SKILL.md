---
name: cangjie-dev-harmonyos
description: HarmonyOS Next Cangjie development assistant with intelligent 3-tier knowledge retrieval (L0 Requirements Analysis -> L1 RAG Query -> L3 Local Docs Search). Use when developing HarmonyOS applications in Cangjie language, including UI development, API queries, syntax questions, and build troubleshooting.
argument-hint: query or build for project building
disable-model-invocation: false
---

# Project Context
这是一个基于 **HarmonyOS Next** 的应用，使用 **仓颉 (Cangjie)** 语言开发。
你的目标是像一个高级工程师一样，通过精准查阅相关知识和文档来辅助开发。

```
由于你的训练数据缺乏最新的仓颉语法，遇到任何不确定的 API 或语法细节，严禁猜测。
鸿蒙应用开发过程你必须严格按照以下 “需求分析L0 -> L1 -> L3” 的顺序获取知识。
```

## 📝 重要提示：脚本路径

**L1 RAG 查询脚本**（位于 `.claude/skills/cangjie-dev-harmonyos/scripts/`）：
- `ask_cangjie.py` - L1 阶段使用的 RAG 查询脚本（带自动初始化功能）
- `cangjie_retriever.py` - 混合检索器（向量 + BM25）
- `Database-Builder.py` - RAG 数据库构建脚本

**项目构建脚本**：
- `build.ps1` - 项目构建脚本，位于 `.claude/skills/cangjie-dev-harmonyos/scripts/`（已与你的环境同步）

# 执行方式：
## 进入 scripts 目录（技能独立运行）
cd .claude\\skills\\cangjie-dev-harmonyos\\scripts

## 🚀 自动初始化（首次使用时推荐）
python ask_cangjie.py "任意查询"
### 首次运行会自动：
1. 检测文件夹 (hm-docs/, chroma_db/) 是否存在
2. 如果不存在，检测压缩包 (hm-docs.zip, chroma_db.zip)
3. 如果有压缩包，自动解压到 scripts/ 目录
4. 如果都没有，则下载官方文档并构建数据库
5. 执行查询

### 手动初始化（可选）
python Database-Builder.py  # 仅构建数据库
python download_hm_docs.py   # 仅下载文档

## L1 查询
python ask_cangjie.py "List"

## 构建项目（先复制到项目根目录再执行脚本构建）
.\\build.ps1

# 具体流程：
## 🔍 Phase 0: 需求技术化分析 (L0 - Requirement Analysis)

**目的**: 将用户的业务需求转换为具体的技术实现点，避免无效检索。
**原则**: 不要直接搜索业务词汇，要分析背后需要的技术组件。

### 📋 需求分析模板

对于任何开发需求，先进行以下分析：

```python
REQUIREMENT_ANALYSIS = {
    "用户需求": "用户的原始描述",
    "界面分析": "需要什么UI组件？(列表、按钮、输入框、图片等)",
    "数据分析": "需要什么数据结构？(数组、对象、状态管理等)",
    "交互分析": "需要什么用户交互？(点击、滑动、输入等)"
}
```

### 🔧 技术关键词细化策略

**识别核心API组件**：
- 提取需要使用的具体技术组件名称
- 使用英文API名称作为查询关键词
- 一个关键词可以匹配到该组件所有相关内容

**细化示例**：
```python
# 原始需求: "创建登录页面"
# 界面分析: 输入框、登录按钮、垂直布局
# 细化后关键词:
["Button", "TextInput", "Column"]
```

**参见示例**: [examples/l0-analysis.md](examples/l0-analysis.md)

> **🛑 L0 评估**:

> - ✅ 已分析出具体技术组件 -> **进入 L1 检索这些组件**

> - ❌ 需求太模糊无法分析 -> **向用户询问更多细节**

## 🟢 Phase 1: 快速精准检索 (L1 - RAG)

**目的**: 获取最常用的代码片段和概念。
**操作**: 根据L0分析出的核心API名称，分别进行精准查询。
**策略**: 使用纯英文API名称，让BM25关键词匹配发挥最大效果。

### 📋 L1 查询策略

**基于L0分析出的核心API名称进行查询**：

> **⚠️ 初始化检查（必须先执行）**：
>
> 在执行查询前，必须先检查 `scripts/hm-docs/` 和 `scripts/chroma_db/` 目录是否存在。
>
> - **目录存在** → 直接执行查询
> - **目录不存在** → **必须先提示用户，再执行初始化**
>
> **⚠️ 用户提示说明（必须执行）**：
>
> 当检测到需要初始化（文档和数据库不存在）时，必须先明确告知用户：
>
> ```
> ⚙️ 正在自动拉取文档和自动构建向量数据库，稍等1-2分钟...
> ```
>
> **执行顺序**：
> 1. 提示用户初始化中
> 2. 执行初始化
> 3. 等待初始化完成
> 4. 初始化完成后执行 L1 查询

> **⚠️ 脚本路径提醒**: 技能内所有脚本位于 `scripts/` 目录，可直接调用
>
> **调用方式**：
>
> ```bash
> cd .claude/skills/cangjie-dev-harmonyos/scripts
> python ask_cangjie.py "Button"
> ```
>
> 脚本会自动检测并处理初始化（文件夹/压缩包/下载）。

- **纯英文关键词**: 直接使用英文API名称（如 "Button"），不添加中文后缀
- **单词精准**: 一个关键词（如 "Button"）可匹配该组件的所有相关信息
- **适度数量**: 控制在3-5个核心组件
- **结果展示**: **必须将L1查询结果贴出来供用户查看**，不要隐藏查询过程

> **🛑 评估 (Self-Reflection)**:

> - 是否获得了足够的核心组件API？

> - **是** -> 停止检索，开始编码

> - **否/不相关** -> **进入 Phase 3 (本地文档搜索)**

## 🏠 Phase 2: 本地官方文档搜索 (L3 - Local Docs)

**目的**: 当 L1 失效时，直接搜索本地下载的官方文档。
**优势**: 无需网络，包含最权威的官方信息和完整代码示例。
**适用场景**: 所有类型的问题，特别是UI开发、API参考、语法说明。


### 🔍 快速定位策略

#### 1. UI组件问题 (最常用)
- **Button组件**: 直接查看 `@./hm-docs/ui-dev/arkui-cj/cj-common-components-button.md`
- **List列表**: 直接查看 `@./hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md`
- **Text文本**: 直接查看 `@./hm-docs/ui-dev/arkui-cj/cj-common-components-text-display.md`
- **布局问题**: 查看 `@./hm-docs/ui-dev/arkui-cj/cj-layout-development-*.md`

#### 2. API参考查询
- **组件API**: 查看 `@./hm-docs/ui-dev/reference/arkui-cj/` 目录
- **标准库API**: 查看 `@./hm-docs/stdlib/std/` 目录

#### 3. 语法和语言特性
- **语法问题**: 查看 `@./hm-docs/syntax/source_zh_cn/` 目录
- **高级功能**: 查看 `@./hm-docs/stdx/libs_stdx/` 目录

#### 4. 构建错误排查
**当构建失败时，根据错误类型搜索解决方案**：
- **导入错误** (`import error`): 搜索 `@./hm-docs/ui-dev/arkui-cj/` 中的导入示例
- **未定义符号** (`undefined symbol`): 搜索 `@./hm-docs/ui-dev/reference/` 中的API定义
- **语法错误** (`syntax error`): 搜索 `@./hm-docs/syntax/source_zh_cn/` 中的语法说明
- **权限错误** (`permission denied`): 搜索 `module.json5` 和权限配置相关文档

#### 📌 L1→L3 路径映射快捷方式

**利用 L1 输出的本地路径优先快速定位文档**：

L1 查询结果会返回格式化的知识片段，其中包含 `[本地路径]` 字段。

**L1→L3 配合原则**：
- **优先**: 使用 L1 返回的路径快速定位到可能相关的文档
- **补充**: 如果单个文档信息不足或需要更多上下文，扩展到正常的 L3 搜索
- **判断**: 当 L1 结果只有概念描述而缺少具体实现细节，或遇到边界情况时触发扩展搜索

**路径映射表**：
| RAG_Lite 源路径 | 映射后的本地路径 |
|----------------|-----------------|
| `zh-cn/application-dev/` | `./hm-docs/ui-dev/` |
| `docs/dev-guide/` | `./hm-docs/syntax/source_zh_cn/` |
| `std/doc/` | `./hm-docs/stdlib/std/` |
| `doc/` | `./hm-docs/stdx/libs_stdx/` |

### 🔍 搜索命令示例 (PowerShell)

```powershell
# 搜索Button相关内容
Select-String -Path "./hm-docs\\ui-dev\\arkui-cj\\*.md" -Pattern "Button" -Context 1

# 搜索List相关内容
Get-ChildItem -Path "./hm-docs\\ui-dev\\arkui-cj" -Filter "*.md" -Recurse | Select-String -Pattern "List" -Context 2

# 搜索Image图片组件
Select-String -Path "./hm-docs\\ui-dev\\reference\\arkui-cj\\cj-image-video-image.md" -Pattern "导入|import|@r" -Context 1

# 搜索特定API (递归搜索所有子目录)
Get-ChildItem -Path "./hm-docs\\ui-dev" -Filter "*.md" -Recurse | Select-String -Pattern "onClick" -Context 1

# 快速查找包含关键词的文件
Get-ChildItem -Path "./hm-docs\\ui-dev\\arkui-cj" -Filter "*.md" -Recurse | Select-String -Pattern "Button" -List

# 构建错误排查示例
# 当出现导入错误时
Get-ChildItem -Path "./hm-docs\\ui-dev" -Filter "*.md" -Recurse | Select-String -Pattern "import.*ArkUI" -Context 1

# 当出现权限错误时
Get-ChildItem -Path "./hm-docs\\ui-dev" -Filter "*.md" -Recurse | Select-String -Pattern "permission|module.json5" -Context 2

# 搜索JSON处理相关
Select-String -Path "./hm-docs\\stdx\\libs_stdx\\encoding\\json\\*.md" -Pattern "JsonValue|parse|stringify" -Context 1

# 搜索并发编程相关
Get-ChildItem -Path "./hm-docs\\syntax\\source_zh_cn\\concurrency" -Filter "*.md" -Recurse | Select-String -Pattern "spawn|线程|并发" -Context 2
```

参见示例: [examples/l3-search.md](examples/l3-search.md)

> **🛑 Phase 2 评估**:

> - ✅ 在本地文档中找到相关信息 -> 基于本地官方文档编码

> - ❌ 本地文档中无相关信息 -> **明确告知"该功能可能不支持或文档未包含"，请求用户提供相关知识或文档**

## ✅ 项目构建指南

> **⚠️ 脚本路径提醒**: 构建脚本位于 `.claude/skills/cangjie-dev-harmonyos/scripts/build.ps1`（已与你的环境同步）

### 🛠️ 构建命令

**方式 1 - 在项目根目录执行**（推荐，先复制到项目根目录再执行脚本构建）：
```powershell
.\\build.ps1
```

### 📦 构建流程说明

`build.ps1` 脚本会自动执行以下步骤：
1. **install** - 安装依赖
2. **CangjiePreBuild** - 仓颉预编译
3. **GenerateCangjieResource** - 生成资源
4. **CompileCangjie** - 编译仓颉代码
5. **CompileArkTS** - 编译 ArkTS
6. **PackageHap** - 打包 HAP
7. **SignHap** - 签名（未配置时跳过）
8. **assembleHap** - 组装最终 HAP

### 🚨 构建失败处理

**关键原则**: 获得足够详细的错误信息是解决问题的前提。

#### 📋 第一步：获取完整的 build.ps1 输出

**⚠️ 强制要求**：在分析报错信息之前，必须先确保已获得完整的构建输出。

**执行流程**：
1. **捕获完整输出**：使用 Bash 工具执行 `build.ps1` 时，设置足够的 `timeout`（建议 300000ms）
2. **检测输出截断**：检查输出中是否包含 `Output too large` 或 `Full output saved to:` 提示
3. **读取完整输出文件**：如果存在输出截断提示，**必须**使用 Read 工具读取完整的输出文件
4. **分析完整报错**：基于完整的输出内容进行下一步分析

**示例执行模式**：
```powershell
# 方式 1: 直接执行（输出较小）
Bash(command: "powershell -ExecutionPolicy Bypass -File '.\\.claude\\skills\\cangjie-dev-harmonyos\\scripts\\build.ps1'",
      timeout: 300000)

# 方式 2: 输出包含截断提示时，必须读取完整文件
# 如果输出中有: "Full output saved to: C:\\Users\\xxx\\tool-results\\xxx.txt"
Read(file_path: "C:\\Users\\xxx\\tool-results\\xxx.txt")
```

**原则**: 只有在获得完整 build.ps1 输出后，才能进入下一步分析。

#### 📋 第二步：评估报错信息充足性

在获得完整输出后，评估报错信息是否足够详细：

**❌ 报错信息不足的情况**（需要主动询问）：
- 只有简单的 "BUILD FAILED" 或 "error occurred"
- 缺少具体的错误行号和错误类型
- 缺少代码上下文（代码片段）
- 缺少宏展开后的错误信息（常见于 ArkUI 组件问题）

**✅ 报错信息充足的情况**：
- 包含完整的错误类型（如 `undefined identifier`、`invalid binary operator`）
- 或者包含具体的文件路径和行号
- 或者包含出错的代码片段
- 或者包含宏展开后的代码（问题跟踪时）

#### 🔧 当报错信息不足时的处理

**⚠️ 重要前提**: 只有在已完整读取 build.ps1 输出（包括截断文件）后，仍然发现信息不详细时，才建议使用 DevEco Studio。

**主动要求用户提供完整报错**：
```
已获取 build.ps1 的完整构建输出，但错误信息仍然不够详细，无法准确定位问题。

请在 DevEco Studio 中重新构建项目，然后将完整的错误信息复制给我。
DevEco Studio 会提供更详细的报错，包括：
- 具体的错误类型和描述
- 出错的代码位置（文件:行号）
- 宏展开后的代码（对于 ArkUI 组件问题）
- 相关的类型信息

请在 DevEco Studio 中构建后将完整报错贴出来。
```

#### 🔍 当获得足够报错信息时的处理

**严格按照以下优先级处理**：

```
获得详细报错信息
    ↓
Step 1: 检查 Evolution.md (优先级最高)
    ↓
    ├─ 找到相同问题 → 应用已验证的解决方案 → 重新构建
    │
    └─ 未找到/无法解决 → 继续 Step 2
         ↓
Step 2: L3 本地文档搜索
    ↓
    ├─ 找到解决方案 → 修复代码 → 重新构建 → 构建成功则更新 Evolution.md
    │
    │                             ↓
    │                        构建失败则重新判断报错信息是否充足，重新修正方案
    │
    └─ 未找到 → 明确告知"该功能可能不支持"
```

**Step 1 - 检查 Evolution.md 的执行要点**：
1. 读取 `Evolution.md` 文件
2. 搜索报错中的关键词（如错误类型、相关API名称）
3. 对比错误描述是否匹配
4. 如果匹配，直接应用已记录的解决方案
5. **不要再进行 L3 搜索**，直接修复

**Step 2 - L3 搜索的执行要点**：
1. 仅在 Evolution.md 中找不到相关问题后才进行
2. 根据错误类型选择合适的搜索路径
3. 修复代码并重新构建
4. **只有在构建成功后，才将新问题添加到 Evolution.md**
5. 如果构建失败，说明方案错误，不能记录，需要重新根据报错信息寻找解决方案

**示例**：
```
用户报错: error: undeclared identifier 'toUInt32'
↓
Step 1: 检查 Evolution.md
    ✓ 搜索关键词: "toUInt32", "类型转换", "未定义标识符"
    ✓ 找到记录 #14: 类型转换方法不存在
    ✓ 解决方案: 使用 UInt32(e) 替代 ch.toUInt32()
    ✓ 直接应用修复，跳过 L3 搜索
↓
重新构建 → ✅ BUILD SUCCESSFUL
✓ 构建成功，方案验证有效
```

**新问题处理示例**（含失败情况）：
```
用户报错: error: invalid binary operator '==' on type 'UInt8' and 'Rune'
↓
Step 1: 检查 Evolution.md
    ✗ 搜索关键词 "UInt8", "Rune", "类型不匹配" - 未找到匹配记录
↓
Step 2: L3 本地文档搜索
    ✓ 搜索结果: String下标返回UInt8，不能与Rune直接比较
    ✓ 解决方案: 使用ASCII码值比较 (ch == 45u8)
↓
修复代码 → 重新构建
    ├─ 构建 ✅ 成功 → 将问题添加到 Evolution.md
    └─ 构建 ❌ 失败 → 方案错误，不能记录，重新寻找解决方案
```

### ✅ 构建成功标识

- 出现 `BUILD SUCCESSFUL` 表示构建成功
- 警告信息通常不影响构建（除非要签名时会提示缺少签名配置）

### 📝 构建成功后的总结要求

**⚠️ 重要原则: 只有在构建成功后才能更新 Evolution.md**
- 修复方案必须先验证（构建成功）
- 构建失败的方案不能记录（说明方案错误）
- 用户自行构建成功后，才能确认问题解决有效

**每次构建成功后，必须执行以下操作**：
1. 将本次开发过程中遇到的**重难点**整理成几点
2. 写入 skills 目录下的 `Evolution.md` 文件（即 `.claude/skills/cangjie-dev-harmonyos/Evolution.md`）
3. 记录内容包括：问题描述、错误代码、原因分析、解决方案、正确代码示例

> **重要**: Evolution.md 位于 skills 目录中，这样当技能迁移到其他项目时，历史问题记录也会一起迁移。

**Evolution.md 预期格式**：
```markdown
# Evolution - 项目重难点记录

## 项目: [项目名称]
### 构建日期: YYYY-MM-DD

## 重难点记录

### 1. [问题标题]
**问题描述**: [描述]
**错误代码**: ```cangjie [代码] ```
**解决方案**: [说明]
**正确语法**: ```cangjie [代码] ```
```

# 📚 本地文档源说明

本地 `./hm-docs/` 文件夹包含从以下官方仓库下载的最新文档：

- **UI开发**: 来自 `openharmony-sig/docs_cangjie` 仓库 → `./hm-docs/ui-dev/`
- **标准扩展库**: 来自 `Cangjie/cangjie_stdx` 仓库 → `./hm-docs/stdx/`
- **语法特性**: 来自 `Cangjie/cangjie_docs` 仓库 → `./hm-docs/syntax/`
- **标准库API**: 来自 `Cangjie/cangjie_runtime` 仓库 → `./hm-docs/stdlib/`
- **工具构建**: 来自 `Cangjie/cangjie_docs` 仓库 → `./hm-docs/tools/`

### 🔍 本地文档搜索优先级

直接搜索本地 `./hm-docs/` 文件夹，按优先级执行：

#### 🥇 UI开发和组件问题 (最高优先级)

**搜索路径**: `./hm-docs/ui-dev/arkui-cj/`

**常用组件快速定位**：
- **Button组件**: `@./hm-docs/ui-dev/arkui-cj/cj-common-components-button.md`
- **Text显示**: `@./hm-docs/ui-dev/arkui-cj/cj-common-components-text-display.md`
- **TextInput输入**: `@./hm-docs/ui-dev/arkui-cj/cj-common-components-text-input.md`
- **Image图片**: `@./hm-docs/ui-dev/reference/arkui-cj/cj-image-video-image.md`
- **List列表**: `@./hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md`
- **Grid网格**: `@./hm-docs/ui-dev/arkui-cj/cj-layout-development-create-grid.md`

#### 🥈 标准扩展库 (高级功能)

**搜索路径**: `./hm-docs/stdx/libs_stdx/`

#### 🥉 语法和语言特性

**搜索路径**: `./hm-docs/syntax/source_zh_cn/`

#### 📚 标准库API

**搜索路径**: `./hm-docs/stdlib/std/`

# Coding Guidelines

- **语言后缀**: `.cj`
- **UI 框架**: ArkUI-X (Cangjie 版本)
- **核心原则**: 宁可多查一次文档，不要写出一行假代码
- **需求分析**: 永远先进行L0需求技术化分析，不要直接搜索业务词汇
- **检索策略**: 搜索具体的技术API名称(Button、List、Image)，不搜索业务概念(篮球、电商、游戏）
- **UI问题优化**: UI/页面/应用开发问题在L1后直接跳到L3本地文档搜索
- **结果展示**: L1查询结果必须完整展示给用户查看，不能隐藏查询过程
- **实现导向**: 关注具体的代码实现步骤，而非抽象的概念描述
- **错误处理**: L1和L3无结果时告知"该功能可能不支持或文档未包含"
- **关键词策略**: 优先使用英文API名、函数名，然后尝试中文描述
- **信息权威性**: L3本地官方文档 > L1 RAG结果
- **UI开发优先级**: 🥇 鸿蒙应用指南 > 🥈 标准扩展库 > 🥉 语言指南 > 其他
- **效率原则**: UI问题直接查鸿蒙应用指南，避免在语法文档中浪费时间
- **构建报错处理** (新增):
  - 必须使用 Bash 工具执行 build.ps1 并设置足够 timeout (300000ms)
  - 输出显示 "Output too large" 时，必须读取完整输出文件
  - 只有在获取完整输出仍不足以定位问题时，才建议使用 DevEco Studio
  - 不提前判断输出大小，必须先执行再根据输出结果决定

# 📋 Additional Resources

- **L0 需求分析示例**: [examples/l0-analysis.md](examples/l0-analysis.md)
- **L1 RAG 查询示例**: [examples/l1-query.md](examples/l1-query.md)
- **L3 本地文档搜索示例**: [examples/l3-search.md](examples/l3-search.md)

## 🛠️ 技能脚本文件说明

### scripts/ 目录

本技能包含以下脚本文件，位于 `.claude/skills/cangjie-dev-harmonyos/scripts/` 目录：

| 脚本文件 | 作用 | 用法 |
|---------|------|------|
| `ask_cangjie.py` | L1 RAG 查询脚本（检测文件夹/压缩包/自动下载） | `python ask_cangjie.py "Button"` （scripts/ 目录内）|
| `cangjie_retriever.py` | 混合检索器（向量+BM25） | 被 ask_cangjie.py 调用 |
| `Database-Builder.py` | 构建向量数据库 | `python Database-Builder.py` （scripts/ 目录内）|
| `download_hm_docs.py` | 下载官方文档 | `python download_hm_docs.py` （scripts/ 目录内）|
| `build.ps1` | **项目构建脚本**（已环境同步） | `cd .claude\\skills\\cangjie-dev-harmonyos\\scripts && .\\build.ps1` |

### 依赖要求

使用 L1 RAG 查询功能需要：

1. **Python 3.x**
2. **Python 包**:
   ```bash
   pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv
   ```
3. **环境变量**: `SILICONFLOW_API_KEY`
4. **RAG_Lite 数据源**: `RAG_Lite/` 目录（包含知识库 JSON 文件）
