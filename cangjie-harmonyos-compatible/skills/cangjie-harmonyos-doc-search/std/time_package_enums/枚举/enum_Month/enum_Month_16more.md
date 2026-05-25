## enum Month

```cangjie
public enum Month <: ToString & Equatable<Month> {
    | January
    | February
    | March
    | April
    | May
    | June
    | July
    | August
    | September
    | October
    | November
    | December
}
```

功能：[Month](time_package_enums.md#enum-month) 用以表示月份，表示一年中的某一月，提供了与 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型转换和计算，相等性判别以及获取枚举值的字符串表示的功能。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[Month](time_package_enums.md#enum-month)>

### April

```cangjie
April
```

功能：构造一个表示四月的 [Month](time_package_enums.md#enum-month) 实例。

### August

```cangjie
August
```

功能：构造一个表示八月的 [Month](time_package_enums.md#enum-month) 实例。

### December

```cangjie
December
```

功能：构造一个表示十二月的 [Month](time_package_enums.md#enum-month) 实例。

### February

```cangjie
February
```

功能：构造一个表示二月的 [Month](time_package_enums.md#enum-month) 实例。

### January

```cangjie
January
```

功能：构造一个表示一月的 [Month](time_package_enums.md#enum-month) 实例。

### July

```cangjie
July
```

功能：构造一个表示七月的 [Month](time_package_enums.md#enum-month) 实例。

### June

```cangjie
June
```

功能：构造一个表示六月的 [Month](time_package_enums.md#enum-month) 实例。

### March

```cangjie
March
```

功能：构造一个表示三月的 [Month](time_package_enums.md#enum-month) 实例。

### May

```cangjie
May
```

功能：构造一个表示五月的 [Month](time_package_enums.md#enum-month) 实例。

### November

```cangjie
November
```

功能：构造一个表示十一月的 [Month](time_package_enums.md#enum-month) 实例。

### October

```cangjie
October
```

功能：构造一个表示十月的 [Month](time_package_enums.md#enum-month) 实例。

### September

```cangjie
September
```

功能：构造一个表示九月的 [Month](time_package_enums.md#enum-month) 实例。

### static func of(Int64)

```cangjie
public static func of(mon: Int64): Month
```

功能：获取参数 `mon` 对应 [Month](time_package_enums.md#enum-month) 类型实例。

参数：

- mon: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 整数形式的月，合法范围为 [1, 12]，分别表示一年中的十二个月。

返回值：

- [Month](time_package_enums.md#enum-month) - 参数 `mon` 对应的 [Month](time_package_enums.md#enum-month) 类型实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `mon` 不在 [1, 12] 范围内时，抛出异常。

### func toInteger()

```cangjie
public func toInteger(): Int64
```

功能：获取当前 [Month](time_package_enums.md#enum-month) 实例的整数表示，一月至十二月分别表示为 1 至 12。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Month](time_package_enums.md#enum-month) 实例的整数表示。

### func toString()

```cangjie
public func toString(): String
```

功能：返回当前 [Month](time_package_enums.md#enum-month) 实例的字符串表示，如 "January" 表示一月。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [Month](time_package_enums.md#enum-month) 实例的字符串表示。