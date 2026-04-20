### extend UInt16 <: LittleEndianOrder\<UInt16>

```cangjie
extend UInt16 <: LittleEndianOrder<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 扩展 [LittleEndianOrder](binary_package_interfaces.md#interface-littleendianordert) 接口，以实现将 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值和小端序字节序列的转换。

父类型：

- [LittleEndianOrder](#interface-littleendianordert)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### static func readLittleEndian(Array\<UInt8>)

```cangjie
public static func readLittleEndian(buffer: Array<UInt8>): UInt16
```

功能：从字节数组中以小端序的方式读取一个 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer: Array<UInt8> = [0x34, 0x12]
    let n = UInt16.readLittleEndian(buffer)
    @Assert(n, 0x1234u16)
}
```

#### func writeLittleEndian(Array\<UInt8>)

```cangjie
public func writeLittleEndian(buffer: Array<UInt8>): Int64
```

功能：将 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值以小端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值时，抛出异常。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let n = 0x1234u16.writeLittleEndian(buffer)
    @Assert(n, 2)
    @Assert(buffer[..n] == [0x34, 0x12])
}
```