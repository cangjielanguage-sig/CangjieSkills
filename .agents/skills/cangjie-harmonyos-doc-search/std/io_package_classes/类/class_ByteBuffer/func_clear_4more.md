### func clear()

```cangjie
public func clear(): Unit
```

功能：清除当前 [ByteBuffer](io_package_classes.md#class-bytebuffer) 中所有数据。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let buffer = ByteBuffer(inputData)
    println(buffer.capacity)

    /* 读取原始数据 */
    println(String.fromUtf8(buffer.bytes()))

    /* 清除缓冲区 */
    buffer.clear()

    /* 读取清除后的缓冲区 */
    println("buffer after clear: " + String.fromUtf8(buffer.bytes()))
    println("capacity after clear: ${buffer.capacity}")
}
```

运行结果：

```text
11
Hello World
buffer after clear: 
capacity after clear: 11
```

### func clone()

```cangjie
public func clone(): ByteBuffer
```

功能：用当前 [ByteBuffer](io_package_classes.md#class-bytebuffer) 中的数据来构造一个新的 [ByteBuffer](io_package_classes.md#class-bytebuffer)。

返回值：

- [ByteBuffer](io_package_classes.md#class-bytebuffer) - 新构造的 [ByteBuffer](io_package_classes.md#class-bytebuffer) 对象。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let originalBuffer = ByteBuffer(inputData)

    /* 克隆原始缓冲区 */
    let clonedBuffer = originalBuffer.clone()

    println("originalBuffer: " + String.fromUtf8(originalBuffer.bytes()))
    println("clonedBuffer: " + String.fromUtf8(clonedBuffer.bytes()))

    /* 修改原始缓冲区的数据 */
    originalBuffer.write(" New Data".toArray())

    println("originalBuffer: " + String.fromUtf8(originalBuffer.bytes()))
    println("clonedBuffer: " + String.fromUtf8(clonedBuffer.bytes()))
}
```

运行结果：

```text
originalBuffer: Hello World
clonedBuffer: Hello World
originalBuffer: Hello World New Data
clonedBuffer: Hello World
```

### func read(Array\<Byte>)

```cangjie
public func read(buffer: Array<Byte>): Int64
```

功能：从输入流中读取数据放到 buffer 中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存放读取的数据的缓冲区。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 读取数据的字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 为空时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let buffer = ByteBuffer(inputData)

    /* 创建一个目标缓冲区，读取数据到目标缓冲区 */
    let targetBuffer = Array<Byte>(5, repeat: 0)
    buffer.read(targetBuffer)
    println(String.fromUtf8(targetBuffer))

    /* 尝试读取空缓冲区 */
    try {
        let emptyBuffer = Array<Byte>()
        buffer.read(emptyBuffer)
    } catch (e: IllegalArgumentException) {
        println("Error: " + e.message)
    }
}
```

运行结果：

```text
Hello
Error: The buffer is empty.
```

### func readByte()

```cangjie
public func readByte(): ?Byte
```

功能：从输入流中读取一个字节。

返回值：

- ?[Byte](../../core/core_package_api/core_package_types.md#type-byte) - 读取到的数据。读取失败时会返回 `None`。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let buffer = ByteBuffer(inputData)

    for (_ in 0..inputData.size) {
        print(String.fromUtf8(buffer.readByte().getOrThrow()))
    }
    println()

    /* 尝试读取下一个不存在的字节 */
    let nextByte = buffer.readByte()
    match (nextByte) {
        case None => println("nextByte: None")
        case _ => println("nextByte: ${nextByte.getOrThrow()}")
    }
}
```

运行结果：

```text
Hello World
nextByte: None
```