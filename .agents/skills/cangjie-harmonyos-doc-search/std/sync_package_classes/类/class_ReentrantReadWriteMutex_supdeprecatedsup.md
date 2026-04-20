## class ReentrantReadWriteMutex <sup>(deprecated)</sup>

```cangjie
public class ReentrantReadWriteMutex {
    public init(mode!: ReadWriteMutexMode = ReadWriteMutexMode.Unfair)
}
```

功能：提供可重入读写锁相关功能。

它和普通互斥锁的差异在于：读写锁同时携带两个互斥锁，分别为“读锁”以及“写锁”，并且它允许多个线程同时持有读锁。

> **注意：**
>
> 未来版本即将废弃，使用 [ReadWriteLock](#class-readwritelock) 替代。

读写锁的特殊性质说明：

- 写互斥性：只有唯一的线程能够持有写锁。当一个线程持有写锁，而其他线程再次获取锁（读锁或是写锁）时将被阻塞。
- 读并发性：允许多个线程同时持有读锁。当一个线程持有读锁，其他线程仍然可以获取读锁。但其他线程获取写锁时将被阻塞。
- 可重入性：一个线程可以重复获取锁。
    - 当线程已持有写锁时，它可以继续获取写锁或者读锁。只有当锁释放操作和获取操作一一对应时，锁才被完全释放。
    - 当线程已持有读锁时，它可以继续获取读锁。当锁释放操作和获取操作一一对应时，锁才被完全释放。注意，不允许在持有读锁的情况下获取写锁，这将抛出异常。
- 锁降级：一个线程在经历“持有写锁--持有读锁--释放写锁”后，它持有的是读锁而不再是写锁。
- 读写公平性：读写锁支持两种不同的模式，分别为“公平”及“非公平”模式。
    - 在非公平模式下，读写锁对线程获取锁的顺序不做任何保证。
    - 在公平模式下，当线程获取读锁时（当前线程未持有读锁），如果写锁已被获取或是存在线程等待写锁，那么当前线程无法获取读锁并进入等待。
    - 在公平模式下，写锁释放会优先唤醒所有读线程、读锁释放会优先唤醒一个等待写锁的线程。当存在多个线程等待写锁，它们之间被唤醒的先后顺序并不做保证。

### prop readMutex

```cangjie
public prop readMutex: ReentrantReadMutex
```

功能：获取读锁。

类型：[ReentrantReadMutex <sup>(deprecated)</sup>](sync_package_classes.md#class-reentrantreadmutex-deprecated)

### prop writeMutex

```cangjie
public prop writeMutex: ReentrantWriteMutex
```

功能：获取写锁。

类型：[ReentrantWriteMutex <sup>(deprecated)</sup>](sync_package_classes.md#class-reentrantwritemutex-deprecated)

### init(ReadWriteMutexMode)

```cangjie
public init(mode!: ReadWriteMutexMode = ReadWriteMutexMode.Unfair)
```

功能：构造读写锁。

参数：

- mode!: [ReadWriteMutexMode <sup>(deprecated)</sup>](sync_package_enums.md#enum-readwritemutexmode-deprecated) - 读写锁模式，默认值为 `Unfair`，即构造“非公平”的读写锁。