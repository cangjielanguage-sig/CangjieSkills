### static func of(Array\<T>)

```cangjie
public static func of(elements: Array<T>): TreeSet<T>
```

功能：构造一个包含指定数组中所有元素的 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

按照 elements 的先后顺序将元素插入到 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 内，由于 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中不允许出现相同的元素，如果 elements 中有多个相同的元素时，[TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 只会保留一个元素。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 传入数组，变长参数语法支持参数省略数组字面量的 `[]` 。

返回值：

- [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - 元素为 T 类型的 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

> **说明：**
>
> 此函数的参数可使用变长参数方式提供，例如： `TreeSet.of(1, 2, 3)` 等价于 `TreeSet.of([1, 2, 3])` 。

### func add(Collection\<T>)

```cangjie
public func add(all!: Collection<T>): Unit
```

功能：添加 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素至此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中，如果元素存在，则不添加。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要被添加的元素的集合。

### func add(T)

```cangjie
public func add(element: T): Bool
```

功能：将新的元素放入 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中。若添加的元素在 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中存在，则添加失败。

参数：

- element: T - 指定的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果添加成功，则返回 true；否则，返回 false。

### func backward(T, Bool)

```cangjie
public func backward(mark: T, inclusive!: Bool = true): Iterator<T>
```

功能：获取从第一个键小于等于 mark 的节点按降序遍历到 [first](./collection_package_class.md#prop-first-4) 的迭代器。如果该节点的键等于 mark ，那么根据 `inclusive!` 确定是否包含该键对应的节点。

参数：

- mark: T - 用于确定从哪里开始的元素。
- inclusive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当 `mark` 是迭代器的首个元素时，指定是否包含 mark 作为起始点，默认为 `true`。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 对应元素的迭代器。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清除所有元素。

### func clone()

```cangjie
public func clone(): TreeSet<T>
```

功能：克隆 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)。

返回值：

- [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - 返回一个 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 实例。