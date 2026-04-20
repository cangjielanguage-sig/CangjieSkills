## func reverse(UInt32)

```cangjie
public func reverse(x: UInt32): UInt32
```

功能：求无符号整数按位反转后的数。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 需要进行反转的无符号整数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 返回反转后的无符号数。

示例：
<!-- verify -->
```cangjie
import std.math.reverse

main() {
    let n: UInt32 = 0x8000_0000
    let reverse = reverse(n)
    println(reverse)
}
```

运行结果：

```text
1
```

## func reverse(UInt64)

```cangjie
public func reverse(x: UInt64): UInt64
```

功能：求无符号整数按位反转后的数。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 需要进行反转的无符号整数。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 返回反转后的无符号数。

示例：
<!-- verify -->
```cangjie
import std.math.reverse

main() {
    let n: UInt64 = 0x8000_0000_0000_0000
    let reverse = reverse(n)
    println(reverse)
}
```

运行结果：

```text
1
```

## func reverse(UInt8)

```cangjie
public func reverse(x: UInt8): UInt8
```

功能：求无符号整数按位反转后的数。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 需要进行反转的无符号整数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 返回反转后的无符号数。

示例：
<!-- verify -->
```cangjie
import std.math.reverse

main() {
    let n: UInt8 = 0x80
    let reverse = reverse(n)
    println(reverse)
}
```

运行结果：

```text
1
```

## func rotate(Int16, Int8)

```cangjie
public func rotate(num: Int16, d: Int8): Int16
```

功能：求整数的按位旋转后的结果。

参数：

- num: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: Int16 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(Int32, Int8)

```cangjie
public func rotate(num: Int32, d: Int8): Int32
```

功能：求整数的按位旋转后的结果。

参数：

- num: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: Int32 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```

## func rotate(Int64, Int8)

```cangjie
public func rotate(num: Int64, d: Int8): Int64
```

功能：求整数的按位旋转后的结果。

参数：

- num: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入一个整数。
- d: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 旋转位数，负数右移，正数左移。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回旋转后的整数。

示例：
<!-- verify -->
```cangjie
import std.math.rotate

main() {
    let n: Int64 = 1
    let rotate = rotate(n, 2)
    println(rotate)
}
```

运行结果：

```text
4
```