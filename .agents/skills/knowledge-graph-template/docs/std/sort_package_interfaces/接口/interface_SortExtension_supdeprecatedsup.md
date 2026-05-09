## interface SortExtension <sup>(deprecated)</sup>

```cangjie
public interface SortExtension {
    func sort(): Unit
    func sort(stable!: Bool): Unit
    func sortDescending(): Unit
    func sortDescending(stable!: Bool): Unit
}
```

功能：此接口作为排序相关的辅助接口。

### func sort() <sup>(deprecated)</sup>

```cangjie
func sort(): Unit
```

功能：实现对应类型的排序。

> **注意：**
>
> 未来版本即将废弃。

### func sort(Bool) <sup>(deprecated)</sup>

```cangjie
func sort(stable!: Bool): Unit
```

功能：依据传入的参数，实现对应类型的稳定或非稳定排序。

> **注意：**
>
> 未来版本即将废弃。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。

### func sortDescending() <sup>(deprecated)</sup>

```cangjie
func sortDescending(): Unit
```

功能：实现对应类型的降序方式排序。

> **注意：**
>
> 未来版本即将废弃。

### func sortDescending(Bool) <sup>(deprecated)</sup>

```cangjie
func sortDescending(stable!: Bool): Unit
```

功能：依据传入的参数，实现对应类型的稳定或非稳定降序排序。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。

> **注意：**
>
> 未来版本即将废弃。

### extend\<T> Array\<T> <: SortExtension where T <: Comparable\<T> <sup>(deprecated)</sup>

```cangjie
extend<T> Array<T> <: SortExtension where T <: Comparable<T>
```

功能：此扩展用于实现 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 的 `sort/sortDescending` 函数。

> **注意：**
>
> 未来版本即将废弃。

父类型：

- [SortExtension](sort_package_interfaces.md#interface-sortextension-deprecated)

#### func sort() <sup>(deprecated)</sup>

```cangjie
public func sort(): Unit
```

功能：以升序的方式非稳定排序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-bool-bool-where-t--comparablet) 替代。

#### func sort(Bool) <sup>(deprecated)</sup>

```cangjie
public func sort(stable!: Bool): Unit
```

功能：以升序的方式排序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-bool-bool-where-t--comparablet) 替代。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。

#### func sortDescending() <sup>(deprecated)</sup>

```cangjie
public func sortDescending(): Unit
```

功能：以降序的方式排序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-bool-bool-where-t--comparablet) 替代。

#### func sortDescending(Bool) <sup>(deprecated)</sup>

```cangjie
public func sortDescending(stable!: Bool): Unit
```

功能：以降序的方式排序 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。

> **注意：**
>
> 未来版本即将废弃，使用 [sort](sort_package_funcs.md#func-sorttarrayt-bool-bool-where-t--comparablet) 替代。

参数：

- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序。