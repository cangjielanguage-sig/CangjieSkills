### func getSocketOption(Int32, Int32, CPointer\<Byte>, CPointer\<Int32>)

```cangjie
public unsafe func getSocketOption(level: Int32, option: Int32, value: CPointer<Byte>, len: CPointer<Int32>): Unit
```

功能：获取套接字选项的值。

参数：

- level: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字选项级别。
- option: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字选项名。
- value: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 套接字选项值。
- len: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> - 套接字选项值的长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或获取套接字选项失败时，抛出异常。

### func listen(Int32)

```cangjie
public func listen(backlog: Int32): Unit
```

功能：监听当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例绑定的地址。

参数：

- backlog: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 等待队列增长的最大长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或监听失败时，抛出异常。

### func receive(Array\<Byte>, Int32)

```cangjie
public func receive(buffer: Array<Byte>, flags: Int32): Int64
```

功能：接收来自连接对端发送的数据。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储接收数据的数组。
- flags: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指定函数行为的标志。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 数据长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或接收数据失败时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当超过指定的读超时时间时，抛出异常。

### func receiveFrom(Array\<Byte>, Int32)

```cangjie
public func receiveFrom(buffer: Array<Byte>, flags: Int32): (RawAddress, Int64)
```

功能：接收来自其他 [RawSocket](net_package_classes.md#class-rawsocket) 实例的数据。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储接收数据的数组。
- flags: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指定函数行为的标志。

返回值：

- ([RawAddress](net_package_structs.md#struct-rawaddress), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 数据来源的地址和数据长度。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或接收数据失败时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当超过指定的读超时时间时，抛出异常。