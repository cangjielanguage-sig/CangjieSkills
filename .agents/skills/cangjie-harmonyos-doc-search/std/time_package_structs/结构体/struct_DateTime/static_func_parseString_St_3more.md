### static func parse(String, String)

```cangjie
public static func parse(str: String, format: String): DateTime
```

功能：根据 `format` 指定的时间格式，从字符串 `str` 中解析得到时间，解析成功时返回 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- str: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时间字符串，例如："2023/04/10 08:00:00 +08:00"。
- format: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时间字符串的格式，例如："yyyy/MM/dd HH:mm:ss OOOO"。格式说明详见[时间字符串格式](../time_package_overview.md#时间字符串格式)。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据参数 `format` 指定的时间格式，从参数 `str` 中解析出的 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [TimeParseException](time_package_exceptions.md#class-timeparseexception) - 当无法正常解析时，或存在同一 `format` 的多次取值时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `format` 格式不正确时，抛出异常。

### static func tryParse(String)

```cangjie
public static func tryParse(str: String): Option<DateTime>
```

功能：从参数 `str` 中解析得到时间，解析成功时返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[DateTime](time_package_structs.md#struct-datetime)> 实例。

参数：

- str: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时间字符串，格式为 `RFC3339` 中 `date-time` 格式，可包含小数秒，如 "2023-04-10T08:00:00[.123456]+08:00"（`[]` 中的内容表示可选项）。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[DateTime](time_package_structs.md#struct-datetime)> - 从参数 `str` 中解析出的 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[DateTime](time_package_structs.md#struct-datetime)> 实例，如果解析失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<DateTime>.None。

### func addDays(Int64)

```cangjie
public func addDays(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 天之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少天的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 天后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 天后的日期时间超过表示范围时，抛出异常。