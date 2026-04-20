## 可重入互斥锁 Mutex

可重入互斥锁的作用是对临界区加以保护，使得任意时刻最多只有一个线程能够执行临界区的代码。当一个线程试图获取一个已被其他线程持有的锁时，该线程会被阻塞，直到锁被释放，该线程才会被唤醒，可重入是指线程获取该锁后可再次获得该锁。

使用可重入互斥锁时，必须牢记两条规则：

1. 在访问共享数据之前，必须尝试获取锁；
2. 处理完共享数据后，必须释放锁，以便其他线程可以获得锁。

`Mutex` 提供的主要成员函数如下：

```cangjie
public class Mutex <: UniqueLock {
    // Create a Mutex.
    public init()

    // Locks the mutex, blocks if the mutex is not available.
    public func lock(): Unit

    // Unlocks the mutex. If there are other threads blocking on this
    // lock, then wake up one of them.
    public func unlock(): Unit

    // Tries to lock the mutex, returns false if the mutex is not
    // available, otherwise returns true.
    public func tryLock(): Bool

    // Generate a Condition instance for the mutex.
    public func condition(): Condition
}
```

下方示例演示了如何使用 `Mutex` 来保护对全局共享变量 `count` 的访问，对 `count` 的操作即属于临界区：

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
            mtx.lock()
            count++
            mtx.unlock()
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

下方示例演示了如何使用 `tryLock`：

<!-- run -->

```cangjie
import std.sync.Mutex


main(): Int64 {
    let mtx: Mutex = Mutex()
    var future: Future<Unit> = spawn {
        mtx.lock()
        println("get the lock, do something")
        sleep(Duration.millisecond * 10)
        mtx.unlock()
    }
    try {
        future.get(Duration.millisecond * 10)
    } catch (e: TimeoutException) {
        if (mtx.tryLock()) {
            println("tryLock success, do something")
            mtx.unlock()
            return 0
        }
        println("tryLock failed, do nothing")
        return 0
    }
    return 0
}
```

一种可能的输出结果如下：

```text
get the lock, do something
```

以下是互斥锁的一些错误示例：

错误示例 1：线程操作临界区后没有解锁，导致其他线程无法获得锁而阻塞。

<!-- compile.error -->
<!-- cfg="libcangjie-std-sync" -->

```cangjie
import std.sync.Mutex

var sum: Int64 = 0
let mutex = Mutex()

main() {
    let foo = spawn { =>
        mutex.lock()
        sum = sum + 1
    }
    let bar = spawn { =>
        mutex.lock()
        sum = sum + 1
    }
    foo.get()
    println("${sum}")
    bar.get() // Because the thread is not unlocked, other threads waiting to obtain the current mutex will be blocked.
}
```

错误示例 2：在本线程没有持有锁的情况下调用 `unlock` 将会抛出异常。

<!-- compile.error -->
<!-- cfg="libcangjie-std-sync" -->

```cangjie
import std.sync.Mutex

var sum: Int64 = 0
let mutex = Mutex()

main() {
    let foo = spawn { =>
        sum = sum + 1
        mutex.unlock() // Error, Unlock without obtaining the lock and throw an exception: IllegalSynchronizationStateException.
    }
    foo.get()
}
```

错误示例 3：`tryLock()` 并不保证获取到锁，可能会造成不在锁的保护下操作临界区和在没有持有锁的情况下调用 `unlock` 抛出异常等行为。

<!-- compile.error -->
<!-- cfg="libcangjie-std-sync" -->

```cangjie
import std.sync.Mutex

var sum: Int64 = 0
let mutex = Mutex()

main() {
    for (i in 0..100) {
        spawn { =>
            mutex.tryLock() // Error, `tryLock()` just trying to acquire a lock, there is no guarantee that the lock will be acquired, and this can lead to abnormal behavior.
            sum = sum + 1
            mutex.unlock()
        }
    }
}
```

另外，`Mutex` 在设计上是一个可重入锁，也就是说：在某个线程已经持有一个 `Mutex` 锁的情况下，再次尝试获取同一个 `Mutex` 锁，永远可以立即获得该 `Mutex` 锁。

> **注意：**
>
> 虽然 `Mutex` 是一个可重入锁，但是调用 `unlock()` 的次数必须和调用 `lock()` 的次数相同，才能成功释放该锁。

下方示例代码演示了 `Mutex` 可重入的特性：

<!-- verify -->