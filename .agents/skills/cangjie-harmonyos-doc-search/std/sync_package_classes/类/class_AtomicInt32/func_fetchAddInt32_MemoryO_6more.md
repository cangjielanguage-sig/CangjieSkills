### func fetchAdd(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(Int32)](#func-fetchaddint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行加操作前的值。

### func fetchAnd(Int32)

```cangjie
public func fetchAnd(val: Int32): Int32
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行与操作的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行与操作前的值。

### func fetchAnd(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(Int32)](#func-fetchandint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行与操作前的值。

### func fetchOr(Int32)

```cangjie
public func fetchOr(val: Int32): Int32
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行或操作的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行或操作前的值。

### func fetchOr(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(Int32)](#func-fetchorint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行或操作前的值。

### func fetchSub(Int32)

```cangjie
public func fetchSub(val: Int32): Int32
```

功能：采用默认内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行减操作的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行减操作前的值。