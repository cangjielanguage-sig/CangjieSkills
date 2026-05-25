### static func upgradeFromClient(Client, URL, Protocol, ArrayList\<String>, HttpHeaders)

```cangjie
public static func upgradeFromClient(client: Client, url: URL,
 version!: Protocol = HTTP1_1,
 subProtocols!: ArrayList<String> = ArrayList<String>(),
 headers!: HttpHeaders = HttpHeaders()): (WebSocket, HttpHeaders)
```

功能：提供客户端升级到 [WebSocket](http_package_classes.md#class-websocket) 协议的函数。

> **说明：**
>
> 客户端的升级流程为：传入 client 对象，url 对象，构建升级请求，请求服务器后验证其响应，如果握手成功，则返回 [WebSocket](http_package_classes.md#class-websocket) 对象用于 [WebSocket](http_package_classes.md#class-websocket) 通讯，并返回 101 响应头的 [HttpHeaders](http_package_classes.md#class-httpheaders) 对象给用户。暂不支持 extensions。如果子协议协商成功，用户可通过调用返回的 [WebSocket](http_package_classes.md#class-websocket) 的 subProtocol 查看子协议。

参数：

- client: [Client](http_package_classes.md#class-client) - 用于请求的 client 对象。
- url: [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) - 用于请求的 url 对象，[WebSocket](http_package_classes.md#class-websocket) 升级时要注意 url 的 scheme 为 ws 或 wss。
- version!: [Protocol](http_package_enums.md#enum-protocol) - 创建 socket 使用的 HTTP 版本，只支持  [HTTP1_1](./http_package_enums.md#enum-protocol) 和  [HTTP2_0](./http_package_enums.md#enum-protocol) 向 [WebSocket](http_package_classes.md#class-websocket) 升级。
- subProtocols!: ArrayList\<String> - 用户配置的子协议列表，按偏好排名，默认为空。若用户配置了，则会随着升级请求发送给服务器。
- headers!: [HttpHeaders](http_package_classes.md#class-httpheaders) - 需要随着升级请求一同发送的非升级必要头，如 cookie 等。

返回值：

- ([WebSocket](http_package_classes.md#class-websocket), HttpHeaders) - 升级成功，则返回 [WebSocket](http_package_classes.md#class-websocket) 对象用于通讯和 101 响应的头。

异常：

- SocketException - 底层连接错误时抛出异常。
- [HttpException](http_package_exceptions.md#class-httpexception) - 握手时 HTTP 请求过程中出现错误时抛出异常。
- [WebSocketException](http_package_exceptions.md#class-websocketexception) - 升级失败，升级响应验证不通过时抛出异常。