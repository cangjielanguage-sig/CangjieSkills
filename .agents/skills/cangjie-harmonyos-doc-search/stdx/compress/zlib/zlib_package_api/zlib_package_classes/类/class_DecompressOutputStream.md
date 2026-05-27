## class DecompressOutputStream

```cangjie
public class DecompressOutputStream <: OutputStream {
    public init(outputStream: OutputStream, wrap!: WrapType = DeflateFormat, bufLen!: Int64 = 512)
}
```

功能：解压输出流。

可将 [DecompressOutputStream](zlib_package_classes.md#class-decompressoutputstream) 实例通过构造函数绑定到指定的 OutputStream 类型输出流，通过调用 write(inBuf: Array\<Byte>) 函数读取、解压指定字节数组中的数据，并将解压后数据输出到绑定的输出流中。

父类型：

- OutputStream

### init(OutputStream, WrapType, Int64)

```cangjie
public init(outputStream: OutputStream, wrap!: WrapType = DeflateFormat, bufLen!: Int64 = 512)
```

功能：构造一个解压输出流。

需绑定一个输出流，可设置压缩数据类型、压缩等级、内部缓冲区大小（解压后数据会存入内部缓冲区，缓冲区存满后再写到输出流）。

参数：

- outputStream: OutputStream - 绑定的输出流，解压后数据将写入该输出流。
- wrap!: [WrapType](zlib_package_enums.md#enum-wraptype) - 待解压数据格式，默认值为 [DeflateFormat](zlib_package_enums.md#deflateformat)。
- bufLen!: Int64 - 输出流缓冲区的大小，取值范围为 (0, Int64.Max]，默认 512 字节。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果 `bufLen` 小于等于 0，输出流分配内存失败，或解压资源初始化失败，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前解压输出流实例。

关闭时，将写入剩余解压后数据，并释放其所占内存资源。当前压缩输出流使用完毕后必须调用此函数来释放其所占内存资源，以免造成内存泄漏。如果之前 [write](./zlib_package_classes.md#func-writearraybyte-1) 函数已处理的压缩数据不完整，调用 [close](./zlib_package_classes.md#func-close-1) 函数时会因为解压数据不全而抛出异常。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前压缩输出流已经被关闭，通过 [write](./zlib_package_classes.md#func-writearraybyte-1) 函数传入的待解压数据不完整，或释放压缩资源失败，抛出异常。

### func flush()

```cangjie
public func flush(): Unit
```

功能：刷新解压输出流。将内部缓冲区里已解压的数据写入绑定的输出流，然后刷新绑定的输出流。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前解压输出流已经被关闭，抛出异常。

### func write(Array\<Byte>)

```cangjie
public func write(inBuf: Array<Byte>): Unit
```

功能：将指定字节数组中的数据进行解压，并写入输出流，当数据全部解压完成并写入输出流，函数返回。

参数：

- inBuf: Array\<Byte> - 待解压的字节数组。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前解压输出流已经被关闭，或解压数据失败，抛出异常。

示例：

<!-- verify -->
```cangjie
import stdx.compress.zlib.*
import std.fs.*
import std.io.*

main(): Unit {
    let arr1 = "Hello, World!Hello, World!Hello, World!Hello, World!Hello, World!".toArray()

    /* 使用压缩输入流进行数据压缩 */
    let byteBuffer = ByteBuffer(arr1)
    var compressInputStream: CompressInputStream = CompressInputStream(byteBuffer)
    var arr2: Array<Byte> = Array<Byte>(1024, repeat: 0)
    /* 原始数据长度 */
    println(arr1.size)
    var len1 = compressInputStream.read(arr2)
    /* 压缩后的数据长度 */
    println(len1)

    /* 使用解压缩输出流进行数据解压后，将数据写入文件，文件的内容为原始数据 */
    var file = File("./file.text", ReadWrite)
    var decompressOutputStream: DecompressOutputStream = DecompressOutputStream(file)
    decompressOutputStream.write(arr2[..len1])
    decompressOutputStream.flush()

    /* 关闭输入流和输出流 */
    compressInputStream.close()
    decompressOutputStream.close()
    file.close()
}
```

运行结果：

```text
65
18
```