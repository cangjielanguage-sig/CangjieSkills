### func toString(DateTimeFormat) <sup>(deprecated)</sup>

```cangjie
public func toString(format: DateTimeFormat): String
```

功能：返回一个表示 [DateTime](time_package_structs.md#struct-datetime) 实例的字符串，其格式由参数 `format` 指定。格式说明详见[时间字符串格式](../time_package_overview.md#时间字符串格式)。

> **注意：**
>
> 未来版本即将废弃不再使用。

参数：

- format: [DateTimeFormat](./time_package_classes.md#class-datetimeformat) - 时间格式，其格式可为 "yyyy/MM/dd HH:mm:ss OOOO"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [DateTime](time_package_structs.md#struct-datetime) 实例在 `format` 指定格式下的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `format` 格式不正确时，抛出异常。

### func toUnixTimeStamp()

```cangjie
public func toUnixTimeStamp(): Duration
```

功能：获取当前实例自 [UnixEpoch](#static-prop-unixepoch) 的时间间隔。

返回值：

- [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 当前实例自 [UnixEpoch](#static-prop-unixepoch) 的时间间隔。

### operator func !=(DateTime)

```cangjie
public operator func !=(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否不等于 `r`。

若两个 [DateTime](time_package_structs.md#struct-datetime) 不相等，那么它们指向的不是同一 UTC 时间。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例不等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func +(Duration)

```cangjie
public operator func +(r: Duration): DateTime
```

功能：实现 [DateTime](time_package_structs.md#struct-datetime) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型加法，即 [DateTime](time_package_structs.md#struct-datetime) + [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 加法的右操作数。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 类型实例和 `r` 的和。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过日期时间的表示范围时，抛出异常。

### operator func -(DateTime)

```cangjie
public operator func -(r: DateTime): Duration
```

功能：实现 [DateTime](time_package_structs.md#struct-datetime) 类型之间的减法，即 [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 运算。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - 减法的右操作数。

返回值：

- [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - [DateTime](time_package_structs.md#struct-datetime) 类型实例和 `r` 的差。