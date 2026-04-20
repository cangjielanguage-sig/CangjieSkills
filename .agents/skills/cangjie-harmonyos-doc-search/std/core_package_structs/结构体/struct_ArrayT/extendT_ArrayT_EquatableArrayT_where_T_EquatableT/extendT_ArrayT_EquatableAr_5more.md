### extend\<T> Array\<T> <: Equatable\<Array\<T>> where T <: Equatable\<T>

```cangjie
extend<T> Array<T> <: Equatable<Array<T>> where T <: Equatable<T>
```

功能：为 [Array](core_package_structs.md#struct-arrayt)\<T> 类型扩展 [Equatable](core_package_interfaces.md#interface-equatablet)\<[Array](core_package_structs.md#struct-arrayt)\<T>> 接口实现，支持判等操作。

父类型：

- [Equatable](core_package_interfaces.md#interface-equatablet)\<[Array](#struct-arrayt)\<T>>

#### func contains(T)

```cangjie
public func contains(element: T): Bool
```

功能：查找当前数组是否包含指定元素。

参数：

- element: T - 需要查找的目标元素。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果存在，则返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 4]
    println(arr.contains(1))
    return 0
}
```

运行结果：

```text
true
```

#### func indexOf(Array\<T>)

```cangjie
public func indexOf(elements: Array<T>): Option<Int64>
```

功能：返回数组中子数组 `elements` 出现的第一个位置，如果数组中不包含此数组，返回 None。

> **注意：**
>
> 当 T 的类型是 [Int64](core_package_intrinsics.md#int64) 时，此函数的变长参数语法糖版本可能会和 `public func indexOf(element: T, fromIndex: Int64): Option<Int64>` 产生歧义，根据优先级，当参数数量是 2 个时，会优先调用 `public func indexOf(element: T, fromIndex: Int64): Option<Int64>`。

参数：

- elements: [Array](core_package_structs.md#struct-arrayt)\<T> - 需要定位的目标数组。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 数组中子数组 `elements` 出现的第一个位置，如果数组中不包含此数组，返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 4]
    let subArr = [2, 3]
    println(arr.indexOf(subArr))
    return 0
}
```

运行结果：

```text
Some(1)
```

#### func indexOf(Array\<T>, Int64)

```cangjie
public func indexOf(elements: Array<T>, fromIndex: Int64): Option<Int64>
```

功能：返回数组中在 `fromIndex`之后，子数组`elements` 出现的第一个位置，未找到返回 None。

函数会对 `fromIndex` 范围进行检查，`fromIndex` 小于 0 时，将会从第 0 位开始搜索，当 `fromIndex` 大于等于本数组的大小时，结果为 None。

参数：

- elements: [Array](core_package_structs.md#struct-arrayt)\<T> - 需要定位的元素。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 开始搜索的起始位置。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 数组中在 `fromIndex`之后，子数组 `elements` 出现的第一个位置，未找到返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 4, 2, 3]
    let subArr = [2, 3]
    println(arr.indexOf(subArr, 3))
    return 0
}
```

运行结果：

```text
Some(4)
```

#### func indexOf(T)

```cangjie
public func indexOf(element: T): Option<Int64>
```

功能：获取数组中 `element` 出现的第一个位置，如果数组中不包含此元素，返回 None。

参数：

- element: T - 需要定位的元素。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 数组中 `element` 出现的第一个位置，如果数组中不包含此元素，返回 None。