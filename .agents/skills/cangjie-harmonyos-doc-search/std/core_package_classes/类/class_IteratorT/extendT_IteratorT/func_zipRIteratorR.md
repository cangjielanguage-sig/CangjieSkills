#### func zip\<R>(Iterator\<R>)

```cangjie
public func zip<R>(it: Iterator<R>): Iterator<(T, R)>
```

功能：将两个迭代器合并成一个（长度取决于短的那个迭代器）。

参数：

- it: [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<R> - 要合并的其中一个迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<(T, R)> - 返回一个新迭代器。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr1: Array<Int64> = [1, 2, 3, 4]
    var arr2: Array<Int64> = [4, 5, 6]

    /* 获取迭代器对象并合并，新迭代器中的元素为对应索引位置元素的元组 */
    var iter1 = arr1.iterator()
    var iter2 = arr2.iterator()
    var iter = iter1.zip(iter2)

    /* 使用迭代器进行遍历，长度取决于较短的迭代器 */
    while (true) {
        match (iter.next()) {
            case Some(i) => println("The current element is (${i[0]}, ${i[1]})")
            case None => break
        }
    }
    return 0
}
```

运行结果：

```text
The current element is (1, 4)
The current element is (2, 5)
The current element is (3, 6)
```