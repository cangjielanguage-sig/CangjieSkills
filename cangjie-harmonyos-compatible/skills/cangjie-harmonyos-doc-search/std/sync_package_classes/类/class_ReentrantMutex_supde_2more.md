## class ReentrantMutex <sup>(deprecated)</sup>

```cangjie
public open class ReentrantMutex <: Lock {
    public init()
}
```

功能：提供可重入锁相关功能。

可重入互斥锁的作用是对临界区加以保护，使得任意时刻最多只有一个线程能够执行临界区的代码。
当一个线程试图获取一个已被其他线程持有的锁时，该线程会被阻塞，直到锁被释放，该线程才会被唤醒，可重入是指线程获取该锁后可再次获得该锁。

> **注意：**
>
> - 未来版本即将废弃，使用 [Mutex](#class-mutex) 替代。
> - [ReentrantMutex <sup>(deprecated)</sup>](sync_package_classes.md#class-reentrantmutex-deprecated) 是内置的互斥锁，开发者需要保证不继承它。
> - 在访问共享数据之前，必须尝试获取锁。
> - 处理完共享数据后，必须进行解锁，以便其他线程可以获得锁。

父类型：

- [Lock](sync_package_interfaces.md#interface-lock)

### init()

```cangjie
public init()
```

功能：创建可重入互斥锁。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 当出现系统错误时，抛出异常。

### func lock()

```cangjie
public open func lock(): Unit
```

功能：锁定互斥体，如果互斥体已被锁定，则阻塞。

### func tryLock()

```cangjie
public open func tryLock(): Bool
```

功能：尝试锁定互斥体。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果互斥体已被锁定，则返回 `false`；反之，则锁定互斥体并返回 `true`。

### func unlock()

```cangjie
public open func unlock(): Unit
```

功能：解锁互斥体。

如果互斥体被重复加锁了 N 次，那么需要调用 N 次该函数来完全解锁，一旦互斥体被完全解锁，如果有其他线程阻塞在此锁上，那么唤醒它们中的一个。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

## class ReentrantReadMutex <sup>(deprecated)</sup>

```cangjie
public class ReentrantReadMutex <: ReentrantMutex {}
```

功能：提供可重入读写锁中的读锁类型。

> **注意：**
>
> 未来版本即将废弃，使用 [Lock](./sync_package_interfaces.md#interface-lock) 替代。

父类型：

- [ReentrantMutex <sup>(deprecated)</sup>](#class-reentrantmutex-deprecated)

### func lock()

```cangjie
public func lock(): Unit
```

功能：获取读锁。

> **注意：**
>
> - 在公平模式下，如果没有其他线程持有或等待写锁，或是当前线程已持有读锁，则立即持有读锁；否则，当前线程进入等待状态。
> - 在非公平模式下，如果没有其他线程持有或等待写锁，则立即持有读锁；如果有其他线程持有写锁，当前线程进入等待状态；否则，线程是否能立即持有读锁不做保证。
> - 多个线程可以同时持有读锁并且一个线程可以重复多次持有读锁；如果一个线程持有写锁，那么它仍可以持有读锁。

### func tryLock()

```cangjie
public func tryLock(): Bool
```

功能：尝试获取读锁。该方法获取读锁时并不遵循公平模式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若成功获取读锁，返回 `true`；若未能获取读锁，返回 `false`。

### func unlock()

```cangjie
public func unlock(): Unit
```

功能：释放读锁。如果一个线程多次持有读锁，那么仅当释放操作和获取操作数量相同时才释放读锁；如果读锁被释放并且存在线程等待写锁，那么唤醒其中一个线程。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 当前线程未持有读锁，那么将抛出异常。