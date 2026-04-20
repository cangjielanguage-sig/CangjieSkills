## class UnixSocket

```cangjie
public class UnixSocket <: StreamingSocket {
    public init(address: SocketAddress, localAddress!: ?SocketAddress = None)
    public init(path: String, localPath!: ?String = None)
}
```

功能：提供基于双工流的主机通讯客户端。

[UnixSocket](net_package_classes.md#class-unixsocket) 实例创建后应调用 `connect()` 接口创建连接，并且在结束时显式调用 `close()` 回收资源。可参阅 [StreamingSocket](net_package_interfaces.md#interface-streamingsocket) 获取更多信息。

> **注意：**
>
> 该类型不支持在 Windows 平台上运行。

父类型：

- [StreamingSocket](net_package_interfaces.md#interface-streamingsocket)

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭或无可用的本地地址（本地地址未配置并且套接字未连接）时，抛出异常。

### prop readTimeout

```cangjie
public override mut prop readTimeout: ?Duration
```

功能：设置和读取读操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值，过大时将设置为`None`，默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop receiveBufferSize

```cangjie
public mut prop receiveBufferSize: Int64
```

功能：设置和读取 `SO_RCVBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### prop remoteAddress

```cangjie
public override prop remoteAddress: SocketAddress
```

功能：读取 `Socket` 已经或将要连接的远端地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### prop sendBufferSize

```cangjie
public mut prop sendBufferSize: Int64
```

功能：设置和读取 `SO_SNDBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### prop writeTimeout

```cangjie
public override mut prop writeTimeout: ?Duration
```

功能：设置和读取写操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。