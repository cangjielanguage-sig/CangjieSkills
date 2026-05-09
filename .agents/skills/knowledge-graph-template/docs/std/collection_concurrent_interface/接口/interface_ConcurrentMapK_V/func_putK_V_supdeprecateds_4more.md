### func put(K, V) <sup>(deprecated)</sup>

```cangjie
func put(key: K, value: V): ?V
```

功能：将指定的值 value 与此 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中指定的键 key 关联。如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中已经包含键 key 的关联，则旧值将被替换；如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不包含键 key 的关联，则添加键 key 与值 value 的关联。

> **注意：**
>
> 未来版本即将废弃，使用 [add(K, V)](#func-addk-v) 替代。

参数：

- key: K - 要放置的键。
- value: V - 要关联的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回旧的值 Some(V)；当赋值前 key 不存在时，返回 None。

### func putIfAbsent(K, V) <sup>(deprecated)</sup>

```cangjie
func putIfAbsent(key: K, value: V): ?V
```

功能：当此 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在键 key 时，在 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中添加指定的值 value 与指定的键 key 的关联。如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 已经包含键 key，则不执行赋值操作。

> **注意：**
>
> 未来版本即将废弃，使用 [addIfAbsent(K, V)](#func-addifabsentk-v) 替代。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回当前 key 对应的值 Some(V)，且不执行赋值操作；当赋值前 key 不存在时，返回 None。

### func remove(K)

```cangjie
func remove(key: K): ?V
```

功能：从此映射中删除指定键 key 的映射（如果存在）。

参数：

- key: K - 传入要删除的 key。

返回值：

- ?V - 如果移除之前 key 存在，则返回 key 对应的值 Some(V)；当移除时 key 不存在时，返回 None。

### func remove(K, (V) -> Bool) <sup>(deprecated)</sup>

```cangjie
func remove(key: K, predicate: (V) -> Bool): ?V
```

功能：如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中存在键 key 且 key 所关联的值 v 满足条件 predicate，则从 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中删除 key 的关联。

> **注意：**
>
> 未来版本即将废弃，使用 [entryView(K, (MapEntryView\<K, V>) -> Unit)](#func-entryviewk-mapentryviewk-v---unit) 替代。

参数：

- key: K - 传入要删除的 key。
- predicate: (V) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递一个 lambda 表达式进行判断。

返回值：

- ?V - 如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中存在 key，则返回 key 对应的旧值 Some(V)；当 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在 key 时，或者 key 关联的值不满足 predicate 时，返回 None。