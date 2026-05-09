### func sortBy(Bool, (T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
public func sortBy(stable!: Bool, comparator!: (T, T) -> Ordering): Unit
```

功能：对数组中的元素进行排序。

通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对数组进行自定义排序 comparator: (t1: T, t2: T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering)，如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 t1 在 t2 后；如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 t1 在 t2 前；如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为稳定排序，那么 t1 在 t2 之前； 如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为不稳定排序，那么 t1，t2 顺序不确定。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。
- comparator!: (T, T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - (T, T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型。

### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：返回一个数组，其中包含此列表中按正确顺序排列的所有元素。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - T 类型数组。

### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): T
```

功能：操作符重载 - get。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 表示 get 接口的索引。

返回值：

- T - 索引位置的元素的值。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 index 超出范围时，抛出异常。

### operator func \[](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

功能：操作符重载，通过下标运算符用指定的元素替换此列表中指定位置的元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要设置的索引值。
- value!: T - 要设置的 T 类型的值。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 index 超出范围时，抛出异常。