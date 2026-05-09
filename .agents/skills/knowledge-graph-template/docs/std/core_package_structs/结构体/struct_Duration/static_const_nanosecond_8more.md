### static const nanosecond

```cangjie
public static const nanosecond: Duration = Duration(0, 1)
```

功能：表示 1 纳秒时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const second

```cangjie
public static const second: Duration = Duration(1, 0)
```

功能：表示 1 秒时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const Zero

```cangjie
public static const Zero: Duration = Duration(0, 0)
```

功能：表示 0 纳秒时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### func abs()

```cangjie
public func abs(): Duration
```

功能：返回一个新的 [Duration](core_package_structs.md#struct-duration) 实例，其值大小为当前 [Duration](core_package_structs.md#struct-duration) 实例绝对值。

返回值：

- [Duration](core_package_structs.md#struct-duration) - 当前 [Duration](core_package_structs.md#struct-duration) 实例取绝对值的结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 如果当前 [Duration](core_package_structs.md#struct-duration) 实例等于 [Duration](core_package_structs.md#struct-duration).Min，会因为取绝对值超出 [Duration](core_package_structs.md#struct-duration) 表示范围而抛出异常。

### func compare(Duration)

```cangjie
public func compare(rhs: Duration): Ordering
```

功能：比较当前 [Duration](core_package_structs.md#struct-duration) 实例与另一个 [Duration](core_package_structs.md#struct-duration) 实例的关系，如果大于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT。

参数：

- rhs: [Duration](core_package_structs.md#struct-duration) - 参与比较的 [Duration](core_package_structs.md#struct-duration) 实例。

返回值：

- [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 当前 [Duration](core_package_structs.md#struct-duration) 实例与 `rhs` 的大小关系。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例的哈希值。

### func toDays()

```cangjie
public func toDays(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以天为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以天为单位的大小。

### func toHours()

```cangjie
public func toHours(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以小时为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以小时为单位的大小。