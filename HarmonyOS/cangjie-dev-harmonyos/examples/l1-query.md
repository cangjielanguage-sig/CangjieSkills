# Phase 1: RAG 查询示例 (L1)

## 示例 1: List 组件相关查询

### 场景
用户需要创建一个商品列表页面（基于 L0 分析细化后）

### 查询计划

```bash
# 进入 workflow 目录
cd cangjie-dev-workflow

# List 组件相关 - 按组件分组查询
python ask_cangjie.py "List"

# Image 组件相关
python ask_cangjie.py "Image"

# Text 组件相关
python ask_cangjie.py "Text"
```

### 查询结果示例

#### 查询 1: `python ask_cangjie.py "List"`

```text
[原始问题]: List
[相关度]: 0.85
[来源]: 文档片段
[本地路径]: hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md

[知识片段]:
List 组件是 ArkUI 中用于展示列表的基础组件，导入方式：
import kit.ArkUI

List 的基本使用需要导入 ArkUI 包，包含列表创建、滚动、数据绑定等功能...
```
**状态**: ✅ 部分结果 - 找到导入方式信息

#### 查询 2: `python ask_cangjie.py "List初始化"`

```text
[原始问题]: List初始化
[相关度]: 0.78
[来源]: API 参考

[知识片段]:
List 的初始化常用方式：

方式1 - 空列表初始化：
List() {
    ListItem({ content: ... })
}

方式2 - 使用 ForEach 创建：
List() {
    ForEach(data) { item =>
        ListItem({ content: ... })
    }
}

方式3 - 自定义渲染器：
List(renderItem: renderFunction)
...
```
**状态**: ✅ 有效结果 - 有代码示例

#### 查询 3: `python ask_cangjie.py "List数据绑定"`

```text
[原始问题]: List数据绑定
[相关度]: 0.45
[来源]: 关键词匹配

[知识片段]:
有关数据绑定的信息，请查看 @Observed 和 @State 装饰器的使用...
```
**状态**: ⚠️ 结果不完整 - 需要进一步搜索

### 评估决策

- List 找到有效信息 ✅
- List 数据绑定信息不完整 ⚠️
- Image、Text 尚未查询...

**决策**: 继续执行其他组件的 L1 查询，然后评估整体结果

---

## 示例 2: 快速成功案例 - 线程创建

### 场景
用户询问："如何创建线程"

### 查询执行

```bash
cd cangjie-dev-workflow
python ask_cangjie.py "如何创建线程"
```

### 查询结果

```text
[原始问题]: 如何创建线程
[相关度]: 0.92
[来源]: 并发编程文档

[知识片段]:
在仓颉语言中，线程创建使用 spawn 关键字：

基本语法：
spawn {
    // 执行的代码
}

示例：
func runTask() {
    spawn {
        println("子线程执行")
    }
    println("主线程继续")
}

也可以返回线程句柄：
let thread = spawn { ... }
thread.join()  // 等待线程完成
```
**状态**: ✅ 完整结果

### 评估决策

- 获得完整的 API 语法和使用示例 ✅
- 有可直接使用的代码 ✅

**决策**: 停止检索，基于此结果编码

---

## 示例 3: 失败后跳转 L3

### 场景
用户询问："HTTP 客户端 API"

### 查询执行

```bash
cd cangjie-dev-workflow
python ask_cangjie.py "HTTP客户端"
```

### 查询结果

```
NO_RAG_RESULT
未找到与 "HTTP客户端" 相关的结果
```
**状态**: ❌ 无结果

### 查询其他变体

```bash
python ask_cangjie.py "HTTP请求"
python ask_cangjie.py "网络请求"
python ask_cangjie.py "HttpClient"
```

```
NO_RAG_RESULT (多次尝试均失败)
```
**状态**: ❌ L1 检索完全失败

### 评估决策

- L1 检索完全失败 ❌
- 需要进入 Phase 3: 本地文档搜索

**跳转 L3**:
```powershell
# 搜索 HTTP 相关文档
Get-ChildItem -Path "hm-docs" -Filter "*.md" -Recurse | Select-String -Pattern "http|HTTP" -Context 1
```

---

## 示例 4: 按控制列表验证

### 完整执行记录表格

| ID | 查询关键词 | 结果状态 | 内容完整性 | 操作 |
|----|-----------|---------|-----------|------|
| 1 | Lis | ✅ | 基本完整 | 继续下一个 |
| 2 | Image | ✅ | 基本完整 | 继续下一个 |
| 3 | Text | ✅ | 基本完整 | 继续下一个 |
| 4 | Button  | ✅ | 基本完整 | 结束评估 |
| 5 | onClick  | ✅ | 基本完整 | 结束评估 |


### 最终评估

```
核心组件查询统计:
- List组件: 3/3 有结果，2个完整 ✅
- Image组件: 1/2 有结果，需补充 ⚠️
- Text组件: 1/1 有结果，完整 ✅
- Button组件: 1/1 有结果，完整 ✅

整体评估: 6/8 查询成功，关键信息较完整
决策: 可以开始编码，Image显示细节必要时通过 L3 补充
```

---

## ✅ L1 查询最佳实践

### 1. 分组执行
按组件分组，每个维度单独查询，提高 BM25 匹配精度

### 2. 精准关键词
- ✅ "Butto" - 精准匹配相关内容
- ❌ "如何创建按钮" - 模糊描述，匹配度低

### 3. 结果展示
必须将查询结果完整展示给用户，包含原始问题和知识片段

### 4. 评估决策
根据查询结果决定下一步：
- ✅ 关键组件有完整代码 → 停止检索，开始编码
- ⚠️ 部分结果不完整 → 可选择性进入 L3 补充
- ❌ 完全无结果 → 必须进入 L3

### 5. 中文优先
仓颉文档多为中文，优先使用中文 API 名称：
- Button < 按钮
- TextInput < 文本输入
- List < 列表

---

## 工作流转决策树

```
L1 查询执行
    ↓
    ├─ ✅ 完整结果 → 停止检索 → 开始编码
    │
    ├─ ⚠️ 部分结果 → 评估必要性
    │                     ↓
    │       ┌─────────────┴────────────┐
    │       ↓                          ↓
    │   可选L3补充                 直接编码(边做边查)
    │
    └─ ❌ 无结果 → 进入 L3 → 本地文档搜索
```
