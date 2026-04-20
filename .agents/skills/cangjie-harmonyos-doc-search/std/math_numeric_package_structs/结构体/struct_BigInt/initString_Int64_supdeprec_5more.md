### init(String, Int64) <sup>(deprecated)</sup>

```cangjie
public init(s: String, base!: Int64 = 10)
```

功能：通过字符串和进制构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体，支持 2 进制到 36 进制。

字符串的规则如下，即开头是可选的符号（正号或负号），接一串字符串表示的数字：

IntegerString : (SignString)? ValueString

- SignString    : + | -

- ValueString   : Digits

    - Digits: Digit | Digit Digits

        - Digit         : '0' ~ '9' | 'A' ~ 'Z' | 'a' ~ 'z'

            - 如果 Digit 在 '0' ~ '9' 内， 需要满足 (Digit - '0') < base；

            - 如果 Digit 在 'A' ~ 'Z' 内， 需要满足 (Digit - 'A') + 10 < base；

            - 如果 Digit 在 'a' ~ 'z' 内， 需要满足 (Digit - 'A') + 10 < base。

> **注意：**
>
> 未来版本即将废弃，使用 [parse(String, Int64)](./math_numeric_package_structs.md) 替代。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于构建 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体的字符串。字符串规则为，开头可选一个正号（+）或者负号（-）。接下来必选非空阿拉伯数字或大小写拉丁字母的字符序列，大小写字符含义一样，'a' 和 'A' 的大小等于十进制的 10，'b' 和 'B' 的大小等于十进制的 11，以此类推。序列中的字符大小不得大于等于进制大小。
- base!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 进制。字符串所表示的进制，范围为 [2, 36]。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串 `s` 不符合上述规则，或 `base` 表示的进制不在 [2, 36] 区间内，抛此异常。

### init(UInt16)

```cangjie
public init(n: UInt16)
```

功能：通过 16 位无符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16 位无符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let uint16: UInt16 = 24
    let bigInt = BigInt(uint16)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(UInt32)

```cangjie
public init(n: UInt32)
```

功能：通过 32 位无符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 32 位无符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let uint32: UInt32 = 24
    let bigInt = BigInt(uint32)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(UInt64)

```cangjie
public init(n: UInt64)
```

功能：通过 64 位无符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 64 位无符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let uint64: UInt64 = 24
    let bigInt = BigInt(uint64)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(UInt8)

```cangjie
public init(n: UInt8)
```

功能：通过 8 位无符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 8 位无符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let uint8: UInt8 = 24
    let bigInt = BigInt(uint8)
    println(bigInt)
}
```

运行结果：

```text
24
```