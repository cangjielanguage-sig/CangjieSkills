## class NoneValueException

```cangjie
public class NoneValueException <: Exception {
    public init()
    public init(message: String)
}
```

功能：表示 [Option](core_package_enums.md#enum-optiont)\<T> 实例的值为 `None` 的异常类，通常在 `getOrThrow` 函数中被抛出。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [NoneValueException](core_package_exceptions.md#class-nonevalueexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [NoneValueException](core_package_exceptions.md#class-nonevalueexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

## class OutOfMemoryError

```cangjie
public class OutOfMemoryError <: Error {}
```

功能：表示内存不足错误的错误类，该类不可被继承，不可初始化，但是可以被捕获到。

父类型：

- [Error](#class-error)

## class OverflowException

```cangjie
public class OverflowException <: ArithmeticException {
    public init()
    public init(message: String)
}
```

功能：表示算术运算溢出的异常类。

父类型：

- [ArithmeticException](#class-arithmeticexception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [OverflowException](core_package_exceptions.md#class-overflowexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据指定异常信息构造 [OverflowException](core_package_exceptions.md#class-overflowexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

## class SpawnException

```cangjie
public class SpawnException <: Exception {
    public init()
    public init(message: String)
}
```

功能：线程异常类，表示线程处理过程中发生异常。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [SpawnException](core_package_exceptions.md#class-spawnexception) 实例，默认错误信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息构造一个 [SpawnException](core_package_exceptions.md#class-spawnexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。

## class StackOverflowError

```cangjie
public class StackOverflowError <: Error {}
```

功能：表示堆栈溢出错误的错误类，该类不可被继承，不可初始化，但是可以被捕获到。

父类型：

- [Error](#class-error)

### func printStackTrace()

```cangjie
public override func printStackTrace(): Unit
```

功能：向控制台打印堆栈信息。

## class TimeoutException

```cangjie
public class TimeoutException <: Exception {
    public init()
    public init(message: String)
}
```

功能：当阻塞操作超时时引发异常。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [TimeoutException](core_package_exceptions.md#class-timeoutexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据指定异常信息构造 [TimeoutException](core_package_exceptions.md#class-timeoutexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。