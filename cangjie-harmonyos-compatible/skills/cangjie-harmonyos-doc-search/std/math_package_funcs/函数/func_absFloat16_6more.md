## func abs(Float16)

```cangjie
public func abs(x: Float16): Float16
```

功能：求一个半精度浮点数的绝对值。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 传入的半精度浮点数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回传入参数的绝对值。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Float16 = -23.0
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23.000000
```

## func abs(Float32)

```cangjie
public func abs(x: Float32): Float32
```

功能：求一个单精度浮点数的绝对值。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 传入的单精度浮点数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回传入参数的绝对值。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Float32 = -23.0
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23.000000
```

## func abs(Float64)

```cangjie
public func abs(x: Float64): Float64
```

功能：求一个双精度浮点数的绝对值。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 传入的双精度浮点数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回传入参数的绝对值。

示例：

<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Float64 = -23.0
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23.000000
```

## func abs(Int16)

```cangjie
public func abs(x: Int16): Int16
```

功能：求一个 16 位有符号整数的绝对值。

参数：

- x: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 传入的 16 位有符号整数。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 返回传入参数的绝对值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当输入参数是有符号整数的最小值，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Int16 = -23
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23
```

以下示例抛出异常：
<!-- verify -->
```cangjie
import std.math.abs

main(): Unit {
    try {
        let n = Int16(-2 ** 15)
        let abs: Int16 = abs(n)
        println(abs)
    } catch (e: OverflowException) {
        println("异常：输入参数是有符号整数的最小值")
    }
}
```

运行结果：

```text
异常：输入参数是有符号整数的最小值
```

## func abs(Int32)

```cangjie
public func abs(x: Int32): Int32
```

功能：求一个 32 位有符号整数的绝对值。

参数：

- x: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 传入的 32 位有符号整数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回传入参数的绝对值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当输入参数是有符号整数的最小值，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Int32 = -23
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23
```

## func abs(Int64)

```cangjie
public func abs(x: Int64): Int64
```

功能：求一个 64 位有符号整数的绝对值。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 传入的 64 位有符号整数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回传入参数的绝对值。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当输入参数是有符号整数的最小值，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.abs

main() {
    let n: Int64 = -23
    let abs = abs(n)
    println(abs)
}
```

运行结果：

```text
23
```