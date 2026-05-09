### init(UIntNative)

```cangjie
public init(n: UIntNative)
```

功能：通过平台相关无符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 平台相关无符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let uintnative: UIntNative = 24
    let bigInt = BigInt(uintnative)
    println(bigInt)
}
```

运行结果：

```text
24
```

### static func randomProbablePrime(Int64, UInt64, Random)

```cangjie
public static func randomProbablePrime(bitLen: Int64, certainty: UInt64, rand!: Random = Random()): BigInt
```

功能：通过可选的随机数种子构建一个随机的 [BigInt](math_numeric_package_structs.md#struct-bigint) 素数，素数的 bit 长度不超过入参 `bitLen`。

显然，素数必定是大于等于 2 的整数，因此 `bitLen` 必须大于等于 2。素数检测使用 Miller-Rabin 素数测试算法。Miller-Rabin 测试会有概率将一个合数判定为素数，其出错概率随着入参 `certainty` 的增加而减少。

参数：

- bitLen: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 所要生成的随机素数的 bit 长度的上限。
- certainty: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 生成的随机素数通过 Miller-Rabin 素数测试算法的次数，通过的次数越多，将合数误判为素数的概率越低。
- rand!: [Random](../../random/random_package_api/random_package_classes.md#class-random) - 指定的随机数种子。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回生成的随机素数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果指定的 bit 长度小于等于 1，则抛此异常。

示例：
<!-- run -->
```cangjie
import std.math.numeric.BigInt

main() {
    let randomProbablePrime = BigInt.randomProbablePrime(6, 3)
    println(randomProbablePrime)
}
```

### func clearBit(Int64)

```cangjie
public func clearBit(index: Int64): BigInt
```

功能：通过将指定索引位置的 bit 修改为 0 来构造一个新 [BigInt](math_numeric_package_structs.md#struct-bigint)。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需要设置的 bit 位置的索引。`index` 需要大于等于 0。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 一个新的 [BigInt](math_numeric_package_structs.md#struct-bigint)，它是将原 [BigInt](math_numeric_package_structs.md#struct-bigint) 的 `index` 处的 bit 改为 0 的产物。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果入参 `index` 小于 0，则抛此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(1024)
    let clearBit = bigInt.clearBit(10)
    println(clearBit)
}
```

运行结果：

```text
0
```