## class IPPrefix

```cangjie
sealed abstract class IPPrefix <: Equatable<IPPrefix> & Hashable & ToString
```

功能：这个类表示一个 IP 前缀，即一个连续的 IP 地址块，边界为 2 的幂（也称为“IP 子网”）。

一个 IP 前缀由两条信息指定：

- 起始 IP 地址（IPv4 或 IPv6）。这是前缀的第一个 IP 地址。
- 前缀长度。这通过指定 IP 地址中的位数来指定前缀的长度，从网络字节顺序中的最高有效位开始，对于前缀中的所有地址都是恒定的。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[IPPrefix](#class-ipprefix)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop address

```cangjie
public prop address: IPAddress
```

功能：获取构造当前 [IPPrefix](net_package_classes.md#class-ipprefix) 对象时的 [IPAddress](net_package_classes.md#class-ipaddress) 地址。

类型：[IPAddress](net_package_classes.md#class-ipaddress)

### prop prefixLength

```cangjie
public prop prefixLength: UInt8
```

功能：获取前缀长度。

类型：[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)

### static func parse(String)

```cangjie
public static func parse(s: String): IPPrefix
```

功能：将 IP 协议的 Socket 字符串转换为 [IPPrefix](net_package_classes.md#class-ipprefix) 对象。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 协议的 Socket 字符串。

异常：

- [IllegalFormatException](../../core/core_package_api/core_package_exceptions.md#class-illegalformatexception) - 如果不是合法字符串，抛出异常。

返回值：

- [IPPrefix](net_package_classes.md#class-ipprefix) - [IPPrefix](net_package_classes.md#class-ipprefix) 对象。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: IPPrefix = IPPrefix.parse("192.168.1.2/24")
    let v6: IPPrefix = IPPrefix.parse("2001:0250:1006:dff0:4913:2aa5:8075:7c10/32")
    @Assert(v4.toString(), "192.168.1.2/24")
    @Assert(v6.toString(), "2001:250:1006:dff0:4913:2aa5:8075:7c10/32")
}
```

### static func tryParse(String)

```cangjie
public static func tryParse(s: String): ?IPPrefix
```

功能：将 IP 协议的 Socket 字符串转换为 [IPPrefix](net_package_classes.md#class-ipprefix) 对象，如果不是合法字符串，则返回 `None`。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 协议的 Socket 字符串。

返回值：

- ?[IPPrefix](net_package_classes.md#class-ipprefix) - ?[IPPrefix](net_package_classes.md#class-ipprefix) 对象。

示例：
<!-- run -->
```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: ?IPPrefix = IPPrefix.tryParse("192.168.1.2/24")
    let v6: ?IPPrefix = IPPrefix.tryParse("2001:0250:1006:dff0:4913:2aa5:8075:7c10/32")
    @Assert(v4.toString(), "Some(192.168.1.2/24)")
    @Assert(v6.toString(), "Some(2001:250:1006:dff0:4913:2aa5:8075:7c10/32)")
}
```

### func broadcast()

```cangjie
public open func broadcast(): IPAddress
```

功能：返回此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的广播地址。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - 此 [IPPrefix](net_package_classes.md#class-ipprefix) 地址的广播地址。