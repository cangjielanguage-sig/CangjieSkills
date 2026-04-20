## class CompressInputStream

```cangjie
public class CompressInputStream <: InputStream {
    public init(inputStream: InputStream, wrap!: WrapType = DeflateFormat, compressLevel!: CompressLevel = DefaultCompression, bufLen!: Int64 = 512)
}
```

功能：压缩输入流。

可将 [CompressInputStream](zlib_package_classes.md#class-compressinputstream) 实例通过构造函数绑定到任意 InputStream 类型输入流，通过循环调用 read(outBuf: Array\<Byte>) 函数，将该输入流中的数据压缩，并将压缩后的数据输出到传入的字节数组。

父类型：

- InputStream

### init(InputStream, WrapType, CompressLevel, Int64)

```cangjie
public init(inputStream: InputStream, wrap!: WrapType = DeflateFormat, compressLevel!: CompressLevel = DefaultCompression, bufLen!: Int64 = 512)
```

功能：构造一个压缩输入流。

需绑定一个输入流，可设置压缩数据格式、压缩等级、内部缓冲区大小（每次从输入流中读取多少数据进行压缩）。

参数：

- inputStream: InputStream - 待压缩的输入流。
- wrap!: [WrapType](zlib_package_enums.md#enum-wraptype) - 压缩数据格式，默认值为 [DeflateFormat](zlib_package_enums.md#deflateformat)。
- compressLevel!: [CompressLevel](zlib_package_enums.md#enum-compresslevel) - 压缩等级，默认值为 [DefaultCompression](zlib_package_enums.md#defaultcompression)。
- bufLen!: Int64 - 输入流缓冲区的大小，取值范围为 (0, Int64.Max]，默认 512 字节。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 当 `bufLen` 小于等于 0，输入流分配内存失败，或压缩资源初始化失败，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭压缩输入流。

当前 [CompressInputStream](zlib_package_classes.md#class-compressinputstream) 实例使用完毕后必须调用此函数来释放其所占内存资源，以免造成内存泄漏。调用该函数前需确保 [read](./zlib_package_classes.md#func-readarraybyte) 函数已返回 0，否则可能导致绑定的 InputStream 并未被全部压缩。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果释放压缩资源失败，抛出异常。

### func read(Array\<Byte>)

```cangjie
public func read(outBuf: Array<Byte>): Int64
```

功能：从绑定的输入流中读取数据并压缩，压缩后数据放入指定的字节数组中。

参数：

- outBuf: Array\<Byte> - 用来存放压缩后数据的缓冲区。

返回值：

- Int64 - 如果压缩成功，返回压缩后字节数，如果绑定的输入流中数据已经全部压缩完成，或者该压缩输入流被关闭，返回 0。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 当 `outBuf` 为空，或压缩数据失败，抛出异常。

示例：

<!-- verify -->
```cangjie
import stdx.compress.zlib.*
import std.fs.*
import std.io.*

main(): Unit {
    let arr1 = "Hello, World!Hello, World!Hello, World!Hello, World!Hello, World!".toArray()
    let byteBuffer = ByteBuffer(arr1)
    let bufferedInputStream = BufferedInputStream(byteBuffer)
    var compressInputStream: CompressInputStream = CompressInputStream(bufferedInputStream)
    var arr: Array<Byte> = Array<Byte>(1024, repeat: 0)
    println(arr1.size)
    var len = compressInputStream.read(arr)
    println(len)
    compressInputStream.close()
}
```

运行结果：

```text
65
18
```