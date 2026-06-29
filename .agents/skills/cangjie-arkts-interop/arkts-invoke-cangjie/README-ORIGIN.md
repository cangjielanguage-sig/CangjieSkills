# ArkTS Cangjie Interop Skill

这个 skill 用于处理 HarmonyOS 工程中的 ArkTS 调用仓颉互操作开发、接线与排障，适合把已有仓颉实现包装成 ArkTS 用户 API。

## 能力范围

- 扫描现有 HarmonyOS 工程中的 ArkTS/仓颉互操作线索。
- 诊断 `@Interop[ArkTS]`、`requireCJLib`、`ark_interop_api`、`.so` 库名、ABI 配置等常见问题。
- 生成一个最小 ArkTS 调用仓颉的混合工程示例。

## 安装

复制到 Codex 默认 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R /Users/huangzhuo/cds/opencode/skills/arkts-cangjie-interop ~/.codex/skills/
```

如果已存在旧版本，先删除再复制：

```bash
rm -rf ~/.codex/skills/arkts-cangjie-interop
cp -R /Users/huangzhuo/cds/opencode/skills/arkts-cangjie-interop ~/.codex/skills/
```

安装后新开 Codex 会话，通过 `$arkts-cangjie-interop` 调用。

## 使用示例

扫描现有工程：

```text
$arkts-cangjie-interop 扫描 /path/to/project 的 ArkTS/仓颉互操作状态
```

给已有仓颉工程增加 ArkTS 用户 API：

```text
$arkts-cangjie-interop 参考当前工程结构，增加仓颉互操作，并通过 ArkTS 接口暴露给用户
```

生成工程示例：

```text
$arkts-cangjie-interop 使用arkts-cangjie-interop这个skill，扫描library，并全量增加 ArkTS 调用仓颉互操作
```

## 脚本

### scan_interop_project.py

扫描 HarmonyOS 工程并输出候选目录、`requireCJLib` 库名、互操作声明目录、修复建议和潜在不一致项。

```bash
scripts/scan_interop_project.py /path/to/project
```

输出 JSON：

```bash
scripts/scan_interop_project.py /path/to/project --json
```

### install_hybrid_demo.py

把内置的 ArkTS 调用仓颉示例骨架复制到指定目录。

```bash
scripts/install_hybrid_demo.py --target /path/to/output
```

可指定包名、模块名、运行库名：

```bash
scripts/install_hybrid_demo.py \
  --target /path/to/output \
  --bundle-name com.example.hybriddemo \
  --module-name entry \
  --lib-name libmathbridge.so \
  --package-name mathbridge
```

## 参考资料

- `references/interop-reference.md`：通用 ArkTS 调用仓颉互操作流程和排障清单。
- `references/full-hybrid-example.md`：完整混合工程示例说明。
- `assets/hybrid-demo/`：可复制的最小互操作示例工程骨架。

## 校验

使用 `skill-creator` 自带校验脚本：

```bash
cd /Users/huangzhuo/cds/opencode/skills
.venv/bin/python /Users/huangzhuo/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/huangzhuo/cds/opencode/skills/arkts-cangjie-interop
```

期望输出：

```text
Skill is valid!
```

## 注意事项

- `ark_interop_api` 相关声明应优先由 DevEco Studio 生成，不要长期维护手写声明。
- `requireCJLib("libxxx.so")` 的库名必须和实际仓颉动态库产物一致。
- 真机通常需要 `arm64-v8a`，模拟器通常需要 `x86_64`。
- 面向最终用户时，优先暴露 ArkTS 包装类，不要让用户直接操作 `requireCJLib` 或生成的 `CustomLib`。
