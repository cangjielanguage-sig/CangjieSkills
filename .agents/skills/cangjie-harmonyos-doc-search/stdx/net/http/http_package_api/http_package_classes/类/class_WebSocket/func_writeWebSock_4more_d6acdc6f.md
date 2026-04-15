### func write(WebSocketFrameType, Array\<UInt8>, Int64)

```cangjie
public func write(frameType: WebSocketFrameType, byteArray: Array<UInt8>, frameSize!: Int64 = FRAMESIZE): Unit
```

功能：发送数据，非线程安全（即对同一个 [WebSocket](http_package_classes.md#class-websocket) 对象不支持多线程写）。

> **注意：**
>
> write 函数将数据以 [WebSocket](http_package_classes.md#class-websocket) 帧的形式发送给对端；
>
> - 如果发送数据帧（Text，Binary），传入的 byteArray 如果大于 frameSize（默认 4 * 1024 bytes），我们会将其分成小于等于 frameSize 的 payload 以分段帧的形式发送，否则不分段；
> - 如果发送控制帧（Close，Ping，Pong），传入的 byteArray 的大小需要小于等于 125 bytes，Close 帧的前两个字节为状态码，可用的状态码见 RFC 6455 7.4. Status Codes 协议规定，Close 帧发送之后，禁止再发送数据帧，如果发送则会抛出异常；
> - 用户需要自己保证其传入的 byteArray 符合协议，如 Text 帧的 payload 需要是 UTF-8 编码，如果数据帧设置了 frameSize，那么需要大于 0，否则抛出异常；
> - 发送数据帧时，frameSize 小于等于 0，抛出异常；
> - 用户发送控制帧时，传入的数据大于 125 bytes，抛出异常；
> - 用户传入非 Text，Binary，Close，Ping，Pong 类型的帧类型，抛出异常；
> - 发送 Close 帧时传入非法的状态码，或 reason 数据超过 123 bytes，抛出异常；
> - 发送完 Close 帧后继续发送数据帧，抛出异常；
> - closeConn 关闭连接后调用写，抛出异常。

参数：

- frameType: [WebSocketFrameType](http_package_enums.md#enum-websocketframetype) - 所需发送的帧的类型。
- byteArray: Array\<UInt8> - 所需发送的帧的 payload（二进制形式）。
- frameSize!: Int64 - 分段帧的大小，默认为 4 * 1024 bytes，frameSize 不会对控制帧生效（控制帧设置了无效）。

异常：

- SocketException - 底层连接错误时抛出异常。
- [WebSocketException](http_package_exceptions.md#class-websocketexception) - 传入非法的帧类型，或者数据时抛出异常。

### func writeCloseFrame(?UInt16, String)

```cangjie
public func writeCloseFrame(status!: ?UInt16 = None, reason!: String = ""): Unit
```

功能：发送 Close 帧。

> **注意：**
>
> 协议规定，Close 帧发送之后，禁止再发送数据帧。如果用户不设置 status，那么 reason 不会被发送（即有 reason 必有 status）；控制帧的 payload 不超过 125 bytes，Close 帧的前两个 bytes 为 status，因此 reason 不能超过 123 bytes，closeConn 关闭连接后调用写，抛出异常。

参数：

- status!: ?UInt16 - 发送的 Close 帧的状态码，默认为 None，表示不发送状态码和 reason。
- reason!: String - 关闭连接的说明，默认为空字符串，发送时会转成 UTF-8，不保证可读，debug 用。

异常：

- [WebSocketException](http_package_exceptions.md#class-websocketexception) - 传入非法的状态码，或 reason 数据超过 123 bytes 时抛出异常。

### func writePingFrame(Array\<UInt8>)

```cangjie
public func writePingFrame(byteArray: Array<UInt8>): Unit
```

功能：提供发送 Ping 帧的快捷函数，closeConn 关闭连接后调用写，抛出异常。

参数：

- byteArray: Array\<UInt8> - 所需发送的帧的 payload（二进制形式）。

异常：

- SocketException - 底层连接错误时抛出异常。
- [WebSocketException](http_package_exceptions.md#class-websocketexception) - 传入的数据大于 125 bytes，抛出异常。

### func writePongFrame(Array\<UInt8>)

```cangjie
public func writePongFrame(byteArray: Array<UInt8>): Unit
```

功能：提供发送 Pong 帧的快捷函数，closeConn 关闭连接后调用写，抛出异常。

参数：

- byteArray: Array\<UInt8> - 所需发送的帧的 payload（二进制形式）。

异常：

- SocketException - 底层连接错误时抛出异常。
- [WebSocketException](http_package_exceptions.md#class-websocketexception) - 传入的数据大于 125 bytes，抛出异常。