## struct Decimal

```cangjie
public struct Decimal <: Comparable<Decimal> & Hashable & ToString {
    public init(val: String)
    public init(val: BigInt, scale: Int32)
    public init(val: BigInt)
    public init(val: Int8)
    public init(val: Int16)
    public init(val: Int32)
    public init(val: IntNative)
    public init(val: Int64)
    public init(val: UInt8)
    public init(val: UInt16)
    public init(val: UInt32)
    public init(val: UIntNative)
    public init(val: UInt64)
    public init(val: Float16)
    public init(val: Float32)
    public init(val: Float64)
}
```

功能：[Decimal](math_numeric_package_structs.md#struct-decimal) 用于表示任意精度的有符号的十进制数。允许操作过程指定结果精度及舍入规则。提供基础类型（Int、UInt、[String](../../core/core_package_api/core_package_structs.md#struct-string)、Float 等）与 [BigInt](math_numeric_package_structs.md#struct-bigint) 类型互相转换能力，支持 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象基本属性查询等能力，支持基础数学运算操作，提供对象比较、hash、字符串打印等基础能力。

父类型：

- [Comparable](../../core/core_package_api/core_package_interfaces.md#interface-comparablet)\<[Decimal](#struct-decimal)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop precision

```cangjie
public prop precision: Int64
```

功能：获取 [Decimal](math_numeric_package_structs.md#struct-decimal) 精度值，即无标度整数部分十进制有效数字位数，非负数。如果精度值为 0，表示无精度限制。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop scale

```cangjie
public prop scale: Int32
```

功能：获取 [Decimal](math_numeric_package_structs.md#struct-decimal) 标度值。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### prop sign

```cangjie
public prop sign: Int64
```

功能：获取 [Decimal](math_numeric_package_structs.md#struct-decimal) 实例符号值。

- [Decimal](math_numeric_package_structs.md#struct-decimal) 值大于 0，返回 1；
- [Decimal](math_numeric_package_structs.md#struct-decimal) 值等于 0，返回 0；
- [Decimal](math_numeric_package_structs.md#struct-decimal) 值小于 0，返回 -1。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop value

```cangjie
public prop value: BigInt
```

功能：获取 [Decimal](math_numeric_package_structs.md#struct-decimal) 无标度整数值，[BigInt](math_numeric_package_structs.md#struct-bigint) 承载。

类型：[BigInt](math_numeric_package_structs.md#struct-bigint)

### init(BigInt)

```cangjie
public init(val: BigInt)
```

功能：通过有符号大整数 [BigInt](math_numeric_package_structs.md#struct-bigint) 构建 `Deciaml` 结构体。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [BigInt](math_numeric_package_structs.md#struct-bigint) - 有符号大整数值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.Decimal

main() {
    let bigInt = BigInt(24)
    let decimal = Decimal(bigInt)
    println(decimal)
}
```

运行结果：

```text
24
```