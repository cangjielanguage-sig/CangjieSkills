### func repeat(Int64)

```cangjie
public func repeat(n: Int64): Array<T>
```

功能：重复当前数组若干次，得到新数组。

参数：

- n: [Int64](core_package_intrinsics.md#int64) - 重复次数。

返回值：

- [Array](./core_package_structs.md#struct-arrayt)\<T> - 重复当前数组 n 次得到的新数组。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 参数 n 小于等于 0。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [0, 1, 2]
    var arr1 = arr.repeat(2)
    println(arr1)
    return 0
}
```

运行结果：

```text
[0, 1, 2, 0, 1, 2]
```

### func reverse()

```cangjie
public func reverse(): Unit
```

功能：反转数组，将数组中元素的顺序进行反转。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    arr.reverse()
    println(arr)
}
```

运行结果：

```text
[5, 4, 3, 2, 1, 0]
```

### func slice(Int64, Int64)

```cangjie
public func slice(start: Int64, len: Int64): Array<T>
```

功能：获取数组切片。

> **注意：**
>
> 切片不会对数组数据进行拷贝，是对原数据特定区间的引用。

参数：

- start: [Int64](core_package_intrinsics.md#int64) - 切片的起始位置，取值需大于 0，且 start + len 小于等于当前 [Array](core_package_structs.md#struct-arrayt) 实例的长度。
- len: [Int64](core_package_intrinsics.md#int64) - 切片的长度，取值需大于 0。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 返回切片后的数组。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果参数不符合上述取值范围，抛出异常。

示例：

<!-- verify -->
```cangjie
class Rectangle <: ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}"
    }
}

main(): Int64 {
    let arr = [Rectangle(1, 2), Rectangle(3, 4), Rectangle(5, 6)]
    let arr1 = arr.slice(1, 2)
    println(arr1)
    /* 由于 slice() 是对原数组的引用，在新数组上修改，原数组引用类型的元素也会变化 */
    arr1[0].width = 5
    println(arr)
    return 0
}
```

运行结果：

```text
[width: 3, height: 4, width: 5, height: 6]
[width: 1, height: 2, width: 5, height: 4, width: 5, height: 6]
```

### func splitAt(Int64)

```cangjie
public func splitAt(mid: Int64): (Array<T>, Array<T>)
```

功能：从指定位置 mid 处分割数组。

得到的两个数组是原数组的切片，取值范围为 [0, mid), [mid, this.size)。

参数：

- mid: [Int64](core_package_intrinsics.md#int64) - 分割的位置，取值范围为 [0, this.size]。

返回值：

- ([Array](./core_package_structs.md#struct-arrayt)\<T>, [Array](./core_package_structs.md#struct-arrayt)\<T>) - 分割原数组得到的两个切片。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - mid 小于 0 或大于 this.size。

### func swap(Int64, Int64)

```cangjie
public func swap(index1: Int64, index2: Int64): Unit
```

功能：交换指定位置的两个元素。

如果 index1 和 index2 指向同一个位置，将不做交换。

参数：

- index1: [Int64](core_package_intrinsics.md#int64) - 需要交换的两个元素的下标之一，取值范围为 [0, this.size)。
- index2: [Int64](core_package_intrinsics.md#int64) - 需要交换的两个元素的下标之一，取值范围为 [0, this.size)。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - index1 / index2 小于 0 或大于等于 this.size。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 4]
    arr.swap(1, 2)
    println(arr)
    return 0
}
```

运行结果：

```text
[1, 3, 2, 4]
```