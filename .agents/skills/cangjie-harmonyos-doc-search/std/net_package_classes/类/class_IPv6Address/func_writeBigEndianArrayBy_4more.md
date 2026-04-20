### func writeBigEndian(Array\<Byte>)

```cangjie
public func writeBigEndian(buffer: Array<Byte>): Int64
```

功能：返回此 [IPv6Address](net_package_classes.md#class-ipv6address) 对象以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 缓冲区，用于存放待写入的数据。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以写入 [IPv6Address](net_package_classes.md#class-ipv6address) 值时，抛出异常。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

### operator func !=(IPv6Address)

```cangjie
public operator func !=(rhs: IPv6Address): Bool
```

功能：判断两个 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是否不等。

参数：

- rhs: [IPv6Address](net_package_classes.md#class-ipv6address) - 参与比较的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPv6Address](net_package_classes.md#class-ipv6address) 对象不等，则返回 `true`；否则，返回 `false`。

### operator func <=(IPv6Address)

```cangjie
public operator func <=(rhs: IPv6Address): Bool
```

功能：判断本 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是否小于等于被比较的 [IPv6Address](net_package_classes.md#class-ipv6address)  对象。

参数：

- rhs: [IPv6Address](net_package_classes.md#class-ipv6address) - 参与比较的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果本 [IPv6Address](net_package_classes.md#class-ipv6address) 对象小于等于被比较的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象，则返回 `true`；否则，返回 `false`。

### operator func ==(IPv6Address)

```cangjie
public operator func ==(rhs: IPv6Address): Bool
```

功能：判断两个 [IPv6Address](net_package_classes.md#class-ipv6address) 对象是否相等。

参数：

- rhs: [IPv6Address](net_package_classes.md#class-ipv6address) - 参与比较的 [IPv6Address](net_package_classes.md#class-ipv6address) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [IPv6Address](net_package_classes.md#class-ipv6address) 对象相等，则返回 `true`；否则，返回 `false`。