### extend\<T> Iterator\<T>

```cangjie
extend<T> Iterator<T>
```

功能：扩展 [Iterator](core_package_classes.md#class-iteratort)\<T> 类型。

迭代器的方法主要包含中间操作和终止操作。中间操作（如 `skip()`、`map()`）会产生一个新的迭代器。而终止操作（如 `count()`、`all()`）会根据迭代器产生的元素计算结果，而不产生新的迭代器。每种迭代器方法都会消耗迭代器中不同数量的元素，详见各方法描述。

#### func all((T) -> Bool)

```cangjie
public func all(predicate: (T)-> Bool): Bool
```

功能：判断迭代器所有元素是否都满足条件。此方法会重复获取并消耗迭代器中元素直到某个元素不满足条件。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 元素是否都满足条件。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取容器的迭代器对象 */
    var iter = arr.iterator()
    var flag: Bool = iter.all({v: Int64 => v > 0})
    println(flag)
    return 0
}
```

运行结果：

```text
true
```

#### func any((T) -> Bool)

```cangjie
public func any(predicate: (T)-> Bool): Bool
```

功能：判断迭代器是否存在任意一个满足条件的元素。此方法会重复获取并消耗迭代器中元素直到某个元素满足条件。

参数：

- predicate: (T) -> [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 给定的条件。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否存在任意满足条件的元素。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取容器的迭代器对象 */
    var iter = arr.iterator()
    var flag: Bool = iter.any({v: Int64 => v > 4})
    println(flag)
    return 0
}
```

运行结果：

```text
true
```

#### func at(Int64)

```cangjie
public func at(n: Int64): Option<T>
```

功能：获取当前迭代器第 n 个元素，n 从 0 开始计数。此方法会消耗指定元素前的所有元素（包括指定元素）。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 给定的元素序号，序号从 0 开始。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 返回对应位置元素，若 n 大于剩余元素数量则返回 None。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]

    /* 获取容器的迭代器对象 */
    var iter = arr.iterator()
    var num: Option<Int64> = iter.at(2)
    println(num)
    return 0
}
```

运行结果：

```text
Some(3)
```

#### func concat(Iterator\<T>)

```cangjie
public func concat(other: Iterator<T>): Iterator<T>
```

功能：串联两个迭代器，当前迭代器在先，参数表示的迭代器在后。

参数：

- other: [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 要串联在后面的迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<T> - 返回串联后的新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr1: Array<Int64> = [1, 2]
    var arr2: Array<Int64> = [3, 4]

    /* 获取容器的迭代器对象 */
    var iter1 = arr1.iterator()
    var iter2 = arr2.iterator()

    /* 合并两个迭代器 */
    var iter = iter1.concat(iter2)

    /* 使用迭代器进行遍历 */
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
1
2
3
4
```