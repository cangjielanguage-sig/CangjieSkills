---
name: cangjie-project-entry
description: "HIGHEST PRIORITY / FIRST ENTRY for 仓颉/Cangjie work. Use when a task mentions Cangjie, 仓颉, .cj, index.cj, cjpm.toml, package/import, HarmonyOS/HMOS Cangjie app, build/debug, API docs, stdx, ArkTS interop, hvigor, ohpm, SyncCangjieResource, build-profile.json5, or oh-package.json5. Load cangjie-package-manage first for local project preflight, then route to build, docs, stdx, interop, or language Skills after the package/cjpm check."
---

# Cangjie 最高优先级入口

## 核心规则

本 Skill 是所有仓颉/Cangjie 任务的入口。只要任务涉及仓颉语言、本地 `.cj` 源码、`cjpm.toml`、包声明、import、HarmonyOS 仓颉应用、构建、调试、文档检索、stdx、ArkTS 互操作、Hvigor 或 ohpm，先使用本 Skill。

进入本 Skill 后，第一步必须加载 `cangjie-package-manage`。不要直接写代码、构建、查文档或手动排查配置。

## 如何加载 cangjie-package-manage

1. 使用 OpenCode 的 skill 工具选择并加载 `cangjie-package-manage`。
2. 读取 `cangjie-package-manage/SKILL.md`，按其中的快速流程执行首检。
3. 首检至少覆盖：入口 `cjpm.toml`、workspace 成员、`package.name`、`package.organization`、`src-dir`、源码目录到 package 的映射、`.cj` 文件 package 声明、import 位置、依赖可见性和明显的 HarmonyOS 构建配置风险。
4. 不要凭记忆复述 `cangjie-package-manage` 的规则；必须实际加载该 Skill 后再执行。

## Cangjie 开发注意点

- 修改 `.cj` 文件前，先确认 package 声明和目录映射正确；`index.cj` 也不能跳过首检。
- `package` 声明必须与 `cjpm.toml` 的模块名、组织名和源码目录结构一致。
- `import` 必须位于 package 声明之后、其它声明之前，并避免导入自身包或制造循环依赖。
- 遇到 `no '.cj' file`、`cyclic dependency`、`can not find dependencies`、包声明位置错误或组织名前缀不一致，优先由 `cangjie-package-manage` 诊断。
- HarmonyOS 项目中看到 `build-profile.json5`、`oh-package.json5`、`hvigor`、`ohpm`、`SyncCangjieResource` 或构建失败日志时，仍先做 `cjpm`/package 首检，再进入构建 Skill。
- 纯语言语法/API 查询可以在首检判断无本地项目风险后进入 `cangjie-lang-features`、`cangjie-std`、`cangjie-stdx` 或 `cangjie-hmos-doc-search`。

## 后续 Skill 路由

- 构建、Hvigor、ohpm 深度排查：首检后使用 `cangjie-hmos-build`。
- 鸿蒙 API、组件、开发指南查询：首检后使用 `cangjie-hmos-doc-search`。
- 纯仓颉语言特性：首检后使用 `cangjie-lang-features`。
- 标准库或扩展库 API：首检后使用 `cangjie-std` 或 `cangjie-stdx`。
- HarmonyOS stdx 二进制配置：首检后使用 `cangjie-hmos-stdx`。
- ArkTS 互操作：首检后使用 `cangjie-arkts-interop`。

## 输出要求

向用户说明本次已先进入 Cangjie 入口，并报告是否已加载 `cangjie-package-manage`。如果未加载，必须说明原因，并在继续前加载它。
