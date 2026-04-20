#### func flatMap\<R>((T) -> Iterator\<R>)

```cangjie
public func flatMap<R>(transform: (T) -> Iterator<R>): Iterator<R>
```

功能：创建一个带 [flatten](../../collection/collection_package_api/collection_package_function.md#func-flattent-riterablet-where-t--iterabler) 功能的映射。

参数：

- transform: (T) -> [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<R> - 给定的映射函数。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 返回一个带 [flatten](../../collection/collection_package_api/collection_package_function.md#func-flattent-riterablet-where-t--iterabler) 功能的映射。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Array<Int64>> = [[1], [2], [3], [4, 5]]

    /* 获取带 flatten 功能的迭代器对象 */
    var iter = arr.iterator()
    var iter1 = iter.flatMap({value => value.iterator()})

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
1
2
3
4
5
```

#### func fold\<R>(R, (R, T) -> R)

```cangjie
public func fold<R>(initial: R, operation: (R, T)->R): R
```

功能：使用指定初始值，从左向右计算。此方法会消耗迭代器中的所有元素。

参数：

- initial: R - 给定的 R 类型的初始值。
- operation: (R, T) -> R - 给定的计算函数。

返回值：

- R - 返回最终计算得到的值。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取迭代器对象，对数组元素进行求和 */
    var iter = arr.iterator()
    var sum: Int64 = iter.fold(0, {total, value => total + value})

    println(sum)
    return 0
}
```

运行结果：

```text
15
```

#### func forEach((T) -> Unit)

```cangjie
public func forEach(action: (T)-> Unit): Unit
```

功能：遍历当前迭代器所有元素，对每个元素执行给定的操作。此方法会消耗迭代器中的所有元素。

参数：

- action: (T) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 给定的操作函数。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    var iter = arr.iterator()
    iter.forEach({value => println(value)})

    return 0
}
```

运行结果：

```text
1
2
3
4
5
```

#### func inspect((T) -> Unit)

```cangjie
public func inspect(action: (T) -> Unit): Iterator<T>
```

功能：迭代器每次调用 next() 对当前元素执行额外操作（不会消耗迭代器中元素）。

参数：

- action: (T) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 给定的操作函数。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取迭代器对象，并为 next 函数附加额外操作 */
    var iter = arr.iterator()
    var iter1 = iter.inspect({value => println("Logging: Processing ${value}")})

    /* 使用迭代器进行展开遍历 */
    while (true) {
        match (iter1.next()) {
            case Some(i) => println("Processing ${i} !")
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
Logging: Processing 1
Processing 1 !
Logging: Processing 2
Processing 2 !
```

#### func intersperse(T)

```cangjie
public func intersperse(separator: T): Iterator<T>
```

功能：迭代器每两个元素之间插入一个给定的新元素。

参数：

- separator: T - 给定的元素。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回一个新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2]

    /* 获取迭代器对象，每两个元素之间插入一个 0 */
    var iter = arr.iterator()
    var iter1 = iter.intersperse(0)

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
1
0
2
```