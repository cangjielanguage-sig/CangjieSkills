## interface ServerSocket

```cangjie
public interface ServerSocket <: Resource & ToString {
    prop localAddress: SocketAddress
    func accept(): StreamingSocket
    func accept(timeout!: ?Duration): StreamingSocket
    func bind(): Unit
}
```

功能：提供服务端的 `Socket` 需要的接口。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop localAddress

```cangjie
prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### func accept()

```cangjie
func accept(): StreamingSocket
```

功能：接受一个客户端套接字的连接请求，阻塞式等待连接请求。

返回值：

- [StreamingSocket](net_package_interfaces.md#interface-streamingsocket) - 连接成功的客户端套接字。

### func accept(?Duration)

```cangjie
func accept(timeout!: ?Duration): StreamingSocket
```

功能：接受一个客户端套接字的连接请求，阻塞式等待连接请求。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待连接超时的时间。

返回值：

- [StreamingSocket](net_package_interfaces.md#interface-streamingsocket) - 连接成功的客户端套接字。

异常：

- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当等待连接请求超时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### func bind()

```cangjie
func bind(): Unit
```

功能：绑定套接字。

当没有设置 `reuse` 属性，本地端口、地址、文件路径已被占用或者上次绑定套接字的连接失败后需要 `close` 套接字。不支持多次重试此操作后可执行 `accept()` 操作。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因绑定失败时，抛出异常。