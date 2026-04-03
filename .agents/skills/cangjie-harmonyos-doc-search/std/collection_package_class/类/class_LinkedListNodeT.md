## class LinkedListNode\<T>

```cangjie
public class LinkedListNode<T> {}
```

功能：[LinkedListNode](collection_package_class.md#class-linkedlistnodet) 是 [LinkedList](collection_package_class.md#class-linkedlistt) 上的节点。

可以通过 [LinkedListNode](collection_package_class.md#class-linkedlistnodet) 对 [LinkedList](collection_package_class.md#class-linkedlistt) 进行前向后向遍历操作，也可以访问和修改元素的值。

[LinkedListNode](collection_package_class.md#class-linkedlistnodet) 只能通过对应 [LinkedList](collection_package_class.md#class-linkedlistt) 的 'nodeAt'、'firstNode'、'lastNode' 获得，当 [LinkedList](collection_package_class.md#class-linkedlistt) 删除掉对应的节点时，会造成一个悬空的节点，对悬空的节点进行任何操作都会抛 '[IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception)' 异常。

### prop next

```cangjie
public prop next: Option<LinkedListNode<T>>
```

功能：获取当前节点的下一个节点，如果没有则返回 None。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T>>

异常：

- [IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception) - 如果该节点不属于任何链表实例，抛此异常。

### prop prev

```cangjie
public prop prev: Option<LinkedListNode<T>>
```

功能：获取当前节点的前一个节点，如果没有则返回 None。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[LinkedListNode](collection_package_class.md#class-linkedlistnodet)\<T>>

异常：

- [IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception) - 如果该节点不属于任何链表实例，抛此异常。

### prop value

```cangjie
public mut prop value: T
```

功能：获取或者修改元素的值。

类型：T

异常：

- [IllegalStateException](../../core/core_package_api/core_package_exceptions.md#class-illegalstateexception) - 如果该节点不属于任何链表实例，抛此异常。