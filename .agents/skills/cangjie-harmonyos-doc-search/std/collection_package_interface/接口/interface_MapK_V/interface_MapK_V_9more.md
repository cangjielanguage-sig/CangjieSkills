## interface Map\<K, V>

```cangjie
public interface Map<K, V> <: ReadOnlyMap<K, V> {
    func add(key: K, value: V): ?V
    func add(all!: Collection<(K, V)>): Unit
    func addIfAbsent(key: K, value: V): ?V
    func clear(): Unit
    func entryView(k: K): MapEntryView<K, V>
    func remove(key: K): Option<V>
    func remove(all!: Collection<K>): Unit
    func removeIf(predicate: (K, V) -> Bool): Unit
    func replace(key: K, value: V): ?V
    operator func [](key: K, value!: V): Unit
}
```

功能：[Map](collection_package_interface.md#interface-mapk-v) 接口提供了一种将键映射到值的方式。它允许我们使用键来查找值，因此可以用于存储和操作键值对。

[Map](collection_package_interface.md#interface-mapk-v) 不能包含重复的 key，每个 key 最多只能映射到一个 value。

父类型：

- [ReadOnlyMap](collection_package_interface.md#interface-orderedmapk-v)\<K, V>

### func add(Collection\<(K, V)>)

```cangjie
func add(all!: Collection<(K, V)>): Unit
```

功能：将新的键值对放入 [Map](collection_package_interface.md#interface-mapk-v) 中。对于 [Map](collection_package_interface.md#interface-mapk-v) 中已有的键，该键映射的值将被新值替换。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 需要放入到 [Map](collection_package_interface.md#interface-mapk-v) 中的键值对集合。

### func add(K, V)

```cangjie
func add(key: K, value: V): ?V
```

功能：将传入的键值对放入该 [Map](collection_package_interface.md#interface-mapk-v) 中。对于 [Map](collection_package_interface.md#interface-mapk-v) 中已有的键，该键映射的值将被新值替换。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- ?V - 如果赋值之前 key 存在，返回旧值，否则返回 None。

### func addIfAbsent(K, V)

```cangjie
func addIfAbsent(key: K, value: V): ?V
```

功能：如果 key 不在当前 [Map](collection_package_interface.md#interface-mapk-v) 中，添加指定键值对 key-value。否则不做修改。

参数：

- key: K - 待添加键值对的键。
- value: V - 待添加键值对的值。

返回值：

- ?V - 如果调用该函数时当前 [Map](collection_package_interface.md#interface-mapk-v) 中已有指定的 key，返回该 key 对应的旧值，否则返回 None。

### func clear()

```cangjie
func clear(): Unit
```

功能：清除所有键值对。

### func entryView(K)

```cangjie
func entryView(k: K): MapEntryView<K, V>
```

功能：获取键 k 对应的视图。

参数：

- k: K - 待获取其视图的键。

返回值：

- [MapEntryView](#interface-mapentryviewk-v)\<K, V> - 键 k 对应的视图。

### func remove(Collection\<K>)

```cangjie
func remove(all!: Collection<K>): Unit
```

功能：从此映射中删除指定集合的映射（如果存在）。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<K> - 传入要删除的集合。

### func remove(K)

```cangjie
func remove(key: K): Option<V>
```

功能：从此 [Map](collection_package_interface.md#interface-mapk-v) 中删除指定键的映射（如果存在）。

参数：

- key: K - 传入要删除的 key。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V> - 从 [Map](collection_package_interface.md#interface-mapk-v) 中移除的键对应的值。用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装。

### func removeIf((K, V) -> Bool)

```cangjie
func removeIf(predicate: (K, V) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足条件，则删除对应的键值对。

参数：

- predicate: (K, V) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递一个 lambda 表达式进行判断。