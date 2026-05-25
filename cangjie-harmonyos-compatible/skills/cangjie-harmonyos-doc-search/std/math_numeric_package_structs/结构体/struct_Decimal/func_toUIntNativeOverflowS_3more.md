### func toUIntNative(OverflowStrategy)

```cangjie
public func toUIntNative(overflowHandling!: OverflowStrategy = Throwing): UIntNative
```

功能：将当前 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象转化为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 转换后的 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(6.25)
    println("A.toUInt8() = ${A.toUInt8()}")
    println("A.toUInt16() = ${A.toUInt16()}")
    println("A.toUInt32() = ${A.toUInt32()}")
    println("A.toUInt64() = ${A.toUInt64()}")
    println("A.toUIntNative() = ${A.toUIntNative()}")
}
```

运行结果：

```text
A.toUInt8() = 6
A.toUInt16() = 6
A.toUInt32() = 6
A.toUInt64() = 6
A.toUIntNative() = 6
```

### operator func !=(Decimal)

```cangjie
public operator func !=(d: Decimal): Bool
```

功能：不等比较运算，不等运算符重载，判断入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象与当前对象是否不相等，返回比较结果值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 待比较对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回不等比较运算结果。当前对象不等于入参时，返回 true，否则返回 false。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(-5)
    let B = Decimal(3)

    println("-A = ${-A}")
    println("A <= B = ${A <= B}")
    println("A != B = ${A != B}")
}
```

运行结果：

```text
-A = 5
A <= B = true
A != B = true
```

### operator func *(Decimal)

```cangjie
public operator func *(d: Decimal): Decimal
```

功能：乘法运算，乘法运算符重载，乘以入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回结果值。保留乘法运算结果实际精度值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 乘数对象。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储乘法运算结果值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当两个乘数标度值相加溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2)
    let B = Decimal(3)
    let C = A * B
    println("C = ${C}")
}
```

运行结果：

```text
C = 6
```