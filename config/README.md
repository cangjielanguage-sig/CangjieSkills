# cangjie.skills.toml 配置参考

`cangjie.skills.toml` 是本套 Skills 的统一配置文件。它不是必需文件：未配置的字段使用自动发现或内置默认值。建议从本目录的 [示例文件](cangjie.skills.toml) 复制，并删除所有不需要覆盖的字段。

## 加载机制

配置由 `cangjie-harmonyos-dev/tools/config_loader.py` 统一解析；项目创建、构建运行、互操作和知识库脚本复用同一个加载器。字段按以下优先级取值，序号越小优先级越高：

1. 当前命令的 CLI 参数。
2. 工具直接支持的环境变量，例如 `DEVECO_HOME`、`CANGJIE_SDK_HOME`，以及 `api_key_env` 指向的密钥变量。
3. `--config` 指定的文件；支持重复指定的命令按出现顺序合并，后者覆盖前者。
4. `CANGJIE_SKILLS_CONFIG` 指向的文件。
5. 当前项目根目录的 `cangjie.skills.toml`。
6. 用户目录 `~/.cangjie/cangjie.skills.toml`。
7. 自动发现或内置默认值。

显式传入 `--config` 后不再自动加载第 4 至第 6 层。显式路径或 `CANGJIE_SKILLS_CONFIG` 指向的文件不存在时会报错；只有未创建的用户和项目默认文件会被跳过。配置文件可以只包含少量覆盖项；表之间逐字段合并。未知表、未知字段、错误类型、越界数值、空白的自动发现覆盖值和明文 `api_key` 均会报错，不会静默忽略。

推荐的职责划分：

- 用户配置保存本机工具链路径和常用设备。
- 项目配置只保存团队需要复现的项目、脚手架和检索设置。
- CLI 参数保存单次任务选项，例如输出目录、等待时间、交互场景、查询条数和增量构建。
- 凭据只保存到环境变量；TOML 仅记录变量名。

## 统一诊断

在项目根目录运行一次有界、只读诊断，可同时查看配置来源、工具链、项目元数据、HAP 与设备状态：

```powershell
python -B <skills-root>/cangjie-harmonyos-dev/tools/doctor.py --project-root . --json
```

输出包含版本化 JSON schema、每个最终值的 `source`、`ready.build`、`ready.runtime` 与 `inspection.stop`。诊断会同时解析 `hdc` 退出码和失败文本，且不会输出凭据环境变量的值。字段完整时应以该报告为准；只有字段缺失或后续命令出现具体失败，才继续检查模板、依赖或构建目录。离线 CI 可加 `--no-device-check`，需要把未就绪作为非零退出时再加 `--strict`。

## 配置项

### `[toolchain]`

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `toolchain.deveco_home` | 自动发现 | DevEco Studio 根目录。依次尝试 `DEVECO_HOME` 和平台标准安装目录；需要构建但仍未找到时给出明确错误。 |
| `toolchain.cangjie_sdk` | 自动发现 | 仓颉 SDK 根目录。依次尝试 `CANGJIE_SDK_HOME`、`~/.cangjie-sdk/` 下最新的有效版本和 SDK 6.1 常用目录；构建或鸿蒙 stdx 配置需要它，缺失时失败。 |
| `toolchain.hdc` | 自动发现 | `hdc` 可执行文件。依次尝试 CLI/配置、`PATH` 和 DevEco 标准 toolchains 目录；设备操作前仍未找到时失败。 |
| `toolchain.ohpm_registry` | `https://ohpm.openharmony.cn/ohpm/` | 构建所用 OHPM 仓库。必须是绝对 HTTP(S) URL；省略时使用官方默认值。 |
| `toolchain.verify_tls` | `true` | 是否校验 OHPM TLS 证书。仅在受信任的私有仓库环境中设为 `false`。 |

### `[device]`

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `device.target` | `127.0.0.1:5555` | UI 与 hilog 采集使用的 `hdc` 目标。连接真机或其他模拟器时，填写 `hdc list targets` 返回的标识。 |

### `[runtime]`

普通单模块项目应省略本表。字段用于解决多模块、多 Ability 或多份 HAP 造成的自动发现歧义，不替代项目内的 `app.json5`、`build-profile.json5` 和 `module.json5`。

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `runtime.bundle` | 自动发现 | 启动和采集目标的 bundle name。读取 `AppScope/app.json5`；仅在需要启动且无法识别时失败。 |
| `runtime.ability` | 自动发现 | 启动 Ability。读取所选模块的 `module.json5`；仅在需要启动且无法识别时失败。 |
| `runtime.module` | 自动发现 | 构建、启动和检查的模块。优先选择唯一模块，其次选择 `entry`，否则选择首个声明模块并警告。 |
| `runtime.hap` | 自动发现 | 安装或采集使用的 HAP。选择目标模块下最新产物；多份产物会警告。相对路径以项目根目录解析。 |

### `[scaffold]`

本表只影响随后执行的纯仓颉或混合项目生成，不改写已有项目。原 `[project]` 表已移除。

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `scaffold.app_name` | 生成器默认值 | 应用显示名称。纯仓颉模板为 `Cangjie App`，混合模板为 `Cangjie ArkTS Hybrid`。 |
| `scaffold.bundle_name` | 生成器默认值 | 应用 bundle name。纯仓颉模板为 `com.example.myapplication`，混合模板为 `com.example.hybrid`。 |
| `scaffold.module_name` | `entry` | 生成的入口 HAP 模块名和目录名。 |

生成器专属参数保留在 CLI：纯仓颉项目的 `--vendor`，混合项目的 `--package-name`，以及高级兼容选项 `--sdk-version`、`--model-version`。模板内部仓颉包名也不作为共享配置项。

### `[knowledge]`

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `knowledge.version` | `default` | 查询随包索引中的文档版本。维护或跨版本检索可用 CLI 指定 `all`；语料和索引路径固定为 Skill 内资源。 |

### `[knowledge.embedding]`

发布索引已包含每个章节的 256 维文档向量。向量服务只把运行时查询转换为同规格向量，不参与生成答案；系统不依赖 LLM。

| 配置项 | 默认值 | 作用与降级策略 |
| --- | --- | --- |
| `knowledge.embedding.mode` | `search` | `off` 仅确定性检索；`search` 在弱查询时使用向量；`index` 严格构建文档向量；`all` 同时允许构建和查询。查询失败会确定性降级，严格构建失败会保留旧索引。 |
| `knowledge.embedding.api_format` | `dashscope` | 请求协议，可选 `dashscope` 或 `openai`。其他值在加载时拒绝。 |
| `knowledge.embedding.model` | `text-embedding-v4` | 向量模型名。查询时模型错误会降级；严格构建时失败且不替换旧索引。 |
| `knowledge.embedding.base_url` | DashScope text-embedding 地址 | 必须是绝对 HTTP(S) URL。`openai` 协议填写 `/embeddings` 之前的 API 根地址。 |
| `knowledge.embedding.api_key_env` | `DASHSCOPE_API_KEY` | 保存密钥的环境变量名。变量未设置时不启用查询向量；显式构建文档向量会在改动索引前失败。 |
| `knowledge.embedding.dimensions` | `256` | 查询和文档向量维度，必须是正整数。256 是默认的质量、延迟和体积平衡；更换模型或维度时必须重建匹配向量。服务不支持时，查询降级、严格构建失败。 |
| `knowledge.embedding.min_similarity` | `0.40` | 向量结果最低余弦相似度，范围 0–1。低于阈值的结果被拒绝；只应根据留出评测调整。 |
| `knowledge.embedding.batch_size` | `10` | 构建或测试时单次请求的文本数，必须是正整数。失败行为由 `mode` 决定。 |
| `knowledge.embedding.timeout_seconds` | `60.0` | 单次服务请求超时秒数，必须大于 0。超时后查询降级、严格构建失败。 |
| `knowledge.embedding.max_retries` | `2` | 瞬时错误和 HTTP 429 的最大重试次数，必须不小于 0；普通 4xx 错误不重试。 |

默认的 DashScope 查询配置示例：

```toml
[knowledge.embedding]
mode = "search"
api_format = "dashscope"
model = "text-embedding-v4"
api_key_env = "DASHSCOPE_API_KEY"
dimensions = 256
```

```powershell
$env:DASHSCOPE_API_KEY = "<API key>"
```

未配置密钥时，精确符号、FTS、示例、错误码和结构化查询仍可离线使用。`search` 模式还会让高置信度词法结果直接返回，因此并非每次查询都会调用向量服务。

## 校验与排错

在仓库根目录验证配置契约和全部 Skills：

```powershell
python -B scripts/validate_skills.py
```

知识库配置可再用以下命令检查发布索引：

```powershell
python -B .agents/skills/cangjie-harmonyos-knowledge/scripts/knowledge.py doctor --strict
```

配置加载错误会包含文件路径和完整字段名。自动发现失败时，优先用对应命令的 CLI 参数验证正确值，再把稳定且需要复用的值写入用户或项目配置。
