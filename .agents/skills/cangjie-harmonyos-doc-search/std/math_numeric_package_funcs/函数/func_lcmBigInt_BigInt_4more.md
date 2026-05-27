## func lcm(BigInt, BigInt)

```cangjie
public func lcm(i1: BigInt, i2: BigInt): BigInt
```

功能：求两个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的最小公倍数。入参为 0 时返回 0，其余情形总是返回正数（相当于绝对值的最小公倍数）。

参数：

- i1: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算最小公倍数的第一个入参。
- i2: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算最小公倍数的第二个入参。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回 `i1` 和 `i2` 的最小公倍数，入参为 0 时返回 0，其余情形总是返回正数（相当于绝对值的最小公倍数）。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let i1: BigInt = BigInt(-36)
    let i2: BigInt = BigInt(48)
    let lcm = lcm(i1, i2)
    println(lcm)
}
```

运行结果：

```text
144
```

## func round(Decimal, RoundingMode)

```cangjie
public func round(d: Decimal, roundingMode!: RoundingMode = RoundingMode.HalfEven): Decimal
```

功能：计算 [Decimal](math_numeric_package_structs.md#struct-decimal) 的舍入值，根据舍入方式向邻近的整数舍入。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - 需要计算舍入值的 [Decimal](math_numeric_package_structs.md#struct-decimal)。
- roundingMode!: [RoundingMode](../../math/math_package_api/math_package_enums.md#enum-roundingmode) - 舍入规则。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 舍入操作生成的新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当舍入操作结果标度值溢出时，抛出此异常。

## func sqrt(BigInt)

```cangjie
public func sqrt(i: BigInt): BigInt
```

功能：求 [BigInt](math_numeric_package_structs.md#struct-bigint) 的算术平方根，向下取整。

参数：

- i: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算算术平方根的 [BigInt](math_numeric_package_structs.md#struct-bigint)，入参需要非负。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的算术平方根，向下取整。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参为负数，则抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let n: BigInt = BigInt(23)
    let sqrt = sqrt(n)
    println(sqrt)
}
```

运行结果：

```text
4
```

## func sqrt(Decimal)

```cangjie
public func sqrt(d: Decimal): Decimal
```

功能：求 [Decimal](math_numeric_package_structs.md#struct-decimal) 的算术平方根。结果为无限小数场景时，默认采用 IEEE 754-2019 decimal128 对结果进行舍入。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - 需要计算算术平方根的 [Decimal](math_numeric_package_structs.md#struct-decimal)，入参需要非负。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 返回入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 的算术平方根。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参为负数，则抛此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当计算平方根操作结果标度值溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let n: Decimal = Decimal.parse("36")
    let sqrt = sqrt(n)
    println(sqrt)
}
```

运行结果：

```text
6
```