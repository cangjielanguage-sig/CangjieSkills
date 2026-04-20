### operator func >(BigInt)

```cangjie
public operator func >(that: BigInt): Bool
```

功能：大于比较运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 大于比较运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较的结果。大于返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt > that)
}
```

运行结果：

```text
true
```

### operator func >=(BigInt)

```cangjie
public operator func >=(that: BigInt): Bool
```

功能：大于等于比较运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 大于等于比较运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较的结果。大于等于返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt >= that)
}
```

运行结果：

```text
true
```

### operator func >>(Int64)

```cangjie
public operator func >>(n: Int64): BigInt
```

功能：右移运算。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 右移 n 位，n 需要大于等于 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 右移 n 位的结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 入参小于 0 时抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let rightShift = bigInt >> 10000
    println(rightShift)
}
```

运行结果：

```text
-1
```

### operator func \/(BigInt)

```cangjie
public operator func /(that: BigInt): BigInt
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 除法。

除法运算的行为与基础类型保持一致，即结果向靠近 0 的方向取整。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相除后的结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-23456789123456789")
    let that = BigInt.parse("-23456789123456789")
    let div = bigInt / that
    println(div)
}
```

运行结果：

```text
1
```

### operator func ^(BigInt)

```cangjie
public operator func ^(that: BigInt): BigInt
```

功能：按位异或。其功能是参与运算的两数各对应的二进位相异或。二进制位结果不相同时，异或结果为 1；二进制位结果相同时，异或结果为 0。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 按位异或运算的另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的按位异或的结果。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("7")
    let xor = bigInt ^ that
    println(xor)
}
```

运行结果：

```text
-8
```