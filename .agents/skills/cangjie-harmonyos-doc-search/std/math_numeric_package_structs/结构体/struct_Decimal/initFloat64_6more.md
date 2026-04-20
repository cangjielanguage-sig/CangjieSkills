### init(Float64)

```cangjie
public init(val: Float64)
```

功能：通过 64 位有符号浮点数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

> **注意：**
>
> 由于部分十进制小数无法通过二进制浮点数精确表示，此构造函数以精确值构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，传入浮点数值可能与最终构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象字符串打印值不一致。

参数：

- val: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 64 位有符号二进制浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参为 `inf`、`-inf` 或 `nan` 时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let float64: Float64 = 0.8
    let decimal = Decimal(float64)
    println(decimal)
}
```

运行结果：

```text
0.8000000000000000444089209850062616169452667236328125
```

### init(Int16)

```cangjie
public init(val: Int16)
```

功能：通过 16 位有符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 16 位有符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let int16: Int16 = 24
    let decimal = Decimal(int16)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(Int32)

```cangjie
public init(val: Int32)
```

功能：通过 32 位有符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 32 位有符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let int32: Int32 = 24
    let decimal = Decimal(int32)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(Int64)

```cangjie
public init(val: Int64)
```

功能：通过 64 位有符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 64 位有符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let int64: Int64 = 24
    let decimal = Decimal(int64)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(Int8)

```cangjie
public init(val: Int8)
```

功能：通过 8 位有符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 8 位有符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let int8: Int8 = 24
    let decimal = Decimal(int8)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(IntNative)

```cangjie
public init(val: IntNative)
```

功能：通过 32 位或 64 位（具体长度与平台相关）有符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 32 位或 64 位有符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let intnative: IntNative = 24
    let decimal = Decimal(intnative)
    println(decimal)
}
```

运行结果：

```text
24
```