### init(UIntNative)

```cangjie
public init(val: UIntNative)
```

功能：通过 32 位或 64 位（具体长度与平台相关）无符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 32 位或 64 位无符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let uintnative: UIntNative = 24
    let decimal = Decimal(uintnative)
    println(decimal)
}
```

运行结果：

```text
24
```

### func compare(Decimal)

```cangjie
public func compare(d: Decimal): Ordering
```

功能：比较当前对象与入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回比较结果值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 待比较对象。

返回值：

- [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 返回比较结果，当前对象小于入参时，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，大于入参时，返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，否则返回 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(-5)
    let B = Decimal(3)

    let C = A.compare(B)
    println(C)
}
```

运行结果：

```text
Ordering.LT
```

### func divAndMod(Decimal)

```cangjie
public func divAndMod(d: Decimal): (BigInt, Decimal)
```

功能：除法取商和余数运算，除以入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回整数商值和余数值。结果保留实际精度值。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 除数对象。

返回值：

- ([BigInt](math_numeric_package_structs.md#struct-bigint), [Decimal](math_numeric_package_structs.md#struct-decimal)) - 生成一个元组对象，分别用于存储整数商值结果和余数结果值。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当除数为 0 时，抛出此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法结果值范围超过 [-(maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)), maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)] 时，抛出此异常。