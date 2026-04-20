### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：使用传入的容量构造一个 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于 0，抛出异常。

### init(Int64, (Int64) -> T)

```cangjie
public init(size: Int64, initElement: (Int64) -> T)
```

功能：通过传入的函数元素个数 size 和函数规则来构造 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。构造出的 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 的容量受 size 大小影响。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化函数中元素的个数。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) ->T - 初始化函数规则。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0，抛出异常。

### func add(Collection\<T>)

```cangjie
public func add(all!: Collection<T>): Unit
```

功能：添加 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素至此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中，如果元素存在，则不添加。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要被添加的元素的集合。

### func add(T)

```cangjie
public func add(element: T): Bool
```

功能：将指定的元素添加到 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中，若添加的元素在 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中存在，则添加失败。

参数：

- element: T - 指定的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果添加成功，则返回 true；否则，返回 false。

示例：

使用示例见 [HashSet 的 add/iterator/remove 函数](../collection_package_samples/sample_hashset_add_iterator_remove.md)。

### func clear()

```cangjie
public func clear(): Unit
```

功能：从此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中移除所有元素。

### func clone()

```cangjie
public func clone(): HashSet<T>
```

功能：克隆 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。

返回值：

- [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - 返回克隆到的 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。