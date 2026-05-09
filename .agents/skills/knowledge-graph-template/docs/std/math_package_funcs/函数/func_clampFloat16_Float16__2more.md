## func clamp(Float16, Float16, Float16)

```cangjie
public func clamp(v: Float16, min: Float16, max: Float16): Float16
```

功能：求浮点数的范围区间数。如果此浮点数在该范围区间则返回此浮点数；如果此浮点数小于这个范围区间，则返回该范围区间的最小值；如果此浮点数大于这个范围区间，则返回该范围区间的最大值；如果是 `NaN` 则返回 `NaN`。

参数：

- v: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入一个浮点数。
- min: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 指定的最小值。
- max: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 指定的最大值。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 如果 `v` 在 `min` 与 `max` 之间则返回 `v`；如果 `v` 小于等于 `min` 则返回 `min`；如果 `v` 大于等于 `max`，则返回 `max`；如果是 `NaN` 则返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `min` 大于参数 `max` 或者 `min` 和 `max` 是 `NaN` 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.clamp

main() {
    let n: Float16 = -23.0
    let clamp = clamp(n, -100.0, 100.0)
    println(clamp)
}
```

运行结果：

```text
-23.000000
```

## func clamp(Float32, Float32, Float32)

```cangjie
public func clamp(v: Float32, min: Float32, max: Float32): Float32
```

功能：求浮点数的范围区间数。如果此浮点数在该范围区间则返回此浮点数；如果此浮点数小于这个范围区间，则返回该范围区间的最小值；如果此浮点数大于这个范围区间，则返回该范围区间的最大值；如果是 `NaN` 则返回 `NaN`。

参数：

- v: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入一个浮点数。
- min: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 指定的最小值。
- max: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 指定的最大值。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 如果 `v` 在 `min` 与 `max` 之间则返回 `v`；如果 `v` 小于等于 `min` 则返回 `min`；如果 `v` 大于等于 `max`，则返回 `max`；如果是 `NaN` 则返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `min` 大于参数 `max` 或者 `min` 和 `max` 是 `NaN` 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.math.clamp

main() {
    var m: Float32 = -23.0
    var clamp1 = clamp(m, -100.0, 100.0)
    println(clamp1)

    var n: Float32 = -123.0
    var clamp2 = clamp(n, -100.0, 100.0)
    println(clamp2)

    var p: Float32 = 123.0
    var clamp3 = clamp(p, -100.0, 100.0)
    println(clamp3)
}
```

运行结果：

```text
-23.000000
-100.000000
100.000000
```