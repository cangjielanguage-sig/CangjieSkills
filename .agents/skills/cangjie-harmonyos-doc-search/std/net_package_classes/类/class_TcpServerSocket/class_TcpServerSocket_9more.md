## class TcpServerSocket

```cangjie
public class TcpServerSocket <: ServerSocket {
    public init(bindAt!: SocketAddress)
    public init(bindAt!: UInt16)
}
```

功能：监听 TCP 连接的服务端。

套接字被创建后，可通过属性和 `setSocketOptionXX` 接口配置属性。
启动监听需要调用 `bind()` 将套接字绑定到本地端口。`accept()` 接口将接受 TCP 连接，阻塞等待连接，若队列中已有连接，则可立即返回。
套接字需要通过 close 显式关闭。

父类型：

- [ServerSocket](net_package_interfaces.md#interface-serversocket)

### prop backlogSize

```cangjie
public mut prop backlogSize: Int64
```

功能：设置和读取 `backlog` 大小。

仅可在调用 `bind` 前调用，否则将抛出异常。
变量是否生效取决于系统行为。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当在 `bind` 后调用时，抛出异常。

### prop bindToDevice

```cangjie
public mut prop bindToDevice: ?String
```

功能：设置和读取绑定网卡。

类型：?[String](../../core/core_package_api/core_package_structs.md#struct-string)

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

### prop reuseAddress

```cangjie
public mut prop reuseAddress: Bool
```

功能：设置和读取 `SO_REUSEADDR` 属性，默认设置为 `true`。

属性生效后的行为取决于系统，使用前，请参阅不同系统针对此属性 `SO_REUSEADDR/SOCK_REUSEADDR` 的说明文档。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### prop reusePort

```cangjie
public mut prop reusePort: Bool
```

功能：设置和读取 `SO_REUSEPORT` 属性。

仅可在绑定前被修改。Windows 上可使用 `SO_REUSEADDR`，无该属性，抛出异常。
属性默认及配置生效后的行为取决于系统，使用前，请参阅不同系统针对此属性 `SO_REUSEPORT` 的说明文档。
同时开启 `SO_REUSEADDR/SO_REUSEPORT` 会导致不可预知的系统错误，用户需谨慎配置值。

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

### init(SocketAddress)

```cangjie
public init(bindAt!: SocketAddress)
```

功能：创建一个 [TcpServerSocket](net_package_classes.md#class-tcpserversocket) 实例，尚未绑定，因此客户端无法连接。

参数：

- bindAt!: [SocketAddress](net_package_classes.md#class-socketaddress) - 指定本地绑定地址，端口号设置为 0 表示随机绑定空闲的本地地址。