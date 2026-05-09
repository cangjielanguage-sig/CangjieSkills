## class ConcurrentHashMapIterator\<K, V> where K <: Hashable & Equatable\<K>

```cangjie
public class ConcurrentHashMapIterator<K, V> <: Iterator<(K, V)> where K <: Hashable & Equatable<K> {
    public init(cmap: ConcurrentHashMap<K, V>)
}
```

功能：此类主要实现 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 的迭代器功能。

> **注意：**
>
> 这里定义的  [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 迭代器：
>
> 1. 不保证迭代结果为并发 [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 某一时刻的 “快照”，建议在环境中没有其他线程并发地修改  [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 时调用；
> 2. 迭代器在迭代过程中，不保证可以感知环境线程对目标  [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 的修改。

父类型：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)>

### init(ConcurrentHashMap\<K, V>)

```cangjie
public init(cmap: ConcurrentHashMap<K, V>)
```

功能：创建 [ConcurrentHashMapIterator](collection_concurrent_class.md#class-concurrenthashmapiteratork-v-where-k--hashable--equatablek)\<K, V> 实例。

参数：

- cmap: [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)\<K, V> - 待获取其迭代器的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)\<K, V> 实例。

### func next()

```cangjie
public func next(): Option<(K, V)>
```

功能：返回迭代中的下一个元素。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)> - [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K,V)> 类型。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let map: ConcurrentHashMap<Int64, Int64> = ConcurrentHashMap<Int64, Int64>(3, {value => (value, value)})
    let iter = ConcurrentHashMapIterator<Int64, Int64>(map)
    while (true) {
        match (iter.next()) {
            case Some(i) => println("(${i[0]},${i[1]})")
            case None => break
        }
    }
}
```

运行结果：

```text
(0,0)
(1,1)
(2,2)
```