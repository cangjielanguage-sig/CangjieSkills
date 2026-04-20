### init(BigInt, Int32)

```cangjie
public init(val: BigInt, scale: Int32)
```

功能：通过有符号大整数 [BigInt](math_numeric_package_structs.md#struct-bigint) 和标度值构建 `Deciaml` 结构体。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [BigInt](math_numeric_package_structs.md#struct-bigint) - 有符号大整数值。
- scale: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 标度值。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt
import std.math.numeric.Decimal

main() {
    let bigInt = BigInt(24)
    let decimal = Decimal(bigInt, 4)
    println(decimal)
}
```

运行结果：

```text
0.0024
```

### init(Float16)

```cangjie
public init(val: Float16)
```

功能：通过 16 位有符号浮点数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

> **注意：**
>
> 由于部分十进制小数无法通过二进制浮点数精确表示，此构造函数以精确值构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，传入浮点数值可能与最终构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象字符串打印值不一致。

参数：

- val: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 16 位有符号二进制浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参为 `inf`、`-inf` 或 `nan` 时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let float16: Float16 = 0.8
    let decimal = Decimal(float16)
    println(decimal)
}
```

运行结果：

```text
0.7998046875
```

### init(Float32)

```cangjie
public init(val: Float32)
```

功能：通过 32 位有符号浮点数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

> **注意：**
>
> 由于部分十进制小数无法通过二进制浮点数精确表示，此构造函数以精确值构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，传入浮点数值可能与最终构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象字符串打印值不一致。

参数：

- val: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 32 位有符号二进制浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参为 `inf`、`-inf` 或 `nan` 时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let float32: Float32 = 0.8
    let decimal = Decimal(float32)
    println(decimal)
}
```

运行结果：

```text
0.800000011920928955078125
```