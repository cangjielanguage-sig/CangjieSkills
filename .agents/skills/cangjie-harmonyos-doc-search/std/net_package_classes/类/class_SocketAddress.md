## class SocketAddress

```cangjie
sealed abstract class SocketAddress <: ToString & Equatable<SocketAddress> & Hashable
```

功能：此类表示协议无关的 Socket 地址。它提供了一个不可变的对象，用于 Socket  的绑定、连接或作为返回值。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[SocketAddress](#class-socketaddress)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### prop family

```cangjie
public prop family: AddressFamily
```

功能：当前 [SocketAddress](net_package_classes.md#class-socketaddress) 对象的地址族。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### prop size

```cangjie
public prop size: Int64
```

功能：当前 [SocketAddress](net_package_classes.md#class-socketaddress) 对象的原始字节长度。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### func getAddressBytes()

```cangjie
public func getAddressBytes(): Array<Byte>
```

功能：返回此 [SocketAddress](net_package_classes.md#class-socketaddress) 对象的原始 IP 地址。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 原始 IP 地址的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示。

### operator func !=(SocketAddress)

```cangjie
public operator func !=(rhs: SocketAddress): Bool
```

功能：判断两个 [SocketAddress](net_package_classes.md#class-socketaddress) 对象是否不等。

参数：

- rhs: [SocketAddress](net_package_classes.md#class-socketaddress) - 参与比较的 [SocketAddress](net_package_classes.md#class-socketaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [SocketAddress](net_package_classes.md#class-socketaddress) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func ==(SocketAddress)

```cangjie
public operator func ==(rhs: SocketAddress): Bool
```

功能：判断两个 [SocketAddress](net_package_classes.md#class-socketaddress) 对象是否相等。

参数：

- rhs: [SocketAddress](net_package_classes.md#class-socketaddress) - 参与比较的 [SocketAddress](net_package_classes.md#class-socketaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [SocketAddress](net_package_classes.md#class-socketaddress) 对象相等，则返回 `true`；否则，返回 `false`。