## class DecompressInputStream

```cangjie
public class DecompressInputStream <: InputStream {
    public init(inputStream: InputStream, wrap!: WrapType = DeflateFormat, bufLen!: Int64 = 512)
}
```

功能：解压输入流。

可将 [DecompressInputStream](zlib_package_classes.md#class-decompressinputstream) 实例通过构造函数绑定到任意 InputStream 输入流，通过循环调用 read(outBuf: Array\<Byte>) 函数读取、解压输入流中的数据，并将解压后数据输出到指定字节数组。

父类型：

- InputStream

### init(InputStream, WrapType, Int64)

```cangjie
public init(inputStream: InputStream, wrap!: WrapType = DeflateFormat, bufLen!: Int64 = 512)
```

功能：构造一个解压输入流。

需绑定一个输入流，可设置待解压数据格式、内部缓冲区大小（每次从输入流中读取多少数据进行解压）。

参数：

- inputStream: InputStream - 待压缩的输入流。
- wrap!: [WrapType](zlib_package_enums.md#enum-wraptype) - 待解压数据格式，默认值为 [DeflateFormat](zlib_package_enums.md#deflateformat)。
- bufLen!: Int64 - 输入流缓冲区的大小，取值范围为 (0, Int64.Max]，默认 512 字节。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果 `bufLen` 小于等于 0，输入流分配内存失败，或待解压资源初始化失败，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭解压输入流。

当前 [DecompressInputStream](zlib_package_classes.md#class-decompressinputstream) 实例使用完毕后必须调用此函数来释放其所占内存资源，以免造成内存泄漏。调用该函数前需确保 [read](./zlib_package_classes.md#func-readarraybyte-1) 函数已返回 0，否则可能导致绑定的 InputStream 并未被全部解压。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 如果释放解压资源失败，抛出异常。

### func read(Array\<Byte>)

```cangjie
public func read(outBuf: Array<Byte>): Int64
```

功能：从绑定的输入流中读取数据并解压，解压后数据放入指定的字节数组中。

参数：

- outBuf: Array\<Byte> - 用来存放解压后数据的缓冲区。

返回值：

- Int64 - 如果解压成功，返回解压后字节数，如果绑定的输入流中数据已经全部解压完成，或者该解压输入流被关闭，返回 0。

异常：

- [ZlibException](zlib_package_exceptions.md#class-zlibexception) - 当 `outBuf` 为空，或解压数据失败，抛出异常。

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

    /* 使用解压缩输入流进行数据解压 */
    var decompressInputStream: DecompressInputStream = DecompressInputStream(ByteBuffer(arr2[..len1]))
    var arr3: Array<Byte> = Array<Byte>(1024, repeat: 0)
    var len2 = decompressInputStream.read(arr3)
    println(String.fromUtf8(arr3[..len2]))

    /* 关闭输入流 */
    compressInputStream.close()
    decompressInputStream.close()
}
```

运行结果：

```text
65
18
Hello, World!Hello, World!Hello, World!Hello, World!Hello, World!
```