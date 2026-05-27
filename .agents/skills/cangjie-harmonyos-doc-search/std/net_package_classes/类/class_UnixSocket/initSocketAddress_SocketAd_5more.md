### init(SocketAddress, ?SocketAddress)

```cangjie
public init(address: SocketAddress, localAddress!: ?SocketAddress = None)
```

功能：创建一个未连接的 [UnixSocket](net_package_classes.md#class-unixsocket) 实例。

参数：

- address: [SocketAddress](net_package_classes.md#class-socketaddress) - 连接的套接字地址。
- localAddress!: ?[SocketAddress](net_package_classes.md#class-socketaddress) - 需要 bind 的本地套接字地址；默认值为 `None`。

### init(String, ?String)

```cangjie
public init(path: String, localPath!: ?String = None)
```

功能：创建一个未连接的 [UnixSocket](net_package_classes.md#class-unixsocket) 实例。

此文件类型可通过 [isSock()](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated) 判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接的文件地址。
- localPath!: ?[String](../../core/core_package_api/core_package_structs.md#struct-string) - 需要 bind 的本地套接字地址路径；默认值为 `None`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当文件地址不合法时，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭套接字，所有操作除了 `close/isClosed` 之外，均不允许再调用。接口允许多次调用。

### func connect(?Duration)

```cangjie
public func connect(timeout!: ?Duration = None): Unit
```

功能：建立远端连接，对端拒绝时连接失败，会自动绑定本地地址，因此不需要进行额外的绑定操作。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 超时时间，`None` 表示无超时时间。Unix 与 Tcp 不同，队列已满时，调用立即返回错误，而非重试阻塞等待。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当远端地址不合法或者超时时间小于 0 时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当连接因系统原因无法建立时。抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当连接超时时。抛出异常。

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