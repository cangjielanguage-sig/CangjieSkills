### func remove(LinkedListNode\<T>)

```cangjie
public func remove(node: LinkedListNode<T>): T
```

功能：删除链表中指定节点。

参数：

- node: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 要被删除的节点。

返回值：

- T - 被删除的节点的值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的节点不属于该链表，则抛此异常。

### func removeFirst()

```cangjie
public func removeFirst() : ?T
```

功能：移除链表的第一个元素，并返回该元素的值。

返回值：

- ?T - 被删除的元素的值，若链表为空则返回 None。

### func removeIf((T)-> Bool)

```cangjie
public func removeIf(predicate: (T)-> Bool): Unit
```

功能：删除此链表中满足给定 lambda 表达式或函数的所有元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 对于要删除的元素，返回值为 true。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [LinkedList](./collection_package_class.md#class-linkedlistt) 内节点时，抛出异常。

### func removeLast()

```cangjie
public func removeLast() : ?T
```

功能：移除链表的最后一个元素，并返回该元素的值。

返回值：

- ?T - 被删除的元素的值，若链表为空则返回 None。

### func reverse()

```cangjie
public func reverse(): Unit
```

功能：反转此链表中的元素顺序。

### func splitOff(LinkedListNode\<T>)

```cangjie
public func splitOff(node: LinkedListNode<T>): LinkedList<T>
```

功能：从指定的节点 node 开始，将链表分割为两个链表，如果分割成功，node 不在当前的链表内，而是作为首个节点存在于新的链表内部。

参数：

- node: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 要分割的位置。

返回值：

- [LinkedList](collection_package_class.md#class-linkedlistt)\<T> - 原链表分割后新产生的链表。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的节点不属于该链表，则抛此异常。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个数组，数组包含该链表中的所有元素，并且顺序与链表的顺序相同。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。