### func getSocketOptionBool(Int32, Int32)

```cangjie
public func getSocketOptionBool(
    level: Int32,
    option: Int32
): Bool
```

功能：获取指定的套接字参数。从 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 强转而来。`0 => false`，非 `0 => true`。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回指定的套接字参数值。从 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 强转而来。`0 => false`，非 `0 => true`。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `getsockopt` 返回失败时或参数大小超过 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 的阈值时，抛出异常。

### func getSocketOptionIntNative(Int32, Int32)

```cangjie
public func getSocketOptionIntNative(
    level: Int32,
    option: Int32
): IntNative
```

功能：获取指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 指定的套接字参数值。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `getsockopt` 返回失败时或参数大小超过 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 的阈值时，抛出异常。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断套接字是否通过调用 `close` 显式关闭。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回套接字是否已经调用 `close` 显示关闭。是则返回 `true`；否则，返回 `false`。

### func read(Array\<Byte>)

```cangjie
public override func read(buffer: Array<Byte>): Int64
```

功能：读取报文。超时情况按 `readTimeout` 决定，详见 `readTimeout`。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 读取的数据存储变量。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 读取的数据长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `buffer` 大小为 0 或者因系统原因读取失败时，抛出异常。

### func setSocketOption(Int32, Int32, CPointer\<Unit>, UIntNative)

```cangjie
public func setSocketOption(
    level: Int32,
    option: Int32,
    value: CPointer<Unit>,
    valueLength: UIntNative
): Unit
```

功能：设置指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Unit](../../core/core_package_api/core_package_intrinsics.md#unit)> - 参数值。
- valueLength: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 参数值长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `setsockopt` 返回失败时，抛出异常。