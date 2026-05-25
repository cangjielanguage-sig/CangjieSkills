## struct RawAddress

```cangjie
public struct RawAddress {
    public init(addr: Array<Byte>)
}
```

功能：提供了 [RawSocket](net_package_classes.md#class-rawsocket) 的通信地址创建和获取功能。

### prop addr

```cangjie
public prop addr: Array<Byte>
```

功能：获取地址。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>

### init(Array\<Byte>)

```cangjie
public init(addr: Array<Byte>)
```

功能：根据字节数组创建地址。

参数：

- addr: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储地址的字节数组。