## class LinkedList\<T>

```cangjie
public class LinkedList<T> <: Collection<T> {
    public init()
    public init(elements: Collection<T>)
    public init(elements: Array<T>)
    public init(size: Int64, initElement: (Int64)-> T)
}
```

功能：实现双向链表的数据结构。

双向链表是一种常见的数据结构，它由一系列节点组成，每个节点都包含两个指针，一个指向前一个节点，另一个指向后一个节点。这种结构允许在任何一个节点上进行双向遍历，即可以从头节点开始向后遍历，也可以从尾节点开始向前遍历。

[LinkedList](collection_package_class.md#class-linkedlistt) 不支持并发操作，并且对集合中元素的修改不会使迭代器失效，只有在添加和删除元素的时候会使迭代器失效。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### prop first

```cangjie
public prop first: ?T
```

功能：链表中第一个元素的值，如果是空链表则返回 None。

类型：?T

### prop firstNode

```cangjie
public prop firstNode: ?LinkedListNode<T>
```

功能：获取链表中的第一个元素的节点。

类型：?[LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T>

### prop last

```cangjie
public prop last: ?T
```

功能：链表中最后一个元素的值，如果是空链表则返回 None。

类型：?T

### prop lastNode

```cangjie
public prop lastNode: ?LinkedListNode<T>
```

功能：获取链表中的最后一个元素的节点。

类型：?[LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T>

### prop size

```cangjie
public prop size: Int64
```

功能：链表中的元素数量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的链表。

### init(Array\<T>)

```cangjie
public init(elements: Array<T>)
```

功能：按照数组的遍历顺序构造一个包含指定集合元素的 [LinkedList](collection_package_class.md#class-linkedlistt) 实例。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 将要放入此链表中的元素数组。

### init(Collection\<T>)

```cangjie
public init(elements: Collection<T>)
```

功能：按照集合迭代器返回元素的顺序构造一个包含指定集合元素的链表。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 将要放入此链表中的元素集合。

### init(Int64, (Int64)-> T)

```cangjie
public init(size: Int64, initElement: (Int64)-> T)
```

功能：创建一个包含 size 个元素，且第 n 个元素满足 ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64))-> T 条件的链表。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要创建的链表元素数量。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) ->T - 元素的初始化参数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的链表长度小于 0 则抛此异常。

### func addAfter(LinkedListNode\<T>,T)

```cangjie
public func addAfter(node: LinkedListNode<T>, element: T): LinkedListNode<T>
```

功能：在链表中指定节点的后面插入一个元素，并且返回该元素的节点。

参数：

- node: [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指定的节点。
- element: T - 要添加到链表中的元素。

返回值：

- [LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T> - 指向被插入元素的节点。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的节点不属于该链表，则抛此异常。