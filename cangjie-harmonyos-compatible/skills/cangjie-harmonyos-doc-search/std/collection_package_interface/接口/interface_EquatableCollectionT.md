## interface EquatableCollection\<T>

```cangjie
public interface EquatableCollection<T> <: Collection<T> {
    func contains(element: T): Bool
    func contains(all!: Collection<T>): Bool
}
```

功能：定义了可以进行比较的集合类型。

父类型：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T>

### func contains(Collection\<T>)

```cangjie
func contains(all!: Collection<T>): Bool
```

功能：判断 Keys 是否包含指定集合的所有元素。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 待判断的集合 all。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 包含则返回 true，否则返回 false。

### func contains(T)

```cangjie
func contains(element: T): Bool
```

功能：判断 Keys 是否包含指定元素。

参数：

- element: T - 指定元素，待判断 Keys 是否包含该元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 包含返回 true，否则返回 false。