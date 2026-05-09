## func log2(Float16)

```cangjie
public func log2(x: Float16): Float16
```

功能：求以 2 为底 `x` 的对数。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 真数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回以 2 为底 `x` 的对数。

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
import std.math.log2

main() {
    let x: Float16 = 1024.0
    let log2 = log2(x)
    println(log2)
}
```

运行结果：

```text
10.000000
```

## func log2(Float32)

```cangjie
public func log2(x: Float32): Float32
```

功能：求以 2 为底 `x` 的对数。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 真数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回以 2 为底 `x` 的对数。

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
import std.math.log2

main() {
    let x: Float32 = 1024.0
    let log2 = log2(x)
    println(log2)
}
```

运行结果：

```text
10.000000
```

## func log2(Float64)

```cangjie
public func log2(x: Float64): Float64
```

功能：求以 2 为底 `x` 的对数。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 真数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回以 2 为底 `x` 的对数。

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
import std.math.log2

main() {
    let x: Float64 = 1024.0
    let log2 = log2(x)
    println(log2)
}
```

运行结果：

```text
10.000000
```