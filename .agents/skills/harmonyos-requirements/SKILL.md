---
name: harmonyos-requirements
description: "鸿蒙应用开发需求分析与设计 Skill。当用户提出鸿蒙应用开发需求时，必须先使用此 Skill 完成需求分析和设计方案，再搜集技术知识，最后才进入编码阶段。禁止跳过分析直接写代码。"
---

# 鸿蒙应用需求分析与设计 Skill

## 目的

在编码之前完成需求理解、方案设计、知识搜集三个阶段，确保开发有据可依，避免边写边猜。

## 适用场景

- 用户提出新功能开发需求（如"帮我做一个XX页面"、"实现XX功能"）
- 用户要求对现有功能进行较大改动
- 涉及多个组件/模块协作的开发任务

## 版本检测

本工作区支持两个版本：**8k** 和 **15k**，版本会影响文档检索与构建 SDK 选择。

1. 检查工作区根目录是否存在 `.openvk-version` 文件
2. 存在且有效（`8k` 或 `15k`）→ 直接使用
3. 不存在时自动创建 `.openvk-version` 并写入默认值 `8k`
4. 后续所有阶段直接读取该文件，不再重复询问

## 核心原则

- **禁止跳过分析直接编码。** 必须完成阶段一和阶段二后才能动手写代码。
- **每个阶段产出明确。** 需求确认清单、设计方案、知识清单都必须输出给用户确认。
- **不确定的地方先确认，不要猜。** 需求歧义、交互细节、边界条件，宁可多问一轮。

## 执行流程（严格按顺序）

### 阶段一：需求分析

**目标：** 把用户的模糊需求转化为明确的功能点清单。

**步骤：**

1. **理解需求**：仔细阅读用户描述，提取核心诉求。
2. **拆解功能点**：将需求拆分为具体的、可实现的功能点，每个功能点用一句话描述。
3. **识别不确定项**：列出需求中含糊或缺失的部分（如交互细节、异常处理、数据来源等）。
4. **输出需求确认清单**：以表格或列表形式呈现给用户，格式如下：

```
## 需求确认清单

### 功能点
1. [功能点1描述]
2. [功能点2描述]
3. ...

### 待确认项（需要你的回复）
- [问题1]
- [问题2]
```

5. **等待用户确认**：用户确认或补充后，更新功能点清单，进入阶段二。

### 阶段二：设计方案

**目标：** 基于确认后的功能点，输出技术设计方案。

**步骤：**

1. **页面/组件拆分**：确定需要哪些页面、自定义组件、弹窗等。
2. **状态管理设计**：确定用哪些状态装饰器（@State、@Prop、@Link、@Provide/@Consume 等），数据如何流转。
3. **布局方案**：确定主要布局结构（Column、Row、Stack、List、Grid 等）。
4. **系统能力依赖**：列出需要调用的系统 API（网络请求、文件读写、权限申请、路由跳转等）。
5. **输出设计方案**：格式如下：

```
## 设计方案

### 组件结构
- PageA（主页面）
  - HeaderComponent（顶部栏）
  - ContentList（内容列表）
  - BottomBar（底部导航）

### 状态管理
- @State items: Array<ItemType>  // 列表数据
- @State isLoading: Bool         // 加载状态
- @Link selectedId: String       // 父组件传入的选中项

### 布局方案
- 主页面：Column 纵向布局
- 列表区域：List + ForEach
- 每项：Row 横向排列图标和文字

### 系统能力
- ohos.net.http：网络请求获取数据
- @ohos.router：页面跳转
```

6. **等待用户确认**：设计方案确认后，进入阶段三。

### 阶段三：知识搜集

**目标：** 针对设计方案中涉及的技术点，搜集足够的文档和代码参考，确保编码时有据可依。

**步骤：**

1. **识别知识缺口**：从设计方案中提取所有需要查阅的技术点（组件用法、API 调用方式、状态管理写法、语法细节等）。

2. **优先查阅仓颉基础 Skill（第一优先级）**：对每个技术点，先在工作区内的仓颉基础 Skill 中查找。这些 Skill 覆盖了语法、标准库、工具链等核心知识，查阅速度快且内容经过整理。

   **常用 Skill 对照表：**

   | 技术点类型 | 对应 Skill |
   |-----------|-----------|
   | 类、继承、构造函数 | cangjie_class |
   | 结构体、值类型 | cangjie_struct |
   | 接口、多态 | cangjie_interface |
   | 泛型 | cangjie_generic |
   | 集合（Array、ArrayList、HashMap、HashSet） | cangjie_collections |
   | 字符串操作 | cangjie_string |
   | 函数、闭包、Lambda | cangjie_function |
   | 错误处理、异常 | cangjie_error_handle |
   | 枚举 | cangjie_enum |
   | 模式匹配 | cangjie_pattern_match |
   | Option 类型 | cangjie_option |
   | 循环、迭代 | cangjie_for |
   | 并发、异步 | cangjie_concurrency |
   | 网络（HTTP/Socket/WebSocket/TLS） | cangjie_network |
   | 包管理、模块 | cangjie_package |
   | 标准库（fs/io/stdio/unittest等） | cangjie_std |
   | 扩展库（json/config等） | cangjie_stdx |
   | 宏 | cangjie_macro |
   | C 互操作 | cangjie_cffi |
   | 扩展 | cangjie_extend |
   | 反射与注解 | cangjie_reflect_and_annotation |
   | 类型系统 | cangjie_type_system |
   | 工具链（cjc/cjfmt/cjlint等） | cangjie_toolchains |

3. **基础 Skill 无法覆盖时，使用 cangjie-harmonyos-doc-search 检索（第二优先级）**：当技术点涉及鸿蒙框架特有内容（UI 组件用法、系统能力 API、状态管理装饰器、应用生命周期等），且仓颉基础 Skill 中没有对应内容时，再使用文档检索工具。

```shell
# 示例：查询鸿蒙 UI 组件
python cangjie-harmonyos-doc-search/search.py "List组件用法" --version <版本>

# 示例：查询系统能力 API
python cangjie-harmonyos-doc-search/search.py "http网络请求" --version <版本>

# 示例：查询状态管理装饰器
python cangjie-harmonyos-doc-search/search.py "State状态管理" --version <版本>
```

4. **输出知识清单**：汇总已搜集的关键信息，格式如下：

```
## 知识搜集结果

### 仓颉基础 Skill 参考（第一优先级）
- [技术点1]：参考 cangjie_xxx Skill，关键写法为 ...
- [技术点2]：参考 cangjie_xxx Skill，注意事项为 ...

### 鸿蒙文档检索结果（第二优先级）
- [技术点3]：已阅读 xxx/xxx.md，关键写法为 ...
- [技术点4]：已阅读 xxx/xxx.md，注意事项为 ...

### 待编码确认
- 所有技术点已有文档支撑，可以开始编码
```

### 阶段四：编码开发

**前置条件：** 阶段一到阶段三全部完成，用户已确认需求和设计方案，知识已搜集充分。

**步骤：**

1. 按设计方案中的组件结构逐个实现。
2. 每个组件实现后，简要说明实现要点。
3. 实现完成后，使用 harmonyos-build Skill 执行构建验证。
4. 构建失败时，按 harmonyos-build Skill 的失败处理优先级排查。

## 轻量需求的简化处理

当需求非常简单（如"改个文字"、"调个颜色"、"加个按钮"）时，可以合并阶段一和阶段二为一段简短确认，但仍然必须：

1. 向用户确认具体改动内容
2. 必要时用 doc-search 查阅相关组件/API 文档
3. 修改后构建验证
