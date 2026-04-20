### func fetchAdd(Int8, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAdd(val: Int8, memoryOrder!: MemoryOrder): Int8
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将原子类型的值与参数 `val` 进行加操作。将结果写入当前原子类型实例，并返回加法运算前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAdd(Int8)](#func-fetchaddint8) 替代。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行加操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行加操作前的值。

### func fetchAnd(Int8)

```cangjie
public func fetchAnd(val: Int8): Int8
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行与操作的值。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行与操作前的值。

### func fetchAnd(Int8, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchAnd(val: Int8, memoryOrder!: MemoryOrder): Int8
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行与操作。将结果写入当前原子类型实例，并返回与操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchAnd(Int8)](#func-fetchandint8) 替代。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行与操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行与操作前的值。

### func fetchOr(Int8)

```cangjie
public func fetchOr(val: Int8): Int8
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行或操作的值。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行或操作前的值。

### func fetchOr(Int8, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchOr(val: Int8, memoryOrder!: MemoryOrder): Int8
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行或操作。将结果写入当前原子类型实例，并返回或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchOr(Int8)](#func-fetchorint8) 替代。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行或操作前的值。

### func fetchSub(Int8)

```cangjie
public func fetchSub(val: Int8): Int8
```

功能：采用默认内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行减操作的值。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行减操作前的值。