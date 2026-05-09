### func addHours(Int64)

```cangjie
public func addHours(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 小时之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少小时的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 小时后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 小时后的日期时间超过表示范围时，抛出异常。

### func addMinutes(Int64)

```cangjie
public func addMinutes(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 分钟之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少分钟的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 分钟后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 分钟后的日期时间超过表示范围时，抛出异常。

### func addMonths(Int64)

```cangjie
public func addMonths(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 月之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

> **注意：**
>
> 由于月的间隔不固定，若设 dt 表示 “2020 年 3 月 31 日”，`dt.addMonths(1)` 不会返回非法日期“2020 年 4 月 31 日”。为了尽量返回有效的日期，会偏移到当月最后一天，返回“2020 年 4 月 30 日”。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少月的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 月后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 月后的日期时间超过表示范围时，抛出异常。

### func addNanoseconds(Int64)

```cangjie
public func addNanoseconds(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 纳秒之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少纳秒的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 纳秒后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 纳秒后时间的日期时间超过表示范围时，抛出异常。