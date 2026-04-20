### operator func -(Duration)

```cangjie
public operator func -(r: Duration): DateTime
```

功能：实现 [DateTime](time_package_structs.md#struct-datetime) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型减法，即 [DateTime](time_package_structs.md#struct-datetime) - [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 减法的右操作数。

返回值：

- [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 类型实例和 `r` 的差。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过日期时间的表示范围时，抛出异常。

### operator func <(DateTime)

```cangjie
public operator func <(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否早于 `r`（指向更早的 UTC 时间的 [DateTime](time_package_structs.md#struct-datetime) 更小）。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例早于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func <=(DateTime)

```cangjie
public operator func <=(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否早于或等于 `r`（指向更早的 UTC 时间的 [DateTime](time_package_structs.md#struct-datetime) 更小）。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例早于或等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func ==(DateTime)

```cangjie
public operator func ==(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否等于 `r`。

若两个 [DateTime](time_package_structs.md#struct-datetime) 相等，那么它们指向同一 UTC 时间。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func >(DateTime)

```cangjie
public operator func >(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否晚于 `r`（指向更晚的 UTC 时间的 [DateTime](time_package_structs.md#struct-datetime) 更大）。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例晚于 `r` 时，返回 `true`；否则，返回 `false`。