## class Future\<T>

```cangjie
public class Future<T> {}
```

功能：[Future](core_package_classes.md#class-futuret)\<T> 实例代表一个仓颉线程任务，可用于获取仓颉线程的计算结果，向仓颉线程发送取消信号。

`spawn` 表达式的返回类型是 [Future](core_package_classes.md#class-futuret)\<T>，其中 `T` 的类型取决于 `spawn` 表达式中的闭包的返回值类型。

### prop thread

```cangjie
public prop thread: Thread
```

功能：获得对应仓颉线程的 [Thread](core_package_classes.md#class-thread) 实例。

类型：[Thread](core_package_classes.md#class-thread)

### func cancel()

```cangjie
public func cancel(): Unit
```

功能：给当前 [Future](core_package_classes.md#class-futuret) 实例对应的仓颉线程发送取消请求。该方法不会立即停止线程执行，仅发送请求，相应地，[Thread](core_package_classes.md#class-thread) 类的函数 `hasPendingCancellation` 可用于检查线程是否存在取消请求，开发者可以通过该检查来自行决定是否提前终止线程以及如何终止线程。

示例：

<!-- verify -->
```cangjie
main(): Unit {
    /* 创建线程 */
    let future = spawn {
        while (true) {
            if (Thread.currentThread.hasPendingCancellation) {
                return 0
            }
        }
        return 1
    }
    /* 向线程发送取消请求 */
    future.cancel()
    let res = future.get()
    println(res)
}
```

运行结果：

```text
0
```

### func get()

```cangjie
public func get(): T
```

功能：阻塞当前线程，等待并获取当前 [Future](core_package_classes.md#class-futuret)\<T> 对象对应的线程的结果。

返回值：

- T - 当前 [Future](core_package_classes.md#class-futuret)\<T> 实例代表的线程运行结束后的返回值。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let fut: Future<Int64> = spawn {
        =>
        sleep(1000 * Duration.millisecond) /* 睡眠 1 秒 */
        return 1
    }

    /* 等待线程完成 */
    let result: Int64 = fut.get()
    println(result)
    return 0
}
```

运行结果：

```text
1
```

### func get(Duration)

```cangjie
public func get(timeout: Duration): T
```

功能：阻塞当前线程，等待指定时长并获取当前 [Future](core_package_classes.md#class-futuret)\<T> 对象对应的线程的返回值。

需指定等待的超时时间，如果相应的线程在指定时间内未完成执行，则该函数将抛出异常 [TimeoutException](./core_package_exceptions.md#class-timeoutexception)。如果 timeout <= Duration.Zero，等同于 get()，即不限制等待时长。如果线程抛出异常退出执行，在 get 调用处将继续抛出该异常。

参数：

- timeout: [Duration](./core_package_structs.md#struct-duration) - 等待时间。

返回值：

- T - 返回指定时长后仓颉线程执行结果。

异常：

- [TimeoutException](./core_package_exceptions.md#class-timeoutexception) - 如果相应的线程在指定时间内未完成执行，则该函数将抛出此异常。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let fut: Future<Int64> = spawn {
        =>
        sleep(1000 * Duration.millisecond) /* 睡眠 1 秒 */
        return 1
    }

    let result: Int64 = fut.get(2000 * Duration.millisecond)
    /* 最大等待时间为 2 秒， 超过该时间抛出 TimeoutException */

    println(result)
    return 0
}
```

运行结果：

```text
1
```

### func tryGet()

```cangjie
public func tryGet(): Option<T>
```

功能：尝试获取执行结果，不会阻塞当前线程。如果相应的线程未完成，则该函数返回 `None`。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 如果当前仓颉线程未完成返回 `None`，否则返回执行结果。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let fut: Future<Int64> = spawn {
        =>
        sleep(1000 * Duration.millisecond) /* 睡眠 1 秒 */
        return 1
    }

    /* 主线程等待 4 秒，保证创建线程已经完成 */
    sleep(4000 * Duration.millisecond)

    /* 尝试获取创建线程的运行结果 */
    let result: Option<Int64> = fut.tryGet()
    println(result)
    return 0
}
```

运行结果：

```text
Some(1)
```