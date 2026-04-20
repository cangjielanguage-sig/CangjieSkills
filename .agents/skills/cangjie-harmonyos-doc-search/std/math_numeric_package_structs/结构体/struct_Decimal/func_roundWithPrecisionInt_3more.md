### func roundWithPrecision(Int64, RoundingMode)

```cangjie
public func roundWithPrecision(precision: Int64, roundingMode!: RoundingMode = RoundingMode.HalfEven): Decimal
```

功能：按照指定舍入精度和舍入规则对当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象进行舍入操作。

参数：

- precision: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 精度值。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 舍入操作生成的新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当舍入操作结果标度值溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal
import std.math.*

main(): Unit {
    let A = Decimal(1.0)
    println("A.roundWithPrecision(1.0) = ${A.roundWithPrecision(0, roundingMode: HalfEven)}")
    let B = Decimal(0.1f16).roundWithPrecision(5, roundingMode: Up)
    println("B = ${B}")
}
```

运行结果：

```text
A.roundWithPrecision(1.0) = 1
B = 0.099976
```

### func scaleUnit()

```cangjie
public func scaleUnit(): Decimal
```

功能：对当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象返回标度单位，即数值为 1 ，标度值与当前对象相等的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 标度单位 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(100)
    println("A.scaleUnit() = ${A.scaleUnit()}")
}
```

运行结果：

```text
A.scaleUnit() = 1
```

### func shiftPoint(Int32)

```cangjie
public func shiftPoint(n: Int32): Decimal
```

功能：移动当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象小数点 `abs(n)` 位返回结果对象，当 n 为正数时，左移小数点，n 为负数时，右移小数点，n 为零时，返回当前对象。

参数：

- n: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指定小数点移动位数及方向。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 对当前对象小数点移动指定位数后生成新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(25)
    println("A.shiftPoint(1) = ${A.shiftPoint(1)}")
}
```

运行结果：

```text
A.shiftPoint(1) = 2.5
```