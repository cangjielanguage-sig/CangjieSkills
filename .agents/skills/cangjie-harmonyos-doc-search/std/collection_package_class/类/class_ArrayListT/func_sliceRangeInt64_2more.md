### func slice(Range\<Int64>)

```cangjie
public func slice(range: Range<Int64>): ArrayList<T>
```

功能：以传入参数 range 作为索引，返回索引对应的 [ArrayList](collection_package_class.md#class-arraylistt)\<T>。

> **注意：**
>
> 如果参数 range 是使用 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>
> 1. start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
> 2. hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，该数组切片取到原数组最后一个元素。

参数：

- range: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 传递切片的范围。

返回值：

- [ArrayList](collection_package_class.md#class-arraylistt)\<T> - 切片所得的数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 range.[step](collection_package_function.md#func-steptint64) 不等于 1 时，抛出异常。
- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 range 无效时，抛出异常。

示例：

使用示例见 [ArrayList 的 remove/clear/slice 函数](../collection_package_samples/sample_arraylist_remove_clear_slice.md)。

### func sortBy((T, T) -> Ordering) <sup>(deprecated)</sup>

```cangjie
public func sortBy(comparator!: (T, T) -> Ordering): Unit
```

功能：对数组中的元素进行非稳定排序。

通过传入的比较函数，根据其返回值 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型的结果，可对数组进行自定义排序 comparator: (t1: T, t2: T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering)，如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 t1 在 t2 后；如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 t1 在 t2 前；如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为稳定排序，那么 t1 在 t2 之前； 如果 comparator 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，且为不稳定排序，那么 t1，t2 顺序不确定。
> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。

参数：

- comparator!: (T, T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - (T, T) -> [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 类型。