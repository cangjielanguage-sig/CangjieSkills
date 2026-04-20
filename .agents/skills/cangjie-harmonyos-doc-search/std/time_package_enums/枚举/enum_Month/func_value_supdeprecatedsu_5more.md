### func value() <sup>(deprecated)</sup>

```cangjie
public func value(): Int64
```

功能：获取当前 [Month](time_package_enums.md#enum-month) 实例的整数表示，一月至十二月分别表示为 1 至 12。

> **注意：**
>
> 未来版本即将废弃，可使用 [toInteger()](#func-tointeger-1) 替代。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Month](time_package_enums.md#enum-month) 实例的整数表示。

### operator func !=(Month)

```cangjie
public operator func !=(r: Month): Bool
```

功能：判断当前 [Month](time_package_enums.md#enum-month) 实例和 `r` 是否不为同一个月。

参数：

- r: [Month](time_package_enums.md#enum-month) - [Month](time_package_enums.md#enum-month) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前 [Month](time_package_enums.md#enum-month) 实例是否不等于 `r`。

### operator func +(Int64)

```cangjie
public operator func +(n: Int64): Month
```

功能：计算基于当前日历月份 `n` 个月之后（n 为正数时）的日历月份。若 `n` 为负数，则表示当月之前。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后多少月的数量。

返回值：

- [Month](time_package_enums.md#enum-month) - `n` 月后的月份。

### operator func -(Int64)

```cangjie
public operator func -(n: Int64): Month
```

功能：计算基于当前日历月份 `n` 个前之后（n 为正数时）的日历月份。若 `n` 为负数，则表示当月之后。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 前多少月的数量。

返回值：

- [Month](time_package_enums.md#enum-month) - `n` 月前的月份。

### operator func ==(Month)

```cangjie
public operator func ==(r: Month): Bool
```

功能：判断当前 [Month](time_package_enums.md#enum-month) 实例和 `r` 是否表示同一个月。

参数：

- r: [Month](time_package_enums.md#enum-month) - [Month](time_package_enums.md#enum-month) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [Month](time_package_enums.md#enum-month) 实例等于 `r` 时，返回 `true`；否则，返回 `false`。