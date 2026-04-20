## 使用 `Future<T>` 等待线程结束并获取返回值

在上面的例子中，新创建的线程会由于主线程结束而提前结束，在缺乏顺序保证的情况下，甚至可能会出现新创建的线程还来不及得到执行就退出了。可以通过 `spawn` 表达式的返回值，来等待线程执行结束。

`spawn` 表达式的返回类型是 `Future<T>`，其中 `T` 是类型变元，其类型与 lambda 表达式的返回类型一致。当调用 `Future<T>` 的 `get()` 成员函数时，它将等待它的线程执行完成。

`Future<T>` 的原型声明如下：

```cangjie
public class Future<T> {
    // Blocking the current thread, waiting for the result of the thread corresponding to the current Future object.
    // If an exception occurs in the corresponding thread, the method will throw the exception.
    public func get(): T

    // Blocking the current thread, waiting for the result of the thread corresponding to the current Future object.
    // If the corresponding thread has not completed execution within Duration, the method will throws TimeoutException.
    // If `timeout` <= Duration.Zero, its behavior is the same as `get()`.
    public func get(timeout: Duration): T

    // Non-blocking method that immediately returns Option<T>.None if thread has not finished execution.
    // Returns the computed result otherwise.
    // If an exception occurs in the corresponding thread, the method will throw the exception.
    public func tryGet(): Option<T>
}
```

下方示例代码演示了如何使用 `Future<T>` 在 `main` 中等待新创建的线程执行完成：

<!-- run -->

```cangjie
main(): Int64 {
    let fut: Future<Unit> = spawn { =>
        println("New thread before sleeping")
        sleep(100 * Duration.millisecond) // sleep for 100ms.
        println("New thread after sleeping")
    }

    println("Main thread")

    fut.get() // wait for the thread to finish.
    return 0
}
```

调用 `Future<T>` 实例的 `get()` 会阻塞当前运行的线程，直到 `Future<T>` 实例所代表的线程运行结束。因此，上方示例有可能会输出类似如下内容：

```text
New thread before sleeping
Main thread
New thread after sleeping
```

主线程在完成打印后会因为调用 `get()` 而等待新创建的线程执行结束。但主线程和新线程的打印顺序具有不确定性。

如果将 `fut.get()` 移动到主线程的打印之前，如下所示：

<!-- verify -->

```cangjie
main(): Int64 {
    let fut: Future<Unit> = spawn { =>
        println("New thread before sleeping")
        sleep(100 * Duration.millisecond) // sleep for 100ms.
        println("New thread after sleeping")
    }

    fut.get() // wait for the thread to finish.

    println("Main thread")
    return 0
}
```

主线程将等待新创建的线程执行完成，然后再执行打印，因此程序的输出将变得确定，如下所示：

```text
New thread before sleeping
New thread after sleeping
Main thread
```

可见，`get()` 的调用位置会影响线程是否能同时运行。

`Future<T>` 除了可以用于阻塞等待线程执行结束以外，还可以获取线程执行的结果。如下是它提供的具体成员函数：

- `get(): T`：阻塞等待线程执行结束，并返回执行结果，如果该线程已经结束，则直接返回执行结果。

    示例代码如下：

    <!-- verify -->

    ```cangjie
    main(): Int64 {
        let fut: Future<Int64> = spawn {
            sleep(Duration.second) // sleep for 1s.
            return 1
        }

        try {
            // wait for the thread to finish, and get the result.
            let res: Int64 = fut.get()
            println("result = ${res}")
        } catch (_) {
            println("oops")
        }
        return 0
    }
    ```

    输出结果如下：

    ```text
    result = 1
    ```

- `get(timeout: Duration): T`：阻塞等待该 `Future<T>` 所代表的线程执行结束，并返回执行结果，当到达超时时间 timeout 时，如果该线程还没有执行结束，将会抛出异常 TimeoutException。如果 `timeout <= Duration.Zero`, 其行为与 `get()` 相同。

    示例代码如下：

    <!-- verify -->

    ```cangjie
    main(): Int64 {
        let fut = spawn {
            sleep(Duration.second) // sleep for 1s.
            return 1
        }

        // wait for the thread to finish, but only for 1ms.
        try {
            let res = fut.get(Duration.millisecond * 1)
            println("result: ${res}")
        } catch (_: TimeoutException) {
            println("oops")
        }
        return 0
    }

    ```

    输出结果如下：

    ```text
    oops
    ```