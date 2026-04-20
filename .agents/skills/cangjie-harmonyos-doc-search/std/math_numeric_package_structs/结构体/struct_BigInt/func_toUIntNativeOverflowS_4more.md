### func toUIntNative(OverflowStrategy)

```cangjie
public func toUIntNative(overflowHandling!: OverflowStrategy = Throwing): UIntNative
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 返回转换后的 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("-800000000000000000", radix: 16)
    let toUIntNative = bigInt.toUIntNative(overflowHandling: Saturating)
    println(toUIntNative)
}
```

运行结果：

```text
0
```

### operator func !()

```cangjie
public operator func !(): BigInt
```

功能：按位非。将操作数中的二进制位 0 变 1，1 变 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 按位非的结果。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let no = !bigInt
    println(no)
}
```

运行结果：

```text
0
```

### operator func !=(BigInt)

```cangjie
public operator func !=(that: BigInt): Bool
```

功能：判不等运算。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 判不等运算的另一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 判不等的结果。不等返回 true，相等返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-1")
    let that = BigInt.parse("-2")
    println(bigInt != that)
}
```

运行结果：

```text
true
```

### operator func %(BigInt)

```cangjie
public operator func %(that: BigInt): BigInt
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 的模运算。

取模运算的行为与基础类型保持一致，即符号与被除数保持一致。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 除数。除数不得为 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是此 [BigInt](math_numeric_package_structs.md#struct-bigint) 与另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 相模后的结果。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 除数为 0 抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("-23456789123456789")
    let that = BigInt.parse("-23456789123456789")
    let mod = bigInt % that
    println(mod)
}
```

运行结果：

```text
0
```