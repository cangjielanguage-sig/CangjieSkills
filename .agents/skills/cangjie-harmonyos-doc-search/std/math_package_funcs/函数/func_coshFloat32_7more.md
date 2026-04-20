## func cosh(Float32)

```cangjie
public func cosh(x: Float32): Float32
```

功能：计算单精度浮点数的双曲余弦函数值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的双曲余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cosh

main() {
    let n: Float32 = 0.0
    let cosh = cosh(n)
    println(cosh)
}
```

运行结果：

```text
1.000000
```

## func cosh(Float64)

```cangjie
public func cosh(x: Float64): Float64
```

功能：计算双精度浮点数的双曲余弦函数值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的双曲余弦函数值。

示例：
<!-- verify -->
```cangjie
import std.math.cosh

main() {
    let n: Float64 = 0.0
    let cosh = cosh(n)
    println(cosh)
}
```

运行结果：

```text
1.000000
```

## func countOne(Int16) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: Int16): Int8
```

功能：求 16 位整型的二进制表达中 1 的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(Int16)](#func-countonesint16) 替代。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的 16 位有符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(Int32) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: Int32): Int8
```

功能：求 32 位整型的二进制表达中 1 的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(Int32)](#func-countonesint32) 替代。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的 32 位有符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(Int64) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: Int64): Int8
```

功能：求 64 位整型的二进制表达中 1 的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(Int64)](#func-countonesint64) 替代。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的 64 位有符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(Int8) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: Int8): Int8
```

功能：求 8 位整型的二进制表达中 1 的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(Int8)](#func-countonesint8) 替代。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的 8 位有符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(UInt16) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: UInt16): Int8
```

功能：求 16 位无符号整型的二进制表达中的 1 的位的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(UInt16)](#func-countonesuint16) 替代。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的 16 位无符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。