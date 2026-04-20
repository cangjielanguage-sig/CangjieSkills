## func atanh(Float16)

```cangjie
public func atanh(x: Float16): Float16
```

功能：计算半精度浮点数的反双曲正切函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。-1.0 < `x` < 1.0。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的反双曲正切函数值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于等于 1.0 或小于等于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.atanh

main() {
    let n: Float16 = 0.0
    let atanh = atanh(n)
    println(atanh)
}
```

运行结果：

```text
0.000000
```

以下示例将抛出异常：
<!-- run.error -->
```cangjie
import std.math.atanh

main(): Unit {
    let n = -1.4
    let atanh = atanh(n)
    println(atanh)
}
```

## func atanh(Float32)

```cangjie
public func atanh(x: Float32): Float32
```

功能：计算单精度浮点数的反双曲正切函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。-1.0 < `x` < 1.0。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的反双曲正切函数值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于等于 1.0 或小于等于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.atanh

main() {
    let n: Float32 = 0.0
    let atanh = atanh(n)
    println(atanh)
}
```

运行结果：

```text
0.000000
```

## func atanh(Float64)

```cangjie
public func atanh(x: Float64): Float64
```

功能：计算双精度浮点数的反双曲正切函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。-1.0 < `x` < 1.0。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的反双曲正切函数值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `x` 大于等于 1.0 或小于等于 -1.0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.atanh

main() {
    let n: Float64 = 0.0
    let atanh = atanh(n)
    println(atanh)
}
```

运行结果：

```text
0.000000
```

## func cbrt(Float16)

```cangjie
public func cbrt(x: Float16): Float16
```

功能：求半精度浮点数的立方根。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的立方根。

示例：
<!-- verify -->
```cangjie
import std.math.cbrt

main() {
    let n: Float16 = -1000.0
    let cbrt = cbrt(n)
    println(cbrt)
}
```

运行结果：

```text
-10.000000
```

## func cbrt(Float32)

```cangjie
public func cbrt(x: Float32): Float32
```

功能：求单精度浮点数的立方根。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的立方根。

示例：
<!-- verify -->
```cangjie
import std.math.cbrt

main() {
    let n: Float32 = -1000.0
    let cbrt = cbrt(n)
    println(cbrt)
}
```

运行结果：

```text
-10.000000
```