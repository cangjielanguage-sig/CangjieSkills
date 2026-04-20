## interface SortByExtension\<T> <sup>(deprecated)</sup>

```cangjie
public interface SortByExtension<T> {
    func sortBy(comparator!: (T, T) -> Ordering): Unit
    func sortBy(stable!: Bool, comparator!: (T, T) -> Ordering): Unit
}
```

功能：此接口作为排序相关的辅助接口，通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对 T 进行自定义排序。

> **注意：**
>
> 未来版本即将废弃。

### func sortBy((T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
func sortBy(comparator!: (T, T) -> Ordering): Unit
```

功能：通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对 T 进行自定义排序。

> **注意：**
>
> 未来版本即将废弃。

参数：

- comparator!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 用户传入的比较函数。

### func sortBy(Bool, (T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
func sortBy(stable!: Bool, comparator!: (T, T) -> Ordering): Unit
```

功能：通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果和稳定排序标志位，可对 T 进行自定义排序。

> **注意：**
>
> 未来版本即将废弃。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。
- comparator!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 用户传入的比较函数。

> **注意：**
>
> 未来版本即将废弃。