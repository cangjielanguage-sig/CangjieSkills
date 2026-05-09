### func toFloat16()

```cangjie
public func toFloat16(): Float16
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 转换后的 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(32)
    let toFloat16 = bigInt.toFloat16()
    println(toFloat16)
}
```

运行结果：

```text
32.000000
```

### func toFloat32()

```cangjie
public func toFloat32(): Float32
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 转换后的 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(32)
    let toFloat32 = bigInt.toFloat32()
    println(toFloat32)
}
```

运行结果：

```text
32.000000
```

### func toFloat64()

```cangjie
public func toFloat64(): Float64
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 转换后的 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 值，溢出时，当前值为正数，返回 `inf`，当前值为负数，返回 `-inf`。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(32)
    let toFloat64 = bigInt.toFloat64()
    println(toFloat64)
}
```

运行结果：

```text
32.000000
```

### func toInt16(OverflowStrategy)

```cangjie
public func toInt16(overflowHandling!: OverflowStrategy = Throwing): Int16
```

功能：将当前 [BigInt](math_numeric_package_structs.md#struct-bigint) 对象转化为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型，支持自定义溢出策略。

参数：

- overflowHandling!: [OverflowStrategy](math_numeric_package_enums.md#enum-overflowstrategy) - 转换溢出策略。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 返回转换后的 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当不指定溢出策略或溢出策略为 `throwing` 转换溢出时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.OverflowStrategy

main() {
    let bigInt = BigInt(0x8000_0000_0000)
    let toInt16 = bigInt.toInt16(overflowHandling: Saturating)
    println(toInt16)
}
```

运行结果：

```text
32767
```