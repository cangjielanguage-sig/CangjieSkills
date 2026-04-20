### init(Bool, Array\<Byte>)

```cangjie
public init(sign: Bool, magnitude: Array<Byte>)
```

功能：通过符号位和真值的绝对值构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。视空数组为 0。

参数：

- sign: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 符号。true 表示非负数，false 表示负数。
- magnitude: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 真值绝对值的二进制原码。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `sign` 为 false 且传入的数组为 0 时，抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(false, [1, 2, 3])
    println(bigInt)
}
```

运行结果：

```text
-66051
```

### init(Bool, Int64, Random)

```cangjie
public init(sign: Bool, bitLen: Int64, rand!: Random = Random())
```

功能：通过指定正负、bit 长度和随机数种子构建一个随机的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。bit 长度需要大于 0。

参数：

- sign: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 指定随机 [BigInt](math_numeric_package_structs.md#struct-bigint) 的正负。
- bitLen: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定随机 [BigInt](math_numeric_package_structs.md#struct-bigint) 的 bit 长度上限。
- rand!: [Random](../../random/random_package_api/random_package_classes.md#class-random) - 指定的随机数种子。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的 bit 长度小于等于 0，则抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.random.*

main() {
    let random = Random(2)
    let bigInt = BigInt(false, 3, rand: random)
    println(bigInt)
}
```

运行结果：

```text
-4
```

### init(Float16)

```cangjie
public init(n: Float16)
```

功能：通过半精度浮点数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

将丢弃浮点数的小数部分，即向零取整。

参数：

- n: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 半精度浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 n 为 `Inf` 或 `NaN`，则抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let float16: Float16 = 24.8
    let bigInt = BigInt(float16)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(Float32)

```cangjie
public init(n: Float32)
```

功能：通过单精度浮点数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

将丢弃浮点数的小数部分，即向零取整。

参数：

- n: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 单精度浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 n 为 `Inf` 或 `NaN`，则抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let float32: Float32 = 24.8
    let bigInt = BigInt(float32)
    println(bigInt)
}
```

运行结果：

```text
24
```