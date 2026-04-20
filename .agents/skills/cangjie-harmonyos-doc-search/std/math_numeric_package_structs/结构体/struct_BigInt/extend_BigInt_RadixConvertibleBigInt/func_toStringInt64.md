#### func toString(Int64)

```cangjie
public func toString(radix!: Int64): String
```

功能：计算并返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的任意进制字符串表示。

参数：

- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 进制。字符串所表示的进制，范围为 [2, 36]。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 返回此 [BigInt](math_numeric_package_structs.md#struct-bigint) 的 `radix` 进制字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参 radix 不在 [2, 36] 范围内时，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt(0x400)
    let toString = bigInt.toString(radix: 2)
    println(toString)
}
```

运行结果：

```text
10000000000
```