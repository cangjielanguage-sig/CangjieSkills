### func toIntNative(OverflowStrategy)

```cangjie
public func toIntNative(overflowHandling!: OverflowStrategy = Throwing): IntNative
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 返回转换后的 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("800000000000000000", radix: 16)
    let toIntNative = bigInt.toIntNative(overflowHandling: Wrapping)
    println(toIntNative)
}
```

运行结果：

```text
0
```

### func toString()

```cangjie
public func toString(): String
```

功能：计算并返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的十进制字符串表示。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的十进制字符串。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(0x400)
    let toString = bigInt.toString()
    println(toString)
}
```

运行结果：

```text
1024
```

### func toUInt16(OverflowStrategy)

```cangjie
public func toUInt16(overflowHandling!: OverflowStrategy = Throwing): UInt16
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 返回转换后的 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("800000000000000000", radix: 16)
    let toUInt16 = bigInt.toUInt16(overflowHandling: Wrapping)
    println(toUInt16)
}
```

运行结果：

```text
0
```