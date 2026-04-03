### func accept(?Duration)

```cangjie
public override func accept(timeout!: ?Duration): UnixSocket
```

功能：等待接受一个客户端的连接，或从队列中读取连接。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 超时时间。

返回值：

- [UnixSocket](net_package_classes.md#class-unixsocket) - 连接的客户端套接字。

异常：

- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当连接超时时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### func bind()

```cangjie
public override func bind(): Unit
```

功能：绑定一个 `Unix domain` 套接字，并创建监听队列。

此接口自动在本地地址中创建一个套接字文件，如该文件已存在则会绑定失败。此文件类型可通过 [isSock()](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated) 接口判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除，失败后需要 `close` 套接字，不支持多次重试。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当因系统原因绑定失败时，抛出异常。

### func close()

```cangjie
public override func close(): Unit
```

功能：关闭套接字，该套接字的所有操作除了 `close/isClosed` 之外，均不允许再调用。此接口允许多次调用。

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

### func getSocketOptionBool(Int32, Int32)

```cangjie
public func getSocketOptionBool(
    level: Int32,
    option: Int32
): Bool
```

功能：获取指定的套接字参数。从 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 强转而来。`0 => false，非 0 => true`。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回指定的套接字参数。从 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 强转而来。`0 => false，非 0 => true`。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `getsockopt` 返回失败时或参数大小超过 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 的阈值时，抛出异常。