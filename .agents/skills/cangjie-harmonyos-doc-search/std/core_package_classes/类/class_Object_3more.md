## class Object

```cangjie
public open class Object <: Any {
    public const init()
}
```

功能：[Object](core_package_classes.md#class-object) 是所有 `class` 的父类，所有 `class` 都默认继承它。[Object](core_package_classes.md#class-object) 类中不包含任何成员，即 [Object](core_package_classes.md#class-object) 是一个“空”的类。

父类型：

- [Any](core_package_interfaces.md#interface-any)

### init()

```cangjie
public const init()
```

功能：构造一个 `object` 实例。

## class RangeIterator\<T> <: Iterator\<T> where T <: Countable\<T> & Comparable\<T> & Equatable\<T>

```cangjie
public class RangeIterator<T> <: Iterator<T> where T <: Countable<T> & Comparable<T> & Equatable<T> {}
```

功能：[Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 类型的迭代器，迭代功能详述见 [Iterable](core_package_interfaces.md#interface-iterablee) 和 [Iterator](core_package_classes.md#class-iteratort) 接口说明。

父类型：

- [Iterator](#class-iteratort)\<T>

### func next()

```cangjie
public func next(): Option<T>
```

功能：获取 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 迭代器中的下一个值。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 迭代器中的下一个成员，用 [Option](core_package_enums.md#enum-optiont) 封装，迭代到末尾时返回 `None`。

## class StackTraceElement

```cangjie
public open class StackTraceElement {
    public let declaringClass: String
    public let methodName: String
    public let fileName: String
    public let lineNumber: Int64
    public init(declaringClass: String, methodName: String, fileName: String, lineNumber: Int64)
}
```

功能：表示一个异常堆栈的具体信息，包括异常发生的类名、函数名、文件名、行号。

### let declaringClass

```cangjie
public let declaringClass: String
```

功能：获取异常发生的类名。

类型：[String](core_package_structs.md#struct-string)

### let fileName

```cangjie
public let fileName: String
```

功能：获取异常发生的文件名。

类型：[String](core_package_structs.md#struct-string)

### let lineNumber

```cangjie
public let lineNumber: Int64
```

功能：获取异常发生的行号。

类型：[Int64](core_package_intrinsics.md#int64)

### let methodName

```cangjie
public let methodName: String
```

功能：获取异常发生的函数名。

类型：[String](core_package_structs.md#struct-string)

### init(String, String, String, Int64)

```cangjie
public init(declaringClass: String, methodName: String, fileName: String, lineNumber: Int64)
```

功能：构造一个异常堆栈实例，指定类名、函数名、文件名、行号。

参数：

- declaringClass: [String](core_package_structs.md#struct-string) - 类名。
- methodName: [String](core_package_structs.md#struct-string) - 函数名。
- fileName: [String](core_package_structs.md#struct-string) - 文件名。
- lineNumber: [Int64](core_package_intrinsics.md#int64) - 行号。