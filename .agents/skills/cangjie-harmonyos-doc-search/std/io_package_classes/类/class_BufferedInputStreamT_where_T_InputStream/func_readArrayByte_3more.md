### func read(Array\<Byte>)

```cangjie
public func read(buffer: Array<Byte>): Int64
```

功能：从绑定的输入流读出数据到 `buffer` 中。

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
import std.io.BufferedInputStream

main(): Unit {
    let inputStream = ByteBuffer()

    /* 使用合法的内部缓冲区容量创建 BufferedInputStream 实例，不会抛出异常 */
    try {
        let capacity = 2048
        let bufferedStream = BufferedInputStream(inputStream, capacity)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 当内部缓冲区被设置成 0 时，抛出异常 */
    try {
        let zeroCapacity = 0
        let bufferedStream = BufferedInputStream(inputStream, zeroCapacity)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 当内部缓冲区被设置成负数时，抛出异常 */
    try {
        let negativeCapacity = -1024
        let bufferedStream = BufferedInputStream(inputStream, negativeCapacity)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

运行结果：

```text
Error: Invalid capacity size: capacity = 0.
Error: Invalid capacity size: capacity = -1024.
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
import std.io.BufferedInputStream

main(): Unit {
    /* 创建输入流并写入数据 */
    let inputStream = ByteBuffer()
    let sourceData = "abc".toArray()
    inputStream.write(sourceData)
    let bufferedStream = BufferedInputStream(inputStream)

    /* 依次读取所有字节 */
    while (true) {
        let byte = bufferedStream.readByte()
        if (byte == None) {
            break
        }
        println(String.fromUtf8(byte.getOrThrow()))
    }
}
```

运行结果：

```text
a
b
c
```

### func reset(T)

```cangjie
public func reset(input: T): Unit
```

功能：绑定新的输入流，重置状态，但不重置 `capacity`。

参数：

- input: T - 待绑定的输入流。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedInputStream
import std.io.IOException

main(): Unit {
    /* 创建第一个输入流并写入数据 */
    let inputStream1 = ByteBuffer()
    let sourceData1 = "First message: Hello".toArray()
    inputStream1.write(sourceData1)

    /* 创建第二个输入流并写入数据 */
    let inputStream2 = ByteBuffer()
    let sourceData2 = "Second message: World".toArray()
    inputStream2.write(sourceData2)

    /* 使用 BufferedInputStream 包装第一个输入流 */
    let bufferedStream = BufferedInputStream(inputStream1)

    /* 读取第一个输入流的部分数据 */
    var result1 = ""
    for (_ in 0..sourceData1.size) {
        let byte = bufferedStream.readByte()
        if (byte == None) {
            break
        }
        result1 += String.fromUtf8(byte.getOrThrow())
    }
    println(result1)

    /* 重置输入流为第二个输入流 */
    bufferedStream.reset(inputStream2)
    var result2 = ""
    for (_ in 0..sourceData2.size) {
        let byte = bufferedStream.readByte()
        if (byte == None) {
            break
        }
        result2 += String.fromUtf8(byte.getOrThrow())
    }
    println(result2)
}
```

运行结果：

```text
First message: Hello
Second message: World
```