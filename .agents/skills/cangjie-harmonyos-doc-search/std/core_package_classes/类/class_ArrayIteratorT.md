## class ArrayIterator\<T>

```cangjie
public class ArrayIterator<T> <: Iterator<T> {
    public init(data: Array<T>)
}
```

功能：数组迭代器，迭代功能详述见 [Iterable](core_package_interfaces.md#interface-iterablee) 和 [Iterator](core_package_classes.md#class-iteratort) 说明。

父类型：

- [Iterator](#class-iteratort)\<T>

### init(Array\<T>)

```cangjie
public init(data: Array<T>)
```

功能：给定一个 [Array](core_package_structs.md#struct-arrayt) 数组实例，创建其对应的迭代器，用来迭代遍历该数组实例中全部对象。

参数：

- data: [Array](core_package_structs.md#struct-arrayt)\<T> - 数组实例。

### func next()

```cangjie
public func next(): Option<T>
```

功能：返回数组迭代器中的下一个值。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 数组迭代器中的下一个成员，用 [Option](core_package_enums.md#enum-optiont) 封装，迭代到末尾时返回 `None`。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<Int64> = [1, 2, 3, 4]
    var arrIterator: ArrayIterator<Int64> = ArrayIterator(arr)
    var num: Option<Int64>
    while (true) {
        num = arrIterator.next()
        if (num.isNone()) {
            break
        }
        println(num.getOrDefault({=> -1}))
    }
}
```

运行结果：

```text
1
2
3
4
```