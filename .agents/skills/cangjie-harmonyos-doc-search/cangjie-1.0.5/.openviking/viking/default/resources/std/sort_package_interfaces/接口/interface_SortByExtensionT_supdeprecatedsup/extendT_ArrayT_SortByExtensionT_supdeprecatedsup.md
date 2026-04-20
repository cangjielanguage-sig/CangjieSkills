### extend\<T> Array\<T> <: SortByExtension\<T> <sup>(deprecated)</sup>

```cangjie
extend<T> Array<T> <: SortByExtension<T>
```

功能：此扩展用于实现 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 的 `sortBy` 函数。

> **注意：**
>
> 未来版本即将废弃。

父类型：

- [SortByExtension](sort_package_interfaces.md#interface-sortbyextensiont-deprecated)

#### func sortBy((T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
public func sortBy(comparator!: (T, T) -> Ordering): Unit
```

功能：通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对数组进行自定义排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-t-t---ordering-bool-bool) 替代。

参数：

- comparator!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 用户传入的比较函数，如，comparator: (t1: T, t2: T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering)，如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 `t1` 在 `t2` 后；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 `t1` 在 `t2` 前；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为稳定排序那么 `t1` 与 `t2` 的位置较排序前保持不变； 如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为不稳定排序，那么 `t1`，`t2` 顺序不确定。

#### func sortBy(Bool, (T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
public func sortBy(stable!: Bool, comparator!: (T, T) -> Ordering): Unit
```

功能：通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对数组进行自定义排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-t-t---ordering-bool-bool) 替代。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。
- comparator!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 用户传入的比较函数，如，comparator: (t1: T, t2: T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering)，如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 `t1` 在 `t2` 后；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 `t1` 在 `t2` 前；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为稳定排序那么 `t1` 与 `t2` 的位置较排序前保持不变； 如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为不稳定排序，那么 `t1`，`t2` 顺序不确定。