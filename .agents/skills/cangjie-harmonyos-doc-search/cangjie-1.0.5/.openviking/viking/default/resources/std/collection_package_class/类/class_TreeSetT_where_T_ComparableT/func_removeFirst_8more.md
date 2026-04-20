### func removeFirst()

```cangjie
public func removeFirst(): ?T
```

功能：删除 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的第一个元素。

返回值：

- ?T - 如果存在第一个元素，那么删除该元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### func removeIf((T) -> Bool)

```cangjie
public func removeIf(predicate: (T) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足 `true` 条件，则删除对应的元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否删除元素的判断条件。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 内元素时，抛出异常。

### func removeLast()

```cangjie
public func removeLast(): ?T
```

功能：删除 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 的最后一个元素。

返回值：

- ?T - 如果存在最后一个元素，那么删除该元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### func retain(Set\<T>)

```cangjie
public func retain(all!: Set<T>): Unit
```

功能：从此 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 中保留 [Set](collection_package_interface.md#interface-sett) 中的元素，其他元素将被移除。

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

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet) 是指定 [ReadOnlySet](collection_package_interface.md#interface-readonlysett) 的子集，则返回 true；否则返回 false。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个包含容器内所有元素的数组。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。

### operator func &(ReadOnlySet\<T>)

```cangjie
public operator func &(other: ReadOnlySet<T>): TreeSet<T>
```

功能：返回包含两个集合交集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - T 类型集合。

### operator func -(ReadOnlySet\<T>)

```cangjie
public operator func -(other: ReadOnlySet<T>): TreeSet<T>
```

功能：返回包含两个集合差集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - T 类型集合。