## class MultiConditionMonitor <sup>(deprecated)</sup>

```cangjie
public class MultiConditionMonitor <: ReentrantMutex {
    public init()
}
```

功能：提供对同一个互斥锁绑定多个条件变量的功能。

> **注意：**
>
> - 未来版本即将废弃，使用 [Mutex](#class-mutex) 替代。
> - 该类应仅当在 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated) 类不足以实现高级并发算法时被使用。
> - 初始化时，[MultiConditionMonitor <sup>(deprecated)</sup>](sync_package_classes.md#class-multiconditionmonitor-deprecated) 没有与之相关的条件变量。
> - 每次调用 `newCondition` 将创建一个新的等待队列并与当前对象关联，并返回[ConditionID <sup>(deprecated)</sup>](sync_package_structs.md#struct-conditionid-deprecated)类型实例作为唯一标识符。

父类型：

- [ReentrantMutex <sup>(deprecated)</sup>](#class-reentrantmutex-deprecated)

### init()

```cangjie
public init()
```

功能：通过默认构造函数创建 [MultiConditionMonitor <sup>(deprecated)</sup>](sync_package_classes.md#class-multiconditionmonitor-deprecated)。

### func newCondition()

```cangjie
public func newCondition(): ConditionID
```

功能：创建一个与该 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated) 相关的 [ConditionID <sup>(deprecated)</sup>](sync_package_structs.md#struct-conditionid-deprecated)，可能被用来实现 “单互斥体多等待队列” 的并发原语。

返回值：

- [ConditionID](sync_package_structs.md#struct-conditionid-deprecated) - 新的 [ConditionID <sup>(deprecated)</sup>](sync_package_structs.md#struct-conditionid-deprecated)。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

### func notify(ConditionID)

```cangjie
public func notify(condID: ConditionID): Unit
```

功能：唤醒等待在所指定的条件变量的线程（如果有）。

参数：

- condID: [ConditionID](sync_package_structs.md#struct-conditionid-deprecated) - 条件变量。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，或 `condID` 不是由该 [MultiConditionMonitor <sup>(deprecated)</sup>](sync_package_classes.md#class-multiconditionmonitor-deprecated) 实例通过 `newCondition` 函数创建时，抛出异常。

### func notifyAll(ConditionID)

```cangjie
public func notifyAll(condID: ConditionID): Unit
```

功能：唤醒所有等待在所指定的条件变量的线程（如果有）。

参数：

- condID: [ConditionID](sync_package_structs.md#struct-conditionid-deprecated) - 条件变量。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，或 `condID` 不是由该 [MultiConditionMonitor <sup>(deprecated)</sup>](sync_package_classes.md#class-multiconditionmonitor-deprecated) 实例通过 `newCondition` 函数创建时，抛出异常。