### extend\<K, V> HashMap\<K, V> <: Shrink\<HashMap\<K, V>>

```cangjie
extend<K, V> HashMap<K, V> <: Shrink<HashMap<K, V>>
```

功能：为 [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<T> 实现了 [Shrink](#interface-shrinkt)\<[HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<T>> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<T>>

#### func shrink()

```cangjie
func shrink(): Iterable<HashMap<K, V>>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<HashMap\<K, V>> - 一组可能的“较小”值的迭代器。