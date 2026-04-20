### operator func >=(DateTime)

```cangjie
public operator func >=(r: DateTime): Bool
```

功能：判断当前 [DateTime](time_package_structs.md#struct-datetime) 实例是否晚于或等于 `r`（指向更晚的 UTC 时间的 [DateTime](time_package_structs.md#struct-datetime) 更大）。

参数：

- r: [DateTime](time_package_structs.md#struct-datetime) - [DateTime](time_package_structs.md#struct-datetime) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [DateTime](time_package_structs.md#struct-datetime) 实例晚于或等于 `r` 时，返回 `true`；否则，返回 `false`。