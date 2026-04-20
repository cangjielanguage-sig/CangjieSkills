- headers name 和 value 需符合特定规则，详见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类说明，此外 name 不能包含大写字符，否则发送 RST 帧关闭流，即无法保证返回响应；
- trailers name 和 value 需符合同样规则，否则关闭流；
- headers 不能包含 "connection"，"transfer-encoding"，"keep-alive"，"upgrade"，"proxy-connection"，否则关闭流；
- 如果有 "te" header，其值只能为 "trailers"，否则关闭流；
- 如果有 "host" header 和 ":authority" pseudo header，"host" 值必须与 ":authority" 一致，否则关闭流；
- 如果有 "content-length" header，需符合 "content-length" 每个值都能解析为 Int64 类型，且如果有多个值，必须相等，否则关闭流；
- 如果有 "content-length" header，且有 body 大小，则 content-length 值与 body 大小必须相等，否则关闭流；
- 如果有 "trailer" header，其值不能包含 "transfer-encoding"，"trailer"，"content-length"，否则关闭流；
- 仅在升级 [WebSocket](http_package_classes.md#class-websocket) 场景下支持 CONNECT 方法，否则关闭流；
- pseudo headers 中，必须包含 ":method"、":scheme"、":path"，其中 ":method" 值必须由 tokens 字符组成，":scheme" 值必须为 "https"，":path" 不能为空，否则关闭流；
- trailer 中条目的 name 必须被包含在 "trailer" 头中，否则将自动删除；
- request headers 大小不能超过 maxHeaderListSize，否则关闭连接。

h2 response 检查和处理：

- 如果 HEAD 请求的响应包含 body，将自动删除；
- 将自动添加 "date" field，用户提供的 "date" 将被忽略；
- 如果 headers 包含 "connection"，"transfer-encoding"，"keep-alive"，"upgrade"，"proxy-connection"，将自动删除；
- response 中 "set-cookie" header 将分条发送，其他 headers 同名条目将合成一条发送；
- 如果 headers 包含 "content-length"，且 method 不为 "HEAD"，"content-length" 将被删除；
- 如果 method 为 "HEAD"，则：
    - headers 包含 "content-length"，但 "content-length" 不合法（无法被解析为 Int64 值，或包含多个不同值），如果用户调用 [HttpResponseWriter](http_package_classes.md#class-httpresponsewriter) 类的 write 函数，将抛出 [HttpException](http_package_exceptions.md#class-httpexception)，如果用户 handler 已经结束，将打印日志；
    - headers 包含 "content-length"，同时 response.body.length 不为 -1，"content-length" 值与 body.length 不符，同 6.1 处理；
    - headers 包含 "content-length"，同时 response.body.length 为 -1，或 body.length 与 "content-length" 值一致，则保留 "content-length" header；
- trailer 中条目必须被包含在 "trailer" 头中，否则将自动删除；
- 如果 handler 中抛出异常，且用户未调用 write 发送部分响应，将返回 500 响应。如果用户已经调用 write 发送部分响应，将发送 RST 帧关闭 stream。

h2 server 发完 response 之后，如果 stream 状态不是 CLOSED，会发送带 NO_ERROR 错误码的 RST 帧关闭 stream，避免已经处理完毕的 stream 继续占用服务器资源。

h2 流量控制：

- connection 流量窗口初始值为 65535，每次收到 DATA 帧将返回一个 connection 层面的 WINDOW-UPDATE，发送 DATA 时，如果 connection 流量窗口值为负数，将阻塞至其变为正数；
- stream 流量窗口初始值可由用户设置，默认值为 65535，每次收到 DATA 帧将返回一个 stream 层面的 WINDOW-UPDATE，发送 DATA 时，如果 stream 流量窗口值为负数，将阻塞至其变为正数。

h2 请求优先级：

- 支持按 urgency 处理请求，h2 服务默认并发处理请求，当并发资源不足时，请求将按 urgency 处理，优先级高的请求优先处理。

默认 [ProtocolServiceFactory](http_package_interfaces.md#interface-protocolservicefactory) 协议选择：

- 如果连接是 tcp，使用 HTTP/1.1 server；
- 如果连接是 tls，根据 alpn 协商结果确定 http 协议版本，如果协商结果为 "http/1.0"，"http/1.1" 或 ""，使用 HTTP/1.1 server，如果协商结果为 "h2"，使用 HTTP/2 server，否则不处理此次请求，打印日志关连接。

异常：

- SocketException - 当端口监听失败时，抛出异常。