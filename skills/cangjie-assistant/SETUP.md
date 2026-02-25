# Cangjie Assistant - 安装指南

本指南帮助你将 Cangjie Assistant 技能安装到其他 HarmonyOS Next + 仓颉开发项目中。

## 前提条件

在安装之前，确保你的环境满足以下要求：

| 条件 | 要求 | 检查命令 |
|------|------|----------|
| Python | 3.7+ | `python --version` 或 `python3 --version` |
| Claude Code | 已安装 | 在项目中运行 `/help` |
| PowerShell | 已安装 | `powershell --version` (Windows) 或 `bash --version` (WSL) |

## 快速安装

### 步骤 1: 复制技能

在目标项目根目录执行：

```bash
# 创建技能目录
mkdir -p .claude/skills

# 复制技能文件 (从源项目)
cp -r /path/to/source-project/.claude/skills/cangjie-assistant .claude/skills/
```

或者在 Windows 上：

```powershell
# 创建技能目录
New-Item -ItemType Directory -Force -Path .claude\skills

# 复制技能文件
Copy-Item -Recurse "C:\path\to\source\.claude\skills\cangjie-assistant" .claude\skills\
```

### 步骤 2: 运行初始化脚本

在项目根目录运行初始化脚本，自动创建工作流目录和必要文件：

```bash
bash .claude/skills/cangjie-assistant/scripts/setup-workflow.sh
```

此脚本会：
- 创建 `cangjie-dev-workflow/` 目录
- 复制 Python 工作流脚本（ask_cangjie.py、cangjie_retriever.py、Database-Builder.py）
- 创建 `build.ps1` 构建脚本（如不存在）
- 创建 `chroma_db/` 和 `hm-docs/` 目录
- 创建 `Evolution.md` 记录文件

### 步骤 3: 验证安装

```bash
cd .claude/skills/cangjie-assistant
bash scripts/validate-workflow.sh
```

或手动验证项目结构：

```bash
# 验证工作流文件
ls cangjie-dev-workflow/

# 验证构建脚本
ls build.ps1

# 验证必要目录
ls -la chroma_db/ hm-docs/
```

### 步骤 4: 测试技能

在 Claude Code 中运行：

```
/cangjie-assistant 帮我理解 List 组件的使用
```

## 完整安装步骤

### 步骤 1: 安装工作流脚本

```bash
# 创建工作流目录
mkdir -p cangjie-dev-workflow

# 从源项目复制脚本
cp /path/to/source/cangjie-dev-workflow/ask_cangjie.py cangjie-dev-workflow/
cp /path/to/source/cangjie-dev-workflow/Database-Builder.py cangjie-dev-workflow/
cp /path/to/source/cangjie-dev-workflow/cangjie_retriever.py cangjie-dev-workflow/
```

### 步骤 2: 安装本地文档 (可选但推荐)

你有两种选择：

**选项 A: 复制现有文档**

```bash
# 直接复制整个 hm-docs 目录
cp -r /path/to/source/hm-docs .
```

**选项 B: 下载官方文档**

访问以下官方仓库下载文档：
- UI 文档: https://gitcode.com/openharmony-sig/docs_cangjie
- 扩展库: https://gitcode.com/Cangjie/cangjie_stdx
- 语法文档: https://gitcode.com/Cangjie/cangjie_docs
- 标准库: https://gitcode.com/Cangjie/cangjie_runtime

下载后按以下结构组织：
```
hm-docs/
├── ui-dev/          # UI 开发文档
├── stdx/            # 标准扩展库
├── syntax/          # 语法特性
├── stdlib/          # 标准库 API
└── tools/           # 构建工具
```

### 步骤 3: 创建构建脚本

在项目根目录创建 `build.ps1`：

```powershell
param(
    [string]$Configuration = "Release"
)

Write-Host "开始构建 HarmonyOS Next Cangjie 项目..." -ForegroundColor Green

try {
    # 1. 安装依赖
    Write-Host "📦 安装依赖..."
    Invoke-Expression "hawk install --rebuild"

    # 2. 仓颉预编译
    Write-Host "🔨 仓颉预编译..."
    Invoke-Expression "hawk CangjiePreBuild"

    # 3. 生成资源
    Write-Host "🎨 生成资源..."
    Invoke-Expression "hawk GenerateCangjieResource"

    # 4. 编译仓颉代码
    Write-Host "⚙️  编译仓颉代码..."
    Invoke-Expression "hawk CompileCangjie"

    # 5. 编译 ArkTS
    Write-Host "🔌 编译 ArkTS..."
    Invoke-Expression "hawk CompileArkTS"

    # 6. 打包 HAP
    Write-Host "📦 打包 HAP..."
    Invoke-Expression "hawk PackageHap"

    # 7. 签名 (可选)
    Write-Host "✍️  签名..."
    Invoke-Expression "hawk SignHap"

    # 8. 组装
    Write-Host "🔧 组装..."
    Invoke-Expression "hawk assembleHap"

    Write-Host "`n🎉 BUILD SUCCESSFUL!" -ForegroundColor Green
    exit 0

} catch {
    Write-Host "`n❌ BUILD FAILED: $_" -ForegroundColor Red
    exit 1
}
```

### 步骤 4: 创建 Evolution.md

Evolution.md 应该位于 skills 目录中，这样当技能迁移到其他项目时，历史问题记录也会一起迁移。

在 `.claude/skills/cangjie-assistant/` 目录下创建 `Evolution.md`：

```markdown
# Evolution - 项目重难点记录

## 项目: [你的项目名称]
### 初始日期: YYYY-MM-DD

## 重难点记录

*(构建成功后，技能会提示在此处记录遇到的重难点)*
```

> **注意**: 首次运行 `ask_cangjie.py` 脚本时会自动创建 Evolution.md 文件。

### 步骤 5: 配置 API 密钥 (L1 查询需要)

如果需要使用 L1 RAG 查询功能，需要配置 API 密钥：

```bash
# 复制 .env.example 为 .env
cp .claude/skills/cangjie-assistant/scripts/.env.example .claude/skills/cangjie-assistant/scripts/.env

# 编辑 .env 文件，填入你的 API 密钥
# SILICONFLOW_API_KEY=your_api_key_here
```

**.env 配置项**：
- `SILICONFLOW_API_KEY`: API 密钥（必需）
- `SILICONFLOW_API_BASE_URL`: API 基础 URL（可选，默认 `https://api.siliconflow.cn/v1`）
- `SILICONFLOW_EMBEDDING_MODEL`: 嵌入模型名称（可选，默认 `Qwen/Qwen3-Embedding-8B`）

### 步骤 6: 配置 Python 环境 (L1 查询需要)

如果需要使用 L1 RAG 查询功能，安装以下 Python 包：

```bash
pip install torch sentencepiece python-dotenv langchain langchain-openai langchain-chroma jieba
```

或者使用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
pip install torch sentencepiece
```

## 目录结构验证

安装完成后，你的项目应该有以下结构：

```
your-project/
├── .claude/
│   └── skills/
│       └── cangjie-assistant/         ✅ 本技能
│           ├── SKILL.md
│           ├── template.md
│           ├── examples/
│           │   ├── l0-analysis.md
│           │   ├── l1-query.md
│           │   └── l3-search.md
│           ├── scripts/
│           │   ├── .env                ✅ API 配置文件
│           │   ├── .env.example        ✅ API 配置模板
│           │   └── validate-workflow.sh
│           ├── Evolution.md           ✅ 重难点记录（会随技能迁移）
│           └── README.md
├── cangjie-dev-workflow/              ✅ 工作流脚本
│   ├── ask_cangjie.py
│   ├── Database-Builder.py
│   └── cangjie_retriever.py
├── hm-docs/                           ✅ 本地文档 (可选)
│   ├── ui-dev/
│   ├── stdx/
│   ├── syntax/
│   └── stdlib/
├── build.ps1                          ✅ 构建脚本
├── package.json5                      # 仓颉包配置
└── entry/                             # 源代码目录
```

## 自定义配置

### 修改技能名称

编辑 `.claude/skills/cangjie-assistant/SKILL.md`：

```yaml
---
name: my-rename-skill  # 改为你的自定义名称
description: 自定义描述
---
```

修改后使用 `/my-rename-skill` 调用。

### 禁用自动触发

如果你不希望 Claude 自动使用该技能，添加 `disable-model-invocation: true`：

```yaml
---
name: cangjie-assistant
description: ...
disable-model-invocation: true  # 添加此项
---
```

### 限制工具访问

只允许特定工具：

```yaml
---
name: cangjie-assistant
description: ...
allowed-tools: Read, Grep, Glob  # 只允许读取和搜索
---
```

## 故障排除

### 问题 1: 运行 `/cangjie-assistant` 无响应

**解决方案**: 验证技能目录是否存在且包含 SKILL.md

```bash
ls .claude/skills/cangjie-assistant/
```

### 问题 2: 验证脚本报告 Python 缺失

**解决方案**: 安装 Python

- Windows: 从 https://python.org/downloads/ 下载安装
- Linux: `sudo apt install python3 python3-pip`
- Mac: `brew install python`

### 问题 3: L1 查询失败

**解决方案**: 检查 Python 环境和依赖包

```bash
python -c "import torch, sentencepiece"
```

如果报错，安装缺失的包：

```bash
pip install torch sentencepiece
```

### 问题 4: 本地文档未找到

**解决方案**: 这是可选的，L3 搜索会优先查找本地文档。如果没有，技能会提示"该功能可能不支持或文档未包含"。

如需完整功能，参考步骤 2 安装本地文档。

## 卸载

如果需要移除技能：

```bash
rm -rf .claude/skills/cangjie-assistant
```

或 Windows 上：

```powershell
Remove-Item -Recurse -Force .claude\skills\cangjie-assistant
```

## 获取帮助

遇到问题？请检查：

1. 验证脚本报告：`bash .claude/skills/cangjie-assistant/scripts/validate-workflow.sh`
2. Claude Code 日志：运行 `/context` 查看加载状态
3. [官方技能文档](https://code.claude.com/docs/zh-CN/skills)
