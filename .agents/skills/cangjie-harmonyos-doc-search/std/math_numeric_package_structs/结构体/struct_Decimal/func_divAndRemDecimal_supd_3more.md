### func divAndRem(Decimal) <sup>(deprecated)</sup>

```cangjie
public func divAndRem(d: Decimal): (BigInt, Decimal)
```

功能：除法取商和余数运算，除以入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回整数商值和余数值。结果保留实际精度值。

> **注意：**
>
> 未来版本即将废弃，使用 [divAndMod(Decimal)](#func-divandmoddecimal) 替代。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 除数对象。

返回值：

- ([BigInt](math_numeric_package_structs.md#struct-bigint), [Decimal](math_numeric_package_structs.md#struct-decimal)) - 生成一个元组对象，分别用于存储整数商值结果和余数结果值。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当除数为 0 时，抛出此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法结果值范围超过 [-(maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)), maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)] 时，抛出此异常。

### func divWithPrecision(Decimal, Int64, RoundingMode)

```cangjie
public func divWithPrecision(d: Decimal, precision: Int64, roundingMode!: RoundingMode = HalfEven): Decimal
```

功能：除法运算，支持自定义运算精度和舍入方式，除以入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回结果值，如果结果精度超过 `precision` 指定精度，则根据指定的精度对除法运算结果进行舍入。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 除数对象。
- precision: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 精度值。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储除法运算结果值。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当除数为 0 时，抛出此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法结果值范围超过 [-(maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)), maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)] 时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2)
    let B = Decimal(3)
    let C = A.divWithPrecision(B, 0)
    println("C = ${C}")
}
```

运行结果：

```text
C = 0.6666666666666666666666666666666667
```

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取当前对象哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回当前对象哈希值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let decimal = Decimal(24)
    let hashcode = decimal.hashCode()
    println(hashcode)
}
```

运行结果：

```text
744
```