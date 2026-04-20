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

### func setSocketOptionBool(Int32, Int32, Bool)

```cangjie
public func setSocketOptionBool(
    level: Int32,
    option: Int32,
    value: Bool
): Unit
```

功能：设置指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 参数值。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `setsockopt` 返回失败时，抛出异常。

### func setSocketOptionIntNative(Int32, Int32, IntNative)

```cangjie
public func setSocketOptionIntNative(
    level: Int32,
    option: Int32,
    value: IntNative
): Unit
```

功能：设置指定的套接字参数。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 层级，例如 `SOL_SOCKET`。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 参数，例如 `SO_KEEPALIVE`。
- value: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 参数值。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `setsockopt` 返回失败时，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：返回当前 [TcpSocket](net_package_classes.md#class-tcpsocket) 的状态信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 包含当前 [TcpSocket](net_package_classes.md#class-tcpsocket) 状态信息的字符串。

### func write(Array\<Byte>)

```cangjie
public override func write(payload: Array<Byte>): Unit
```

功能：写入报文。超时情况按 `writeTimeout` 决定，详见 `writeTimeout`。

参数：

- payload: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储写入数据的缓冲区。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `buffer` 大小为 0 或者当因系统原因写入失败时，抛出异常。

### operator func !=(TcpSocket)

```cangjie
public override operator func !=(other: TcpSocket): Bool
```

功能：判断两个 [TcpSocket](net_package_classes.md#class-tcpsocket) 实例是否不等。

参数：

- other: [TcpSocket](net_package_classes.md#class-tcpsocket) - 参与比较的 [TcpSocket](net_package_classes.md#class-tcpsocket) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [TcpSocket](net_package_classes.md#class-tcpsocket) 实例不等，则返回 `true`；否则，返回 `false`。