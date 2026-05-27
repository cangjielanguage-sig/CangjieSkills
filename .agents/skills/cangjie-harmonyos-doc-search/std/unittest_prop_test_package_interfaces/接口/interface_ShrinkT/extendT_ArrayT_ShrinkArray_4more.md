### extend\<T> Array\<T> <: Shrink\<Array\<T>>

```cangjie
extend<T> Array<T> <: Shrink<Array<T>>
```

功能：为 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 实现了 [Shrink](#interface-shrinkt)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T>> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T>>

#### func shrink()

```cangjie
func shrink(): Iterable<Array<T>>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Array\<T>> - 一组可能的“较小”值的迭代器。

### extend\<T> Option\<T> <: Shrink\<Option\<T>>

```cangjie
extend<T> Option<T> <: Shrink<Option<T>>
```

功能：为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> 实现了 [Shrink](#interface-shrinkt)\<[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>>

#### func shrink()

```cangjie
func shrink(): Iterable<Option<T>>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Option\<T>> - 一组可能的“较小”值的迭代器。

### extend\<T> ArrayList\<T> <: Shrink\<ArrayList\<T>>

```cangjie
extend<T> ArrayList<T> <: Shrink<ArrayList<T>>
```

功能：为 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T> 实现了 [Shrink](#interface-shrinkt)\<[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T>> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T>>

#### func shrink()

```cangjie
func shrink(): Iterable<ArrayList<T>>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<ArrayList\<T>> - 一组可能的“较小”值的迭代器。

### extend\<T> HashSet\<T> <: Shrink\<HashSet\<T>>

```cangjie
extend<T> HashSet<T> <: Shrink<HashSet<T>>
```

功能：为 [HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 实现了 [Shrink](#interface-shrinkt)\<[HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>>

#### func shrink()

```cangjie
func shrink(): Iterable<HashSet<T>>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<HashSet\<T>> - 一组可能的“较小”值的迭代器。