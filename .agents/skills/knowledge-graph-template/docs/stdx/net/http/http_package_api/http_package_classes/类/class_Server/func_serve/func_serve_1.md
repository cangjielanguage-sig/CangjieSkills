### func serve()

```cangjie
public func serve(): Unit
```

功能：启动服务端进程，不支持重复启动。

h1 request 检查和处理：

- request-line 不符合 RFC 9112 中 request-line = method SP request-target SP HTTP-version 的规则，将会返回 400 响应；
- method 由 tokens 组成，且大小写敏感；request-target 为能够被解析的 url；HTTP-version 为 HTTP/1.0 或 HTTP/1.1 ，否则将会返回 400 响应；
- headers name 和 value 需符合特定规则，详见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类说明，否则返回 400 响应；
- 当 headers 的大小超出 server 设定的 maxRequestHeaderSize 时将自动返回 431 响应；
- headers 中必须包含 "host" 请求头，且值唯一，否则返回 400 响应 headers 中不允许同时存在 "content-length" 与 "transfer-encoding" 请求头，否则返回 400 响应；
- 请求头 "transfer-encoding" 的 value 经过 "," 分割后最后一个 value 必须为 "chunked"，且之前的 value 不允许存在 "chunked"，否则返回 400 响应；
- 请求头 "content-length" 其 value 必须能解析为 Int64 类型，且不能为负值，否则返回 400 响应，当其 value 值超出 server 设定 maxRequestBodySize，将返回 413 响应；
- headers 中若不存在 "content-length" 和 "transfer-encoding: chunked" 时默认不存在 body；
- 请求头 "trailer" 中，value 不允许存在 "transfer-encoding"，"trailer"，"content-length"；
- 请求头 "expect" 中，value 中存在非 "100-continue" 的值，将会返回 417 响应；
- HTTP/1.0 默认短连接，若想保持长连接需要包含请求头 "connection: keep-alive" 与 "keep-alive: timeout = XX, max = XX"，将会自动保持 timeout 时长的连接。HTTP/1.1 默认长连接，当解析 request 失败则关闭连接；
- 仅允许在 chunked 模式下存在 trailer，且 trailer 中条目的 name 必须被包含在 "trailer" 请求头中，否则将自动删除。

h1 response 检查和处理：

- 若用户不对 response 进行配置，将会自动返回 200 响应；
- 若接收到的 request 包含请求头 "connection: close" 而配置 response 未添加响应头 "connection" 或响应头 "connection" 的 value 不包含 "close"，将自动添加 "connection: close"，若接收到的 request 不包含请求头 "connection: close" 且响应头不存在 "connection: keep-alive"，将会自动添加；
- 如果 headers 包含逐跳响应头："proxy-connection"，"keep-alive"，"te"，"transfer-encoding"，"upgrade"，将会在响应头 "connection" 自动添加这些头作为 value；
- 将自动添加 "date" 响应头，用户提供的 "date" 将被忽略；
- 若请求方法为 "HEAD" 或响应状态码为 "1XX\204\304"，body 将配置为空；
- 若已知提供 body 的长度时，将会与响应头 "content-length" 进行比较，若不存在响应头 "content-length"，将自动添加此响应头，其 value 值为 body 长度。若响应头 "content-length" 长度大于 body 长度，将会在 handler 中抛出 [HttpException](http_package_exceptions.md#class-httpexception)，若小于 body 长度，将对 body 进行截断处理，发送的 body 长度将为 "content-length" 的值；
- response 中 "set-cookie" header 将分条发送，其他 headers 同名条目将合成一条发送；
- 在处理包含请求头："expect: 100-continue" 的 request 时，在调用 request 的 body.read() 时将会自动发送状态码为 100 的响应给客户端。不允许用户主动发送状态码为 100 的 response，若进行发送则被认定为服务器异常。

启用 h2 服务：tlsConfig 中 supportedAlpnProtocols 需包含 "h2"，此后如果 tls 层 alpn 协商结果为 h2，则启用 h2 服务。

h2 request 检查和处理：