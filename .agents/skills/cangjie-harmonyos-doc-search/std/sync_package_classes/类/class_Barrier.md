## class Barrier

```cangjie
public class Barrier {
    public init(count: Int64)
}
```

功能：提供协调多个线程一起执行到某一个程序点的功能。

率先达到程序点的线程将进入阻塞状态，当所有线程都达到程序点后，才一起继续执行。

### init(Int64)

```cangjie
public init(count: Int64)
```

功能：创建 [Barrier](sync_package_classes.md#class-barrier) 对象。

参数：

- count: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 表示需要协调的线程数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) 为负数。

### func wait(Duration)

```cangjie
public func wait(timeout!: Duration = Duration.Max): Unit
```

功能：线程进入 [Barrier](sync_package_classes.md#class-barrier) 等待点。

如果 [Barrier](sync_package_classes.md#class-barrier) 对象所有调用 `wait` 的次数（即进入等待点的线程数）等于初始值，那么唤醒所有等待的线程；如果调用 `wait` 方法次数仍小于初始值，那么当前线程进入阻塞状态直到被唤醒或者等待时间超过 `timeout`；如果调用 `wait` 次数已大于初始值，那么线程继续执行。

参数：

- timeout!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 阻塞时等待的最大时长，其默认值为 [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)。