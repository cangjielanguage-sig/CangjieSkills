## interface ReadOnlySet\<T>

```cangjie
public interface ReadOnlySet<T> <: Collection<T> {
    func contains(element: T): Bool
    func contains(all!: Collection<T>): Bool
    func subsetOf(other: ReadOnlySet<T>): Bool
}
```

功能：[ReadOnlySet](collection_package_interface.md#interface-readonlysett) 接口提供了一组集合的相关操作，允许我们以只读方式操作内部元素。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### func contains(Collection\<T>)

```cangjie
func contains(all!: Collection<T>): Bool
```

功能：检查该集合是否包含其他集合。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 其他集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该集合包含指定集合，则返回 true；否则，返回 false。

### func contains(T)

```cangjie
func contains(element: T): Bool
```

功能：如果该集合包含指定元素，则返回 true。

参数：

- element: T - 需要判断的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果包含，则返回 true；否则，返回 false。

### func subsetOf(ReadOnlySet\<T>)

```cangjie
func subsetOf(other: ReadOnlySet<T>): Bool
```

功能：检查该集合是否为其他集合的子集。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 其他集合。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 果该集合是指定集合的子集，则返回 true；否则，返回 false。