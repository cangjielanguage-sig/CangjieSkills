---
name: cangjie-project-entry
description: "Routing gateway for broad Cangjie tasks and .cj code filling. Use when a request asks to 生成/填充/实现仓颉代码, edit a .cj file, fill a TODO/function skeleton, or mixes Cangjie language/API work with local project files, cjpm.toml, package/import structure, HarmonyOS/HMOS app build, Hvigor/ohpm, stdx setup, ArkTS interop, or docs. For standalone func implementation from signatures, comments, examples, prompt-only code generation, or isolated .cj snippets, route to cangjie-lang-features plus cangjie-std, adding cangjie-stdx only for configured extension-library APIs."
---

# Cangjie 路由入口

## 核心规则

本 Skill 是仓颉/Cangjie 复杂任务的入口。它只负责判断下一步应该加载哪些专门 Skill，不直接替代语言、标准库、项目管理或 HarmonyOS Skill。

优先判断任务形态：

1. 函数签名/注释/示例驱动的独立实现、prompt-only 生成、孤立 `.cj` 片段、纯语法/类型/集合/字符串问题：直接加载 `cangjie-lang-features` 和 `cangjie-std`；涉及 JSON、编码、哈希、HTTP、TLS、WebSocket、压缩、序列化或其他扩展库且环境已配置时再加载 `cangjie-stdx`。不要先加载 `cangjie-package-manage`。
2. 本地项目包含 `cjpm.toml`、workspace、package/import 结构、依赖可见性、`no '.cj' file`、`cyclic dependency`、`can not find dependencies` 等包管理信号：先加载 `cangjie-package-manage`。
3. HarmonyOS/HMOS 应用、Hvigor、ohpm、`build-profile.json5`、`oh-package.json5`、`SyncCangjieResource`、设备运行或平台 API 文档：按后续路由加载对应 HarmonyOS Skill。
4. `.cj` 文件含 `@Entry`、`@Component`、`build()`、`@State`、`@Prop`、`@Link`、`@Observed`、`ForEach` 或 `LazyForEach` 等 ArkUI 信号：同时加载 `cangjie-hmos-arkui`，并保留 `cangjie-lang-features` + `cangjie-std` 的通用写入门禁；不要因出现 `build()` 就误路由到 `cangjie-hmos-build`。

## 如何加载 cangjie-package-manage

仅当任务有真实 cjpm 项目信号时加载：

1. 使用 OpenCode 的 skill 工具选择并加载 `cangjie-package-manage`。
2. 读取 `cangjie-package-manage/SKILL.md`，按其中的快速流程执行首检。
3. 首检至少覆盖：入口 `cjpm.toml`、workspace 成员、`package.name`、`package.organization`、`src-dir`、源码目录到 package 的映射、`.cj` 文件 package 声明、import 位置、依赖可见性和明显的 HarmonyOS 构建配置风险。
4. 不要凭记忆复述 `cangjie-package-manage` 的规则；必须实际加载该 Skill 后再执行。

## Cangjie 开发注意点

- 修改本地 cjpm 项目中的 `.cj` 文件前，先确认 package 声明和目录映射正确；`index.cj` 也不能跳过首检。
- 生成独立函数或孤立 `.cj` 片段时，优先使用语言与库 Skill，不做 cjpm/package 首检。
- `package` 声明必须与 `cjpm.toml` 的模块名、组织名和源码目录结构一致。
- `import` 必须位于 package 声明之后、其它声明之前，并避免导入自身包或制造循环依赖。
- 遇到 `no '.cj' file`、`cyclic dependency`、`can not find dependencies`、包声明位置错误或组织名前缀不一致，优先由 `cangjie-package-manage` 诊断。
- HarmonyOS 项目中看到 `build-profile.json5`、`oh-package.json5`、`hvigor`、`ohpm`、`SyncCangjieResource` 或构建失败日志时，仍先做 `cjpm`/package 首检，再进入构建 Skill。
- 纯语言语法/API 查询直接进入 `cangjie-lang-features`、`cangjie-std`、`cangjie-stdx` 或 `cangjie-hmos-doc-search`，不因出现“仓颉/Cangjie”字样而自动做 package 预检。

## 后续 Skill 路由

- 独立函数 / 孤立 `.cj` 片段：使用 `cangjie-lang-features` + `cangjie-std`；需要且可用扩展库时加 `cangjie-stdx`。
- 本地 cjpm/package/import 问题：使用 `cangjie-package-manage`。
- 构建、Hvigor、ohpm 深度排查：使用 `cangjie-hmos-build`；若同时有 cjpm/package 信号，先用 `cangjie-package-manage`。
- 鸿蒙 API、组件、开发指南查询：使用 `cangjie-hmos-doc-search`。
- ArkUI 声明式 UI、`build()` 规则、状态宏与渲染控制：使用 `cangjie-hmos-arkui`；如需写入 `.cj`，同时使用 `cangjie-lang-features` + `cangjie-std`。
- 纯仓颉语言特性：使用 `cangjie-lang-features`。
- 标准库或扩展库 API：使用 `cangjie-std` 或 `cangjie-stdx`。
- HarmonyOS stdx 二进制配置：使用 `cangjie-hmos-stdx`。
- ArkTS 互操作：使用 `cangjie-arkts-interop`。

## 输出要求

向用户说明本次已先进入 Cangjie 入口，并报告选择了哪些后续 Skill。只有在存在真实 cjpm 项目信号时才报告并加载 `cangjie-package-manage`；如果是独立函数或孤立片段任务，应明确说明已跳过 package 预检。
