### static func ofUTC(Int64, Month, Int64, Int64, Int64, Int64, Int64)

```cangjie
public static func ofUTC(
    year!: Int64,
    month!: Month,
    dayOfMonth!: Int64,
    hour!: Int64 = 0,
    minute!: Int64 = 0,
    second!: Int64 = 0,
    nanosecond!: Int64 = 0
): DateTime
```

功能：根据参数指定的年、月、日、时、分、秒、纳秒构造 `UTC` 时区 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- year!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 年，范围 [-999,999,999, 999,999,999]。
- month!: [Month](time_package_enums.md#enum-month) - 月，[Month](time_package_enums.md#enum-month) 类型。
- dayOfMonth!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 日，范围 [1, 31]，最大取值需要跟 month 匹配，可能是 28、29、30、31。
- hour!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 时，范围 [0, 23]。
- minute!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 分，范围 [0, 59]。
- second!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 秒，范围 [0, 59]。
- nanosecond!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 纳秒，范围 [0, 999,999,999]。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据指定参数构造的 `UTC` 时区 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数值超出指定范围时，抛出异常。

### static func parse(String)

```cangjie
public static func parse(str: String): DateTime
```

功能：从参数 `str` 中解析得到时间，解析成功时返回 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- str: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时间字符串，格式为 `RFC3339` 中 `date-time` 格式，可包含小数秒，如 "2023-04-10T08:00:00[.123456]+08:00"（`[]` 中的内容表示可选项）。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 从参数 `str` 中解析出的 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [TimeParseException](time_package_exceptions.md#class-timeparseexception) - 无法正常解析时，抛出异常。

### static func parse(String, DateTimeFormat) <sup>(deprecated)</sup>

```cangjie
public static func parse(str: String, format: DateTimeFormat): DateTime
```

功能：根据 `format` 指定的时间格式，从字符串 `str` 中解析得到时间，解析成功时返回 [DateTime](time_package_structs.md#struct-datetime) 实例。

> **注意：**
>
> 未来版本即将废弃，使用 [parse(String, String)](#static-func-parsestring-string) 替代。

参数：

- str: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时间字符串，例如："2023/04/10 08:00:00 +08:00"。
- format: [DateTimeFormat](./time_package_classes.md#class-datetimeformat) - 时间格式，例如："yyyy/MM/dd HH:mm:ss OOOO"对应的时间格式。格式说明详见[时间字符串格式](../time_package_overview.md#时间字符串格式)。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据参数 `format` 指定的时间格式，从参数 `str` 中解析出的 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [TimeParseException](time_package_exceptions.md#class-timeparseexception) - 当无法正常解析时，或存在同一 `format` 的多次取值时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `format` 格式不正确时，抛出异常。