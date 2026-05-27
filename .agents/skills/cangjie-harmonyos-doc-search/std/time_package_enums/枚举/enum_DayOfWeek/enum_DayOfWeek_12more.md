## enum DayOfWeek

```cangjie
public enum DayOfWeek <: ToString & Equatable<DayOfWeek> {
    | Sunday
    | Monday
    | Tuesday
    | Wednesday
    | Thursday
    | Friday
    | Saturday
}
```

功能：[DayOfWeek](time_package_enums.md#enum-dayofweek) 表示一周中的某一天，提供了与 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型转换，相等性判别以及获取枚举值的字符串表示的功能。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[DayOfWeek](time_package_enums.md#enum-dayofweek)>

### Friday

```cangjie
Friday
```

功能：构造一个表示周五的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Monday

```cangjie
Monday
```

功能：构造一个表示周一的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Saturday

```cangjie
Saturday
```

功能：构造一个表示周六的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Sunday

```cangjie
Sunday
```

功能：构造一个表示周日的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Thursday

```cangjie
Thursday
```

功能：构造一个表示周四的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Tuesday

```cangjie
Tuesday
```

功能：构造一个表示周二的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### Wednesday

```cangjie
Wednesday
```

功能：构造一个表示周三的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

### static func of(Int64)

```cangjie
public static func of(dayOfWeek: Int64): DayOfWeek
```

功能：获取参数 `dayOfWeek` 对应的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

参数：

- dayOfWeek: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 周几的整数表示，合法范围为 [0, 6]。其中，0 表示周日，1 至 6 表示周一至周六。

返回值：

- [DayOfWeek](time_package_enums.md#enum-dayofweek) - 参数 `dayOfWeek` 对应的 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `dayOfWeek` 不在 [0, 6] 范围内时，抛出异常。

### func toInteger()

```cangjie
public func toInteger(): Int64
```

功能：获取当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的整数表示，周日表示为 0，周一至周六表示为 1 至 6。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的整数表示。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的字符串表示，如 "Monday" 表示周一。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的字符串表示。

### func value() <sup>(deprecated)</sup>

```cangjie
public func value(): Int64
```

功能：获取当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的整数表示，周日表示为 0，周一至周六表示为 1 至 6。

> **注意：**
>
> 未来版本即将废弃，可使用 [toInteger()](#func-tointeger) 替代。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [DayOfWeek](time_package_enums.md#enum-dayofweek) 实例的整数表示。