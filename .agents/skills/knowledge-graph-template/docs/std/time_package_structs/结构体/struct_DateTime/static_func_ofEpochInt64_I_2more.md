### static func ofEpoch(Int64, Int64)

```cangjie
public static func ofEpoch(second!: Int64, nanosecond!: Int64): DateTime
```

功能：根据入参 `second` 和 `nanosecond` 构造 [DateTime](time_package_structs.md#struct-datetime) 实例。入参 `second` 表示 unix 时间的秒部分，`nanosecond` 表示 unix 时间的纳秒部分。unix 时间以 [UnixEpoch](#static-prop-unixepoch) 开始计算，`nanosecond` 的范围不可以超过 [0, 999,999,999]，否则抛出异常。

参数：

- second!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - unix 时间的秒部分。
- nanosecond!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - unix 时间的纳秒部分，范围不可以超过 [0, 999,999,999]。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 自 [UnixEpoch](#static-prop-unixepoch) 开始，指定 `second` 和 `nanosecond` 后的时间。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `nanosecond` 值超出指定范围时，抛出异常。
- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过日期时间的表示范围时，抛出异常。

### static func ofUTC(Int64, Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public static func ofUTC(
    year!: Int64,
    month!: Int64,
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
- month!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 月，范围 [1, 12]。
- dayOfMonth!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 日，范围 [1, 31]，最大取值需要跟 month 匹配，可能是 28、29、30、31。
- hour!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 时，范围 [0, 23]。
- minute!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 分，范围 [0, 59]。
- second!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 秒，范围 [0, 59]。
- nanosecond!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 纳秒，范围 [0, 999,999,999]。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - 根据指定参数构造的 `UTC` 时区 [DateTime](time_package_structs.md#struct-datetime) 实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数值超出指定范围时，抛出异常。