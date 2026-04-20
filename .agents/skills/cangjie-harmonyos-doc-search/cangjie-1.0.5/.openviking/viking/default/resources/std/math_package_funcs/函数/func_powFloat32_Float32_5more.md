## func pow(Float32, Float32)

```cangjie
public func pow(base: Float32, exponent: Float32): Float32
```

功能：求浮点数 `base` 的 `exponent` 次幂。

参数：

- base: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 底数。
- exponent: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 指数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入浮点数 `base` 的 `exponent` 次幂。如果值不存在，则返回 `nan`。

示例：
<!-- verify -->
```cangjie
import std.math.pow

main() {
    let base: Float32 = -1.0
    let exponent: Float32 = 0.5
    let pow = pow(base, exponent)
    println(pow)
}
```

运行结果：

```text
nan
```

## func pow(Float32, Int32)

```cangjie
public func pow(base: Float32, exponent: Int32): Float32
```

功能：求浮点数 `base` 的 `exponent` 次幂。

参数：

- base: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 底数。
- exponent: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 指数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入浮点数 `base` 的 `exponent` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.pow

main() {
    let base: Float32 = -1.0
    let exponent: Int32 = 2
    let pow = pow(base, exponent)
    println(pow)
}
```

运行结果：

```text
1.000000
```

## func pow(Float64, Float64)

```cangjie
public func pow(base: Float64, exponent: Float64): Float64
```

功能：求浮点数 `base` 的 `exponent` 次幂。

参数：

- base: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 底数。
- exponent: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 指数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入浮点数 `base` 的 `exponent` 次幂。如果值不存在，则返回 `nan`。

示例：
<!-- verify -->
```cangjie
import std.math.pow

main() {
    let base: Float64 = -1.0
    let exponent: Float64 = 0.5
    let pow = pow(base, exponent)
    println(pow)
}
```

运行结果：

```text
nan
```

## func pow(Float64, Int64)

```cangjie
public func pow(base: Float64, exponent: Int64): Float64
```

功能：求浮点数 `base` 的 `exponent` 次幂。

参数：

- base: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 底数。
- exponent: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入浮点数 `base` 的 `exponent` 次幂。

示例：
<!-- verify -->
```cangjie
import std.math.pow

main() {
    let base: Float64 = -1.0
    let exponent: Int64 = 2
    let pow = pow(base, exponent)
    println(pow)
}
```

运行结果：

```text
1.000000
```

## func reverse(UInt16)

```cangjie
public func reverse(x: UInt16): UInt16
```

功能：求无符号整数按位反转后的数。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 需要进行反转的无符号整数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 返回反转后的无符号数。

示例：
<!-- verify -->
```cangjie
import std.math.reverse

main() {
    let n: UInt16 = 0x8000
    let reverse = reverse(n)
    println(reverse)
}
```

运行结果：

```text
1
```