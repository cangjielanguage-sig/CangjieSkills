### func fetchAdd(UInt32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: UInt32, memoryOrder!: MemoryOrder): UInt32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(UInt32)](#func-fetchadduint32) 替代。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 执行加操作前的值。

### func fetchAnd(UInt32)

```cangjie
public func fetchAnd(val: UInt32): UInt32
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 与原子类型进行与操作的值。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 执行与操作前的值。

### func fetchAnd(UInt32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: UInt32, memoryOrder!: MemoryOrder): UInt32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(UInt32)](#func-fetchanduint32) 替代。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 执行与操作前的值。

### func fetchOr(UInt32)

```cangjie
public func fetchOr(val: UInt32): UInt32
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 与原子类型进行或操作的值。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 执行或操作前的值。

### func fetchOr(UInt32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: UInt32, memoryOrder!: MemoryOrder): UInt32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(UInt32)](#func-fetchoruint32) 替代。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 执行或操作前的值。