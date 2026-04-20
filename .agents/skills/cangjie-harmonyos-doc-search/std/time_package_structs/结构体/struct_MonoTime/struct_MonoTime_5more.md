## struct MonoTime

```cangjie
public struct MonoTime <: Hashable & Comparable<MonoTime> {}
```

功能：[MonoTime](time_package_structs.md#struct-monotime) 表示单调时间，是一个用来衡量经过时间的时间类型，类似于一直运行的秒表，提供了获取当前时间，计算和比较等功能。

- [MonoTime](time_package_structs.md#struct-monotime) 可表示的范围为 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero) 至 [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)，数值表示为 [0, 2<sup>63</sup>)（单位为秒），精度为纳秒。通过 [now](#static-func-now) 方法创建的 [MonoTime](time_package_structs.md#struct-monotime) 总是晚于先使用该方式创建的 [MonoTime](time_package_structs.md#struct-monotime)，常用于性能测试和时间优先的任务队列。
- 以下为 [MonoTime](time_package_structs.md#struct-monotime) 中 [now](#static-func-now) 函数获取当前时间使用的系统调用函数：

  | 系统    | 系统调用函数   | 时钟类型 |
  | ------- | ------------- |---------------- |
  | Linux   | clock_gettime | CLOCK_MONOTONIC |
  | Windows | clock_gettime | CLOCK_MONOTONIC |
  | macOS   | clock_gettime | CLOCK_MONOTONIC |

父类型：

- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [Comparable](../../core/core_package_api/core_package_interfaces.md#interface-comparablet)\<[MonoTime](#struct-monotime)>

### static func now()

```cangjie
public static func now(): MonoTime
```

功能：获取与当前时间对应的 [MonoTime](time_package_structs.md#struct-monotime)。

返回值：

- [MonoTime](time_package_structs.md#struct-monotime) - 与当前时间对应的 [MonoTime](time_package_structs.md#struct-monotime)。

### func compare(MonoTime)

```cangjie
public func compare(rhs: MonoTime): Ordering
```

功能：判断一个 [MonoTime](time_package_structs.md#struct-monotime) 实例与参数 `rhs` 的大小关系。如果大于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT。

参数：

- rhs: [MonoTime](time_package_structs.md#struct-monotime) - 参与比较的 [MonoTime](time_package_structs.md#struct-monotime) 实例。

返回值：

- [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 当前 [MonoTime](time_package_structs.md#struct-monotime) 实例与 `rhs` 大小关系。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取当前 [MonoTime](time_package_structs.md#struct-monotime) 实例的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 哈希值。

### operator func !=(MonoTime)

```cangjie
public operator func !=(r: MonoTime): Bool
```

功能：判断当前 [MonoTime](time_package_structs.md#struct-monotime) 实例是否不等于 `r`。

参数：

- r: [MonoTime](time_package_structs.md#struct-monotime) - 单调时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [MonoTime](time_package_structs.md#struct-monotime) 实例不等于 `r` 时，返回 `true`；否则，返回 `false`。