### operator func \[](Range\<Int64>, Array\<T>)

```cangjie
public operator func [](range: Range<Int64>, value!: Array<T>): Unit
```

功能：用指定的数组对本数组一个连续范围的元素赋值。

range 表示的区见的长度和目标数组 value 的大小需相等。

> **注意：**
>
> 1. 如果参数 range 是使用 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>    - start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
>    - hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，该数组切片取到原数组最后一个元素。
> 2. range 的步长只能为 1。

参数：

- range: [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](core_package_intrinsics.md#int64)> - 需要修改的数组范围，range 表示的范围不能超过数组范围。
- value!: [Array](core_package_structs.md#struct-arrayt)\<T> - 修改的目标值。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果 range 的步长不等于 1，或 range 长度不等于 value 长度，抛出异常。
- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 range 表示的数组范围无效，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    arr[1..3] = [10, 11]
    println(arr)
}
```

运行结果：

```text
[0, 10, 11, 3, 4, 5]
```

### extend\<T> Array\<Array\<T>>

```cangjie
extend<T> Array<Array<T>>
```

功能：为二维数组进行扩展，提供将其展开为一维数组的方法。

#### func flatten()

```cangjie
public func flatten(): Array<T>
```

功能：将当前二维数组展开为一维数组。

例如将 [[1, 2], [3, 4]] 展开为 [1, 2, 3, 4]。

返回值：

- [Array](./core_package_structs.md#struct-arrayt)\<T> - 展开后的一维数组。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [[1, 2], [3, 4]].flatten()
    println(arr)
    return 0
}
```

运行结果：

```text
[1, 2, 3, 4]
```

### extend\<T> Array\<T> <: Collection\<T>

```cangjie
extend<T> Array<T> <: Collection<T>
```

功能：为 [Array](core_package_structs.md#struct-arrayt)\<T> 类型实现 [Collection](core_package_interfaces.md#interface-collectiont) 接口。

父类型：

- [Collection](core_package_interfaces.md#interface-collectiont)\<T>

#### prop size

```cangjie
public prop size: Int64
```

功能：获取元素数量。

类型：[Int64](core_package_intrinsics.md#int64)

#### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断数组是否为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果数组为空，返回 true，否则，返回 false。

#### func iterator()

```cangjie
public func iterator(): Iterator<T>
```

功能：获取当前数组的迭代器，用于遍历数组。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<T> - 当前数组的迭代器。

#### func toArray()

```cangjie
public func toArray(): Array<T>
```

功能：根据当前 [Array](core_package_structs.md#struct-arrayt) 实例拷贝一个新的 [Array](core_package_structs.md#struct-arrayt) 实例。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 拷贝得到的新的 [Array](core_package_structs.md#struct-arrayt) 实例。