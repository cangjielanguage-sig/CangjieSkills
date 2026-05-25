### operator func -(BigInt)

```cangjie
public operator func -(that: BigInt): BigInt
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 减法。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 减数。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相减后的结果。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("100000000000000000")
    let that = BigInt.parse("-23456789123456789")
    let sub = bigInt - that
    println(sub)
}
```

运行结果：

```text
123456789123456789
```

### operator func <(BigInt)

```cangjie
public operator func <(that: BigInt): Bool
```

功能：小于比较运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 小于比较运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较的结果。小于返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt < that)
}
```

运行结果：

```text
false
```

### operator func <<(Int64)

```cangjie
public operator func <<(n: Int64): BigInt
```

功能：左移运算。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 左移 n 位，n 需要大于等于 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 左移 n 位的结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 入参小于 0 时抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let leftShift = bigInt << 64
    println(leftShift.toString(radix: 16))
}
```

运行结果：

```text
-10000000000000000
```

### operator func <=(BigInt)

```cangjie
public operator func <=(that: BigInt): Bool
```

功能：小于等于比较运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 小于等于比较运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 比较的结果。小于等于返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt <= that)
}
```

运行结果：

```text
false
```

### operator func ==(BigInt)

```cangjie
public operator func ==(that: BigInt): Bool
```

功能：判等运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 判等运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 判等的结果。相等返回 true，不等返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt == that)
}
```

运行结果：

```text
false
```