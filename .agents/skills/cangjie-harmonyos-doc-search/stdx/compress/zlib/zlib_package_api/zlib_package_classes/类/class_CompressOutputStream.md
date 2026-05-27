## class CompressOutputStream

```cangjie
public class CompressOutputStream <: OutputStream {
    public init(outputStream: OutputStream, wrap!: WrapType = DeflateFormat, compressLevel!: CompressLevel = DefaultCompression, bufLen!: Int64 = 512)
}
```

功能：压缩输出流。

可将 [CompressOutputStream](zlib_package_classes.md#class-compressoutputstream) 实例通过构造函数绑定到任意 OutputStream 类型输出流，调用 write(inBuf: Array\<Byte>) 函数读取、压缩指定字节数组中的数据，并将压缩后的数据输出到绑定的输出流。

父类型：

- OutputStream

### init(OutputStream, WrapType, CompressLevel, Int64)

```cangjie
public init(outputStream: OutputStream, wrap!: WrapType = DeflateFormat, compressLevel!: CompressLevel = DefaultCompression, bufLen!: Int64 = 512)
```

功能：构造一个压缩输出流，需绑定一个输出流，可设置压缩数据类型、压缩等级、内部缓冲区大小（每得到多少压缩后数据往输出流写出）。

参数：

- outputStream: OutputStream - 绑定的输出流，压缩后数据将写入该输出流。
- wrap!: [WrapType](zlib_package_enums.md#enum-wraptype) - 压缩数据格式，默认值为 [DeflateFormat](zlib_package_enums.md#deflateformat)。
- compressLevel!: [CompressLevel](zlib_package_enums.md#enum-compresslevel) - 压缩等级，默认值为 [DefaultCompression](zlib_package_enums.md#defaultcompression)。
- bufLen!: Int64 - 输出流缓冲区的大小，取值范围为 (0, Int64.Max]，默认 512 字节。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果 `bufLen` 小于等于 0，输出流分配内存失败，或压缩资源初始化失败，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前压缩输出流实例。

关闭时，将写入剩余压缩数据（包括缓冲区中数据，以及压缩尾部信息），并释放其所占内存资源。当前压缩输出流使用完毕后必须调用此函数来释放其所占内存资源，以免造成内存泄漏。在调用 [close](./zlib_package_classes.md#func-close-1) 函数前，绑定的输出流里已写入的数据并不是一段完整的压缩数据，调用 [close](./zlib_package_classes.md#func-close-1) 函数后，才会把剩余压缩数据写入绑定的输出流，使其完整。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前压缩输出流已经被关闭，或释放压缩资源失败，抛出异常。

### func flush()

```cangjie
public func flush(): Unit
```

功能：刷新压缩输出流。将内部缓冲区里已压缩的数据刷出并写入绑定的输出流，然后刷新绑定的输出流。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前压缩输出流已经被关闭，抛出异常。

### func write(Array\<Byte>)

```cangjie
public func write(inBuf: Array<Byte>): Unit
```

功能：将指定字节数组中的数据进行压缩，并写入输出流，当数据全部压缩完成并写入输出流，函数返回。

参数：

- inBuf: Array\<Byte> - 待压缩的字节数组。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果当前压缩输出流已经被关闭，或压缩数据失败，抛出异常。

示例：

<!-- run -->
```cangjie
import stdx.compress.zlib.*
import std.io.*

main(): Unit {
    var byteBuffer = ByteBuffer()
    var compressOutputStream: CompressOutputStream = CompressOutputStream(byteBuffer, bufLen: 39)

    var arr = "Hello, World!Hello, World!Hello, World!".toArray()

    /* 将字节数组压缩后写入压缩输出流的缓冲区 */
    compressOutputStream.write(arr)

    /* 将内部缓冲区里已压缩的数据刷出并写入绑定的输出流，然后刷新绑定的输出流 */
    compressOutputStream.flush()

    /* 关闭压缩输出流 */
    compressOutputStream.close()
}
```