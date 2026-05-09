## interface ToBytes

```cangjie
public interface ToBytes {
    func toBytes(): Array<UInt8>
}
```

功能：提供对应类型的序列化功能。

### func toBytes()

```cangjie
func toBytes(): Array<UInt8>
```

功能：提供对应类型的序列化功能。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 序列化后的字节序列。