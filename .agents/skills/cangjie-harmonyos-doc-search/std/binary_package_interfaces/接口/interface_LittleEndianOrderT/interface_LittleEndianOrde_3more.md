## interface LittleEndianOrder\<T>

```cangjie
public interface LittleEndianOrder<T> {
    func writeLittleEndian(buffer: Array<UInt8>): Int64
    static func readLittleEndian(buffer: Array<UInt8>): T
}
```

功能：小端序字节序列转换接口。

### static func readLittleEndian(Array\<UInt8>)

```cangjie
static func readLittleEndian(buffer: Array<UInt8>): T
```

功能：从字节数组中以小端序的方式读取一个 T 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- T - T 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 T 值时，抛出异常。

### func writeLittleEndian(Array\<UInt8>)

```cangjie
func writeLittleEndian(buffer: Array<UInt8>): Int64
```

功能：将 T 值以小端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 T 值时，抛出异常。