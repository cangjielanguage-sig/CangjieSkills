## func leadingZeros(UInt8)

```cangjie
public func leadingZeros(x: UInt8): Int64
```

功能：求 8 位无符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: UInt8 = 64
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
1
```

## func log(Float16)

```cangjie
public func log(x: Float16): Float16
```

功能：求以 e 为底 `x` 的对数。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 真数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回以 e 为底 `x` 的对数。

> **说明：**
>
> 返回值存在如下特殊场景：
>
> - 如果传入 `x` 小于 0 或为 [NaN](../../core/core_package_api/core_package_intrinsics.md)，返回 [NaN](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 等于 0，返回 -[Inf](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 为 [Inf](../../core/core_package_api/core_package_intrinsics.md)，返回 [Inf](../../core/core_package_api/core_package_intrinsics.md)。

示例：
<!-- verify -->
```cangjie
import std.math.log

main() {
    let x: Float16 = 2.718282
    let log1 = log(x)
    let log2 = log(-x)
    let log3 = log(0.0)

    println(log1)
    println(log2)
    println(log3)

    let log4 = -log3
    println(log4)
}
```

运行结果：

```text
1.000000
nan
-inf
inf
```

## func log(Float32)

```cangjie
public func log(x: Float32): Float32
```

功能：求以 e 为底 `x` 的对数。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 真数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回以 e 为底 `x` 的对数。

> **说明：**
>
> 返回值存在如下特殊场景：
>
> - 如果传入 `x` 小于 0 或为 [NaN](../../core/core_package_api/core_package_intrinsics.md)，返回 [NaN](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 等于 0，返回 -[Inf](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 为 [Inf](../../core/core_package_api/core_package_intrinsics.md)，返回 [Inf](../../core/core_package_api/core_package_intrinsics.md)。

示例：
<!-- verify -->
```cangjie
import std.math.log

main() {
    let x: Float32 = 2.718282
    let log = log(x)
    println(log)
}
```

运行结果：

```text
1.000000
```

## func log(Float64)

```cangjie
public func log(x: Float64): Float64
```

功能：求以 e 为底 `x` 的对数。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 真数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回以 e 为底 `x` 的对数。

> **说明：**
>
> 返回值存在如下特殊场景：
>
> - 如果传入 `x` 小于 0 或为 [NaN](../../core/core_package_api/core_package_intrinsics.md)，返回 [NaN](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 等于 0，返回 -[Inf](../../core/core_package_api/core_package_intrinsics.md)。
> - 如果传入 `x` 为 [Inf](../../core/core_package_api/core_package_intrinsics.md)，返回 [Inf](../../core/core_package_api/core_package_intrinsics.md)。

示例：
<!-- verify -->
```cangjie
import std.math.log

main() {
    let x: Float64 = 2.718282
    let log = log(x)
    println(log)
}
```

运行结果：

```text
1.000000
```