## func collectHashSet\<T>(Iterable\<T>) where T <: Hashable & Equatable\<T>

```cangjie
public func collectHashSet<T>(it: Iterable<T>): HashSet<T> where T <: Hashable & Equatable<T>
```

功能：将一个迭代器转换成 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet) 类型。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - 返回一个 [HashSet](collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。

## func collectString\<T>(String) where T <: ToString

```cangjie
public func collectString<T>(delimiter!: String = ""): (Iterable<T>) -> String where T <: ToString
```

功能：将一个对应元素实现了 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口的迭代器转换成 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型。

参数：

- delimiter!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串拼接分隔符。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [String](../../core/core_package_api/core_package_structs.md#struct-string) - 返回一个转换函数。

## func concat\<T>(Iterable\<T>)

```cangjie
public func concat<T>(other: Iterable<T>): (Iterable<T>) -> Iterator<T>
```

功能：串联两个迭代器。

参数：

- other: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 要串联在后面的迭代器。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个串联函数。

## func contains\<T>(T) where T <: Equatable\<T>

```cangjie
public func contains<T>(element: T): (Iterable<T>) -> Bool where T <: Equatable<T>
```

功能：获得一个针对特定元素的查找函数。

参数：

- element: T - 要查找的元素。

返回值：

- ([Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回一个查找函数。

示例：

<!-- verify -->
```cangjie
import std.collection.*

main() {
    var searchFunc = contains<Int64>(6) // 获得查找元素 6 的函数
    let arr = ArrayList.of([1, 2, 3, 4, 5, 6])
    let i = arr.iterator()
    var result = searchFunc(i) // 调用函数
    println(result)
    searchFunc = contains<Int64>(7) // 获得查找元素 7 的函数
    result = searchFunc(i) // 调用函数
    println(result)
    return 0
}
```

运行结果：

```text
true
false
```

## func count\<T>(Iterable\<T>)

```cangjie
public func count<T>(it: Iterable<T>): Int64
```

功能：统计迭代器包含元素数量。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回迭代器包含元素数量。

## func enumerate\<T>(Iterable\<T>)

```cangjie
public func enumerate<T>(it: Iterable<T>): Iterator<(Int64, T)>
```

功能：用于获取带索引的迭代器。

参数：

- it: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 给定的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<([Int64](../../core/core_package_api/core_package_intrinsics.md#int64), T)> - 返回一个带索引的迭代器。