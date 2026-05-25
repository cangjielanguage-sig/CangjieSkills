### func remove(Range\<Int64>)

```cangjie
public func remove(range: Range<Int64>): Unit
```

功能：删除此 [ArrayList](collection_package_class.md#class-arraylistt) 中 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 范围所包含的所有元素。

> **注意：**
>
> 如果参数 range 是使用 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，数组切片取到原数组最后一个元素。

参数：

- range: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 需要被删除的元素的范围。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 range 的 [step](collection_package_function.md#func-steptint64) 不等于 1 时抛出异常。
- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 range 的 start 或 end 小于 0，或 end 大于 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 的长度时抛出。

### func removeIf((T) -> Bool)

```cangjie
public func removeIf(predicate: (T) -> Bool): Unit
```

功能：删除此 [ArrayList](collection_package_class.md#class-arraylistt) 中满足给定 lambda 表达式或函数的所有元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递判断删除的条件。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [ArrayList](collection_package_class.md#class-arraylistt) 内元素时，抛出异常。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：增加此 [ArrayList](collection_package_class.md#class-arraylistt) 实例的容量。

将 [ArrayList](collection_package_class.md#class-arraylistt) 扩容 additional 大小，当 additional 小于等于零时，不发生扩容；当 [ArrayList](collection_package_class.md#class-arraylistt) 剩余容量大于等于 additional 时，不发生扩容；当 [ArrayList](collection_package_class.md#class-arraylistt) 剩余容量小于 additional 时，取（原始容量的 1.5 倍向下取整）与（additional + 已使用容量）两个值中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当 additional + 已使用容量超过 Int64.Max 时，抛出异常。

### func reverse()

```cangjie
public func reverse(): Unit
```

功能：反转此 [ArrayList](collection_package_class.md#class-arraylistt) 中元素的顺序。