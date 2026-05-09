### func compare(BigInt)

```cangjie
public func compare(that: BigInt): Ordering
```

功能：判断 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的关系。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的关系。如果等于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT；如果大于，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1024)
    let that1 = BigInt(512)
    let that2 = BigInt(2048)
    let that3 = BigInt(1024)

    let compare1 = bigInt.compare(that1)
    println(compare1)

    let compare2 = bigInt.compare(that2)
    println(compare2)

    let compare3 = bigInt.compare(that3)
    println(compare3)
}
```

运行结果：

```text
Ordering.GT
Ordering.LT
Ordering.EQ
```

### func divAndMod(BigInt)

```cangjie
public func divAndMod(that: BigInt): (BigInt, BigInt)
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 的除法运算。

与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除，返回商和模。此除法运算的行为与基础类型保持一致，即商向靠近 0 的方向取整，模的符号与被除数保持一致。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- ([BigInt](math_numeric_package_structs.md#struct-bigint), [BigInt](math_numeric_package_structs.md#struct-bigint)) - 商和模。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1025)
    let that = BigInt(512)
    let (div, mod) = bigInt.divAndMod(that)
    println(div)
    println(mod)
}
```

运行结果：

```text
2
1
```

### func flipBit(Int64)

```cangjie
public func flipBit(index: Int64): BigInt
```

功能：通过翻转指定索引位置的 bit 来构造一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要翻转的 bit 位置的索引。`index` 需要大于等于 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新的 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是将原 [BigInt](math_numeric_package_structs.md#struct-bigint) `index` 处的 bit 翻转后的产物。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参 `index` 小于 0，则抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1024)
    let flipBit = bigInt.flipBit(10)
    println(flipBit)
}
```

运行结果：

```text
0
```