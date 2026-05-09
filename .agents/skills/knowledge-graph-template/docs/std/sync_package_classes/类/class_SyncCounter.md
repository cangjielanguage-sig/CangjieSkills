## class SyncCounter

```cangjie
public class SyncCounter {
    public init(count: Int64)
}
```

功能：提供倒数计数器功能。

线程可以等待计数器变为零。

### prop count

```cangjie
public prop count: Int64
```

功能：获取计数器的当前值。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Int64)

```cangjie
public init(count: Int64)
```

功能：创建倒数计数器。

参数：

- [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet): [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 倒数计数器的初始值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果参数 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) 为负数。

### func dec()

```cangjie
public func dec(): Unit
```

功能：计数器减一。

如果计数器变为零，那么唤醒所有等待的线程；如果计数器已经为零，那么数值保持不变。

### func waitUntilZero(Duration)

```cangjie
public func waitUntilZero(timeout!: Duration = Duration.Max): Unit
```

功能：当前线程等待直到计数器变为零，或等待时间超过 `timeout`。

参数：

- timeout!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 阻塞时等待的最大时长，其默认值为 [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)。