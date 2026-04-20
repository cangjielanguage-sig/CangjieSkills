### extend\<K, V> HashMap\<K, V> <: ToString where V <: ToString, K <: ToString

```cangjie
extend<K, V> HashMap<K, V> <: ToString where V <: ToString, K <: ToString
```

功能：为 [HashMap](./collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [HashMap](./collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> 实例转换为字符串。

该字符串包含 [HashMap](./collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> 内每个键值对的字符串表示，形如："[(k1, v1), (k2, v2), (k3, v3)]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。