## class UdpSocket

```cangjie
public class UdpSocket <: DatagramSocket {
    public init(bindAt!: SocketAddress)
    public init(bindAt!: UInt16)
}
```

功能：提供 udp 报文通信。

`UdpSocket` 创建实例后，需要调用 `bind()` 绑定，可在不与远端建连的前提下接受报文。`UdpSocket` 也可以通过 `connect()/disconnect()` 接口进行建连。UDP 协议要求传输报文大小不可超过 64KB 。
`UdpSocket` 需要被显式 `close()` 。可参见 [DatagramSocket](net_package_interfaces.md#interface-datagramsocket) 获取更多信息。

父类型：

- [DatagramSocket](net_package_interfaces.md#interface-datagramsocket)

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭或无可用的本地地址（本地地址未配置并且套接字未连接）时，抛出异常。

### prop receiveBufferSize

```cangjie
public mut prop receiveBufferSize: Int64
```

功能：设置和读取 `SO_RCVBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### prop receiveTimeout

```cangjie
public override mut prop receiveTimeout: ?Duration
```

功能：设置和读取 `receive/receiveFrom` 操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop remoteAddress

```cangjie
public override prop remoteAddress: ?SocketAddress
```

功能：读取 `Socket` 已经连接的远端地址，当 `Socket` 未连接时返回 `None`。

类型：?[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### prop reuseAddress

```cangjie
public mut prop reuseAddress: Bool
```

功能：设置和读取 `SO_REUSEADDR` 属性。

属性默认以及生效后的行为取决于系统，使用前，请参阅不同系统针对此属性 `SO_REUSEADDR/SOCK_REUSEADDR` 的说明文档。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### prop reusePort

```cangjie
public mut prop reusePort: Bool
```

功能：设置和读取 `SO_REUSEPORT` 属性。

Windows 上可使用 `SO_REUSEADDR`，但无 `SO_REUSEPORT` 属性，因此会抛出异常。
属性默认以及配置生效后的行为取决于系统，使用前，请参阅不同系统针对此属性 `SO_REUSEPORT` 的说明文档。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - Windows 上不支持此类型，抛出异常。

### prop sendBufferSize

```cangjie
public mut prop sendBufferSize: Int64
```

功能：设置和读取 `SO_SNDBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。