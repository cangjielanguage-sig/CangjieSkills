### func toUInt32(OverflowStrategy)

```cangjie
public func toUInt32(overflowHandling!: OverflowStrategy = Throwing): UInt32
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 返回转换后的 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("800000000000000000", radix: 16)
    let toUInt32 = bigInt.toUInt32(overflowHandling: Wrapping)
    println(toUInt32)
}
```

运行结果：

```text
0
```

### func toUInt64(OverflowStrategy)

```cangjie
public func toUInt64(overflowHandling!: OverflowStrategy = Throwing): UInt64
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 返回转换后的 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("-800000000000000000", radix: 16)
    let toUInt64 = bigInt.toUInt64(overflowHandling: Saturating)
    println(toUInt64)
}
```

运行结果：

```text
0
```

### func toUInt8(OverflowStrategy)

```cangjie
public func toUInt8(overflowHandling!: OverflowStrategy = Throwing): UInt8
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 返回转换后的 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt.parse("800000000000000000", radix: 16)
    try {
        bigInt.toUInt8(overflowHandling: Throwing)
    } catch (e: OverflowException) {
        println(e.message)
    }
    return
}
```

运行结果：

```text
Out of range of the UInt8.
```