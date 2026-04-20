## class TreeMap\<K, V> where K <: Comparable\<K>

```cangjie
public class TreeMap<K, V> <: OrderedMap<K, V> where K <: Comparable<K> {
    public init()
    public init(elements: Collection<(K, V)>)
    public init(elements: Array<(K,V)>)
    public init(size: Int64, initElement: (Int64) -> (K, V))
}
```

功能：基于平衡二叉搜索树实现的 [OrderedMap](collection_package_interface.md#interface-orderedmapk-v) 接口实例。

这个类的主要目的是提供一个有序的 key-value 存储结构，它可以快速地插入、删除、查找元素。

[TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 可以用于任何需要有序键值对存储的场景，例如数据库、缓存、查找表等。

父类型：

- [OrderedMap](collection_package_interface.md#interface-orderedmapk-v)\<K, V>

### prop first

```cangjie
public prop first: ?(K, V)
```

功能：获取 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的第一个元素。如果存在第一个元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)>.None。

类型：?(K, V)

### prop last

```cangjie
public prop last: ?(K, V)
```

功能：获取 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的最后一个元素。如果存在最后一个元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)>.None。

返回值：

类型：?(K, V)

### prop size

```cangjie
public prop size: Int64
```

功能：返回键值的个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)。

### init(Array\<(K,V)>)

```cangjie
public init(elements: Array<(K,V)>)
```

功能：通过传入的键值对数组构造一个 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)。

按照 elements 的先后顺序将元素插入到 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 内，由于 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中不允许出现相同的键，如果 elements 中有相同的键时，后出现的键值对将会覆盖先出现的键值对。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<(K, V)> - 初始化该 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的键值对数组。

### init(Collection\<(K, V)>)

```cangjie
public init(elements: Collection<(K, V)>)
```

功能：通过传入的键值对集合构造一个 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)。

按照 elements 的迭代器顺序将元素插入到 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 内，由于 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中不允许出现相同的键，如果 elements 中有相同的键时，后出现（迭代器顺序）的键值对将会覆盖先出现的键值对。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 初始化该 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的键值对集合。