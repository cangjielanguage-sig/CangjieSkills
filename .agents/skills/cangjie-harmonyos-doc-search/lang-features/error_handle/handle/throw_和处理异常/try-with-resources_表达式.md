## try-with-resources 表达式

try-with-resources 表达式主要是为了自动释放非内存资源。不同于普通 try 表达式，try-with-resources 表达式中的 catch 块和 finally 块均是可选的，并且 try 关键字其后的块之间可以插入一个或者多个 `ResourceSpecification` 用来申请一系列的资源（`ResourceSpecification` 并不会影响整个 try 表达式的类型）。这里所讲的资源对应到语言层面即指对象，因此 `ResourceSpecification` 其实就是实例化一系列的对象（多个实例化之间使用“,”分隔）。使用 try-with-resources 表达式的例子如下所示：

<!-- compile -->

```cangjie
class Worker <: Resource {
    var hasTools: Bool = false
    let name: String

    public init(name: String) {
        this.name = name
    }
    public func getTools() {
        println("${name} picks up tools from the warehouse.")
        hasTools = true
    }

    public func work() {
        if (hasTools) {
            println("${name} does some work with tools.")
        } else {
            println("${name} doesn't have tools, does nothing.")
        }
    }

    public func isClosed(): Bool {
        if (hasTools) {
            println("${name} hasn't returned the tool.")
            false
        } else {
            println("${name} has no tools")
            true
        }
    }
    public func close(): Unit {
        println("${name} returns the tools to the warehouse.")
        hasTools = false
    }
}

main() {
    try (r = Worker("Tom")) {
        r.getTools()
        r.work()
    }
    try (r = Worker("Bob")) {
        r.work()
    }
    try (r = Worker("Jack")) {
        r.getTools()
        throw Exception("Jack left, because of an emergency.")
    }
}
```

程序输出结果为：

```text
Tom picks up tools from the warehouse.
Tom does some work with tools.
Tom hasn't returned the tool.
Tom returns the tools to the warehouse.
Bob doesn't have tools, does nothing.
Bob has no tools
Jack picks up tools from the warehouse.
Jack hasn't returned the tool.
Jack returns the tools to the warehouse.
An exception has occurred:
Exception: Jack left, because of an emergency.
         at test.main()(xxx/xx.cj:xx)
```

`try` 关键字和 `{}` 之间引入的名字，其作用域与 `{}` 中引入的变量作用域级别相同，在 `{}` 中再次引入相同名字会触发重定义错误。

<!-- compile.error -->

```cangjie
class R <: Resource {
    public func isClosed(): Bool {
        true
    }
    public func close(): Unit {
        print("R is closed")
    }
}

main() {
    try (r = R()) {
        println("Get the resource")
        let r = 0 // Error, redefinition
        println(r)
    }
}
```

try-with-resources 表达式中的 `ResourceSpecification` 的类型必须实现 Resource 接口：

<!-- run -->

```cangjie
interface Resource {
    func isClosed(): Bool  // 离开 try-with-resources 作用域时，判断是否需要调用 close 函数释放资源
    func close(): Unit  // 在 isClosed 返回 false 的场景下释放资源。
}
```

需要说明的是，try-with-resources 表达式中一般没有必要再包含 catch 块和 finally 块，也不建议开发者再手动释放资源（逻辑冗余）。但是，如果需要显式地捕获 try 块或资源申请和释放过程中可能抛出的异常并处理，仍可在 try-with-resources 表达式中包含 catch 块和 finally 块：

<!-- verify -->

```cangjie
class R <: Resource {
    public func isClosed(): Bool {
        true
    }
    public func close(): Unit {
        print("R is closed")
    }
}

main() {
    try (r = R()) {
        println("Get the resource")
    } catch (e: Exception) {
        println("Exception happened when executing the try-with-resources expression")
    } finally {
        println("End of the try-with-resources expression")
    }
}
```

程序输出结果如下：

```text
Get the resource
End of the try-with-resources expression
```

try-with-resources 表达式的类型是 `Unit`。