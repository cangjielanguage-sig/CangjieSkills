## class HashMap\<K, V> where K <: Hashable & Equatable\<K>

```cangjie
public class HashMap<K, V> <: Map<K, V> where K <: Hashable & Equatable<K> {
    public init()
    public init(elements: Array<(K, V)>)
    public init(elements: Collection<(K, V)>)
    public init(capacity: Int64)
    public init(size: Int64, initElement: (Int64) -> (K, V))
}
```

功能：[Map](collection_package_interface.md#interface-mapk-v) 接口的哈希表实现。

哈希表是一种常用的数据结构，它可以用来快速地查找、插入和删除数据。哈希表的基本原理是将数据映射到一个数组中，这个数组称为哈希表。每个数据元素都有一个对应的哈希值，这个哈希值可以用来确定该元素在哈希表中的位置。

哈希表的特点是快速的查找、插入和删除操作，时间复杂度通常是 O(1)。由于哈希表底层的数组大小是动态的，所以哈希表不能保证元素的顺序不可变。

父类型：

- [Map](collection_package_interface.md#interface-mapk-v)\<K, V>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：返回 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的容量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：返回键值对的个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个具有默认初始容量为 16 和默认负载因子为空的 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

### init(Array\<(K, V)>)

```cangjie
public init(elements: Array<(K, V)>)
```

功能：通过传入的键值对数组构造一个 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

该构造函数根据传入数组的 size 设置 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的容量。由于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 内部不允许键重复，当 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 中存在重复的键时，按照迭代器顺序，出现在后面的键值对将会覆盖前面的键值对。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<(K, V)> - 初始化该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的键值对数组。

### init(Collection\<(K, V)>)

```cangjie
public init(elements: Collection<(K, V)>)
```

功能：通过传入的键值对集合构造一个 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

该构造函数根据传入集合 elements 的 size 设置 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的容量。由于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 内部不允许键重复，当 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 中存在重复的键时，按照迭代器顺序，出现在后面的键值对将会覆盖前面的键值对。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 初始化该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的键值对集合。