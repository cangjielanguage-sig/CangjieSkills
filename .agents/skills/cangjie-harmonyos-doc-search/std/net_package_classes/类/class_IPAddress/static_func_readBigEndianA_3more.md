### static func readBigEndian(Array\<Byte>)

```cangjie
public static func readBigEndian(buffer: Array<Byte>): IPAddress
```

功能：从字节数组中以大端序的方式读取一个 [IPAddress](net_package_classes.md#class-ipaddress) 对象。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待读取的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [IPAddress](net_package_classes.md#class-ipaddress) 值时，抛出异常。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - [IPAddress](net_package_classes.md#class-ipaddress) 对象。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let bufferV4: Array<Byte> = [0xC0, 0xA8, 0x1, 0x2]
    let bufferV6: Array<Byte> = [0x20, 0x01, 0x02, 0x50, 0x10, 0x06, 0xdf, 0xf0, 0x49, 0x13, 0x2a, 0xa5, 0x80, 0x75,
        0x7c, 0x10]
    let v4: IPAddress = IPAddress.readBigEndian(bufferV4)
    let v6: IPAddress = IPAddress.readBigEndian(bufferV6)
    @Assert(v4.toString(), "192.168.1.2")
    @Assert(v6.toString(), "2001:250:1006:dff0:4913:2aa5:8075:7c10")
}
```

### static func resolve(AddressFamily, String)

```cangjie
public static func resolve(family: AddressFamily, domain: String): Array<IPAddress>
```

功能：解析域名，得到 [IPAddress](net_package_classes.md#class-ipaddress) 列表。

参数：

- family: [AddressFamily](net_package_structs.md#struct-addressfamily) - 地址族。
- domain: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 域名。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[IPAddress](net_package_classes.md#class-ipaddress)> - [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[IPAddress](net_package_classes.md#class-ipaddress)> 对象。

示例：
<!-- run -->

```cangjie
import std.net.*

main() {
    let iplist: Array<IPAddress> = IPAddress.resolve(AddressFamily.UNSPEC, "localhost")
    println(iplist)
}
// may output: [127.0.0.1, ::1]
```

### static func resolve(String)

```cangjie
public static func resolve(domain: String): Array<IPAddress>
```

功能：解析域名，得到 [IPAddress](net_package_classes.md#class-ipaddress) 列表。

参数：

- domain: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 域名。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[IPAddress](net_package_classes.md#class-ipaddress)> - [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[IPAddress](net_package_classes.md#class-ipaddress)> 对象。

示例：
<!-- run -->

```cangjie
import std.net.*

main() {
    let iplist: Array<IPAddress> = IPAddress.resolve("localhost")
    println(iplist)
}
// may output: [127.0.0.1, ::1]
```