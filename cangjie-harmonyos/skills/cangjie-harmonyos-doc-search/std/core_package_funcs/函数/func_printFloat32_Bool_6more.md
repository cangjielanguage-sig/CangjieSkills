## func print(Float32, Bool)

```cangjie
public func print(f: Float32, flush!: Bool = false): Unit
```

功能：向控制台输出 [Float32](core_package_intrinsics.md#float32) 类型数据的小数点后六位的字符串表达，即超出六位的小数位不会输出，不足六位的小数位会补零。

参数：

- f: [Float32](core_package_intrinsics.md#float32) - 待输出的 [Float32](core_package_intrinsics.md#float32) 类型数据。
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

## func print(Float64, Bool)

```cangjie
public func print(f: Float64, flush!: Bool = false): Unit
```

功能：向控制台输出 [Float64](core_package_intrinsics.md#float64) 类型数据的小数点后六位的字符串表达，即超出六位的小数位不会输出，不足六位的小数位会补零。

参数：

- f: [Float64](core_package_intrinsics.md#float64) - 待输出的 [Float64](core_package_intrinsics.md#float64) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float64 = 0.76453
    var num2: Float64 = 0.683456
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
0.764530
0.683456
```

## func print(Int16, Bool)

```cangjie
public func print(i: Int16, flush!: Bool = false): Unit
```

功能：向控制台输出 [Int16](core_package_intrinsics.md#int16) 类型数据的字符串表达。

参数：

- i: [Int16](core_package_intrinsics.md#int16) - 待输出的 [Int16](core_package_intrinsics.md#int16) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int16 = 10
    var num2: Int16 = 2222
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
10
2222
```

## func print(Int32, Bool)

```cangjie
public func print(i: Int32, flush!: Bool = false): Unit
```

功能：向控制台输出 [Int32](core_package_intrinsics.md#int32) 类型数据的字符串表达。

参数：

- i: [Int32](core_package_intrinsics.md#int32) - 待输出的 [Int32](core_package_intrinsics.md#int32) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int32 = 1024
    var num2: Int32 = 2048
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
1024
2048
```

## func print(Int64, Bool)

```cangjie
public func print(i: Int64, flush!: Bool = false): Unit
```

功能：向控制台输出 [Int64](core_package_intrinsics.md#int64) 类型数据的字符串表达。

参数：

- i: [Int64](core_package_intrinsics.md#int64) - 待输出的 [Int64](core_package_intrinsics.md#int64) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int64 = 1024
    var num2: Int64 = 2048
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
1024
2048
```

## func print(Int8, Bool)

```cangjie
public func print(i: Int8, flush!: Bool = false): Unit
```

功能：向控制台输出 [Int8](core_package_intrinsics.md#int8) 类型数据的字符串表达。

参数：

- i: [Int8](core_package_intrinsics.md#int8) - 待输出的 [Int8](core_package_intrinsics.md#int8) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int8 = 8
    var num2: Int8 = 32
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