## func all\<T>((T) -> Bool)

```cangjie
public func all<T>(predicate: (T) -> Bool): (Iterable<T>) -> Bool
```

功能：判断迭代器所有元素是否都满足条件。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回一个判断全部满足条件的函数。

## func any\<T>((T) -> Bool)

```cangjie
public func any<T>(predicate: (T) -> Bool): (Iterable<T>) -> Bool
```

功能：判断迭代器是否存在任意一个满足条件的元素。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回一个判断存在任意一个满足条件的函数。

## func at\<T>(Int64)

```cangjie
public func at<T>(n: Int64): (Iterable<T>) -> Option<T>
```

功能：获取迭代器指定位置的元素。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 给定的个数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回获取对应位置元素的函数，若迭代器为空则该函数返回 None。

## func collectArray\<T>(Iterable\<T>)

```cangjie
public func collectArray<T>(it: Iterable<T>): Array<T>
```

功能：将一个迭代器转换成 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 类型。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 返回一个数组。

## func collectArrayList\<T>(Iterable\<T>)

```cangjie
public func collectArrayList<T>(it: Iterable<T>): ArrayList<T>
```

功能：将一个迭代器转换成 [ArrayList](collection_package_class.md#class-arraylistt) 类型。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [ArrayList](collection_package_class.md#class-arraylistt)\<T> - 返回一个 [ArrayList](collection_package_class.md#class-arraylistt)。

## func collectHashMap\<K, V>(Iterable\<(K, V)>) where K <: Hashable & Equatable\<K>

```cangjie
public func collectHashMap<K, V>(it: Iterable<(K, V)>): HashMap<K, V> where K <: Hashable & Equatable<K>
```

功能：将一个迭代器转换成 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 类型。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<(K, V)> - 给定的迭代器。

返回值：

- [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<K, V> - 返回一个 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。