### func swap(Int64)

```cangjie
public func swap(val: Int64): Int64
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入原子类型的值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入前的值。

### func swap(Int64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: Int64, memoryOrder!: MemoryOrder): Int64
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(Int64)](#func-swapint64) 替代。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 写入前的值。

示例：

<!-- verify -->
```cangjie
import std.sync.*

let count = AtomicInt64(1)

main(): Int64 {
    var val1 = 0
    if (count.compareAndSwap(1, 2)) {
        val1 = count.load()
        println("count1 = ${val1}")
    }

    if (count.fetchAdd(2) == val1) {
        var val2 = count.load()
        println("count2 = ${val2}")
    }

    count.store(6)
    var val3 = count.load()
    println("count3 = ${val3}")

    if (count.swap(8) == val3) {
        var val4 = count.load()
        println("count4 = ${val4}")
    }

    return 0
}
```

运行结果：

```text
count1 = 2
count2 = 4
count3 = 6
count4 = 8
```