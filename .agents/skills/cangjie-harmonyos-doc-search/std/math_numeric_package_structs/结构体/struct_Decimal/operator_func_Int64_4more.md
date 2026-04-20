### operator func **(Int64)

```cangjie
public operator func **(n: Int64): Decimal
```

功能：乘方运算，乘方运算符重载，获取当前对象为底数，入参 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 为指数的乘方运算结果，其中指数为入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象的整数部分。

> **注意：**
>
> 指数为负值且结果为无限小数场景时，默认采用 IEEE 754-2019 decimal128 对结果进行舍入。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘方运算的指数值。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储乘方运算结果值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘方运算结果标度值溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2.5)
    println("A ** 3 = ${A ** 3}")
}
```

运行结果：

```text
A ** 3 = 15.625
```

### operator func +(Decimal)

```cangjie
public operator func +(d: Decimal): Decimal
```

功能：加法运算，加法运算符重载，加上入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回结果值。结果保留实际精度值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 加数对象。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储加法结果值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当两个加数标度值相减溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2)
    let B = Decimal(3)
    let C = A + B
    println("C = ${C}")
}
```

运行结果：

```text
C = 5
```

### operator func -()

```cangjie
public operator func -(): Decimal
```

功能：取反运算，一元负数运算符重载，对当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象取反，返回结果值。保留取反运算结果实际精度值。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储取反结果值。

### operator func -(Decimal)

```cangjie
public operator func -(d: Decimal): Decimal
```

功能：减法运算，减法运算符重载，减去入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回结果值。保留减法运算结果实际精度值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 减数对象。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储减法运算结果值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当被减数与减数标度值相减溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2)
    let B = Decimal(3)
    let C = A - B
    println("C = ${C}")
}
```

运行结果：

```text
C = -1
```