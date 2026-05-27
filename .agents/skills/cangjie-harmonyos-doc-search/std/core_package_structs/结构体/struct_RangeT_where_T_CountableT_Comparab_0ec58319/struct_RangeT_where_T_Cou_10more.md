## struct Range\<T> where T <: Countable\<T> & Comparable\<T> & Equatable\<T>

```cangjie
public struct Range<T> <: Iterable<T> where T <: Countable<T> & Comparable<T> & Equatable<T> {
    public let end: T
    public let hasEnd: Bool
    public let hasStart: Bool
    public let isClosed: Bool
    public let start: T
    public let step: Int64
    public const init(start: T, end: T, step: Int64, hasStart: Bool, hasEnd: Bool, isClosed: Bool)
}
```

功能：该类是区间类型，用于表示一个拥有固定范围和步长的 `T` 的序列，要求 `T` 是可数的，有序的。

区间类型有对应的字面量表示，其格式为：

- 左闭右开区间：`start..end : step`，它表示一个从 start 开始，以 [step](#let-step) 为步长，到 end（不包含 end）为止的区间。
- 左闭右闭区间：`start..=end : step`，它表示一个从 start 开始，以 [step](#let-step) 为步长，到 end（包含 end）为止的区间。

> **注意：**
>
> - 当 [step](#let-step) > 0 且 start >= end，或者 [step](#let-step) < 0 且 start <= end 时，该 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例将是一个空区间。
> - 当 [step](#let-step) > 0 且 start > end，或者 [step](#let-step) < 0 且 start < end 时，该 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例将是一个空区间。

父类型：

- [Iterable](core_package_interfaces.md#interface-iterablee)\<T>

### let end

```cangjie
public let end: T
```

功能：表示结束值。

类型：T

### let hasEnd

```cangjie
public let hasEnd: Bool
```

功能：表示是否包含结束值。

类型：[Bool](core_package_intrinsics.md#bool)

### let hasStart

```cangjie
public let hasStart: Bool
```

功能：表示是否包含开始值。

类型：[Bool](core_package_intrinsics.md#bool)

### let isClosed

```cangjie
public let isClosed: Bool
```

功能：表示区间开闭情况，为 true 表示左闭右闭，为 false 表示左闭右开。

类型：[Bool](core_package_intrinsics.md#bool)

### let start

```cangjie
public let start: T
```

功能：表示开始值。

类型：T

### let step

```cangjie
public let step: Int64
```

功能：表示步长。

类型：[Int64](core_package_intrinsics.md#int64)

### init(T, T, Int64, Bool, Bool, Bool)

```cangjie
public const init(start: T, end: T, step: Int64, hasStart: Bool, hasEnd: Bool, isClosed: Bool)
```

功能：使用该构造函数创建 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 序列。

参数：

- start: T - 开始值。
- end: T - 结束值。
- [step](#let-step): [Int64](core_package_intrinsics.md#int64) - 步长，取值不能为 0。
- hasStart: [Bool](core_package_intrinsics.md#bool) - 是否有开始值。
- hasEnd: [Bool](core_package_intrinsics.md#bool) - 是否有结束值。
- isClosed: [Bool](core_package_intrinsics.md#bool) - true 代表左闭右闭，false 代表左闭右开。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当 [step](#let-step) 等于 0 时，抛出异常。

### func isEmpty()

```cangjie
public const func isEmpty(): Bool
```

功能：判断该区间是否为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果为空，返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：获取当前区间的迭代器。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<T> - 当前区间的迭代器。