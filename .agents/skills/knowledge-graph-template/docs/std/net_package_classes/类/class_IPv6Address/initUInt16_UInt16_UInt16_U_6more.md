### init(UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, UInt16, ?UInt32)

```cangjie
public init(a: UInt16, b: UInt16, c: UInt16, d: UInt16, e: UInt16, f: UInt16, g: UInt16, h: UInt16, scopeId!: ?UInt32 = None)
```

功能：根据 8 个 16-bit 分段构造 [IPv6Address](net_package_classes.md#class-ipv6address) 地址对象，文本将表示为 `a:b:c:d:e:f:g:h%scopeId`。

参数：

- a: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- b: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- c: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- d: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- e: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- f: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- g: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- h: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16-bit 分段。
- scopeId!: ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 范围 ID。

### static func readBigEndian(Array\<Byte>)

```cangjie
public static func readBigEndian(buffer: Array<Byte>): IPv6Address
```

功能：从字节数组中以大端序的方式读取一个 [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待读取的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [IPv6Address](net_package_classes.md#class-ipv6address) 值时，抛出异常。

返回值：

- [IPv6Address](net_package_classes.md#class-ipv6address) - [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

### func getPrefix(UInt8)

```cangjie
public func getPrefix(prefixLen: UInt8): IPPrefix
```

功能：此 [IPv6Address](net_package_classes.md#class-ipv6address) 地址对象根据指定的网络前缀长度创建一个网络前缀对象。

参数：

- prefixLen: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 网络前缀长度，必须 \>= 0 且 <= 128。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 prefixLen 大小超出范围，抛出异常。

返回值：

- [IPPrefix](net_package_classes.md#class-ipprefix) - 网络前缀对象。

### func isGlobalUnicast()

```cangjie
public func isGlobalUnicast(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是全局单播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是全局单播地址，否则返回 false。

### func isIPv4Mapped()

```cangjie
public func isIPv4Mapped(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是 IPv4 映射地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是 IPv4 映射地址，否则返回 false。

### func isLinkLocal()

```cangjie
public func isLinkLocal(): Bool
```

功能：判断此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是不是链路本地地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是链路本地地址，否则返回 false。