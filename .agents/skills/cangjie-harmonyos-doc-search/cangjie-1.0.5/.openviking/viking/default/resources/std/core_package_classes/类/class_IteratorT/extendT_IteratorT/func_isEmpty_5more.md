#### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断当前迭代器是否为空。此方法会调用 [next()](#func-next-1) ，根据其返回值判断当前迭代器是否为空。因此如果当前迭代器不为空，则会消耗一个元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回当前迭代器是否为空。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取迭代器对象 */
    var iter = arr.iterator()

    /* 判断迭代器中是否有元素，如果有会消耗一个元素 */
    println(iter.isEmpty())

    /* 使用迭代器进行展开遍历 */
    while (true) {
        match (iter.next()) {
            case Some(i) => println(i)
            case None => break
        }
    }
    println(iter.isEmpty())
    return 0
}
```

运行结果：

```text
false
2
true
```

#### func last()

```cangjie
public func last(): Option<T>
```

功能：获取当前迭代器尾部元素。此方法会获取并消耗迭代器中的所有元素，并返回最后一个元素。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回尾部元素，若为空则返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取迭代器对象 */
    var iter = arr.iterator()
    println(iter.last())
    return 0
}
```

运行结果：

```text
Some(2)
```

#### func map\<R>((T) -> R)

```cangjie
public func map<R>(transform: (T)-> R): Iterator<R>
```

功能：创建一个映射。

参数：

- transform: (T) ->R - 给定的映射函数。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个映射。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4]

    /* 获取迭代器对象，并对元素进行映射，获取新的迭代器对象 */
    var iter = arr.iterator()
    var iter1 = iter.map({value => value * 2})

    /* 使用迭代器进行展开遍历 */
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
2
4
6
8
```

#### func none((T) -> Bool)

```cangjie
public func none(predicate: (T)-> Bool): Bool
```

功能：判断当前迭代器中所有元素是否都不满足条件。此方法会重复获取并消耗迭代器中元素直到某个元素满足条件。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前迭代器中元素是否都不满足条件。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4]

    /* 获取迭代器对象，并对元素进行映射，获取新的迭代器对象 */
    var iter1 = arr.iterator()
    var iter2 = arr.iterator()

    /* 存在元素大于 2，返回 false */
    var flag1: Bool = iter1.none({value => value > 2})
    println(flag1)

    /* 不存在元素大于 5，返回 true */
    var flag2: Bool = iter2.none({value => value > 5})
    println(flag2)
    return 0
}
```

运行结果：

```text
false
true
```

#### func reduce((T, T) -> T)

```cangjie
public func reduce(operation: (T, T) -> T): Option<T>
```

功能：使用第一个元素作为初始值，从左向右计算。此方法会消耗迭代器中的所有元素。

参数：

- operation: (T, T) -> T - 给定的计算函数。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回计算结果。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取迭代器对象，对数组元素进行求和 */
    var iter = arr.iterator()
    var sum: Option<Int64> = iter.reduce({total, value => total + value})
    println(sum)
    return 0
}
```

运行结果：

```text
Some(15)
```