## func erf(Float64)

```cangjie
public func erf(x: Float64): Float64
```

功能：求双精度浮点数的误差值。相关定义是：$$erf(x) = \frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}dt$$。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的双精度浮点数的误差值。

示例：
<!-- verify -->
```cangjie
import std.math.erf

main() {
    let n: Float64 = 5.0
    let erf = erf(n)
    println(erf)
}
```

运行结果：

```text
1.000000
```

## func exp(Float16)

```cangjie
public func exp(x: Float16): Float16
```

功能：求自然常数 e 的 `x` 次幂。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数指数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回自然常数 e 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp

main() {
    let n: Float16 = 1.0
    let exp = exp(n)
    println(exp)
}
```

运行结果：

```text
2.718750
```

## func exp(Float32)

```cangjie
public func exp(x: Float32): Float32
```

功能：求自然常数 e 的 `x` 次幂。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数指数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回自然常数 e 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp

main() {
    let n: Float32 = 1.0
    let exp = exp(n)
    println(exp)
}
```

运行结果：

```text
2.718282
```

## func exp(Float64)

```cangjie
public func exp(x: Float64): Float64
```

功能：求自然常数 e 的 `x` 次幂。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数指数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回自然常数 e 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp

main() {
    let n: Float64 = 1.0
    let exp = exp(n)
    println(exp)
}
```

运行结果：

```text
2.718282
```

## func exp2(Float16)

```cangjie
public func exp2(x: Float16): Float16
```

功能：求 2 的 `x` 次幂。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数指数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回 2 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp2

main() {
    let n: Float16 = 10.0
    let exp2 = exp2(n)
    println(exp2)
}
```

运行结果：

```text
1024.000000
```

## func exp2(Float32)

```cangjie
public func exp2(x: Float32): Float32
```

功能：求 2 的 `x` 次幂。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数指数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回 2 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp2

main() {
    let n: Float32 = 10.0
    let exp2 = exp2(n)
    println(exp2)
}
```

运行结果：

```text
1024.000000
```

## func exp2(Float64)

```cangjie
public func exp2(x: Float64): Float64
```

功能：求 2 的 `x` 次幂。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数指数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回 2 的 `x` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.exp2

main() {
    let n: Float64 = 10.0
    let exp = exp2(n)
    println(exp)
}
```

运行结果：

```text
1024.000000
```