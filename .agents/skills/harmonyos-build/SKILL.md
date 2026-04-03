---
name: harmonyos-build
description: "当需要构建鸿蒙应用项目时，使用此 Skill 执行构建流程。此 Skill 包含构建命令、日志采集要求和构建失败处理优先级。"
---

# 鸿蒙应用构建 Skill

## 目的

执行鸿蒙应用项目的标准构建流程，并在失败时按固定优先级排查，避免无依据的发散式修复。

## 工具

- 构建脚本：build.py（跨平台，`--version` 参数可选）
- 环境变量配置：.env（仅需配置 `DEVECO_HOME`，仓颉 SDK 路径自动检测）

## 版本检测

构建前必须确定当前项目使用的版本（8k 或 15k），版本决定使用哪个仓颉 SDK。

1. 读取项目根目录 `.openvk-version` 文件
2. 存在且有效 → 直接使用；不存在 → 自动创建并写入默认值 `8k`
3. 15k 用户需手动将文件内容改为 `15k`

| 版本 | SDK 自动检测路径 |
|------|-----------------|
| 8k   | `~/.cangjie-sdk/<ver>/cangjie` |
| 15k  | `~/.cangjie-sdk/<ver>/compatibility-sdk-*/compatibility` |

> 如需覆盖自动检测，可在 .env 中取消注释 `CANGJIE_SDK_HOME-8k` 或 `CANGJIE_SDK_HOME-15k` 并填写绝对路径。

## 核心原则

- 所有判断必须基于完整构建日志 build-full.log，不允许凭猜测修复。
- 构建失败后必须按固定顺序处理：Evolution.md → 仓颉基础技能 → cangjie-harmonyos-doc-search。
- 不允许跳步、并行开启多个无依据方案。
- 只有出现 BUILD SUCCESSFUL 后，才允许将经验写入 Evolution.md。

## 标准执行流程

### 1. 准备脚本

如果目标项目根目录不存在 build.py 和 .env，先复制：

```powershell
Copy-Item -Force '.\build.py','.\.env' '<path-to-app-project>\'
```

### 2. 执行构建并落盘日志

```bash
cd <path-to-app-project>
python build.py 2>&1 | tee build-full.log
# 或显式指定版本
python build.py --version 15k 2>&1 | tee build-full.log
```

说明：
- 构建输出可能在 UI 中被截断，必须写入 build-full.log。
- timeout 建议 >= 900000ms，避免构建未完成就超时。
- `--version` 可选，未传时自动从 `.openvk-version` 读取，文件不存在则默认 `8k`。

### 3. 读取完整日志

```powershell
Get-Content -Path build-full.log -Encoding UTF8
```

若出现 Cannot read binary file，使用上述 Get-Content 命令代替 Read 工具。

## 构建阶段

build.py 串联以下阶段（由工具链驱动）：

install → CangjiePreBuild → GenerateCangjieResource → CompileCangjie → CompileArkTS → PackageHap → SignHap → assembleHap

## 失败处理优先级

1. **查 Evolution.md**：使用 harmonyos-evolution skill，按错误类型/API/关键词匹配已有记录，命中则直接应用。
2. **仓颉基础技能调试**：Step 1 未命中时，使用仓颉基础技能分析修复后重新构建。
3. **文档检索补证**：Step 2 仍无法解决时，基于 build-full.log 使用 cangjie-harmonyos-doc-search 检索。

## 信息不足时的处理

若日志不含足够定位信息（缺少错误类型、行号、代码上下文），要求用户在 DevEco Studio 重新构建并提供完整报错。

## 成功判定与沉淀

- 以 `BUILD SUCCESSFUL` 作为成功标识。
- 成功后使用 harmonyos-evolution skill 更新 Evolution.md，记录：问题描述、错误信息、原因分析、解决方案、正确代码示例。
- 构建失败的方案不得写入 Evolution.md。
