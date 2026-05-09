## interface Queue\<T>

```cangjie
public interface Queue<T> <: Collection<T> {
    func add(element: T): Unit
    func peek(): ?T
    func remove(): ?T
}
```

功能：队列数据结构，它遵循先进先出（First In First Out, FIFO）原则。Queue 的主要功能包括：

- 添加元素：将指定的元素添加到队列的尾部。
- 访问操作：可以访问队列的前端元素，而不进行删除操作。
- 删除操作：可以删除队列的前端元素。
- 其他集合类型支持的操作，比如元素数量、判空、迭代器操作。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### func add(T)

```cangjie
func add(element: T): Unit
```

功能：在队列尾部插入指定的元素。

参数：

- element: T - 被添加到队列中的元素。

### func peek()

```cangjie
func peek(): ?T
```

功能：访问双端队列头部元素，该操作不会删除头部元素。

返回值：

- ?T - Option 封装的头部元素的值，如果双端队列为空，返回 `None`。

### func remove()

```cangjie
func remove(): ?T
```

功能：删除队列中的头部元素并返回这个元素的值。

返回值：

- ?T - Option 封装的被删除的元素的值，如果队列为空，返回 `None`。

## interface ReadOnlyList\<T>

```cangjie
public interface ReadOnlyList<T> <: Collection<T> {
    prop first: ?T
    prop last: ?T
    func get(index: Int64): ?T
    operator func [](index: Int64): T
}
```

功能：定义了只读列表。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### prop first

```cangjie
prop first: ?T
```

功能：返回此列表中的第一个元素，如果没有则返回 None。

类型：?T

### prop last

```cangjie
prop last: ?T
```

功能：返回此列表中的最后一个元素，如果没有则返回 None。

类型：?T

### func get(Int64)

```cangjie
func get(index: Int64): ?T
```

功能：返回此列表中指定位置的元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要返回的元素的索引。

返回值：

- ?T - 返回指定位置的元素，如果 index 大小小于 0 或者大于等于此列表中的元素数量，返回 None。

### operator func \[](Int64)

```cangjie
operator func [](index: Int64): T
```

功能：操作符重载 - get。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 表示 get 接口的索引。

返回值：

- T - 索引位置的元素的值。