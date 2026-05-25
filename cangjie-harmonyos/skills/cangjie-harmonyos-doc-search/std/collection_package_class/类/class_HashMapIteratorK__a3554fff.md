## class HashMapIterator\<K, V> where K <: Hashable & Equatable\<K>

```cangjie
public class HashMapIterator<K, V> <: Iterator<(K, V)> where K <: Hashable & Equatable<K> {
    public init(map: HashMap<K, V>)
}
```

功能：此类主要实现 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的迭代器功能。

父类型：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)>

### init(HashMap\<K, V>)

```cangjie
public init(map: HashMap<K, V>)
```

功能：创建 [HashMapIterator](collection_package_class.md#class-hashmapiteratork-v-where-k--hashable--equatablek)\<K, V> 实例。

参数：

- [map](collection_package_function.md#func-mapt-rt---r): [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> - 传入 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V>。

### func next()

```cangjie
public func next(): ?(K, V)
```

功能：返回迭代器中的下一个元素。

返回值：

- ?(K, V) - 迭代器中的下一个元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装。

异常：

- [ConcurrentModificationException](collection_package_exception.md#class-concurrentmodificationexception) - 当函数检测到不同步的并发修改，抛出异常。

### func remove()

```cangjie
public func remove(): Option<(K, V)>
```

功能：删除此 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 迭代器的 next 函数返回的元素，此函数只能在 next 函数调用时调用一次。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)> - 返回被删除的元素。

异常：

- [ConcurrentModificationException](collection_package_exception.md#class-concurrentmodificationexception) - 当函数检测到不同步的并发修改，抛出异常。