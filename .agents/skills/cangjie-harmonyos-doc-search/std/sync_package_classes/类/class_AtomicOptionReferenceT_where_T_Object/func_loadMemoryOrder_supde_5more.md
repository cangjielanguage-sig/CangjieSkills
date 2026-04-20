### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): Option<T>
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load-5) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 当前原子类型的值。

### func store(Option\<T>)

```cangjie
public func store(val: Option<T>): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入原子类型的值。

### func store(Option\<T>, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: Option<T>, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(Option\<T>)](#func-storeoptiont) 替代。

参数：

- val: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(Option\<T>)

```cangjie
public func swap(val: Option<T>): Option<T>
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入原子类型的值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入前的值。

### func swap(Option\<T>, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func swap(val: Option<T>, memoryOrder!: MemoryOrder): Option<T>
```

功能：交换操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

> **注意：**
>
> 未来版本即将废弃，使用 [swap(Option\<T>)](#func-swapoptiont) 替代。

参数：

- val: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 写入前的值。