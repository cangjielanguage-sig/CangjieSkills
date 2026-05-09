## func inspect\<T>((T) -> Unit)

```cangjie
public func inspect<T>(action: (T)->Unit): (Iterable<T>) ->Iterator<T>
```

功能：迭代器每次调用 next() 对当前元素执行额外操作（不会消耗迭代器中元素）。

参数：

- action: (T) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 给定的操作函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个能对迭代器每个元素执行额外操作的函数。

## func isEmpty\<T>(Iterable\<T>)

```cangjie
public func isEmpty<T>(it: Iterable<T>): Bool
```

功能：判断迭代器是否为空。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回迭代器是否为空。

## func last\<T>(Iterable\<T>)

```cangjie
public func last<T>(it: Iterable<T>): Option<T>
```

功能：获取尾部元素。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回尾部元素，若为空则返回 None。

## func map\<T, R>((T) -> R)

```cangjie
public func map<T, R>(transform: (T) -> R): (Iterable<T>) -> Iterator<R>
```

功能：创建一个映射。

参数：

- transform: (T) ->R - 给定的映射函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个映射函数。

## func max\<T>(Iterable\<T>) where T <: Comparable\<T>

```cangjie
public func max<T>(it: Iterable<T>): Option<T> where T <: Comparable<T>
```

功能：筛选最大的元素。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回最大的元素，若为空则返回 None。

## func min\<T>(Iterable\<T>) where T <: Comparable\<T>

```cangjie
public func min<T>(it: Iterable<T>): Option<T> where T <: Comparable<T>
```

功能：筛选最小的元素。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回最小的元素，若为空则返回 None。

## func none\<T>((T) -> Bool)

```cangjie
public func none<T>(predicate: (T) -> Bool): (Iterable<T>) -> Bool
```

功能：判断迭代器中所有元素是否都不满足条件。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回一个判断都不满足条件的函数。

## func reduce\<T>((T, T) -> T)

```cangjie
public func reduce<T>(operation: (T, T) -> T): (Iterable<T>) -> Option<T>
```

功能：使用第一个元素作为初始值，从左向右计算。

参数：

- operation: (T, T) -> T - 给定的操作函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回一个归并函数。