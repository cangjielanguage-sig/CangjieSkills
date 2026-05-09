### func contains(K)

```cangjie
public func contains(key: K): Bool
```

功能：判断是否包含指定键的映射。

参数：

- key: K - 传递要判断的 key。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在，则返回 true；否则，返回 false。

### func entryView(K)

```cangjie
public func entryView(k: K): MapEntryView<K, V>
```

功能：如果不包含特定键，返回一个空的引用视图。如果包含特定键，则返回该键对应的元素的引用视图。

参数：

- k: K - 要添加的键值对的键。

返回值：

- [MapEntryView](./collection_package_interface.md#interface-mapentryviewk-v)\<K, V> - 一个引用视图。

### func forward(K, Bool)

```cangjie
public func forward(mark: K, inclusive!: Bool = true): Iterator<(K, V)>
```

功能：获取从第一个键大于等于 mark 的节点按升序遍历到 [last](./collection_package_class.md#prop-last-3) 结束的一个迭代器。如果该节点的键等于 mark ，那么根据 `inclusive!` 确定是否包含该键对应的节点。

参数：

- mark: K - 用于确定从哪里开始的键。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 `mark` 是迭代器的首个元素的 key 时，指定是否包含 mark 作为起始点，默认为 `true`。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)> - 对应元素的迭代器。

### func get(K)

```cangjie
public func get(key: K): ?V
```

功能：返回指定键映射的值。

参数：

- key: K - 指定的键。

返回值：

- ?V - 如果存在这样一个值，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该值并返回；否则，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V>.None。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<(K, V)>
```

功能：返回 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的迭代器，迭代器按 Key 值从小到大的顺序迭代。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)> - [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的迭代器。

### func keys()

```cangjie
public func keys(): EquatableCollection<K>
```

功能：返回 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中所有的 key，并将所有 key 存储在一个容器中。

返回值：

- [EquatableCollection](collection_package_interface.md#interface-equatablecollectiont)\<K> - 包含所有键的集合。

### func remove(Collection\<K>)

```cangjie
public func remove(all!: Collection<K>): Unit
```

功能：从此映射中删除指定集合的映射（如果存在）。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 传入要删除的键的集合。

### func remove(K)

```cangjie
public func remove(key: K): Option<V>
```

功能：从此映射中删除指定键的映射（如果存在）。

参数：

- key: K - 传入要删除的 key。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V> - 被移除映射的值用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装，如果 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中不存在指定的键，返回 None。