## enum ExplicitGcType

```cangjie
public enum ExplicitGcType <: ToString {
    | Disabled
    | Heavy
    | Light
}
```

功能：用于指定 `@Configure` 宏的 `explicitGC` 配置参数。表示 [GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 执行的三种不同方式。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### Disabled

```cangjie
Disabled
```

功能：[GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 不会被框架显式调用。

### Heavy

```cangjie
Heavy
```

功能：[std.runtime.GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool)(heavy: true) 将在性能测试执行期间由框架显式调用。

### Light

```cangjie
Light
```

功能：[std.runtime.GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool)(heavy: false) 将在 Benchmark 函数执行期间由框架显式调用。这是默认设置。

### func toString()

```cangjie
public func toString(): String
```

功能：[GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 执行的三种不同方式字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 执行的三种不同方式字符串。

## enum TimeUnit

```cangjie
public enum TimeUnit <: ToString {
    | Micros
    | Millis
    | Nanos
    | Seconds
}
```

功能：可以在 [TimeNow](./unittest_package_structs.md#struct-timenow) 构造函数中使用的时间单位。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### Micros

```cangjie
Micros
```

功能：单位为微秒。

### Millis

```cangjie
Millis
```

功能：单位为毫秒。

### Nanos

```cangjie
Nanos
```

功能：单位为纳秒。

### Seconds

```cangjie
Seconds
```

功能：单位为秒。

### func toString()

```cangjie
public func toString(): String
```

功能： 将时间转换为字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 由四个不同的时间表示组成的字符串。