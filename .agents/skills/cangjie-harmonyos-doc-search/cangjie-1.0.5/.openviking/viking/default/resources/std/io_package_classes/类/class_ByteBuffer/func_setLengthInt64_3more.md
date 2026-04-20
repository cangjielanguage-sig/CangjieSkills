### func setLength(Int64)

```cangjie
public func setLength(length: Int64): Unit
```

功能：将当前数据修改为指定长度。该操作不会改变 seek 的偏移。

参数：

- length: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要修改的长度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `length` 小于 0 时，抛此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当 length 过大导致扩容后的缓冲区大小超过 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 的最大值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer("Hello World".toArray())
    println("initial length: " + buffer.length.toString())

    /* 设置长度为 5，并读取缓冲区中所有的内容 */
    buffer.setLength(5)
    println("set length to 5: " + String.fromUtf8(buffer.bytes()))

    /* 尝试设置扩容后的缓冲区大小超过 Int64 的最大值时，抛出异常 */
    try {
        buffer.setLength(Int64.Max + 1)
    } catch (e: OverflowException) {
        println("Error: " + e.message)
    }

    /* 尝试设置长度为-1，抛出异常 */
    try {
        buffer.setLength(-1)
    } catch (e: IllegalArgumentException) {
        println("Error: " + e.message)
    }
}
```

运行结果：

```text
initial length: 11
set length to 5: Hello
Error: add
Error: The length must be greater than or equal to 0.
```

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：将 `buffer` 中的数据写入到输出流中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入数据的缓冲区。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer()
    let dataToWrite = "Hello World".toArray()

    /* 写入数据 */
    buffer.write(dataToWrite)
    println(String.fromUtf8(buffer.bytes()))
}
```

运行结果：

```text
Hello World
```

### func writeByte(Byte)

```cangjie
public func writeByte(v: Byte): Unit
```

功能：将一个字节写入到输出流中。

参数：

- v: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 待写入的字节。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer()
    let dataToWrite: Array<Byte> = "Hello World".toArray()

    /* 每次写入单个字节 */
    for (i in 0..dataToWrite.size) {
        buffer.writeByte(dataToWrite[i])
    }

    println(String.fromUtf8(buffer.bytes()))
}
```

运行结果：

```text
Hello World
```