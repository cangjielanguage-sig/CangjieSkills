## func fmod(Float64, Float64)

```cangjie
public func fmod(x: Float64, y: Float64): Float64
```

功能：求两个双精度浮点数 x/y 的余数。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的被除数。
- y: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的除数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回 x/y 的余数, 当 x 或 y 为 `NaN` 时 返回 `NaN`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 x 为 `Inf` 或 y 为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.fmod
import std.convert.Formattable

main() {
    let x: Float64 = 3.3
    let y: Float64 = 2.2
    let fmod = fmod(x, y)
    println(fmod.format(".1"))
}
```

运行结果：

```text
1.1
```

## func gamma(Float16)

```cangjie
public func gamma(x: Float16): Float16
```

功能：求浮点数的伽马函数值，该函数是阶乘概念在实数上的推广，其求值公式为：

$${\displaystyle \Gamma (x)=\int _{0}^{\infty }t^{x-1}\mathrm {e} ^{-t}{\rm {{d}t,}}}$$

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的需要求伽马函数值的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入浮点数的伽马函数值。

示例：
<!-- verify -->
```cangjie
import std.math.gamma

main() {
    let n: Float16 = -1.1
    let gamma = gamma(n)
    println(gamma)
}
```

运行结果：

```text
9.750000
```

## func gamma(Float32)

```cangjie
public func gamma(x: Float32): Float32
```

功能：求浮点数的伽马函数值，该函数是阶乘概念在实数上的推广。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的需要求伽马函数值的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入浮点数的伽马函数值。

示例：
<!-- verify -->
```cangjie
import std.math.gamma

main() {
    let n: Float32 = -1.1
    let gamma = gamma(n)
    println(gamma)
}
```

运行结果：

```text
9.714804
```

## func gamma(Float64)

```cangjie
public func gamma(x: Float64): Float64
```

功能：求浮点数的伽马函数值，该函数是阶乘概念在实数上的推广。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的需要求伽马函数值的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入浮点数的伽马函数值。

示例：
<!-- verify -->
```cangjie
import std.math.gamma

main() {
    let n: Float64 = -1.1
    let gamma = gamma(n)
    println(gamma)
}
```

运行结果：

```text
9.714806
```

## func gcd(Int16, Int16)

```cangjie
public func gcd(x: Int16, y: Int16): Int16
```

功能：求两个 16 位有符号整数的最大公约数。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的需要计算最大公约数的第一个整数。
- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 返回两个整数的最大公约数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当两参数都为有符号整数最小值，或一个参数为有符号整数的最小值且另一个参数为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: Int16 = 15
    let y: Int16 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```