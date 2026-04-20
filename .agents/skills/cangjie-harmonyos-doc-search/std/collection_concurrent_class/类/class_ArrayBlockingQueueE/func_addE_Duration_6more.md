### func add(E, Duration)

```cangjie
public func add(element: E, timeout: Duration): Bool
```

功能：阻塞的入队操作，将元素添加到队列尾部，如果队列满了，将等待指定的时间。如果 timeout 为负，则会立即执行入队操作并且返回操作结果。

参数：

- element: E - 要添加的元素。
- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素返回 true，超出等待时间还未成功添加元素返回 false。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*
import std.sync.*
import std.time.*

main() {
    let blockArr: ArrayBlockingQueue<Int64> = ArrayBlockingQueue<Int64>(2)

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
> 未来版本即将废弃，使用 [remove()](#func-remove) 替代。

返回值：

- E - 返回队首元素。

### func dequeue(Duration) <sup>(deprecated)</sup>

```cangjie
public func dequeue(timeout: Duration): Option<E>
```

功能：阻塞的出队操作，获得队首元素并删除，如果队列为空，将等待指定的时间。如果 timeout 为负，则会立即执行出队操作并且返回操作结果。

> **注意：**
>
> 未来版本即将废弃，使用 [remove(Duration)](#func-removeduration) 替代。

参数：

- timeout: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待时间。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素。如果超出等待时间还未成功获取队首元素，则返回 None。

### func enqueue(E) <sup>(deprecated)</sup>

```cangjie
public func enqueue(element: E): Unit
```

功能：阻塞的入队操作，将元素添加到队列尾部。

> **注意：**
>
> 未来版本即将废弃，使用 [add(E)](#func-adde) 替代。

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

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加元素返回 true，超出等待时间还未成功添加元素返回 false。

### func head() <sup>(deprecated)</sup>

```cangjie
public func head(): Option<E>
```

功能：获取队首元素。

该函数是非阻塞的。

> **注意：**
>
> 未来版本即将废弃，使用 [peek()](#func-peek) 替代。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素，队列为空时返回 None。