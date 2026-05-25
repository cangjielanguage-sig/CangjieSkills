## func leadingZeros(Int32)

```cangjie
public func leadingZeros(x: Int32): Int64
```

功能：求 32 位有符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: Int32 = 512
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
22
```

## func leadingZeros(Int64)

```cangjie
public func leadingZeros(x: Int64): Int64
```

功能：求 64 位有符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: Int64 = 512
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
54
```

## func leadingZeros(Int8)

```cangjie
public func leadingZeros(x: Int8): Int64
```

功能：求 8 位有符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: Int8 = 4
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
5
```

## func leadingZeros(UInt16)

```cangjie
public func leadingZeros(x: UInt16): Int64
```

功能：求 16 位无符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: UInt16 = 512
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
6
```

## func leadingZeros(UInt32)

```cangjie
public func leadingZeros(x: UInt32): Int64
```

功能：求 32 位无符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: UInt32 = 512
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
22
```

## func leadingZeros(UInt64)

```cangjie
public func leadingZeros(x: UInt64): Int64
```

功能：求 64 位无符号整数的二进制表达中的从最高位算起，连续位为 0 的个数。如果最高位不是 0，则返回 0。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 需要求前导 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回前导 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.leadingZeros

main() {
    let x: UInt64 = 512
    let leadingZeros = leadingZeros(x)
    println(leadingZeros)
}
```

运行结果：

```text
54
```