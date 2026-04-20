## class IPv6Address

```cangjie
public class IPv6Address <: IPAddress & ToString & Equatable<IPv6Address> & LessOrEqual<IPv6Address> {
    public static let localhost: IPv6Address = IPv6Address(0u16, 0, 0, 0, 0, 0, 0, 1)
    public static let unspecified: IPv6Address = IPv6Address(0u16, 0, 0, 0, 0, 0, 0, 0)
    public init(octets: Array<Byte>, scopeId!: ?UInt32 = None)
    public init(a: UInt16, b: UInt16, c: UInt16, d: UInt16, e: UInt16, f: UInt16, g: UInt16, h: UInt16, scopeId!: ?UInt32 = None)
}
```

功能：此类表示 Internet 协议版本 6 （IPv6）地址。由 [RFC4291](https://datatracker.ietf.org/doc/html/rfc4291)、[RFC5952](https://datatracker.ietf.org/doc/html/rfc5952)、[RFC4007](https://datatracker.ietf.org/doc/html/rfc4007) 定义。

父类型：

- [IPAddress](#class-ipaddress)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[IPv6Address](#class-ipv6address)>
- [LessOrEqual](../../core/core_package_api/core_package_interfaces.md#interface-lessorequalt)\<[IPv6Address](#class-ipv6address)>

### static let localhost

```cangjie
public static let localhost: IPv6Address = IPv6Address(0u16, 0, 0, 0, 0, 0, 0, 1)
```

功能：返回 [IPv6Address](net_package_classes.md#class-ipv6address) 的 `localhost` 地址：`::1`。

类型：[IPv6Address](net_package_classes.md#class-ipv6address)

### static let unspecified

```cangjie
public static let unspecified: IPv6Address = IPv6Address(0u16, 0, 0, 0, 0, 0, 0, 0)
```

功能：返回表示未指定的 [IPv6Address](net_package_classes.md#class-ipv6address) 地址：`::`，这对应于其他语言中的常量 `INADDR_ANY`。

类型：[IPv6Address](net_package_classes.md#class-ipv6address)

### prop scopeId

```cangjie
public prop scopeId: ?UInt32
```

功能：获取默认范围 ID。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

### init(Array\<Byte>, ?UInt32)

```cangjie
public init(octets: Array<Byte>, scopeId!: ?UInt32 = None)
```

功能：根据大端序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 构造 [IPv6Address](net_package_classes.md#class-ipv6address) 地址。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 octets 长度小于 16，抛出异常。

参数：

- octets: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 大端序字节数组。
- scopeId!: ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 范围 ID。