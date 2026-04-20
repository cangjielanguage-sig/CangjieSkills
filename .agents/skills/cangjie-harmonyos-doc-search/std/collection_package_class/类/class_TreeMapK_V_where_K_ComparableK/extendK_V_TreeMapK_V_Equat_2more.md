### extend\<K, V> TreeMap\<K, V> <: Equatable\<TreeMap\<K, V>> where V <: Equatable\<V>

```cangjie
extend<K, V> TreeMap<K, V> <: Equatable<TreeMap<K, V>> where V <: Equatable<V>
```

功能：为 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 类型扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V>> 接口，支持判等操作。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V>>

#### operator func !=(TreeMap\<K, V>)

```cangjie
public operator func !=(right: TreeMap<K, V>): Bool
```

功能：判断当前实例与参数指向的 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 实例是否不等。

参数：

- right: [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 true，否则返回 false。

#### operator func ==(TreeMap\<K, V>)

```cangjie
public operator func ==(right: TreeMap<K, V>): Bool
```

功能：判断当前实例与参数指向的 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 实例是否相等。

两个 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 相等指的是其中包含的键值对完全相等。

参数：

- right: [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。

### extend\<K, V> TreeMap\<K, V> <: ToString where V <: ToString, K <: ToString & Comparable\<K>

```cangjie
extend<K, V> TreeMap<K, V> <: ToString where V <: ToString, K <: ToString & Comparable<K>
```

功能：为 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 实例转换为字符串。

该字符串包含 [TreeMap](./collection_package_class.md#class-treemapk-v-where-k--comparablek)\<K, V> 内每个键值对的字符串表示，形如："[(k1, v1), (k2, v2), (k3, v3)]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。