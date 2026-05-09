### func get(Int64)

```cangjie
public func get(index: Int64): ?T
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 中指定位置的元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要返回的元素的索引。

返回值：

- ?T - 返回指定位置的元素，如果 index 大小小于 0 或者大于等于 [ArrayList](collection_package_class.md#class-arraylistt) 中的元素数量，返回 None。

示例：

使用示例见 [ArrayList 的 get/set 函数](../collection_package_samples/sample_arraylist_get_set.md)。

### func getRawArray()

```cangjie
public unsafe func getRawArray(): Array<T>
```

功能：返回 [ArrayList](collection_package_class.md#class-arraylistt) 的原始数据。

> **注意：**
>
> 这是一个 unsafe 的接口，使用处需要在 unsafe 上下文中。
>
> 原始数据是指 [ArrayList](collection_package_class.md#class-arraylistt) 底层实现的数组，其大小大于等于 [ArrayList](collection_package_class.md#class-arraylistt) 中的元素数量，且索引大于等于 [ArrayList](collection_package_class.md#class-arraylistt) 大小的位置中可能包含有未初始化的元素，对其进行访问可能会产生未定义的行为。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - [ArrayList](collection_package_class.md#class-arraylistt) 的底层原始数据。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [ArrayList](collection_package_class.md#class-arraylistt) 是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，则返回 `true`，否则，返回 `false`。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 中元素的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - [ArrayList](collection_package_class.md#class-arraylistt) 中元素的迭代器。

### func remove(Int64)

```cangjie
public func remove(at!: Int64): T
```

功能：删除此 [ArrayList](collection_package_class.md#class-arraylistt) 中指定位置的元素。

参数：

- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 被删除元素的索引。

返回值：

- T - 被移除的元素。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 at 超出范围时，抛出异常。

示例：

使用示例见 [ArrayList 的 remove/clear/slice 函数](../collection_package_samples/sample_arraylist_remove_clear_slice.md)。