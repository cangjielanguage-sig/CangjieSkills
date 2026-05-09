## synchronized 关键字

`Lock` 提供了一种便利灵活的加锁的方式，同时因为它的灵活性，也可能引起忘记解锁，或者在持有锁的情况下抛出异常不能自动释放持有的锁的问题。因此，仓颉编程语言提供一个 `synchronized` 关键字，搭配 `Lock` 一起使用，可以在其后跟随的作用域内自动进行加锁解锁操作，用来解决类似的问题。

下方示例代码演示了如何使用 `synchronized` 关键字来保护共享数据：

<!-- verify -->

```cangjie
import std.sync.Mutex
import std.collection.ArrayList

var count: Int64 = 0
let mtx = Mutex()

main(): Int64 {
    let list = ArrayList<Future<Unit>>()

    // create 1000 threads.
    for (i in 0..1000) {
        let fut = spawn {
            sleep(Duration.millisecond) // sleep for 1ms.
            // Use synchronized(mtx), instead of mtx.lock() and mtx.unlock().
            synchronized(mtx) {
                count++
            }
        }
        list.add(fut)
    }

    // Wait for all threads finished.
    for (f in list) {
        f.get()
    }

    println("count = ${count}")
    return 0
}
```

输出结果应为：

```text
count = 1000
```

通过在 `synchronized` 后面加上一个 `Lock` 实例，对其后面修饰的代码块进行保护，可以使得任意时刻最多只有一个线程可以执行被保护的代码：

1. 一个线程在进入 `synchronized` 修饰的代码块之前，会自动获取 `Lock` 实例对应的锁，如果无法获取锁，则当前线程被阻塞；
2. 一个线程在退出 `synchronized` 修饰的代码块之前，会自动释放该 `Lock` 实例的锁。

对于控制转移表达式（如 `break`、`continue`、`return`、`throw`），在导致程序的执行跳出 `synchronized` 代码块时，也符合上面第 2 条的说明，也就说也会自动释放 `synchronized` 表达式对应的锁。

下方示例演示了在 `synchronized` 代码块中出现 `break` 语句的情况：

<!-- verify -->

```cangjie
import std.sync.Mutex
import std.collection.ArrayList

var count: Int64 = 0
var mtx: Mutex = Mutex()

main(): Int64 {
    let list = ArrayList<Future<Unit>>()
    for (i in 0..10) {
        let fut = spawn {
            while (true) {
                synchronized(mtx) {
                    count = count + 1
                    break
                    println("in thread")
                }
            }
        }
        list.add(fut)
    }

    // Wait for all threads finished.
    for (f in list) {
        f.get()
    }

    synchronized(mtx) {
        println("in main, count = ${count}")
    }
    return 0
}
```

输出结果应为：

```text
in main, count = 10
```

实际上 `in thread` 这行不会被打印，因为 `break` 语句实际上会让程序执行跳出 `while` 循环（在跳出 `while` 循环之前，先跳出 `synchronized` 代码块）。