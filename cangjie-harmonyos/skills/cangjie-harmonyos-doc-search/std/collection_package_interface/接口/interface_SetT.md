## interface Set\<T>

```cangjie
public interface Set<T> <: ReadOnlySet<T> {
    func add(element: T): Bool
    func add(all!: Collection<T>): Unit
    func remove(element: T): Bool
    func remove(all!: Collection<T>): Unit
    func removeIf(predicate: (T) -> Bool): Unit
    func clear(): Unit
    func retain(all!: Set<T>): Unit
}
```

功能：[Set](collection_package_interface.md#interface-sett) 接口提供了一组集合的相关操作，允许我们以可读写的方式操作内部元素。

[Set](collection_package_interface.md#interface-sett) 接口不规定内部的实现方式，在 [Set](collection_package_interface.md#interface-sett) 接口的实例中，其内部的元素通常是无序的，不能通过索引访问，也不能保证元素的插入顺序。

父类型：

- [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T>

### func add(Collection\<T>)

```cangjie
func add(all!: Collection<T>): Unit
```

功能：添加 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素至此 [Set](collection_package_interface.md#interface-sett) 中，如果元素存在，则不添加。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要被添加的元素的集合。

### func add(T)

```cangjie
func add(element: T): Bool
```

功能：添加元素操作。如果元素已经存在，则不会添加它。

参数：

- element: T - 要添加的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果添加成功，则返回 true；否则，返回 false。

### func clear()

```cangjie
func clear(): Unit
```

功能：清除所有键值对。

### func remove(Collection\<T>)

```cangjie
func remove(all!: Collection<T>): Unit
```

功能：移除此 [Set](collection_package_interface.md#interface-sett) 中那些也包含在指定 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont) 中的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 传入 [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>。

### func remove(T)

```cangjie
func remove(element: T): Bool
```

功能：从该集合中移除指定元素（如果存在）。

参数：

- element: T - 要删除的元素。

返回值：

- Bool - 集合中存在指定的元素并且删除成功返回 `true`，否则返回 `false` 。

### func removeIf((T) -> Bool)

```cangjie
func removeIf(predicate: (T) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足 `true` 条件，则删除对应的元素。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入一个 lambda 表达式进行判断。

### func retain(Set\<T>)

```cangjie
func retain(all!: Set<T>): Unit
```

功能：仅保留该 [Set](collection_package_interface.md#interface-sett) 与入参 [Set](collection_package_interface.md#interface-sett) 中重复的元素。

参数：

- all!: [Set](collection_package_interface.md#interface-sett)\<T> - 要保存的元素集合。