### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：将 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 扩容 additional 大小，当 additional 小于等于零时，不发生扩容；当 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 剩余容量大于等于 additional 时，不发生扩容；当 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 剩余容量小于 additional 时，取（原始容量的 1.5 倍向下取整）与（additional + 已使用容量）中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当 additional + 已使用容量超过 Int64.Max 时，抛出异常。

### func retain(Set\<T>)

```cangjie
public func retain(all!: Set<T>): Unit
```

功能：从此 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 中保留 [Set](collection_package_interface.md#interface-sett) 中的元素。

参数：

- all!: [Set](collection_package_interface.md#interface-sett)\<T> - 需要保留的 [Set](collection_package_interface.md#interface-sett)。

### func subsetOf(ReadOnlySet\<T>)

```cangjie
public func subsetOf(other: ReadOnlySet<T>): Bool
```

功能：检查该集合是否为其他 [ReadOnlySet](collection_package_interface.md#interface-readonlysett) 的子集。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合，此函数将判断当前集合是否为 other 的子集。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [Set](collection_package_interface.md#interface-sett) 是指定 [ReadOnlySet](collection_package_interface.md#interface-readonlysett) 的子集，则返回 true；否则返回 false。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个包含容器内所有元素的数组。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。

### operator func &(ReadOnlySet\<T>)

```cangjie
public operator func &(other: ReadOnlySet<T>): HashSet<T>
```

功能：返回包含两个集合交集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - T 类型集合。

### operator func -(ReadOnlySet\<T>)

```cangjie
public operator func -(other: ReadOnlySet<T>): HashSet<T>
```

功能：返回包含两个集合差集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - T 类型集合。

### operator func |(ReadOnlySet\<T>)

```cangjie
public operator func |(other: ReadOnlySet<T>): HashSet<T>
```

功能：返回包含两个集合并集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - T 类型集合。