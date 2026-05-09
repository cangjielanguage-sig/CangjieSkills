## interface OrderedSet\<T>

```cangjie
public interface OrderedSet<T> <: Set<T> {
    prop first: ?T
    prop last: ?T
    func removeFirst(): ?T
    func removeLast(): ?T
    func backward(mark: T, inclusive!: Bool): Iterator<T>
    func forward(mark: T, inclusive!: Bool): Iterator<T>
}
```

功能：[OrderedSet](collection_package_interface.md#interface-orderedsett) 接口提供了一组集合的相关操作，允许我们以可读写的方式操作内部元素。

在 [OrderedSet](collection_package_interface.md#interface-orderedsett) 接口的实例中，其内部的元素是有序的。

父类型：

- [Set](collection_package_interface.md#interface-sett)\<T>

### prop first

```cangjie
prop first: ?T
```

功能：获取 [OrderedSet](collection_package_interface.md#interface-orderedsett) 第一个元素。

类型：?T

### prop last

```cangjie
prop last: ?T
```

功能：获取 [OrderedSet](collection_package_interface.md#interface-orderedsett) 最后一个元素。

类型：?T

### func backward(T, Bool)

```cangjie
func backward(mark: T, inclusive!: Bool): Iterator<T>
```

功能：获取从第一个元素小于等于 mark 的节点按降序遍历到 [first](./collection_package_interface.md#prop-first) 的迭代器。如果该节点的元素等于 mark ，那么根据 `inclusive!` 确定是否包含该元素对应的节点。

参数：

- mark: T - 用于确定从哪里开始的元素。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 mark 是迭代器的首个元素时，指定是否包含 mark 作为起始点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 迭代器。

### func forward(T, Bool)

```cangjie
func forward(mark: T, inclusive!: Bool): Iterator<T>
```

功能：获取从第一个元素大于等于 mark 的节点按升序遍历到 [last](./collection_package_interface.md#prop-last) 结束的一个迭代器。如果该节点的元素等于 mark ，那么根据 `inclusive!` 确定是否包含该元素对应的节点。

参数：

- mark: T - 用于确定从哪里开始的元素。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 mark 是迭代器的首个元素时，指定是否包含 mark 作为起始点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 迭代器。

### func removeFirst()

```cangjie
func removeFirst(): ?T
```

功能：删除 [OrderedSet](collection_package_interface.md#interface-orderedsett) 的第一个元素。

返回值：

- ?T - 如果当前 [OrderedSet](collection_package_interface.md#interface-orderedsett) 不为空，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装的被删除的元素，否则返回 `None`。

### func removeLast()

```cangjie
func removeLast(): ?T
```

功能：删除 [OrderedSet](collection_package_interface.md#interface-orderedsett) 的最后一个元素。

返回值：

- ?T - 如果当前 [OrderedSet](collection_package_interface.md#interface-orderedsett) 不为空，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装的被删除的元素，否则返回 `None`。