## struct ProtocolType

```cangjie
public struct ProtocolType <: Equatable<ProtocolType> & ToString & Hashable {
    public static let ICMP: ProtocolType = ProtocolType(1)
    public static let IPV4: ProtocolType = ProtocolType(4)
    public static let IPV6: ProtocolType = ProtocolType(41)
    public static let RAW: ProtocolType = ProtocolType(255)
    public static let TCP: ProtocolType = ProtocolType(6)
    public static let UDP: ProtocolType = ProtocolType(17)
    public static let Unspecified: ProtocolType = ProtocolType(0)
    public init(protocol: Int32)
}
```

功能：提供了常用的套接字协议，以及通过指定 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值来构建套接字协议的功能。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ProtocolType](#struct-protocoltype)>
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### static let ICMP

```cangjie
public static let ICMP: ProtocolType = ProtocolType(1)
```

功能：指定协议类型为 `ICMP`。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let IPV4

```cangjie
public static let IPV4: ProtocolType = ProtocolType(4)
```

功能：指定协议类型为 `IPv4` 。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let IPV6

```cangjie
public static let IPV6: ProtocolType = ProtocolType(41)
```

功能：指定协议类型为 `IPv6`。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let RAW

```cangjie
public static let RAW: ProtocolType = ProtocolType(255)
```

功能：指定协议类型为 `RAW`。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let TCP

```cangjie
public static let TCP: ProtocolType = ProtocolType(6)
```

功能：指定协议类型为 `TCP`。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let UDP

```cangjie
public static let UDP: ProtocolType = ProtocolType(17)
```

功能：指定协议类型为 `UDP`。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### static let Unspecified

```cangjie
public static let Unspecified: ProtocolType = ProtocolType(0)
```

功能：不指定协议类型。

类型：[ProtocolType](net_package_structs.md#struct-protocoltype)

### init(Int32)

```cangjie
public init(protocol: Int32)
```

功能：通过指定套接字协议值创建协议。

参数：

- protocol: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 套接字协议值。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：返回当前 [ProtocolType](net_package_structs.md#struct-protocoltype) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [ProtocolType](net_package_structs.md#struct-protocoltype) 实例的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [ProtocolType](net_package_structs.md#struct-protocoltype) 实例的字符串表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [ProtocolType](net_package_structs.md#struct-protocoltype) 实例的字符串表示。