### func contains(Collection\<T>)

```cangjie
public func contains(all!: Collection<T>): Bool
```

功能：判断 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 是否包含指定 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 指定的元素集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 包含 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素，则返回 true；否则，返回 false。

### func contains(T)

```cangjie
public func contains(element: T): Bool
```

功能：判断是否包含指定元素。

参数：

- element: T - 指定的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果包含指定元素，则返回 true；否则，返回 false。

### func forward(T, Bool)

```cangjie
public func forward(mark: T, inclusive!: Bool = true): Iterator<T>
```

功能：获取从第一个元素大于等于 mark 的节点按升序遍历到 [last](./collection_package_class.md#prop-last-3) 结束的一个迭代器。如果该节点的元素等于 mark ，那么根据 `inclusive!` 确定是否包含该元素对应的节点。

参数：

- mark: T - 用于确定从哪里开始的元素。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 `mark` 是迭代器的首个元素时，指定是否包含 mark 作为起始点，默认为 `true`。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 对应元素的迭代器。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：返回 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的迭代器，迭代器按元素值从小到大的顺序迭代。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的迭代器。

### func remove(Collection\<T>)

```cangjie
public func remove(all!: Collection<T>): Unit
```

功能：移除此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中那些也包含在指定 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要从此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中移除的元素的集合。

### func remove(T)

```cangjie
public func remove(element: T): Bool
```

功能：如果指定元素存在于此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中，则将其移除。

参数：

- element: T - 需要被移除的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，表示移除成功；false，表示移除失败。