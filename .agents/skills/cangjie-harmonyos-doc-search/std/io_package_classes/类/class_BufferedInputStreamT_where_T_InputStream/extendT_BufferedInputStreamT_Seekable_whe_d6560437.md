### extend\<T> BufferedInputStream\<T> <: Seekable where T <: Seekable

```cangjie
extend<T> BufferedInputStream<T> <: Seekable where T <: Seekable
```

功能：为 [BufferedInputStream](./io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实现 [Seekable](./io_package_interfaces.md#interface-seekable) 接口，支持查询数据长度，移动光标等操作。

父类型：

- [Seekable](io_package_interfaces.md#interface-seekable)

#### prop length

```cangjie
public prop length: Int64
```

功能：返回当前流中的总数据量（以字节为单位）。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

#### prop position

```cangjie
public prop position: Int64
```

功能：返回当前光标位置。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

#### prop remainLength

```cangjie
public prop remainLength: Int64
```

功能：返回当前流中未读的数据量（以字节为单位）。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

#### func seek(SeekPosition)

```cangjie
public func seek(sp: SeekPosition): Int64
```

功能：移动光标到指定的位置。

> **说明：**
>
> - 指定的位置不能位于流中数据头部之前。
> - 指定位置可以超过流中数据末尾。
> - 调用该函数会先清空缓存区，再移动光标的位置。

参数：

- sp: [SeekPosition](io_package_enums.md#enum-seekposition) - 指定光标移动后的位置。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回流中数据的起点到移动后位置的偏移量（以字节为单位）。

异常：

- [IOException](io_package_exceptions.md#class-ioexception) - 当指定的位置位于流中数据头部之前时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.BufferedInputStream
import std.io.InputStream
import std.io.ByteBuffer
import std.io.Seekable
import std.io.SeekPosition
import std.io.IOException
import std.io.readToEnd

/**
 * 自定义实现 InputStream 和 Seekable 接口的类 A
 */
public class A <: InputStream & Seekable {
    public var inputStream: ByteBuffer = ByteBuffer()

    public func read(buffer: Array<Byte>): Int64 {
        let inputData = "Hello World".toArray()
        inputStream = ByteBuffer(inputData)
        let num = inputStream.read(buffer)
        return num
    }

    public func seek(sp: SeekPosition): Int64 {
        return inputStream.seek(sp)
    }
}

main(): Unit {
    let seekableStream = A()
    let bufferedStream = BufferedInputStream(seekableStream)
    let buffer = Array<Byte>(11, repeat: 0)
    bufferedStream.read(buffer)

    /* 输出当前流中总数据量，当前光标位置，当前流中未读的数据量 */
    println("Length : " + bufferedStream.length.toString())
    println("Position : " + bufferedStream.position.toString())
    println("Remain Length : " + bufferedStream.remainLength.toString())

    /* 移动光标到指定位置，虽然超过了流中数据末尾但是合法的 */
    println("Position after seek() : " + bufferedStream.seek(SeekPosition.Current(11)).toString())

    /* 尝试移动到数据头部之前，抛出异常 */
    try {
        bufferedStream.seek(SeekPosition.Begin(-1))
    } catch (e: IOException) {
        println("Error: " + e.message)
    }

    /* 将光标移动到第一个单词之后，读取后续的数据 */
    bufferedStream.seek(SeekPosition.Begin(6))
    println(String.fromUtf8(readToEnd(seekableStream.inputStream)))
}
```

运行结果：

```text
Length : 11
Position : 11
Remain Length : 0
Position after seek() : 22
Error: Can't move the position before the beginning of the stream.
World
```