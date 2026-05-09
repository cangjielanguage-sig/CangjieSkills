### func store(UInt16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: UInt16, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(UInt16)](#func-storeuint16) 替代。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(UInt16)

```cangjie
public func swap(val: UInt16): UInt16
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 写入原子类型的值。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 写入前的值。

### func swap(UInt16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: UInt16, memoryOrder!: MemoryOrder): UInt16
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(UInt16)](#func-swapuint16) 替代。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 写入前的值。