### prop month

```cangjie
public prop month: Month
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的月份。

类型：[Month](time_package_enums.md#enum-month)

### prop monthValue <sup>(deprecated)</sup>

```cangjie
public prop monthValue: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例以数字形式表示的月份。

> **注意：**
>
> 未来版本即将废弃不再使用。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop nanosecond

```cangjie
public prop nanosecond: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的纳秒。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop second

```cangjie
public prop second: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的秒。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop time

```cangjie
public prop time: (Int64, Int64, Int64)
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的时、分、秒。

类型：([Int64](../../core/core_package_api/core_package_intrinsics.md#int64),[Int64](../../core/core_package_api/core_package_intrinsics.md#int64), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64))

### prop year

```cangjie
public prop year: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的年份。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop zone

```cangjie
public prop zone: TimeZone
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例所关联的时区。

类型：[TimeZone](time_package_classes.md#class-timezone)

### prop zoneId

```cangjie
public prop zoneId: String
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例所关联的 [TimeZone](time_package_classes.md#class-timezone) 实例的时区 ID。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop zoneOffset

```cangjie
public prop zoneOffset: Duration
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例所关联的 [TimeZone](time_package_classes.md#class-timezone) 实例的时间偏移。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### static func fromUnixTimeStamp(Duration)

```cangjie
public static func fromUnixTimeStamp(d: Duration): DateTime
```

功能：获取自 [UnixEpoch](#static-prop-unixepoch) 开始，参数 `d` 指定时间间隔后的日期时间。

参数：

- d: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 时间间隔。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 自 [UnixEpoch](#static-prop-unixepoch) 开始，指定 `d` 后的日期时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过日期时间的表示范围时，抛出异常。

### static func now(TimeZone)

```cangjie
public static func now(timeZone!: TimeZone = TimeZone.Local): DateTime
```

功能：获取参数 `timeZone` 指定时区的当前时间。该方法获取的当前时间受系统时间影响，如存在使用不受系统时间影响的计时场景，可使用 [MonoTime](time_package_structs.md#struct-monotime).now() 替代。

参数：

- timeZone!: [TimeZone](time_package_classes.md#class-timezone) - 时区，默认为本地时区。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 返回指定时区当前时间。