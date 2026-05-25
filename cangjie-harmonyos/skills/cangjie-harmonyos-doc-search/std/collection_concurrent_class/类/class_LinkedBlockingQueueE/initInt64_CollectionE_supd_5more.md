### init(Int64, Collection\<E>) <sup>(deprecated)</sup>

```cangjie
public init(capacity: Int64, elements: Collection<E>)
```

功能：构造一个带有传入容量大小，并带有传入迭代器的 [LinkedBlockingQueue](collection_concurrent_class.md#class-linkedblockingqueuee)。

> **注意：**
>
> 未来版本即将废弃，如需实现等效功能，可先创建空队列，再依次将 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的元素添加到队列中。

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
    var blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)
    blockArr.add(10)
    println(blockArr.peek())
}
```

运行结果：

```text
Some(10)
```

### func add(E, Duration)

```cangjie
public func add(element: E, timeout: Duration): Bool
```

功能：阻塞的入队操作，将元素添加到队列尾部，如果队列满了，将等待指定的时间。如果 timeout 为负，则会立即执行入队操作并且返回操作结果。

参数：

- element: E - 要添加的元素。
- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素返回 true。超出等待时间还未成功添加元素返回 false。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*
import std.sync.*
import std.time.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)

    /* 创建新线程，填满阻塞队列，休眠 1 秒后移除阻塞队列队首元素 */
    spawn {
        =>
        blockArr.add(0)
        blockArr.add(1)
        sleep(1000 * Duration.millisecond)
        println("New thread moves out of blocked queue head element.")
        blockArr.remove()
    }

    /* 主线程立即让出执行权，唤醒后阻塞的添加 */
    sleep(-1 * Duration.millisecond)
    println("The main thread is woken up.")
    let isSuccess: Bool = blockArr.add(2, 2000 * Duration.millisecond)
    println(isSuccess)
}
```

运行结果：

```text
The main thread is woken up.
New thread moves out of blocked queue head element.
true
```

### func dequeue() <sup>(deprecated)</sup>

```cangjie
public func dequeue(): E
```

功能：阻塞的出队操作，获得队首元素并删除。

> **注意：**
>
> 未来版本即将废弃，使用 [remove()](#func-remove-1) 替代。

返回值：

- E - 返回队首元素。

### func dequeue(Duration) <sup>(deprecated)</sup>

```cangjie
public func dequeue(timeout: Duration): Option<E>
```

功能：阻塞的出队操作，获得队首元素并删除。如果队列为空，将等待指定的时间。如果 timeout 为负，则会立即执行出队操作并且返回操作结果。

> **注意：**
>
> 未来版本即将废弃，使用 [remove(Duration)](#func-removeduration-1) 替代。

参数：

- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素。如果超出等待时间还未成功获取队首元素，则返回 None。