### func receiveFrom(Array\<Byte>)

```cangjie
func receiveFrom(buffer: Array<Byte>): (SocketAddress, Int64)
```

功能：阻塞式等待收取报文到 `buffer` 中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储报文内容的缓存空间，`buffer` 应当有一个合适的大小，否则可能导致收取报文时报文被截断，并且返回的报文大小值大于 `buffer` 的大小。

返回值：

- ([SocketAddress](net_package_classes.md#class-socketaddress), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 报文发送地址和收取到的报文大小（可能为 0，或大于参数 `buffer` 大小）。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当本机缓存过小无法读取报文时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当读取超时时，抛出异常。

### func sendTo(SocketAddress, Array\<Byte>)

```cangjie
func sendTo(address: SocketAddress, payload: Array<Byte>): Unit
```

功能：发送报文到指定的远端地址，当对端无足够缓存时，此操作可能被阻塞，报文可能被丢弃。

参数：

- address: [SocketAddress](net_package_classes.md#class-socketaddress) - 需要发送到的远端地址。
- payload: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 需要发送的报文内容。