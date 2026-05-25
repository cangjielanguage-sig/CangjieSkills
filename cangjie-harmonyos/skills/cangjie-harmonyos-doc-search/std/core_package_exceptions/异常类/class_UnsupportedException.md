## class UnsupportedException

```cangjie
public class UnsupportedException <: Exception {
    public init()
    public init(message: String)
}
```

功能：表示功能未支持的异常类。

父类型：

- [Exception](#class-exception)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [UnsupportedException](core_package_exceptions.md#class-unsupportedexception) 实例，默认异常信息为空。

### init(String)

```cangjie
public init(message: String)
```

功能：根据指定异常信息构造 [UnsupportedException](core_package_exceptions.md#class-unsupportedexception) 实例。

参数：

- message: [String](core_package_structs.md#struct-string) - 异常提示信息。