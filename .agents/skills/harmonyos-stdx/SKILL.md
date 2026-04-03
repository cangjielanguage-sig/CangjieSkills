---
name: harmonyos-stdx
description: "在鸿蒙应用（Cangjie）开发中，当需要使用 stdx 拓展库（如 crypto、encoding、net、log、actors 等），或在构建/链接阶段出现 stdx 相关错误时，使用此 Skill 自动解压 stdx 包并在 entry/cjpm.toml 中配置 bin-dependencies.path-option。"
argument-hint: 描述你的 stdx 使用场景或报错信息，例如 "鸿蒙 stdx crypto 配置"、"actors 无法链接"、"stdx 找不到"
---

# 鸿蒙应用 stdx 依赖配置 Skill

## 职责

专门处理 Cangjie stdx 拓展库的获取、解压与 `entry/cjpm.toml` 依赖配置。不负责 UI/业务逻辑、整体构建流程或非 stdx 构建错误。

### 被调用时机

1. 编码中需要 stdx 模块能力（见下方速查表）
2. 构建/链接出现 stdx 相关错误（`undefined reference to stdx::...`、找不到 stdx 库等）
3. 用户明确要求配置 stdx

## 内置资源

| 平台 | 压缩包 | 适用场景 |
|------|--------|---------|
| x86_64 | `cangjie-stdx-ohos-x86_64-1.1.0-beta.10.1.zip` | 模拟器/PC |
| aarch64 | `cangjie-stdx-ohos-aarch64-1.1.0-beta.10.1.zip` | 真机 |

## 自动解压流程

被调用且检测到未配置 stdx 依赖时，**按以下顺序自动执行，不询问用户**：

1. 确定鸿蒙应用工程根目录和目标平台（x86_64 或 aarch64）
2. 创建固定目标目录：`<项目根>/cjnative/stdx`
3. 将对应平台的 zip 包解压到该目录
4. 在 `entry/cjpm.toml` 对应 target 节中追加 stdx 路径

> 如果两个平台都需要，分别解压到 `cjnative/stdx-x86_64` 和 `cjnative/stdx-aarch64`，并在各自的 target 节中配置。

## cjpm.toml 配置

### x86_64（模拟器/PC）

```toml
[target.x86_64-linux-ohos.bin-dependencies]
path-option = [
  "${X86_64_OHOS_LIBS}",
  "${X86_64_OHOS_MACRO_LIBS}",
  "${X86_64_OHOS_KIT_LIBS}",
  "C:/Users/zhangsan/MyApplication/cjnative/stdx"
]
```

### aarch64（真机）

```toml
[target.aarch64-linux-ohos.bin-dependencies]
path-option = [
  "${AARCH64_OHOS_LIBS}",
  "${AARCH64_OHOS_MACRO_LIBS}",
  "${AARCH64_OHOS_KIT_LIBS}",
  "C:/Users/zhangsan/MyApplication/cjnative/stdx"
]
```

## stdx 能力速查

| 模块 | 能力 |
|------|------|
| `aspectCJ` | 面向切面编程注解 |
| `compress` | 压缩/解压缩 |
| `crypto` | 加解密、签名、摘要、证书 |
| `encoding` | base64/hex/json/url 编解码 |
| `fuzz` | 模糊测试框架 |
| `log` | 统一日志 API |
| `logger` | 文本/JSON 格式日志 |
| `net` | 网络通信与 TLS |
| `serialization` | 序列化/反序列化 |
| `unittest` | 单测序列化输入 |
| `actors` | Actor 并发模型 |
| `effect` | Effect 系统 |

> API 级别文档请使用 cangjie-harmonyos-doc-search 或 cangjie_stdx Skill 检索。

## 决策树

1. 检查 `<项目根>/cjnative/stdx` 是否已解压 → 未解压则执行自动解压
2. 检查 `entry/cjpm.toml` 是否已配置 stdx 路径 → 未配置则自动追加
3. 确认目标平台 → x86_64 用 x86_64 包，aarch64 用 aarch64 包
4. 仍报错 → 要求用户贴出完整错误信息，判断是路径、版本还是符号问题

