### func nextInt16(Int16)

```cangjie
public func nextInt16(upper: Int16): Int16
```

功能：获取一个范围在 [0, `upper`) 的 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型的伪随机数。

参数：

- upper: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 表示生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [Int16](../../core/core_package_api/core_package_intrinsics.md#int16).Max]。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 一个 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 小于等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int16 = m.nextInt16(5)
    if (n is Int16) {
        println("n is Int16")
    }
    try {
        let p: Int16 = m.nextInt16(-1)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 小于等于 0")
    }
    return 0
}
```

运行结果：

```text
n is Int16
参数异常：upper 小于等于 0
```

### func nextInt32()

```cangjie
public func nextInt32(): Int32
```

功能：获取一个 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型的伪随机数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 一个 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int32 = m.nextInt32()
    if (n is Int32) {
        println("n is Int32")
    }
    return 0
}
```

运行结果：

```text
n is Int32
```

### func nextInt32(Int32)

```cangjie
public func nextInt32(upper: Int32): Int32
```

功能：获取一个范围在 [0, `upper`) 的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型的伪随机数。

参数：

- upper: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 表示生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [Int32](../../core/core_package_api/core_package_intrinsics.md#int32).Max]。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 一个 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 小于等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int32 = m.nextInt32(5)
    if (n is Int32) {
        println("n is Int32")
    }
    try {
        let p: Int32 = m.nextInt32(-1)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 小于等于 0")
    }
    return 0
}
```

运行结果：

```text
n is Int32
参数异常：upper 小于等于 0
```

### func nextInt64()

```cangjie
public func nextInt64(): Int64
```

功能：获取一个 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的伪随机数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 一个 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int64 = m.nextInt64()
    if (n is Int64) {
        println("n is Int64")
    }
    return 0
}
```

运行结果：

```text
n is Int64
```