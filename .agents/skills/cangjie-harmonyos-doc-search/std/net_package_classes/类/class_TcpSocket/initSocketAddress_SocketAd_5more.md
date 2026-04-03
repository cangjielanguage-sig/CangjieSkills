### init(SocketAddress, ?SocketAddress)

```cangjie
public init(address: SocketAddress, localAddress!: ?SocketAddress)
```

功能：创建一个未连接的套接字，并且绑定到指定本地地址，本地地址为 `None` 时，将随机选定地址去绑定。

此接口当 `localAddress` 不为 `None` 时，将默认设置 `SO_REUSEADDR` 为 `true`，否则可能导致 "address already in use" 的错误。如果需要变更此配置，可以通过调用 setSocketOptionBool([SocketOptions](net_package_structs.md#struct-socketoptions).SOL_SOCKET, [SocketOptions](net_package_structs.md#struct-socketoptions).SO_REUSEADDR, false)。另外，本地地址和远端地址需要均为 IPv4。

参数：

- address: [SocketAddress](net_package_classes.md#class-socketaddress) - 即将要连接的地址。
- localAddress!: ?[SocketAddress](net_package_classes.md#class-socketaddress) - 绑定的本地地址。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `address` 参数不合法或者 Windows 平台下地址为全零地址时，抛出异常。

### init(String, UInt16)

```cangjie
public init(address: String, port: UInt16)
```

功能：创建一个未连接的套接字。

参数：

- address: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 即将要连接的地址。
- port: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 即将要连接的端口。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `address` 参数不合法或者 Windows 平台下地址为全零地址时，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭套接字，所有操作除了 `close/isClosed` 之外，均不允许再调用。接口允许多次调用。

### func connect(?Duration)

```cangjie
public func connect(timeout!: ?Duration = None): Unit
```

功能：连接远端套接字，会自动绑定本地地址，因此不需要进行额外的绑定操作。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 连接超时时间，`None` 表示无超时时间，并且连接操作无重试，当服务端拒绝连接时，将返回连接失败。并且此操作包含了绑定操作，因此无需重复调用 `bind` 接口。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当远端地址不合法或者连接超时时间小于 0 或者超时时间小于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当连接因系统原因（例如：套接字已关闭，没有访问权限，系统错误等）无法建立时，抛出异常。再次调用可能成功。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当连接超时时，抛出异常。

### func getSocketOption(Int32, Int32, CPointer\<Unit>, CPointer\<UIntNative>)

```cangjie
public func getSocketOption(
    level: Int32,
    option: Int32,
    value: CPointer<Unit>,
    valueLength: CPointer<UIntNative>
): Unit
```

功能：读取指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Unit](../../core/core_package_api/core_package_intrinsics.md#unit)> - 参数值。
- valueLength: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)> - 参数值长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `getsockopt` 返回失败时，抛出异常。