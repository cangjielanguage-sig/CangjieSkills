### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：将 `buffer` 中的数据写入到绑定的输出流中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入数据的缓冲区。

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

### func writeByte(Byte)

```cangjie
public func writeByte(v: Byte): Unit
```

功能：写入一个字节到绑定的输出流中。

参数：

- v: [Byte](../../core/core_package_api/core_package_types.md#type-byte) - 待写入的字节。

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

    /* 将输出数据逐个写入缓冲流 bufferedStream 并刷新内部绑定的输出流 outputStream */
    let outputData = "Hello World".toArray()
    for (byte in outputData) {
        bufferedStream.writeByte(byte)
    }
    bufferedStream.flush()
    println(String.fromUtf8(readToEnd(outputStream)))
}
```

运行结果：

```text
Hello World
```