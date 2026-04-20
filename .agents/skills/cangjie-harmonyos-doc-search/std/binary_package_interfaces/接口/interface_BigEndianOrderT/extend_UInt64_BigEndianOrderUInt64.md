### extend UInt64 <: BigEndianOrder\<UInt64>

```cangjie
extend UInt64 <: BigEndianOrder<UInt64>
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 扩展 [BigEndianOrder](binary_package_interfaces.md#interface-bigendianordert) 接口，以实现将 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值和大端序字节序列的转换。

父类型：

- [BigEndianOrder](#interface-bigendianordert)\<[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)>

#### static func readBigEndian(Array\<UInt8>)

```cangjie
public static func readBigEndian(buffer: Array<UInt8>): UInt64
```

功能：从字节数组中以大端序的方式读取一个 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer: Array<UInt8> = [0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]
    let n = UInt64.readBigEndian(buffer)
    @Assert(n, 0x1234567890123456)
}
```

#### func writeBigEndian(Array\<UInt8>)

```cangjie
public func writeBigEndian(buffer: Array<UInt8>): Int64
```

功能：将 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let n = 0x1234567890123456u64.writeBigEndian(buffer)
    @Assert(n, 8)
    @Assert(buffer[..n] == [0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56])
}
```