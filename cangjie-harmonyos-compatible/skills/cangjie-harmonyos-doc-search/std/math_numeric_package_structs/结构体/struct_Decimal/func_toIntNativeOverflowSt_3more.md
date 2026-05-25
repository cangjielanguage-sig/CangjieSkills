### func toIntNative(OverflowStrategy)

```cangjie
public func toIntNative(overflowHandling!: OverflowStrategy = Throwing): IntNative
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 转换后的 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(6.25)
    println("A.toInt8() = ${A.toInt8()}")
    println("A.toInt16() = ${A.toInt16()}")
    println("A.toInt32() = ${A.toInt32()}")
    println("A.toInt64() = ${A.toInt64()}")
    println("A.toIntNative() = ${A.toIntNative()}")
}
```

运行结果：

```text
A.toInt8() = 6
A.toInt16() = 6
A.toInt32() = 6
A.toInt64() = 6
A.toIntNative() = 6
```

### func toSciString()

```cangjie
public func toSciString(): String
```

功能：以科学计数法的形式打印输出 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，当值小于 0 时以 “-” 开头后跟十进制数字，大于等于 0 时，直接打印输出数字，不额外添加 “+”。指数小于 0 时同样遵循以上规则。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 科学计数法形式的 [Decimal](math_numeric_package_structs.md#struct-decimal) 字符串。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(6.25)
    println("A.toFloat16() = ${A.toFloat16()}")
    println("A.toFloat32() = ${A.toFloat32()}")
    println("A.toFloat64() = ${A.toFloat64()}")
    println("A.toBigInt() = ${A.toBigInt()}")
    println("A.toEngString() = ${A.toEngString()}")
    println("A.toSciString() = ${A.toSciString()}")
}
```

运行结果：

```text
A.toFloat16() = 6.250000
A.toFloat32() = 6.250000
A.toFloat64() = 6.250000
A.toBigInt() = 6
A.toEngString() = 6.25E0
A.toSciString() = 6.25E0
```

### func toString()

```cangjie
public func toString(): String
```

功能：以不带指数形式打印输出 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，小于 0 时以 “-” 开头后跟十进制数字，大于等于 0 时，直接打印输出数字，不额外添加 “+”。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 不带指数形式的 [Decimal](math_numeric_package_structs.md#struct-decimal) 字符串。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(-5)
    let B = Decimal(3 ** 5)

    println("A.hashCode() = ${A.hashCode()}")
    println("B.toString() = ${B.toString()}")
}
```

运行结果：

```text
A.hashCode() = 155
B.toString() = 243
```