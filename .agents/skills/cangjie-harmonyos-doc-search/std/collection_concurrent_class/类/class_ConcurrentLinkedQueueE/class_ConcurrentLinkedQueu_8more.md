## class ConcurrentLinkedQueue\<E>

```cangjie
public class ConcurrentLinkedQueue<E> <: Collection<E> {
    public init()
    public init(elements: Collection<E>)
}
```

功能：提供一个线程安全的队列，可以在多线程环境下安全地进行元素的添加和删除操作。

非阻塞队列的目的是为了解决多线程环境下的同步问题，使得多个线程可以并发地进行队列的操作，而不会出现数据冲突或者死锁的问题。

非阻塞队列在多线程编程中非常常见，它可以用于任何需要线程安全队列的场景，例如生产者消费者模型、任务调度、线程池等。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<E>

使用示例：

使用示例见 [ConcurrentLinkedQueue 使用示例](../collection_concurrent_samples/sample_concurrent_linked_queue.md)。

### prop size

```cangjie
public prop size: Int64
```

功能：获取此 [ConcurrentLinkedQueue](collection_concurrent_class.md#class-concurrentlinkedqueuee) 的元素个数。

> **注意：**
>
> 此方法不保证并发场景下的原子性，建议在环境中没有其他线程并发地修改 [ConcurrentLinkedQueue](collection_concurrent_class.md#class-concurrentlinkedqueuee) 时调用。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ConcurrentLinkedQueue](collection_concurrent_class.md#class-concurrentlinkedqueuee) 实例。

### init(Collection\<E>) <sup>(deprecated)</sup>

```cangjie
public init(elements: Collection<E>)
```

功能：根据 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<E> 实例构造一个 [ConcurrentLinkedQueue](collection_concurrent_class.md#class-concurrentlinkedqueuee) 实例。

> **注意：**
>
> 未来版本即将废弃，如需实现等效功能，可先创建空队列，再依次将 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中元素添加到队列中。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<E> - 将该容器中元素放入新构造的 [ConcurrentLinkedQueue](collection_concurrent_class.md#class-concurrentlinkedqueuee)

### func add(E)

```cangjie
public func add(element: E): Bool
```

功能：非阻塞的入队操作，将元素添加到队列尾部。

> **注意：**
>
> 该函数不会返回 false。

参数：

- element: E - 要添加的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素则返回 true。

### func dequeue() <sup>(deprecated)</sup>

```cangjie
public func dequeue(): Option<E>
```

功能：获取并删除队首元素。

> **注意：**
>
> 未来版本即将废弃，使用 [remove()](#func-remove-2) 替代。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 成功删除则返回队首元素，队列为空则返回 None。

### func enqueue(E) <sup>(deprecated)</sup>

```cangjie
public func enqueue(element: E): Bool
```

功能：非阻塞的入队操作，将元素添加到队列尾部。

> **注意：**
>
> - 该函数不会返回 false。
> - 未来版本即将废弃，使用 [add(E)](#func-adde-2) 替代。

参数：

- element: E - 要添加的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素则返回 true。

### func head() <sup>(deprecated)</sup>

```cangjie
public func head(): Option<E>
```

功能：获取队首元素，不会删除该元素。

> **注意：**
>
> 未来版本即将废弃，使用 [peek()](#func-peek-2) 替代。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 成功获取则返回队首元素，队列为空则返回 None。