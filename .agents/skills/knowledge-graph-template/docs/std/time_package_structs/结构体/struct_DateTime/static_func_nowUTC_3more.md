### static func nowUTC()

```cangjie
public static func nowUTC(): DateTime
```

功能：获取 UTC 时区的当前时间。该方法获取的当前时间受系统时间影响，如存在使用不受系统时间影响的计时场景，可使用 [MonoTime](time_package_structs.md#struct-monotime).now() 替代。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - UTC 时区当前时间。

### static func of(Int64, Int64, Int64, Int64, Int64, Int64, Int64, TimeZone)

```cangjie
public static func of(
    year!: Int64,
    month!: Int64,
    dayOfMonth!: Int64,
    hour!: Int64 = 0,
    minute!: Int64 = 0,
    second!: Int64 = 0,
    nanosecond!: Int64 = 0,
    timeZone!: TimeZone = TimeZone.Local
): DateTime
```

功能：根据参数指定的年、月、日、时、分、秒、纳秒、时区构造 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- year!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 年，范围 [-999,999,999, 999,999,999]。
- month!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 月，范围 [1, 12]。
- dayOfMonth!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 日，范围 [1, 31]，最大取值需要跟 month 匹配，可能是 28、29、30、31。
- hour!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 时，范围 [0, 23]。
- minute!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 分，范围 [0, 59]。
- second!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 秒，范围 [0, 59]。
- nanosecond!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 纳秒，范围 [0, 999,999,999]。
- timeZone!: [TimeZone](time_package_classes.md#class-timezone) - 时区。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据指定参数构造的 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数值超出指定范围，抛出异常。

### static func of(Int64, Month, Int64, Int64, Int64, Int64, Int64, TimeZone)

```cangjie
public static func of(
    year!: Int64,
    month!: Month,
    dayOfMonth!: Int64,
    hour!: Int64 = 0,
    minute!: Int64 = 0,
    second!: Int64 = 0,
    nanosecond!: Int64 = 0,
    timeZone!: TimeZone = TimeZone.Local
): DateTime
```

功能：根据参数指定的年、月、日、时、分、秒、纳秒、时区构造 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- year!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 年，范围 [-999,999,999, 999,999,999]。
- month!: [Month](time_package_enums.md#enum-month) - 月，[Month](time_package_enums.md#enum-month) 类型。
- dayOfMonth!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 日，范围 [1, 31]，最大取值需要跟 month 匹配，可能是 28、29、30、31。
- hour!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 时，范围 [0, 23]。
- minute!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 分，范围 [0, 59]。
- second!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 秒，范围 [0, 59]。
- nanosecond!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 纳秒，范围 [0, 999,999,999]。
- timeZone!: [TimeZone](time_package_classes.md#class-timezone) - 时区。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据指定参数构造的 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数值超出指定范围，抛出异常。