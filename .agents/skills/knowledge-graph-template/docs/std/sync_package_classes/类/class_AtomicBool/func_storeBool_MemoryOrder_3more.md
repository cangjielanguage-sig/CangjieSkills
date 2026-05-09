### func store(Bool, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: Bool, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(Bool)](#func-storebool) 替代。

参数：

- val: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(Bool)

```cangjie
public func swap(val: Bool): Bool
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入前的值。

### func swap(Bool, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: Bool, memoryOrder!: MemoryOrder): Bool
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(Bool)](#func-swapbool) 替代。

参数：

- val: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入前的值。