## class BufferedInputStream\<T> where T <: InputStream

```cangjie
public class BufferedInputStream<T> <: InputStream where T <: InputStream {
    public init(input: T)
    public init(input: T, buffer: Array<Byte>)
    public init(input: T, capacity: Int64)
}
```

功能：提供带缓冲区的输入流。

可将其他 [InputStream](io_package_interfaces.md#interface-inputstream) 类型的输入流（如 [ByteBuffer](io_package_classes.md#class-bytebuffer)）绑定到 [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实例，从该实例读取数据时，先把数据从被绑定的流读入缓冲区暂存，再从缓冲区读取用户需要的数据。

父类型：

- [InputStream](io_package_interfaces.md#interface-inputstream)

### init(T)

```cangjie
public init(input: T)
```

功能：创建 [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实例，缓冲区容量取默认值 4096。

参数：

- input: T - 绑定指定输入流。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedInputStream

main(): Unit {
    let inputData = "Hello World".toArray()
    let inputStream = ByteBuffer(inputData)
    /* 绑定指定输入流 */
    let bufferedStream = BufferedInputStream(inputStream)

    /* 从输入流中读取数据 */
    let data = Array<Byte>(inputData.size, repeat: 0)
    bufferedStream.read(data)
    println(String.fromUtf8(data))
}
```

运行结果：

```text
Hello World
```

### init(T, Array\<Byte>)

```cangjie
public init(input: T, buffer: Array<Byte>)
```

功能：创建 [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实例。

其内部使用的缓存区由入参决定，在注重性能的场景下，通过复用传入的 `buffer`，可以减少内存分配次数，提高性能。

参数：

- input: T - 绑定一个输入流。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 使用的内部缓存区。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 大小等于 0 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.BufferedInputStream

main(): Unit {
    let inputStream = ByteBuffer()

    /* 使用合法的内部缓冲区创建 BufferedInputStream 实例，不会抛出异常 */
    try {
        let buffer = Array<Byte>(1024, repeat: 0)
        let bufferedStream = BufferedInputStream(inputStream, buffer)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }

    /* 内部缓冲区大小被定义为 0 的情况 */
    try {
        let invalidBuffer = Array<Byte>()
        let bufferedStream = BufferedInputStream(inputStream, invalidBuffer)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

运行结果：

```text
Error: The buffer cannot be empty.
```

### init(T, Int64)

```cangjie
public init(input: T, capacity: Int64)
```

功能：创建 [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实例。

参数：

- input: T - 绑定指定输入流。
- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 内部缓冲区容量。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 capacity 小于等于 0 时，抛出异常。