### func swap(T, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: T, memoryOrder!: MemoryOrder): T
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(T)](#func-swapt) 替代。

参数：

- val: T - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- T - 写入前的值。