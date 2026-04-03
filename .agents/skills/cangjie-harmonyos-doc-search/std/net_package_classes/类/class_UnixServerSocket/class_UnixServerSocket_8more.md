## class UnixServerSocket

```cangjie
public class UnixServerSocket <: ServerSocket {
    public init(bindAt!: String)
    public init(bindAt!: SocketAddress)
}
```

功能：提供基于双工流的主机通讯服务端。

[UnixServerSocket](net_package_classes.md#class-unixserversocket) 监听连接，创建后可以通过属性和 `setSocketOptionXX` 接口配置属性值。需要调用 `bind()` 接口绑定本地地址开始监听连接。可以通过 `accept()` 接口接受连接。

> **注意：**
>
> 该类型不支持在 Windows 平台上运行。

父类型：

- [ServerSocket](net_package_interfaces.md#interface-serversocket)

### prop backlogSize

```cangjie
public mut prop backlogSize: Int64
```

功能：设置和读取 `backlog` 大小。仅可在调用 `bind` 前调用，否则将抛出异常。
变量是否生效取决于系统行为。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当在 `bind` 后调用，将抛出异常。

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### prop receiveBufferSize

```cangjie
public mut prop receiveBufferSize: Int64
```

功能：设置和读取 `SO_RCVBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### prop sendBufferSize

```cangjie
public mut prop sendBufferSize: Int64
```

功能：设置和读取 `SO_SNDBUF` 属性。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `size` 小于等于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已关闭时，抛出异常。

### init(SocketAddress)

```cangjie
public init(bindAt!: SocketAddress)
```

功能：创建一个未连接的 [UnixServerSocket](net_package_classes.md#class-unixserversocket) 实例。

参数：

- bindAt!: [SocketAddress](net_package_classes.md#class-socketaddress) - 连接的套接字地址。

### init(String)

```cangjie
public init(bindAt!: String)
```

功能：创建一个未连接的 [UnixServerSocket](net_package_classes.md#class-unixserversocket) 实例。

此文件类型可通过 [isSock()](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated) 判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除。

参数：

- bindAt!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接的文件地址。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当文件地址不合法时，抛出异常。

### func accept()

```cangjie
public override func accept(): UnixSocket
```

功能：等待接受一个客户端的连接，或从队列中读取连接。

返回值：

- [UnixSocket](net_package_classes.md#class-unixsocket) - 连接的客户端套接字。