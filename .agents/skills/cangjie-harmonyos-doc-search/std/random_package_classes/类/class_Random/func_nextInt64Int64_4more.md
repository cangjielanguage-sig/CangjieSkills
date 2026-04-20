### func nextInt64(Int64)

```cangjie
public func nextInt64(upper: Int64): Int64
```

功能：获取一个范围在 [0, `upper`) 的 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的伪随机数。

参数：

- upper: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [Int64](../../core/core_package_api/core_package_intrinsics.md#int64).Max]。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 一个 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 小于等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int64 = m.nextInt64(5)
    if (n is Int64) {
        println("n is Int64")
    }
    try {
        let p: Int64 = m.nextInt64(-1)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 小于等于 0")
    }
    return 0
}
```

运行结果：

```text
n is Int64
参数异常：upper 小于等于 0
```

### func nextInt8()

```cangjie
public func nextInt8(): Int8
```

功能：获取一个 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的伪随机数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 一个 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int8 = m.nextInt8()
    if (n is Int8) {
        println("n is Int8")
    }
    return 0
}
```

运行结果：

```text
n is Int8
```

### func nextInt8(Int8): Int8

```cangjie
public func nextInt8(upper: Int8): Int8
```

功能：获取一个范围在 [0, `upper`) 的 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的伪随机数。

参数：

- upper: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [Int8](../../core/core_package_api/core_package_intrinsics.md#int8).Max]。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 一个 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 小于等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int8 = m.nextInt8(5)
    if (n is Int8) {
        println("n is Int8")
    }
    try {
        let p: Int8 = m.nextInt8(-1)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 小于等于 0")
    }
    return 0
}
```

运行结果：

```text
n is Int8
参数异常：upper 小于等于 0
```

### func nextUInt16()

```cangjie
public func nextUInt16(): UInt16
```

功能：获取一个 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型的伪随机数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 一个 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt16 = m.nextUInt16()
    if (n is UInt16) {
        println("n is UInt16")
    }
    return 0
}
```

运行结果：

```text
n is UInt16
```