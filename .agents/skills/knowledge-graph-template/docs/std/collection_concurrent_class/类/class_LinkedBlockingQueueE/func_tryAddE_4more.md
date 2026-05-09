### func tryAdd(E)

```cangjie
public func tryAdd(element: E): Bool
```

功能：非阻塞的入队操作，将元素添加到队列尾部。

参数：

- element: E - 要添加的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加返回 true；如果队列满了，添加失败返回 false。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)
    blockArr.tryAdd(2)
    blockArr.tryAdd(3)
    println(blockArr.size)
}
```

运行结果：

```text
2
```

### func tryDequeue() <sup>(deprecated)</sup>

```cangjie
public func tryDequeue(): Option<E>
```

功能：非阻塞的出队操作，获得队首元素并删除。

> **注意：**
>
> 未来版本即将废弃，使用 [tryRemove()](#func-tryremove-1) 替代。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素，队列为空时返回 None。

### func tryEnqueue(E) <sup>(deprecated)</sup>

```cangjie
public func tryEnqueue(element: E): Bool
```

功能：非阻塞的入队操作，将元素添加到队列尾部。

> **注意：**
>
> 未来版本即将废弃，使用 [tryAdd(E)](#func-tryadde-1) 替代。

参数：

- element: E - 要添加的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 成功添加返回 true；如果队列满了，添加失败返回 false。

### func tryRemove()

```cangjie
public func tryRemove(): Option<E>
```

功能：非阻塞的出队操作，获得队首元素并删除。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 返回队首元素，队列为空时返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let blockArr: LinkedBlockingQueue<Int64> = LinkedBlockingQueue<Int64>(2)
    blockArr.tryAdd(3)
    println(blockArr.tryRemove())
    println(blockArr.tryRemove())
}
```

运行结果：

```text
Some(3)
None
```