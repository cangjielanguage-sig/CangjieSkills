## func min\<T>(T, T, Array\<T>) where T <: Comparable\<T>

```cangjie
public func min<T>(a: T, b: T, others: Array<T>): T where T <: Comparable<T>
```

功能：根据 T 类型的 [Comparable](./core_package_interfaces.md#interface-comparablet) 接口实现，返回一组数据中的最小值，由于此函数的第三个参数是一个变长参数，支持获取二个以上的数据的比较。

> **注意：**
>
> 浮点数类型的比较也将按照 [Comparable](./core_package_interfaces.md#interface-comparablet) 的结果进行比较，如果浮点书中有非数`NaN`，结果将不正确，此时建议使用 [Float16](./core_package_intrinsics.md#float16)、[Float32](./core_package_intrinsics.md#float32)、[Float64](./core_package_intrinsics.md#float64) 的 `static func min`方法。

参数：

- a: T - 第一个待比较的数。
- b: T - 第二个待比较的数。
- others: [Array](./core_package_structs.md#struct-arrayt)\<T> - 其他待比较的数。

返回值：

- T - 返回参数中的最小值。

示例：

<!-- verify -->
```cangjie
class Rectangle <: Comparable<Rectangle> & ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }
    public prop area: Int64 {
        get() {
            return this.width * this.height
        }
    }
    public func compare(t: Rectangle): Ordering {
        if (t.area > this.area) {
            return Ordering.LT
        } else if (t.area == this.area) {
            return Ordering.EQ
        } else {
            Ordering.GT
        }
    }
    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}, area: ${this.area}"
    }
}

main() {
    var r1: Rectangle = Rectangle(10, 20)
    var r2: Rectangle = Rectangle(20, 30)
    println("The smaller one is ${min(r1, r2)}")
}
```

运行结果：

```text
The smaller one is width: 10, height: 20, area: 200
```

## func print(Bool, Bool)

```cangjie
public func print(b: Bool, flush!: Bool = false): Unit
```

功能：向控制台输出 [Bool](core_package_intrinsics.md#bool) 类型数据的字符串表达。

> **注意：**
>
> 下列 [print](core_package_funcs.md#func-printbool-bool)、 [println](core_package_funcs.md#func-println)、 [eprint](core_package_funcs.md#func-eprintstring-bool)、 [eprintln](core_package_funcs.md#func-eprintlnstring) 函数默认为 UTF-8 编码。

参数：

- b: [Bool](core_package_intrinsics.md#bool) - 待输出的 [Bool](core_package_intrinsics.md#bool) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var flag: Bool = false
    print(flag)
    flag = true
    println()
    print(flag)
}
```

运行结果：

```text
false
true
```

## func print(Float16, Bool)

```cangjie
public func print(f: Float16, flush!: Bool = false): Unit
```

功能：向控制台输出 [Float16](core_package_intrinsics.md#float16) 类型数据的小数点后六位的字符串表达，即超出六位的小数位不会输出，不足六位的小数位会补零。

参数：

- f: [Float16](core_package_intrinsics.md#float16) - 待输出的 [Float16](core_package_intrinsics.md#float16) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float16 = 0.76
    var num2: Float16 = 0.68
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
0.759766
0.680176
```

> **注意：**
>
> 仓颉采用 IEEE 754 格式表示浮点数，保存数值可能会有误差。
>