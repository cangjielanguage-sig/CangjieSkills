# Cangjie Skills

## 通用程序开发 Skills

**Common** 目录下提供了仓颉通用程序开发 Skills，并给出了基于 OpenCode 的项目模板，如果您使用其他 AI 开发工具，可以提取 `.opencode` 目录下的 `skills`，按其他工具要求部署使用。

**示例**：使用 OpenCode + GLM5 开发仓颉子集解释器，生成 LuaVM 字节码并执行：

![运行效果.png](https://raw.gitcode.com/user-images/assets/9193544/b90baedb-c7e8-474e-b18a-70c0aacc4454/运行效果.png '运行效果.png')

![glm5-初始过程.png](https://raw.gitcode.com/user-images/assets/9193544/1f6e4e6d-7b38-4893-8abe-c78ddd0574e2/glm5-初始过程.png 'glm5-初始过程.png')

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
