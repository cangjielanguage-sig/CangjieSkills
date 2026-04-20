### func fetchAdd(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: Int16, memoryOrder!: MemoryOrder): Int16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(Int16)](#func-fetchaddint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行加操作前的值。

### func fetchAnd(Int16)

```cangjie
public func fetchAnd(val: Int16): Int16
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行与操作的值。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行与操作前的值。

### func fetchAnd(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: Int16, memoryOrder!: MemoryOrder): Int16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(Int16)](#func-fetchandint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行与操作前的值。

### func fetchOr(Int16)

```cangjie
public func fetchOr(val: Int16): Int16
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行或操作的值。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行或操作前的值。

### func fetchOr(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: Int16, memoryOrder!: MemoryOrder): Int16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(Int16)](#func-fetchorint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行或操作前的值。

### func fetchSub(Int16)

```cangjie
public func fetchSub(val: Int16): Int16
```

功能：采用默认内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行减操作的值。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行减操作前的值。