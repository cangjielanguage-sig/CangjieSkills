## func log10(Float16)

```cangjie
public func log10(x: Float16): Float16
```

功能：求以 10 为底 `x` 的对数。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 真数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回以 10 为底 `x` 的对数。

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
import std.math.log10

main() {
    let x: Float16 = 1000.0
    let log10 = log10(x)
    println(log10)
}
```

运行结果：

```text
3.000000
```

## func log10(Float32)

```cangjie
public func log10(x: Float32): Float32
```

功能：求以 10 为底 `x` 的对数。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 真数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回以 10 为底 `x` 的对数。

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
import std.math.log10

main() {
    let x: Float32 = 1000.0
    let log10 = log10(x)
    println(log10)
}
```

运行结果：

```text
3.000000
```

## func log10(Float64)

```cangjie
public func log10(x: Float64): Float64
```

功能：求以 10 为底 `x` 的对数。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 真数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回以 10 为底 `x` 的对数。

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
import std.math.log10

main() {
    let x: Float64 = 1000.0
    let log10 = log10(x)
    println(log10)
}
```

运行结果：

```text
3.000000
```