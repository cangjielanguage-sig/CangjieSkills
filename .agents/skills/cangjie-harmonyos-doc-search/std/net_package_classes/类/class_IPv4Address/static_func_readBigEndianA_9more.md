### static func readBigEndian(Array\<Byte>)

```cangjie
public static func readBigEndian(buffer: Array<Byte>): IPv4Address
```

功能：从字节数组中以大端序的方式读取一个 [IPv4Address](net_package_classes.md#class-ipv4address) 对象。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待读取的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [IPv4Address](net_package_classes.md#class-ipv4address) 值时，抛出异常。

返回值：

- [IPv4Address](net_package_classes.md#class-ipv4address) - [IPv4Address](net_package_classes.md#class-ipv4address) 对象。

### func getPrefix(UInt8)

```cangjie
public func getPrefix(prefixLen: UInt8): IPPrefix
```

功能：将 [IPv4Address](net_package_classes.md#class-ipv4address) 地址根据指定的网络前缀长度创建一个网络前缀对象。

参数：

- prefixLen: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 网络前缀长度，必须 \>= 0 且 <= 32。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 prefixLen 大小超出范围，抛出异常。

返回值：

- [IPPrefix](net_package_classes.md#class-ipprefix) - 网络前缀对象。

### func isBroadcast()

```cangjie
public func isBroadcast(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是广播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是广播地址，否则返回 false。

### func isGlobalUnicast()

```cangjie
public func isGlobalUnicast(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是全局单播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是全局单播地址，否则返回 false。

### func isLinkLocal()

```cangjie
public func isLinkLocal(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是链路本地地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是链路本地地址，否则返回 false。

### func isLoopback()

```cangjie
public func isLoopback(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是环回地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是环回地址，否则返回 false。

### func isMulticast()

```cangjie
public func isMulticast(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是多播地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是多播地址，否则返回 false。

### func isPrivate()

```cangjie
public func isPrivate(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是私有地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是私有地址，否则返回 false。

### func isUnspecified()

```cangjie
public func isUnspecified(): Bool
```

功能：判断此 [IPv4Address](net_package_classes.md#class-ipv4address) 对象是不是“未指定” IP 地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示是“未指定” IP 地址，否则返回 false。