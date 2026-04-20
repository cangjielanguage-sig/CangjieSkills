## struct Duration

```cangjie
public struct Duration <: ToString & Hashable & Comparable<Duration> {
    public static const Max: Duration = Duration(0x7FFF_FFFF_FFFF_FFFF, 999999999)
    public static const Min: Duration = Duration(-0x8000_0000_0000_0000, 0)
    public static const Zero: Duration = Duration(0, 0)
    public static const day: Duration = Duration(24 * 60 * 60, 0)
    public static const hour: Duration = Duration(60 * 60, 0)
    public static const microsecond: Duration = Duration(0, 1000u32)
    public static const millisecond: Duration = Duration(0, 1000000u32)
    public static const minute: Duration = Duration(60, 0)
    public static const nanosecond: Duration = Duration(0, 1)
    public static const second: Duration = Duration(1, 0)
}
```

功能：[Duration](core_package_structs.md#struct-duration) 表示时间间隔，是一个描述一段时间的时间类型，提供了常用的静态实例，以及计算、比较等功能。

> **说明：**
>
> - [Duration](core_package_structs.md#struct-duration) 表示范围为 [Duration](core_package_structs.md#struct-duration).Min 至 [Duration](core_package_structs.md#struct-duration).Max，数值表示为 [-2<sup>63</sup>, 2<sup>63</sup>)（单位为秒），精度为纳秒。
> - [Duration](core_package_structs.md#struct-duration) 每个时间单位均用整数表示，如果实际值不为整数，则向绝对值小的方向取整。例如表示 `1 小时 30 分 46 秒` 的 [Duration](core_package_structs.md#struct-duration) 实例调用 `toHours` 方法，将返回结果 1 而不是 1.5 或 2。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)
- [Hashable](core_package_interfaces.md#interface-hashable)
- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Duration](#struct-duration)>

### static const day

```cangjie
public static const day: Duration = Duration(24 * 60 * 60, 0)
```

功能：表示 1 天时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const hour

```cangjie
public static const hour: Duration = Duration(60 * 60, 0)
```

功能：表示 1 小时时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const Max

```cangjie
public static const Max: Duration = Duration(0x7FFF_FFFF_FFFF_FFFF, 999999999)
```

功能：表示最大时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const microsecond

```cangjie
public static const microsecond: Duration = Duration(0, 1000u32)
```

功能：表示 1 微秒时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const millisecond

```cangjie
public static const millisecond: Duration = Duration(0, 1000000u32)
```

功能：表示 1 毫秒时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const Min

```cangjie
public static const Min: Duration = Duration(-0x8000_0000_0000_0000, 0)
```

功能：表示最小时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)

### static const minute

```cangjie
public static const minute: Duration = Duration(60, 0)
```

功能：表示 1 分钟时间间隔的 [Duration](core_package_structs.md#struct-duration) 实例。

类型：[Duration](core_package_structs.md#struct-duration)