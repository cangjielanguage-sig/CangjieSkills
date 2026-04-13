---
name: harmonyos-requirements
description: "鸿蒙应用开发需求分析与设计 Skill。当用户提出鸿蒙应用开发需求时，必须先使用此 Skill 完成需求分析和设计方案，再搜集技术知识，最后才进入编码阶段。禁止跳过分析直接写代码。"
---

# 鸿蒙应用需求分析与设计 Skill

## 目的

在编码之前完成需求理解、方案设计、知识搜集三个阶段，确保开发有据可依，避免边写边猜

## 适用场景

- 用户提出新功能开发需求（如"帮我做一个XX页面"、"实现XX功能"）
- 用户要求对现有功能进行较大改动
- 涉及多个组件/模块协作的开发任务

## 核心原则

- 禁止跳过分析直接编码，必须完成阶段一和阶段二后才能动手写代码
- 每个阶段产出明确，需求确认清单、设计方案、知识清单都必须输出给用户确认
- 不确定的地方先确认不要猜，需求歧义、交互细节、边界条件宁可多问一轮

## 执行流程（严格按顺序）

### 阶段一：需求分析

把用户的模糊需求转化为明确的功能点清单

1. 理解需求，提取核心诉求
2. 拆解为具体可实现的功能点，每点一句话描述
3. 识别不确定项（交互细节、异常处理、数据来源等）
4. 输出需求确认清单（功能点列表 + 待确认项），等待用户确认后进入阶段二

### 阶段二：设计方案

基于确认后的功能点输出技术设计方案

1. 页面/组件拆分 — 确定需要哪些页面、自定义组件、弹窗等
2. 状态管理设计 — 确定状态装饰器（@State/@Prop/@Link/@Provide/@Consume 等）及数据流转
3. 布局方案 — 确定主要布局结构（Column/Row/Stack/List/Grid 等）
4. 系统能力依赖 — 列出需要调用的系统 API（网络请求、文件读写、权限申请、路由跳转等）
5. 输出设计方案，等待用户确认后进入阶段三

### 阶段三：知识搜集

针对设计方案中的技术点搜集文档和代码参考

**第一优先级 — 仓颉基础 Skill：**

| 技术点类型 | 对应 Skill |
|-----------|-----------|
| 类/继承/构造函数 | cangjie_class |
| 结构体/值类型 | cangjie_struct |
| 接口/多态 | cangjie_interface |
| 泛型 | cangjie_generic |
| 集合（Array/ArrayList/HashMap/HashSet） | cangjie_collections |
| 字符串操作 | cangjie_string |
| 函数/闭包/Lambda | cangjie_function |
| 错误处理/异常 | cangjie_error_handle |
| 枚举 | cangjie_enum |
| 模式匹配 | cangjie_pattern_match |
| Option 类型 | cangjie_option |
| 循环/迭代 | cangjie_for |
| 并发/异步 | cangjie_concurrency |
| 网络（HTTP/Socket/WebSocket/TLS） | cangjie_network |
| 包管理/模块 | cangjie_package |
| 标准库（fs/io/stdio/unittest 等） | cangjie_std |
| 扩展库（json/config 等） | cangjie_stdx |
| 宏 | cangjie_macro |
| C 互操作 | cangjie_cffi |
| 扩展 | cangjie_extend |
| 反射与注解 | cangjie_reflect_and_annotation |
| 类型系统 | cangjie_type_system |
| 工具链（cjc/cjfmt/cjlint 等） | cangjie_toolchains |

**第二优先级 — cangjie-harmonyos-doc-search 文档检索：**

当技术点涉及鸿蒙框架特有内容（UI 组件、系统能力 API、状态管理装饰器、生命周期等），且基础 Skill 未覆盖时使用

```bash
python .agents/skills/cangjie-harmonyos-doc-search/search.py "List列表组件"
python .agents/skills/cangjie-harmonyos-doc-search/search.py "http网络请求"
python .agents/skills/cangjie-harmonyos-doc-search/search.py "@State装饰器"
```

### 阶段四：编码开发

前置条件：阶段一到阶段三全部完成，用户已确认需求和设计方案

1. 按设计方案中的组件结构逐个实现
2. 每个组件实现后简要说明实现要点
3. 实现完成后使用 harmonyos-build Skill 执行构建验证
4. 构建失败时按 harmonyos-build Skill 的失败处理优先级排查

## 轻量需求的简化处理

需求非常简单时（改文字、调颜色、加按钮），可合并阶段一和阶段二为一段简短确认，但仍需：向用户确认具体改动 → 必要时查阅文档 → 修改后构建验证
