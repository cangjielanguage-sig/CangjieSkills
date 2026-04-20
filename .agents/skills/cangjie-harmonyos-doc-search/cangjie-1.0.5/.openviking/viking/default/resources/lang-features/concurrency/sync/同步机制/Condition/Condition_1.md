## Condition

`Condition` 是与某个互斥锁绑定的条件变量（也就是等待队列），`Condition` 实例由互斥锁创建，一个互斥锁可以创建多个 `Condition` 实例。`Condition` 可以使线程阻塞并等待来自另一个线程的信号以恢复执行。这是一种利用共享变量进行线程同步的机制，主要提供如下方法：

```cangjie
public class Mutex <: UniqueLock {
    // ...
    // Generate a Condition instance for the mutex.
    public func condition(): Condition
}

public interface Condition {
    // Wait for a signal, blocking the current thread.
    func wait(): Unit
    func wait(timeout!: Duration): Bool

    // Wait for a signal and predicate, blocking the current thread.
    func waitUntil(predicate: ()->Bool): Unit
    func waitUntil(predicate: ()->Bool, timeout!: Duration): Bool

    // Wake up one thread of those waiting on the monitor, if any.
    func notify(): Unit

    // Wake up all threads waiting on the monitor, if any.
    func notifyAll(): Unit
}
```

调用 `Condition` 接口的 `wait`、`notify` 或 `notifyAll` 方法前，需要确保当前线程已经持有绑定的锁。`wait` 方法包含如下动作：

1. 添加当前线程到对应锁的等待队列中；
2. 阻塞当前线程，同时完全释放该锁，并记录锁的重入次数；
3. 等待某个其他线程使用同一个 `Condition` 实例的 `notify` 或 `notifyAll` 方法向该线程发出信号；
4. 当前线程被唤醒后，会自动尝试重新获取锁，且持有锁的重入状态与第 2 步记录的重入次数相同；但是如果尝试获取锁失败，则当前线程会阻塞在该锁上。

`wait` 方法接受一个可选参数 `timeout`。需要注意的是，业界很多常用的常规操作系统不保证调度的实时性，因此无法保证一个线程会被阻塞“精确的 N 纳秒”——可能会观察到与系统相关的不精确情况。此外，当前语言规范明确允许实现产生虚假唤醒——在这种情况下，`wait` 返回值是由实现决定的——可能为 `true` 或 `false`。因此鼓励开发者始终将 `wait` 包在一个循环中：

```cangjie
synchronized (obj) {
  while (<condition is not true>) {
    obj.wait()
  }
}
```

以下是使用 `Condition` 的一个正确示例：

<!-- verify -->

```cangjie
import std.sync.Mutex

let mtx = Mutex()
let condition = synchronized(mtx) {
    mtx.condition()
}
var flag: Bool = true

main(): Int64 {
    let fut = spawn {
        mtx.lock()
        while (flag) {
            println("New thread: before wait")
            condition.wait()
            println("New thread: after wait")
        }
        mtx.unlock()
    }

    // Sleep for 10ms, to make sure the new thread can be executed.
    sleep(10 * Duration.millisecond)

    mtx.lock()
    println("Main thread: set flag")
    flag = false
    mtx.unlock()

    mtx.lock()
    println("Main thread: notify")
    condition.notifyAll()
    mtx.unlock()

    // wait for the new thread finished.
    fut.get()
    return 0
}
```

输出结果应为：

```text
New thread: before wait
Main thread: set flag
Main thread: notify
New thread: after wait
```

`Condition` 对象执行 `wait` 时，必须在锁的保护下进行，否则 `wait` 中释放锁的操作会抛出异常。

以下是使用条件变量的一些错误示例：

<!-- run.error -->

```cangjie
import std.sync.Mutex

let m1 = Mutex()
let c1 = synchronized(m1) {
    m1.condition()
}
let m2 = Mutex()
var flag: Bool = true
var count: Int64 = 0

func foo1() {
    spawn {
        m2.lock()
        while (flag) {
            c1.wait() // Error：The lock used together with the condition variable must be the same lock and in the locked state. Otherwise, the unlock operation in `wait` throws an exception.
        }
        count = count + 1
        m2.unlock()
    }
    m1.lock()
    flag = false
    c1.notifyAll()
    m1.unlock()
}

func foo2() {
    spawn {
        while (flag) {
            c1.wait() // Error：The `wait` of a conditional variable must be called with a lock held.
        }
        count = count + 1
    }
    m1.lock()
    flag = false
    c1.notifyAll()
    m1.unlock()
}

main() {
    foo1()
    foo2()
    c1.wait()
}
```

有时在复杂的线程间同步的场景下需要对同一个锁对象生成多个 `Condition` 实例，以下示例实现了一个长度固定的有界 `FIFO` 队列。当队列为空，`get()` 会被阻塞；当队列已满，`put()` 会被阻塞。

<!-- compile -->

```cangjie
import std.sync.{Mutex, Condition}