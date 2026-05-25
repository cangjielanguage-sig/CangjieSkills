## class AtomicUInt64

```cangjie
public class AtomicUInt64 {
    public init(val: UInt64)
}
```

功能：提供 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的原子操作相关函数。

### init(UInt64)

```cangjie
public init(val: UInt64)
```

功能：构造一个封装 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 数据类型的原子类型 [AtomicUInt64](sync_package_classes.md#class-atomicuint64) 的实例，其内部数据初始值为入参 `val` 的值。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 原子类型的初始值。

### func compareAndSwap(UInt64, UInt64)

```cangjie
public func compareAndSwap(old: UInt64, new: UInt64): Bool
```

功能：CAS 操作，采用默认内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，则写入参数 `new` 指定的值，并返回 `true`；否则，不写入值，并返回 `false`。

参数：

- old: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与当前原子类型进行比较的值。
- new: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 比较结果相等时，写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func compareAndSwap(UInt64, UInt64, MemoryOrder, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func compareAndSwap(old: UInt64, new: UInt64, successOrder!: MemoryOrder, failureOrder!: MemoryOrder): Bool
```

功能：CAS 操作，成功时使用 `successOrder` 指定的内存排序方式，失败时则使用 `failureOrder` 指定的内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，写入参数 `new` 指定的值，返回 `true`；否则，不写入值，并返回 `false`。

> **注意：**
>
> 未来版本即将废弃，使用 [compareAndSwap(UInt64, UInt64)](#func-compareandswapuint64-uint64) 替代。

参数：

- old: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与当前原子类型进行比较的值。
- new: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 比较结果相等时，写入原子类型的值。
- successOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作成功时，执行“读 > 修改 > 写”操作需要的内存排序方式。
- failureOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作失败时，执行“读”操作需要的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func fetchAdd(UInt64)

```cangjie
public func fetchAdd(val: UInt64): UInt64
```

功能：采用默认内存排序方式，将原子类型的值与参数 `val` 进行加操作，将结果写入当前原子类型实例，并返回加操作前的值。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 与原子类型进行加操作的值。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 执行加操作前的值。