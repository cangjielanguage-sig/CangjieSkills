## func sinh(Float32)

```cangjie
public func sinh(x: Float32): Float32
```

功能：计算单精度浮点数的双曲正弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sinh

main() {
    let n: Float32 = 0.0
    let sinh = sinh(n)
    println(sinh)
}
```

运行结果：

```text
0.000000
```

## func sinh(Float64)

```cangjie
public func sinh(x: Float64): Float64
```

功能：计算双精度浮点数的双曲正弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的双曲正弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.sinh

main() {
    let n: Float64 = 0.0
    let sinh = sinh(n)
    println(sinh)
}
```

运行结果：

```text
0.000000
```

## func sqrt(Float16)

```cangjie
public func sqrt(x: Float16): Float16
```

功能：求浮点数的算术平方根。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 需要计算算数平方根的浮点数。`x` 需要大于等于 0。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入的浮点数的算术平方根。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数为负数时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.sqrt

main() {
    let n: Float16 = 16.0
    let sqrt = sqrt(n)
    println(sqrt)
}
```

运行结果：

```text
4.000000
```

## func sqrt(Float32)

```cangjie
public func sqrt(x: Float32): Float32
```

功能：求浮点数的算术平方根。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 需要计算算数平方根的浮点数。`x` 需要大于等于 0。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入的浮点数的算术平方根。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数为负数时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.sqrt

main() {
    let n: Float32 = 16.0
    let sqrt = sqrt(n)
    println(sqrt)
}
```

运行结果：

```text
4.000000
```

## func sqrt(Float64)

```cangjie
public func sqrt(x: Float64): Float64
```

功能：求浮点数的算术平方根。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 需要计算算数平方根的浮点数。`x` 需要大于等于 0。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入的浮点数的算术平方根。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数为负数时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.sqrt

main() {
    let n: Float64 = 16.0
    let sqrt = sqrt(n)
    println(sqrt)
}
```

运行结果：

```text
4.000000
```

## func tan(Float16)

```cangjie
public func tan(x: Float16): Float16
```

功能：计算半精度浮点数的正切函数值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数，入参单位为弧度。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的正切函数值。

示例：
<!-- verify -->
```cangjie
import std.math.tan

main() {
    let n: Float16 = 0.0
    let tan = tan(n)
    println(tan)
}
```

运行结果：

```text
0.000000
```