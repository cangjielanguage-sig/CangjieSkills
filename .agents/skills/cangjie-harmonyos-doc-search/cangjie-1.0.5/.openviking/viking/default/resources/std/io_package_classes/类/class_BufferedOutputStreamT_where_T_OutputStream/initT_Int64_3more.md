### init(T, Int64)

```cangjie
public init(output: T, capacity: Int64)
```

功能：创建 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 实例。

参数：

- output: T - 绑定指定输出流。
- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 内部缓冲区容量。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 capacity 小于等于 0 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedOutputStream

main(): Unit {
    let outputStream = ByteBuffer()

    /* 使用合法的内部缓冲区容量创建 BufferedoutputStream 实例，不会抛出异常 */
    try {
        let capacity = 2048
        let bufferedStream = BufferedOutputStream(outputStream, capacity)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 当内部缓冲区被设置成 0 时，抛出异常 */
    try {
        let zeroCapacity = 0
        let bufferedStream = BufferedOutputStream(outputStream, zeroCapacity)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 当内部缓冲区被设置成负数时，抛出异常 */
    try {
        let negativeCapacity = -1024
        let bufferedStream = BufferedOutputStream(outputStream, negativeCapacity)
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

### func flush()

```cangjie
public func flush(): Unit
```

功能：刷新 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream)：将内部缓冲区的剩余数据写入绑定的输出流，并刷新 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream)。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedOutputStream
import std.io.readToEnd

main(): Unit {
    let outputStream = ByteBuffer()
    /* 绑定指定输出流 */
    let bufferedStream = BufferedOutputStream(outputStream)

    /* 将输出数据写入缓冲流 bufferedStream 并刷新内部绑定的输出流 outputStream */
    let outputData = "Hello World".toArray()
    bufferedStream.write(outputData)
    bufferedStream.flush()
    println(String.fromUtf8(readToEnd(outputStream)))
}
```

运行结果：

```text
Hello World
```

### func reset(T)

```cangjie
public func reset(output: T): Unit
```

功能：绑定新的输出流，重置状态，但不重置 `capacity`。

参数：

- output: T - 待绑定的输出流。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedOutputStream
import std.io.IOException
import std.io.readToEnd

main(): Unit {
    /* 创建第一个输出流 */
    let outputStream1 = ByteBuffer()
    let sourceData1 = "First message: Hello".toArray()

    /* 创建第二个输出流 */
    let outputStream2 = ByteBuffer()
    let sourceData2 = "Second message: World".toArray()

    /* 使用 BufferedOutputStream 包装第一个输出流 */
    let bufferedStream = BufferedOutputStream(outputStream1)

    /* 将第一个源数据写入到绑定的第一个输出流中并刷新 */
    bufferedStream.write(sourceData1)
    bufferedStream.flush()
    println(String.fromUtf8(readToEnd(outputStream1)))

    /* 重置输出流为第二个输出流，将第二个源数据写入到绑定的第二个输出流中并刷新 */
    bufferedStream.reset(outputStream2)
    bufferedStream.write(sourceData2)
    bufferedStream.flush()
    println(String.fromUtf8(readToEnd(outputStream2)))
}
```

运行结果：

```text
First message: Hello
Second message: World
```