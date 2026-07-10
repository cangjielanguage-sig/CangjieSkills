---
name: cangjie-stdx
description: "Use when generating or reviewing Cangjie code that explicitly needs configured stdx APIs or dependency gates: JSON, Base64/Hex/URL encoding, compression, serialization, logging, HTTP/HTTPS, WebSocket, TLS, crypto, hashing, HMAC, MD5/SHA/SM3-style digest work, or stdx configuration examples. For core .cj language and std.* APIs, use cangjie-lang-features plus cangjie-std."
---

## stdx 使用流程

1. 先判断需求是否确属扩展标准库：JSON、HTTP/HTTPS、WebSocket、TLS、具体密码学算法、Hex/Base64/URL、压缩、序列化、日志等走本 Skill；核心类型、集合、字符串、数学和 `std.*` API 仍交给 `cangjie-std`。
2. 再判断构建环境是否能使用 `stdx`：优先查项目是否有 `cjpm.toml`、目标架构、`bin-dependencies.path-option`、动态/静态库路径和运行方式；裸 `cjc`、单文件编译环境或未知环境不能默认导入 `stdx.*`。
3. 如果 `glob **/cjpm.toml` 无结果、只能改 `.cj` 源码、用户禁止改配置，或项目没有 stdx 配置，把 `stdx.*` 代码生成标为不可用路径，不得写入会编译失败的 `stdx.*` import；应改用可用的 `std.*` 能力，给出可编译降级实现，或明确说明当前契约下无法完成。
4. 确认可用后再选择精确包并添加顶层 import：例如摘要算法用 `stdx.crypto.digest.*`，摘要展示再配 `stdx.encoding.hex.*`；HTTPS/HTTP2 通常同时涉及 `stdx.net.http.*`、`stdx.net.tls.*` 和证书相关包。
5. 写入后复核三件事：`.cj` import 与 API 包匹配、`cjpm.toml` 或等效配置能解析依赖、运行时系统依赖可满足。

## 触发边界

- 不要仅因为任务是仓颉 `.cj` 代码生成就加载本 Skill；普通集合、字符串、数学、转换、Option、排序和测试能力属于 `cangjie-std`。
- 只有出现明确扩展库需求时才进入本 Skill：JSON/编码/压缩/序列化/日志、HTTP/HTTPS/WebSocket/TLS、具体摘要或加密算法、HMAC、MD5/SHA/SM3、OpenSSL/证书、stdx 配置示例。
- 在 HarmonyOS/HMOS 项目里，如果问题是 stdx 二进制包、平台 zip、`bin-dependencies.path-option` 或 Hvigor/ohpm 打包路径，转给 `cangjie-hmos-stdx`；本 Skill 只处理通用扩展库 API 和非平台化配置门禁。

## 配置门禁

- `stdx` 不是 `std.core` 自动能力，也不是仅靠 import 就可用的内置包；看到本目录文档只能说明 API 形态，不能证明目标项目已经配置了依赖。
- 无 `cjpm.toml`、临时生成包、裸 `cjc` 或单文件编译环境、只能修改 `.cj` 源码、用户禁止改配置、或无法确认依赖可见性时，禁止采用“源码里写入 `stdx.*` import、回复里提示依赖风险”的做法；该路径会直接制造不可编译代码。
- 动态库方式需要在 `cjpm.toml` 的目标平台 `bin-dependencies` 中把 `path-option` 指向 `dynamic/stdx`；`cjpm run` 会处理动态库搜索路径，直接运行产物时还要设置 Linux `LD_LIBRARY_PATH`、macOS `DYLD_LIBRARY_PATH` 或 Windows `PATH`。
- 静态库方式把 `path-option` 指向 `static/stdx`；涉及 crypto/net 时按平台补充编译选项，例如 Linux 的 `-ldl`、Windows 的 `-lcrypt32`，具体以 [config](./config/README.md) 为准。
- crypto、TLS、HTTPS 和部分 net 能力依赖 OpenSSL 3；生成相关代码前要把 OpenSSL 安装/路径视为运行前提，不能只检查仓颉 import。
- 只有任务明确允许修改项目配置时才编辑 `cjpm.toml` 或构建脚本；否则在实现说明里列出缺失配置，而不是把依赖问题藏在源码里。

## 不可用路径处理

- 若任务要求 MD5/SHA/Hex/Base64/URL/JSON 等扩展能力，但当前契约只允许改 `.cj` 源码或不能证明 `stdx` 配置可用，优先报告依赖缺口，并避免写入任何 `stdx.*` import。
- 只有在算法规模可控、仓颉语法和位运算可逐项静态复核、且不会引入不可验证的大段移植代码时，才考虑自包含替代实现；否则明确说明当前约束下无法可靠完成。
- 若必须手写位运算或编码逻辑，复核 `!x` 按位取反、整数类型、移位范围、字节/字符串转换和返回类型；不要移植其它语言的 `~x`、隐式字节数组或字符串构造习惯。

## 能力路由首检

- `std.crypto.digest` 只提供摘要接口；MD5/SHA/SM3/HMAC 等具体算法在 `stdx.crypto.digest`，二进制摘要转文本通常再用 `stdx.encoding.hex` 或 `stdx.encoding.base64`。若 MD5 任务没有可用 stdx 配置且只能改 `.cj`，不得导入 `stdx.crypto.digest`；报告依赖缺口，或仅在契约允许且可控时选择自包含替代实现。
- Hex/Base64/URL 解码函数可能返回 `Option<Array<Byte>>`；解码结果参与字符串构造、比较或写入前必须先处理 `None`。
- JSON 简单值解析/构建优先查 `stdx.encoding.json`；流式读写或自定义类型互转查 `stdx.encoding.json.stream` 和序列化文档，不要把 JSON 当作普通字符串拼接。
- HTTP 客户端、服务端、Cookie、分块传输和 WebSocket 都属于 `stdx.net.http` 相关文档；HTTPS/TLS、HTTP/2 ALPN、证书解析/验证需要同时查 TLS 与 crypto/x509 文档。
- 日志抽象与实现分在 `stdx.log` 和 `stdx.logger`；压缩在 `stdx.compress.zlib`；通用序列化在 `stdx.serialization.serialization`。不要把这些包名归入 `std.*`。

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
