## func round(Float32)

```cangjie
public func round(x: Float32): Float32
```

功能：此函数采用 IEEE-754 的向最近舍入规则，计算浮点数的舍入值。如果该浮点数有两个最近整数，则向偶数舍入。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 需要计算舍入值的浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回浮点数向最近整数方向的舍入值。如果该浮点数有两个最近整数，则返回向偶数舍入值。

示例：
<!-- verify -->
```cangjie
import std.math.round

main() {
    let n: Float32 = 1.5
    let round = round(n)
    println(round)
}
```

运行结果：

```text
2.000000
```

## func round(Float64)

```cangjie
public func round(x: Float64): Float64
```

功能：此函数采用 IEEE-754 的向最近舍入规则，计算浮点数的舍入值。如果该浮点数有两个最近整数，则向偶数舍入。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 需要计算舍入值的浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回浮点数向最近整数方向的舍入值。如果该浮点数有两个最近整数，则返回向偶数舍入值。

示例：
<!-- verify -->
```cangjie
import std.math.round

main() {
    let n: Float64 = 1.5
    let round = round(n)
    println(round)
}
```

运行结果：

```text
2.000000
```

## func sin(Float16)

```cangjie
public func sin(x: Float16): Float16
```

功能：计算半精度浮点数的正弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数，入参单位为弧度。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sin

main() {
    let n: Float16 = 3.1415926 / 2.0
    let sin = sin(n)
    println(sin)
}
```

运行结果：

```text
1.000000
```

## func sin(Float32)

```cangjie
public func sin(x: Float32): Float32
```

功能：计算单精度浮点数的正弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数，入参单位为弧度。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sin

main() {
    let n: Float32 = 3.1415926 / 2.0
    let sin = sin(n)
    println(sin)
}
```

运行结果：

```text
1.000000
```

## func sin(Float64)

```cangjie
public func sin(x: Float64): Float64
```

功能：计算双精度浮点数的正弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数，入参单位为弧度。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sin

main() {
    let n: Float64 = 3.1415926 / 2.0
    let sin = sin(n)
    println(sin)
}
```

运行结果：

```text
1.000000
```

## func sinh(Float16)

```cangjie
public func sinh(x: Float16): Float16
```

功能：计算半精度浮点数的双曲正弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sinh

main() {
    let n: Float16 = 0.0
    let sinh = sinh(n)
    println(sinh)
}
```

运行结果：

```text
0.000000
```