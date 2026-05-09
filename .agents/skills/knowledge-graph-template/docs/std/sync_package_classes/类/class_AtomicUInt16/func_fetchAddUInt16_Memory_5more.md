### func fetchAdd(UInt16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: UInt16, memoryOrder!: MemoryOrder): UInt16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(UInt16)](#func-fetchadduint16) 替代。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 执行加操作前的值。

### func fetchAnd(UInt16)

```cangjie
public func fetchAnd(val: UInt16): UInt16
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 与原子类型进行与操作的值。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 执行与操作前的值。

### func fetchAnd(UInt16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: UInt16, memoryOrder!: MemoryOrder): UInt16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(UInt16)](#func-fetchanduint16) 替代。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 执行与操作前的值。

### func fetchOr(UInt16)

```cangjie
public func fetchOr(val: UInt16): UInt16
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 与原子类型进行或操作的值。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 执行或操作前的值。

### func fetchOr(UInt16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: UInt16, memoryOrder!: MemoryOrder): UInt16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(UInt16)](#func-fetchoruint16) 替代。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 执行或操作前的值。