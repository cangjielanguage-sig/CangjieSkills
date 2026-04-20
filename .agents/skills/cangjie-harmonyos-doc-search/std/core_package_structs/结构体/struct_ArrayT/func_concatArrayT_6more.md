### func concat(Array\<T>)

```cangjie
public func concat(other: Array<T>): Array<T>
```

功能：该函数将创建一个新的数组，数组内容是当前数组后面串联 other 指向的数组。

参数：

- other: [Array](core_package_structs.md#struct-arrayt)\<T> - 串联到当前数组末尾的数组。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 串联得到的新数组。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    let new = arr.concat([6, 7, 8, 9, 10])
    println(new)
}
```

运行结果：

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### func copyTo(Array\<T>)

```cangjie
public func copyTo(dst: Array<T>): Unit
```

功能：将当前数组的全部元素拷贝到目标数组 dst 中。

拷贝长度为当前数组的长度，从目标数组的起始位置开始写入，要求当前数组的长度不大于目标数组的长度。

参数：

- dst: [Array](core_package_structs.md#struct-arrayt)\<T> - 目标数组。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当前数组的长度大于目标数组的长度。

### func copyTo(Array\<T>, Int64, Int64, Int64)

```cangjie
public func copyTo(dst: Array<T>, srcStart: Int64, dstStart: Int64, copyLen: Int64): Unit
```

功能：将当前数组中的一段数据拷贝到目标数组中。

参数：

- dst: [Array](core_package_structs.md#struct-arrayt)\<T> - 目标数组。
- srcStart: [Int64](core_package_intrinsics.md#int64) - 从 this 数组的 srcStart 下标开始拷贝，取值范围为 [0, this.size)。
- dstStart: [Int64](core_package_intrinsics.md#int64) - 从目标数组的 dstStart 下标开始写入，取值范围为 [0, dst.size)。
- copyLen: [Int64](core_package_intrinsics.md#int64) - 拷贝数组的长度，取值要求为 copyLen + srcStart < this.size，copyLen + dstStart < dst.size。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - copyLen 小于 0 则抛出此异常。
- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果参数不满足上述取值范围，抛出此异常。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    let new = [0, 0, 0, 0, 0, 0]
    arr.copyTo(new, 2, 2, 4)
    println(new)
}
```

运行结果：

```text
[0, 0, 2, 3, 4, 5]
```

### func fill(T)

```cangjie
public func fill(value: T): Unit
```

功能：将当前数组内所有元素都替换成指定的 value。

参数：

- value: T - 修改的目标值。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2]
    arr[1..3].fill(-1)
    println(arr)
}
```

运行结果：

```text
[0, -1, -1]
```

### func get(Int64)

```cangjie
public func get(index: Int64): Option<T>
```

功能：获取数组中下标 index 对应的元素。

该函数结果将用 [Option](core_package_enums.md#enum-optiont) 封装，如果 index 越界，将返回 None。

也可以通过 [] 操作符获取数组指定下标的元素，该接口将在 index 越界时抛出异常。

参数：

- index: [Int64](core_package_intrinsics.md#int64) - 要获取的值的下标。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - 当前数组中下标 index 对应的值。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2]
    let num = arr.get(0)
    println(num)
}
```

运行结果：

```text
Some(0)
```

### func map\<R>((T)->R)

```cangjie
public func map<R>(transform: (T)->R): Array<R>
```

功能：将当前数组内所有 T 类型元素根据 transform 映射为 R 类型的元素，组成新的数组。

参数：

- transform: (T)->R - 映射函数。

返回值：

- [Array](./core_package_structs.md#struct-arrayt)\<R> - 原数组中所有元素映射后得到的元素组成的新数组。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [0, 1, 2]
    let arr1 = arr.map({value => value + 1})
    println(arr1)
    return 0
}
```

运行结果：

```text
[1, 2, 3]
```