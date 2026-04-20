## class IPAddress

```cangjie
sealed abstract class IPAddress <: ToString & Equatable<IPAddress> & Hashable & BigEndianOrder<IPAddress>
```

功能：此类表示 Internet 协议（IP）地址。互联网协议地址（IP 地址）是一个数字标签，例如 *192.0.2.1* 或 *2001:0db8:0000:0000:0000:ff00:0042:8329*，分配给连接到使用互联网协议进行通信的计算机网络设备。IP 地址有两个主要功能：网络接口标识和位置寻址。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[IPAddress](#class-ipaddress)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [BigEndianOrder](../../binary/binary_package_api/binary_package_interfaces.md#interface-bigendianordert)\<[IPAddress](#class-ipaddress)>

### prop hostName

```cangjie
public prop hostName: ?String
```

功能：返回当前 [IPAddress](net_package_classes.md#class-ipaddress)  对象对应的主机名，如果无法成功解析，则为 None，当前暂未实现。

异常：

- [UnsupportedException](../../core/core_package_api/core_package_exceptions.md#class-unsupportedexception) - 如果不是合法字符串，抛出异常。

类型：?[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop size

```cangjie
public prop size: Int64
```

功能：获取 IP 地址对象字节长度。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### static func parse(String)

```cangjie
public static func parse(s: String): IPAddress
```

功能：将 IP 协议的 Socket 字符串转换为 [IPAddress](net_package_classes.md#class-ipaddress) 对象。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - IP 协议的 Socket 字符串。

返回值：

- [IPAddress](net_package_classes.md#class-ipaddress) - [IPAddress](net_package_classes.md#class-ipaddress) 对象。

异常：

- [IllegalFormatException](../../core/core_package_api/core_package_exceptions.md#class-illegalformatexception) - 如果不是合法字符串，抛出异常。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: IPAddress = IPAddress.parse("192.168.1.2")
    let v6: IPAddress = IPAddress.parse("2001:0250:1006:dff0:4913:2aa5:8075:7c10")
    @Assert(v4.toString(), "192.168.1.2")
    @Assert(v6.toString(), "2001:250:1006:dff0:4913:2aa5:8075:7c10")
}
```