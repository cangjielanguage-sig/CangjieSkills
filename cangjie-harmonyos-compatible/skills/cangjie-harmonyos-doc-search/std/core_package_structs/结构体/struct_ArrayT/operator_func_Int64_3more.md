### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): T
```

功能：获取数组下标 index 对应的值。

该函数中如果 index 越界，将抛出异常。

也可以通过 get 函数获取数组指定下标的元素，get 函数将在 index 越界时返回 None。

参数：

- index: [Int64](core_package_intrinsics.md#int64) - 要获取的值的下标，取值范围为 [0, [Int64](core_package_intrinsics.md#int64).Max]。

返回值：

- T - 数组中下标 index 对应的值。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 index 小于 0，或大于等于数组长度，抛出异常。

### operator func \[](Int64, T)

```cangjie
public operator func [](index: Int64, value!: T): Unit
```

功能：修改数组中下标 index 对应的值。

参数：

- index: [Int64](core_package_intrinsics.md#int64) - 需要修改值的下标，取值范围为 [0, [Int64](core_package_intrinsics.md#int64).Max]。
- value!: T - 修改的目标值。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 index 小于 0，或大于等于数组长度，抛出异常。

### operator func \[](Range\<Int64>)

```cangjie
public operator func [](range: Range<Int64>): Array<T>
```

功能：根据给定区间获取数组切片。

> **注意：**
>
> 1. 如果参数 range 是使用 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>    - start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
>    - hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，该数组切片取到原数组最后一个元素。
> 2. range 的步长只能为 1。

参数：

- range: [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](core_package_intrinsics.md#int64)> - 切片的范围，range 表示的范围不能超过数组范围。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 数组切片。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果 range 的步长不等于 1，抛出异常。
- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 range 表示的数组范围无效，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    let slice = arr[1..4]
    arr[3] = 10
    println(slice)
}
```

运行结果：

```text
[1, 2, 10]
```