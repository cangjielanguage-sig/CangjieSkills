## interface Deque\<T>

```cangjie
public interface Deque<T> <: Collection<T> {
    prop first: ?T
    prop last: ?T
    func addFirst(element: T): Unit
    func addLast(element: T): Unit
    func removeFirst(): ?T
    func removeLast(): ?T
}
```

功能：Deque（double-ended queue）是一种具有队列和栈特性的数据结构，允许从两端插入和删除元素。Deque 接口的主要功能包括：

- 插入操作：可以在双端队列的前端或后端插入元素。使用 addFirst 方法在双端队列头部插入元素，使用 addLast 在双端队列尾部插入元素。
- 访问操作：可以访问双端队列的前端或后端的元素，而不进行删除操作。使用 first 访问头部元素，使用 last 访问尾部元素。
- 删除操作：可以在双端队列的前端或后端删除元素。使用 removeFirst 删除头部元素并返回其值，使用 removeLast 删除尾部元素并返回其值。
- 其他集合类型支持的操作，比如元素数量、判空、迭代器操作。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### prop first

```cangjie
prop first: ?T
```

功能：访问双端队列头部元素，该操作不会删除头部元素。如果双端队列为空，返回 None。

类型：?T

### prop last

```cangjie
prop last: ?T
```

功能：访问双端队列尾部元素，该操作不会删除尾部元素。如果双端队列为空，返回 None。

类型：?T

### func addFirst(T)

```cangjie
func addFirst(element: T): Unit
```

功能：在双端队列头部插入指定的元素。

参数：

- element: T - 被添加到双端队列中的元素。

### func addLast(T)

```cangjie
func addLast(element: T): Unit
```

功能：在双端队列尾部插入指定的元素。

参数：

- element: T - 被添加到双端队列中的元素。

### func removeFirst()

```cangjie
func removeFirst(): ?T
```

功能：删除双端队列中的头部元素并返回这个元素的值。

返回值：

- ?T - Option 封装的被删除的元素的值，如果双端队列为空，返回 None。

### func removeLast()

```cangjie
func removeLast(): ?T
```

功能：删除双端队列中的尾部元素并返回这个元素的值。

返回值：

- ?T - Option 封装的被删除的元素的值，如果双端队列为空，返回 None。