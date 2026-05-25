## class UnixSocketAddress

```cangjie
public class UnixSocketAddress <: SocketAddress & Equatable<UnixSocketAddress> {
    public init(path: Array<Byte>)
    public init(path: String)
}
```

功能：此类实现了 Unix Domain Socket 地址，Unix Domain Socket 地址封装了 Unix Domain Socket 绑定或连接到的文件系统路径，路径长度不可超过 108。

如果路径是空字符串，那么表示它是 `unnamed` 地址，如果路径以`\0` 开头，那么它是 `abstract` 地址。路径中间不可包含 `\0`。

父类型：

- [SocketAddress](#class-socketaddress)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[UnixSocketAddress](#class-unixsocketaddress)>

### prop family

```cangjie
public prop family: AddressFamily
```

功能：获取当前 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 对象的地址族，总是 [AddressFamily.UNIX](net_package_structs.md#static-const-unix)。

类型：[AddressFamily](net_package_structs.md#struct-addressfamily)

### prop size

```cangjie
public prop size: Int64
```

功能：获取当前 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 对象的原始字节长度。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Array\<Byte>)

```cangjie
public init(path: Array<Byte>)
```

功能：根据 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示的文件系统路径构造 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 地址。

参数：

- path: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>  - 文件系统路径字节数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 address 不合法，抛出异常。

### init(String)

```cangjie
public init(path: String)
```

功能：根据字符串表示的文件系统路径构造 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 地址。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件系统路径字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 address 不合法，抛出异常。

### func getAddressBytes()

```cangjie
public func getAddressBytes(): Array<Byte>
```

功能：返回此 [UnixSocketAddress](net_package_classes.md#class-unixsocketaddress) 对象的原始 IP 地址，内容布局与 `sockaddr_un` 形式一致。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 原始 IP 地址的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 表示。

示例：
<!-- run -->

```cangjie
import std.net.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let udsa1_1: UnixSocketAddress = UnixSocketAddress("/tmp/server1.sock")
    @Assert(udsa1_1.getAddressBytes(), "\u{1}\u{0}/tmp/server1.sock".toArray())
}
```

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 `hashcode` 值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - `hashcode` 值。