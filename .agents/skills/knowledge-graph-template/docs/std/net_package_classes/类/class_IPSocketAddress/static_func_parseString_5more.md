### static func parse(String)

```cangjie
public static func parse(s: String): IPSocketAddress
```

功能：将 IP 协议的 Socket 字符串转换为 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 协议的 Socket 字符串。

返回值：

- [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) - [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象。

异常：

- [IllegalFormatException](../../core/core_package_api/core_package_exceptions.md#class-illegalformatexception) - 入参需要是合法的 socket 地址，比如 192.168.0.0:80 或 [fc00::1]:8080，否则抛出异常。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: IPSocketAddress = IPSocketAddress.parse("192.168.1.2:8080")
    let v6: IPSocketAddress = IPSocketAddress.parse("[2001:0250:1006:dff0:4913:2aa5:8075:7c10]:8080")
    @Assert(v4.address.toString(), "192.168.1.2")
    @Assert(v4.port, 8080u16)
    @Assert(v6.address.toString(), "2001:250:1006:dff0:4913:2aa5:8075:7c10")
    @Assert(v6.port, 8080u16)
    @Assert(v4.toString(), "192.168.1.2:8080")
    @Assert(v6.toString(), "[2001:250:1006:dff0:4913:2aa5:8075:7c10]:8080")
}
```

### static func tryParse(String)

```cangjie
public static func tryParse(s: String): ?IPSocketAddress
```

功能：将 IP 协议的 Socket 字符串转换为 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象，如果不是合法字符串，则返回 `None`。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 协议的 Socket 字符串。

返回值：

- ?[IPSocketAddress](net_package_classes.md#class-ipsocketaddress) - ?[IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: ?IPSocketAddress = IPSocketAddress.tryParse("192.168.1.2:8080")
    let v6: ?IPSocketAddress = IPSocketAddress.tryParse("[2001:0250:1006:dff0:4913:2aa5:8075:7c10]:8080")
    @Assert(v4.toString(), "Some(192.168.1.2:8080)")
    @Assert(v6.toString(), "Some([2001:250:1006:dff0:4913:2aa5:8075:7c10]:8080)")
}
```

### func getAddressBytes()

```cangjie
public func getAddressBytes(): Array<Byte>
```

功能：返回此 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的原始地址的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示，内容布局与 `sockaddr_in` 或 `sockaddr_in6` 一致。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象的原始地址的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 `hashcode` 值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - `hashcode` 值。

### func isIPv4()

```cangjie
public func isIPv4(): Bool
```

功能：判断此 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象是不是 IPv4 Socket 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 IPv4 地址，否则返回 false。