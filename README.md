# CangjieSkills Release Bundle

CangjieSkills 是面向仓颉语言与 HarmonyOS 仓颉应用开发的 Skills 发行包仓库。当前稳定发行标签为 `release-1.0.1`，根目录下按使用场景拆分为 4 个可独立安装的 bundle。

当前仓库地址：<https://gitcode.com/Cangjie-SIG/CangjieSkills>

## 快速安装

通过 `npx skills add` 从 GitCode 标签下载并安装。普通用户建议按场景只安装一个主包；维护人员可在主包之外额外安装维护包。

```bash
# 语言基础场景：仓颉语法、标准库、扩展库、原始文档兜底
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-language-basic -y

# HarmonyOS 仓颉应用开发场景：推荐给普通 HarmonyOS/Cangjie App 开发者
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos -y

# HarmonyOS 兼容包开发场景：推荐给普通 HarmonyOS/Cangjie App 开发者
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos-compatible -y

# 维护与增强场景：检索索引维护、知识图谱、项目经验沉淀，不建议普通用户默认安装
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos-maintenance -y
```

如果已经克隆了本仓库，也可以从本地目录安装：

```bash
npx skills add ./cangjie-language-basic -y
npx skills add ./cangjie-harmonyos -y
npx skills add ./cangjie-harmonyos-compatible -y
npx skills add ./cangjie-harmonyos-maintenance -y
```

## Bundle 选择

| Bundle | 适用对象 | 说明 |
| --- | --- | --- |
| `cangjie-language-basic` | 仓颉语言学习、基础编码、标准库/扩展库速查 | 只包含语言基础能力，体积和触发面更克制，适合作为所有场景的基础包 |
| `cangjie-harmonyos` | HarmonyOS 仓颉应用普通开发者 | 覆盖需求分析、项目初始化、文档检索、构建、诊断、stdx 配置、ArkTS 互操作，并包含语言基础 Skills |
| `cangjie-harmonyos-compatible` | HarmonyOS 仓颉应用普通开发者 | 覆盖需求分析、项目初始化、文档检索、构建、诊断、stdx 配置、ArkTS 互操作，并包含语言基础 Skills |
| `cangjie-harmonyos-maintenance` | Skill 维护者、检索索引维护者、团队知识沉淀负责人 | 维护和增强能力包，不建议默认给普通终端用户安装 |

## 如何使用

安装完成后，在支持 Skills 的 Agent 中直接用自然语言描述任务即可。Agent 会根据任务触发对应 Skill，不需要用户手动指定脚本路径。

典型提问示例：

```text
帮我解释仓颉 match 表达式的常见写法，并给一个 enum 示例。
帮我查一下 stdx.json 解析对象数组应该怎么写。
帮我初始化一个 HarmonyOS 仓颉应用，并生成基础页面。
这个 HarmonyOS 仓颉项目构建失败了，请根据日志定位原因。
帮我排查应用白屏，结合截图、控件树和 hilog 给诊断结论。
帮我检索 ArkTS 调用仓颉函数的推荐互操作方式。
维护检索索引，跑一次发布前回归评测。
```

## 语言基础场景

Bundle：`cangjie-language-basic`

| Skill | package 定位 | 说明 |
| --- | --- | --- |
| `cangjie-lang-features` | `cj-lang-core`，语言核心 Hub | 语法、类型系统、函数、泛型、模式匹配、并发、宏等语言核心问题入口 |
| `cangjie-std` | `cj-std`，标准库 Hub | 标准库速查入口，覆盖集合、IO、时间、正则、测试等常用模块 |
| `cangjie-stdx` | `cj-stdx`，扩展库 Hub | 扩展库速查入口，覆盖 JSON、日志、网络、TLS、压缩、序列化等 |
| `cangjie-original-docs` | `cj-original-docs`，原始文档兜底 | 当 Hub 型 Skill 命中不足时，回到原始文档子域检索和核对 |

安装命令：

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-language-basic -y
```

## HarmonyOS 开发场景

Bundle：`cangjie-harmonyos`

| Skill | package 定位 | 说明 |
| --- | --- | --- |
| `harmonyos-app-agent-development` | `cj-hmos-app-agent` | HarmonyOS 仓颉 App 自主开发总入口，编排需求、检索、实现、构建、诊断和沉淀 |
| `harmonyos-requirements` | `cj-hmos-requirements` | 需求分析、验收标准、页面/能力拆分 |
| `harmonyos-project-init` | `cj-hmos-project` | 项目初始化、模板创建、目录与配置生成 |
| `cangjie-harmonyos-doc-search` | `cj-hmos-doc-search` | HarmonyOS 仓颉文档检索核心能力，覆盖任务、API、示例、文档卡片 |
| `harmonyos-build` | `cj-hmos-build` | 构建执行、日志分析、失败排查 |
| `harmonyos-app-diagnose` | `cj-hmos-diagnose` | 截图、控件树、hilog、运行态诊断 |
| `harmonyos-stdx` | `cj-hmos-stdx-config` | HarmonyOS 工程中的 stdx 依赖配置 |
| `cangjie-arkts-interop` | `cj-interop` | 仓颉与 ArkTS 互操作，覆盖声明式互操作、互操作库、混合 UI |
| `cangjie-lang-features` | `cj-lang-core` | HarmonyOS 开发中遇到的仓颉语言问题入口 |
| `cangjie-std` | `cj-std` | HarmonyOS 开发中遇到的标准库问题入口 |
| `cangjie-stdx` | `cj-stdx` | HarmonyOS 开发中遇到的扩展库问题入口 |
| `cangjie-original-docs` | `cj-original-docs` | 原始仓颉文档兜底 |

安装命令：

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos -y
```

## HarmonyOS 兼容包开发场景

Bundle：`cangjie-harmonyos-compatible`

该包面向 HarmonyOS 仓颉应用开发场景，覆盖需求分析、项目初始化、文档检索、构建、诊断、stdx 配置、ArkTS 互操作，并包含语言基础 Skills。

| Skill | package 定位 | 说明 |
| --- | --- | --- |
| `harmonyos-requirements` | `cj-hmos-requirements` | 需求分析、验收标准、页面/能力拆分 |
| `harmonyos-project-init` | `cj-hmos-project` | 项目初始化、模板创建、目录与配置生成 |
| `cangjie-harmonyos-doc-search` | `cj-hmos-doc-search` | HarmonyOS 仓颉文档检索核心能力，覆盖任务、API、示例、文档卡片 |
| `harmonyos-build` | `cj-hmos-build` | 构建、日志、失败排查 |
| `harmonyos-app-diagnose` | `cj-hmos-diagnose` | 截图、控件树、hilog、运行诊断 |
| `harmonyos-stdx` | `cj-hmos-stdx-config` | HarmonyOS stdx 依赖配置 |
| `cangjie-arkts-interop` | `cj-interop` | 仓颉与 ArkTS 互操作，覆盖声明式互操作、互操作库、混合 UI |
| `cangjie-lang-features` | `cj-lang-core` | HarmonyOS 开发中遇到的仓颉语言问题入口 |
| `cangjie-std` | `cj-std` | 标准库速查入口 |
| `cangjie-stdx` | `cj-stdx` | 扩展库速查入口 |
| `cangjie-original-docs` | `cj-original-docs` | 原始文档兜底 |

安装命令：

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos-compatible -y
```

## 维护与增强场景

Bundle：`cangjie-harmonyos-maintenance`

| Skill | package 定位 | 说明 |
| --- | --- | --- |
| `cangjie-harmonyos-doc-search-maintenance` | `cj-hmos-doc-search-maintenance` | 文档检索索引维护、评测、回归、语料扩展，不默认给普通用户安装 |
| `knowledge-graph-template` | `cj-hmos-knowledge-graph` | 知识图谱增强、子图构建、语义查询增强 |
| `harmonyos-evolution` | `cj-hmos-evolution` | 项目经验沉淀，适合团队长期维护 HarmonyOS 仓颉项目 |

安装命令：

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills/-/tree/release-1.0.1/cangjie-harmonyos-maintenance -y
```

## 发行文件

每个 bundle 目录都包含以下发行元数据：

| 文件 | 说明 |
| --- | --- |
| `distribution.json` | bundle 名称、版本、package 列表、Skill 到 package 的映射 |
| `release-manifest.json` | 发布清单、文件摘要、生成产物记录 |
| `release-check.json` | 发布检查结果 |

当前发布标签：`release-1.0.1`。
