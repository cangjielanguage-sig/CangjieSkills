### operator func !=(DayOfWeek)

```cangjie
public operator func !=(r: DayOfWeek): Bool
```

功能：判断当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 和 `r` 是否不为一周中的同一天。

参数：

- r: [DayOfWeek](time_package_enums.md#enum-dayofweek) - [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例不等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func +(Int64)

```cangjie
public operator func +(n: Int64): DayOfWeek
```

功能：计算基于当前实例 `n` 天之后（n 为正数时）的表示值。若 `n` 为负数，则表示当天之前。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后多少天。

返回值：

- [DayOfWeek](time_package_enums.md#enum-dayofweek) - `n` 天后的周数值。

### operator func -(Int64)

```cangjie
public operator func -(n: Int64): DayOfWeek
```

功能：计算基于当前实例 `n` 天之前（n 为正数时）的表示值。若 `n` 为负数，则表示当天之后。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 前多少天。

返回值：

- [DayOfWeek](time_package_enums.md#enum-dayofweek) - `n` 天前的周数值。

### operator func ==(DayOfWeek)

```cangjie
public operator func ==(r: DayOfWeek): Bool
```

功能：判断当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 和 `r` 是否表示一周中的同一天。

参数：

- r: [DayOfWeek](time_package_enums.md#enum-dayofweek) - [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例等于 `r` 时，返回 `true`；否则，返回 `false`。