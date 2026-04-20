### extend\<T> BufferedOutputStream\<T> <: Resource where T <: Resource

```cangjie
extend<T> BufferedOutputStream<T> <: Resource where T <: Resource
```

功能：为 [BufferedOutputStream](./io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 实现 [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource) 接口，该类型对象可在 `try-with-resource` 语法上下文中实现自动资源释放。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

#### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前流。

> **注意：**
>
> 调用此方法后不可再调用 [BufferedOutputStream](io_package_classes.md#class-bufferedoutputstreamt-where-t--outputstream) 的其他接口，否则会造成非预期现象。

#### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断当前流是否关闭。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果当前流已经被关闭，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
import std.io.BufferedOutputStream
import std.io.OutputStream
import std.io.ByteBuffer
import std.io.readToEnd

/**
 * 自定义实现 OutputStream 和 Resource 接口的类 A
 */
public class A <: OutputStream & Resource {
    private var closed: Bool = false
    public var outputStream = ByteBuffer()

    public func write(buffer: Array<Byte>): Unit {
        this.outputStream = ByteBuffer(buffer)
    }

    public func isClosed(): Bool {
        return closed
    }

    public func close(): Unit {
        println("Resource is closed")
        closed = true
    }
}

main(): Unit {
    let resourceStream = A()
    let bufferedStream = BufferedOutputStream(resourceStream)

    /* 使用 try-with-resource 语法获取资源 */
    try (r = bufferedStream) {
        println("Get the resource")
        let data = "Hello World".toArray()
        r.write(data)
        r.flush()
        println(r.isClosed())
        println(String.fromUtf8(readToEnd(resourceStream.outputStream)))
    }

    /* 自动调用 close() 函数释放资源 */
    println(bufferedStream.isClosed())
}
```

运行结果：

```text
Get the resource
false
Hello World
Resource is closed
true
```