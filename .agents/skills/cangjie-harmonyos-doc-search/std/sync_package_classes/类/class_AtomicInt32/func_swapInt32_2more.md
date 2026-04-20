### func swap(Int32)

```cangjie
public func swap(val: Int32): Int32
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入原子类型的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入前的值。

### func swap(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(Int32)](#func-swapint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入前的值。