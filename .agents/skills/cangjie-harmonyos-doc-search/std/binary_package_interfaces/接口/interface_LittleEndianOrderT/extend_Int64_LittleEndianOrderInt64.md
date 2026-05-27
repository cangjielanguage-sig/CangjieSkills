### extend Int64 <: LittleEndianOrder\<Int64>

```cangjie
extend Int64 <: LittleEndianOrder<Int64>
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 扩展 [LittleEndianOrder](binary_package_interfaces.md#interface-littleendianordert) 接口，以实现将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值和小端序字节序列的转换。

父类型：

- [LittleEndianOrder](#interface-littleendianordert)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

#### static func readLittleEndian(Array\<UInt8>)

```cangjie
public static func readLittleEndian(buffer: Array<UInt8>): Int64
```

功能：从字节数组中以小端序的方式读取一个 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer: Array<UInt8> = [0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]
    let n = Int64.readLittleEndian(buffer)
    @Assert(n, 0x1234567890123456)
}
```

#### func writeLittleEndian(Array\<UInt8>)

```cangjie
public func writeLittleEndian(buffer: Array<UInt8>): Int64
```

功能：将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值以小端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let n = 0x1234567890123456i64.writeLittleEndian(buffer)
    @Assert(n, 8)
    @Assert(buffer[..n] == [0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12])
}
```