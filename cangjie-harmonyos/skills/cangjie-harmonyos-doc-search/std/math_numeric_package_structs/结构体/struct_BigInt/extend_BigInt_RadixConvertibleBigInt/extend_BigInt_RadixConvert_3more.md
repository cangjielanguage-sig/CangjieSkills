### extend BigInt <: RadixConvertible\<BigInt>

```cangjie
extend BigInt <: RadixConvertible<BigInt>
```

功能：此扩展主要用于实现将 [BigInt](#struct-bigint) 类型字面量的字符串转换为 [BigInt](#struct-bigint) 结构体的相关操作函数。

父类型：

- [RadixConvertible](../../convert/convert_package_api/convert_package_interfaces.md#interface-radixconvertiblet)\<[BigInt](#struct-bigint)>

#### static func parse(String, Int64)

```cangjie
public static func parse(value: String, radix!: Int64): BigInt
```

功能：根据指定进制将字符串解析成一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体，支持 2 进制到 36 进制。

字符串的规则如下，即开头是可选的符号（正号或负号），接一串字符串表示的数字：

IntegerString : SignString? ValueString

- SignString : + | -

- ValueString : Digits

    - Digits: Digit | Digit Digits

        - Digit : '0' ~ '9' | 'A' ~ 'Z' | 'a' ~ 'z'

            - 如果 Digit 在 '0' ~ '9' 内， 需要满足 (Digit - '0') < radix；

            - 如果 Digit 在 'A' ~ 'Z' 内， 需要满足 (Digit - 'A') + 10 < radix；

            - 如果 Digit 在 'a' ~ 'z' 内， 需要满足 (Digit - 'A') + 10 < radix。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于构建 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体的字符串。字符串规则为，开头可选一个正号（+）或者负号（-）。接下来必选非空阿拉伯数字或大小写拉丁字母的字符序列，大小写字符含义一样，'a' 和 'A' 的大小等于十进制的 10，'b' 和 'B' 的大小等于十进制的 11，以此类推。序列中的字符大小不得大于等于进制大小。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 进制。字符串所表示的进制，范围为 [2, 36]。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 解析出的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串 `value` 不符合上述规则，或 `radix` 表示的进制不在 [2, 36] 区间内，抛此异常。

#### static func tryParse(String, Int64)

```cangjie
public static func tryParse(value: String, radix!: Int64): ?BigInt
```

功能：尝试根据指定进制将字符串解析成一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体，支持 2 进制到 36 进制。

字符串的规则如下，即开头是可选的符号（正号或负号），接一串字符串表示的数字：

IntegerString : SignString? ValueString

- SignString : + | -

- ValueString : Digits

    - Digits: Digit | Digit Digits

        - Digit : '0' ~ '9' | 'A' ~ 'Z' | 'a' ~ 'z'

            - 如果 Digit 在 '0' ~ '9' 内， 需要满足 (Digit - '0') < radix；

            - 如果 Digit 在 'A' ~ 'Z' 内， 需要满足 (Digit - 'A') + 10 < radix；

            - 如果 Digit 在 'a' ~ 'z' 内， 需要满足 (Digit - 'A') + 10 < radix。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于构建 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体的字符串。字符串规则为，开头可选一个正号（+）或者负号（-）。接下来必选非空阿拉伯数字或大小写拉丁字母的字符序列，大小写字符含义一样，'a' 和 'A' 的大小等于十进制的 10，'b' 和 'B' 的大小等于十进制的 11，以此类推。序列中的字符大小不得大于等于进制大小。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 进制。字符串所表示的进制，范围为 [2, 36]。

返回值：

- ?[BigInt](math_numeric_package_structs.md#struct-bigint) - 解析出的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体，解析失败时返回 `None`。