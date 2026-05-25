### prop readTimeout

```cangjie
public override mut prop readTimeout: ?Duration
```

功能：设置和读取读操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop receiveBufferSize

```cangjie
public mut prop receiveBufferSize: Int64
```

功能：设置和读取 `SO_RCVBUF` 属性，提供一种方式指定收包缓存大小。选项的生效情况取决于系统。

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

功能：设置和读取 `SO_SNDBUF` 属性，提供一种方式指定发包缓存大小。选项的生效情况取决于系统。

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

### init(SocketAddress)

```cangjie
public init(address: SocketAddress)
```

功能：创建一个未连接的套接字。

参数：

- address: [SocketAddress](net_package_classes.md#class-socketaddress) - 即将要连接的地址。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `address` 参数不合法或者 Windows 平台下地址为全零地址时，抛出异常。