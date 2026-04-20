#### func count()

```cangjie
public func count(): Int64
```

功能：统计当前迭代器包含元素数量。此方法会消耗迭代器中所有元素来计算迭代器中的元素数量。

> **注意：**
>
> 该方法会消耗迭代器，即使用该方法后迭代器内不再包含任何元素。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回迭代器包含元素数量。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取容器的迭代器对象 */
    var iter = arr.iterator()
    let len: Int64 = iter.count()
    println(len)

    /* 使用迭代器进行遍历，但是 count 消耗了迭代器中的元素，因此不会打印 */
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
2
```

#### func enumerate()

```cangjie
public func enumerate(): Iterator<(Int64, T)>
```

功能：用于获取带索引的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<([Int64](../../core/core_package_api/core_package_intrinsics.md#int64), T)> - 返回一个带索引的迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取容器的迭代器对象 */
    var iter = arr.iterator()
    var iter1 = iter.enumerate()

    /* 使用迭代器进行遍历 */
    while (true) {
        match (iter1.next()) {
            case Some(i) =>
                print(i[0].toString() + ' ')
                print(i[1])
                println()
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
0 1
1 2
```

#### func filter((T) -> Bool)

```cangjie
public func filter(predicate: (T)-> Bool): Iterator<T>
```

功能：筛选出满足条件的元素。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件，条件为 `true` 的元素会按顺序出现在返回的迭代器里。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取过滤后的迭代器对象 */
    var iter = arr.iterator()
    var iter1 = iter.filter({value: Int64 => value > 2})

    /* 使用迭代器进行遍历 */
    while (true) {
        match (iter1.next()) {
            case Some(i) => println(i)
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
3
4
5
```

#### func filterMap\<R>((T) -> Option\<R>)

```cangjie
public func filterMap<R>(transform: (T) -> Option<R>): Iterator<R>
```

功能：同时进行筛选操作和映射操作，返回一个新的迭代器。

参数：

- transform: (T) -> [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 给定的映射函数。函数返回值为 Some 对应 filter 的 predicate 为 true，反之表示 false。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取过滤后的迭代器对象，对元素进行过滤和映射，映射需返回 Option 类型 */
    var iter = arr.iterator()
    var iter1 = iter.filterMap({
        value: Int64 => if (value > 2) {
            return Some(value + 1)
        } else {
            return None<Int64>
        }
    })

    /* 使用迭代器进行遍历 */
    while (true) {
        match (iter1.next()) {
            case Some(i) => println(i)
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
4
5
6
```

#### func first()

```cangjie
public func first(): Option<T>
```

功能：获取当前迭代器的头部元素。此方法会获取并消耗第一个元素。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回头部元素，若为空则返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取迭代器对象 */
    var iter = arr.iterator()
    var head: Option<Int64> = iter.first()
    println(head)

    return 0
}
```

运行结果：

```text
Some(1)
```