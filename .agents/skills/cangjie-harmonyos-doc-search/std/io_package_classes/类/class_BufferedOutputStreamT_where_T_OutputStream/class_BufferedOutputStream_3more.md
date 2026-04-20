## class BufferedOutputStream\<T> where T <: OutputStream

```cangjie
public class BufferedOutputStream<T> <: OutputStream where T <: OutputStream {
    public init(output: T)
    public init(output: T, buffer: Array<Byte>)
    public init(output: T, capacity: Int64)
}
```

功能：提供带缓冲区的输出流。

可将其他 [OutputStream](io_package_interfaces.md#interface-outputstream) 类型的输入流（如 [ByteBuffer](io_package_classes.md#class-bytebuffer)）绑定到 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 实例，从该实例写入数据时，先把数据写入缓冲区暂存，再从缓冲区写入数据到流中。

父类型：

- [OutputStream](io_package_interfaces.md#interface-outputstream)

### init(T)

```cangjie
public init(output: T)
```

功能：创建 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 实例，缓冲区容量取默认值 4096。

参数：

- output: T - 绑定指定输出流。

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

### init(T, Array\<Byte>)

```cangjie
public init(output: T, buffer: Array<Byte>)
```

功能：创建 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 实例。

其内部使用的缓存区由入参决定，在注重性能的场景下，通过复用传入的 `buffer`，可以减少内存分配次数，提高性能。

参数：

- output: T - 绑定一个输出流。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 使用的内部缓存区。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 大小等于 0 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedOutputStream

main(): Unit {
    let outputStream = ByteBuffer()

    /* 使用合法的内部缓冲区创建 BufferedOutputStream 实例，不会抛出异常 */
    try {
        let buffer = Array<Byte>(1024, repeat: 0)
        let bufferedStream = BufferedOutputStream(outputStream, buffer)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 内部缓冲区大小被定义为 0 的情况 */
    try {
        let invalidBuffer = Array<Byte>()
        let bufferedStream = BufferedOutputStream(outputStream, invalidBuffer)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

运行结果：

```text
Error: The buffer cannot be empty.
```