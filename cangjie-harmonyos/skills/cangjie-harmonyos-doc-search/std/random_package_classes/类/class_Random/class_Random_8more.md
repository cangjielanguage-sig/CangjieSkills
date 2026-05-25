## class Random

```cangjie
public class Random {
    public init()
    public init(seed: UInt64)
}
```

功能：提供生成伪随机数的相关功能。

示例:
<!-- verify -->
```cangjie
import std.random.*

main() {
    /* 创建 Random 对象并设置种子来获取随机对象 */
    let m: Random = Random(3)
    let b: Bool = m.nextBool()
    let c: Int8 = m.nextInt8()
    print("b=${b is Bool},") /* 对象也可以是 Bool 类型 */
    println("c=${c is Int8}")
    return 0
}
```

运行结果：

```text
b=true,c=true
```

### prop seed

```cangjie
public prop seed: UInt64
```

功能：获取随机数种子。

类型：[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)

### init()

```cangjie
public init()
```

功能：默认无参构造函数创建新的 [Random](random_package_classes.md#class-random) 对象。

### init(UInt64)

```cangjie
public init(seed: UInt64)
```

功能：使用随机数种子创建新的 [Random](random_package_classes.md#class-random) 对象。

参数：

- seed: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 随机数种子，如果设置相同随机种子，生成的伪随机数列表相同。

### func next(UInt64) <sup>(deprecated)</sup>

```cangjie
public func next(bits: UInt64): UInt64
```

功能：生成一个用户指定位长的随机整数。

> **注意：**
>
> 未来版本即将废弃，使用 [nextBits](#func-nextbitsuint64) 替代。

参数：

- bits: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 要生成的伪随机数的位数，取值范围 (0, 64]。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 用户指定位长的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `bits` 等于 0 ，或大于 64，超过所能截取的 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 长度，则抛出异常。

### func nextBits(UInt64)

```cangjie
public func nextBits(bits: UInt64): UInt64
```

功能：生成一个指定位长的随机整数。

参数：

- bits: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 要生成的伪随机数的位数，取值范围 (0, 64]。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 生成的用户指定位长的伪随机数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `bits` 等于 0，或大于 64，超过所能截取的 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 长度，则抛出异常。

### func nextBool()

```cangjie
public func nextBool(): Bool
```

功能：获取一个布尔类型的伪随机值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 一个 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Bool = m.nextBool()
    println("n=${n is Bool}")
    return 0
}
```

运行结果：

```text
n=true
```

### func nextBytes(Array\<Byte>)

```cangjie
public func nextBytes(bytes: Array<Byte>): Unit
```

功能：生成随机数替换入参数组中的每个元素。

参数：

- bytes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 被替换的数组。