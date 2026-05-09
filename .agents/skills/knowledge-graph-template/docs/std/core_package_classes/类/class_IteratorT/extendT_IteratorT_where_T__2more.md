### extend\<T> Iterator\<T> where T <: Comparable\<T>

```cangjie
extend<T> Iterator<T> where T <: Comparable<T>
```

功能：为 [Iterator](core_package_classes.md#class-iteratort)\<T> 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<T> 接口，支持比较操作。

#### func max()

```cangjie
public func max(): Option<T>
```

功能：筛选最大的元素。此方法会消耗迭代器中的所有元素。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 返回最大的元素，若为空则返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4]

    /* 获取迭代器对象，使用 max() 求最大值 */
    var iter = arr.iterator()
    match (iter.max()) {
        case Some(i) => println(i)
        case None => println("None!")
    }
    return 0
}
```

运行结果：

```text
4
```

#### func min()

```cangjie
public func min(): Option<T>
```

功能：筛选最小的元素。此方法会消耗迭代器中的所有元素。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 返回最小的元素，若为空则返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4]

    /* 获取迭代器对象，使用 min() 求最小值 */
    var iter = arr.iterator()
    match (iter.min()) {
        case Some(i) => println(i)
        case None => println("None!")
    }
    return 0
}
```

运行结果：

```text
1
```

### extend\<T> Iterator\<T> where T <: Equatable\<T>

```cangjie
extend<T> Iterator<T> where T <: Equatable<T>
```

功能：为 [Iterator](core_package_classes.md#class-iteratort)\<T> 类型扩展 扩展 [Equatable](core_package_interfaces.md#interface-equatablet)\<T> 接口，支持判等操作。

#### func contains(T)

```cangjie
public func contains(element: T): Bool
```

功能：遍历所有元素，判断是否包含指定元素。此方法会重复获取并消耗迭代器中元素直到某个元素与参数 `element` 相等。

参数：

- element: T - 要查找的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否包含指定元素。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4]

    /* 获取迭代器对象，查找是否包含元素 3 */
    var iter = arr.iterator()
    println(iter.contains(3))

    /* 使用迭代器进行遍历，输出剩余元素 */
    while (true) {
        match (iter.next()) {
            case Some(i) => println(i)
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
true
4
```