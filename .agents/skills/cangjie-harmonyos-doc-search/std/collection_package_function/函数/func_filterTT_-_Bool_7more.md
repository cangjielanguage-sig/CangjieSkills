## func filter\<T>((T) -> Bool)

```cangjie
public func filter<T>(predicate: (T) -> Bool): (Iterable<T>) -> Iterator<T>
```

功能：筛选出满足条件的元素。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个筛选函数。

## func filterMap\<T, R>((T) -> ?R)

```cangjie
public func filterMap<T, R>(transform: (T) -> ?R): (Iterable<T>) -> Iterator<R>
```

功能：同时进行筛选操作和映射操作，返回一个新的迭代器。

参数：

- transform: (T) -> ?R - 给定的映射函数。函数返回值为 Some 对应 filter 的 predicate 为 true，反之表示 false。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个筛选和映射的函数。

## func first\<T>(Iterable\<T>)

```cangjie
public func first<T>(it: Iterable<T>): Option<T>
```

功能：获取头部元素。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回头部元素，若为空则返回 None。

## func flatMap\<T, R>((T) -> Iterable\<R>)

```cangjie
public func flatMap<T, R>(transform: (T) -> Iterable<R>): (Iterable<T>) -> Iterator<R>
```

功能：创建一个带 [flatten](collection_package_function.md#func-flattent-riterablet-where-t--iterabler) 功能的映射。

参数：

- transform: (T) -> [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<R> - 给定的映射函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个带 [flatten](collection_package_function.md#func-flattent-riterablet-where-t--iterabler) 功能的映射函数。

## func flatten\<T, R>(Iterable\<T>) where T <: Iterable\<R>

```cangjie
public func flatten<T, R>(it: Iterable<T>): Iterator<R> where T <: Iterable<R>
```

功能：将嵌套的迭代器展开一层。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回展开一层后的迭代器。

## func fold\<T, R>(R, (R, T) -> R)

```cangjie
public func fold<T, R>(initial: R, operation: (R, T) -> R): (Iterable<T>) -> R
```

功能：使用指定初始值，从左向右计算。

参数：

- initial: R - 给定的 R 类型的初始值。
- operation: (R, T) -> R - 给定的计算函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> R - 返回一个折叠函数。

## func forEach\<T>((T) -> Unit)

```cangjie
public func forEach<T>(action: (T) -> Unit): (Iterable<T>) -> Unit
```

功能：遍历所有元素，指定给定的操作。

参数：

- action: (T) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 给定的操作函数。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 返回一个执行遍历操作的函数。