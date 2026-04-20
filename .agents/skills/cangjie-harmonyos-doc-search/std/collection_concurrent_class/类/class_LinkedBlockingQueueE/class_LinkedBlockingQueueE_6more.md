## class LinkedBlockingQueue\<E>

```cangjie
public class LinkedBlockingQueue<E> {
    public let capacity: Int64
    public init()
    public init(capacity: Int64)
    public init(capacity: Int64, elements: Array<E>)
    public init(capacity: Int64, elements: Collection<E>)
}
```

功能：实现是带阻塞机制并支持用户指定容量上界的并发队列。

阻塞队列的特点是，当队列满时，尝试向队列中添加元素的线程会被阻塞，直到队列有空余位置；当队列空时，尝试从队列中获取元素的线程会被阻塞，直到队列有可取元素。

### let capacity

```cangjie
public let capacity: Int64
```

功能：返回此 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee) 的容量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：返回此 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee) 的元素个数。

> **注意：**
>
> 此方法不保证并发场景下的原子性，建议在环境中没有其他线程并发地修改 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee) 时调用。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个具有默认初始容量（[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).Max）的 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee)。

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个带有传入容量大小的 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于等于 0 则抛出异常。

### init(Int64, Array\<E>) <sup>(deprecated)</sup>

```cangjie
public init(capacity: Int64, elements: Array<E>)
```

功能：构造一个带有传入容量大小，并带有传入数组元素的 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee)。

> **注意：**
>
> 未来版本即将废弃，如需实现等效功能，可先创建空队列，再依次将数组中的元素添加到队列中。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。
- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<E> - 初始化数组元素。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于等于 0 或小于数组元素 elements 的 size 则抛出异常。