### func replace(K, V)

```cangjie
func replace(key: K, value: V): ?V
```

功能：如果当前 [Map](collection_package_interface.md#interface-mapk-v) 中已有指定 key，将其值修改为 value。否则不做修改。

参数：

- key: K - 待修改键值对的键。
- value: V - 待修改键值对的新值。

返回值：

- ?V - 如果当前 [Map](collection_package_interface.md#interface-mapk-v) 中已有指定 key，返回其旧值。否则返回 None。

### operator func \[](K, V)

```cangjie
operator func [](key: K, value!: V): Unit
```

功能：运算符重载集合，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

参数：

- key: K - 需要进行设置的键。
- value!: V - 传递要设置的值。