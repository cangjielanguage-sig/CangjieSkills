## func cbrt(Float64)

```cangjie
public func cbrt(x: Float64): Float64
```

功能：求双精度浮点数的立方根。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的立方根。

示例：
<!-- verify -->
```cangjie
import std.math.cbrt

main() {
    let n: Float64 = -1000.0
    let cbrt = cbrt(n)
    println(cbrt)
}
```

运行结果：

```text
-10.000000
```

## func ceil(Float16)

```cangjie
public func ceil(x: Float16): Float16
```

功能：求半精度浮点数的向上取整值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的向上取整值。

示例：
<!-- verify -->
```cangjie
import std.math.ceil

main() {
    let n: Float16 = 0.7
    let ceil = ceil(n)
    println(ceil)
}
```

运行结果：

```text
1.000000
```

## func ceil(Float32)

```cangjie
public func ceil(x: Float32): Float32
```

功能：求单精度浮点数的向上取整值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的向上取整值。

示例：
<!-- verify -->
```cangjie
import std.math.ceil

main() {
    let n: Float32 = 0.7
    let ceil = ceil(n)
    println(ceil)
}
```

运行结果：

```text
1.000000
```

## func ceil(Float64)

```cangjie
public func ceil(x: Float64): Float64
```

功能：求双精度浮点数的向上取整值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的向上取整值。

示例：
<!-- verify -->
```cangjie
import std.math.ceil

main() {
    let n: Float64 = 0.7
    let ceil = ceil(n)
    println(ceil)
}
```

运行结果：

```text
1.000000
```

## func checkedAbs(Int16)

```cangjie
public func checkedAbs(x: Int16): Option<Int16>
```

功能：求一个 16 位有符号整数的绝对值。如果入参是 16 位有符号整数的最小值，函数返回 [None](../../core/core_package_api/core_package_enums.md#none)；否则，返回 [Some](../../core/core_package_api/core_package_enums.md#somet)(abs(x))。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的 16 位有符号整数。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)> - 返回传入参数的绝对值的 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 类型。

示例：
<!-- verify -->
```cangjie
import std.math.checkedAbs

main() {
    let n: Int16 = -23
    let checkedAbs = checkedAbs(n)
    println(checkedAbs)
}
```

运行结果：

```text
Some(23)
```