# 仓颉鸿蒙应用开发 Skills

面向仓颉鸿蒙应用开发的 Agent Skills 套件，技能涵盖仓颉/鸿蒙知识库、项目创建、构建运行、操作测试与问题诊断等。主入口 `cangjie-harmonyos-dev` 为 Agent 提供技能导航，并实现整套 Skills 的配置管理。

## Skills 简介

| Skill | 功能 |
| --- | --- |
| `cangjie-harmonyos-dev` | 总入口，提供 Skills 导航与配置管理 |
| `harmonyos-project-bootstrap` | 创建或修复仓颉鸿蒙项目，并为模拟器与真机下载、安装和配置 stdx |
| `cangjie-harmonyos-knowledge` | 鸿蒙知识库和查询工具，可选向量化增强 |
| `cangjie-coding` | 仓颉语言、标准库、扩展标准库与工具链的通用知识库和查询工具 |
| `cangjie-arkts-interop` | 仓颉-ArkTS 混合项目开发指导，包括混合项目创建和检查 |
| `harmonyos-build-run-diagnose` | 构建应用、安装启动、测试操作、故障诊断，包括获取 UI 和 hilog 快照 |
| `harmonyos-evolution` | 读取和记录已经构建或运行证实的工程经验，避免把猜测写入长期记忆 |

## 安装

将 `.agents/skills/` 目录复制到所用 Coding Agent 工具支持的 Skills 配置路径。如果系统已安装 node/npx，也可以执行以下命令交互式安装配置：

```shell
npx skills add https://gitcode.com/Cangjie-SIG/CangjieSkills.git#harmonyos-6.1
```

使用前确保环境已配置如下工具：

- DevEco Studio + Cangjie Plugin，6.1 及以上版本
- Python 3.11+，目前 Skills 中 python 脚本只使用了标准库，无需安装其他库
- 连接模拟器或真机，设备系统版本要适配 SDK 版本

## 使用

一般情况下，只需要向 Agent 描述开发目标即可，Agent 会按需加载使用相关 Skills。

也可以显式提及入口 `cangjie-harmonyos-dev`，例如：

```text
使用 cangjie-harmonyos-dev skill，开发一个记账本应用，并在模拟器上测试验证各项功能
```

基于入口 Skill 指导，Agent 会按需调用其余 Skills。

在某些开发场景中，可以限定只使用某个 Skill，例如用 `cangjie-harmonyos-knowledge` 查询学习 ArkUI 知识，或用 `harmonyos-build-run-diagnose` 诊断已有项目。在另一些开发场景，还可以移除/禁用不需要的 Skills，例如不涉及项目
创建和 ArkTS 互操作时，可以移除 `harmonyos-project-bootstrap` 和 `cangjie-arkts-interop`。

## 配置

鸿蒙应用开发 Skills 涉及一套复杂工具，需要从环境获取很多参数，为此实现了一套配置系统，详细内容请参阅[配置参考](config/README.md)。

配置是可选的，所有配置项都有默认值或自动探索/降级策略。当工具路径、测试设备和知识库向量服务等内容需要定制时，就需要创建配置文件 `cangjie.skills.toml`。

[config/cangjie.skills.toml](config/cangjie.skills.toml) 给出了一个配置模板。通常只保留需要覆盖的字段，并放在应用项目根目录或用户目录 `~/.cangjie/`。例如：

```toml
[device]
target = "127.0.0.1:5555"

[knowledge.embedding]
mode = "search"
model = "text-embedding-v4"
base_url = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding"
api_key_env = "DASHSCOPE_API_KEY"
```

如果需要判断配置是否完整可用，可以在项目根目录执行诊断脚本，将输出每个配置项取值和来源，并给出构建/运行就绪状态：

```powershell
python -B <skills-root>/cangjie-harmonyos-dev/tools/doctor.py --project-root . --json
```

> [!IMPORTANT]
>
> 实测启用向量查询后，混合检索质量会更好，因此建议配置向量模型。当前 `cangjie-harmonyos-knowledge` 知识库中已预置了基于
> text-embedding-v4 建立的 256 维向量索引数据，如果要复用这些数据，就只能配置 text-embedding-v4 模型。如果您使用
> 其他向量模型或调整向量维度，需要重建向量索引。

## 注意事项

- 随包知识库可离线执行符号、全文、示例和结构化检索。自然语言弱查询若要使用发布向量，需要配置兼容的查询向量服务。服务不可用时自动退回确定性检索。
- 截图或设计稿复刻必须由具备视觉能力的模型检查参考图和最终截图；文本模型可以实现与构建，但不能单独确认视觉对齐。
- 模板以 Skill 内标明的 SDK/仓颉版本为已验证基线。切换 SDK、模型版本、ABI 或真机架构后，应重新完成构建与设备验证。
- `harmonyos-evolution` 只记录可复现且已有证据的结论。项目专属经验写入项目根目录的 `Evolution.md`，跨项目经验写入 `~/.cangjie/harmonyos-evolution.md`。

## 开发与验证

快速校验仓库结构、文档链接和配置契约：

```powershell
python -B scripts/validate_skills.py
```

提交前运行完整测试，包括所有单元测试、知识库健康检查、确定性/留出检索、离线语义诊断、域外拒答、Agent 高频合约和 p95 性能回归测试：

```powershell
python -B scripts/validate_skills.py --full
```

鸿蒙知识库技术方案和开发维护指导请参阅 [cangjie-harmonyos-knowledge](.agents/skills/cangjie-harmonyos-knowledge/README.md)。
