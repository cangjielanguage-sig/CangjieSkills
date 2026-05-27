### func store(UInt32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: UInt32, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(UInt32)](#func-storeuint32) 替代。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(UInt32)

```cangjie
public func swap(val: UInt32): UInt32
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 写入原子类型的值。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 写入前的值。

### func swap(UInt32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: UInt32, memoryOrder!: MemoryOrder): UInt32
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(UInt32)](#func-swapuint32) 替代。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 写入前的值。