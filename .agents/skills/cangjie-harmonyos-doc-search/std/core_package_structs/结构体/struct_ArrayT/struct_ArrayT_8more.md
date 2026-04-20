## struct Array\<T>

```cangjie
public struct Array<T> {
    public const init()
    public init(size: Int64, repeat!: T)
    public init(size: Int64, initElement: (Int64) -> T)
}
```

功能：仓颉数组类型，用来表示单一类型的元素构成的有序序列。

T 表示数组的元素类型，T 可以是任意类型。

### prop first

```cangjie
public prop first: Option<T>
```

功能：获取当前数组的第一个元素，如果当前数组为空，返回 None。

类型：[Option](core_package_enums.md#enum-optiont)\<T>

### prop last

```cangjie
public prop last: Option<T>
```

功能：获取当前数组的最后一个元素，如果当前数组为空，返回 None。

类型：[Option](core_package_enums.md#enum-optiont)\<T>

### init()

```cangjie
public const init()
```

功能：构造一个空数组。

### init(Int64, (Int64) -> T)

```cangjie
public init(size: Int64, initElement: (Int64) -> T)
```

功能：创建指定长度的数组，其中元素根据初始化函数计算获取。

即：将 [0, size) 范围内的值分别传入初始化函数 initElement，执行得到数组对应下标的元素。

参数：

- size: [Int64](core_package_intrinsics.md#int64) - 数组大小。
- initElement: ([Int64](core_package_intrinsics.md#int64)) ->T - 初始化函数。

异常：

- [NegativeArraySizeException](core_package_exceptions.md#class-negativearraysizeexception) - 当 size 小于 0，抛出异常。

### init(Int64, T)

```cangjie
public init(size: Int64, repeat!: T)
```

功能：构造一个指定长度的数组，其中元素都用指定初始值进行初始化。

> **注意：**
>
> 该构造函数不会拷贝 repeat， 如果 repeat 是一个引用类型，构造后数组的每一个元素都将指向相同的引用。

参数：

- size: [Int64](core_package_intrinsics.md#int64) - 数组大小，取值范围为 [0, [Int64](core_package_intrinsics.md#int64).Max]。
- repeat!: T - 数组元素初始值。

异常：

- [NegativeArraySizeException](core_package_exceptions.md#class-negativearraysizeexception) - 当 size 小于 0，抛出异常。

### func clone()

```cangjie
public func clone(): Array<T>
```

功能：克隆数组，将对数组数据进行深拷贝。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 克隆得到的新数组。

### func clone(Range\<Int64>)

```cangjie
public func clone(range: Range<Int64>) : Array<T>
```

功能：克隆数组的指定区间。

> **注意：**
>
> 1. 如果参数 range 是使用 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>    - start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
>    - hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，数组切片取到原数组最后一个元素。
> 2. range 的步长只能为 1。

参数：

- range: [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](core_package_intrinsics.md#int64)> - 克隆的区间。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 克隆得到的新数组。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - range 超出数组范围时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    let new = arr.clone(1..4)
    println(new)
}
```

运行结果：

```text
[1, 2, 3]
```