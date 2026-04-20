## struct SocketDomain

```cangjie
public struct SocketDomain <: Equatable<SocketDomain> & ToString & Hashable {
    public static let IPV4: SocketDomain = SocketDomain(2)
    public static let IPV6: SocketDomain
    public static let NETLINK: SocketDomain = SocketDomain(16)
    public static let PACKET: SocketDomain = SocketDomain(17)
    public static let UNIX: SocketDomain
    public init(domain: Int32)
}
```

功能：提供了常用的套接字通信域，以及通过指定 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值来构建套接字通信域的功能。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[SocketDomain](#struct-socketdomain)>
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)

### static let IPV4

```cangjie
public static let IPV4: SocketDomain = SocketDomain(2)
```

功能：`IPv4` 通信域。

类型：[SocketDomain](net_package_structs.md#struct-socketdomain)

### static let IPV6

```cangjie
public static let IPV6: SocketDomain
```

功能：`IPv6` 通信域。不同系统下的值分别为：

- macOS: SocketDomain(30)
- Windows: SocketDomain(23)
- 其他情况：SocketDomain(10)

类型：[SocketDomain](net_package_structs.md#struct-socketdomain)

### static let NETLINK

```cangjie
public static let NETLINK: SocketDomain = SocketDomain(16)
```

功能：内核和用户空间进程之间通信。

> **注意：**
>
> 该常量在 Windows 和 macOS 平台不提供。

类型：[SocketDomain](net_package_structs.md#struct-socketdomain)

### static let PACKET

```cangjie
public static let PACKET: SocketDomain = SocketDomain(17)
```

功能：允许用户空间程序直接访问网络数据包。

> **注意：**
>
> 该常量在 Windows 和 macOS 平台不提供。

类型：[SocketDomain](net_package_structs.md#struct-socketdomain)

### static let UNIX

```cangjie
public static let UNIX: SocketDomain
```

功能：本机通信。不同系统下的值分别为：

- Windows: SocketDomain(0)
- 其他情况：SocketDomain(1)

类型：[SocketDomain](net_package_structs.md#struct-socketdomain)

### init(Int32)

```cangjie
public init(domain: Int32)
```

功能：根据指定通信域值创建套接字通信域。

参数：

- domain: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 通信域值。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：返回当前 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例的字符串表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例的字符串表示。

### operator func !=(SocketDomain)

```cangjie
public operator func !=(r: SocketDomain): Bool
```

功能：比较两个 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例是否不等。

参数：

- r: [SocketDomain](net_package_structs.md#struct-socketdomain) - 参与比较的 [SocketDomain](net_package_structs.md#struct-socketdomain) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当二者代表的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值不等时，返回 `true`；否则，返回 `false`。