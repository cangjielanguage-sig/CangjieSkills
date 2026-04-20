### extend\<T> ArrayList\<T> <: SortExtension where T <: Comparable\<T> <sup>(deprecated)</sup>

```cangjie
extend<T> ArrayList<T> where T <: Comparable<T>
```

功能：为 [ArrayList](./collection_package_class.md#class-arraylistt)\<T> 扩展 [SortExtension](../../sort/sort_package_api/sort_package_interfaces.md#interface-sortextension-deprecated) 接口，支持数组排序。

> **注意：**
>
> 未来版本即将废弃。

父类型：

- [SortExtension](../../sort/sort_package_api/sort_package_interfaces.md#interface-sortextension-deprecated)

#### func sort() <sup>(deprecated)</sup>

```cangjie
public func sort(): Unit
```

功能：将当前数组内元素以升序的方式非稳定排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。

#### func sort(Bool) <sup>(deprecated)</sup>

```cangjie
public func sort(stable!: Bool): Unit
```

功能：将当前数组内元素以升序的方式排序。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。

#### func sortDescending() <sup>(deprecated)</sup>

```cangjie
public func sortDescending(): Unit
```

功能：将当前数组内元素以降序的方式非稳定排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。

#### func sortDescending(Bool) <sup>(deprecated)</sup>

```cangjie
public func sortDescending(stable!: Bool): Unit
```

功能：将当前数组内元素以降序的方式排序。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](../../sort/sort_package_api/sort_package_funcs.md#func-sorttlistt-bool-bool-where-t--comparablet) 替代。