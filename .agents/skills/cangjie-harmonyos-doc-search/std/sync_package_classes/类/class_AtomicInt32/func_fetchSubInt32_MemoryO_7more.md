### func fetchSub(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchSub(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchSub(Int32)](#func-fetchsubint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行减操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行减操作前的值。

### func fetchXor(Int32)

```cangjie
public func fetchXor(val: Int32): Int32
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行异或操作的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行异或操作前的值。

### func fetchXor(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchXor(val: Int32, memoryOrder!: MemoryOrder): Int32
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchXor(Int32)](#func-fetchxorint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 与原子类型进行异或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行异或操作前的值。

### func load()

```cangjie
public func load(): Int32
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 当前原子类型的值。

### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): Int32
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load-2) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 当前原子类型的值。

### func store(Int32)

```cangjie
public func store(val: Int32): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入原子类型的值。

### func store(Int32, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: Int32, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(Int32)](#func-storeint32) 替代。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。