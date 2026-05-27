## class AtomicOptionReference\<T> where T <: Object

```cangjie
public class AtomicOptionReference<T> where T <: Object {
    public init()
    public init(val: Option<T>)
}
```

功能：提供引用类型原子操作相关函数。

该引用类型必须是 [Object](../../core/core_package_api/core_package_classes.md#class-object) 的子类。

### init()

```cangjie
public init()
```

功能：构造一个空的 [AtomicOptionReference](sync_package_classes.md#class-atomicoptionreferencet-where-t--object) 实例。

### init(Option\<T>)

```cangjie
public init(val: Option<T>)
```

功能：构造一个封装 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> 数据类型的原子类型 [AtomicOptionReference](sync_package_classes.md#class-atomicoptionreferencet-where-t--object) 的实例，其内部数据初始值为入参 `val` 的值。

参数：

- val: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 原子类型的初始值。

### func compareAndSwap(Option\<T>, Option\<T>)

```cangjie
public func compareAndSwap(old: Option<T>, new: Option<T>): Bool
```

功能：CAS 操作，采用默认内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，则写入参数 `new` 指定的值，并返回 `true`；否则，不写入值，并返回 `false`。

参数：

- old: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 与当前原子类型进行比较的值。
- new: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 比较结果相等时，写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func compareAndSwap(Option\<T>, Option\<T>, MemoryOrder, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func compareAndSwap(old: Option<T>, new: Option<T>, successOrder!: MemoryOrder, failureOrder!: MemoryOrder): Bool
```

功能：CAS 操作，成功时使用 `successOrder` 指定的内存排序方式，失败时则使用 `failureOrder` 指定的内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，写入参数 `new` 指定的值，返回 `true`；否则，不写入值，并返回 `false`。

> **注意：**
>
> 未来版本即将废弃，使用 [compareAndSwap(Option\<T>, Option\<T>)](#func-compareandswapoptiont-optiont) 替代。

参数：

- old: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 与当前原子类型进行比较的值。
- new: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 比较结果相等时，写入原子类型的值。
- successOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作成功时，执行“读 > 修改 > 写”操作需要的内存排序方式。
- failureOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作失败时，执行“读”操作需要的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func load()

```cangjie
public func load(): Option<T>
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 当前原子类型的值。