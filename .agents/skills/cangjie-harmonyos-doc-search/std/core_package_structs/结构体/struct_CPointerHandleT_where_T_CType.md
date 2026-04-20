## struct CPointerHandle\<T> where T <: CType

```cangjie
public struct CPointerHandle<T> where T <: CType {
    public let array: Array<T>
    public let pointer: CPointer<T>
    public init()
    public init(ptr: CPointer<T>, arr: Array<T>)
}
```

功能：表示 [Array](core_package_structs.md#struct-arrayt) 数组的原始指针，该类型中的泛型参数应该满足 [CType](core_package_interfaces.md#interface-ctype) 约束。

### let array

```cangjie
public let array: Array<T>
```

功能：原始指针对应的 [Array](core_package_structs.md#struct-arrayt) 数组实例。

类型：[Array](core_package_structs.md#struct-arrayt)\<T>

### let pointer

```cangjie
public let pointer: CPointer<T>
```

功能：获取指定 [Array](core_package_structs.md#struct-arrayt) 数组对应的原始指针。

类型：[CPointer](core_package_intrinsics.md#cpointert)\<T>

### init() <sup>(deprecated)</sup>

```cangjie
public init()
```

功能：构造一个默认 [CPointerHandle](core_package_structs.md#struct-cpointerhandlet-where-t--ctype) 实例，其中原始指针为空指针，仓颉数组为空数组。

> **注意：**
>
> 未来版本即将废弃不再使用，可使用 [acquireArrayRawData](./core_package_funcs.md#func-acquirearrayrawdatatarrayt-where-t--ctype) 函数构造 CPointerHandle 实例。

### init(CPointer\<T>, Array\<T>) <sup>(deprecated)</sup>

```cangjie
public init(ptr: CPointer<T>, arr: Array<T>)
```

功能：通过传入的 [CPointer](core_package_intrinsics.md#cpointert) 和 [Array](core_package_structs.md#struct-arrayt) 初始化一个 [CPointerHandle](core_package_structs.md#struct-cpointerhandlet-where-t--ctype)。

参数：

- ptr: [CPointer](core_package_intrinsics.md#cpointert)\<T> - 数组原始指针。
- arr: [Array](core_package_structs.md#struct-arrayt)\<T> - 指针对应的仓颉数组。

> **注意：**
>
> 未来版本即将废弃不再使用，可使用 [acquireArrayRawData](./core_package_funcs.md#func-acquirearrayrawdatatarrayt-where-t--ctype) 函数构造 CPointerHandle 实例。