### func add(K, V)

```cangjie
func add(key: K, value: V): ?V
```

功能：将指定的值 value 与此 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中指定的键 key 关联。如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中已经包含键 key 的关联，则旧值将被替换；如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不包含键 key 的关联，则添加键 key 与值 value 的关联。

参数：

- key: K - 要放置的键。
- value: V - 要关联的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回旧的值 Some(V)；当赋值前 key 不存在时，返回 None。

### func addIfAbsent(K, V)

```cangjie
func addIfAbsent(key: K, value: V): ?V
```

功能：当此 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在键 key 时，在 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中添加指定的值 value 与指定的键 key 的关联。如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 已经包含键 key，则不执行赋值操作。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回当前 key 对应的值 Some(V)，且不执行赋值操作；当赋值前 key 不存在时，返回 None。

### func contains(K)

```cangjie
func contains(key: K): Bool
```

功能：判断 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中是否包含指定键 key 的关联。

参数：

- key: K - 传递要判断的 key。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 key 存在时返回 true；当 key 不存在时返回 false。

### func entryView(K, (MapEntryView\<K, V>) -> Unit)

```cangjie
func entryView(key: K, fn: (MapEntryView<K, V>) -> Unit): ?V
```

功能：根据指定键 key 获取当前映射中相应的键值对视图 entryView，并调用函数 fn 对该键值对进行增、删、改操作，并返回最终映射中键 key 对应的值。

如果当前映射中不包含键 key，则将获取一个空视图 entryView，如果将其 value 置为非 None 值，则将在当前映射中增加 key-value 键值对。

如果当前映射中包含键 key，则将获取 key-value 的视图，如果将 value 置为 None，则相当于从当前映射中删除该键值对；如果将 value 置为新的非 None 值，则相当于修改当前映射中键 key 对应的值。

参数：

- key: K - 待获取其相应视图的键。
- fn: ([MapEntryView](../../collection/collection_package_api/collection_package_interface.md#interface-mapentryviewk-v)\<K, V>) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 对指定视图进行的自定义操作，可用于对映射中键值对进行增、删、改操作。

返回值：

- ?V - 函数 fn 调用结束后当前映射中键 key 对应的值，如果 key 不存在，返回 None。

### func get(K)

```cangjie
func get(key: K): ?V
```

功能：返回 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中键 key 所关联的值。

参数：

- key: K - 传递 key，获取 value。

返回值：

- ?V - 当 key 存在时，返回其关联的值 Some(V)；当 key 不存在时，返回 None。