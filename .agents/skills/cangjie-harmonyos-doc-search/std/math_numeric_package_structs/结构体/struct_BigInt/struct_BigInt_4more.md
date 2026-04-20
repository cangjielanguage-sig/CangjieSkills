## struct BigInt

```cangjie
public struct BigInt <: Comparable<BigInt> & Hashable & ToString {
    public init(bytes: Array<Byte>)
    public init(sign: Bool, magnitude: Array<Byte>)
    public init(n: Int8)
    public init(n: Int16)
    public init(n: Int32)
    public init(n: Int64)
    public init(n: UInt8)
    public init(n: UInt16)
    public init(n: UInt32)
    public init(n: UInt64)
    public init(n: UIntNative)
    public init(n: IntNative)
    public init(n: Float16)
    public init(n: Float32)
    public init(n: Float64)
    public init(sign: Bool, bitLen: Int64, rand!: Random = Random())
    public init(s: String, base!: Int64 = 10)
}
```

功能：[BigInt](math_numeric_package_structs.md#struct-bigint) 定义为任意精度（二进制）的有符号整数。仓颉的 struct [BigInt](math_numeric_package_structs.md#struct-bigint) 用于任意精度有符号整数的计算，类型转换等。

父类型：

- [Comparable](../../core/core_package_api/core_package_interfaces.md#interface-comparablet)\<[BigInt](#struct-bigint)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop bitLen

```cangjie
public prop bitLen: Int64
```

功能：获取此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的最短 bit 长度。如 -3 (101) 返回 3，-1 (11) 返回 2，0 (0) 返回 1。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt1 = BigInt(-3)
    let bitLen1 = bigInt1.bitLen
    println(bitLen1)

    let bigInt2 = BigInt(-1)
    let bitLen2 = bigInt2.bitLen
    println(bitLen2)

    let bigInt3 = BigInt(0)
    let bitLen3 = bigInt3.bitLen
    println(bitLen3)
}
```

运行结果：

```text
3
2
1
```

### prop sign

```cangjie
public prop sign: Int64
```

功能：获取此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的符号。正数返回 1；0 返回 0；负数返回 -1。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt1 = BigInt(-3)
    let sign1 = bigInt1.sign
    println(sign1)

    let bigInt2 = BigInt(3)
    let sign2 = bigInt2.sign
    println(sign2)

    let bigInt3 = BigInt(0)
    let sign3 = bigInt3.sign
    println(sign3)
}
```

运行结果：

```text
-1
1
0
```

### init(Array\<Byte>)

```cangjie
public init(bytes: Array<Byte>)
```

功能：通过大端的 [Byte](../../core/core_package_api/core_package_types.md#type-byte) 数组以补码形式构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

> **说明：**
>
> 数据存储方法有以下两种：
>
> - 大端存储方式：高位字节存放在低位地址。
> - 小端存储方式：将数据的低位字节存放在内存的高位地址。

参数：

- bytes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 大端二进制补码数组，数组长度不能为空。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当传入空数组时，抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt([1, 2, 3])
    println(bigInt)
}
```

运行结果：

```text
66051
```