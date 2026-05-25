## func asin(Float32)

```cangjie
public func asin(x: Float32): Float32
```

功能：计算单精度浮点数的反正弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。-1.0 <= `x` <= 1.0。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的反正弦函数值，单位为弧度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于 1.0 或小于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.asin

main() {
    let n: Float32 = 0.0
    let asin = asin(n)
    println(asin)
}
```

运行结果：

```text
0.000000
```

## func asin(Float64)

```cangjie
public func asin(x: Float64): Float64
```

功能：计算双精度浮点数的反正弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。-1.0 <= `x` <= 1.0。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的反正弦函数值，单位为弧度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于 1.0 或小于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.asin

main() {
    let n: Float64 = 0.0
    let asin = asin(n)
    println(asin)
}
```

运行结果：

```text
0.000000
```

## func asinh(Float16)

```cangjie
public func asinh(x: Float16): Float16
```

功能：计算半精度浮点数的反双曲正弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的反双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.asinh

main() {
    let n: Float16 = 0.0
    let asinh = asinh(n)
    println(asinh)
}
```

运行结果：

```text
0.000000
```

## func asinh(Float32)

```cangjie
public func asinh(x: Float32): Float32
```

功能：计算单精度浮点数的反双曲正弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的反双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.asinh

main() {
    let n: Float32 = 0.0
    let asinh = asinh(n)
    println(asinh)
}
```

运行结果：

```text
0.000000
```

## func asinh(Float64)

```cangjie
public func asinh(x: Float64): Float64
```

功能：计算双精度浮点数的反双曲正弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的反双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.asinh

main() {
    let n: Float64 = 0.0
    let asinh = asinh(n)
    println(asinh)
}
```

运行结果：

```text
0.000000
```

## func atan(Float16)

```cangjie
public func atan(x: Float16): Float16
```

功能：计算半精度浮点数的反正切函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.atan

main() {
    let n: Float16 = 0.0
    let atan = atan(n)
    println(atan)
}
```

运行结果：

```text
0.000000
```