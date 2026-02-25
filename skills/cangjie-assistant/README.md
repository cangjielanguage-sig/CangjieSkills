# Cangjie Assistant - HarmonyOS Next 开发助手

这是一个为 **HarmonyOS Next + 仓颉(Cangjie)** 开发设计的 Claude Code 技能，提供智能的三级知识检索策略，帮助开发者高效开发鸿蒙应用。

首次使用要提问后要等待1-2分钟用于构建本地文档库和向量数据库。

## 功能特点

- **智能三级检索**: L0 需求分析 → L1 RAG 查询 → L3 本地文档搜索
- **精准技术分解**: 将业务需求自动拆解为技术组件和实现步骤
- **本地优先**: 优先使用离线的官方文档，加速开发流程
- **构建错误处理**: Evolution.md 记录历史问题，避免重复踩坑
- **即插即用**: 可轻松复制到其他项目复用

## 快速使用

### 前置要求

在开始使用前，请确保：
1. ✅ Python 3.8+ 已安装
2. ✅ Python 包已安装: `pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv`
3. ✅ API 密钥配置到 `.env` 文件
3. ✅ build.ps1根据自己DevEco Studio实际安装位置替换

### 安装到项目
复制技能目录到你的项目："项目根目录下	.claude/skills/<skill-name>/SKILL.md	仅此项目"

```bash
# Windows (PowerShell)
mkdir -p .claude\skills
xcopy /E /I /Y cangjie-assistant .claude\skills\cangjie-assistant

# Linux/macOS
mkdir -p .claude/skills
cp -r cangjie-assistant .claude\skills\cangjie-assistant
```

### 首次使用

首次运行时，技能会自动初始化：
- 如果有已解压的文件夹 → 直接使用
- 如果只有压缩包 → 自动解压
- 如果都没有 → 自动下载并构建

无需手动操作，直接在 Claude Code 中对话即可。

开始使用：
```bash
# 直接在 Claude Code 中对话
/cangjie-assistant 如何创建 List 组件？

# 或让 Claude 自动识别
帮我创建一个登录页面
```

## 文件结构

### 技能目录结构

```
cangjie-assistant/
├── SKILL.md                      # 主技能文件 (必需)
├── skill.md                      # 详细技能配置和说明
├── template.md                   # 查询和构建模板
├── README.md                     # 本文件
├── SETUP.md                      # 安装指南
├── QUICKREF.md                   # 快捷参考
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
    ├── build-template.ps1       # 构建脚本模板
    ├── build.ps1                # 构建脚本 (已同步到项目)
    ├── .env                     # API 配置文件
    ├── .env.example            # API 配置模板
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

### 安装后项目结构

```
your-project/
├── .claude/
│   └── skills/
│       └── cangjie-assistant/     # 技能目录
├── entry/
│   └── src/main/cangjie/
│       └── index.cj               # 仓颉源码
└── CLAUDE.md                       # 项目说明文件
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
    └─ 技术关键词细化 → 导包→初始化→使用
    ↓
Phase 1 (L1): RAG 快速检索
    └─ 按"导包→初始化→使用"维度精准查询
    ↓
    ├─ ✅ 完整结果 → 编码
    └─ ❌ 无结果 → Phase 3
    ↓
Phase 2 (L3): 本地文档搜索
    ├─ UI 组件问题 → hm-docs/ui-dev/
    ├─ 标准库问题 → hm-docs/stdlib/
    ├─ 扩展库问题 → hm-docs/stdx/
    └─ 语法问题 → hm-docs/syntax/
```

## 验证安装

检查环境是否配置正确：

```bash
# 1. 检查 Python
python --version

# 2. 检查 Python 包
python -c "import langchain_chroma, langchain_openai, jieba, dotenv"

# 3. 检查 .env 配置
cat .claude/skills/cangjie-assistant/scripts/.env

# 4. 检查文档目录
ls .claude/skills/cangjie-assistant/scripts/hm-docs/

# 5. 检查 RAG 数据库
ls .claude/skills/cangjie-assistant/scripts/chroma_db/
```

**Windows PowerShell 验证：**
```powershell
# 检查 Python
python --version

# 检查 Python 包
python -c "import langchain_chroma, langchain_openai, jieba, dotenv"

# 检查目录
Test-Path .claude\skills\cangjie-assistant\scripts\hm-docs\
Test-Path .claude\skills\cangjie-assistant\scripts\chroma_db\

# 检查配置文件
Get-Content .claude\skills\cangjie-assistant\scripts\.env
```

## 依赖要求

### 必需

1. **Claude Code** - Claude 代码助手 (必需)
2. **Python 3.x** - 用于 L1 RAG 查询 (必需)
3. **本地文档** `hm-docs/` 目录 - 包含鸿蒙官方文档 (必需)

### Python 包安装

L1 RAG 查询需要以下 Python 包：

```bash
pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv
```

**详细安装说明：**
- `langchain-chroma` - 向量数据库
- `langchain-openai` - OpenAI 接口支持
- `langchain-community` - 社区扩展
- `jieba` - 中文分词
- `python-dotenv` - 环境变量管理

**验证安装：**
```bash
python -c "import langchain_chroma, langchain_openai, jieba, dotenv; print('所有包安装成功')"
```

### 获取 API 密钥

L1 RAG 查询需要嵌入模型的 API 支持：

1. **硅基流动 SiliconFlow** (推荐 - 免费额度)
   - 访问: https://cloud.siliconflow.cn/
   - 注册并获取 API Key
   - 支持 Qwen3-Embedding-8B 等嵌入模型

2. **其他兼容 API 提供商**
   - OpenAI (需付费)
   - 兼容 OpenAI 接口的服务

### 可选依赖

- **DevEco Studio** - HarmonyOS 官方 IDE (用于编译和调试)
- **Node.js** - 某些构建工具需要

## 配置说明

### API 配置 (.env)

使用 L1 RAG 查询功能时，需要在 `.claude/skills/cangjie-assistant/scripts/.env` 文件中配置 API 密钥：

```bash
# API 密钥 (必需)
SILICONFLOW_API_KEY=your_api_key_here

# API 基础 URL (可选，默认硅基流动)
SILICONFLOW_API_BASE_URL=https://api.siliconflow.cn/v1

# 嵌入模型名称 (可选)
SILICONFLOW_EMBEDDING_MODEL=Qwen/Qwen3-Embedding-8B
```

**首次设置步骤：**

#### Linux/macOS
```bash
# 1. 复制模板文件
cd .claude/skills/cangjie-assistant/scripts/
cp .env.example .env

# 2. 编辑配置文件
nano .env
# 或
vim .env

# 3. 填入你的 API 密钥
SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxxx

# 4. 保存并退出
```

#### Windows PowerShell
```powershell
# 1. 进入 scripts 目录
cd .claude\skills\cangjie-assistant\scripts\

# 2. 复制模板文件
Copy-Item .env.example .env

# 3. 编辑配置文件
notepad .env
# 或使用 VS Code
code .env

# 4. 填入你的 API 密钥并保存
```

## 使用示例

### 示例 1: UI 组件开发

```bash
/cangjie-assistant 创建一个商品列表页面
```

技能会自动：
1. 分析出需要 List, Image, Text, Button 组件
2. 分别查询每个组件的导包、初始化、使用
3. 返回完整的代码示例

### 示例 2: 构建错误处理

```bash
/cangjie-assistant 构建失败，提示 undefined symbol
```

技能会：
1. 检查 Evolution.md 是否有相同问题
2. 如果没有，搜索本地文档中的 API 定义
3. 返回解决方案
4. 提示更新 Evolution.md

### 示例 3: API 查询

```bash
/cangjie-assistant 如何使用 HTTP 客户端？
```

技能会：
1. 定位到 `hm-docs/stdx/libs_stdx/net/http/`
2. 查找 HttpClient 相关文档
3. 返回完整的 API 使用示例

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

A: 这是正常的，请继续进入 L3 本地文档搜索。L3 是更权威的官方文档来源。

### Q: 如何添加新的本地文档？

A: 将文档放在 `hm-docs/` 目录下对应的位置：
- UI 文档 → `hm-docs/ui-dev/`
- 标准库 → `hm-docs/stdlib/`
- 扩展库 → `hm-docs/stdx/`

### Q: 技能在其他 IDE 中可用吗？

A: 这是 Claude Code 专用技能，需要在 Claude Code 环境中使用。

### Q: 如何禁用自动触发？

A: 在 SKILL.md 中添加 `disable-model-invocation: true`，然后只能手动调用 `/cangjie-assistant`。

### Q: Python 提示 "ModuleNotFoundError"？

A: 安装必需的 Python 包：
```bash
pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv
```

### Q: 首次查询报错 "RAG 数据库未初始化"？

A: 首次运行 L1 查询时会自动初始化，或者手动运行：
```bash
cd .claude/skills/cangjie-assistant/scripts
python Database-Builder.py
```

### Q: Windows 环境下脚本无法执行？

A: 可能是 PowerShell 执行策略问题，运行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q: API 密钥从哪里获取？

A: 推荐使用硅基流动 SiliconFlow：
1. 访问 https://cloud.siliconflow.cn/
2. 注册并登录
3. 进入「API Keys」页面
4. 创建新的 API Key
5. 复制 API Key 到 `.env` 文件

### Q: 离线使用需要准备什么？

A: 准备以下内容即可离线使用：
- `hm-docs/` 目录（完整文档）
- `chroma_db/` 目录（RAG 数据库）
- `.env` 文件（如果不使用 L1 查询，可跳过）

### Q: 如何更新本地文档？

A: 运行文档下载脚本：
```bash
cd .claude/skills/cangjie-assistant/scripts
python download_hm_docs.py
```

### Q: Evolution.md 是什么？

A: Evolution.md 记录项目中遇到的构建错误和解决方案，避免重复踩坑。每次构建成功后，技能会提示更新此文件。

## 故障排除

### 问题 1: 首次使用无响应

**症状**: 调用技能后没有任何返回

**排查步骤**:
```bash
# 1. 检查 Python
python --version

# 2. 检查 Python 包
python -c "import langchain_chroma, langchain_openai, jieba, dotenv; print('OK')"

# 3. 检查 .env 配置
cat .claude/skills/cangjie-assistant/scripts/.env

# 4. 检查文档目录
ls .claude/skills/cangjie-assistant/scripts/hm-docs/
```

### 问题 2: API 调用失败

**症状**: L1 查询提示 API 错误

**解决方案**:
1. 检查 `.env` 中的 API 密钥是否正确
2. 确认 API 密钥是否有效且未过期
3. 检查网络连接
4. 验证 API 基础 URL 是否正确

### 问题 3: 文档搜索无结果

**症状**: L3 搜索找不到任何相关内容

**解决方案**:
```bash
# 1. 检查文档目录
ls .claude/skills/cangjie-assistant/scripts/hm-docs/

# 2. 检查文档是否完整
tree .claude/skills/cangjie-assistant/scripts/hm-docs/

# 3. 如文档缺失，重新下载
cd .claude/skills/cangjie-assistant/scripts
python download_hm_docs.py

# 4. 尝试更宽泛的关键词搜索
```

### 问题 4: Windows 脚本执行权限错误

**症状**: "Permission denied" 或 "无法加载文件"

**解决方案**:
```powershell
# 修改 PowerShell 执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 问题 5: 构建脚本找不到

**症状**: `.\build.ps1` 提示命令不存在

**解决方案**:
```bash
# 1. 确认在正确的工作目录
cd 你的项目目录

# 2. 检查构建脚本是否存在
ls build.ps1

# 3. 如果不存在，从技能模板复制
cp .claude/skills/cangjie-assistant/scripts/build-template.ps1 build.ps1
```

### 问题 6: Python 包冲突

**症状**: 导入错误或版本不兼容

**解决方案**:
```bash
# 升级所有包
pip install --upgrade langchain-chroma langchain-openai langchain-community

# 或使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows
pip install langchain-chroma langchain-openai langchain-community jieba python-dotenv
```

## 技能更新

### 更新依赖

```bash
cd .claude/skills/cangjie-assistant/scripts
pip install --upgrade langchain-chroma langchain-openai langchain-community
```

### 更新文档

```bash
cd .claude/skills/cangjie-assistant/scripts
python download_hm_docs.py
python Database-Builder.py
```

### 同步到其他项目

```bash
# 将更新后的技能复制到其他项目
cp -r .claude/skills/cangjie-assistant /path/to/other-project/.claude/skills/
```

## 相关链接

### 官方资源
- [Claude Code Skills 文档](https://code.claude.com/docs/zh-CN/skills)
- [仓颉语言官方文档](https://gitcode.com/Cangjie)
- [HarmonyOS 开发者文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ide-V5)
- [HarmonyOS Next SDK 下载](https://developer.huawei.com/consumer/cn/download/)

### 文档索引
- [L0 需求分析示例](./examples/l0-analysis.md)
- [L1 RAG 查询示例](./examples/l1-query.md)
- [L3 本地文档搜索示例](./examples/l3-search.md)
- [快速参考指南](./QUICKREF.md)
- [完整安装指南](./SETUP.md)

## 支持与反馈

- **问题反馈**: [提交 Issue](https://github.com/your-repo/issues)
- **功能建议**: [提交 Feature Request](https://github.com/your-repo/issues)
- **文档改进**: 欢迎提交 PR 改进文档

## 版本历史

- **v1.2.0** (2025-02-25)
  - 新增 Evolution.md 自动记录功能
  - 优化构建错误处理流程
  - 添加 `layoutWeight` 布局指南

- **v1.1.0** (2025-02-24)
  - 优化 L3 文档搜索策略
  - 新增自动初始化功能
  - 完善 Windows 环境支持

- **v1.0.0** (2025-02-20)
  - 初始版本发布
  - 支持三级知识检索
  - L1 RAG 集成
