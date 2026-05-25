## func logBase(Float16, Float16)

```cangjie
public func logBase(x: Float16, base: Float16): Float16
```

功能：求以 `base` 为底 `x` 的对数。

参数：

- x: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 真数。真数需要大于 0。
- base: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 底数。底数需要大于 0，且不能为 1。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 返回以 `base` 为底 `x` 的对数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当真数或底数不为正，或底数为 1 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.logBase

main() {
    let x: Float16 = 512.0
    let base: Float16 = 2.0
    let logBase = logBase(x, base)
    println(logBase)
}
```

运行结果：

```text
9.000000
```

以下示例将抛出相应异常：
<!-- verify -->
```cangjie
import std.math.logBase

main() {
    let x: Float16 = 512.0
    let base: Float16 = -2.0

    // 示例1：底数为负数
    try {
        let logBase1 = logBase(x, base)
        println(logBase1)
    } catch (e: IllegalArgumentException) {
        println("异常1：底数为负数")
    }

    // 示例2：真数为负数
    try {
        let logBase2 = logBase(-x, base)
        println(logBase2)
    } catch (e: IllegalArgumentException) {
        println("异常2：真数为负数")
    }

    // 示例3：底数为1
    try {
        let logBase3 = logBase(x, 1.0)
        println(logBase3)
    } catch (e: IllegalArgumentException) {
        println("异常3：底数为1")
    }
}
```

运行结果：

```text
异常1：底数为负数
异常2：真数为负数
异常3：底数为1
```

## func logBase(Float32, Float32)

```cangjie
public func logBase(x: Float32, base: Float32): Float32
```

功能：求以 `base` 为底 `x` 的对数。

参数：

- x: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 真数。真数需要大于 0。
- base: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 底数。底数需要大于 0，且不能为 1。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回以 `base` 为底 `x` 的对数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当真数或底数不为正，或底数为 1 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.logBase

main() {
    let x: Float32 = 1024.0
    let base: Float32 = 2.0
    let logBase = logBase(x, base)
    println(logBase)
}
```

运行结果：

```text
10.000000
```

## func logBase(Float64, Float64)

```cangjie
public func logBase(x: Float64, base: Float64): Float64
```

功能：求以 `base` 为底 `x` 的对数。

参数：

- x: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 真数。真数需要大于 0。
- base: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 底数。底数需要大于 0，且不能为 1。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 返回以 `base` 为底 `x` 的对数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当真数或底数不为正，或底数为 1 时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.logBase

main() {
    let x: Float64 = 1024.0
    let base: Float64 = 2.0
    let logBase = logBase(x, base)
    println(logBase)
}
```

运行结果：

```text
10.000000
```