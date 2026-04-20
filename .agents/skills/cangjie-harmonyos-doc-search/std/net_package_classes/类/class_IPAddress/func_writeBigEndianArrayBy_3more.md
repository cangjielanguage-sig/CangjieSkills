### func writeBigEndian(Array\<Byte>)

```cangjie
public open func writeBigEndian(buffer: Array<Byte>): Int64
```

功能：返回此 [IPAddress](net_package_classes.md#class-ipaddress) 对象以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待写入的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以写入 [IPv4Address](net_package_classes.md#class-ipv4address) 或 [IPv6Address](net_package_classes.md#class-ipv6address) 值时，抛出异常。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer = Array<Byte>(128, repeat: 0)
    let expectV4: Array<Byte> = [0xC0, 0xA8, 0x1, 0x2]
    let expectV6: Array<Byte> = [0x20, 0x01, 0x02, 0x50, 0x10, 0x06, 0xdf, 0xf0, 0x49, 0x13, 0x2a, 0xa5, 0x80, 0x75,
        0x7c, 0x10]
    let v4: IPAddress = IPAddress.parse("192.168.1.2")
    let v6: IPAddress = IPAddress.parse("2001:0250:1006:dff0:4913:2aa5:8075:7c10")
    var len = v4.writeBigEndian(buffer)
    @Assert(buffer[..len], expectV4)
    len = v6.writeBigEndian(buffer)
    @Assert(buffer[..len], expectV6)
}
```

### operator func !=(IPAddress)

```cangjie
public operator func !=(rhs: IPAddress): Bool
```

功能：判断两个 [IPAddress](net_package_classes.md#class-ipaddress) 对象是否不等。

参数：

- rhs: [IPAddress](net_package_classes.md#class-ipaddress) - 参与比较的 [IPAddress](net_package_classes.md#class-ipaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPAddress](net_package_classes.md#class-ipaddress) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func ==(IPAddress)

```cangjie
public operator func ==(rhs: IPAddress): Bool
```

功能：判断两个 [IPAddress](net_package_classes.md#class-ipaddress) 对象是否相等。

参数：

- rhs: [IPAddress](net_package_classes.md#class-ipaddress) - 参与比较的 [IPAddress](net_package_classes.md#class-ipaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPAddress](net_package_classes.md#class-ipaddress) 对象相等，则返回 `true`；否则，返回 `false`。