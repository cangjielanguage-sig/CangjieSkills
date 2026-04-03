### static func tryParse(String)

```cangjie
public static func tryParse(s: String): ?IPAddress
```

功能：将 IP 地址字符串转换为 [IPAddress](net_package_classes.md#class-ipaddress) 对象，如果不是合法字符串，则返回 `None`。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 地址字符串。

返回值：

- ?[IPAddress](net_package_classes.md#class-ipaddress) - ?[IPAddress](net_package_classes.md#class-ipaddress) 对象。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: ?IPAddress = IPAddress.tryParse("192.168.1.2")
    let v6: ?IPAddress = IPAddress.tryParse("2001:0250:1006:dff0:4913:2aa5:8075:7c10")
    @Assert(v4.toString(), "Some(192.168.1.2)")
    @Assert(v6.toString(), "Some(2001:250:1006:dff0:4913:2aa5:8075:7c10)")
}
```

### func getAddressBytes()

```cangjie
public func getAddressBytes(): Array<Byte>
```

功能：返回此 [IPAddress](net_package_classes.md#class-ipaddress) 对象的原始 IP 地址。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 原始 IP 地址的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let expectV4: Array<Byte> = [0xC0, 0xA8, 0x1, 0x2]
    let expectV6: Array<Byte> = [0x20, 0x01, 0x02, 0x50, 0x10, 0x06, 0xdf, 0xf0, 0x49, 0x13, 0x2a, 0xa5, 0x80, 0x75,
        0x7c, 0x10]
    let v4: IPAddress = IPAddress.parse("192.168.1.2")
    let v6: IPAddress = IPAddress.parse("2001:0250:1006:dff0:4913:2aa5:8075:7c10")
    @Assert(v4.getAddressBytes(), expectV4)
    @Assert(v6.getAddressBytes(), expectV6)
}
```

### func getPrefix(UInt8)

```cangjie
public open func getPrefix(prefixLen: UInt8): IPPrefix
```

功能：此 [IPAddress](net_package_classes.md#class-ipaddress) 地址对象根据指定的网络前缀长度创建一个网络前缀对象。

参数：

- prefixLen: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 网络前缀长度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 prefixLen 大小超出范围，抛出异常。

返回值：

- [IPPrefix](net_package_classes.md#class-ipprefix) - 网络前缀对象。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let prefix: IPPrefix = IPAddress.parse("192.168.1.2").getPrefix(24)
    @Assert(prefix.toString(), "192.168.1.2/24")
}
```

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 `hashcode` 值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - `hashcode` 值。

### func isGlobalUnicast()

```cangjie
public open func isGlobalUnicast(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是全局单播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是全局单播地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    // 2000::/3
    @Assert(IPAddress.parse("2001:250:1006:dff0:4913:2aa5:8075:7c10").isGlobalUnicast(), true)
}
```