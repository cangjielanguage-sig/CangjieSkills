## class ByteBuffer

```cangjie
public class ByteBuffer <: IOStream & Seekable {
    public init()
    public init(capacity: Int64)
    public init(source: Array<Byte>)
}
```

功能：基于 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 数据类型，提供对字节流的写入、读取等操作。

父类型：

- [IOStream](io_package_interfaces.md#interface-iostream)
- [Seekable](io_package_interfaces.md#interface-seekable)

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：获取当前缓冲区容量。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前缓冲区容量。

### init()

```cangjie
public init()
```

功能：创建 [ByteBuffer](io_package_classes.md#class-bytebuffer) 实例，默认的初始容量是 32。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer()
    println(buffer.capacity)
}
```

运行结果：

```text
32
```

### init(Array\<Byte>)

```cangjie
public init(source: Array<Byte>)
```

功能：根据传入的数组构造 [ByteBuffer](io_package_classes.md#class-bytebuffer) 实例。

参数：

- source: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 传入的数组。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let buffer = ByteBuffer(inputData)
    println(buffer.capacity)

    /* 从缓冲区中读取数据 */
    println(String.fromUtf8(buffer.bytes()))
}
```

运行结果：

```text
11
Hello World
```

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：创建 [ByteBuffer](io_package_classes.md#class-bytebuffer) 实例。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的初始容量。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 capacity 小于 0 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer(1024)
    println(buffer.capacity)

    try {
        let errorBuffer = ByteBuffer(-1024)
        println(errorBuffer.capacity)
    } catch (e: Exception) {
        println("Error: ${e.message}")
    }
}
```

运行结果：

```text
1024
Error: The capacity must be greater than or equal to 0: -1024.
```

### func bytes()

```cangjie
public func bytes(): Array<Byte>
```

功能：获取当前 [ByteBuffer](io_package_classes.md#class-bytebuffer) 中未被读取的数据的切片。

> **注意：**
>
> - 缓冲区进行读取，写入或重置等修改操作会导致这个切片失效。
> - 对切片的修改会影响缓冲区的内容。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 当前流中未被读取的数据的切片。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let inputData = "Hello World".toArray()
    let buffer = ByteBuffer(inputData)

    /* 从缓冲区中读取数据 */
    println(String.fromUtf8(buffer.bytes()))
}
```

运行结果：

```text
Hello World
```