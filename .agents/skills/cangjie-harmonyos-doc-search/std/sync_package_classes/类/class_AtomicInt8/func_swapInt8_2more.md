### func swap(Int8)

```cangjie
public func swap(val: Int8): Int8
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 写入原子类型的值。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 写入前的值。

### func swap(Int8, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: Int8, memoryOrder!: MemoryOrder): Int8
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(Int8)](#func-swapint8) 替代。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 写入前的值。