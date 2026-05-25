## struct DateTime

```cangjie
public struct DateTime <: ToString & Hashable & Comparable<DateTime> & Formattable & Parsable<DateTime> {}
```

功能：[DateTime](time_package_structs.md#struct-datetime) 表示日期时间，是一个描述某一时间点的时间类型，提供了基于时区的日期时间读取、计算、比较、转换，以及序列化和反序列化等功能。

- [DateTime](time_package_structs.md#struct-datetime) 是不可变的类型，包含了日期，时间和时区信息。可表示的时间区间为 [-999,999,999-01-01T00:00:00.000000000, 999,999,999-12-31T23:59:59.999999999]，该区间适用于任何合法的时区。
- 以下为 [DateTime](time_package_structs.md#struct-datetime) 中 [now](#static-func-nowtimezone) 和 [nowUTC](#static-func-nowutc) 函数获取当前时间使用的系统调用函数：

  | 系统    | 系统调用函数   | 时钟类型 |
  | ------- | ------------- |--------------- |
  | Linux   | clock_gettime | CLOCK_REALTIME |
  | Windows | clock_gettime | CLOCK_REALTIME |
  | macOS   | clock_gettime | CLOCK_REALTIME |

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [Comparable](../../core/core_package_api/core_package_interfaces.md#interface-comparablet)\<[DateTime](#struct-datetime)>
- [Formattable](../../convert/convert_package_api/convert_package_interfaces.md#interface-formattable)
- [Parsable](../../convert/convert_package_api/convert_package_interfaces.md#interface-parsablet)\<[DateTime](#struct-datetime)>

### static prop UnixEpoch

```cangjie
public static prop UnixEpoch: DateTime
```

功能：获取 Unix 时间纪元，即表示零时区 `1970 年 1 月 1 日 0 时 0 分 0 秒 0 纳秒` 的 [DateTime](time_package_structs.md#struct-datetime) 实例。

类型：[DateTime](time_package_structs.md#struct-datetime)

### prop date

```cangjie
public prop date: (Int64, Month, Int64)
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的年份、月份和当前月第几日。

类型：([Int64](../../core/core_package_api/core_package_intrinsics.md#int64),[Month](time_package_enums.md#enum-month), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64))

### prop dayOfMonth

```cangjie
public prop dayOfMonth: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例基于当前月第几日。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop dayOfWeek

```cangjie
public prop dayOfWeek: DayOfWeek
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例基于当前周的第几日。

类型：[DayOfWeek](time_package_enums.md#enum-dayofweek)

### prop dayOfYear

```cangjie
public prop dayOfYear: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例基于当前年份的第几日。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop hour

```cangjie
public prop hour: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的小时。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop isoWeek

```cangjie
public prop isoWeek: (Int64, Int64)
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例基于 ISO8601 标准的年份和基于年的周数。

类型：([Int64](../../core/core_package_api/core_package_intrinsics.md#int64), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64))

### prop minute

```cangjie
public prop minute: Int64
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例的分钟。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)