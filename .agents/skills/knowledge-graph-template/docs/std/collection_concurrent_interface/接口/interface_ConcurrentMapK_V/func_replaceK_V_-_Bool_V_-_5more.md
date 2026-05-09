### func replace(K, (V) -> Bool, (V) -> V) <sup>(deprecated)</sup>

```cangjie
func replace(key: K, predicate: (V) -> Bool, eval: (V) -> V): ?V
```

功能：如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中存在键 key（假设其关联的值为 v），且 v 满足条件 predicate，则将 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中键 key 关联的值替换为 eval(v) 的计算结果；如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在键 key，或者存在键 key 但关联的值不满足 predicate，则不对 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 做任何修改。

> **注意：**
>
> 未来版本即将废弃，使用 [entryView(K, (MapEntryView\<K, V>) -> Unit)](#func-entryviewk-mapentryviewk-v---unit) 替代。

参数：

- key: K - 传入要替换所关联值的键。
- predicate: (V) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递一个 lambda 表达式进行判断。
- eval: (V) ->V - 传入计算用于替换的新值的函数。

返回值：

- ?V - 如果 key 存在，则返回 key 对应的旧值 Some(V)；当 key 不存在时，或者 key 关联的值不满足 predicate 时，返回 None。

### func replace(K, (V) -> V) <sup>(deprecated)</sup>

```cangjie
func replace(key: K, eval: (V) -> V): ?V
```

功能：如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中存在键 key（假设其关联的值为 v），则将 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中键 key 关联的值替换为 eval(v) 的计算结果；如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在键 key，则不对 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 做任何修改。

> **注意：**
>
> 未来版本即将废弃，使用 [entryView(K, (MapEntryView\<K, V>) -> Unit)](#func-entryviewk-mapentryviewk-v---unit) 替代。

参数：

- key: K - 传入要替换所关联值的键。
- eval: (V) ->V - 传入计算用于替换的新值的函数。

返回值：

- ?V - 如果 key 存在，则返回 key 对应的旧值 Some(V)；当 key 不存在时，返回 None。

### func replace(K, V)

```cangjie
func replace(key: K, value: V): ?V
```

功能：如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中存在 key，则将 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中键 key 关联的值替换为 value；如果 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 中不存在 key，则不对 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 做任何修改。

参数：

- key: K - 传入要替换所关联值的键。
- value: V - 传入要替换成的新值。

返回值：

- ?V - 如果 key 存在，则返回 key 对应的旧值 Some(V)；当 key 不存在时，返回 None。

### operator func \[](K)

```cangjie
operator func [](key: K): V
```

功能：根据指定键 key 获取值。如果键 key 存在，返回对应的值；如果不存在，抛出异常。

参数：

- key: K - 待获取其值的键。

返回值：

- V - 键 key 对应的值。

异常：

- [NoneValueException](../../core/core_package_api/core_package_exceptions.md#class-nonevalueexception) - 当前映射中不存在键 key。

### operator func \[](K, V)

```cangjie
operator func [](key: K, value!: V): Unit
```

功能：设置指定键 key 的值为 value。如果键 key 存在，新 value 覆盖旧 value；如果键不存在，添加此键值对。

参数：

- key: K - 待设置其值的键。
- value!: V - 待设置的值。