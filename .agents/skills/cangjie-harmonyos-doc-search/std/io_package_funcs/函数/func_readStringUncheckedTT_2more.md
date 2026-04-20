## func readStringUnchecked\<T>(T) where T <: InputStream & Seekable

```cangjie
public unsafe func readStringUnchecked<T>(from: T): String where T <: InputStream & Seekable
```

功能：读取入参中的所有剩余内容，并返回一个字符串。该函数不会检查字符串的合法性。

参数：

- from: T - 要读取数据的对象。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 读取到的结果字符串。

示例：

<!-- run -->
```cangjie
import std.io.ByteBuffer
import std.io.readStringUnchecked
import std.io.ContentFormatException

main(): Unit {
    let inputStream = ByteBuffer()

    /* 向输入流写入数据 */
    let sourceData = "Hello, World!".toArray()
    inputStream.write(sourceData)

    /* 使用 readString 函数读取输入流中的所有剩余内容，可以正常输出：Read string: Hello, World! */
    unsafe {
        let result = readStringUnchecked(inputStream)
        println("Read string: ${result}")
    }

    /* 向输入流写入一个不合法的 UTF-8 字符串 */
    let sourceDataError: Array<UInt8> = [0xC3, 0x28, 0x48, 0x65, 0x6C, 0x6C, 0x6F]
    inputStream.write(sourceDataError)

    /* 使用 readString 函数读取输入流中的所有剩余内容，由于 inputStream 的第一位是不合法的UTF-8字符，所以将产生非预期的输出字符 */
    unsafe {
        let result = readStringUnchecked(inputStream)
        println("Read string: ${result}")
    }
}
```

## func readToEnd\<T>(T) where T <: InputStream & Seekable

```cangjie
public func readToEnd<T>(from: T): Array<Byte> where T <: InputStream & Seekable
```

功能：获取入参中未被读取的数据。

参数：

- from: T - 要读取数据的对象。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 未被读取的数据的拷贝。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.readToEnd

main(): Unit {
    let inputStream = ByteBuffer()

    /* 向输入流写入数据 */
    let sourceData = "Hello, World!".toArray()
    inputStream.write(sourceData)

    /* 使用 readToEnd 函数读取输入流中的所有剩余内容 */
    let data = readToEnd(inputStream)
    println("${String.fromUtf8(data)}")
}
```

运行结果：

```text
Hello, World!
```