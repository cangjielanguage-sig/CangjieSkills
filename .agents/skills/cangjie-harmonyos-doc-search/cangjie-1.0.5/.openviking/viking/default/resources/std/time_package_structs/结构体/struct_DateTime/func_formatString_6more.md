### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：返回一个表示 [DateTime](time_package_structs.md#struct-datetime) 实例的字符串，其格式由参数 `fmt` 指定。格式说明详见[时间字符串格式](../time_package_overview.md#时间字符串格式)。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 返回字符串的格式，其格式可为 "yyyy/MM/dd HH:mm:ss OOOO"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [DateTime](time_package_structs.md#struct-datetime) 实例在 `fmt` 指定格式下的字符串，如果无法解析则原样返回 `fmt` 指定格式。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `fmt` 格式不符合[时间字符串格式](../time_package_overview.md#时间字符串格式)，则抛出异常。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 哈希值。

### func inLocal()

```cangjie
public func inLocal(): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例在本地时区的时间。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例在本地时区的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当返回的 [DateTime](time_package_structs.md#struct-datetime) 实例表示的日期时间超过表示范围时，抛出异常。

### func inTimeZone(TimeZone)

```cangjie
public func inTimeZone(timeZone: TimeZone): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例在参数 `timeZone` 指定时区的时间。

参数：

- timeZone: [TimeZone](time_package_classes.md#class-timezone) - 目标时区。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例在参数 `timezone` 指定时区的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当返回的 [DateTime](time_package_structs.md#struct-datetime) 实例表示的日期时间超过表示范围时，抛出异常。

### func inUTC()

```cangjie
public func inUTC(): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例在 `UTC` 时区的时间。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例在 `UTC` 时区的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当返回的 [DateTime](time_package_structs.md#struct-datetime) 实例表示的日期时间超过表示范围时，抛出异常。

### func toString()

```cangjie
public func toString(): String
```

功能：返回一个表示 [DateTime](time_package_structs.md#struct-datetime) 实例的字符串，其格式为 `RFC3339` 中 `date-time` 格式，如果时间包含纳秒信息（不为零），会打印出小数秒。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [DateTime](time_package_structs.md#struct-datetime) 实例的字符串表示。