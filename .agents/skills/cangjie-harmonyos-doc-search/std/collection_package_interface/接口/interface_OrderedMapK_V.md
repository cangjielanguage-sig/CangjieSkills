## interface OrderedMap\<K, V>

```cangjie
public interface OrderedMap<K, V> <: Map<K, V> {
    prop first: ?(K, V)
    prop last: ?(K, V)
    func removeFirst(): ?(K, V)
    func removeLast(): ?(K, V)

    func backward(mark: K, inclusive!: Bool): Iterator<(K, V)>
    func forward(mark: K, inclusive!: Bool): Iterator<(K, V)>
}
```

功能：[OrderedMap](collection_package_interface.md#interface-orderedmapk-v) 接口提供了一种将键映射到值的方式。它允许我们使用键来查找值，因此可以用于存储和操作键值对。

在 [OrderedMap](collection_package_interface.md#interface-orderedmapk-v) 接口的实例中，其内部的元素是有序的。

父类型：

- [Map](collection_package_interface.md#interface-mapk-v)\<K, V>

### prop first

```cangjie
prop first: ?(K, V)
```

功能：获取 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 第一个元素。

类型：?(K, V)

### prop last

```cangjie
prop last: ?(K, V)
```

功能：获取 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 最后一个元素。

类型：?(K, V)

### func backward(K, Bool)

```cangjie
func backward(mark: K, inclusive!: Bool): Iterator<(K, V)>
```

功能：获取从第一个键小于等于 mark 的节点按降序遍历到 [first](./collection_package_interface.md#prop-first) 的迭代器。如果该节点的键等于 mark ，那么根据 `inclusive!` 确定是否包含该键对应的节点。

参数：

- mark: K - 用于确定从哪里开始的键。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 mark 是迭代器的首个元素的 key 时，指定是否包含 mark 作为起始点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)> - 迭代器。

### func forward(K, Bool)

```cangjie
func forward(mark: K, inclusive!: Bool): Iterator<(K, V)>
```

功能：获取从第一个键大于等于 mark 的节点按升序遍历到 [last](./collection_package_interface.md#prop-last) 结束的一个迭代器。如果该节点的键等于 mark ，那么根据 `inclusive!` 确定是否包含该键对应的节点。

参数：

- mark: K - 用于确定从哪里开始的键。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 mark 是迭代器的首个元素的 key 时，指定是否包含 mark 作为起始点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(K, V)> - 迭代器。

### func removeFirst()

```cangjie
func removeFirst(): ?(K, V)
```

功能：删除 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 的第一个元素。

返回值：

- ?(K, V) - 如果当前 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 不为空，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装的被删除的键值对，否则返回 `None`。

### func removeLast()

```cangjie
func removeLast(): ?(K, V)
```

功能：删除 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 的最后一个元素。

返回值：

- ?(K, V) - 如果当前 [OrderedMap](./collection_package_interface.md#interface-orderedmapk-v) 不为空，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装的被删除的键值对，否则返回 `None`。