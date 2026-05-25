## class IPSocketAddress

```cangjie
public class IPSocketAddress <: SocketAddress & Equatable<IPSocketAddress>{
    public init(address: Array<Byte>, port: UInt16)
    public init(address: String, port: UInt16)
    public init(address: IPAddress, port: UInt16)
}
```

功能：此类实现了 IP 协议 Socket 地址（IP 地址+端口号）。它提供了一个不可变的对象，用于 Socket  的绑定、连接或作为返回值。

父类型：

- [SocketAddress](#class-socketaddress)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[IPSocketAddress](#class-ipsocketaddress)>

### prop address

```cangjie
public prop address: IPAddress
```

功能：获取当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的 IP 地址。

类型：[IPAddress](net_package_classes.md#class-ipaddress)

### prop family

```cangjie
public prop family: AddressFamily
```

功能：获取当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的地址族。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### prop port

```cangjie
public prop port: UInt16
```

功能：获取当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的端口。

类型：[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)

### prop size

```cangjie
public prop size: Int64
```

功能：获取当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的原始字节长度。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Array\<Byte>, UInt16)

```cangjie
public init(address: Array<Byte>, port: UInt16)
```

功能：根据大端序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示的 IP 地址和本机序 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 端口构造 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 地址。

参数：

- address: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>  - 大端序 IP 地址。
- port: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 本机序端口。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 address 不合法，抛出异常。

### init(IPAddress, UInt16)

```cangjie
public init(address: IPAddress, port: UInt16)
```

功能：根据 [IPAddress](net_package_classes.md#class-ipaddress) 对象和 本机序 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 端口构造 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 地址。

参数：

- address: [IPAddress](net_package_classes.md#class-ipaddress) - [IPAddress](net_package_classes.md#class-ipaddress) 对象。
- port: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 本机序端口。

### init(String, UInt16)

```cangjie
public init(address: String, port: UInt16)
```

功能：根据字符串表示的 IP 地址和 本机序 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 端口构造 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 地址。

参数：

- address: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 地址字符串。
- port: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 本机序端口。

异常：

- [IllegalFormatException](../../core/core_package_api/core_package_exceptions.md#class-illegalformatexception) - 如果传入的 IP 地址不合法，抛出异常。