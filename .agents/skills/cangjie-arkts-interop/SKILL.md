---
name: cangjie-arkts-interop
description: "提供仓颉与 ArkTS 互操作的实战指导文档，当需要实现 ArkTS 调用仓颉、仓颉调用 ArkTS、或仓颉与 ArkTS 混合 UI 开发时，应优先使用此 Skill"
---

# 仓颉 ↔ ArkTS 互操作目录

> 请按需查阅相关文档

- [声明式互操作宏 @Interop](./interop-macro/README.md): ArkTS 调用仓颉的首选方式。覆盖 @Interop 宏修饰函数/异步函数/interface/class/enum 的用法、场景速查、Async 替代方案（String JSON）、interface 成员函数与 mut prop、class 完整约束（静态初始化器/多构造函数/类型标注）、枚举示例与约束、类型分离原则、类型映射表、命名冲突规则

- [互操作库与 JSRuntime](./interop-lib/README.md): 宏覆盖不了时的底层方案，以及仓颉主动调用 ArkTS 系统模块。覆盖 JSModule.registerModule 手工导出、JSRuntime 单例模式与主线程限制、requireSystemNativeModule 与 requireArkModule 模块加载、模块名映射（含 @hms prefix）、多线程与线程切换（isInBindThread/postJSTask/死锁警告）、promiseCapability 手工 Promise、跨语言异常处理（JSCodeError）、跨语言对象引用与内存泄漏、JSObject 属性安全提取、thisArg 补全、JSValue 生命周期

- [混合 UI 与跨语言路由](./hybrid-ui/README.md): 仓颉页面作为组件嵌入 ArkTS 容器页。覆盖 CJHybridComponent 用法、跨语言路由回调桥接模式、混合工程关键目录与配置文件、新增混合页面步骤、模拟器 abiFilters 配置

- [工程扫描与全量互操作生成（ArkTS 调仓颉）](./arkts-invoke-cangjie/README.md): 从 `arkts-cangjie-interop` skill 迁移的完整流程。用于扫描某个 DevEco 仓颉工程目录，并在未指定增量对象时按工程内公开对象执行全量互操作接线（bridge、声明、`CustomLib` 暴露、ArkTS wrapper、装载校验与常见故障排查）

- [ArkTS 声明读取与仓颉封装生成（仓颉调 ArkTS）](./cangjie-invoke-arkts/README.md): 从 `cangjie-arkts` skill 迁移的生成流程。用于读取某个 `.d.ts`、`.d.ets` 或 `.ets` 文件（或其所在目录），提取接口/类/函数等 API 表面，并生成仓颉调用 ArkTS 的互操作代码（含 `ark_wrapper` helper 与 API 封装代码）
