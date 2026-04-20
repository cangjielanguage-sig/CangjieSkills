### func enqueue(E) <sup>(deprecated)</sup>

```cangjie
public func enqueue(element: E): Unit
```

功能：阻塞的入队操作，将元素添加到队列尾部。

> **注意：**
>
> 未来版本即将废弃，使用 [add(E)](#func-adde-1) 替代。

参数：

- element: E - 要添加的元素。

### func enqueue(E, Duration) <sup>(deprecated)</sup>

```cangjie
public func enqueue(element: E, timeout: Duration): Bool
```

功能：阻塞的入队操作，将元素添加到队列尾部，如果队列满了，将等待指定的时间。如果 timeout 为负，则会立即执行入队操作并且返回操作结果。

> **注意：**
>
> 未来版本即将废弃，使用 [add(E, Duration)](#func-adde-duration) 替代。

参数：

- element: E - 要添加的元素。
- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素返回 true。超出等待时间还未成功添加元素返回 false。

### func head() <sup>(deprecated)</sup>

```cangjie
public func head(): Option<E>
```

功能：获取队首元素。

> **注意：**
>
> - 该函数是非阻塞的。
> - 未来版本即将废弃，使用 [peek()](#func-peek-1) 替代。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素，队列为空时返回 None。

### func peek()

```cangjie
public func peek(): Option<E>
```

功能：获取队首元素。

> **注意：**
>
> 该函数是非阻塞的。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素，队列为空时返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)
    blockArr.add(2)
    blockArr.add(3)
    println(blockArr.peek())
}
```

运行结果：

```text
Some(2)
```

### func remove()

```cangjie
public func remove(): E
```

功能：阻塞的出队操作，获得队首元素并删除。

返回值：

- E - 返回队首元素。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)
    blockArr.add(2)
    blockArr.add(3)
    println(blockArr.remove())
    println(blockArr.size)
}
```

运行结果：

```text
2
1
```

### func remove(Duration)

```cangjie
public func remove(timeout: Duration): Option<E>
```

功能：阻塞的出队操作，获得队首元素并删除。如果队列为空，将等待指定的时间。如果 timeout 为负，则会立即执行出队操作并且返回操作结果。

参数：

- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素。如果超出等待时间还未成功获取队首元素，则返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*
import std.sync.*
import std.time.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)

    /* 创建新线程，休眠 1 秒后向队列添加元素 */
    spawn {
        =>
        sleep(1000 * Duration.millisecond)
        println("This new thread adds new elements to the queue.")
        blockArr.add(3)
    }

    /* 主线程立即让出执行权，唤醒后阻塞的取出队首元素 */
    sleep(-1 * Duration.millisecond)
    println("The main thread is woken up.")
    let num: Option<Int64> = blockArr.remove(2000 * Duration.millisecond)
    println(num)
}
```

运行结果：

```text
The main thread is woken up.
This new thread adds new elements to the queue.
Some(3)
```