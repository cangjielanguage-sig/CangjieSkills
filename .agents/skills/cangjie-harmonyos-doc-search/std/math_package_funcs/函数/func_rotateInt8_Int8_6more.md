## func rotate(Int8, Int8)

```cangjie
public func rotate(num: Int8, d: Int8): Int8
```

功能：求整数的按位旋转后的结果。

参数：

- num: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: Int8 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(UInt16, Int8)

```cangjie
public func rotate(num: UInt16, d: Int8): UInt16
```

功能：求整数的按位旋转后的结果。

参数：

- num: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: UInt16 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(UInt32, Int8)

```cangjie
public func rotate(num: UInt32, d: Int8): UInt32
```

功能：求整数的按位旋转后的结果。

参数：

- num: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: UInt32 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(UInt64, Int8)

```cangjie
public func rotate(num: UInt64, d: Int8): UInt64
```

功能：求整数的按位旋转后的结果。

参数：

- num: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: UInt64 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(UInt8, Int8)

```cangjie
public func rotate(num: UInt8, d: Int8): UInt8
```

功能：求整数的按位旋转后的结果。

参数：

- num: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: UInt8 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func round(Float16)

```cangjie
public func round(x: Float16): Float16
```

功能：此函数采用 IEEE-754 的向最近舍入规则，计算浮点数的舍入值。如果该浮点数有两个最近整数，则向偶数舍入。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 需要计算舍入值的浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回浮点数向最近整数方向的舍入值。如果该浮点数有两个最近整数，则返回向偶数舍入值。

示例：
<!-- verify -->
```cangjie
import std.math.round

main() {
    let n: Float16 = 1.5
    let round = round(n)
    println(round)
}
```

运行结果：

```text
2.000000
```