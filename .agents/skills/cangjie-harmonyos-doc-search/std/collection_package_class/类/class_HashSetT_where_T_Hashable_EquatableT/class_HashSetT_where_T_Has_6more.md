## class HashSet\<T> where T <: Hashable & Equatable\<T>

```cangjie
public class HashSet<T> <: Set<T> where T <: Hashable & Equatable<T> {
    public init()
    public init(elements: Collection<T>)
    public init(elements: Array<T>)
    public init(capacity: Int64)
    public init(size: Int64, initElement: (Int64) -> T)
}
```

功能：基于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 实现的 [Set](collection_package_interface.md#interface-sett) 接口的实例。

[HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中的元素是无序的，不允许有重复元素。当我们向 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中添加元素时，[HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 会根据元素的哈希值来确定该元素在哈希表中的位置。

> **提示：**
>
> [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 是基于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 实现的，因此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的容量、内存布局、时间性能等都和 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 相同。

父类型：

- [Set](collection_package_interface.md#interface-sett)\<T>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：返回此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的内部数组容量大小。

> **注意：**
>
> 容量大小不一定等于 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的 size。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：返回此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的元素个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)，初始容量为 16。

### init(Array\<T>)

```cangjie
public init(elements: Array<T>)
```

功能：使用传入的数组构造 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。该构造函数根据传入数组 elements 的 size 设置 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的容量。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 初始化 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的数组。

### init(Collection\<T>)

```cangjie
public init(elements: Collection<T>)
```

功能：使用传入的集合构造 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。该构造函数根据传入集合 elements 的 size 设置 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的容量。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 初始化 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的集合。