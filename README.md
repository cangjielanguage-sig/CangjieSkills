# Cangjie Skills

> 本项目近期快速迭代中，欢迎持续关注和参与共建，期待您的 PR

[Release](https://gitcode.com/Cangjie-SIG/CangjieSkills/releases/1.0.5.1) 板块提供了一个仓颉定制版 OpenCode（Beta），接入仓颉 LSP 和 cjfmt，并集成 cangjie-tree-sitter.wasm 支持仓颉语法高亮。使用前请确保环境中可正常引用仓颉工具链，OpenCode 会适时引用 LSP 和 cjfmt。

- OpenCode for Cangjie：https://github.com/SunriseSummer/opencode
- TreeSitter for Cangjie：https://github.com/SunriseSummer/CangjieTreeSitter

![2026-03-09 00 35 41.png](https://raw.gitcode.com/user-images/assets/9193544/088b512b-e8b2-4d5c-a2dd-3d53b8e4a0b9/2026-03-09_00_35_41.png '2026-03-09 00 35 41.png')

## 通用程序开发 Skills

**Common** 目录下提供了仓颉通用程序开发 Skills，并给出了基于 OpenCode 的项目模板，如果您使用其他 AI 开发工具，可以提取 `.opencode` 目录下的 `skills`，按其他工具要求部署使用。

这套 Skills 可支撑 AI 开发工具从零创建开发仓颉项目，包括项目配置、开发、构建、运行、单元测试等，包括 stdx、macro、CFFI 等场景的自动处理。

**注意事项**

- 请在全局环境配置好[仓颉通用版本工具链](https://cangjie-lang.cn/download/)，全局可引用 cjpm 等工具。
- 如果项目需要使用 stdx，鉴于一些 AI 开发工具未启用网络下载功能，因此建议您手动下载所需版本的 stdx 并解压到项目根目录，AI 会根据 Skills 指导自动配置。


**示例**

1、使用 OpenCode/GLM5 开发的 [AI 聊天工具](https://gitcode.com/Cangjie/Cangjie-Examples/tree/1.0.0/AIChatPro)，支持多模型切换、JSON 配置文件、流式请求、控流打字机效果、对话上下文等功能。

![完成开发.png](https://raw.gitcode.com/user-images/assets/9193544/d5824ec8-8fa6-4841-8a4d-10d282324109/完成开发.png '完成开发.png')

![运行效果.png](https://raw.gitcode.com/user-images/assets/9193544/65bf2447-a413-4046-99cd-f6cefc947dd4/运行效果.png '运行效果.png')

2、使用 OpenCode/GLM5 + Claude Opus 4.6 开发的[仓颉语言子集解释器](https://gitcode.com/Cangjie/Cangjie-Examples/tree/1.0.0/CangjieLua)，生成 LuaVM 字节码并执行。

![glm5-初始过程.png](https://raw.gitcode.com/user-images/assets/9193544/1f6e4e6d-7b38-4893-8abe-c78ddd0574e2/glm5-初始过程.png 'glm5-初始过程.png')

![image.png](https://raw.gitcode.com/user-images/assets/9193544/36fb1954-6d3c-4eb7-b54f-acf6d5f670e0/image.png 'image.png')

![798bcbe3952cb5113338efd234771581.png](https://raw.gitcode.com/user-images/assets/9193544/6b2ad68a-a2e6-448b-b581-14a79f18763e/798bcbe3952cb5113338efd234771581.png '798bcbe3952cb5113338efd234771581.png')

## 鸿蒙应用开发 Skills

**HarmonyOS** 目录下提供了仓颉鸿蒙应用开发 Skills。

### cangjie-dev-harmonyos

本 Skill 赋能仓颉鸿蒙应用开发，涵盖需求分析、文档检索（文本/向量混合检索，分级检索）、本地构建、错误排查、经验沉淀等功能。

三级知识检索流程：
-  L0：先帮你把“业务需求”拆成具体技术点（UI、API、数据结构、交互等）
-  L1：用 RAG知识库+混合搜索精准返回项目所需知识点和代码片段
-  L2：必要时直接查本地 hm-docs 完整文档

构建与报错闭环：通过 scripts/build.ps1 触发完整构建流程，拿到详细错误后按“先查 Evolution.md → 再查L3文档”顺序指导你修复，并在构建成功后要求把关键问题整理进 Evolution.md。

**前置条件**
- 安装 DevEco Studio 及仓颉插件
- 当前仅支持 6.0.2 版本应用开发

**使用步骤**
1. 首次使用前，请打开 `cangjie-dev-harmonyos/scripts/.env` 文件，配置 DevEco 安装路径和词嵌入模型服务的 API KEY（用于 L1 向量搜索）
2. 在鸿蒙应用项目目录，根据所用的 AI 工具部署此 Skill，如 `MyApplication/.opencode/skills/cangjie-dev-harmonyos`（使用 OpenCode）
3. 在 AI 工具中提出开发需求，例如：“用仓颉语言写一个计算器应用”

**示例**：使用 Claude Code + GLM4.7 开发一个计算器应用

![微信图片_20260225115922_232_63.png](https://raw.gitcode.com/user-images/assets/9193544/ad4b63c4-f26d-4fe4-a33e-dfded2054010/微信图片_20260225115922_232_63.png '微信图片_20260225115922_232_63.png')
