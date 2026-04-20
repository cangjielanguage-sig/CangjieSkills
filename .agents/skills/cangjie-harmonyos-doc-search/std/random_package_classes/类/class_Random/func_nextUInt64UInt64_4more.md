### func nextUInt64(UInt64)

```cangjie
public func nextUInt64(upper: UInt64): UInt64
```

功能：获取一个范围在 [0, `upper`) 的 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的伪随机数。

参数：

- upper: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).Max]。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 一个 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt64 = m.nextUInt64(5)
    if (n is UInt64) {
        println("n is UInt64")
    }
    try {
        let p: UInt64 = m.nextUInt64(0)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 等于 0")
    }
    return 0
}
```

运行结果：

```text
n is UInt64
参数异常：upper 等于 0
```

### func nextUInt8()

```cangjie
public func nextUInt8(): UInt8
```

功能：获取一个 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型的伪随机数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 一个 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt8 = m.nextUInt8()
    if (n is UInt8) {
        println("n is UInt8")
    }
    return 0
}
```

运行结果：

```text
n is UInt8
```

### func nextUInt8(UInt8)

```cangjie
public func nextUInt8(upper: UInt8): UInt8
```

功能：获取一个范围在 [0, `upper`) 的 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型的伪随机数。

参数：

- upper: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 生成的伪随机数范围上界（不包括 `upper`），取值范围 (0, [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).Max]。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 一个 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 类型的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `upper` 等于 0，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: UInt8 = m.nextUInt8(5)
    if (n is UInt8) {
        println("n is UInt8")
    }
    try {
        let p: UInt8 = m.nextUInt8(0)
        println(p)
    } catch (e: IllegalArgumentException) {
        println("参数异常：upper 等于 0")
    }
    return 0
}
```

运行结果：

```text
n is UInt8
参数异常：upper 等于 0
```

### func nextUInt8s(Array\<UInt8>) <sup>(deprecated)</sup>

```cangjie
public func nextUInt8s(array: Array<UInt8>): Array<UInt8>
```

功能：生成随机数替换入参数组中的每个元素。

> **注意：**
>
> 未来版本即将废弃，使用 [nextBytes](#func-nextbytesarraybyte) 替代。

参数：

- array: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 被替换的数组。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 返回替换后的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。