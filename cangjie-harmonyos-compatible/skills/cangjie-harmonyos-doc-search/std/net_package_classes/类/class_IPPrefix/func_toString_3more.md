### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [IPPrefix](net_package_classes.md#class-ipprefix)  的文本表示字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [IPPrefix](net_package_classes.md#class-ipprefix) 的文本表示字符串，比如 `192.168.0.0/16` 或 `fc00::/16`。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let v4: IPPrefix = IPAddress.parse("192.168.1.2").getPrefix(24)
    let v6: IPPrefix = IPAddress.parse("2001:0250:1006:dff0:4913:2aa5:8075:7c10").getPrefix(32)
    @Assert(v4.toString(), "192.168.1.2/24")
    @Assert(v6.toString(), "2001:250:1006:dff0:4913:2aa5:8075:7c10/32")
}
```

### operator func !=(IPPrefix)

```cangjie
public operator func !=(rhs: IPPrefix): Bool
```

功能：判断两个 [IPPrefix](net_package_classes.md#class-ipprefix) 对象是否不等。

参数：

- rhs: [IPPrefix](net_package_classes.md#class-ipprefix) - 参与比较的 [IPPrefix](net_package_classes.md#class-ipprefix) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPPrefix](net_package_classes.md#class-ipprefix) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func ==(IPPrefix)

```cangjie
public operator func ==(rhs: IPPrefix): Bool
```

功能：判断两个 [IPPrefix](net_package_classes.md#class-ipprefix) 对象是否相等。

参数：

- rhs: [IPPrefix](net_package_classes.md#class-ipprefix) - 参与比较的 [IPPrefix](net_package_classes.md#class-ipprefix) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPPrefix](net_package_classes.md#class-ipprefix) 对象相等，则返回 `true`；否则，返回 `false`。