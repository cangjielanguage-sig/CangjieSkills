## class Iterator\<T>

```cangjie
public abstract class Iterator<T> <: Iterable<T> {
    public init()
}
```

功能：该类表示迭代器，提供 `next` 方法支持对容器内的成员进行迭代遍历。

父类型：

- [Iterable](core_package_interfaces.md#interface-iterablee)\<T>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Iterator](core_package_classes.md#class-iteratort)\<T> 对象。

### func iterator()

```cangjie
public func iterator() : Iterator<T>
```

功能：返回迭代器自身。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<T> - 迭代器自身。

### func next()

```cangjie
public func next(): Option<T>
```

功能：获取迭代过程中的下一个元素。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 迭代过程中的下一个元素。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    var arr: Array<Int64> = [1, 2, 3, 4, 5]
    var iter = arr.iterator() /* 获取容器的迭代器对象 */

    while (true) { /* 使用迭代器进行遍历 */
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
5
```