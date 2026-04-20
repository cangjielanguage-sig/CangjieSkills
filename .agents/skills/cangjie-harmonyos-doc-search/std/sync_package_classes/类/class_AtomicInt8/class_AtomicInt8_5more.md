## class AtomicInt8

```cangjie
public class AtomicInt8 {
    public init(val: Int8)
}
```

功能：提供 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的原子操作相关函数。

### init(Int8)

```cangjie
public init(val: Int8)
```

功能：构造一个封装 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 数据类型的原子类型 [AtomicInt8](sync_package_classes.md#class-atomicint8) 的实例，其内部数据初始值为入参 `val` 的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 原子类型的初始值。

### func compareAndSwap(Int8, Int8)

```cangjie
public func compareAndSwap(old: Int8, new: Int8): Bool
```

功能：CAS 操作，采用默认内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，则写入参数 `new` 指定的值，并返回 `true`；否则，不写入值，并返回 `false`。

参数：

- old: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与当前原子类型进行比较的值。
- new: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 比较结果相等时，写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func compareAndSwap(Int8, Int8, MemoryOrder, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func compareAndSwap(old: Int8, new: Int8, successOrder!: MemoryOrder, failureOrder!: MemoryOrder): Bool
```

功能：CAS 操作，成功时使用 `successOrder` 指定的内存排序方式，失败时则使用 `failureOrder` 指定的内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，写入参数 `new` 指定的值，返回 `true`；否则，不写入值，并返回 `false`。

> **注意：**
>
> 未来版本即将废弃，使用 [compareAndSwap(Int8, Int8)](#func-compareandswapint8-int8) 替代。

参数：

- old: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与当前原子类型进行比较的值。
- new: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 比较结果相等时，写入原子类型的值。
- successOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作成功时，执行“读 > 修改 > 写”操作需要的内存排序方式。
- failureOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作失败时，执行“读”操作需要的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func fetchAdd(Int8)

```cangjie
public func fetchAdd(val: Int8): Int8
```

功能：采用默认内存排序方式，将原子类型的值与参数 `val` 进行加操作，将结果写入当前原子类型实例，并返回加操作前的值。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 与原子类型进行加操作的值。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 执行加操作前的值。