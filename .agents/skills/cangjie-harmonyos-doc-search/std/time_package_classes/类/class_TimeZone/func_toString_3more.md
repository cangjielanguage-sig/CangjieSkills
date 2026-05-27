### func toString()

```cangjie
public func toString(): String
```

功能：获取本 [TimeZone](time_package_classes.md#class-timezone) 实例时区 ID 的字符串表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时区 ID 的字符串表示。

### operator func !=(TimeZone)

```cangjie
public operator func !=(r: TimeZone): Bool
```

功能：判断当前 [TimeZone](time_package_classes.md#class-timezone) 实例的引用是否不等于 `r` 的引用。

参数：

- r: [TimeZone](time_package_classes.md#class-timezone) - [TimeZone](time_package_classes.md#class-timezone) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [TimeZone](time_package_classes.md#class-timezone) 实例的引用不等于 `r` 的引用时，返回 `true`；否则，返回 `false`。

### operator func ==(TimeZone)

```cangjie
public operator func ==(r: TimeZone): Bool
```

功能：判断当前 [TimeZone](time_package_classes.md#class-timezone) 实例的引用是否等于 `r` 的引用。

参数：

- r: [TimeZone](time_package_classes.md#class-timezone) - [TimeZone](time_package_classes.md#class-timezone) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [TimeZone](time_package_classes.md#class-timezone) 实例的引用等于 `r` 的引用时，返回 `true`；否则，返回 `false`。