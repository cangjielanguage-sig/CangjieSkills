### func wait(ConditionID, Duration)

```cangjie
public func wait(condID: ConditionID, timeout!: Duration = Duration.Max): Bool
```

功能：当前线程挂起，直到对应的 `notify` 函数被调用。

> **说明：**
>
> 线程在进入等待时会释放对应的互斥锁，被唤醒后再次持有互斥锁。

参数：

- condID: [ConditionID](sync_package_structs.md#struct-conditionid-deprecated) - 条件变量。
- timeout!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 挂起时间，其默认值为 [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated) 指定的条件变量被其他线程唤醒，返回 `true`；如果超时，则返回 `false`。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，或者挂起时间超过 `timeout` 或 `condID` 不是由该 [MultiConditionMonitor <sup>(deprecated)</sup>](sync_package_classes.md#class-multiconditionmonitor-deprecated) 实例通过 `newCondition` 函数创建时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `timeout` 小于等于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero)，抛出异常。