## func gcd(Int32, Int32)

```cangjie
public func gcd(x: Int32, y: Int32): Int32
```

功能：求两个 32 位有符号整数的最大公约数。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的需要计算最大公约数的第一个整数。
- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回两个整数的最大公约数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当两参数都为有符号整数最小值，或一个参数为有符号整数的最小值且另一个参数为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: Int32 = 15
    let y: Int32 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func gcd(Int64, Int64)

```cangjie
public func gcd(x: Int64, y: Int64): Int64
```

功能：求两个 64 位有符号整数的最大公约数。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的需要计算最大公约数的第一个整数。
- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回两个整数的最大公约数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当两参数都为有符号整数最小值，或一个参数为有符号整数的最小值且另一个参数为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: Int64 = 15
    let y: Int64 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func gcd(Int8, Int8)

```cangjie
public func gcd(x: Int8, y: Int8): Int8
```

功能：求两个 8 位有符号整数的最大公约数。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的需要计算最大公约数的第一个整数。
- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回两个整数的最大公约数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当两参数都为有符号整数最小值，或一个参数为有符号整数的最小值且另一个参数为 0 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: Int8 = 15
    let y: Int8 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func gcd(UInt16, UInt16)

```cangjie
public func gcd(x: UInt16, y: UInt16): UInt16
```

功能：求两个 16 位无符号整数的最大公约数。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的需要计算最大公约数的第一个整数。
- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 返回两个整数的最大公约数。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: UInt16 = 15
    let y: UInt16 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```