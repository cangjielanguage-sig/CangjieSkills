# Cangjie HarmonyOS Skills

面向**仓颉语言 + 鸿蒙应用开发**的 AI Skills 工具集，支撑 AI 开发工具从零完成鸿蒙应用的需求分析、编码、构建与调试。

## 快速安装

以下三种方式任选其一，在你的**鸿蒙项目根目录**（与 `entry`、`AppScope` 同级）操作。

### 方式一：Git Clone（推荐）

**Linux / macOS：**

```bash
# 启用长路径（Windows 必须，仅需执行一次）
git config --global core.longpaths true

# 克隆 → 取出 .agents → 清理
git clone --depth 1 -b cangjie-harmonyos https://gitcode.com/Cangjie-SIG/CangjieSkills.git _tmp_skills \
  && mv _tmp_skills/.agents . && rm -rf _tmp_skills
```

**Windows PowerShell：**

```powershell
git config --global core.longpaths true
git clone --depth 1 -b cangjie-harmonyos https://gitcode.com/Cangjie-SIG/CangjieSkills.git _tmp_skills
Move-Item _tmp_skills\.agents .
Remove-Item _tmp_skills -Recurse -Force
```

> 根据你的 AI 工具重命名：OpenCode 用户将 `.agents` 改为 `.opencode`，Claude Code 用户改为 `.claude`。

### 方式二：下载 ZIP

1. 打开 https://gitcode.com/Cangjie-SIG/CangjieSkills ，切换到 `cangjie-harmonyos` 分支，点击「下载zip」
2. 解压后将其中的 `.agents/skills` 目录复制到项目根目录
3. 根据你的 AI 工具将 `.agents` 重命名为 `.opencode` 或 `.claude`

### 方式三：npx skills CLI

```bash
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills.git#cangjie-harmonyos -a opencode -y
```

> `-a` 后可替换为 `claude-code`、`cursor`、`github-copilot`、`trae` 等，详见 [skills CLI 文档](https://www.npmjs.com/package/skills)。
>
> **注意**：本分支文件较多，`npx skills` 内置 60s 克隆超时可能不够。若超时失败，请改用方式一或方式二。

## 安装后配置

构建路径直接写在 `harmonyos-build/build.py` 顶部。如果你的 DevEco Studio 安装位置与默认值不同，请打开该文件修改对应平台的常量：

```python
# Windows 默认路径
DEVECO_HOME_WINDOWS = r"C:/Program Files/Huawei/DevEco Studio"
# Linux 默认路径
DEVECO_HOME_LINUX = "/opt/DevEco-Studio"
# macOS 默认路径
DEVECO_HOME_MACOS = "/Applications/DevEco-Studio.app/Contents"
```

仓颉 SDK 路径会自动检测，无需手动配置。**改完即可使用。**

## 开发样例

| 读书应用 | 电影院选座应用 |
|:---:|:---:|
| ![读书应用](https://raw.gitcode.com/user-images/assets/9193544/2a6fce05-0a70-4ca3-93ae-34d232fa688b/book.png '读书应用') | ![电影院选座应用](https://raw.gitcode.com/user-images/assets/9193544/70ba4747-ed4e-4508-bdbc-264b7376c22c/微信图片_20260324103103_152_4.png '电影院选座应用') |

## Skills 一览

| 分类 | Skill | 说明 |
|------|-------|------|
| **鸿蒙开发** | `cangjie-harmonyos-doc-search` | 基于Openviking的鸿蒙开发文档语义检索 |
| | `harmonyos-project-init` | 从零初始化可运行的仓颉鸿蒙项目模板（含完整目录与配置） |
| | `harmonyos-requirements` | 鸿蒙需求分析与设计 Skill（需求分析→方案设计→知识搜集） |
| | `harmonyos-build` | 标准构建与日志采集，失败按固定优先级排查（Evolution→基础技能→文档检索） |
| | `harmonyos-evolution` | 仅沉淀 BUILD SUCCESSFUL 后的已验证经验，失败排查优先复用历史记录 |
| | `harmonyos-stdx` | 鸿蒙项目 stdx 依赖自动解压与 `entry/cjpm.toml` 路径配置 |
| | `harmonyos-app-diagnose` | 构建成功后采集截图与控件树、抓取 hilog 日志，结合源码生成交互测试场景，进行 UI 验证与运行时崩溃/异常诊断 |
| **仓颉语言** | `cangjie-lang-features` | 仓颉语言核心特性优先参考（语法、类型、泛型、并发、项目管理等） |
| **互操作** | `cangjie_arkts_interop` | 仓颉与 ArkTS 互操作实战（@Interop 宏优先，库方式兜底） |
| **标准库** | `cangjie-std` | 仓颉标准库常用功能速查（核心类型、集合、IO、网络、并发、正则等） |
| | `cangjie-stdx` | 仓颉扩展标准库速查（JSON、日志、编码、HTTP、WebSocket、TLS 等） |
| **文档兜底** | `cangjie-original-docs` | 仓颉语言 / 标准库 / 扩展标准库 / 工具链原始文档 |
