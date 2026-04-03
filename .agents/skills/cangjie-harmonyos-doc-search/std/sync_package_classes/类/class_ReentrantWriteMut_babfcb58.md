## class ReentrantWriteMutex <sup>(deprecated)</sup>

```cangjie
public class ReentrantWriteMutex <: ReentrantMutex {}
```

功能：提供可重入读写锁中的写锁类型。

> **注意：**
>
> 未来版本即将废弃，使用 [UniqueLock](./sync_package_interfaces.md#interface-uniquelock) 替代。

父类型：

- [ReentrantMutex <sup>(deprecated)</sup>](#class-reentrantmutex-deprecated)

### func lock()

```cangjie
public func lock(): Unit
```

功能：获取写锁。只允许唯一线程能够持有写锁，且该线程能多次重复持有写锁。如果存在其他线程持有写锁或是读锁，那么当前线程进入等待状态。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 当前线程已持有读锁。

### func tryLock()

```cangjie
public func tryLock(): Bool
```

功能：尝试获取写锁。该方法获取读锁时并不遵循公平模式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若成功获取写锁，返回 `true`；若未能获取写锁，返回 `false`。

### func unlock()

```cangjie
public func unlock(): Unit
```

功能：释放写锁。

> **注意：**
>
> - 如果一个线程多次持有读锁，那么仅当释放操作和获取操作数量相同时才释放读锁；如果读锁被释放并且存在线程等待写锁，那么唤醒其中一个线程。
> - 在公平模式下，如果写锁被释放并且存在线程等待读锁，那么优先唤醒这些等待线程；如果没有线程等待读锁，但存在线程等待写锁，那么唤醒其中一个线程。
> - 在非公平模式下，如果写锁被释放，优先唤醒等待写锁的线程还是等待读锁的线程不做保证，交由具体实现决定。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 当前线程未持有写锁。