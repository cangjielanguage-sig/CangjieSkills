## func checkedAbs(Int32)

```cangjie
public func checkedAbs(x: Int32): Option<Int32>
```

功能：求一个 32 位有符号整数的绝对值。如果入参是 32 位有符号整数的最小值，函数返回 [None](../../core/core_package_api/core_package_enums.md#none)；否则，返回 [Some](../../core/core_package_api/core_package_enums.md#somet)(abs(x))。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的 32 位有符号整数。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> - 返回传入参数的绝对值的 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 类型。

示例：
<!-- verify -->
```cangjie
import std.math.checkedAbs

main() {
    let n: Int32 = -23
    let checkedAbs = checkedAbs(n)
    println(checkedAbs)
}
```

运行结果：

```text
Some(23)
```

## func checkedAbs(Int64)

```cangjie
public func checkedAbs(x: Int64): Option<Int64>
```

功能：求一个 64 位有符号整数的绝对值。如果入参是 64 位有符号整数的最小值，函数返回 [None](../../core/core_package_api/core_package_enums.md#none)；否则，返回 [Some](../../core/core_package_api/core_package_enums.md#somet)(abs(x))。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的 64 位有符号整数。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 返回传入参数的绝对值的 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 类型。

示例：
<!-- verify -->
```cangjie
import std.math.checkedAbs

main() {
    let n: Int64 = -23
    let checkedAbs = checkedAbs(n)
    println(checkedAbs)
}
```

运行结果：

```text
Some(23)
```

## func checkedAbs(Int8)

```cangjie
public func checkedAbs(x: Int8): Option<Int8>
```

功能：求一个 8 位有符号整数的绝对值。如果入参是 8 位有符号整数的最小值，函数返回 [None](../../core/core_package_api/core_package_enums.md#none)；否则，返回 [Some](../../core/core_package_api/core_package_enums.md#somet)(abs(x))。

参数：

- x: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 传入的 8 位有符号整数。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)> - 返回传入参数的绝对值的 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 类型。

示例：
<!-- verify -->
```cangjie
import std.math.checkedAbs

main() {
    let n: Int8 = -23
    let checkedAbs = checkedAbs(n)
    println(checkedAbs)
}
```

运行结果：

```text
Some(23)
```