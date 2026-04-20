### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：计算并返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的哈希值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1024)
    let hashCode = bigInt.hashCode()
    println(hashCode)
}
```

运行结果：

```text
1024
```

### func isProbablePrime(UInt64)

```cangjie
public func isProbablePrime(certainty: UInt64): Bool
```

功能：判断一个数是不是素数。

> **说明：**
>
> 该函数使用了 Miller-Rabin 测试算法，此算法的准确率会随着 certainty 参数的增加而增加。如果该数是素数，那么 Miller-Rabin 测试必定返回 true；如果该数是合数（期待返回 false），那么会有低于 1/4<sup>certainty</sup> 概率返回 true。素数只对大于等于 2 的正整数有意义，即负数，0，1 都不是素数。

参数：

- certainty: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 需要执行 Miller-Rabin 测试的次数。注意，如果测试次数为 0，表示不测试，那么总是返回 true（即不是素数的数也必定返回 true）。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果使用此函数测定了一个数为素数，则返回 true；不为素数，则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1024)
    let isProbablePrime = bigInt.isProbablePrime(10)
    println(isProbablePrime)
}
```

运行结果：

```text
false
```

### func lowestOneBit() <sup>(deprecated)</sup>

```cangjie
public func lowestOneBit(): Int64
```

功能：判断为 1 的最低位的 bit 的位置。

> **注意：**
>
> 未来版本即将废弃，使用 [trailingZeros(BigInt)](./math_numeric_package_funcs.md#func-trailingzerosbigint) 替代。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回为 1 的最低位的 bit 的位置。如果 bit 全为 0，则返回 -1。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(-1)
    let lowestOneBit = bigInt.lowestOneBit()
    println(lowestOneBit)
}
```

运行结果：

```text
0
```

### func modInverse(BigInt)

```cangjie
public func modInverse(that: BigInt): BigInt
```

功能：求模逆元。

模逆元 r 满足 $(this * r) \% that == 1$。显然，`this` 和 `that` 必须互质。当 `that` 为 正负 1 时，结果总是 0。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。入参不得为 0，且需要与 `this` 互质。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回模逆元。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `this` 和 `that` 不互质或 `that` 为 0 时，抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1025)
    let that = BigInt(512)
    let modInverse = bigInt.modInverse(that)
    println(modInverse)
}
```

运行结果：

```text
1
```