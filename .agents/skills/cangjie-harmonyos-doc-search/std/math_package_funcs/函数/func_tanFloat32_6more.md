## func tan(Float32)

```cangjie
public func tan(x: Float32): Float32
```

功能：计算单精度浮点数的正切函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数，入参单位为弧度。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tan

main() {
    let n: Float32 = 0.0
    let tan = tan(n)
    println(tan)
}
```

运行结果：

```text
0.000000
```

## func tan(Float64)

```cangjie
public func tan(x: Float64): Float64
```

功能：计算双精度浮点数的正切函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数，入参单位为弧度。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tan

main() {
    let n: Float64 = 0.0
    let tan = tan(n)
    println(tan)
}
```

运行结果：

```text
0.000000
```

## func tanh(Float16)

```cangjie
public func tanh(x: Float16): Float16
```

功能：计算半精度浮点数的双曲正切函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的双曲正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tanh

main() {
    let n: Float16 = 0.0
    let tanh = tanh(n)
    println(tanh)
}
```

运行结果：

```text
0.000000
```

## func tanh(Float32)

```cangjie
public func tanh(x: Float32): Float32
```

功能：计算单精度浮点数的双曲正切函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的双曲正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tanh

main() {
    let n: Float32 = 0.0
    let tanh = tanh(n)
    println(tanh)
}
```

运行结果：

```text
0.000000
```

## func tanh(Float64)

```cangjie
public func tanh(x: Float64): Float64
```

功能：计算双精度浮点数的双曲正切函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的双曲正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tanh

main() {
    let n: Float64 = 0.0
    let tanh = tanh(n)
    println(tanh)
}
```

运行结果：

```text
0.000000
```

## func trailingZeros(Int16)

```cangjie
public func trailingZeros(x: Int16): Int64
```

功能：求 16 位有符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: Int16 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```