## func lcm(Int32, Int32)

```cangjie
public func lcm(x: Int32, y: Int32): Int32
```

功能：求两个 32 位有符号整数的最小的非负的公倍数，当入参有 0 时才返回 0。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的需要计算最小公倍数的第一个整数。
- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的需要计算最小公倍数的第二个整数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回两个整数的最小的非负的公倍数，当入参有 0 时才返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当返回值超出 32 位有符号整数的最大值时抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.lcm

main() {
    let x: Int32 = -15
    let y: Int32 = 9
    let lcm = lcm(x, y)
    println(lcm)
}
```

运行结果：

```text
45
```

## func lcm(Int64, Int64)

```cangjie
public func lcm(x: Int64, y: Int64): Int64
```

功能：求两个 64 位有符号整数的最小的非负的公倍数，当入参有 0 时才返回 0。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的需要计算最小公倍数的第一个整数。
- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的需要计算最小公倍数的第二个整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回两个整数的最小的非负的公倍数，当入参有 0 时才返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当返回值超出 64 位有符号整数的最大值时抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.lcm

main() {
    let x: Int64 = 15
    let y: Int64 = 9
    let lcm = lcm(x, y)
    println(lcm)
}
```

运行结果：

```text
45
```

## func lcm(Int8, Int8)

```cangjie
public func lcm(x: Int8, y: Int8): Int8
```

功能：求两个 8 位有符号整数的最小的非负的公倍数，当入参有 0 时才返回 0。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的需要计算最小公倍数的第一个整数。
- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的需要计算最小公倍数的第二个整数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 返回两个整数的最小的非负的公倍数，当入参有 0 时才返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当返回值超出 8 位有符号整数的最大值时抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.lcm

main() {
    let x: Int8 = 15
    let y: Int8 = 9
    let lcm = lcm(x, y)
    println(lcm)
}
```

运行结果：

```text
45
```

## func lcm(UInt16, UInt16)

```cangjie
public func lcm(x: UInt16, y: UInt16): UInt16
```

功能：求两个 16 位无符号整数的最小的非负的公倍数，当入参有 0 时才返回 0。

参数：

- x: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的需要计算最小公倍数的第一个整数。
- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 传入的需要计算最小公倍数的第二个整数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 返回两个整数的最小的非负的公倍数，当入参有 0 时才返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当返回值超出 16 位无符号整数的最大值时抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.lcm

main() {
    let x: UInt16 = 15
    let y: UInt16 = 9
    let lcm = lcm(x, y)
    println(lcm)
}
```

运行结果：

```text
45
```