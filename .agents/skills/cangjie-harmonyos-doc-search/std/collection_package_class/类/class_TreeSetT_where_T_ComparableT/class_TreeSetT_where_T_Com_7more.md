## class TreeSet\<T> where T <: Comparable\<T>

```cangjie
public class TreeSet<T> <: OrderedSet<T> where T <: Comparable<T> {
    public init()
    public init(elements: Collection<T>)
    public init(size: Int64, initElement: (Int64) -> T)
}
```

功能：基于 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 实现的 [Set](collection_package_interface.md#interface-sett) 接口的实例。

这个类的主要目的是提供一个有序的元素存储结构，它可以快速地插入、删除、查找元素。

[TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 可以用于任何需要有序元素存储的场景，例如数据库、缓存、查找表等。

父类型：

- [OrderedSet](collection_package_interface.md#interface-orderedsett)\<T>

### prop first

```cangjie
public prop first: ?T
```

功能：获取 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的第一个元素。

类型：?T - 如果存在第一个元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### prop last

```cangjie
public prop last: ?T
```

功能：获取 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的最后一个元素。

类型：?T - 如果存在最后一个元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### prop size

```cangjie
public prop size: Int64
```

功能：返回元素的个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

### init(Collection\<T>)

```cangjie
public init(elements: Collection<T>)
```

功能：通过传入的元素集合构造一个 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

按照 elements 的迭代器顺序将元素插入到 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 内，由于 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中不允许出现相同的元素，如果 elements 中有多个相同的元素时，[TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 只会保留一个元素。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 初始化该 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的元素集合。

### init(Int64, (Int64) -> T)

```cangjie
public init(size: Int64, initElement: (Int64) -> T)
```

功能：通过传入的元素个数 size 和函数规则来构造 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的元素个数。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) -> T - 初始化该 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的函数规则。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0 则抛出异常。