## func countOnes(UInt16)

```cangjie
public func countOnes(x: UInt16): Int64
```

功能：求 16 位无符号整型的二进制表达中的 1 的位的个数。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的 16 位无符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: UInt16 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(UInt32)

```cangjie
public func countOnes(x: UInt32): Int64
```

功能：求 32 位无符号整型的二进制表达中的 1 的位的个数。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 传入的 32 位无符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: UInt32 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(UInt64)

```cangjie
public func countOnes(x: UInt64): Int64
```

功能：求 64 位无符号整型的二进制表达中的 1 的位的个数。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 传入的 64 位无符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: UInt64 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(UInt8)

```cangjie
public func countOnes(x: UInt8): Int64
```

功能：求 8 位无符号整型的二进制表达中的 1 的位的个数。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 传入的 8 位无符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: UInt8 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func erf(Float16)

```cangjie
public func erf(x: Float16): Float16
```

功能：求半精度浮点数的误差值。相关定义是：$$erf(x) = \frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}dt$$。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的半精度浮点数的误差值。

示例：
<!-- verify -->
```cangjie
import std.math.erf

main() {
    let n: Float16 = 5.0
    let erf = erf(n)
    println(erf)
}
```

运行结果：

```text
1.000000
```

## func erf(Float32)

```cangjie
public func erf(x: Float32): Float32
```

功能：求单精度浮点数的误差值。相关定义是：$$erf(x) = \frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}dt$$。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的单精度浮点数的误差值。

示例：
<!-- verify -->
```cangjie
import std.math.erf

main() {
    let n: Float32 = 5.0
    let erf = erf(n)
    println(erf)
}
```

运行结果：

```text
1.000000
```