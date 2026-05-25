## func floor(Float16)

```cangjie
public func floor(x: Float16): Float16
```

功能：求浮点数的向下取整值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的需要向下取整的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入浮点数的向下取整值。

示例：
<!-- verify -->
```cangjie
import std.math.floor

main() {
    let n: Float16 = 10.5
    let floor = floor(n)
    println(floor)
}
```

运行结果：

```text
10.000000
```

## func floor(Float32)

```cangjie
public func floor(x: Float32): Float32
```

功能：求浮点数的向下取整值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的需要向下取整的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入浮点数的向下取整值。

示例：
<!-- verify -->
```cangjie
import std.math.floor

main() {
    let n: Float32 = 10.5
    let floor = floor(n)
    println(floor)
}
```

运行结果：

```text
10.000000
```

## func floor(Float64)

```cangjie
public func floor(x: Float64): Float64
```

功能：求浮点数的向下取整值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的需要向下取整的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入浮点数的向下取整值。

示例：
<!-- verify -->
```cangjie
import std.math.floor

main() {
    let n: Float64 = 10.5
    let floor = floor(n)
    println(floor)
}
```

运行结果：

```text
10.000000
```

## func fmod(Float16, Float16)

```cangjie
public func fmod(x: Float16, y: Float16): Float16
```

功能：求两个半精度浮点数 x/y 的余数。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的被除数。
- y: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的除数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回 x/y 的余数, 当 x 或 y 为 `NaN` 时 返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 x 为 `Inf` 或 y 为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.fmod
import std.convert.Formattable

main() {
    let x: Float16 = 3.3
    let y: Float16 = 2.2
    let fmod = fmod(x, y)
    println(fmod.format(".1"))
}
```

运行结果：

```text
1.1
```

## func fmod(Float32, Float32)

```cangjie
public func fmod(x: Float32, y: Float32): Float32
```

功能：求两个单精度浮点数 x/y 的余数。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的被除数。
- y: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的除数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回 x/y 的余数, 当 x 或 y 为 `NaN` 时 返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 x 为 `Inf` 或 y 为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.fmod
import std.convert.Formattable

main() {
    let x: Float32 = 3.3
    let y: Float32 = 2.2
    let fmod = fmod(x, y)
    println(fmod.format(".1"))
}
```

运行结果：

```text
1.1
```