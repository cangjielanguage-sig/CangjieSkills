### func sqrtWithPrecision(Int64, RoundingMode)

```cangjie
public func sqrtWithPrecision(precision: Int64, roundingMode!: RoundingMode = RoundingMode.HalfEven): Decimal
```

功能：开方运算，支持自定义运算精度和结果舍入方式，获取当前对象开方结果，如果运算结果超过 `presision` 指定的精度，则根据指定的精度对开方结果进行舍入。

参数：

- precision: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 精度值。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 返回入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 的算术平方根，根据输入精度和舍入方式进行取整。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果被计算平方根的对象为负数，则抛此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当计算平方根操作结果标度值溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let n: Decimal = Decimal.parse("2")
    let s = n.sqrtWithPrecision(2)
    println(s)
}
```

运行结果：

```text
1.4
```

### func toBigInt()

```cangjie
public func toBigInt(): BigInt
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [BigInt](math_numeric_package_structs.md#struct-bigint) 类型。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 转换后的 [BigInt](math_numeric_package_structs.md#struct-bigint) 值。

### func toEngString()

```cangjie
public func toEngString(): String
```

功能：以工程计数法的形式打印输出 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，指数为 3 的倍数，当值小于 0 时以 “-” 开头后跟十进制数字，大于等于 0 时，直接打印输出数字，不额外添加 “+”。指数小于 0 时同样遵循以上规则。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 工程计数法形式的 [Decimal](math_numeric_package_structs.md#struct-decimal) 字符串。

### func toFloat16()

```cangjie
public func toFloat16(): Float16
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 转换后的 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。

### func toFloat32()

```cangjie
public func toFloat32(): Float32
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 转换后的 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。

### func toFloat64()

```cangjie
public func toFloat64(): Float64
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 转换后的 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。