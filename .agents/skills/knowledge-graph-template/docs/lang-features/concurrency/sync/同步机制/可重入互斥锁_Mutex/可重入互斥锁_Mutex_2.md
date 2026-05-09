```cangjie
import std.sync.Mutex

var count: Int64 = 0
let mtx = Mutex()

func foo() {
    mtx.lock()
    count += 10
    bar()
    mtx.unlock()
}

func bar() {
    mtx.lock()
    count += 100
    mtx.unlock()
}

main(): Int64 {
    let fut = spawn {
        sleep(Duration.millisecond) // sleep for 1ms.
        foo()
    }

    foo()

    fut.get()

    println("count = ${count}")
    return 0
}
```

输出结果应为：

```text
count = 220
```

在上方示例中，无论是主线程还是新创建的线程，如果在 `foo()` 中已经获得了锁，那么继续调用 `bar()` 的话，在 `bar()` 函数中由于是对同一个 `Mutex` 进行加锁，因此也是能立即获得该锁的，不会出现死锁。