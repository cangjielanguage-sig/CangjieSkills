## interface IReentrantMutex <sup>(deprecated)</sup>

```cangjie
public interface IReentrantMutex {
    func lock(): Unit
    func tryLock(): Bool
    func unlock(): Unit
}
```

功能：提供实现可重入互斥锁的接口。

> **注意：**
>
> - 未来版本即将废弃，使用 [Lock](#interface-lock) 替代。
> - 开发者在实现该接口时需要保证底层互斥锁确实支持嵌套锁，否则在嵌套使用时，将会产生死锁问题。

### func lock()

```cangjie
func lock(): Unit
```

功能：锁定互斥体。

如果互斥体已被锁定，则阻塞当前线程。

### func tryLock()

```cangjie
func tryLock(): Bool
```

功能：尝试锁定互斥体。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果互斥体已被锁定，则返回 false；反之，则锁定互斥体并返回 true。

### func unlock()

```cangjie
func unlock(): Unit
```

功能：解锁互斥体。

如果互斥体被重复加锁了 N 次，那么需要调用 N 次该函数来完全解锁。一旦互斥体被完全解锁，如果有其他线程阻塞在此锁上，则唤醒其中一个线程。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

## interface Lock

```cangjie
public interface Lock {
    func lock(): Unit
    func tryLock(): Bool
    func unlock(): Unit
}
```

功能：提供实现可重入互斥锁的接口。

> **注意：**
>
> 开发者在实现该接口时需要保证底层互斥锁确实支持嵌套锁，否则在嵌套使用时，将会产生死锁问题。

### func lock()

```cangjie
func lock(): Unit
```

功能：锁定互斥体。

如果互斥体已被锁定，则阻塞当前线程。

### func tryLock()

```cangjie
func tryLock(): Bool
```

功能：尝试锁定互斥体。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果互斥体已被锁定，则返回 false；反之，则锁定互斥体并返回 true。

### func unlock()

```cangjie
func unlock(): Unit
```

功能：解锁互斥体。

如果互斥体被重复加锁了 N 次，那么需要调用 N 次该函数来完全解锁。一旦互斥体被完全解锁，如果有其他线程阻塞在此锁上，则唤醒其中一个线程。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。

## interface UniqueLock

```cangjie
public interface UniqueLock <: Lock {
    func condition(): Condition
}
```

功能：提供实现独占锁的接口。

父类型：

- [Lock](#interface-lock)

### func condition()

```cangjie
func condition(): Condition
```

功能：创建一个与该 [Lock](#interface-lock) 相关的 [Condition](#interface-condition)。

可能被用来实现 “单 Lock 多等待队列” 的并发原语。

返回值：

- [Condition](#interface-condition) - 创建的与该 [Lock](#interface-lock) 相关的 [Condition](#interface-condition) 实例。

异常：

- [IllegalSynchronizationStateException](sync_package_exceptions.md#class-illegalsynchronizationstateexception) - 如果当前线程没有持有该互斥体，抛出异常。