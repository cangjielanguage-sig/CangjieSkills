### extend Float16 <: BigEndianOrder\<Float16>

```cangjie
extend Float16 <: BigEndianOrder<Float16>
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 扩展 [BigEndianOrder](binary_package_interfaces.md#interface-bigendianordert) 接口，以实现将 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值和大端序字节序列的转换。

父类型：

- [BigEndianOrder](#interface-bigendianordert)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

#### static func readBigEndian(Array\<UInt8>)

```cangjie
public static func readBigEndian(buffer: Array<UInt8>): Float16
```

功能：从字节数组中以大端序的方式读取一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.binary.*

main() {
    /* 12.5的IEEE 754表示为0x4A40 */
    let buffer: Array<UInt8> = [0x4A, 0x40]
    let n = Float16.readBigEndian(buffer)
    println(n == 12.5)
}
```

运行结果：

```text
true
```

#### func writeBigEndian(Array\<UInt8>)

```cangjie
public func writeBigEndian(buffer: Array<UInt8>): Int64
```

功能：将 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.binary.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let len = 12.5f16.writeBigEndian(buffer)
    println(len)

    /* 0x4A的十进制表示为74,0x40的十进制表示为64 */
    println(buffer[0..len])
}
```

运行结果：

```text
2
[74, 64]
```