## func countOne(UInt32) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: UInt32): Int8
```

功能：求 32 位无符号整型的二进制表达中的 1 的位的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(UInt32)](#func-countonesuint32) 替代。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 传入的 32 位无符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(UInt64) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: UInt64): Int8
```

功能：求 64 位无符号整型的二进制表达中的 1 的位的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(UInt64)](#func-countonesuint64) 替代。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 传入的 64 位无符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOne(UInt8) <sup>(deprecated)</sup>

```cangjie
public func countOne(x: UInt8): Int8
```

功能：求 8 位无符号整型的二进制表达中的 1 的位的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [countOnes(UInt8)](#func-countonesuint8) 替代。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 传入的 8 位无符号整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回传入参数的二进制表达中的 1 的位的个数。

## func countOnes(Int16)

```cangjie
public func countOnes(x: Int16): Int64
```

功能：求 16 位整型的二进制表达中 1 的个数。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的 16 位有符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: Int16 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(Int32)

```cangjie
public func countOnes(x: Int32): Int64
```

功能：求 32 位整型的二进制表达中 1 的个数。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的 32 位有符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: Int32 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(Int64)

```cangjie
public func countOnes(x: Int64): Int64
```

功能：求 64 位整型的二进制表达中 1 的个数。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的 64 位有符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: Int64 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```

## func countOnes(Int8)

```cangjie
public func countOnes(x: Int8): Int64
```

功能：求 8 位整型的二进制表达中 1 的个数。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的 8 位有符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的二进制表达中的 1 的位的个数。

示例：
<!-- verify -->
```cangjie
import std.math.countOnes

main() {
    let n: Int8 = 15
    let countOnes = countOnes(n)
    println(countOnes)
}
```

运行结果：

```text
4
```