## interface List\<T>

```cangjie
public interface List<T> <: ReadOnlyList<T> {
    func add(element: T): Unit
    func add(all!: Collection<T>): Unit
    func add(element: T, at!: Int64): Unit
    func add(all!: Collection<T>, at!: Int64): Unit
    func remove(at!: Int64): T
    func remove(range: Range<Int64>): Unit
    func removeIf(predicate: (T) -> Bool): Unit
    func clear(): Unit

    operator func [](index: Int64, value!: T): Unit
}
```

功能：定义了只提供对索引友好操作的列表类型。

父类型：

- [ReadOnlyList](#interface-readonlylistt)\<T>

### func add(Collection\<T>)

```cangjie
func add(all!: Collection<T>): Unit
```

功能：将指定集合中的所有元素附加到此列表的末尾。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要插入的元素的集合。

### func add(Collection\<T>, Int64)

```cangjie
func add(all!: Collection<T>, at!: Int64): Unit
```

功能：从指定位置开始，将指定集合中的所有元素插入此列表。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 要插入的 T 类型元素集合。
- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 插入集合的目标索引。

### func add(T)

```cangjie
func add(element: T): Unit
```

功能：将指定的元素附加到此列表的末尾。

参数：

- element: T - 插入的元素，类型为 T。

### func add(T, Int64)

```cangjie
func add(element: T, at!: Int64): Unit
```

功能：在此列表中的指定位置插入指定元素。

参数：

- element: T - 要插入的 T 类型元素。
- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 插入元素的目标索引。

### func clear()

```cangjie
func clear(): Unit
```

功能：从此列表中删除所有元素。

### func remove(Int64)

```cangjie
func remove(at!: Int64): T
```

功能：删除此列表中指定位置的元素。

参数：

- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 被删除元素的索引。

返回值：

- T - 被移除的元素。

### func remove(Range\<Int64>)

```cangjie
func remove(range: Range<Int64>): Unit
```

功能：删除此列表中 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 范围所包含的所有元素。

参数：

- range: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 需要被删除的元素的范围。

### func removeIf((T) -> Bool)

```cangjie
func removeIf(predicate: (T) -> Bool): Unit
```

功能：删除此列表中满足给定 lambda 表达式或函数的所有元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递判断删除的条件。

### operator func \[](Int64, T)

```cangjie
operator func [](index: Int64, value!: T): Unit
```

功能：操作符重载 - set，通过下标运算符用指定的元素替换此列表中指定位置的元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要设置的索引值。
- value!: T - 要设置的 T 类型的值。