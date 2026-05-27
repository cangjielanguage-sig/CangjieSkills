## func abs(BigInt)

```cangjie
public func abs(i: BigInt): BigInt
```

功能：求一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的绝对值。

参数：

- i: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算绝对值的 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的绝对值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let n: BigInt = BigInt(-23)
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23
```

## func abs(Decimal)

```cangjie
public func abs(d: Decimal): Decimal
```

功能：求一个 [Decimal](math_numeric_package_structs.md#struct-decimal) 的绝对值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - 需要计算绝对值的 [Decimal](math_numeric_package_structs.md#struct-decimal)。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 返回入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 的绝对值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let d: Decimal = Decimal.parse("-1.23")
    let abs = abs(d)
    println(abs)
}
```

运行结果：

```text
1.23
```

## func countOne(BigInt) <sup>(deprecated)</sup>

```cangjie
public func countOne(i: BigInt): Int64
```

功能：计算并返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的二进制补码中 1 的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(BigInt)](#func-countonesbigint) 替代。

参数：

- i: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算二进制补码中 1 的个数的 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的二进制补码中 1 的个数。

## func countOnes(BigInt)

```cangjie
public func countOnes(i: BigInt): Int64
```

功能：计算并返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的二进制补码中 1 的个数。

参数：

- i: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算二进制补码中 1 的个数的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回入参 [BigInt](math_numeric_package_structs.md#struct-bigint) 的二进制补码中 1 的个数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let i: BigInt = BigInt(255)
    let countOnes = countOnes(i)
    println(countOnes)
}
```

运行结果：

```text
8
```

## func gcd(BigInt, BigInt)

```cangjie
public func gcd(i1: BigInt, i2: BigInt): BigInt
```

功能：求两个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的最大公约数。总是返回非负数（相当于绝对值的最大公约数）。

参数：

- i1: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算最大公约数的第一个入参。
- i2: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要计算最大公约数的第二个入参。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回 `i1` 和 `i2` 的最大公约数，总是返回非负数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.*

main() {
    let i1: BigInt = BigInt(-36)
    let i2: BigInt = BigInt(48)
    let gcd = gcd(i1, i2)
    println(gcd)
}
```

运行结果：

```text
12
```