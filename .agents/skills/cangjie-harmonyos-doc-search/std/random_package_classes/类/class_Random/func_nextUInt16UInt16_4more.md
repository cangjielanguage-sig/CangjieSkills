### func nextUInt16(UInt16)

```cangjie
public func nextUInt16(upper: UInt16): UInt16
```

功能：获取一个范围在 [0, `upper`) 的 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型的伪随机数。

参数：

- upper: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).Max]。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 一个 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt16 = m.nextUInt16(5)
    if (n is UInt16) {
        println("n is UInt16")
    }
    try {
        let p: UInt16 = m.nextUInt16(0)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 等于 0")
    }
    return 0
}
```

运行结果：

```text
n is UInt16
参数异常：upper 等于 0
```

### func nextUInt32()

```cangjie
public func nextUInt32(): UInt32
```

功能：获取一个 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型的伪随机数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 一个 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt32 = m.nextUInt32()
    if (n is UInt32) {
        println("n is UInt32")
    }
    return 0
}
```

运行结果：

```text
n is UInt32
```

### func nextUInt32(UInt32)

```cangjie
public func nextUInt32(upper: UInt32): UInt32
```

功能：获取一个范围在 [0, `upper`) 的 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型的伪随机数。

参数：

- upper: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).Max]。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 一个 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt32 = m.nextUInt32(5)
    if (n is UInt32) {
        println("n is UInt32")
    }
    try {
        let p: UInt32 = m.nextUInt32(0)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 等于 0")
    }
    return 0
}
```

运行结果：

```text
n is UInt32
参数异常：upper 等于 0
```

### func nextUInt64()

```cangjie
public func nextUInt64(): UInt64
```

功能：获取一个 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的伪随机数。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 一个 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt64 = m.nextUInt64()
    if (n is UInt64) {
        println("n is UInt64")
    }
    return 0
}
```

运行结果：

```text
n is UInt64
```