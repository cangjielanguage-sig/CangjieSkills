## 线程局部变量 ThreadLocal

使用 core 包中的 `ThreadLocal` 可以创建并使用线程局部变量，每一个线程都有它独立的一个存储空间来保存这些线程局部变量。因此，在每个线程可以安全地访问他们各自的线程局部变量，而不受其他线程的影响。

```cangjie
public class ThreadLocal<T> {
    /* 构造一个携带空值的仓颉线程局部变量 */
    public init()

    /* 获得仓颉线程局部变量的值 */
    public func get(): Option<T> // 如果值不存在，则返回 Option<T>.None。返回值 Option<T> - 仓颉线程局部变量的值

    /* 通过 value 设置仓颉线程局部变量的值 */
    public func set(value: Option<T>): Unit // 如果传入 Option<T>.None，该局部变量的值将被删除，在线程后续操作中将无法获取。参数 value - 需要设置的局部变量的值。
}
```

下方示例代码演示了如何通过 `ThreadLocal`类来创建并使用各自线程的局部变量：

<!-- run -->

```cangjie

main(): Int64 {
    let tl = ThreadLocal<Int64>()
    let fut1 = spawn {
        tl.set(123)
        println("tl in spawn1 = ${tl.get().getOrThrow()}")
    }
    let fut2 = spawn {
        tl.set(456)
        println("tl in spawn2 = ${tl.get().getOrThrow()}")
    }
    fut1.get()
    fut2.get()
    0
}
```

可能的输出结果如下：

```text
tl in spawn1 = 123
tl in spawn2 = 456
```

或者

```text
tl in spawn2 = 456
tl in spawn1 = 123
```