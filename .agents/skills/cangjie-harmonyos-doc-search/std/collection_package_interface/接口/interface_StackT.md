## interface Stack\<T>

```cangjie
public interface Stack<T> <: Collection<T> {
    func add(element: T): Unit
    func peek(): ?T
    func remove(): ?T
}
```

功能：Stack（栈）是一种数据结构，具有后进先出（Last In First Out，LIFO）的特点。可以在一端（称为栈顶）进行插入和删除操作，而另一端（称为栈底）则不允许进行操作。

栈的基本操作包括入栈（add）、出栈（remove）、查看栈顶元素（peek）。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### func add(T)

```cangjie
func add(element: T): Unit
```

功能：向栈中添加元素。

参数：

- element: T - 将被放到栈顶的元素。

### func peek()

```cangjie
func peek(): ?T
```

功能：查看栈顶元素，该操作不会删除栈顶元素。

返回值：

- ?T - 栈顶元素，如果栈为空，返回 `None`。

### func remove()

```cangjie
func remove(): ?T
```

功能：删除并返回栈顶的元素。

返回值：

- ?T - 被删除的栈顶元素，如果栈为空，返回 `None`。