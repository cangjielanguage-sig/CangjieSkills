### func isLoopback()

```cangjie
public func isLoopback(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是环回地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是环回地址，否则返回 false。

### func isMulticast()

```cangjie
public func isMulticast(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是多播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是多播地址，否则返回 false。

### func isPrivate()

```cangjie
public func isPrivate(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是私有地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是私有地址，否则返回 false。

### func isTeredo()

```cangjie
public func isTeredo(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是 `Teredo` 地址。`Teredo` 前缀为 `2001::/32`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 `Teredo` 地址，否则返回 false。

### func isUnspecified()

```cangjie
public func isUnspecified(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是“未指定” IP 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是“未指定” IP 地址，否则返回 false。

### func scope(?UInt32)

```cangjie
public func scope(scopeId: ?UInt32): IPv6Address
```

功能：使用本 [IPv6Address](net_package_classes.md#class-ipv6address) 对象的地址值和指定的范围 ID 转换为新的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象，如果指定的范围 ID 为 None，则去除已有的范围 ID。

参数：

- scopeId: ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 范围 ID。

返回值：

- [IPv6Address](net_package_classes.md#class-ipv6address) - 转换后的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

### func toIPv4()

```cangjie
public func toIPv4(): ?IPv4Address
```

功能：此 [IPv6Address](net_package_classes.md#class-ipv6address) 地址转换为 IPv4 兼容的 [IPv4Address](net_package_classes.md#class-ipv4address) 地址。比如 `::a.b.c.d` 和 `::ffff:a.b.c.d` 转成 `a.b.c.d`；  `::1` 转成 `0.0.0.1`. 所有不以全零或 `::ffff` 开头的地址将返回 `None`。

返回值：

- ?[IPv4Address](net_package_classes.md#class-ipv4address) - ?[IPv4Address](net_package_classes.md#class-ipv4address) 值。

### func toIPv4Mapped()

```cangjie
public func toIPv4Mapped(): ?IPv4Address
```

功能：此 [IPv6Address](net_package_classes.md#class-ipv6address) 地址转换为 IPv4 映射的 [IPv4Address](net_package_classes.md#class-ipv4address) 地址。比如 `::ffff:a.b.c.d` 转换为 `a.b.c.d`， 所有不以 `::ffff` 开头的地址将返回 `None`。

返回值：

- ?[IPv4Address](net_package_classes.md#class-ipv4address) - ?[IPv4Address](net_package_classes.md#class-ipv4address) 值。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [IPv6Address](net_package_classes.md#class-ipv6address)  的文本表示字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [IPv6Address](net_package_classes.md#class-ipv6address) 的文本表示字符串，比如 `2001:db8:1:2:ffff:ffff:ffff:ffff`。