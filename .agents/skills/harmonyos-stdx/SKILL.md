---
name: harmonyos-stdx
description: "在鸿蒙应用（Cangjie）开发中，当需要使用 stdx 拓展库（如 crypto、encoding、net、log、actors 等），或在构建/链接阶段出现 stdx 相关错误时，使用此 Skill 自动解压 stdx 包并在 entry/cjpm.toml 中配置 bin-dependencies.path-option。"
---

# 鸿蒙应用 stdx 依赖配置 Skill

## 目的

处理 Cangjie stdx 拓展库的解压与 `entry/cjpm.toml` 依赖配置

触发时机：编码需要 stdx 模块 / 构建链接出现 stdx 相关错误 / 用户明确要求

## 内置资源

| 平台 | 压缩包 | 场景 |
|------|--------|------|
| x86_64 | `cangjie-stdx-ohos-x86_64-1.1.0-beta.10.1.zip` | 模拟器/PC |
| aarch64 | `cangjie-stdx-ohos-aarch64-1.1.0-beta.10.1.zip` | 真机 |

## 配置流程

检测到未配置 stdx 依赖时自动执行，不询问用户

1. 确定工程根目录和目标平台（x86_64 或 aarch64）
2. 创建目标目录 `<项目根>/cjnative/stdx`，解压对应平台 zip 包
3. 在 `entry/cjpm.toml` 对应 target 节追加 stdx 路径
4. 两个平台都需要时分别解压到 `cjnative/stdx-x86_64` 和 `cjnative/stdx-aarch64`

x86_64 配置示例：

```toml
[target.x86_64-linux-ohos.bin-dependencies]
path-option = [
  "${X86_64_OHOS_LIBS}",
  "${X86_64_OHOS_MACRO_LIBS}",
  "${X86_64_OHOS_KIT_LIBS}",
  "C:/Users/zhangsan/MyApplication/cjnative/stdx"
]
```

aarch64 配置示例：

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

API 详情请使用 cangjie-harmonyos-doc-search 或 cangjie_stdx Skill 检索

## 排错

1. 检查 `<项目根>/cjnative/stdx` 是否已解压 → 未解压则执行自动解压
2. 检查 `entry/cjpm.toml` 是否已配置 stdx 路径 → 未配置则自动追加
3. 确认目标平台匹配 → x86_64 用 x86_64 包，aarch64 用 aarch64 包
4. 仍报错 → 要求用户贴出完整错误信息，判断是路径、版本还是符号问题

