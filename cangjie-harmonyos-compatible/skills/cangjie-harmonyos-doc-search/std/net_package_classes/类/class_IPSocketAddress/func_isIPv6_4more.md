### func isIPv6()

```cangjie
public func isIPv6(): Bool
```

功能：判断此 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象是不是 IPv6 Socket 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 IPv6 地址，否则返回 false。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 的文本表示字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 的文本表示字符串，比如 `192.168.1.2:8080` 或 `[fc00::/16]:8080` 。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: IPSocketAddress = IPSocketAddress.parse("192.168.1.2:8080")
    let v6: IPSocketAddress = IPSocketAddress.parse("[2001:0250:1006:dff0:4913:2aa5:8075:7c10]:8080")
    @Assert(v4.toString(), "192.168.1.2:8080")
    @Assert(v6.toString(), "[2001:250:1006:dff0:4913:2aa5:8075:7c10]:8080")
}
```

### operator func !=(IPSocketAddress)

```cangjie
public operator func !=(rhs: IPSocketAddress): Bool
```

功能：判断两个 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象是否不等。

参数：

- rhs: [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) - 参与比较的 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func ==(IPSocketAddress)

```cangjie
public operator func ==(rhs: IPSocketAddress): Bool
```

功能：判断两个 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象是否相等。

参数：

- rhs: [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) - 参与比较的 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPSocketAddress](net_package_classes.md#class-ipsocketaddress) 对象相等，则返回 `true`；否则，返回 `false`。