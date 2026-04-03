## class TcpSocket

```cangjie
public class TcpSocket <: StreamingSocket & Equatable<TcpSocket> & Hashable {
    public init(address: String, port: UInt16)
    public init(address: SocketAddress)
    public init(address: SocketAddress, localAddress!: ?SocketAddress)
}
```

功能：请求 TCP 连接的客户端。

当实例对象被创建后，可使用 `connect` 函数创建连接，并在结束时显式执行 `close` 操作。
该类型继承自 [StreamingSocket](net_package_interfaces.md#interface-streamingsocket)， 可参阅 [StreamingSocket](net_package_interfaces.md#interface-streamingsocket) 章节获取更多信息。

父类型：

- [StreamingSocket](net_package_interfaces.md#interface-streamingsocket)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TcpSocket](#class-tcpsocket)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### prop bindToDevice

```cangjie
public mut prop bindToDevice: ?String
```

功能：设置和读取绑定网卡。

类型：?[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop keepAlive

```cangjie
public mut prop keepAlive: ?SocketKeepAliveConfig
```

功能：设置和读取保活属性，`None` 表示关闭保活。

用户未设置时将使用系统默认配置。设置此配置可能会被延迟或被系统忽略，取决于系统的处理能力。

类型：?[SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig)

### prop linger

```cangjie
public mut prop linger: ?Duration
```

功能：设置和读取 `SO_LINGER` 属性，默认值取决于系统，`None` 表示禁用此选项。

> **说明：**
>
> - 如果 `SO_LINGER` 被设置为 `Some(v)`，当套接字关闭时，如果还有等待的字节流，我们将在关闭连接前等待 `v` 时间，如果超过时间，字节流还未被发送，连接将会被异常终止（通过 RST 报文关闭）。
> - 如果 `SO_LINGER` 被设置为 `None`，当套接字关闭时，连接将被立即关闭，如果当前等待发送的字符，使用 FIN-ACK 关闭连接，当还有剩余待发送的字符时，使用 RST 关闭连接。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭或无可用的本地地址（本地地址未配置并且套接字未连接）时，抛出异常。

### prop noDelay

```cangjie
public mut prop noDelay: Bool
```

功能：设置和读取 `TCP_NODELAY` 属性，默认为 `true`。

这个选项将禁用 Nagel 算法，所有写入字节被无延迟得转发。当属性设置为 `false` 时，Nagel 算法将在发包前引入延时时间。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### prop quickAcknowledge

```cangjie
public mut prop quickAcknowledge: Bool
```

功能：设置和读取 `TCP_QUICKACK` 属性，默认为 `false`。

这个选项类似于 `noDelay`，但仅影响 TCP ACK 和第一次响应。不支持 Windows 和 macOS 系统。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)