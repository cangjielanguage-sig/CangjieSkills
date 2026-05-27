## class LazySeq\<T>

```cangjie
public class LazySeq<T> <: Iterable<T> {
    public init()
    public init(element: T) 
}
```

功能：延迟计算的 T 类型值序列。用于在迭代时计算和记忆值。
这是完全不可变的，每次操作都会产生一个新的序列。

父类型：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>

### init()

```cangjie
public init()
```

功能：构造器。

### init(T)

```cangjie
public init(element: T)
```

功能：构造器。

参数：

- element: T - 初始元素。

### func append(T)

```cangjie
public func append(element: T): LazySeq<T>
```

功能：增加一个元素。

参数：

- element: T - 被增加的元素。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 增加元素后的序列。

### func concat(LazySeq\<T>)

```cangjie
public func concat(other: LazySeq<T>): LazySeq<T>
```

功能：增加一个序列到此序列中。复杂度为 O(1) 。

参数：

- other: [LazySeq](#class-lazyseqt)\<T> - 被增加的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 增加元素后的序列。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：实现序列的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 序列迭代器。

### func map\<U>((T) -> U)

```cangjie
public func map<U>(body: (T) -> U): LazySeq<U>
```

功能：对序列中的每个元素执行闭包处理。

参数：

- body: (T) -> U - 对每个元素执行的闭包。

返回值：

- [LazySeq](#class-lazyseqt)\<U> - 处理后的序列。

### func mixWith(LazySeq\<T>)

```cangjie
public func mixWith(other: LazySeq<T>): LazySeq<T>
```

功能：将新序列穿插进原序列中。

例如：{1,2,3,4}.mixWith({5,6,7}) -> {1,5,2,6,3,7,4}

参数：

- other: [LazySeq](#class-lazyseqt)\<T> - 待插入的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### func prepend(T)

```cangjie
public func prepend(element: T): LazySeq<T>
```

功能：将新序列插进原序列的开头。

参数：

- other: [LazySeq](#class-lazyseqt)\<T> - 待插入的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### static func mix(LazySeq\<T>,LazySeq\<T>)

```cangjie
public static func mix(l1: LazySeq<T>, l2: LazySeq<T>): LazySeq<T>
```

功能：两个序列穿插混合成一个。

例如：mix({1,2,3,4}, {5,6,7}) -> {1,5,2,6,3,7,4}

参数：

- l1: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l2: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### static func mix(LazySeq\<T>,LazySeq\<T>,LazySeq\<T>)

```cangjie
public static func mix(l1: LazySeq<T>, l2: LazySeq<T>, l3: LazySeq<T>): LazySeq<T>
```

功能：三个序列穿插混合成一个。

参数：

- l1: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l2: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l3: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。

### static func mix(LazySeq\<T>,LazySeq\<T>,LazySeq\<T>,LazySeq\<T>)

```cangjie
public static func mix(l1: LazySeq<T>, l2: LazySeq<T>, l3: LazySeq<T>, l4: LazySeq<T>): LazySeq<T>
```

功能：四个序列穿插混合成一个。

参数：

- l1: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l2: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l3: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。
- l4: [LazySeq](#class-lazyseqt)\<T> - 待穿插的序列。

返回值：

- [LazySeq](#class-lazyseqt)\<T> - 处理后的序列。