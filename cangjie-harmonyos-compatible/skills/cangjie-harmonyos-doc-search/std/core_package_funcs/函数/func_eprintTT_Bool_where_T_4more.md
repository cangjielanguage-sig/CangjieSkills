## func eprint\<T>(T, Bool) where T <: ToString

```cangjie
public func eprint<T>(arg: T, flush!: Bool = false): Unit where T <: ToString
```

功能：将指定 T 类型实例的字符串表示打印到标准错误文本流。

如抛出异常时，消息将打印到标准错误文本流（stderr），而不是标准输出（stdout）。

参数：

- arg: T - 待打印的 T 类型实例，该函数将打印其 toString 的返回值。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
class Rectangle <: ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func area() {
        width * height
    }
    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}"
    }
}

main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        eprint<Rectangle>(Rectangle(10, 20), flush: true)
    }
}
```

运行结果：

```text
width: 10, height: 20
```

## func eprintln(String)

```cangjie
public func eprintln(str: String): Unit
```

功能：将指定字符串打印到标准错误文本流，末尾添加换行。

如抛出异常时，消息将打印到标准错误文本流（stderr），而不是标准输出（stdout）。

参数：

- str: [String](core_package_structs.md#struct-string) - 待输出的字符串。

示例：

<!-- verify -->
```cangjie
main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        eprintln("NegativeArraySizeException is caught!")
    }
}
```

运行结果：

```text
NegativeArraySizeException is caught!
```

## func eprintln\<T>(T) where T <: ToString

```cangjie
public func eprintln<T>(arg: T): Unit where T <: ToString
```

功能：将指定 T 类型实例的字符串表示打印到标准错误文本流，末尾添加换行。

如抛出异常时，消息将打印到标准错误文本流（stderr），而不是标准输出（stdout）。

参数：

- arg: T - 待打印的 T 类型实例，该函数将打印其 toString 的返回值。

示例：

<!-- verify -->
```cangjie
class Rectangle <: ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func area() {
        width * height
    }
    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}"
    }
}

main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        eprintln<Rectangle>(Rectangle(10, 20))
    }
}
```

运行结果：

```text
width: 10, height: 20
```

## func ifNone\<T>(Option\<T>, () -> Unit)

```cangjie
public func ifNone<T>(o: Option<T>, action: () -> Unit): Unit
```

功能：如果输入是 [Option](core_package_enums.md#enum-optiont).None 类型数据，则执行 action 函数。

参数：

- o: [Option](core_package_enums.md#enum-optiont)\<T> - 待判断是否为 [Option](core_package_enums.md#enum-optiont).None 的 [Option](core_package_enums.md#enum-optiont)\<T> 类型实例。
- action: () ->[Unit](core_package_intrinsics.md#unit) - 待执行函数。

示例：

<!-- verify -->
```cangjie
main() {
    let num: Option<Int64> = None
    ifNone<Int64>(num, {=> println("num is None")})
}
```

运行结果：

```text
num is None
```