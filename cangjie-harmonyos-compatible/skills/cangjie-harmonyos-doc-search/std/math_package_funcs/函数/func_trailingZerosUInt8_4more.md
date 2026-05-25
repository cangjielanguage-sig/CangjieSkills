## func trailingZeros(UInt8)

```cangjie
public func trailingZeros(x: UInt8): Int64
```

功能：求 8 位无符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: UInt8 = 64
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
6
```

## func trunc(Float16)

```cangjie
public func trunc(x: Float16): Float16
```

功能：求浮点数的截断取整值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 需要截断取整的浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入浮点数截断取整后的值。

示例：
<!-- verify -->
```cangjie
import std.math.trunc

main() {
    let x: Float16 = 64.555566
    let trunc = trunc(x)
    println(trunc)
}
```

运行结果：

```text
64.000000
```

## func trunc(Float32)

```cangjie
public func trunc(x: Float32): Float32
```

功能：求浮点数的截断取整值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 需要截断取整的浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入浮点数截断取整后的值。

示例：
<!-- verify -->
```cangjie
import std.math.trunc

main() {
    let x: Float32 = 64.555566
    let trunc = trunc(x)
    println(trunc)
}
```

运行结果：

```text
64.000000
```

## func trunc(Float64)

```cangjie
public func trunc(x: Float64): Float64
```

功能：求浮点数的截断取整值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 需要截断取整的浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入浮点数截断取整后的值。

示例：
<!-- verify -->
```cangjie
import std.math.trunc

main() {
    let x: Float64 = 64.555566
    let trunc = trunc(x)
    println(trunc)
}
```

运行结果：

```text
64.000000
```