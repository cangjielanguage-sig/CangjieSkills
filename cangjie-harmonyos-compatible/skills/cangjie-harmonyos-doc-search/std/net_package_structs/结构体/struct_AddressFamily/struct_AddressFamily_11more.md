## struct AddressFamily

```cangjie
public struct AddressFamily <: ToString & Equatable<AddressFamily> {
    public static const INET: AddressFamily = AddressFamily("INET", 2)
    public static const INET6: AddressFamily
    public static const NETLINK: AddressFamily
    public static const UNIX: AddressFamily = AddressFamily("UNIX", 1)
    public static const UNSPEC: AddressFamily = AddressFamily("UNSPEC", 0)
    public let name: String
    public let value: UInt16
    public const init(name: String, value: UInt16)
}
```

功能：[AddressFamily](net_package_structs.md#struct-addressfamily) 地址族用于指示 `Socket` 的寻址方案，常用的有 `INET` / `INET6` / `UNIX` 地址族。地址族标识符最初在 [RFC 2453](https://datatracker.ietf.org/doc/html/rfc2453) 中定义。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[AddressFamily](#struct-addressfamily)>

### static const INET

```cangjie
public static const INET: AddressFamily = AddressFamily("INET", 2)
```

功能：IPv4 地址族。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### static const INET6

```cangjie
public static const INET6: AddressFamily
```

功能：IPv6 地址族。不同系统下的值分别为：

- macOS: AddressFamily("INET6", 30)
- Windows: AddressFamily("INET6", 23)
- 其他情况：AddressFamily("INET6", 10)

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### static const NETLINK

```cangjie
public static const NETLINK: AddressFamily
```

功能：NetLink 地址族，仅 Linux 下支持，其值为：

- Linux: AddressFamily("NETLINK", 16)

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### static const UNIX

```cangjie
public static const UNIX: AddressFamily = AddressFamily("UNIX", 1)
```

功能：unix domain socket 地址族。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### static const UNSPEC

```cangjie
public static const UNSPEC: AddressFamily = AddressFamily("UNSPEC", 0)
```

功能：未指定的地址族。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### let name

```cangjie
public let name: String
```

功能：地址族名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### let value

```cangjie
public let value: UInt16
```

功能：地址族值。

类型：[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)

### init(String, UInt16)

```cangjie
public const init(name: String, value: UInt16)
```

功能：常量构造函数，创建 [AddressFamily](net_package_structs.md#struct-addressfamily) 对象。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 地址族名。
- value: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 地址族值。

### func toString()

```cangjie
public func toString(): String
```

功能：获取地址族对应的名称。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前地址族的名称。

### operator func !=(AddressFamily)

```cangjie
public operator func !=(rhs: AddressFamily): Bool
```

功能：比较地址族值是否不等。

参数：

- rhs: [AddressFamily](net_package_structs.md#struct-addressfamily) - 参与比较的 [AddressFamily](net_package_structs.md#struct-addressfamily) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [AddressFamily](net_package_structs.md#struct-addressfamily) 对象不等，则返回 `true`；否则，返回 `false`。