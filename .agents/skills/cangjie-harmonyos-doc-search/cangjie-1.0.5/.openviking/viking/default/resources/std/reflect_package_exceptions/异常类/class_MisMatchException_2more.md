## class MisMatchException

```cangjie
public class MisMatchException <: ReflectException {
    public init()
    public init(message: String)
}
```

功能：[MisMatchException](reflect_package_exceptions.md#class-mismatchexception) 为调用对应函数抛出异常。

父类型：

- [ReflectException](#class-reflectexception)

### init()

```cangjie
public init()
```

功能：创建 [MisMatchException](reflect_package_exceptions.md#class-mismatchexception) 实例。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息创建 [MisMatchException](reflect_package_exceptions.md#class-mismatchexception) 实例。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 异常信息。

## class ReflectException

```cangjie
public open class ReflectException <: Exception {
    public init()
    public init(message: String)
}
```

功能：[ReflectException](reflect_package_exceptions.md#class-reflectexception) 为 Reflect 包的基异常类。

父类型：

- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception)

### init()

```cangjie
public init()
```

功能：创建 [ReflectException](reflect_package_exceptions.md#class-reflectexception) 实例。

### init(String)

```cangjie
public init(message: String)
```

功能：根据异常信息创建 [ReflectException](reflect_package_exceptions.md#class-reflectexception) 实例。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 异常信息。