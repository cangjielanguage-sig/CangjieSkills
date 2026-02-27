# Cangjie-dev-HarmonyOS

🚀 专为 HarmonyOS Next 与 仓颉 (Cangjie) 语言打造的 Claude Code 智能工作流引擎。

Cangjie-dev-HarmonyOS 是一个支持即插即用的 Claude Code Skill。它通过构建**三级级联检索架构**，大幅优化大语言模型在仓颉开发中常常面临的 API 幻觉与语法滞后问题，并深度集成了从代码编写、本地构建到错误沉淀的完整闭环。

## ✨ 核心特性
一、🧠 三级智能级联检索 (L0 -> L1 -> L3)

L0 需求降维: 自动将模糊的业务需求拆解为“界面设计、关键组件”的精准技术路径。

L1 RAG 向量检索 (可选): 通过关键词、向量数据库混合搜索，快速返回所需知识点。默认禁用，需配置 API Key 启用。

L3 离线文档溯源: 无缝接入本地官方 hm-docs，提供权威海量的 API 参考与 UI 开发规范支持。

二、🔄 自动化构建闭环

直接接管项目根目录的 build.ps1，支持在 Claude 对话框内一键编译。

三、🧬 错误自我演进 (Evolution)

自动追踪并分析构建失败日志，将重难点解决方案沉淀至 Evolution.md，打造你的专属知识库，拒绝重复踩坑。

四、📦 极简跨项目复用

完全解耦的设计，只需将 .claude/skills/cangjie-dev-harmonyos 目录拖入新项目即可激活。

## 快速使用

### 1、前置要求

在开始使用前，请确保：
1. ✅ Python 3.8+ 已安装
2. ✅ Python 包已安装: `pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv`

### 2、安装到项目
将本技能目录复制到你的目标项目下

### 3、基础配置
1. ✅ **DevEco Studio 路径配置**：在 `.env` 文件中设置 `DEVECO_HOME` 为你的 DevEco Studio 安装路径
2. ✅ **L1 RAG 功能（可选）**：如需启用向量搜索，将 `.env` 文件中的 `SILICONFLOW_API_KEY` 从默认值 `YOUR_API_KEY` 替换为有效的 API Key

🧩 架构与工作流
用户需求 ➔ L0 分析(技术细化) ➔ L1 RAG(精准片段) ➔ (若不足) ➔ L3 Local(全量权威文档) ➔ 编写代码 ➔ 构建排错 ➔ 记录 Evolution.md

### 4、首次使用

在首次启动开发时，系统会自动进行数据库初始化（预计耗时约 1 分钟）。资源加载策略如下：

1. 检测到已解压目录：直接读取并使用

2. 仅检测到本地压缩包：自动执行解压操作

3. 未检测到本地资源：自动触发下载并完成构建

4. 全程无需任何手动配置，您只需在 Claude Code 中直接对话即可。


## 文件结构

### 技能目录结构

```
cangjie-dev-harmonyos/
├── SKILL.md                      # 主技能文件 (必需)
├── README.md                     # 本文件
├── Evolution.md                  # 构建重难点记录 (随项目迁移)
├── examples/
│   ├── l0-analysis.md           # L0 需求分析示例
│   ├── l1-query.md              # L1 RAG 查询示例
│   └── l3-search.md             # L3 本地文档搜索示例
└── scripts/                      # 核心脚本目录
    ├── ask_cangjie.py           # L1 RAG 查询脚本
    ├── cangjie_retriever.py     # 混合检索器
    ├── Database-Builder.py     # RAG 数据库构建脚本
    ├── download_hm_docs.py     # 官方文档下载脚本
    ├── build.ps1                # 构建脚本 (已同步到项目)
    ├── .env                     # API 配置文件
    ├── chroma_db.zip            # 向量数据库压缩包（可选）
    ├── hm-docs.zip              # 官方文档压缩包（可选）
    ├── chroma_db/               # RAG 向量数据库（解压或下载后）
    │   └── ...
    └── hm-docs/                # 本地官方文档（解压或下载后）
        ├── ui-dev/             # UI 开发文档
        ├── stdx/               # 标准扩展库文档
        ├── syntax/             # 语法和语言特性文档
        └── stdlib/             # 标准库 API 文档
```

**注意**：所有查询脚本、文档和数据库都包含在技能的 `scripts/` 目录内，技能自包含，无需额外创建工作流目录。

## 工作流说明

```
用户需求
    ↓
Phase 0 (L0): 需求技术化分析
    ├─ 界面分析 → 识别 UI 组件
    ├─ 数据分析 → 识别数据结构
    ├─ 交互分析 → 识别用户交互
    └─ 技术关键词
    ↓
Phase 1 (L1): RAG 快速检索 (可选)
    └─ 按"关键词"精准查询 (需配置 API Key)
    ↓
    ├─ ✅ 完整结果 → 编码
    ├─ ❌ 无结果 → Phase 2
    └─ 🔒 未启用 → 直接 Phase 2
    ↓
Phase 2 (L3): 本地文档搜索 (免费)
    ├─ UI 组件问题 → hm-docs/ui-dev/
    ├─ 标准库问题 → hm-docs/stdlib/
    ├─ 扩展库问题 → hm-docs/stdx/
    └─ 语法问题 → hm-docs/syntax/
```

## 使用示例

### 示例 1: UI 组件开发

```bash
/cangjie-dev-harmonyos 创建一个商品列表页面
```

技能会自动：
1. 分析出需要 List, Image, Text, Button 组件
2. 分别查询每个组件的关键词
3. 返回完整的代码示例

### 示例 2: 构建错误处理

```bash
/cangjie-dev-harmonyos 构建失败，提示 undefined symbol
```

技能会：
1. 检查 Evolution.md 是否有相同问题
2. 如果没有，搜索本地文档中的 API 定义
3. 返回解决方案
4. 提示更新 Evolution.md


## 依赖要求

### 必需

1. **Claude Code** - Claude 代码助手 (必需)
2. **Python 3.x** - 用于 L1 RAG 查询 (必需)
3. **本地文档** `hm-docs/` 目录 - 包含鸿蒙官方文档 (必需)

### 1、Python 包安装

L1 RAG 查询需要以下 Python 包：

```bash
pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv
```

### 2、获取 API 密钥（可选）

**注意**：L1 RAG 功能是可选的。默认情况下系统使用免费的 L3 本地文档搜索，已能满足大部分开发需求。

如需启用 L1 RAG 向量搜索功能：

1. **硅基流动 SiliconFlow** (推荐 - 免费额度)
   - 访问: https://cloud.siliconflow.cn/
   - 注册并获取 API Key
   - 支持 Qwen3-Embedding-8B 等嵌入模型

2. **其他兼容 API 提供商**
   - OpenAI (需付费)
   - 兼容 OpenAI 接口的服务

**启用方式**：将 `.env` 文件中的 `SILICONFLOW_API_KEY=YOUR_API_KEY` 替换为你的真实 API Key。

### 3、可选依赖

- **DevEco Studio** - HarmonyOS 官方 IDE (用于编译和调试)
- **Node.js** - 某些构建工具需要

## 构建流程

技能集成了完整的构建工作流：

```powershell
# 在 PowerShell 中执行
.\build.ps1
```

构建失败时，技能会：
1. 自动读取错误信息
2. 优先检查 Evolution.md
3. 使用 L3 搜索解决方案
4. 提示修复后重新构建

构建成功后，技能会提示更新 Evolution.md 记录本次重难点。

## 常见问题

### Q: L1 查询返回 NO_RAG_RESULT？

A: 这是正常的，有两种可能：
1. **L1 功能未启用**：`SILICONFLOW_API_KEY` 仍为默认值 `YOUR_API_KEY`，系统自动跳过 L1
2. **L1 功能已启用但无结果**：请继续进入 L3 本地文档搜索

L3 本地文档搜索是更权威的官方文档来源，完全免费且内容完整。

### Q: 首次查询报错 "RAG 数据库未初始化"？

A: 首次运行 L1 查询时会自动初始化，或者手动运行：
```bash
cd .claude/skills/cangjie-dev-harmonyos/scripts
python Database-Builder.py
```

### Q: Windows 环境下脚本无法执行？

A: 可能是 PowerShell 执行策略问题，运行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q: API 密钥从哪里获取？

A: **注意**：API 密钥是可选的，仅用于启用 L1 RAG 功能。默认使用免费的 L3 本地文档搜索。

如需启用 L1 功能，比如使用硅基流动 SiliconFlow：
1. 访问 https://cloud.siliconflow.cn/
2. 注册并登录
3. 进入「API Keys」页面
4. 创建新的 API Key
5. 将 `.env` 文件中的 `SILICONFLOW_API_KEY=YOUR_API_KEY` 替换为你的 API Key

### Q: 如何更新本地文档？

A: 运行文档下载脚本：
```bash
cd .claude/skills/cangjie-dev-harmonyos/scripts
python download_hm_docs.py
```

### Q: Evolution.md 是什么？

A: Evolution.md 记录项目中遇到的构建错误和解决方案，避免重复踩坑。每次构建成功后，技能会提示更新此文件。

## 相关链接

### 文档索引
- [L0 需求分析示例](./examples/l0-analysis.md)
- [L1 RAG 查询示例](./examples/l1-query.md)
- [L3 本地文档搜索示例](./examples/l3-search.md)
