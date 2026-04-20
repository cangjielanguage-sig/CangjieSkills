### func clone()

```cangjie
public func clone(): HashMap<K, V>
```

功能：克隆 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

返回值：

- [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> - 返回一个 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

### func contains(Collection\<K>)

```cangjie
public func contains(all!: Collection<K>): Bool
```

功能：判断是否包含指定集合中所有键的映射。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 键传递待判断的 keys。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果都包含，则返回 true；否则，返回 false。

### func contains(K)

```cangjie
public func contains(key: K): Bool
```

功能：判断是否包含指定键的映射。

参数：

- key: K - 传递要判断的 key。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在，则返回 true；否则，返回 false。

示例：

使用示例见 [HashMap 的 get/add/contains 函数](../collection_package_samples/sample_hashmap_get_add_contains.md)。

### func entryView(K)

```cangjie
public func entryView(key: K): MapEntryView<K, V>
```

功能：如果不包含特定键，返回一个空的引用视图。如果包含特定键，则返回该键对应的元素的引用视图。

参数：

- key: K - 要添加的键值对的键。

返回值：

- [MapEntryView](./collection_package_interface.md#interface-mapentryviewk-v)\<K, V> - 一个引用视图。

### func get(K)

```cangjie
public func get(key: K): ?V
```

功能：返回指定键映射到的值，如果 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 不包含指定键的映射，则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V>.None。

参数：

- key: K - 传入的键。

返回值：

- ?V - 键对应的值。用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装。

示例：

使用示例见 [HashMap 的 get/add/contains 函数](../collection_package_samples/sample_hashmap_get_add_contains.md)。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 是否为空，如果是，则返回 true；否则，返回 false。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 是否为空。

### func iterator()

```cangjie
public func iterator(): HashMapIterator<K, V>
```

功能：返回 HashMap 的迭代器。

返回值：

- [HashMapIterator](collection_package_class.md#class-hashmapiteratork-v-where-k--hashable--equatablek)\<K, V> - 返回 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的迭代器。

### func keys()

```cangjie
public func keys(): EquatableCollection<K>
```

功能：返回 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中所有的 key，并将所有 key 存储在一个 Keys 容器中。

返回值：

- [EquatableCollection](collection_package_interface.md#interface-equatablecollectiont)\<K> - 保存所有返回的 key。

### func remove(Collection\<K>)

```cangjie
public func remove(all!: Collection<K>): Unit
```

功能：从此 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中删除指定集合中键的映射（如果存在）。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 传入要删除的键的集合。