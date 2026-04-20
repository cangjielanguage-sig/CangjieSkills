## func clamp(Float64, Float64, Float64)

```cangjie
public func clamp(v: Float64, min: Float64, max: Float64): Float64
```

功能：求浮点数的范围区间数。如果此浮点数在该范围区间则返回此浮点数；如果此浮点数小于这个范围区间，则返回该范围区间的最小值；如果此浮点数大于这个范围区间，则返回该范围区间的最大值；如果是 `NaN` 则返回 `NaN`。

参数：

- v: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入一个浮点数。
- min: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 指定的最小值。
- max: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 指定的最大值。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 如果 `v` 在 `min` 与 `max` 之间则返回 `v`；如果 `v` 小于等于 `min` 则返回 `min`；如果 `v` 大于等于 `max`，则返回 `max`；如果是 `NaN` 则返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `min` 大于参数 `max` 或者 `min` 和 `max` 是 `NaN` 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.clamp

main() {
    let n: Float64 = -23.0
    let clamp = clamp(n, -100.0, 100.0)
    println(clamp)
}
```

运行结果：

```text
-23.000000
```

## func cos(Float16)

```cangjie
public func cos(x: Float16): Float16
```

功能：计算半精度浮点数的余弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数，入参单位为弧度。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cos

main() {
    let n: Float16 = 3.14159265
    let cos = cos(n)
    println(cos)
}
```

运行结果：

```text
-1.000000
```

## func cos(Float32)

```cangjie
public func cos(x: Float32): Float32
```

功能：计算单精度浮点数的余弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数，入参单位为弧度。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cos

main() {
    let n: Float32 = 3.14159265
    let cos = cos(n)
    println(cos)
}
```

运行结果：

```text
-1.000000
```

## func cos(Float64)

```cangjie
public func cos(x: Float64): Float64
```

功能：计算双精度浮点数的余弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数，入参单位为弧度。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cos

main() {
    let n: Float64 = 3.14159265
    let cos = cos(n)
    println(cos)
}
```

运行结果：

```text
-1.000000
```

## func cosh(Float16)

```cangjie
public func cosh(x: Float16): Float16
```

功能：计算半精度浮点数的双曲余弦函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的双曲余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cosh

main() {
    let n: Float16 = 0.0
    let cosh = cosh(n)
    println(cosh)
}
```

运行结果：

```text
1.000000
```