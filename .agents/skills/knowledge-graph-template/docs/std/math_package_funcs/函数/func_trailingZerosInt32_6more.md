## func trailingZeros(Int32)

```cangjie
public func trailingZeros(x: Int32): Int64
```

功能：求 32 位有符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: Int32 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```

## func trailingZeros(Int64)

```cangjie
public func trailingZeros(x: Int64): Int64
```

功能：求 64 位有符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: Int64 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```

## func trailingZeros(Int8)

```cangjie
public func trailingZeros(x: Int8): Int64
```

功能：求 16 位有符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: Int8 = 64
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
6
```

## func trailingZeros(UInt16)

```cangjie
public func trailingZeros(x: UInt16): Int64
```

功能：求 16 位无符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: UInt16 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```

## func trailingZeros(UInt32)

```cangjie
public func trailingZeros(x: UInt32): Int64
```

功能：求 32 位无符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: UInt32 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```

## func trailingZeros(UInt64)

```cangjie
public func trailingZeros(x: UInt64): Int64
```

功能：求 64 位无符号整数的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 需要求后置 0 的整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.trailingZeros

main() {
    let x: UInt64 = 512
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
9
```