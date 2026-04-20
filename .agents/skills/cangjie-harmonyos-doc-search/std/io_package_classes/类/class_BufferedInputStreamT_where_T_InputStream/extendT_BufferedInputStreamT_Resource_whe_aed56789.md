### extend\<T> BufferedInputStream\<T> <: Resource where T <: Resource

```cangjie
extend<T> BufferedInputStream<T> <: Resource where T <: Resource
```

功能：为 [BufferedInputStream](./io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 实现 [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource) 接口，该类型对象可在 `try-with-resource` 语法上下文中实现自动资源释放。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)

#### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前流。

> **注意：**
>
> 调用此方法后不可再调用 [BufferedInputStream](io_package_classes.md#class-bufferedinputstreamt-where-t--inputstream) 的其他接口，否则会造成非预期现象。

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
import std.io.BufferedInputStream
import std.io.InputStream
import std.io.ByteBuffer

/**
 * 自定义实现 InputStream 和 Resource 接口的类 A
 */
public class A <: InputStream & Resource {
    private var closed: Bool = false

    public func read(buffer: Array<Byte>): Int64 {
        let inputData = "Hello World".toArray()
        let inputStream = ByteBuffer(inputData)
        let num = inputStream.read(buffer)
        return num
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
    let bufferedStream = BufferedInputStream(A())

    /* 使用 try-with-resource 语法获取资源 */
    try (r = bufferedStream) {
        println("Get the resource")
        let data = Array<Byte>(11, repeat: 0)
        r.read(data)
        println(r.isClosed())
        println(String.fromUtf8(data))
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