## func abs(Int8)

```cangjie
public func abs(x: Int8): Int8
```

功能：求一个 8 位有符号整数的绝对值。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的 8 位有符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的绝对值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当输入参数是有符号整数的最小值，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Int8 = -23
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23
```

## func acos(Float16)

```cangjie
public func acos(x: Float16): Float16
```

功能：计算半精度浮点数的反余弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。-1.0 <= `x` <= 1.0。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的反余弦函数值，单位为弧度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于 1.0 或小于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.acos

main() {
    let n: Float16 = 1.0
    let acos = acos(n)
    println(acos)
}
```

运行结果：

```text
0.000000
```

以下示例将抛出异常：
<!-- run.error -->
```cangjie
import std.math.acos

main(): Unit {
    let n = -1.5
    let acos = acos(n)
    println(acos)
}
```

## func acos(Float32)

```cangjie
public func acos(x: Float32): Float32
```

功能：计算单精度浮点数的反余弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。-1.0 <= `x` <= 1.0。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的反余弦函数值，单位为弧度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于 1.0 或小于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.acos

main() {
    let n: Float32 = 1.0
    let acos = acos(n)
    println(acos)
}
```

运行结果：

```text
0.000000
```

## func acos(Float64)

```cangjie
public func acos(x: Float64): Float64
```

功能：计算双精度浮点数的反余弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。-1.0 <= `x` <= 1.0。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的反余弦函数值，单位为弧度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于 1.0 或小于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.acos

main() {
    let n: Float64 = 1.0
    let acos = acos(n)
    println(acos)
}
```

运行结果：

```text
0.000000
```