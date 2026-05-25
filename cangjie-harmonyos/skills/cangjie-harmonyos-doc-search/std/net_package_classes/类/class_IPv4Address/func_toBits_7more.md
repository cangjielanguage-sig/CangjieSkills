### func toBits()

```cangjie
public func toBits(): UInt32
```

功能：此 [IPv4Address](net_package_classes.md#class-ipv4address) 地址转换为本机字节序的 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 本机字节序的 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值。

### func toIPv6Compatible()

```cangjie
public func toIPv6Compatible(): IPv6Address
```

功能：此 [IPv4Address](net_package_classes.md#class-ipv4address) 地址转换为 IPv4 兼容的 [IPv6Address](net_package_classes.md#class-ipv4address) 地址。`a.b.c.d` 变为 `::a.b.c.d`。

返回值：

- [IPv6Address](net_package_classes.md#class-ipv4address) - [IPv6Address](net_package_classes.md#class-ipv4address) 对象。

### func toIPv6Mapped()

```cangjie
public func toIPv6Mapped(): IPv6Address
```

功能：此 [IPv4Address](net_package_classes.md#class-ipv4address) 地址转换为 IPv4 映射的 [IPv6Address](net_package_classes.md#class-ipv4address) 地址。`a.b.c.d` 变为 `::ffff:a.b.c.d`。

返回值：

- [IPv6Address](net_package_classes.md#class-ipv4address) - [IPv6Address](net_package_classes.md#class-ipv4address) 对象。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [IPv4Address](net_package_classes.md#class-ipv4address)  的文本表示字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [IPv4Address](net_package_classes.md#class-ipv4address) 的文本表示字符串，比如 `a.b.c.d`。

### func writeBigEndian(Array\<Byte>)

```cangjie
public func writeBigEndian(buffer: Array<Byte>): Int64
```

功能：此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待写入的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以写入 [IPv4Address](net_package_classes.md#class-ipv4address) 值时，抛出异常。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

### operator func !=(IPv4Address)

```cangjie
public operator func !=(rhs: IPv4Address): Bool
```

功能：判断两个 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是否不等。

参数：

- rhs: [IPv4Address](net_package_classes.md#class-ipv4address) - 参与比较的 [IPv4Address](net_package_classes.md#class-ipv4address) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPv4Address](net_package_classes.md#class-ipv4address) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func <=(IPv4Address)

```cangjie
public operator func <=(rhs: IPv4Address): Bool
```

功能：判断本 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是否小于等于被比较的 [IPv4Address](net_package_classes.md#class-ipv4address) 对象。

参数：

- rhs: [IPv4Address](net_package_classes.md#class-ipv4address) - 被比较的 [IPv4Address](net_package_classes.md#class-ipv4address) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果本 [IPv4Address](net_package_classes.md#class-ipv4address) 对象小于等于被比较的 [IPv4Address](net_package_classes.md#class-ipv4address) 对象，则返回 `true`；否则，返回 `false`。