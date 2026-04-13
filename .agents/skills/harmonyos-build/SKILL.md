---
name: harmonyos-build
description: "当需要构建鸿蒙应用项目时，使用此 Skill 执行构建流程。"
---

# 鸿蒙应用构建 Skill

## 目的

执行构建并按固定优先级排查失败，所有判断基于日志，禁止猜测修复和跳步。

## 构建流程

### 步骤 1：执行构建

```bash
python .agents/skills/harmonyos-build/build.py --project-root <项目根目录>
```

- `--project-root` 可选，默认当前工作目录。
- 串联执行 `ohpm install` → `SyncCangjieResource` → `assembleHap`。
- `DEVECO_HOME` 等路径常量在 build.py 顶部，按需修改。

### 步骤 2：判定结果

- 日志含 `BUILD SUCCESSFUL` 即成功，跳过签名不影响。
- 完整日志写入项目目录 `build.log`，排查必读此文件。
- 启动即报路径不存在时，检查 build.py 顶部常量。

### 步骤 3：失败排查（按顺序，禁止跳步）

1. **查 Evolution.md** — 用 harmonyos-evolution skill 匹配已有记录。
2. **仓颉技能调试** — 未命中则基于日志分析修复后重建。
3. **文档检索** — 仍未解决则用 cangjie-harmonyos-doc-search 检索。
4. **请求用户协助** — 日志信息不足时要求用户在 DevEco Studio 重建并提供报错。

### 步骤 4：成功沉淀

用 harmonyos-evolution skill 写入 Evolution.md，失败方案不得写入。
