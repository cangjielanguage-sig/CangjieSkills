# Cangjie Assistant - 快捷参考

## 目录结构

```
claude/skills/cangjie-assistant/
├── SKILL.md                    ✅ 主技能文件（含 YAML 前置元数据）
├── template.md                 ✅ 查询和构建模板
├── README.md                   ✅ 功能说明
├── SETUP.md                    ✅ 详细的安装指南
├── QUICKREF.md                 ✅ 本文件 - 快捷参考
├── examples/
│   ├── l0-analysis.md          ✅ L0 需求分析示例
│   ├── l1-query.md             ✅ L1 RAG 查询示例
│   └── l3-search.md            ✅ L3 本地文档搜索示例
└── scripts/
    └── validate-workflow.sh    ✅ 环境验证脚本
```

## 三级检索流程

```
用户需求
    ↓
┌─────────────────────────────────────────┐
│ L0: 需求技术化分析                       │
│ → 识别 UI 组件、数据结构、交互方式      │
│ → 细化为"导包→初始化→使用"关键词      │
│ → 确定: Button, List, Image, onClick 等  │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ L1: RAG 快速检索                         │
│ cd cangjie-dev-workflow                  │
│ python ask_cangjie.py "Button导包"      │
│ python ask_cangjie.py "List初始化"      │
│ ...                                      │
└─────────────────────────────────────────┘
    ↓
    ├─ ✅ 完整结果 → 开始编码
    └─ ❌ 无结果 → 进入 L3
        ↓
┌─────────────────────────────────────────┐
│ L3: 本地文档搜索                         │
│ UI 问题 → hm-docs/ui-dev/               │
│ API 问题 → hm-docs/stdlib/              │
│ 语法问题 → hm-docs/syntax/              │
│ 错误排查 → 先查 Evolution.md            │
└─────────────────────────────────────────┘
```

## L0 分析 - 技术关键词细化示例

| 原始需求 | 不要搜索 | ✅ 正确拆解 |
|---------|---------|-----------|
| 登录页面 | "登录"、"认证" | TextInput导包, TextInput初始化, TextInput验证 |
| 商品列表 | "商品"、"购物" | List导包, List初始化, List数据绑定 |
| 篮球页面 | "篮球"、"球队" | List导包, Image显示, Text样式 |
| 数据请求 | "API"、"后端" | HTTP客户端, JSON解析, 异步处理 |

## PowerShell 搜索命令 (L3)

```powershell
# 搜索 UI 组件
Select-String -Path "hm-docs\ui-dev\arkui-cj\*.md" -Pattern "Button" -Context 2

# 递归搜索 API
Get-ChildItem -Path "hm-docs\ui-dev" -Filter "*.md" -Recurse | Select-String -Pattern "onClick" -Context 1

# 快速定位 Button API
Select-String -Path "hm-docs\ui-dev\reference\arkui-cj\cj-button-picker-button.md" -Pattern "import" -Context 1

# 搜索加密相关
Get-ChildItem -Path "hm-docs\stdx\libs_stdx\crypto" -Filter "*.md" -Recurse | Select-String -Pattern "encrypt" -Context 2
```

## 构建命令

```powershell
# 执行构建
.\build.ps1

# 构建失败时
1. 检查 Evolution.md 是否有相同问题
2. 如果没有，搜索关键词: "undefined symbol", "import error", "syntax error"
3. 修复后重新构建
4. 构建成功后更新 Evolution.md 记录重难点
```

## 常用文档路径

| 问题类型 | 路径 |
|---------|------|
| Button | `hm-docs/ui-dev/arkui-cj/cj-common-components-button.md` |
| List | `hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md` |
| Text/TextInput | `hm-docs/ui-dev/arkui-cj/cj-common-components-text-*.md` |
| Image | `hm-docs/ui-dev/reference/arkui-cj/cj-image-video-image.md` |
| HTTP | `hm-docs/stdx/libs_stdx/net/http/` |
| JSON | `hm-docs/stdx/libs_stdx/encoding/json/` |
| 并发/线程 | `hm-docs/syntax/source_zh_cn/concurrency/` |
| 泛型 | `hm-docs/syntax/source_zh_cn/generic/` |

## 技能调用方式

```bash
# 方式 1: 斜杠命令直接调用
/cangjie-assistant 如何创建 List 组件？

# 方式 2: 让 Claude 自动识别
帮我创建一个登录页面

# 方式 3: 带参数调用
/cangjie-assistant 查询 Button 组件的 onClick 事件
```

## 安装到其他项目

```bash
# 快速复制
cp -r .claude/skills/cangjie-assistant ~/.claude/skills/

# 验证
bash ~/.claude/skills/cangjie-assistant/scripts/validate-workflow.sh
```

## 核心原则

1. **严禁猜测** - 不确定时一定查文档
2. **技术优先** - 不搜索业务词汇，搜索技术组件
3. **三维拆解** - "导包→初始化→使用"
4. **结果展示** - L1 查询结果必须展示给用户
5. **本地优先** - L3 比网络搜索更快更准确
6. **进化记录** - 构建成功后更新 Evolution.md

## 错误处理决策树

```
构建失败
    ↓
检查 Evolution.md
    ↓
    ├─ 找到相同问题 → 应用解决方案 → 重新构建
    └─ 未找到
        ↓
    进入 L3 搜索
        ↓
        ├─ UI 问题 → hm-docs/ui-dev/
        ├─ API 问题 → hm-docs/ui-dev/reference/
        ├─ 语法问题 → hm-docs/syntax/
        └─ 构建问题 → DevEco Studio 查看完整错误
        ↓
    修复 → 更新 Evolution.md → 重新构建
```

## YAML 前置元数据参考

```yaml
---
name: cangjie-assistant
description: HarmonyOS Next Cangjie development assistant...
argument-hint: [query] or [build]
disable-model-invocation: false
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
---
```

## 文件说明

| 文件 | 作用 | 参考 |
|------|------|------|
| SKILL.md | 主技能定义 + 工作流逻辑 | 本文件被 Claude 自动加载 |
| template.md | 统一的查询和构建模板 | Claude 按模板结构化输出 |
| examples/l0-*.md | 需求分析示例 | 学习如何拆解需求 |
| examples/l1-*.md | RAG 查询示例 | 学习如何精准查询 |
| examples/l3-*.md | 本地搜索示例 | 学习如何搜索文档 |
| scripts/validate.sh | 环境验证 | 检查安装是否完整 |

## 速查表

| 需求 | 操作 |
|------|------|
| 创建 UI 组件 | L0 分析 → L1 查询 → L3 补充 |
| 查询 API | L3 直接搜索 hm-docs |
| 构建失败 | 查 Evolution.md → L3 搜索 |
| 学习语法 | L3 搜索 hm-docs/syntax/ |
| 验证环境 | `bash scripts/validate-workflow.sh` |
| 复用技能 | 复制 `.claude/skills/cangjie-assistant/` |
