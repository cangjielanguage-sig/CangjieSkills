---
name: cangjie-package-manage
description: "cjpm/package 专项预检 Skill。Use when 需要检查 Cangjie/cjpm 项目的 cjpm.toml、workspace、package 声明、目录到包名映射、src-dir、organization/orgName::、import 位置/语法、依赖可见性。用于定位 no '.cj' file、cyclic dependency、can not find dependencies、包声明位置错误和包依赖语法问题；不覆盖纯语言、纯文档、UI 组件或深度 Hvigor/ohpm 构建排查。"
---

# cjpm 包管理预检

## 核心目标

在修改或编译 cjpm 项目前，先通过静态阅读确认源码包能被 cjpm 正确识别，并确认包声明、导入语句、模块依赖配置和包间依赖没有明显语法或结构问题。尽量减少 cjpm 命令调用次数；需要工具验证时优先使用一次 `cjpm build -V`，因为 `build` 本身会执行依赖检查。

只按 cjpm 模块和 `cjpm.toml` 语义判断包管理问题。不要把 cjc 单文件编译、手工 `-p` 编译或语言级默认包规则直接套用到 cjpm 包管理体系。

## 快速流程

1. 定位入口配置：从当前目录或用户指定目录找到 `cjpm.toml`。
2. 判断项目形态：如果存在 `[package]`，按单模块处理；如果存在 `[workspace]`，按工作空间成员逐个处理。
3. 读取模块字段：记录 `package.name`、可选 `package.organization`、可选 `package.src-dir`，以及 `[dependencies]`、`[test-dependencies]`、`[script-dependencies]`、`[replace]` 和 target 专用依赖。
4. 建立源码包清单：以 `src-dir` 为源码根目录，默认是 `src`；如果 `src-dir` 配置为相对路径，按 `cjpm.toml` 所在目录解析。
5. 检查每个源码目录是否是有效源码包：目录必须直接包含至少一个 `.cj` 文件；其父包链直到 root 包也必须是有效源码包。
6. 检查每个 `.cj` 文件的包声明：位置、包名、组织名、同目录一致性、目录路径映射。
7. 检查每个 `.cj` 文件的 `import`：位置、语法、组织名前缀、访问修饰符、别名、是否导入自身包。
8. 若需要验证，直接执行用户最终需要的 `cjpm build`、`cjpm test` 或 `cjpm run`；需要观察编译命令时使用 `cjpm build -V`。

## 包声明规则

从 `cjpm.toml` 推导期望包名：

- root 包名来自 `[package].name`，它同时是模块名和 root 包名。
- 如果配置了 `[package].organization`，源码中的包声明和跨模块导入应使用 `organization::package.path` 形式。
- 如果没有配置 `organization`，源码中不要凭空添加 `org::` 前缀。
- `src-dir` 未配置时源码根目录是 `src`；配置为相对路径时，路径基准是 `cjpm.toml` 所在目录。
- 子包名由源码目录相对 `src-dir` 的路径决定，路径分隔符替换为 `.`。

检查 package 声明时执行这些规则：

- 包声明必须出现在源文件非空非注释的首行。
- 同一个目录中的不同 `.cj` 文件必须属于同一个包，包声明必须一致。
- 源码根目录中的 `.cj` 文件也应显式声明模块 root 包，例如 `package demo`；若模块组织名是 `org`，应声明 `package org::demo`。
- 源码根目录下的子目录中的 `.cj` 文件应声明与目录路径一致的包名，例如 `src/foo/bar/a.cj` 在模块 `demo` 中应声明 `package demo.foo.bar`；若模块组织名是 `org`，应声明 `package org::demo.foo.bar`。
- 目录名必须与包名路径中的对应分量一致。
- 包声明可以使用 `internal`、`protected`、`public` 修饰，默认是 `public`；不要把合法的访问修饰符误判成非法包声明。
- 如果遇到 `macro package`，按宏包语义保留，不要机械改写成普通 `package`；仍需确认其包名与目录映射一致。
- 子包名不能和当前包内的顶层声明同名，否则后续导入可能产生歧义。

有效源码包规则：

- 一个源码包目录必须直接包含至少一个 `.cj` 文件。
- 如果 `src/pkg0/aoo/aoo.cj` 存在，但 `src/pkg0/` 没有直接的 `.cj` 文件，则 `pkg0` 不是有效源码包，`pkg0.aoo` 也不会被 cjpm 作为源码包继续扫描。
- 看到 `Warning: there is no '.cj' file in directory ... and its subdirectories will not be scanned as source code` 时，优先补齐父包目录的空包声明文件，例如 `src/pkg0/pkg0.cj` 只包含 `package demo.pkg0`。

## import 与依赖规则

检查导入语句时执行这些规则：

- `import` 必须位于包声明之后、其他声明或定义之前。
- `import` 可以带 `private`、`internal`、`protected`、`public` 修饰；默认是 `private import`。
- 常见合法形式包括：
  - `import fullPackageName.itemName`
  - `import orgName::fullPackageName.itemName`
  - `import packageName.*`
  - `import fullPackageName.{itemName, otherName}`
  - `import {package1.foo, package2.bar}`
  - `import packageName.name as newName`
  - `import packageName as newPackageName`
- `::` 后必须接包名；多导入中不要嵌套组织名前缀，例如不要写成 `import {org::a.b, org::a.c}`。
- 使用完整包名访问已导入成员时，不要带组织名前缀；`org::pkg.f()` 不是合法的成员访问形式。
- 禁止导入当前源文件所在包的声明或定义。
- 禁止包间循环依赖。`cjpm build` 会在构建前执行依赖检查，并在发现循环依赖时报告路径。
- 如果多个导入名称冲突，优先使用 `import as` 或导入包作为命名空间，不要盲目删除依赖。

检查 `cjpm.toml` 依赖时执行这些规则：

- `[dependencies]` 用于源码构建依赖，支持中心仓版本、本地 `path`、远程 `git`。
- `[test-dependencies]` 格式同 `[dependencies]`，只应被 `xxx_test.cj` 测试文件使用。
- `[script-dependencies]` 格式同 `[dependencies]`，只应被构建脚本使用；源代码和测试代码不能直接使用仅配置在 `script-dependencies` 的模块。
- `[replace]` 只替换间接依赖的同名模块，不要把它当作普通直接依赖。
- 有组织名的中心仓依赖 key 使用字符串形式，例如 `"org::boo" = "2.0.0"`。
- target 专用依赖位于 `[target.<target-name>.dependencies]`、`[target.<target-name>.test-dependencies]` 或相关 debug/release 子表；如果用户指定 `--target`，必须把 target 专用依赖纳入判断。
- 二进制依赖的 `package-option` key 如果包含 `.`，必须用引号包住，例如 `"pro0.xoo" = "./test/pro0/pro0.xoo.cjo"`。

## 推荐命令策略

`cjpm build` 执行前会检查依赖项，足以覆盖依赖顺序、缺失依赖和循环依赖这类构建前问题。

静态预检后，优先执行用户最终需要的命令。如果任务目标是确认能否编译，执行：

```bash
cjpm build -V
```

使用 `-V` 是为了看到每个包对应的 `cjc` 命令、`-p` 源码路径、`--import-path` 和输出产物，从而确认包编译顺序与预期一致。

工作空间中需要指定成员时，直接在最终命令上加 `-m <member>`：

```bash
cjpm build -m <member> -V
```

涉及 target 专用依赖时，直接在最终命令上加 `--target <target-name>`：

```bash
cjpm build --target <target-name> -V
```

如果用户最终需要运行测试，且静态预检没有发现明显包管理问题，可以直接执行：

```bash
cjpm test
```

## 常见诊断

`no '.cj' file`：

- 根因通常是某个父包目录没有直接 `.cj` 文件，导致它及子包不被扫描。
- 修复方式是补齐父包目录中的包声明文件，或调整目录结构让每一级有效包都直接包含 `.cj` 文件。

`cyclic dependency`：

- 先按报错路径逐个定位对应包目录中的 `import`。
- 删除未使用导入；若确有功能循环，优先抽出公共定义到更底层包，或合并强耦合包。
- 不要通过新增反向 `public import` 掩盖循环。

`can not find the following dependencies`：

- 先确认源码 import 的 root 包是否在 `[dependencies]`、`[test-dependencies]`、target 专用依赖或二进制依赖中可见。
- 确认本地 `path` 指向包含 `cjpm.toml` 的模块目录。
- 确认组织名是否一致：配置了 `organization = "org"` 的模块应通过 `org::module` 形式声明和导入。

包声明位置错误：

- 将 `package` 或带修饰符的 `package` 移到非空非注释首行。
- `import` 放在 package 后，其他声明前。

导入冲突或歧义：

- 使用 `import package.name as Alias` 为声明重命名。
- 使用 `import package as pkgAlias` 把包作为命名空间导入。
- 避免子包名与当前包顶层声明同名。

## 输出要求

当使用本 skill 完成预检时，向用户报告：

- 入口 `cjpm.toml` 路径、项目形态、模块名、组织名和源码根目录。
- 检查过的包目录数量、发现的无效源码包目录、包声明不一致文件、import 语法或位置问题。
- 执行过的 cjpm 命令及结果；如果只执行了 `cjpm build -V` 或 `cjpm test`，说明 build/test 已覆盖依赖检查。
- 若未执行某个命令，说明原因和剩余风险。
- 若提出修复，说明改动范围，并优先给出最小变更。

## 资料依据

- `cangjie_docs/docs/dev-guide/source_zh_cn/package/package_module_management.md`
- `cangjie_docs/docs/dev-guide/source_zh_cn/package/package_name.md`
- `cangjie_docs/docs/dev-guide/source_zh_cn/package/import.md`
- `cangjie_docs/docs/dev-guide/source_zh_cn/package/toplevel_access.md`
- `cangjie_docs/docs/dev-guide/source_zh_cn/compile_and_build/cjpm_usage.md`
- `cangjie_docs/docs/tools/source_zh_cn/cmd-tools/cjpm_manual.md`
