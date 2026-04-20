### func isInteger()

```cangjie
public func isInteger(): Bool
```

功能：判断当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象是否为整数。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回当前对象是否为整数判断结果。当前对象为整数时返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(100)
    println("${A}.isInteger() = ${A.isInteger()}")
}
```

运行结果：

```text
100.isInteger() = true
```

### func powWithPrecision(Int64, Int64, RoundingMode)

```cangjie
public func powWithPrecision(n: Int64, precision: Int64, roundingMode!: RoundingMode = RoundingMode.HalfEven): Decimal
```

功能：乘方运算，支持自定义运算精度和舍入方式，获取当前对象为底数，入参 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 为指数的乘方运算结果，如果运算结果超过 `precision` 指定的精度，则根据指定的精度对乘方结果进行舍入。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘方运算的指数值。
- precision: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 精度值。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储乘方运算结果值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘方运算结果标度值溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*
import std.math.*

main(): Unit {
    let A = Decimal(2.5)
    println("A.powWithPrecision(3, 0) = ${A.powWithPrecision(3, 0, roundingMode: HalfEven)}")
}
```

运行结果：

```text
A.powWithPrecision(3, 0) = 15.625
```

### func removeTrailingZeros()

```cangjie
public func removeTrailingZeros(): Decimal
```

功能：对当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象移除尾部零，不改变对象数值。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 新的无尾部零的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(1.00)
    println("A.removeTrailingZeros() = ${A.removeTrailingZeros()}")
}
```

运行结果：

```text
A.removeTrailingZeros() = 1
```

### func reScale(Int32, RoundingMode)

```cangjie
public func reScale(newScale: Int32, roundingMode!: RoundingMode = HalfEven): Decimal
```

功能：调整 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象标度值，允许指定舍入规则，返回标度调整后新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

参数：

- newScale: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 新的标度值。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 新的标度值的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(1.234568)
    println("A.reScale(3) = ${A.reScale(3)}")
}
```

运行结果：

```text
A.reScale(3) = 1.235
```