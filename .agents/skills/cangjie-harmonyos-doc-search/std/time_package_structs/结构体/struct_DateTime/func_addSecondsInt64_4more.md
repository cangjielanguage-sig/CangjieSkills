### func addSeconds(Int64)

```cangjie
public func addSeconds(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 秒之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少秒的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 秒后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 秒后的日期时间超过表示范围时，抛出异常。

### func addWeeks(Int64)

```cangjie
public func addWeeks(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 周之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少周的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 周后的时间。

异常：

功能：获取入参 n 周之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

### func addYears(Int64)

```cangjie
public func addYears(n: Int64): DateTime
```

功能：获取 [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 年之后的时间，返回新的 [DateTime](time_package_structs.md#struct-datetime) 实例。

> **注意：**
>
> 由于年的间隔不固定，若设 dt 表示 “2020 年 2 月 29 日”，`dt.addYears(1)` 不会返回非法日期“2021 年 2 月 29 日”。为了尽量返回有效的日期，会偏移到当月最后一天，返回 “2021 年 2 月 28 日”。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自 [DateTime](time_package_structs.md#struct-datetime) 实例后多少年的数量。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 年后的时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - [DateTime](time_package_structs.md#struct-datetime) 实例 `n` 年后的日期时间超过表示范围时，抛出异常。

### func compare(DateTime)

```cangjie
public func compare(rhs: DateTime): Ordering
```

功能：判断一个 [DateTime](time_package_structs.md#struct-datetime) 实例与参数 `rhs` 的大小关系。如果大于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT。

参数：

- rhs: [DateTime](time_package_structs.md#struct-datetime) - 参与比较的 [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - [DateTime](time_package_structs.md#struct-datetime) 实例与 `rhs` 大小关系。