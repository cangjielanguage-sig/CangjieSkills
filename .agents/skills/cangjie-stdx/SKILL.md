---
name: cangjie-stdx
description: "Use for generating, reviewing, or configuring Cangjie code that needs an extension capability or an stdx availability decision: JSON, Base64/Hex/URL, compression, serialization, logging, HTTP/HTTPS, WebSocket, TLS, crypto, hashing/HMAC, certificates, or stdx configuration. The project need not be preconfigured; this Skill selects among existing configuration, authorized configuration changes, source-level alternatives, and an explicit dependency gap."
---

## 职责边界

- 本 Skill 负责扩展能力识别、stdx 可行性选路、精确包路由和运行前提；核心语法与 `std.*` API 分别交给 `cangjie-lang-features` 和 `cangjie-std`。
- “需要 stdx 能力”本身就是加载条件。是否已配置由本 Skill 检查，不能要求调用方在加载前先证明依赖可用。
- 构建、动态/静态链接、系统库和部署细节只在 [config](./config/README.md) 与各专题中维护，主文件不复制平台参数。
- HarmonyOS/HMOS 的 stdx 二进制包和打包路径由 `cangjie-hmos-stdx` 负责；本 Skill 只保留这条路由。

## 扩展能力选路流程

1. 判断需求是否确属扩展库，并读取对应 API 专题；普通集合、数学、Unicode、转换、Option 和排序不进入本 Skill。
2. 检查项目形态、`cjpm.toml` 或等效配置、目标平台、允许修改范围和运行方式；仅看到 API 文档不能证明依赖已可用。
3. 按下表选择可行路径。路径选择先于源码 import，不能把依赖风险留到写入之后说明。
4. 采用 stdx 时核对精确包、API 签名、返回/错误模型及配置专题中的构建前提；采用源码替代时同步加载语言与标准库专题核对实现所需能力。
5. 写入后检查源码、构建配置和运行时依赖三层闭包；无法验证的层级必须明确列出。

## 可行路径矩阵

| 环境与权限 | 选择 |
| --- | --- |
| 项目已有匹配目标平台的 stdx 配置 | 使用对应 stdx API，并验证 import、链接和运行时依赖 |
| 当前未配置，但用户允许修改项目配置 | 先按 [config](./config/README.md) 完成配置，再使用 stdx API |
| 只能修改源码或使用裸编译环境 | 比较 `std.*` 组合与自包含实现；只有契约必须产出实现且语法、算法和验证路径均可满足时才选择自包含方案 |
| 没有可用依赖，也没有可可靠实现的源码路径 | 说明缺失能力、所需配置和受影响产物，不生成明知无法解析的 stdx import |

自包含实现不是默认方案，也不是一律禁止的方案。应根据任务是否必须完成、算法规模、已有语言能力和可用验证证据作出选择；复杂度超过当前可复核范围时保留依赖缺口，而不是伪造可用性。

## 交付收敛与停止条件

- 当任务明确要求生成、填充或修改产物时，把“产物已写入且路径闭合”或“已明确报告不可消除的依赖缺口”作为终止条件；完成环境调研本身不算交付。
- 将可行性调查限制为一轮项目配置检查、一轮直接相关 API/算法专题检查和必要的目标平台确认。除非出现推翻前提的新证据，不要扩展到评测框架、无关源码、其它任务或宽泛仓库探索。
- 调查结束后立即固定矩阵中的一条路径并执行：已有配置则使用；允许改配置则先配置；源码受限但存在可验证替代则实现；没有可靠路径则停止并报告依赖缺口。不要在这些路径之间反复切换。
- 对 one-shot/single-pass 源码任务，若存在满足契约且可静态复核或用已知向量验证的自包含路径，应在唯一写入中完成它；不得以继续调查代替写入。若不存在可靠路径，不写占位实现、不伪造 stdx import，并在写入前说明阻塞条件。
- 最终回复列出采用路径、实际修改的源码/配置、未验证层级和剩余依赖；如果没有修改产物，必须明确说明为什么所有可行路径均被排除。

## 扩展 API 闭包

- **能力闭包**：专题确实提供所需算法、编码、协议或序列化语义，不能把相邻接口当作具体实现。
- **源码闭包**：包名、import、参数、返回类型、Option/异常处理和资源释放与专题一致。
- **配置闭包**：目标平台的依赖路径和链接方式可由项目配置解析，且修改权限明确。
- **运行闭包**：系统库、证书、动态库搜索路径和部署方式满足对应专题前提。
- **替代闭包**：若不使用 stdx，替代路径覆盖原契约，并能对关键边界或已知向量进行验证。

## 高频能力路由

| 能力 | 必读专题 |
| --- | --- |
| 下载、动态/静态依赖、平台配置 | [config](./config/README.md) |
| JSON | [json](./json/README.md)；流式或类型映射同时读 [serialization](./serialization/README.md) |
| Base64、Hex、URL | [encoding](./encoding/README.md) |
| 摘要、HMAC、非对称算法、X509 | [crypto](./crypto/README.md) |
| HTTP 客户端/服务端与 WebSocket | [http_client](./http_client/README.md)、[http_server](./http_server/README.md)、[websocket](./websocket/README.md) |
| HTTPS、证书与 ALPN | [tls](./tls/README.md) 及对应 HTTP HTTPS 专题 |
| 日志、压缩、通用序列化 | [log](./log/README.md)、[compress](./compress/README.md)、[serialization](./serialization/README.md) |

请按需查询当前目录下的工具文档：

[config](./config/README.md)：扩展标准库的下载、配置、构建指导

[json](./json/README.md)：JSON 编解码库（stdx.encoding.json / stdx.encoding.json.stream）的使用指导

[encoding](./encoding/README.md)：Base64 / Hex / URL 编解码工具（stdx.encoding.base64 / hex / url）的使用指导

[log](./log/README.md)：日志系统（stdx.log / stdx.logger）的使用指导

[compress](./compress/README.md)：Gzip / Deflate 压缩与解压缩（stdx.compress.zlib）的使用指导

[serialization](./serialization/README.md)：序列化框架（stdx.serialization.serialization）的使用指导

[http_client](./http_client/README.md)：HTTP/HTTPS 客户端编程（stdx.net.http），包括 ClientBuilder 配置、请求发送、响应处理等。进阶话题见：[HTTPS 配置](./http_client/HTTPS.md)、[Cookie 管理](./http_client/COOKIE.md)、[自定义 TCP 连接](./http_client/CONNECTOR.md)、[分块上传与 Trailer](./http_client/CHUNKED.md)

[http_server](./http_server/README.md)：HTTP/HTTPS 服务端编程（stdx.net.http），包括 ServerBuilder 配置、路由注册、请求处理、自定义分发器等。进阶话题见：[HTTPS 配置](./http_server/HTTPS.md)、[分块响应与 Trailer](./http_server/CHUNKED.md)、[HTTP/2 Server Push](./http_server/PUSH.md)

[websocket](./websocket/README.md)：WebSocket 编程（stdx.net.http），包括客户端/服务端升级、帧读写、分片处理、关闭流程等

[tls](./tls/README.md)：TLS 安全通信（stdx.net.tls），包括 TlsSocket 加密传输、证书验证与解析、会话恢复、ALPN 协商等；配置构建指导见 [tls/BUILD.md](./tls/BUILD.md)

[crypto](./crypto/README.md)：加密与证书（stdx.crypto），包括 SecureRandom 安全随机数、消息摘要(SHA256/SM3/HMAC)、RSA/ECDSA/SM2 非对称加密与签名、X509 数字证书处理等
