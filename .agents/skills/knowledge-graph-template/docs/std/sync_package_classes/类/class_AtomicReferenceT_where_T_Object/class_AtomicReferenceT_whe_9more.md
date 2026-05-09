## class AtomicReference\<T> where T <: Object

```cangjie
public class AtomicReference<T> where T <: Object {
    public init(val: T)
}
```

功能：引用类型原子操作相关函数。

该引用类型必须是 [Object](../../core/core_package_api/core_package_classes.md#class-object) 的子类。

### init(T)

```cangjie
public init(val: T)
```

功能：构造一个封装 `T` 数据类型的原子类型 [AtomicReference](sync_package_classes.md#class-atomicreferencet-where-t--object) 的实例，其内部数据初始值为入参 `val` 的值。

参数：

- val: T - 原子类型的初始值。

### func compareAndSwap(T, T)

```cangjie
public func compareAndSwap(old: T, new: T): Bool
```

功能：CAS 操作，采用默认内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，则写入参数 `new` 指定的值，并返回 `true`；否则，不写入值，并返回 `false`。

参数：

- old: T - 与当前原子类型进行比较的值。
- new: T - 比较结果相等时，写入原子类型的值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func compareAndSwap(T, T, MemoryOrder, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func compareAndSwap(old: T, new: T, successOrder!: MemoryOrder, failureOrder!: MemoryOrder): Bool
```

功能：CAS 操作，成功时使用 `successOrder` 指定的内存排序方式，失败时则使用 `failureOrder` 指定的内存排序方式。

比较当前原子类型的值与参数 `old` 指定的值是否相等。若相等，写入参数 `new` 指定的值，返回 `true`；否则，不写入值，并返回 `false`。

> **注意：**
>
> 未来版本即将废弃，使用 [compareAndSwap(T, T)](#func-compareandswapt-t) 替代。

参数：

- old: T - 与当前原子类型进行比较的值。
- new: T - 比较结果相等时，写入原子类型的值。
- successOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作成功时，执行“读 > 修改 > 写”操作需要的内存排序方式。
- failureOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - CAS 操作失败时，执行“读”操作需要的内存排序方式。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较后交换成功返回 `true`，否则返回 `false`。

### func load()

```cangjie
public func load(): T
```

功能：读取操作，采用默认内存排序方式，读取原子类型的值。

返回值：

- T - 当前原子类型的值。

### func load(MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func load(memoryOrder!: MemoryOrder): T
```

功能：读取操作，采用参数 `memoryOrder` 指定的内存排序方式，读取原子类型的值。

> **注意：**
>
> 未来版本即将废弃，使用 [load()](#func-load-6) 替代。

参数：

- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

返回值：

- T - 当前原子类型的值。

### func store(T)

```cangjie
public func store(val: T): Unit
```

功能：写入操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型。

参数：

- val: T - 写入原子类型的值。

### func store(T, MemoryOrder) <sup>(deprecated)</sup>

```cangjie
public func store(val: T, memoryOrder!: MemoryOrder): Unit
```

功能：写入操作，采用参数 `memoryOrder` 指定的内存排序方式，将参数 `val` 指定的值写入原子类型。

> **注意：**
>
> 未来版本即将废弃，使用 [store(T)](#func-storet) 替代。

参数：

- val: T - 写入原子类型的值。
- memoryOrder!: [MemoryOrder <sup>(deprecated)</sup>](sync_package_enums.md#enum-memoryorder-deprecated) - 当前操作的内存排序方式。

### func swap(T)

```cangjie
public func swap(val: T): T
```

功能：交换操作，采用默认内存排序方式，将参数 `val` 指定的值写入原子类型，并返回写入前的值。

参数：

- val: T - 写入原子类型的值。

返回值：

- T - 写入前的值。