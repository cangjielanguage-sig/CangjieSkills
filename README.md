# Cangjie HarmonyOS Skills

面向**仓颉语言 + 鸿蒙应用开发**的 AI Skills 工具集，支撑 AI 开发工具从零完成鸿蒙应用的需求分析、编码、构建与调试。

## 快速安装

在你的**鸿蒙项目根目录**（与 `entry`、`AppScope` 同级）执行：

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills.git#cangjie-harmonyos -a opencode -y
```

> 根据你使用的 AI 开发工具，`-a` 后可替换为 `claude-code`、`cursor`、`github-copilot`、`trae` 等，详见 [skills CLI 文档](https://www.npmjs.com/package/skills)。

如果没有 Node.js 环境，也可以手动克隆本仓库的 `cangjie-harmonyos` 分支，将 `.agents/skills` 目录复制到项目根目录，并根据你实际使用的工具将`.agents`更名为`.opencode`或`.claude`。

## 安装后配置

由于 `npx skills add` 目前不会自动拉取 `harmonyos-build/.env`，请先在**鸿蒙项目根目录**执行以下命令创建 `.env`：

```bash
echo 'DEVECO_HOME=C:\Program Files\Huawei\DevEco Studio' > .env
```

以上路径仅为示例，请按你本机 DevEco Studio 的实际安装位置修改 `DEVECO_HOME`：

仓颉 SDK 路径会自动检测，无需手动配置。**改完即可使用。**

## 开发样例

| 读书应用 | 电影院选座应用 |
|:---:|:---:|
| ![读书应用](https://raw.gitcode.com/user-images/assets/9193544/2a6fce05-0a70-4ca3-93ae-34d232fa688b/book.png '读书应用') | ![电影院选座应用](https://raw.gitcode.com/user-images/assets/9193544/70ba4747-ed4e-4508-bdbc-264b7376c22c/微信图片_20260324103103_152_4.png '电影院选座应用') |

## Skills 一览

| 分类 | Skill | 说明 |
|------|-------|------|
| **鸿蒙开发** | `cangjie-harmonyos-doc-search` | 鸿蒙 UI 组件、系统能力 API、框架机制文档语义检索 |
| | `harmonyos-project-init` | 从零创建可运行的仓颉鸿蒙 Hello World 项目 |
| | `harmonyos-requirements` | 需求分析与技术设计方案 |
| | `harmonyos-build` | 构建执行、日志采集与错误诊断 |
| | `harmonyos-evolution` | 构建经验沉淀，失败排查时优先匹配已有记录 |
| | `harmonyos-stdx` | stdx 拓展库自动解压与依赖配置 |
| | `harmonyos-ui-inspect` | 采集设备 UI 截图与控件树，分析界面并给出迭代建议 |
| **仓颉语言** | `cangjie-lang-features` | 语言核心特性参考（类、函数、泛型、并发等 20+ 子项） |
| **标准库** | `cangjie-std` | 标准库常用功能速查（集合、IO、网络、并发、正则等） |
| | `cangjie-stdx` | 扩展标准库速查（JSON、HTTP、WebSocket、TLS 等） |
| **文档兜底** | `cangjie-original-docs` | 仓颉语言 / 标准库 / 工具链原始文档 |

## 关于 15k 兼容版

默认使用 8k（cangjie 标准版 SDK），适用于绝大多数场景。如果你的项目需要使用 15k 兼容版 SDK，在项目根目录执行：

```bash
echo '15k' > .openvk-version
```

构建时会自动读取该文件并切换到对应 SDK。
