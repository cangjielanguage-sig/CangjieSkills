## func atan(Float32)

```cangjie
public func atan(x: Float32): Float32
```

功能：计算单精度浮点数的反正切函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.atan

main() {
    let n: Float32 = 0.0
    let atan = atan(n)
    println(atan)
}
```

运行结果：

```text
0.000000
```

## func atan(Float64)

```cangjie
public func atan(x: Float64): Float64
```

功能：计算双精度浮点数的反正切函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.atan

main() {
    let n: Float64 = 0.0
    let atan = atan(n)
    println(atan)
}
```

运行结果：

```text
0.000000
```

## func atan2(Float16, Float16)

```cangjie
public func atan2(y: Float16, x: Float16): Float16
```

功能：计算两个半精度浮点数 y/x 的反正切函数值，单位为弧度。

参数：

- y: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。
- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回 y/x 的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.*
import std.convert.Formattable

main() {
    let y: Float16 = 1.0
    let x: Float16 = 1.0
    let atan2 = atan2(y, x) / Float16.getPI() * 180.0 // 将弧度值转为角度值打印
    println("${atan2.format(".1")}°")
}
```

运行结果：

```text
45.0°
```

## func atan2(Float32, Float32)

```cangjie
public func atan2(y: Float32, x: Float32): Float32
```

功能：计算两个单精度浮点数 y/x 的反正切函数值，单位为弧度。

参数：

- y: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。
- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回 y/x 的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.*
import std.convert.Formattable

main() {
    let y: Float32 = 1.0
    let x: Float32 = 1.0
    let atan2 = atan2(y, x) / Float32.getPI() * 180.0 // 将弧度值转为角度值打印
    println("${atan2.format(".1")}°")
}
```

运行结果：

```text
45.0°
```

## func atan2(Float64, Float64)

```cangjie
public func atan2(y: Float64, x: Float64): Float64
```

功能：计算两个双精度浮点数 y/x 的反正切函数值，单位为弧度。

参数：

- y: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。
- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回 y/x 的反正切函数值，单位为弧度。

示例：
<!-- verify -->
```cangjie
import std.math.*
import std.convert.Formattable

main() {
    let y: Float64 = 1.0
    let x: Float64 = 1.0
    let atan2 = atan2(y, x) / Float64.getPI() * 180.0 // 将弧度值转为角度值打印
    println("${atan2.format(".1")}°")
}
```

运行结果：

```text
45.0°
```