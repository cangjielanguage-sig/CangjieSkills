### func fetchSub(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchSub(val: Int16, memoryOrder!: MemoryOrder): Int16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchSub(Int16)](#func-fetchsubint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行减操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行减操作前的值。

### func fetchXor(Int16)

```cangjie
public func fetchXor(val: Int16): Int16
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行异或操作的值。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行异或操作前的值。

### func fetchXor(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchXor(val: Int16, memoryOrder!: MemoryOrder): Int16
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchXor(Int16)](#func-fetchxorint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 与原子类型进行异或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 执行异或操作前的值。

### func load()

```cangjie
public func load(): Int16
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 当前原子类型的值。

### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): Int16
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load-1) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 当前原子类型的值。

### func store(Int16)

```cangjie
public func store(val: Int16): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 写入原子类型的值。

### func store(Int16, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: Int16, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(Int16)](#func-storeint16) 替代。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。