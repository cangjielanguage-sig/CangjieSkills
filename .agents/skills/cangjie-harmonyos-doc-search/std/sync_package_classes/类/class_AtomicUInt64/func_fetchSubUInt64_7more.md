### func fetchSub(UInt64)

```cangjie
public func fetchSub(val: UInt64): UInt64
```

功能：采用默认内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与原子类型进行减操作的值。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 执行减操作前的值。

### func fetchSub(UInt64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchSub(val: UInt64, memoryOrder!: MemoryOrder): UInt64
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，以原子类型的值为被减数，参数 `val` 为减数，做减操作。将结果写入当前原子类型实例，并返回减操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchSub(UInt64)](#func-fetchsubuint64) 替代。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与原子类型进行减操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 执行减操作前的值。

### func fetchXor(UInt64)

```cangjie
public func fetchXor(val: UInt64): UInt64
```

功能：采用默认内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与原子类型进行异或操作的值。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 执行异或操作前的值。

### func fetchXor(UInt64, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func fetchXor(val: UInt64, memoryOrder!: MemoryOrder): UInt64
```

功能：采用参数 `memoryOrder` 指定的内存排序方式，将当前原子类型实例的值与参数 `val` 进行异或操作。将结果写入当前原子类型实例，并返回异或操作前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [fetchXor(UInt64)](#func-fetchxoruint64) 替代。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与原子类型进行异或操作的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 执行异或操作前的值。

### func load()

```cangjie
public func load(): UInt64
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 当前原子类型的值。

### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): UInt64
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load-9) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 当前原子类型的值。

### func store(UInt64)

```cangjie
public func store(val: UInt64): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 写入原子类型的值。