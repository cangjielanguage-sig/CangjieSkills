## interface ConcurrentMap\<K, V>

```cangjie
public interface ConcurrentMap<K, V> {
    func add(key: K, value: V): ?V
    func addIfAbsent(key: K, value: V): ?V
    func entryView(key: K, fn: (MapEntryView<K, V>) -> Unit): ?V
    func get(key: K): ?V
    func contains(key: K): Bool
    func put(key: K, value: V): ?V
    func putIfAbsent(key: K, value: V): ?V
    func remove(key: K): ?V
    func remove(key: K, predicate: (V) -> Bool): ?V
    func replace(key: K, value: V): ?V
    func replace(key: K, eval: (V) -> V): ?V
    func replace(key: K, predicate: (V) -> Bool, eval: (V) -> V): ?V
    operator func [](key: K): V
    operator func [](key: K, value!: V): Unit
}
```

功能：保证线程安全和操作原子性的 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 接口定义。

[ConcurrentMap](collection_concurrent_interface.md#interface-concurrentmapk-v) 接口中声明了并发场景下线程安全的 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 必须保证**原子性**的方法，我们希望定义的线程安全 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 类都能实现 [ConcurrentMap](collection_concurrent_interface.md#interface-concurrentmapk-v) 接口。例如我们在该包中定义的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 就实现了 [ConcurrentMap](collection_concurrent_interface.md#interface-concurrentmapk-v) 接口，并提供了 [ConcurrentMap](collection_concurrent_interface.md#interface-concurrentmapk-v) 中所声明方法的保证原子性的实现。

[ConcurrentMap](collection_concurrent_interface.md#interface-concurrentmapk-v) 接口中声明了并发 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 在并发场景下需要保证原子性的方法。

并发 [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v) 为“键”到“值”的映射，其中 K 为键的类型，V 为值的类型。