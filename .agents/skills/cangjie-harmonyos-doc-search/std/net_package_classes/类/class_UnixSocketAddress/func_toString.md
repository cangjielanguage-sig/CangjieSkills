### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 的文本表示字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 的文本表示字符串，比如 `/tmp/socket1` 。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let expect1 = "/tmp/server1.sock"
    let expect2 = "\u{0}/tmp/server1.sock"
    let udsa1_1: UnixSocketAddress = UnixSocketAddress("/tmp/server1.sock")
    let udsa2_1: UnixSocketAddress = UnixSocketAddress("/tmp/server1.sock".toArray())
    let udsa2_2: UnixSocketAddress = UnixSocketAddress("/tmp/server1.sock\u{0}\u{0}".toArray())
    let udsa3_1: UnixSocketAddress = UnixSocketAddress("\u{0}/tmp/server1.sock")
    let udsa4_1: UnixSocketAddress = UnixSocketAddress("\u{0}/tmp/server1.sock".toArray())
    let udsa4_2: UnixSocketAddress = UnixSocketAddress("\u{0}/tmp/server1.sock\u{0}\u{0}".toArray())
    @Assert(udsa1_1.toString(), expect1)
    @Assert(udsa2_1.toString(), expect1)
    @Assert(udsa2_2.toString(), expect1)
    @Assert(udsa3_1.toString(), expect2)
    @Assert(udsa1_1, udsa2_1)
    @Assert(udsa1_1, udsa2_2)
    @Assert(udsa3_1, udsa4_1)
    @Assert(udsa3_1, udsa4_2)
    @Assert(udsa4_1.toString(), expect2)
    @Assert(udsa4_2.toString(), expect2)

    try {
        UnixSocketAddress("/tmp/server1\u{0}.sock")
    } catch (e: IllegalArgumentException) {
        @Assert(true)
    }

    try {
        UnixSocketAddress("/tmp/server1.sock\u{0}\u{0}")
    } catch (e: IllegalArgumentException) {
        @Assert(true)
    }
    try {
        UnixSocketAddress("\u{0}/tmp/server1.sock\u{0}\u{0}")
    } catch (e: IllegalArgumentException) {
        @Assert(true)
    }
    try {
        UnixSocketAddress("/tmp/server1\u{0}.sock".toArray())
    } catch (e: IllegalArgumentException) {
        @Assert(true)
    }
    return
}
```