#### func indexOf(T, Int64)

```cangjie
public func indexOf(element: T, fromIndex: Int64): Option<Int64>
```

功能：返回数组中在 `fromIndex`之后， `element` 出现的第一个位置，未找到返回 None。

函数会从下标 `fromIndex` 开始查找，`fromIndex` 小于 0 时，将会从第 0 位开始搜索，当 `fromIndex` 大于等于本数组的大小时，结果为 None。

参数：

- element: T - 需要定位的元素。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 查找的起始位置。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 返回数组中在 `fromIndex`之后， `element` 出现的第一个位置，未找到返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 4, 2, 3]
    let subArr = [2, 3]
    println(arr.lastIndexOf(subArr, 3))
    return 0
}
```

运行结果：

```text
Some(4)
```

#### func lastIndexOf(Array\<T>)

```cangjie
public func lastIndexOf(elements: Array<T>): Option<Int64>
```

功能：返回数组中子数组 `elements` 出现的最后一个位置，如果数组中不存在此子数组，返回 None。

参数：

- elements: [Array](core_package_structs.md#struct-arrayt)\<T> - 需要定位的目标数组。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 数组中 `elements` 出现的最后一个位置，如果数组中不存在此子数组，返回 None。

#### func lastIndexOf(Array\<T>, Int64)

```cangjie
public func lastIndexOf(elements: Array<T>, fromIndex: Int64): Option<Int64>
```

功能：从 `fromIndex` 开始向后搜索，返回数组中子数组 `elements` 出现的最后一个位置，如果数组中不存在此子数组，返回 None。

函数会对 `fromIndex` 范围进行检查，`fromIndex` 小于 0 时，将会从第 0 位开始搜索，当 `fromIndex` 大于等于本数组的大小时，结果为 None。

参数：

- elements: [Array](core_package_structs.md#struct-arrayt)\<T> - 需要定位的目标数组。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 搜索开始的位置。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 从 `fromIndex` 开始向后搜索，数组中子数组 `elements` 出现的最后一个位置，如果数组中不存在此子数组，返回 None。

#### func lastIndexOf(T)

```cangjie
public func lastIndexOf(element: T): Option<Int64>
```

功能：返回数组中 `element` 出现的最后一个位置，如果数组中不存在此元素，返回 None。

参数：

- element: T - 需要定位的目标元素。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 数组中 `element` 出现的最后一个位置，如果数组中不存在此元素，返回 None。

#### func lastIndexOf(T, Int64)

```cangjie
public func lastIndexOf(element: T, fromIndex: Int64): Option<Int64>
```

功能：从 `fromIndex` 开始向后搜索，返回数组中 `element` 出现的最后一个位置，如果数组中不存在此元素，返回 None。

函数会对 `fromIndex` 范围进行检查，`fromIndex` 小于 0 时，将会从第 0 位开始搜索，当 `fromIndex` 大于等于本数组的大小时，结果为 None。

参数：

- element: T - 需要定位的目标元素。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 搜索开始的位置。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 从 `fromIndex` 开始向后搜索，返回数组中 `element` 出现的最后一个位置，如果数组中不存在此元素，返回 None。