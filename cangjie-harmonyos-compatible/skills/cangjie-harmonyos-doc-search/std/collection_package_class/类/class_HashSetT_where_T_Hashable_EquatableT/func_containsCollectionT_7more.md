### func contains(Collection\<T>)

```cangjie
public func contains(all!: Collection<T>): Bool
```

功能：判断 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 是否包含指定 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 指定的元素集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 包含 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素，则返回 true；否则，返回 false。

### func contains(T)

```cangjie
public func contains(element: T): Bool
```

功能：判断 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 是否包含指定元素。

参数：

- element: T - 指定的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果包含指定元素，则返回 true；否则，返回 false。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果为空，则返回 true；否则，返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：返回此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的迭代器。

示例：

使用示例见 [HashSet 的 add/iterator/remove 函数](../collection_package_samples/sample_hashset_add_iterator_remove.md)。

### func remove(Collection\<T>)

```cangjie
public func remove(all!: Collection<T>): Unit
```

功能：移除此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中那些也包含在指定 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要从此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中移除的元素的集合。

### func remove(T)

```cangjie
public func remove(element: T): Bool
```

功能：如果指定元素存在于此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中，则将其移除。

参数：

- element: T - 需要被移除的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，表示移除成功；false，表示移除失败。

示例：

使用示例见 [HashSet 的 add/iterator/remove 函数](../collection_package_samples/sample_hashset_add_iterator_remove.md)。

### func removeIf((T) -> Bool)

```cangjie
public func removeIf(predicate: (T) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足 `true` 条件，则删除对应的元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否删除元素的判断条件。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 内元素时，抛出异常。