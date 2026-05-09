## 原子操作 Atomic

仓颉提供整数类型、`Bool` 类型和引用类型的原子操作。

其中整数类型包括： `Int8`、`Int16`、`Int32`、`Int64`、`UInt8`、`UInt16`、`UInt32`、`UInt64`。

整数类型的原子操作支持基本的读写、交换以及算术运算操作：

| 操作             | 功能                                              |
| ---------------- | ------------------------------------------------- |
| `load`           | 读取                                              |
| `store`          | 写入                                              |
| `swap`           | 交换，返回交换前的值                               |
| `compareAndSwap` | 比较再交换，交换成功返回 `true`，否则返回 `false` |
| `fetchAdd`       | 加法，返回执行加操作之前的值                      |
| `fetchSub`       | 减法，返回执行减操作之前的值                      |
| `fetchAnd`       | 与，返回执行与操作之前的值                        |
| `fetchOr`        | 或，返回执行或操作之前的值                        |
| `fetchXor`       | 异或，返回执行异或操作之前的值                    |

需要注意的是：

1. 交换操作和算术操作的返回值是修改前的值。
2. compareAndSwap 是判断当前原子变量的值是否等于 old 值，如果等于，则使用 new 值替换；否则不替换。

以 `Int8` 类型为例，对应的原子操作类型声明如下：

```cangjie
class AtomicInt8 {
    public func load(): Int8
    public func store(val: Int8): Unit
    public func swap(val: Int8): Int8
    public func compareAndSwap(old: Int8, new: Int8): Bool
    public func fetchAdd(val: Int8): Int8
    public func fetchSub(val: Int8): Int8
    public func fetchAnd(val: Int8): Int8
    public func fetchOr(val: Int8): Int8
    public func fetchXor(val: Int8): Int8
}
```

上述每一种原子类型的方法都有一个对应的方法可以接收内存排序参数，目前内存排序参数仅支持顺序一致性。

类似的，其他整数类型对应的原子操作类型有：

```cangjie
class AtomicInt16 {...}
class AtomicInt32 {...}
class AtomicInt64 {...}
class AtomicUInt8 {...}
class AtomicUInt16 {...}
class AtomicUInt32 {...}
class AtomicUInt64 {...}
```

下方示例演示了如何在多线程程序中，使用原子操作实现计数：

<!-- verify -->

```cangjie
import std.sync.AtomicInt64
import std.collection.ArrayList

let count = AtomicInt64(0)

main(): Int64 {
    let list = ArrayList<Future<Int64>>()

    // create 1000 threads.
    for (_ in 0..1000) {
        let fut = spawn {
            sleep(Duration.millisecond) // sleep for 1ms.
            count.fetchAdd(1)
        }
        list.add(fut)
    }

    // Wait for all threads finished.
    for (f in list) {
        f.get()
    }

    let val = count.load()
    println("count = ${val}")
    return 0
}
```

输出结果应为：

```text
count = 1000
```

以下是使用整数类型原子操作的一些其他正确示例：

<!-- compile -->

```cangjie
var obj: AtomicInt32 = AtomicInt32(1)
var x = obj.load() // x: 1, the type is Int32
x = obj.swap(2) // x: 1
x = obj.load() // x: 2
var y = obj.compareAndSwap(2, 3) // y: true, the type is Bool.
y = obj.compareAndSwap(2, 3) // y: false, the value in obj is no longer 2 but 3. Therefore, the CAS operation fails.
x = obj.fetchAdd(1) // x: 3
x = obj.load() // x: 4
```

`Bool` 类型和引用类型的原子操作只提供读写和交换操作：

| 操作             | 功能                                              |
| ---------------- | ------------------------------------------------- |
| `load`           | 读取                                              |
| `store`          | 写入                                              |
| `swap`           | 交换，返回交换前的值                              |
| `compareAndSwap` | 比较再交换，交换成功返回 `true`，否则返回 `false` |

> **注意：**
>
> 引用类型原子操作只对引用类型有效。

原子引用类型是 `AtomicReference`，以下是使用 `Bool` 类型、引用类型原子操作的一些正确示例：

<!-- verify -->

```cangjie
import std.sync.{AtomicBool, AtomicReference}

class A {}

main() {
    var obj = AtomicBool(true)
    var x1 = obj.load() // x1: true, the type is Bool
    println(x1)
    var t1 = A()
    var obj2 = AtomicReference(t1)
    var x2 = obj2.load() // x2 and t1 are the same object
    var y1 = obj2.compareAndSwap(x2, t1) // x2 and t1 are the same object, y1: true
    println(y1)
    var t2 = A()
    var y2 = obj2.compareAndSwap(t2, A()) // x and t1 are not the same object, CAS fails, y2: false
    println(y2)
    y2 = obj2.compareAndSwap(t1, A()) // CAS successes, y2: true
    println(y2)
}
```

编译执行上述代码，输出结果为：

```text
true
true
false
true
```