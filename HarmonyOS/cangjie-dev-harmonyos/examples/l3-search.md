# Phase 2: 本地文档搜索示例 (L3)

## 示例 1: UI 组件问题 - Button 查询

### 场景
L1 检索没有找到 Button 组件的完整使用方法，需要查询本地文档

### 问题分析
- 组件类型: Button (UI 基础组件)
- 问题类别: UI 开发问题
- 优先路径: `hm-docs/ui-dev/arkui-cj/`

### 搜索策略

#### 步骤 1: 使用快速定位路径

```powershell
# 直接读取 Button 组件文档
Get-Content "hm-docs\ui-dev\arkui-cj\cj-common-components-button.md"
```

**搜索结果:**
```
# Button 组件

Button 是基础按钮组件，用于响应用户点击操作。

## 导入
```cangjie
import kit.ArkUI
```

## 初始化
```cangjie
// 基础按钮
Button("点击我")

// 图标按钮
Button("图标", image: @r("icon.png"))

// 自定义内容按钮
Button() {
    Text("自定义内容")
}
```

## 属性
- width: 宽度
- height: 高度
- enabled: 是否可用
- type: 按钮类型 (Normal, Capsule)

## 事件
- onClick: 点击事件
- onHover: 悬停事件
```

#### 步骤 2: 如果文档信息不足，扩展搜索

```powershell
# 在 UI 文档中搜索相关文件
Get-ChildItem -Path "hm-docs\ui-dev\arkui-cj" -Filter "*.md" -Recurse |
    Select-String -Pattern "onClick|button" -Context 1
```

---

## 示例 2: 构建错误排查 - undefined symbol

### 场景
构建失败，错误信息: `undefined symbol: SomeFunction`

### 问题分析
- 错误类型: undefined symbol
- 问题类别: 构建错误 / API 查询
- 优先路径: `hm-docs/ui-dev/reference/` 或 `hm-docs/stdlib/std/`

### 搜索策略

#### 步骤 1: 检查 Evolution.md

```powershell
# Evolution.md 位于 skills 目录中
# 先检查是否有相同问题的历史记录
$skillEvolution = ".claude/skills/cangjie-dev-harmonyos/Evolution.md"
if (Test-Path $skillEvolution) {
    Select-String -Path $skillEvolution -Pattern "undefined symbol|SomeFunction" -Context 3
}
```

**结果** - 如果找到：
```text
### 1. undefined symbol 错误
错误原因: 函数未正确导入
解决方案: 添加 import kit.ArkUI
```
**操作**: 应用已验证的解决方案，跳过文档搜索

**结果** - 如果未找到：进入步骤 2

#### 步骤 2: 搜索 API 定义

```powershell
# 在 API 参考文档中搜索符号定义
Get-ChildItem -Path "hm-docs\ui-dev\reference" -Filter "*.md" -Recurse |
    Select-String -Pattern "SomeFunction" -Context 2
```

#### 步骤 3: 搜索导入示例

```powershell
# 在 UI 开发指南中搜索导入示例
Get-ChildItem -Path "hm-docs\ui-dev\arkui-cj" -Filter "*.md" -Recurse |
    Select-String -Pattern "import.*SomeFunction|import.*ArkUI" -Context 1
```

---

## 示例 3: 高级功能 - HTTP 请求

### 场景
用户需要实现 HTTP 请求功能，L1 检索失败

### 问题分析
- 功能类型: HTTP 客户端
- 问题类别: 标准扩展库 / 网络编程
- 优先路径: `hm-docs/stdx/libs_stdx/net/http/`

### 搜索策略

#### 步骤 1: 定位 HTTP 模块

```powershell
# 快速查找 HTTP 相关文件
Get-ChildItem -Path "hm-docs\stdx\libs_stdx\net\http" -Filter "*.md"
```

**结果:**
```
hm-docs\stdx\libs_stdx\net\http\http_client.md
hm-docs\stdx\libs_stdx\net\http\http_request.md
hm-docs\stdx\libs_stdx\net\http\http_response.md
```

#### 步骤 2: 读取核心文档

```powershell
Get-Content "hm-docs\stdx\libs_stdx\net\http\http_client.md"
```

**核心信息:**
```cangjie
// 导包
import stdx.net.http.*

// 创建 HTTP 客户端
let client = HttpClient()

// 发送 GET 请求
let response = client.get("https://api.example.com/data")

// 发送 POST 请求
let response = client.post(
    url = "https://api.example.com/data",
    body = "{\"key\": \"value\"}"
)

// 处理响应
if (response.statusCode == 200) {
    let body = response.body
    // 解析响应数据
}
```

---

## 示例 4: L1→L3 路径映射快捷方式

### 场景
L1 查询返回了本地路径引用，需要快速定位文档

### L1 查询结果
```text
[查询]: List初始化
[结果]:
List 组件的正确初始化方式请参考:
[本地路径]: hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md

List 使用 ForEach 创建动态列表...
```

### 快速执行

```powershell
# 1. 使用 L1 返回的路径直接读取
Get-Content "hm-docs\ui-dev\arkui-cj\cj-layout-development-create-list.md"

# 2. 如果需要更多上下文，扩展搜索
Get-ChildItem -Path "hm-docs\ui-dev\arkui-cj" -Filter "*.md" -Recurse |
    Select-String -Pattern "List|ForEach|ListItem" -Context 2
```

---

## 示例 5: 语法查询 - 泛型使用

### 场景
用户询问仓颉语言的泛型语法

### 问题分析
- 问题类型: 语言语法
- 问题类别: 泛型编程
- 优先路径: `hm-docs/syntax/source_zh_cn/generic/`

### 搜索策略

```powershell
# 定位泛型相关文档
Get-ChildItem -Path "hm-docs\syntax\source_zh_cn\generic" -Filter "*.md"
```

**结果:**
```
hm-docs\syntax\source_zh_cn\generic\generic_function.md
hm-docs\syntax\source_zh_cn\generic\generic_class.md
hm-docs\syntax\source_zh_cn\generic\generic_constraints.md
```

```powershell
# 读取泛型函数文档
Get-Content "hm-docs\syntax\source_zh_cn\generic\generic_function.md"
```

---

## 常用搜索命令速查表

### PowerShell 命令

| 用途 | 命令 |
|------|------|
| 搜索关键词（带上下文） | `Select-String -Path "path" -Pattern "keyword" -Context 2` |
| 列出所有匹配文件 | `Select-String -Path "path" -Pattern "keyword" -List` |
| 递归搜索所有子目录 | `Get-ChildItem -Path "path" -Filter "*.md" -Recurse \| Select-String -Pattern "keyword"` |
| 直接读取文件 | `Get-Content "path/to/file.md"` |
| 搜索多个关键词 | `Select-String -Pattern "keyword1|keyword2" -Context 1` |

### 路径映射表

| RAG_Lite 源路径 | 映射后的本地路径 |
|----------------|-----------------|
| `zh-cn/application-dev/` | `hm-docs/ui-dev/` |
| `docs/dev-guide/` | `hm-docs/syntax/source_zh_cn/` |
| `std/doc/` | `hm-docs/stdlib/std/` |
| `doc/` | `hm-docs/stdx/libs_stdx/` |

---

## L3 搜索决策流程

```
L1 检索失败/不完整
    ↓
优先检查 Evolution.md
    ↓
    ├─ 找到相同问题 → 应用解决方案
    │
    └─ 未找到 → 进入 L3 搜索
        ↓
    分类判断问题类型
        ↓
        ├─ UI 组件问题 → 搜 ui-dev/arkui-cj/
        ├─ UI API 问题 → 搜 ui-dev/reference/
        ├─ 标准扩展库 → 搜 stdx/libs_stdx/
        ├─ 标准库 API → 搜 stdlib/std/
        ├─ 语法问题 → 搜 syntax/source_zh_cn/
        ├─ 构建错误 → 按错误类型搜索
        └─ 构建错误 → 搜 tools/source_zh_cn/
        ↓
    评估搜索结果
        ↓
        ├─ 找到相关信息 → 编码
        └─ 未找到 → 告知"该功能可能不支持或文档未包含"
```

---

## ✅ L3 搜索最佳实践

### 1. 优先级顺序
UI 开发问题优先查 `ui-dev/`，避免在语法文档中浪费时间

### 2. 路径提示
L1 查询结果包含 `[本地路径]` 时优先使用该路径

### 3. Evolution 优先
构建错误首先检查 `Evolution.md`，避免重复工作

### 4. 上下文扩展
如果单个文档信息不足，扩展搜索相关联的其他文档

### 5. 构建错误处理
- `import error` → 搜索导入示例
- `undefined symbol` → 搜索 API 定义
- `syntax error` → 搜索语法说明
- `permission error` → 搜索 module.json5

---

## 常见问题类型对应的搜索路径

| 问题类型 | 优先路径 | 备用路径 |
|---------|---------|---------|
| Button/Text/List 等组件 | `ui-dev/arkui-cj/cj-common-components-*.md` | `ui-dev/reference/arkui-cj/cj-*-*.md` |
| 布局问题 | `ui-dev/arkui-cj/cj-layout-development-*.md` | - |
| 事件处理 | `ui-dev/arkui-cj/cj-common-events-*.md` | - |
| HTTP/TLS | `stdx/libs_stdx/net/http/` | `stdx/libs_stdx/net/tls/` |
| JSON/Base64 | `stdx/libs_stdx/encoding/json/` | `stdx/libs_stdx/encoding/base64/` |
| 加密/摘要 | `stdx/libs_stdx/crypto/` | - |
| 数据库 | `stdlib/std/database_sql/` | - |
| 并程/线程 | `syntax/source_zh_cn/concurrency/` | - |
| 泛型/宏 | `syntax/source_zh_cn/generic/` 或 `/Macro/` | - |
| 构建错误 | `syntax/source_zh_cn/compile_and_build/` | `tools/source_zh_cn/` |
