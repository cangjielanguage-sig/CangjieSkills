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
    let blockArr: ArrayBlockingQueue<Int64> = ArrayBlockingQueue<Int64>(2)
    blockArr.tryAdd(2)
    println(blockArr.tryRemove())
    println(blockArr.tryRemove())
}
```

运行结果：

```text
Some(2)
None
```