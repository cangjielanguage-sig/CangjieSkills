## func print\<T>(T, Bool) where T <: ToString

```cangjie
public func print<T>(arg: T, flush!: Bool = false): Unit where T <: ToString
```

功能：向控制台输出 `T` 类型实例的字符串表示。

参数：

- arg: T - 待输出的数据，支持实现了 [ToString](core_package_interfaces.md#interface-tostring) 接口的类型。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

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

    public func area() {
        width * height
    }
    public func toString(): String {
        return "width: ${this.width}, height: ${this.height}"
    }
}

main() {
    print<Rectangle>(Rectangle(10, 20))
}
```

运行结果：

```text
width: 10, height: 20
```

## func println()

```cangjie
public func println(): Unit
```

功能：向标准输出（stdout）输出换行符。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt8 = 8
    var num2: UInt8 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```

## func println(Bool)

```cangjie
public func println(b: Bool): Unit
```

功能：向控制台输出 [Bool](core_package_intrinsics.md#bool) 类型数据的字符串表达，末尾添加换行。

参数：

- b: [Bool](core_package_intrinsics.md#bool) - 待输出的 [Bool](core_package_intrinsics.md#bool) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var flag1: Bool = true
    var flag2: Bool = false
    println(flag1)
    println(flag2)
}
```

运行结果：

```text
true
false
```

## func println(Float16)

```cangjie
public func println(f: Float16): Unit
```

功能：向控制台输出 [Float16](core_package_intrinsics.md#float16) 类型数据的字符串表达，末尾添加换行。

参数：

- f: [Float16](core_package_intrinsics.md#float16) - 待输出的 [Float16](core_package_intrinsics.md#float16) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float16 = 3.1415
    var num2: Float16 = 3.141592
    println(num1)
    println(num2)
}
```

运行结果：

```text
3.140625
3.140625
```

## func println(Float32)

```cangjie
public func println(f: Float32): Unit
```

功能：向控制台输出 [Float32](core_package_intrinsics.md#float32) 类型数据的字符串表达，末尾添加换行。

参数：

- f: [Float32](core_package_intrinsics.md#float32) - 待输出的 [Float32](core_package_intrinsics.md#float32) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float32 = 3.1415
    var num2: Float32 = 3.141592
    println(num1)
    println(num2)
}
```

运行结果：

```text
3.141500
3.141592
```

## func println(Float64)

```cangjie
public func println(f: Float64): Unit
```

功能：向控制台输出 [Float64](core_package_intrinsics.md#float64) 类型数据的字符串表达，末尾添加换行。

参数：

- f: [Float64](core_package_intrinsics.md#float64) - 待输出的 [Float64](core_package_intrinsics.md#float64) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float64 = 3.1415
    var num2: Float64 = 3.141592
    println(num1)
    println(num2)
}
```

运行结果：

```text
3.141500
3.141592
```

## func println(Int16)

```cangjie
public func println(i: Int16): Unit
```

功能：向控制台输出 [Int16](core_package_intrinsics.md#int16) 类型数据的字符串表达，末尾添加换行。

参数：

- i: [Int16](core_package_intrinsics.md#int16) - 待输出的 [Int16](core_package_intrinsics.md#int16) 类型数据。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int16 = 8
    var num2: Int16 = 32
    println(num1)
    println(num2)
}
```

运行结果：

```text
8
32
```