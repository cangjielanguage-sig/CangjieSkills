### func rem(BigInt) <sup>(deprecated)</sup>

```cangjie
public func rem(that: BigInt): BigInt
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 的模运算。

与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除，返回余数。余数的结果总是大于等于 0。

> **注意：**
>
> 未来版本即将废弃。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除后的余数。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1025)
    let that = BigInt(512)
    let rem = bigInt.rem(that)
    println(rem)
}
```

运行结果：

```text
1
```

### func setBit(Int64)

```cangjie
public func setBit(index: Int64): BigInt
```

功能：通过将指定索引位置的 bit 修改为 1 来构造一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要设置的 bit 位置的索引。`index` 需要大于等于 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新的 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是将原 [BigInt](math_numeric_package_structs.md#struct-bigint) `index` 处的 bit 改为 1 的产物。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参 `index` 小于 0，则抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(0)
    let setBit = bigInt.setBit(10)
    println(setBit)
}
```

运行结果：

```text
1024
```

### func testBit(Int64)

```cangjie
public func testBit(index: Int64): Bool
```

功能：判断指定位置的 bit 信息，如果指定位置的 bit 为 0，则返回 false；为 1，则返回 true。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要知道的 bit 的索引。`index` 需要大于等于 0。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 指定位置的 bit 信息。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参 `index` 小于 0，则抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(-1)
    let testBit = bigInt.testBit(100)
    println(testBit)
}
```

运行结果：

```text
true
```

### func toBytes()

```cangjie
public func toBytes(): Array<Byte>
```

功能：计算并返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的大端补码字节数组。

字节数组最低索引的最低位为符号位，如 128 返回 [0, 128]（符号位为 0），-128 返回 [128]（符号位为 1）。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的大端补码字节数组。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(0x400)
    let toBytes = bigInt.toBytes()
    println(toBytes)
}
```

运行结果：

```text
[4, 0]
```