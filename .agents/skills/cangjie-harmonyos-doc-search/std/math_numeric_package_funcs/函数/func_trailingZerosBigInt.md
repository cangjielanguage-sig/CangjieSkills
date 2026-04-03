## func trailingZeros(BigInt)

```cangjie
public func trailingZeros(x: BigInt): Int64
```

功能：求 `BigInt` 的二进制表达中的从最低位算起，连续位为 0 的个数。如果最低位不是 0，则返回 0。

参数：

- x: [BigInt](math_numeric_package_structs.md#struct-bigint) - 需要求后置 0 的 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 后置 0 的位数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.{BigInt, trailingZeros}

main() {
    let x: BigInt = BigInt(0xC000_0000)
    let trailingZeros = trailingZeros(x)
    println(trailingZeros)
}
```

运行结果：

```text
30
```