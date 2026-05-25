## class ArrayBlockingQueue\<E>

```cangjie
public class ArrayBlockingQueue<E> {
    public let capacity: Int64
    public init(capacity: Int64)
    public init(capacity: Int64, elements: Collection<E>)
}
```

功能：基于数组实现的 Blocking Queue 数据结构及相关操作函数。

[ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee) 是带阻塞机制且需要用户指定容量上界的并发队列。

### let capacity

```cangjie
public let capacity: Int64
```

功能：此 [ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee) 的容量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：返回此 [ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee) 的元素个数。

> **注意：**
>
> 此方法不保证并发场景下的原子性，建议在环境中没有其他线程并发地修改 [ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee) 时调用。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个带有传入容量大小的 [ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于等于 0 则抛出异常。

### init(Int64, Collection\<E>) <sup>(deprecated)</sup>

```cangjie
public init(capacity: Int64, elements: Collection<E>)
```

功能：构造一个带有传入容量大小，并带有传入迭代器的 [ArrayBlockingQueue](collection_concurrent_class.md#class-arrayblockingqueuee)。

> **注意：**
>
> 未来版本即将废弃，同等功能替代写法为：创建空队列，再将 elements 中元素依次添加到队列中。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。
- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<E> - 初始化迭代器元素。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于等于 0 或小于迭代器元素 elements 的 size 则抛出异常。

### func add(E)

```cangjie
public func add(element: E): Unit
```

功能：阻塞的入队操作，将元素添加到队列尾部。如果队列已满，则阻塞等待。

参数：

- element: E - 要添加的元素。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    var blockArr: ArrayBlockingQueue<Int64> = ArrayBlockingQueue<Int64>(2)
    blockArr.add(10)
    println(blockArr.peek())
}
```

运行结果：

```text
Some(10)
```