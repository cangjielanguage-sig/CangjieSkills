## class ArrayStack\<T>

```cangjie
public class ArrayStack<T> <: Stack<T> {
    public init(capacity: Int64)
    public init()
}
```

功能：[ArrayStack](#class-arraystackt) 是一种基于数组 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 实现的栈 [Stack](./collection_package_interface.md#interface-stackt) 数据结构。ArrayStack 的实现方式是使用一个数组来存储栈中的元素，同时使用一个指针来指向栈顶元素的位置。

[ArrayStack](#class-arraystackt) 只支持后进先出（Last In First Out，LIFO），只能在头部进行插入删除操作，并且 [ArrayStack](#class-arraystackt) 会根据实际需要进行扩容。

父类型：

- [Stack](./collection_package_interface.md#interface-stackt)\<T>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：栈的容量大小。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：栈中元素的数量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### func init()

```cangjie
public init()
```

功能：构造一个空的 [ArrayStack](#class-arraystackt)，其初始容量为 8。

### func init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个空的 [ArrayStack](#class-arraystackt)，其初始容量为指定的值。当 capacity 小于默认容量 8 时，构造的 [ArrayStack](#class-arraystackt) 初始容量为 8。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参为负数时，抛出此异常。

### func add(T)

```cangjie
public func add(element: T): Unit
```

功能：在栈顶添加元素。

参数：

- element: T - 添加的元素。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清空当前的 [ArrayStack](#class-arraystackt)。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断此 [ArrayStack](#class-arraystackt) 是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：返回此 [ArrayStack](#class-arraystackt) 中元素的迭代器，其顺序为出栈的顺序。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 栈中元素的迭代器。

### func peek()

```cangjie
public func peek(): ?T
```

功能：获取栈顶的元素，该操作不会做出栈操作，只查看栈顶的元素。当栈为空时，返回 `None`。

返回值：

- ?T - 栈顶的元素。

### func remove()

```cangjie
public func remove(): ?T
```

功能：出栈操作，删除栈顶的元素并且返回这个元素。当栈为空时，返回 `None`。

返回值：

- ?T - 被删除的栈顶元素。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：为当前 [ArrayStack](#class-arraystackt) 扩容相应的空间。当 additional 小于等于零时，不发生扩容；如果当前剩余空间大小大于等于 additional，不进行扩容操作，否则当前 [ArrayStack](#class-arraystackt) 会扩容至 size + additional 大小。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个数组，其中元素为栈中的元素，顺序为栈的出栈顺序。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。