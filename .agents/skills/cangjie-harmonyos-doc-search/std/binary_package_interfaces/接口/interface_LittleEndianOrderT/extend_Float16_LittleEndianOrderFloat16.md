### extend Float16 <: LittleEndianOrder\<Float16>

```cangjie
extend Float16 <: LittleEndianOrder<Float16>
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 扩展 [LittleEndianOrder](binary_package_interfaces.md#interface-littleendianordert) 接口，以实现将 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值和小端序字节序列的转换。

父类型：

- [LittleEndianOrder](#interface-littleendianordert)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

#### static func readLittleEndian(Array\<UInt8>)

```cangjie
public static func readLittleEndian(buffer: Array<UInt8>): Float16
```

功能：从字节数组中以小端序的方式读取一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer: Array<UInt8> = [0x40, 0x4A]
    let n = Float16.readLittleEndian(buffer)
    @Assert(n, 12.5)
}
```

#### func writeLittleEndian(Array\<UInt8>)

```cangjie
public func writeLittleEndian(buffer: Array<UInt8>): Int64
```

功能：将 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值以小端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let n = 12.5f16.writeLittleEndian(buffer)
    @Assert(n, 2)
    @Assert(buffer[..n] == [0x40, 0x4A])
}
```