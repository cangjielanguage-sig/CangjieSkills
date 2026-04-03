## func ifSome\<T>(Option\<T>, (T) -> Unit)

```cangjie
public func ifSome<T>(o: Option<T>, action: (T) -> Unit): Unit
```

功能：如果输入是 [Option](core_package_enums.md#enum-optiont).Some 类型数据，则执行 action 函数。

参数：

- o: [Option](core_package_enums.md#enum-optiont)\<T> - 待判断是否为 [Option](core_package_enums.md#enum-optiont).Some 的 [Option](core_package_enums.md#enum-optiont)\<T> 类型实例，同时其封装的 `T` 类型实例将作为 action 函数的输入。
- action: (T) ->[Unit](core_package_intrinsics.md#unit) - 待执行函数。

示例：

<!-- verify -->
```cangjie
main() {
    let num: Option<Int64> = Some(200)
    ifSome<Int64>(num, {numValue: Int64 => println("num is ${numValue}")})
}
```

运行结果：

```text
num is 200
```

## func max\<T>(T, T, Array\<T>) where T <: Comparable\<T>

```cangjie
public func max<T>(a: T, b: T, others: Array<T>): T where T <: Comparable<T>
```

功能：根据 T 类型的 [Comparable](./core_package_interfaces.md#interface-comparablet) 接口实现，返回一组数据中的最大值，由于此函数的第三个参数是一个变长参数，支持获取二个以上的数据的比较。

> **注意：**
>
> 浮点数类型的比较也将按照 [Comparable](./core_package_interfaces.md#interface-comparablet) 的结果进行比较，如果浮点书中有非数 `NaN`，结果将不正确，此时建议使用 [Float16](./core_package_intrinsics.md#float16)、[Float32](./core_package_intrinsics.md#float32)、[Float64](./core_package_intrinsics.md#float64) 的 `static func max`方法。

参数：

- a: T - 第一个待比较的数。
- b: T - 第二个待比较的数。
- others: [Array](./core_package_structs.md#struct-arrayt)\<T> - 其他待比较的数。

返回值：

- T - 返回参数中的最大值。

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
    println("The larger one is ${max(r1, r2)}")
}
```

运行结果：

```text
The larger one is width: 20, height: 30, area: 600
```