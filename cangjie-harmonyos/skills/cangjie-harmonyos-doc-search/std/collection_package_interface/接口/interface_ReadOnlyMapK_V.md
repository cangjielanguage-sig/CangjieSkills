## interface ReadOnlyMap\<K, V>

```cangjie
public interface ReadOnlyMap<K, V> <: Collection<(K, V)> {
    func get(key: K): ?V
    func contains(key: K): Bool
    func contains(all!: Collection<K>): Bool
    func keys(): EquatableCollection<K>
    func values(): Collection<V>

    operator func [](key: K): V
}
```

功能：[ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 接口提供了一种将键映射到值的方式。它允许我们使用键来查找值，因此可以用于存储键值对。

[ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 不能包含重复的 key，每个 key 最多只能映射到一个 value。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)>

### func contains(Collection\<K>)

```cangjie
func contains(all!: Collection<K>): Bool
```

功能：判断是否包含指定集合键的映射。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 传递待判断的 的集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在，则返回 true；否则，返回 false。

### func contains(K)

```cangjie
func contains(key: K): Bool
```

功能：判断是否包含指定键的映射。

参数：

- key: K - 传递要判断的 key。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在，则返回 true；否则，返回 false。

### func get(K)

```cangjie
func get(key: K): ?V
```

功能：根据 key 得到 [ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 中映射的值。

参数：

- key: K - 传递 key，获取 value。

返回值：

- ?V - [ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 中与 Key 对应的值。

### func keys()

```cangjie
func keys(): EquatableCollection<K>
```

功能：返回 [ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 中所有的 key，并将所有 key 存储在一个 [EquatableCollection](collection_package_interface.md#interface-equatablecollectiont)\<K> 容器中。

返回值：

- [EquatableCollection](collection_package_interface.md#interface-equatablecollectiont)\<K> - 保存所有返回的 key。

### func values()

```cangjie
func values(): Collection<V>
```

功能：返回 [ReadOnlyMap](collection_package_interface.md#interface-readonlymapk-v) 中所有的 value，并将所有 value 存储在一个 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<V> 容器中。

返回值：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<V> - 保存所有返回的 value。

### operator func \[](K)

```cangjie
operator func [](key: K): V
```

功能：运算符重载集合，如果键存在，返回键对应的值，如果不存在，抛出异常。

参数：

- key: K - 需要进行查找的键。

返回值：

- V - 与键对应的值。