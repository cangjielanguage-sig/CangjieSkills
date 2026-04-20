### func send(Array\<Byte>)

```cangjie
public func send(payload: Array<Byte>): Unit
```

功能：发送报文到 `connect` 连接到的地址。

参数：

- payload: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 发送报文内容。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `payload` 的大小超出系统限制或者系统发送失败（例如：当 `connect` 被调用，并且收到异常 ICMP 报文时，发送失败）时，抛出异常。

### func sendTo(SocketAddress, Array\<Byte>)

```cangjie
public override func sendTo(recipient: SocketAddress, payload: Array<Byte>): Unit
```

功能：发送报文。当没有足够的缓存地址时可能会被阻塞。

参数：

- recipient: [SocketAddress](net_package_classes.md#class-socketaddress) - 发送的对端地址。
- payload: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 发送报文内容。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `payload` 的大小超出系统限制、系统发送失败（例如：当 `connect` 被调用，并且收到异常 ICMP 报文时，发送失败）、Windows 平台下远端地址为全零地址或者 macOS 平台下 `connect` 被调用后调用 `sendTo` 时，抛出异常。

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