## class WebSocket

```cangjie
public class WebSocket
```

功能：提供 [WebSocket](http_package_classes.md#class-websocket) 服务的相关类，提供 [WebSocket](http_package_classes.md#class-websocket) 连接的读、写、关闭等函数。用户通过 upgradeFrom 函数以获取 [WebSocket](http_package_classes.md#class-websocket) 连接。

- 调用 `read()` 读取一个 [WebSocketFrame](http_package_classes.md#class-websocketframe)，用户可通过 [WebSocketFrame](http_package_classes.md#class-websocketframe).frameType 来知晓帧的类型，通过 [WebSocketFrame](http_package_classes.md#class-websocketframe).fin 来知晓是否是分段帧。
- 调用 `write(frameType: WebSocketFrameType, byteArray: Array<UInt8>)`，传入 message 的类型和 message 的 byte 来发送 [WebSocket](http_package_classes.md#class-websocket) 信息，如果写的是控制帧，则不会分段发送，如果写的是数据帧（Text、Binary），则会将 message 按底层 buffer 的大小分段（分成多个 fragment）发送。

详细说明见下文接口说明，接口行为以 RFC 6455 为准。

### prop logger

```cangjie
public prop logger: Logger
```

功能：日志记录器。

类型：[Logger](../../../log/log_package_api/log_package_classes.md#class-logger)

### prop subProtocol

```cangjie
public prop subProtocol: String
```

功能：获取与对端协商到的 subProtocol，协商时，客户端提供一个按偏好排名的 subProtocols 列表，服务器从中选取一个或零个子协议。

类型：String