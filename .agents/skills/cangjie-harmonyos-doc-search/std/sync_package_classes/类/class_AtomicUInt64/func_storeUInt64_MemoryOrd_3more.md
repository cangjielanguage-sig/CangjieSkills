### func store(UInt64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: UInt64, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(UInt64)](#func-storeuint64) 替代。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(UInt64)

```cangjie
public func swap(val: UInt64): UInt64
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入原子类型的值。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入前的值。

### func swap(UInt64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: UInt64, memoryOrder!: MemoryOrder): UInt64
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(UInt64)](#func-swapuint64) 替代。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入前的值。