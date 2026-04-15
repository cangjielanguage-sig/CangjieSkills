### http

用户可以选择 http 协议的版本，如 HTTP/1.1、HTTP/2。http 包的多数 API 并不区分这两种协议版本，只有当用户用到某个版本的特有功能时，才需要做这种区分，如 HTTP/1.1 中的 chunked 的 transfer-encoding，HTTP/2 中的 server push。

http 库默认使用 HTTP/1.1 版本。当开发者需要使用 HTTP/2 协议时，需要为 Client/Server 配置 tls，并且设置 alpn 的值为 `h2`；不支持 HTTP/1.1 通过 `Upgrade: h2c` 协议升级的方式升级到 HTTP/2。

如果创建 HTTP/2 连接握手失败，Client/Server 会自动将协议退回 HTTP/1.1。

- 用户通过 [ClientBuilder](./http_package_api/http_package_classes.md#class-clientbuilder) 构建一个 Client 实例，构建过程可以指定多个参数，如 httpProxy、logger、cookieJar、是否自动 redirect、连接池大小等。

- 用户通过 [ServerBuilder](./http_package_api/http_package_classes.md#class-serverbuilder) 构建一个 Server 实例，构建过程可以指定多个参数，如 addr、port、logger、distributor 等。

用户如果需要自己设置 Logger，需要保证它是线程安全的。

Client、Server 的大多数参数在构建后便不允许修改，如果想要更改，用户需要重新构建一个新的 Client 或 Server 实例；如果该参数支持动态修改，本实现会提供显式的功能，如 Server 端 cert、CA 的热更新。

- 通过 Client 实例，用户可以发送 http request、接收 http response。

- 通过 Server 实例，用户可以配置 request 转发处理器，启动 http server。在 server handler 中，用户可以通过 HttpContext 获取 client 发来的 request 的详细信息，构造发送给 client 的 response。
Server 端根据 Client 端请求，创建对应的 ProtocolService 实例，同一个 Server 实例可同时支持两种协议：HTTP/1.1、HTTP/2。

- 在 client 端，用户通过 HttpRequestBuilder 构造 request，构建过程可以指定多个参数，如 method、url、version、headers、body、trailers 等等；构建之后的 request 不允许再进行修改。

- 在 server 端，用户通过 HttpResponseBuilder 构造 response，构建过程可以指定多个参数，如 status、headers、body、trailers 等等；构建之后的 response 不允许再进行修改。

另外，本实现提供一些工具类，方便用户构造一些常用 response，如 RedirectHandler 构造 redirect response，NotFoundHandler 构造 404 response。