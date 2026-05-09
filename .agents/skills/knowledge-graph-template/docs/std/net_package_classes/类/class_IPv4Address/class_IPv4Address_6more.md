## class IPv4Address

```cangjie
public class IPv4Address <: IPAddress & ToString & Equatable<IPv4Address> & LessOrEqual<IPv4Address> {
    public static let broadcast: IPv4Address = IPv4Address(0xFF, 0xFF, 0xFF, 0xFF)
    public static let localhost: IPv4Address = IPv4Address(0x7F, 0, 0, 0x01)
    public static let unspecified: IPv4Address = IPv4Address(0, 0, 0, 0)
    public init(bits: UInt32)
    public init(a: Byte, b: Byte, c: Byte, d: Byte)
}
```

功能：此类表示 Internet 协议版本 4（IPv4）地址。由 [RFC 790](https://datatracker.ietf.org/doc/html/rfc790)、[RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) 和 [RFC 2365](https://datatracker.ietf.org/doc/html/rfc2365) 定义。

父类型：

- [IPAddress](#class-ipaddress)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[IPv4Address](#class-ipv4address)>
- [LessOrEqual](../../core/core_package_api/core_package_interfaces.md#interface-lessorequalt)\<[IPv4Address](#class-ipv4address)>

### static let broadcast

```cangjie
public static let broadcast: IPv4Address = IPv4Address(0xFF, 0xFF, 0xFF, 0xFF)
```

功能：返回 [IPv4Address](net_package_classes.md#class-ipv4address) 的广播地址：`255.255.255.255`。

类型：[IPv4Address](net_package_classes.md#class-ipv4address)

### static let localhost

```cangjie
public static let localhost: IPv4Address = IPv4Address(0x7F, 0, 0, 0x01)
```

功能：返回 [IPv4Address](net_package_classes.md#class-ipv4address) 的 `localhost` 地址：`127.0.0.1`。

类型：[IPv4Address](net_package_classes.md#class-ipv4address)

### static let unspecified

```cangjie
public static let unspecified: IPv4Address = IPv4Address(0, 0, 0, 0)
```

功能：返回表示未指定的 [IPv4Address](net_package_classes.md#class-ipv4address) 地址：`0.0.0.0`，这对应于其他语言中的常量 `INADDR_ANY`。

类型：[IPv4Address](net_package_classes.md#class-ipv4address)

### init(Byte, Byte, Byte, Byte)

```cangjie
public init(a: Byte, b: Byte, c: Byte, d: Byte)
```

功能：根据 4 个 8-bit 字节构造 [IPv4Address](net_package_classes.md#class-ipv4address) 地址对象，文本将表示为 `a.b.c.d`。

参数：

- a: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 8-bit 字节。
- b: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 8-bit 字节。
- c: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 8-bit 字节。
- d: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 8-bit 字节。

### init(UInt32)

```cangjie
public init(bits: UInt32)
```

功能：根据本机字节序 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值构造 [IPv4Address](net_package_classes.md#class-ipv4address) 地址。

参数：

- bits: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 本机字节序 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值。