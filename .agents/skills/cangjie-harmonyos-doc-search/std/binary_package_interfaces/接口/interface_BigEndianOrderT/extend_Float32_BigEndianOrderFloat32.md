### extend Float32 <: BigEndianOrder\<Float32>

```cangjie
extend Float32 <: BigEndianOrder<Float32>
```

功能：为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 扩展 [BigEndianOrder](binary_package_interfaces.md#interface-bigendianordert) 接口，以实现将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值和大端序字节序列的转换。

父类型：

- [BigEndianOrder](#interface-bigendianordert)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

#### static func readBigEndian(Array\<UInt8>)

```cangjie
public static func readBigEndian(buffer: Array<UInt8>): Float32
```

功能：从字节数组中以大端序的方式读取一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待读取的数据。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以读出 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.binary.*

main() {
    let buffer: Array<UInt8> = [0x41, 0x48, 0x00, 0x00]
    let n = Float32.readBigEndian(buffer)
    println(n)
}
```

运行结果：

```text
12.500000
```

#### func writeBigEndian(Array\<UInt8>)

```cangjie
public func writeBigEndian(buffer: Array<UInt8>): Int64
```

功能：将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值以大端序的方式写入字节数组中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区，用于存放待写入的数据。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入的数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 太小，不足以存储 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.binary.*

main() {
    let buffer = Array<UInt8>(8, repeat: 0)
    let len = 12.5f32.writeBigEndian(buffer)
    println(len)

    /* 12.5的IEEE 754的单精度浮点表示为 0x4148 ,0x41的十进制表示为65，0x48的十进制表示为72 */
    println(buffer[0..len])
}
```

运行结果：

```text
4
[65, 72, 0, 0]
```