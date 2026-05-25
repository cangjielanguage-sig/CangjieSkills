### func addBefore(LinkedListNode\<T>,T)

```cangjie
public func addBefore(node: LinkedListNode<T>, element: T): LinkedListNode<T>
```

功能：在链表中指定节点的前面插入一个元素，并且返回该元素的节点。

参数：

- node: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指定的节点。
- element: T - 要添加到链表中的元素。

返回值：

- [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指向被插入元素的节点。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的节点不属于该链表，则抛此异常。

### func addFirst(T)

```cangjie
public func addFirst(element: T): LinkedListNode<T>
```

功能：在链表的头部位置插入一个元素，并且返回该元素的节点。

参数：

- element: T - 要添加到链表中的元素。

返回值：

- [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指向该元素的节点。

### func addLast(T)

```cangjie
public func addLast(element: T): LinkedListNode<T>
```

功能：在链表的尾部位置添加一个元素，并且返回该元素的节点。

参数：

- element: T - 要添加到链表中的元素。

返回值：

- [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指向该元素的节点。

### func backward(LinkedListNode\<T>)

```cangjie
public func backward(mark: LinkedListNode<T>): Iterator<T>
```

功能：获取一个从 mark 节点开始，到所对应链表的头部节点的所有元素的迭代器。

参数：

- mark: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 开始的元素节点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 对应元素的迭代器。

异常：

- [IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception) - 如果该节点不属于任何链表实例，抛此异常。

### func clear()

```cangjie
public func clear(): Unit
```

功能：删除链表中的所有元素。

### func forward(LinkedListNode\<T>)

```cangjie
public func forward(mark: LinkedListNode<T>): Iterator<T>
```

功能：获取一个从 mark 节点开始，到所对应链表的尾部节点的所有元素的迭代器。

参数：

- mark: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 开始的元素节点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 对应元素的迭代器。

异常：

- [IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception) - 如果该节点不属于任何链表实例，抛此异常。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：返回此链表是否为空链表的判断。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果此链表中不包含任何元素，返回 true。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：返回当前集合中元素的迭代器，其顺序是从链表的第一个节点到链表的最后一个节点。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 当前集合中元素的迭代器。

### func nodeAt(Int64)

```cangjie
public func nodeAt(index: Int64): Option<LinkedListNode<T>>
```

功能：获取链表中的第 index 个元素的节点，编号从 0 开始。

该函数的时间复杂度为 O(n)。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定获取第 index 个元素的节点。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T>> - 编号为 index 的节点，如果没有则返回 None。