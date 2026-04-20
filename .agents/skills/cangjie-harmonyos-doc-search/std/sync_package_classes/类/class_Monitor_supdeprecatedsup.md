## class Monitor <sup>(deprecated)</sup>

```cangjie
public class Monitor <: ReentrantMutex {
    public init()
}
```

功能：提供使线程阻塞并等待来自另一个线程的信号以恢复执行的功能。

这是一种利用共享变量进行线程同步的机制，当一些线程因等待共享变量的某个条件成立而挂起时，另一些线程改变共享的变量，使条件成立，
然后执行唤醒操作。这使得挂起的线程被唤醒后可以继续执行。

> **注意：**
>
> 未来版本即将废弃，使用 [Condition](./sync_package_interfaces.md#interface-condition) 替代。

父类型：

- [ReentrantMutex <sup>(deprecated)</sup>](#class-reentrantmutex-deprecated)

### init()

```cangjie
public init()
```

功能：通过默认构造函数创建 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated)。

### func notify()

```cangjie
public func notify(): Unit
```

功能：唤醒一个等待在该 `Montior` 上的线程。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

### func notifyAll()

```cangjie
public func notifyAll(): Unit
```

功能：唤醒所有等待在该 `Montior` 上的线程。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

### func wait(Duration)

```cangjie
public func wait(timeout!: Duration = Duration.Max): Bool
```

功能：当前线程挂起，直到对应的 `notify` 函数被调用，或者挂起时间超过 `timeout`。

> **说明：**
>
> 线程在进入等待时会释放对应的互斥锁，被唤醒后再次持有互斥锁。

参数：

- timeout!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 挂起时间，其默认值为 [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果 [Monitor <sup>(deprecated)</sup>](sync_package_classes.md#class-monitor-deprecated) 被其他线程唤醒，返回 `true`；如果超时，则返回 `false`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `timeout` 小于等于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero)，抛出异常。
- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。