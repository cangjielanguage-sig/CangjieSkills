## func gcd(UInt32, UInt32)

```cangjie
public func gcd(x: UInt32, y: UInt32): UInt32
```

功能：求两个 32 位无符号整数的最大公约数。

参数：

- x: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 传入的需要计算最大公约数的第一个整数。
- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 返回两个整数的最大公约数。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: UInt32 = 15
    let y: UInt32 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func gcd(UInt64, UInt64)

```cangjie
public func gcd(x: UInt64, y: UInt64): UInt64
```

功能：求两个 64 位无符号整数的最大公约数。

参数：

- x: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 传入的需要计算最大公约数的第一个整数。
- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 返回两个整数的最大公约数。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: UInt64 = 15
    let y: UInt64 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func gcd(UInt8, UInt8)

```cangjie
public func gcd(x: UInt8, y: UInt8): UInt8
```

功能：求两个 8 位无符号整数的最大公约数。

参数：

- x: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 传入的需要计算最大公约数的第一个整数。
- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 传入的需要计算最大公约数的第二个整数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 返回两个整数的最大公约数。

示例：
<!-- verify -->
```cangjie
import std.math.gcd

main() {
    let x: UInt8 = 15
    let y: UInt8 = 9
    let gcd = gcd(x, y)
    println(gcd)
}
```

运行结果：

```text
3
```

## func lcm(Int16, Int16)

```cangjie
public func lcm(x: Int16, y: Int16): Int16
```

功能：求两个 16 位有符号整数的最小的非负的公倍数，当入参有 0 时才返回 0。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的需要计算最小公倍数的第一个整数。
- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的需要计算最小公倍数的第二个整数。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 返回两个整数的最小的非负的公倍数，当入参有 0 时才返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当返回值超出 16 位有符号整数的最大值时抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.lcm

main() {
    let x: Int16 = -15
    let y: Int16 = 9
    let lcm = lcm(x, y)
    println(lcm)
}
```

运行结果：

```text
45
```