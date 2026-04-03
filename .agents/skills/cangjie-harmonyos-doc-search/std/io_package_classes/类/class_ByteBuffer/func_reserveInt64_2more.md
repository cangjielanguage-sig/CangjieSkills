### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：将缓冲区扩容指定大小。

> **说明：**
>
> - 当缓冲区剩余字节数大于等于 `additional` 时不发生扩容。
> - 当缓冲区剩余字节数量小于 `additional` 时，取（`additional` + `capacity`）与（`capacity`的 1.5 倍向下取整）两个值中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 additional 小于 0 时，抛出异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当扩容后的缓冲区大小超过 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 的最大值时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer

main(): Unit {
    let buffer = ByteBuffer(11)
    println("initial capacity: " + buffer.capacity.toString())
    buffer.write("Hello World".toArray())

    /* 尝试扩容，需要增加的容量大于剩余空间，发生扩容 */
    buffer.reserve(5)
    println("reserve 5: " + buffer.capacity.toString())

    /* 尝试扩容，需要增加的容量小于剩余空间，不发生扩容 */
    buffer.reserve(2)
    println("reserve 2: " + buffer.capacity.toString())

    /* 尝试扩容，additional 为负数 */
    try {
        buffer.reserve(-1)
    } catch (e: IllegalArgumentException) {
        println("Error: " + e.message)
    }

    /* 尝试扩容，导致容量超过 Int64 最大值 */
    try {
        buffer.reserve(Int64.Max - buffer.capacity + 1)
    } catch (e: OverflowException) {
        println("Error: " + e.message)
    }
}
```

运行结果：

```text
initial capacity: 11
reserve 5: 16
reserve 2: 16
Error: The additional must be greater than or equal to 0.
Error: The maximum value for capacity expansion cannot exceed the maximum value of Int64.
```

### func seek(SeekPosition)

```cangjie
public func seek(sp: SeekPosition): Int64
```

功能：将光标跳转到指定位置。

> **说明：**
>
> - 指定的位置不能位于流中数据头部之前。
> - 指定位置可以超过流中数据末尾。

参数：

- sp: [SeekPosition](io_package_enums.md#enum-seekposition) - 指定光标跳转后的位置。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 流中数据的头部到跳转后位置的偏移量（以字节为单位）。

异常：

- [IOException](io_package_exceptions.md#class-ioexception) - 当指定的位置位于流中数据头部之前时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.io.ByteBuffer
import std.io.SeekPosition
import std.io.IOException

main(): Unit {
    let buffer = ByteBuffer("Hello World".toArray())
    println("initial position: ${buffer.position}")

    /* 移动到当前位置之后 6 个字节 */
    buffer.seek(SeekPosition.Current(6))
    println(String.fromUtf8(buffer.bytes()))

    /* 移动位置超过流中数据末尾，为合法操作 */
    println(buffer.seek(SeekPosition.End(1)))

    /* 尝试移动到数据头部之前，抛出异常 */
    try {
        buffer.seek(SeekPosition.Begin(-1))
    } catch (e: IOException) {
        println("Error: " + e.message)
    }
}
```

运行结果：

```text
initial position: 0
World
12
Error: Can't move the position before the beginning of the stream.
```