### func isIPv4()

```cangjie
public func isIPv4(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是 IPv4 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 IPv4 地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    @Assert(IPAddress.parse("192.168.1.2").isIPv4(), true)
}
```

### func isIPv6()

```cangjie
public func isIPv6(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是 IPv6 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 IPv6 地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    @Assert(IPAddress.parse("2001:250:1006:dff0:4913:2aa5:8075:7c10").isIPv6(), true)
}
```

### func isLinkLocal()

```cangjie
public open func isLinkLocal(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是链路本地地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是链路本地地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    // 169.254.0.0 ~ 169.254.255.255
    @Assert(IPAddress.parse("169.254.0.1").isLinkLocal(), true)
    // fe80::/10
    @Assert(IPAddress.parse("fe80::1").isLinkLocal(), true)
}
```

### func isLoopback()

```cangjie
public open func isLoopback(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是环回地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是环回地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    @Assert(IPAddress.parse("127.0.0.1").isLoopback(), true)
    @Assert(IPAddress.parse("::1").isLoopback(), true)
}
```

### func isMulticast()

```cangjie
public open func isMulticast(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是多播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是多播地址，否则返回 false。

### func isPrivate()

```cangjie
public open func isPrivate(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是私有地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是私有地址，否则返回 false。

### func isUnspecified()

```cangjie
public open func isUnspecified(): Bool
```

功能：判断此 [IPAddress](net_package_classes.md#class-ipaddress) 对象是不是“未指定” IP 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是“未指定” IP 地址，否则返回 false。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    @Assert(IPAddress.parse("0.0.0.0").isUnspecified(), true)
    @Assert(IPAddress.parse("::").isUnspecified(), true)
}
```