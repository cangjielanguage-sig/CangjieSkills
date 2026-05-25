## class ChainedInputStream\<T> where T <: InputStream

```cangjie
public class ChainedInputStream<T> <: InputStream where T <: InputStream {
    public init(input: Array<T>)
}
```

功能：提供顺序从 [InputStream](io_package_interfaces.md#interface-inputstream) 数组中读取数据的能力。

父类型：

- [InputStream](io_package_interfaces.md#interface-inputstream)

### init(Array\<T>)

```cangjie
public init(input: Array<T>)
```

功能：创建 [ChainedInputStream](io_package_classes.md#class-chainedinputstreamt-where-t--inputstream) 实例。

参数：

- input: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 绑定指定输入流数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 input 为空时，抛出异常。

### func read(Array\<Byte>)

```cangjie
public func read(buffer: Array<Byte>): Int64
```

功能：依次从绑定 [InputStream](io_package_interfaces.md#interface-inputstream) 数组中读出数据到 buffer 中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储读出数据的缓冲区。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 读取字节数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 buffer 为空时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.*

main(): Unit {
    let inputData = "Hello World".toArray()
    let bufferInput = ByteBuffer(inputData)
    let cis = ChainedInputStream(bufferInput)

    // 缓冲区容量是 7
    let bufferOutput = Array<Byte>(7, repeat: 0)
    cis.read(bufferOutput)
    let result = String.fromUtf8(bufferOutput)
    println(result)
}
```

运行结果：

```text
Hello W
```

## class MultiOutputStream\<T> where T <: OutputStream

```cangjie
public class MultiOutputStream<T> <: OutputStream where T <: OutputStream {
    public init(output: Array<T>)
}
```

功能：提供将数据同时写入到 [OutputStream](io_package_interfaces.md#interface-outputstream) 数组中每个输出流中的能力。

父类型：

- [OutputStream](io_package_interfaces.md#interface-outputstream)

### init(Array\<T>)

```cangjie
public init(output: Array<T>)
```

功能：创建 [MultiOutputStream](io_package_classes.md#class-multioutputstreamt-where-t--outputstream) 实例。

参数：

- output: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 绑定指定输出流数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 output 为空时，抛出异常。

### func flush()

```cangjie
public func flush(): Unit
```

功能：刷新绑定的输出流数组里的每个输出流。

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：将 buffer 同时写入到绑定的 [OutputStream](io_package_interfaces.md#interface-outputstream) 数组里的每个输出流中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 存储待写入数据的缓冲区。