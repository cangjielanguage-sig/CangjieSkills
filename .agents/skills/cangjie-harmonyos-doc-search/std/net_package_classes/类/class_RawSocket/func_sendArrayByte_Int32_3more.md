### func send(Array\<Byte>, Int32)

```cangjie
public func send(buffer: Array<Byte>, flags: Int32): Unit
```

功能：向连接的对端发送数据。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 数据。
- flags: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指定函数行为的标志。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或发送数据失败时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当超过指定的写超时时间时，抛出异常。

### func sendTo(RawAddress, Array\<Byte>, Int32)

```cangjie
public func sendTo(addr: RawAddress, buffer: Array<Byte>, flags: Int32): Unit
```

功能：向目标地址发送数据。若 [RawSocket](net_package_classes.md#class-rawsocket) 是 `DATAGRAM` 类型，发送的数据包大小不允许超过 65507 字节。

参数：

- addr: [RawAddress](net_package_structs.md#struct-rawaddress) - 发送数据的目标地址。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 数据。
- flags: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指定函数行为的标志。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭、发送数据失败或者 macOS 平台下 `connect` 被调用后调用 `sendTo` 时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当超过指定的写超时时间时，抛出异常。

### func setSocketOption(Int32, Int32, CPointer\<Byte>, Int32)

```cangjie
public unsafe func setSocketOption(level: Int32, option: Int32, value: CPointer<Byte>, len: Int32): Unit
```

功能：设置套接字选项。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字选项级别。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字选项名。
- value: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 套接字选项值。
- len: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字选项值的长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或设置套接字选项失败时，抛出异常。