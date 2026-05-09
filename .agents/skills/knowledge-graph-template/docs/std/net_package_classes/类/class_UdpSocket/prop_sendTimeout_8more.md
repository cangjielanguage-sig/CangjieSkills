### prop sendTimeout

```cangjie
public override mut prop sendTimeout: ?Duration
```

功能：设置和读取 `send/sendTo` 操作超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### init(SocketAddress)

```cangjie
public init(bindAt!: SocketAddress)
```

功能：创建一个未绑定的 `UdpSocket` 实例。

参数：

- bindAt!: [SocketAddress](net_package_classes.md#class-socketaddress) - 绑定地址及端口。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### init(UInt16)

```cangjie
public init(bindAt!: UInt16)
```

功能：创建一个未绑定的 `UdpSocket` 实例。

参数：

- bindAt!: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 绑定端口。

### func bind()

```cangjie
public func bind(): Unit
```

功能：绑定本地端口失败后需要 `close` 套接字，不支持多次重试。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因绑定失败时，抛出异常。

### func close()

```cangjie
public override func close(): Unit
```

功能：关闭套接字，所有操作除了 `close/isClosed` 之外，均不允许再调用。接口允许多次调用。

### func connect(SocketAddress)

```cangjie
public func connect(remote: SocketAddress): Unit
```

功能：连接特定远端地址，可通过 `disconnect` 撤销配置。

仅接受该远端地址的报文。必须在调用 `bind` 后执行。此操作执行后，端口将开始接收 ICMP 报文，若收到异常报文后，可能导致 `send/sendTo` 执行失败。

参数：

- remote: [SocketAddress](net_package_classes.md#class-socketaddress) - 远端地址。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当远端地址不合法时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当端口未绑定、连接因系统原因无法建立或者 Windows 平台下远端地址为全零地址时，抛出异常。

### func disconnect()

```cangjie
public func disconnect(): Unit
```

功能：停止连接。取消仅收取特定对端报文。可在 `connect` 前调用，可多次调用。

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