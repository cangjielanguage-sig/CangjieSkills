## class AtomicBool

```cangjie
public class AtomicBool {
    public init(val: Bool)
}
```

功能：提供 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的原子操作相关函数。

### init(Bool)

```cangjie
public init(val: Bool)
```

功能：构造一个封装 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 数据类型的原子类型 [AtomicBool](sync_package_classes.md#class-atomicbool) 的实例，其内部数据初始值为入参 `val` 的值。

参数：

- val: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 原子类型的初始值。

### func compareAndSwap(Bool, Bool)

```cangjie
public func compareAndSwap(old: Bool, new: Bool): Bool
```

功能：CAS（Compare and Swap）操作，采用[默认内存排序方式](sync_package_constants_vars.md#let-defaultmemoryorder-deprecated)。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，则写入参数 `new` 指定的值，并返回 `true`；否则，不写入值，并返回 `false`。

参数：

- old: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 与当前原子类型进行比较的值。
- new: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较结果相等时，写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func compareAndSwap(Bool, Bool, MemoryOrder, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func compareAndSwap(old: Bool, new: Bool, successOrder!: MemoryOrder, failureOrder!: MemoryOrder): Bool
```

功能：CAS 操作，成功时使用 `successOrder` 指定的内存排序方式，失败时则使用 `failureOrder` 指定的内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，写入参数 `new` 指定的值，返回 `true`；否则，不写入值，并返回 `false`。

> **注意：**
>
> 未来版本即将废弃，使用 [compareAndSwap(Bool, Bool)](#func-compareandswapbool-bool) 替代。

参数：

- old: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 与当前原子类型进行比较的值。
- new: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较结果相等时，写入原子类型的值。
- successOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作成功时，执行“读 > 修改 > 写”操作需要的内存排序方式。
- failureOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作失败时，执行“读”操作需要的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func load()

```cangjie
public func load(): Bool
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前原子类型的值。

### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): Bool
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前原子类型的值。

### func store(Bool)

```cangjie
public func store(val: Bool): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 写入原子类型的值。