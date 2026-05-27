### init(Int64, (Int64) -> (K, V))

```cangjie
public init(size: Int64, initElement: (Int64) -> (K, V))
```

功能：通过传入的元素个数 size 和函数规则来构造 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的元素个数。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) -> (K, V) - 初始化该 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的函数规则。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0 则抛出异常。

### func add(Collection\<(K, V)>)

```cangjie
public func add(all!: Collection<(K, V)>): Unit
```

功能：将新的键值对集合放入 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中。对于 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中已有的键，该键的值将被新值替换。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 需要添加进 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的键值对集合。

### func add(K, V)

```cangjie
public func add(key: K, value: V): Option<V>
```

功能：将新的键值对放入 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中。对于 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中已有的键，该键的值将被新值替换。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V> - 如果赋值之前 key 存在，旧的 value 用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装并返回；否则，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V>.None。

### func backward(K, Bool)

```cangjie
public func backward(mark: K, inclusive!: Bool = true): Iterator<(K, V)>
```

功能：获取从第一个键小于等于 mark 的节点按降序遍历到 [first](./collection_package_class.md#prop-first-3) 的迭代器。如果该节点的键等于 mark ，那么根据 `inclusive!` 确定是否包含该键对应的节点。

参数：

- mark: K - 用于确定从哪里开始的键。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 `mark` 是迭代器的首个元素的 key 时，指定是否包含 mark 作为起始点，默认为 `true`。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)> - 对应元素的迭代器。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清除所有键值对。

### func clone()

```cangjie
public func clone(): TreeMap<K, V>
```

功能：克隆 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)。

返回值：

- [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> - 返回一个 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 实例。

### func contains(Collection\<K>)

```cangjie
public func contains(all!: Collection<K>): Bool
```

功能：判断是否包含指定集合键的映射。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 键的集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在，则返回 true；否则，返回 false。