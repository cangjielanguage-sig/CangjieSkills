## func sort\<T>(List\<T>, (T, T) -> Ordering, Bool, Bool)

```cangjie
public func sort<T>(data: List<T>, by!: (T, T) -> Ordering, stable!: Bool = false, descending!: Bool = false): Unit
```

功能：对 `List` 按照比较函数进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入自定义的比较函数 `by`。如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 `t1` 在 `t2` 后；如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 `t1` 在 `t2` 前；如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，排序后 `t1` 与 `t2` 的位置与是否是稳定排序有关，稳定则较排序前保持不变，否则有可能发生改变。

参数：

- data: [List](../../collection/collection_package_api/collection_package_interface.md#interface-listt)\<T> - 需要排序的 `List`。
- by!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 传入的比较函数。
- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序，默认为否。
- descending!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用降序排序，默认为否。

## func sort\<T>(List\<T>, Bool, Bool) where T <: Comparable\<T>

```cangjie
public func sort<T>(data: List<T>, stable!: Bool = false, descending!: Bool = false): Unit where T <: Comparable<T>
```

功能：对 `List` 进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

参数：

- data: [List](../../collection/collection_package_api/collection_package_interface.md#interface-listt)\<T> - 需要排序的 `List`。

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序，默认为否。
- descending!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用降序排序，默认为否。

## func stableSort\<T>(Array\<T>) where T <: Comparable\<T> <sup>(deprecated)</sup>

```cangjie
public func stableSort<T>(data: Array<T>): Unit where T <: Comparable<T>
```

功能：对数组进行稳定升序排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-bool-bool-where-t--comparablet) 替代。

参数：

- data: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 需要排序的数组。

## func stableSort\<T>(Array\<T>, (T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
public func stableSort<T>(data: Array<T>, comparator: (T, T) -> Ordering): Unit
```

功能：对数组进行稳定排序。

用户可传入自定义的比较函数 `comparator`，如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 `t1` 在 `t2` 后；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 `t1` 在 `t2` 前；如果 `comparator` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，排序后 `t1` 与 `t2` 的位置较排序前保持不变。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-t-t---ordering-bool-bool) 替代。

参数：

- data: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 需要排序的数组。
- comparator: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 用户传入的比较函数。