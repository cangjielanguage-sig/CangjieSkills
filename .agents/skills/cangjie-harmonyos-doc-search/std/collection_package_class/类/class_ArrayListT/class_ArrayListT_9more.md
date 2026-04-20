## class ArrayList\<T>

```cangjie
public class ArrayList<T> <: List<T> {
    public init()
    public init(capacity: Int64)
    public init(size: Int64, initElement: (Int64) -> T)
    public init(elements: Collection<T>)
}
```

功能：提供可变长度的数组的功能。

[ArrayList](collection_package_class.md#class-arraylistt) 是一种线性的动态数组，与 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 不同，它可以根据需要自动调整大小，并且在创建时不需要指定大小。

> **说明：**
>
> - 当向动态数组中添加元素时，如果数组已满，则会重新分配更大的内存空间，并将原有的元素复制到新的内存空间中。
>
> - 动态数组的优点是可以节省内存空间，并且可以根据需要自动调整大小，因此非常适合需要频繁添加或删除元素的情况。但是，动态数组的缺点是在重新分配内存空间时可能会导致性能下降，因此在使用动态数组时需要考虑这一点。

父类型：

- [List](./collection_package_interface.md#interface-listt)\<T>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 的容量大小。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop first

```cangjie
public prop first: ?T
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 中的第一个元素，如果没有则返回 None。

类型：?T

### prop last

```cangjie
public prop last: ?T
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 中的最后一个元素，如果没有则返回 None。

类型：?T

### prop size

```cangjie
public prop size: Int64
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 中的元素个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个初始容量大小为默认值`16`的 [ArrayList](collection_package_class.md#class-arraylistt)。

### init(Collection\<T>)

```cangjie
public init(elements: Collection<T>)
```

功能：构造一个包含指定集合中所有元素的 [ArrayList](collection_package_class.md#class-arraylistt)。这些元素按照集合的迭代器返回的顺序排列。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 传入集合。

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个初始容量为指定大小的 [ArrayList](collection_package_class.md#class-arraylistt)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的初始容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果参数的大小小于 0 则抛出异常。

### init(Int64, (Int64) -> T)

```cangjie
public init(size: Int64, initElement: (Int64) -> T)
```

功能：构造具有指定初始元素个数和指定规则函数的 [ArrayList](collection_package_class.md#class-arraylistt)。该构造函数根据参数 size 设置 [ArrayList](collection_package_class.md#class-arraylistt) 的容量。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化函数元素个数。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) ->T - 传入初始化函数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0 则抛出异常。