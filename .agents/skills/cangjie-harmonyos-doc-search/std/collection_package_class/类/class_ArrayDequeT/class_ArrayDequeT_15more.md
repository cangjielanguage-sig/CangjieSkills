## class ArrayDeque\<T>

```cangjie
public class ArrayDeque<T> <: Deque<T> {
    public init()
    public init(capacity: Int64)
}
```

功能：ArrayDeque 是双端队列（deque）实现类，可以在双端队列的两端进行元素的插入和删除操作。ArrayDeque 是根据可调整大小的数组实现的，其容量会在插入元素的过程中不断地增长，默认每次扩容 50% 大小。ArrayDeque 的实现采用了循环队列的方式，在没有扩容的情况下，其插入、删除、查看等操作的时间复杂度为 O(1)。

父类型：

- [Deque](./collection_package_interface.md#interface-dequet)\<T>

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：获取此双端队列的容量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop first

```cangjie
public prop first: ?T
```

功能：获取双端队列的头部元素。如果双端队列为空，返回 None。

类型：?T

### prop last

```cangjie
public prop last: ?T
```

功能：获取双端队列的尾部元素。如果双端队列为空，返回 None。

类型：?T

### prop size

```cangjie
public prop size: Int64
```

功能：返回此双端队列中的元素个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个空的双端队列，其容量大小为默认值 8。

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个具有指定容量的双端队列，当 capacity 小于默认容量 8 时，构造的 [ArrayDeque](#class-arraydequet) 初始容量为 8 。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的初始容量。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果参数的大小小于 0 则抛出异常。

### func addFirst(T)

```cangjie
public func addFirst(element: T): Unit
```

功能：在此双端队列头部插入元素。

参数：

- element: T - 被插入到此双端队列的元素。

### func addLast(T)

```cangjie
public func addLast(element: T): Unit
```

功能：在此双端队列尾部插入元素。

参数：

- element: T - 被插入到此双端队列的元素。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清空此双端队列中的所有元素。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断此双端队列是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，则返回 `true`，否则，返回 `false`。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：获取此双端队列中元素的迭代器，其顺序为从前到后的顺序。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 元素的迭代器。

### func removeFirst()

```cangjie
public func removeFirst(): ?T
```

功能：删除双端队列中的头部元素并返回该值，如果此双端队列为空，返回 `None`。

返回值：

- ?T - 被删除的头部元素。

### func removeLast()

```cangjie
public func removeLast(): ?T
```

功能：删除双端队列中的尾部元素并返回该值，如果此双端队列为空，返回 `None`。

返回值：

- ?T - 被删除的尾部元素。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：增加此双端队列的容量。

将双端队列扩容 additional 大小，当 additional 小于等于零时，不发生扩容；当此双端队列剩余容量大于等于 additional 时，不发生扩容；当此双端队列剩余容量小于 additional 时，取（原始容量的 1.5 倍向下取整）与（additional + 已使用容量）两个值中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。