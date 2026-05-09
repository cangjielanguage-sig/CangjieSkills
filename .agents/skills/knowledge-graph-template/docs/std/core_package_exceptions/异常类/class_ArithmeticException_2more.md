## class ArithmeticException

```cangjie
public open class ArithmeticException <: Exception {
    public init()
    public init(message: String)
}
```

功能：算术异常类，发生算术异常时使用。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ArithmeticException](core_package_exceptions.md#class-arithmeticexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [ArithmeticException](core_package_exceptions.md#class-arithmeticexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

## class Error

```cangjie
public open class Error <: ToString
```

功能：[Error](core_package_exceptions.md#class-error) 是所有错误类的基类。该类不可被继承，不可初始化，但是可以被捕获到。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

### prop message

```cangjie
public open prop message: String
```

功能：获取错误信息。

类型：[String](core_package_structs.md#struct-string)

### func getStackTrace()

```cangjie
public func getStackTrace(): Array<StackTraceElement>
```

功能：获取堆栈信息，每一条堆栈信息用一个 [StackTraceElement](core_package_classes.md#class-stacktraceelement) 实例表示，最终返回一个 [StackTraceElement](core_package_classes.md#class-stacktraceelement) 的数组。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[StackTraceElement](core_package_classes.md#class-stacktraceelement)> - 堆栈信息数组。

### func getStackTraceMessage()

```cangjie
public open func getStackTraceMessage(): String
```

功能：获取堆栈信息。

返回值：

- [String](core_package_structs.md#struct-string) - 堆栈信息。

### func printStackTrace()

```cangjie
public open func printStackTrace(): Unit
```

功能：向控制台打印堆栈信息。

### func toString()

```cangjie
public open func toString(): String
```

功能：获取当前 [Error](core_package_exceptions.md#class-error) 实例的字符串值，包括类名和错误信息。

返回值：

- [String](core_package_structs.md#struct-string) - 错误信息字符串。