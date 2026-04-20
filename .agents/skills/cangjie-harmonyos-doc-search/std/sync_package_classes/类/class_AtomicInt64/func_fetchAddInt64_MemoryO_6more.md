### func fetchAdd(Int64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: Int64, memoryOrder!: MemoryOrder): Int64
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(Int64)](#func-fetchaddint64) 替代。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行加操作前的值。

### func fetchAnd(Int64)

```cangjie
public func fetchAnd(val: Int64): Int64
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行与操作的值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行与操作前的值。

### func fetchAnd(Int64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: Int64, memoryOrder!: MemoryOrder): Int64
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(Int64)](#func-fetchandint64) 替代。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行与操作前的值。

### func fetchOr(Int64)

```cangjie
public func fetchOr(val: Int64): Int64
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行或操作的值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行或操作前的值。

### func fetchOr(Int64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: Int64, memoryOrder!: MemoryOrder): Int64
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(Int64)](#func-fetchorint64) 替代。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行或操作前的值。

### func fetchSub(Int64)

```cangjie
public func fetchSub(val: Int64): Int64
```

功能：采用默认内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 与原子类型进行减操作的值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行减操作前的值。