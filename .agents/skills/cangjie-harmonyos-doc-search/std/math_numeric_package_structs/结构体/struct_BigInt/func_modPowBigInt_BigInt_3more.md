### func modPow(BigInt, ?BigInt)

```cangjie
public func modPow(n: BigInt, m!: ?BigInt = None): BigInt
```

功能：计算此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的 n 次幂模 `m` 的结果，并返回。

模的规则与基础类型一致，即模的符号与被除数保持一致。

参数：

- n: [BigInt](math_numeric_package_structs.md#struct-bigint) - 指数，必须为非负数。
- m!: ?[BigInt](math_numeric_package_structs.md#struct-bigint) - 除数，此入参不得为 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 乘方后取模的运算结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 指数为负数时抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(2)
    let n = BigInt(10)
    let modPow = bigInt.modPow(n)
    println(modPow)
}
```

运行结果：

```text
1024
```

### func quo(BigInt) <sup>(deprecated)</sup>

```cangjie
public func quo(that: BigInt): BigInt
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 的除法运算。

与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除，返回结果。此除法运算的行为与[运算符重载函数](#operator-func-bigint-10)区别于，如果被除数为负数，此函数的结果向着远离 0 的方向取整，保证余数大于等于 0。

> **注意：**
>
> 未来版本即将废弃。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除后的结果

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1025)
    let that = BigInt(512)
    let quo = bigInt.quo(that)
    println(quo)
}
```

运行结果：

```text
2
```

### func quoAndRem(BigInt) <sup>(deprecated)</sup>

```cangjie
public func quoAndRem(that: BigInt): (BigInt, BigInt)
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 的除法运算。

与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除，返回商和余数。此除法运算的行为与 [divAndMod](#func-divandmodbigint) 函数区别于，如果被除数为负数，此函数的结果向着远离 0 的方向取整，保证余数总是大于等于 0。

> **注意：**
>
> 未来版本即将废弃。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- ([BigInt](math_numeric_package_structs.md#struct-bigint), [BigInt](math_numeric_package_structs.md#struct-bigint)) - 商和余数。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1025)
    let that = BigInt(512)
    let (quo, rem) = bigInt.quoAndRem(that)
    println(quo)
    println(rem)
}
```

运行结果：

```text
2
1
```