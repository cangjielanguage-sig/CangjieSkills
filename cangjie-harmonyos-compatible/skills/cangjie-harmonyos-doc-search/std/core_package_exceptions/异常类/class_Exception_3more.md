## class Exception

```cangjie
public open class Exception <: ToString {
    public init()
    public init(message: String)
}
```

功能：[Exception](core_package_exceptions.md#class-exception) 是所有异常类的父类。

支持构造一个异常类，设置、获取异常信息，转换为字符串，获取、打印堆栈，设置异常名（用于字符串表示）。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

### prop message

```cangjie
public open prop message: String
```

功能：获取异常信息。

类型：[String](core_package_structs.md#struct-string)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Exception](core_package_exceptions.md#class-exception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [Exception](core_package_exceptions.md#class-exception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

### func getStackTrace()

```cangjie
public func getStackTrace(): Array<StackTraceElement>
```

功能：获取堆栈信息，每一条堆栈信息用一个 [StackTraceElement](core_package_classes.md#class-stacktraceelement) 实例表示，最终返回一个 [StackTraceElement](core_package_classes.md#class-stacktraceelement) 的数组。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[StackTraceElement](core_package_classes.md#class-stacktraceelement)> - 堆栈信息数组。

### func printStackTrace()

```cangjie
public func printStackTrace(): Unit
```

功能：向控制台打印堆栈信息。

### func toString()

```cangjie
public open func toString(): String
```

功能：获取当前 [Exception](core_package_exceptions.md#class-exception) 实例的字符串值，包括类名和异常信息。

返回值：

- [String](core_package_structs.md#struct-string) - 异常字符串。

## class IllegalArgumentException

```cangjie
public open class IllegalArgumentException <: Exception {
    public init()
    public init(message: String)
}
```

功能：表示参数非法的异常类。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

## class IllegalFormatException

```cangjie
public open class IllegalFormatException <: IllegalArgumentException {
    public init()
    public init(message: String)
}
```

功能：表示变量的格式无效或不标准时的异常类。

父类型：

- [IllegalArgumentException](#class-illegalargumentexception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [IllegalFormatException](core_package_exceptions.md#class-illegalformatexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [IllegalFormatException](core_package_exceptions.md#class-illegalformatexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。