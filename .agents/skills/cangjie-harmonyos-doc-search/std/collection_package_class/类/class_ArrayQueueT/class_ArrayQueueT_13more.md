## class ArrayQueue\<T>

```cangjie
public class ArrayQueue<T> <: Queue<T> {
    public init()
    public init(capacity: Int64)
}
```

功能：基于数组实现的循环队列数据结构。

父类型：

- [Queue](./collection_package_interface.md#interface-queuet)\<T>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：获取此队列的容量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：返回此队列中的元素个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的队列，其容量大小为默认值 8。

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个具有指定容量的队列，当 capacity 小于默认容量 8 时，构造的 [ArrayQueue](#class-arrayqueuet) 初始容量为 8 。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的初始容量。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果参数的大小小于 0 则抛出异常。

### func add(T)

```cangjie
public func add(element: T): Unit
```

功能：在此队列尾部插入元素。

参数：

- element: T - 被插入到此双端队列的元素。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清空此队列中的所有元素。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断此队列是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，则返回 `true`，否则，返回 `false`。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：获取此队列中元素的迭代器，其顺序为从前到后的顺序。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 元素的迭代器。

### func peek()

```cangjie
public func peek():?T
```

功能：查看此队列头部元素。此操作不会删除元素。

返回值：

- ?T - 队列的头部元素，如果队列为空，返回`None`。

### func remove()

```cangjie
public func remove(): ?T
```

功能：删除队列中的头部元素并返回该值，如果此队列为空，返回 `None`。

返回值：

- ?T - 被删除的头部元素。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：增加此队列的容量。

将队列扩容 additional 大小，当 additional 小于等于零时，不发生扩容；当此队列剩余容量大于等于 additional 时，不发生扩容；当此队列剩余容量小于 additional 时，取（原始容量的 1.5 倍向下取整）与（additional + 已使用容量）两个值中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个数组，其包含此队列中的所有元素，且顺序为从前到后的顺序。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。