## class Semaphore

```cangjie
public class Semaphore {
    public init(count: Int64)
}
```

功能：提供信号量相关功能。

[Semaphore](sync_package_classes.md#class-semaphore) 可以被视为携带计数器的 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated)，常用于控制并发访问共享资源的线程数量。

### prop count

```cangjie
public prop count: Int64
```

功能：返回当前内部计数器的值。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Int64)

```cangjie
public init(count: Int64)
```

功能：创建一个 [Semaphore](sync_package_classes.md#class-semaphore) 对象并初始化内部计数器的值。

参数：

- [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet): [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 计数器初始值, 取值范围 [0, [Int64](../../core/core_package_api/core_package_intrinsics.md#int64).Max]。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) 为负数时抛出异常。

### func acquire(Int64)

```cangjie
public func acquire(amount!: Int64 = 1): Unit
```

功能：向 [Semaphore](sync_package_classes.md#class-semaphore) 对象获取指定值。

如果当前计数器小于要求的数值，那么当前线程将被阻塞，直到获取满足数量的值后才被唤醒。

参数：

- amount!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 向对象内部计数器中获取的数值，默认值为 1。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数 `amount` 为负数，或大于初始值。

### func release(Int64)

```cangjie
public func release(amount!: Int64 = 1): Unit
```

功能：向 [Semaphore](sync_package_classes.md#class-semaphore) 对象释放指定值。

如果内部计数器在累加释放值后能够满足当前阻塞在 [Semaphore](sync_package_classes.md#class-semaphore) 对象的线程，那么将得到满足的线程唤醒；内部计数器的值不会大于初始值，即如果计数器的值在累加后大于初始值，那么仍被设置为初始值。所有在调用 `release` 之前的操作都先发生于调用 `acquire/tryAcquire` 之后的操作。

参数：

- amount!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 向对象内部计数器中释放的数值，默认值为 1。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数 `amount` 为负数，或大于初始值。

### func tryAcquire(Int64)

```cangjie
public func tryAcquire(amount!: Int64 = 1): Bool
```

功能：尝试向 [Semaphore](sync_package_classes.md#class-semaphore) 对象获取指定值。

该方法不会阻塞线程。如果有多个线程并发执行获取操作，则无法保证线程间的获取顺序。

参数：

- amount!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 向对象内部计数器中获取的数值，默认值为 1。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果当前计数器小于要求的数值，则获取失败并返回 `false`；成功获取值时返回 `true`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数 `amount` 为负数，或大于初始值。