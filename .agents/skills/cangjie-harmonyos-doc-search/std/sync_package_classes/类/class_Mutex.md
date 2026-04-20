## class Mutex

```cangjie
public class Mutex <: UniqueLock {
    public init()
}
```

功能：提供可重入互斥锁相关功能。

可重入互斥锁的作用是对临界区加以保护，使得任意时刻最多只有一个线程能够执行临界区的代码。
当一个线程试图获取一个已被其他线程持有的锁时，该线程会被阻塞，直到锁被释放，该线程才会被唤醒，可重入是指线程获取该锁后可再次获得该锁。

> **注意：**
>
> - 在访问共享数据之前，必须尝试获取锁。
> - 处理完共享数据后，必须进行解锁，以便其他线程可以获得锁。

父类型：

- [UniqueLock](./sync_package_interfaces.md#interface-uniquelock)

### init()

```cangjie
public init()
```

功能：创建可重入互斥锁。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 当出现系统错误时，抛出异常。

### func condition()

```cangjie
public func condition(): Condition
```

功能：创建一个与该 [Mutex](#class-mutex) 相关的 [Condition](./sync_package_interfaces.md#interface-condition)。

可能被用来实现 “单 Lock 多等待队列” 的并发原语。

返回值：

- [Condition](./sync_package_interfaces.md#interface-condition) - 创建的与该 [Mutex](#class-mutex) 相关的 [Condition](./sync_package_interfaces.md#interface-condition) 实例。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

### func lock()

```cangjie
public func lock(): Unit
```

功能：锁定互斥体，如果互斥体已被锁定，则阻塞。

### func tryLock()

```cangjie
public func tryLock(): Bool
```

功能：尝试锁定互斥体。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果互斥体已被锁定，则返回 `false`；反之，则锁定互斥体并返回 `true`。

### func unlock()

```cangjie
public func unlock(): Unit
```

功能：解锁互斥体。

如果互斥体被重复加锁了 N 次，那么需要调用 N 次该函数来完全解锁，一旦互斥体被完全解锁，如果有其他线程阻塞在此锁上，那么唤醒它们中的一个。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。