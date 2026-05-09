## class WebSocketFrame

```cangjie
public class WebSocketFrame
```

功能：[WebSocket](http_package_classes.md#class-websocket) 用于读的基本单元。

[WebSocketFrame](http_package_classes.md#class-websocketframe) 提供了三个属性，其中 fin 和 frameType 共同说明了帧是否分段和帧的类型。payload 为帧的载荷。

- 分段帧的首帧为 fin == false，frameType == TextWebFrame 或 BinaryWebFrame；
- 中间帧 fin == false，frameType == ContinuationWebFrame；
- 尾帧 fin == true， frameType == ContinuationWebFrame；
- 非分段帧为     fin == true， frameType != ContinuationWebFrame；
- 用户仅能通过 [WebSocket](http_package_classes.md#class-websocket) 对象的 read 函数得到 [WebSocketFrame](http_package_classes.md#class-websocketframe)。数据帧可分段，如果用户收到分段帧，则需要多次调用 read 函数直到收到完整的 message，并将所有分段的 payload 按接收顺序拼接。

> **注意：**
>
> 由于控制帧可以穿插在分段帧之间，用户在拼接分段帧的 payload 时需要单独处理控制帧。分段帧之间仅可穿插控制帧，如果用户在分段帧之间接收到其他数据帧，则需要当作错误处理。

### prop fin

```cangjie
public prop fin: Bool
```

功能：获取 [WebSocketFrame](http_package_classes.md#class-websocketframe) 的 fin 属性，fin 与 frameType 共同说明了帧是否分段和帧的类型。

类型：Bool

### prop frameType

```cangjie
public prop frameType: WebSocketFrameType
```

功能：获取 [WebSocketFrame](http_package_classes.md#class-websocketframe) 的帧类型，fin 与 frameType 共同说明了帧是否分段和帧的类型。

类型：[WebSocketFrameType](http_package_enums.md#enum-websocketframetype)

### prop payload

```cangjie
public prop payload: Array<UInt8>
```

功能：获取 [WebSocketFrame](http_package_classes.md#class-websocketframe) 的帧载荷。如果是分段数据帧，用户需要在接收到完整的 message 后，将所有分段的 payload 按接收序拼接。

类型：Array\<UInt8>