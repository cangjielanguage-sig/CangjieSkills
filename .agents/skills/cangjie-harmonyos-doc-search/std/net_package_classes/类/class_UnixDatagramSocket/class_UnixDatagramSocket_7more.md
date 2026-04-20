## class UnixDatagramSocket

```cangjie
public class UnixDatagramSocket <: DatagramSocket {
    public init(bindAt!: SocketAddress)
    public init(bindAt!: String)
}
```

功能：提供基于数据包的主机通讯能力。

[UnixDatagramSocket](net_package_classes.md#class-unixdatagramsocket) 实例创建后，应当显式调用 `bind()` 接口绑定。`Unix` 数据包套接字不需要连接，不需要与远端握手多次。不过用户也可以通过 `connect/disconnect` 接口与远端建连和断连。
不同于 UDP，UDS 没有数据包大小限制，限制来源于操作系统和接口实现。
套接字资源需要用 `close` 接口显式回收。可参阅 [DatagramSocket](net_package_interfaces.md#interface-datagramsocket) 获取更多信息。

> **注意：**
>
> 该类型不支持在 Windows 平台上运行。

父类型：

- [DatagramSocket](net_package_interfaces.md#interface-datagramsocket)

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 `socket` 将要或已经绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `socket` 已经关闭时，抛出异常。

### prop receiveBufferSize

```cangjie
public mut prop receiveBufferSize: Int64
```

功能：设置和读取 `SO_RCVBUF` 属性，提供一种方式指定发包缓存大小。选项的生效情况取决于系统。

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

### prop sendBufferSize

```cangjie
public mut prop sendBufferSize: Int64
```

功能：设置和读取 `SO_SNDBUF` 属性，提供一种方式指定发包缓存大小。选项的生效情况取决于系统。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### prop sendTimeout

```cangjie
public override mut prop sendTimeout: ?Duration
```

功能：设置和读取 `send/sendTo` 操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。