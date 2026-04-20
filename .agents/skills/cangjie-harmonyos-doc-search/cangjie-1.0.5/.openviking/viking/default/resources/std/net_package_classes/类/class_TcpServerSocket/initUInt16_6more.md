### init(UInt16)

```cangjie
public init(bindAt!: UInt16)
```

功能：创建一个 [TcpServerSocket](net_package_classes.md#class-tcpserversocket) 实例，尚未绑定，因此客户端无法连接。

参数：

- bindAt!: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 指定本地绑定端口，0 表示随机绑定空闲的本地端口。

### func accept()

```cangjie
public override func accept(): TcpSocket
```

功能：监听或接受客户端连接。阻塞等待。

返回值：

- [TcpSocket](net_package_classes.md#class-tcpsocket) - 客户端套接字。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因监听失败时，抛出异常。

### func accept(?Duration)

```cangjie
public override func accept(timeout!: ?Duration): TcpSocket
```

功能：监听或接受客户端连接。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 超时时间。

返回值：

- [TcpSocket](net_package_classes.md#class-tcpsocket) - 客户端套接字。

异常：

- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当连接超时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因监听失败时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### func bind()

```cangjie
public override func bind(): Unit
```

功能：绑定本地端口失败后需要 `close` 套接字，不支持多次重试。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因绑定失败时，抛出异常。

### func close()

```cangjie
public override func close(): Unit
```

功能：关闭套接字。接口允许多次调用。

### func getSocketOption(Int32, Int32, CPointer\<Unit>, CPointer\<UIntNative>)

```cangjie
public func getSocketOption(
    level: Int32,
    option: Int32,
    value: CPointer<Unit>,
    valueLength: CPointer<UIntNative>
): Unit
```

功能：获取指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Unit](../../core/core_package_api/core_package_intrinsics.md#unit)> - 参数值。
- valueLength: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)> - 参数值长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `getsockopt` 返回失败时，抛出异常。