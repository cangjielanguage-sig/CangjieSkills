### extend BigInt <: Parsable\<BigInt>

```cangjie
extend BigInt <: Parsable<BigInt>
```

功能：此扩展主要用于实现将 [BigInt](#struct-bigint) 类型字面量的字符串转换为 [BigInt](#struct-bigint) 结构体的相关操作函数。

父类型：

- [Parsable](../../convert/convert_package_api/convert_package_interfaces.md#interface-parsablet)\<[BigInt](#struct-bigint)>

#### static func parse(String)

```cangjie
public static func parse(value: String): BigInt
```

功能：将字符串解析成一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

字符串的规则如下，即开头是可选的符号（正号或负号），接进制前缀，再接一串字符串表示的数字：

IntegerString : SignString? BaseString? ValueString

- SignString : + | -

- BaseString : "0b" | "0B" | "0o" | "0O" | "0x" | "0X" | ""

- ValueString : Digits

    - Digits: Digit | Digit Digits

        - Digit : '0' ~ '9' | 'A' ~ 'Z' | 'a' ~ 'z'

            - 如果进制前缀是 "0b" 或 "0B"，则 Digit 取值范围应为 '0' ~ '1'；

            - 如果进制前缀是 "0o" 或 "0O"，则 Digit 取值范围应为 '0' ~ '7'；

            - 如果进制前缀是 "0x" 或 "0X"，则 Digit 取值范围应为 '0' ~ '9'、'a' ~ 'z' 或 'A' ~ 'Z'；

            - 如果进制前缀是空，则 Digit 取值范围应为 '0' ~ '9'。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于构建 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体的字符串。字符串规则为，开头可选一个正号（+）或者负号（-）。接下来可选的进制前缀，默认为十进制，使用 "0b" 或 "0B" 表示二进制，使用 "0o" 或 "0O" 表示八进制，使用 "0x" 或 "0X" 表示十六进制。再接下来必选非空阿拉伯数字或大小写拉丁字母的字符序列，大小写字符含义一样，'a' 和 'A' 的大小等于十进制的 10，'b' 和 'B' 的大小等于十进制的 11，以此类推。序列中的字符应符合相应进制的字符集要求。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 解析出的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串 `value` 不符合上述规则，抛此异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(value: String): ?BigInt
```

功能：尝试将字符串解析成一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

字符串的规则如下，即开头是可选的符号（正号或负号），接进制前缀，再接一串字符串表示的数字：

IntegerString : SignString? BaseString? ValueString

- SignString : + | -

- BaseString : "0b" | "0B" | "0o" | "0O" | "0x" | "0X" | ""

- ValueString : Digits

    - Digits: Digit | Digit Digits

        - Digit : '0' ~ '9' | 'A' ~ 'Z' | 'a' ~ 'z'

            - 如果进制前缀是 "0b" 或 "0B"，则 Digit 取值范围应为 '0' ~ '1'；

            - 如果进制前缀是 "0o" 或 "0O"，则 Digit 取值范围应为 '0' ~ '7'；

            - 如果进制前缀是 "0x" 或 "0X"，则 Digit 取值范围应为 '0' ~ '9'、'a' ~ 'z' 或 'A' ~ 'Z'；

            - 如果进制前缀是空，则 Digit 取值范围应为 '0' ~ '9'。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于构建 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体的字符串。字符串规则为，开头可选一个正号（+）或者负号（-）。接下来可选的进制前缀，默认为十进制，使用 "0b" 或 "0B" 表示二进制，使用 "0o" 或 "0O" 表示八进制，使用 "0x" 或 "0X" 表示十六进制。再接下来必选非空阿拉伯数字或大小写拉丁字母的字符序列，大小写字符含义一样，'a' 和 'A' 的大小等于十进制的 10，'b' 和 'B' 的大小等于十进制的 11，以此类推。序列中的字符应符合相应进制的字符集要求。

返回值：

- ?[BigInt](math_numeric_package_structs.md#struct-bigint) - 解析出的 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体，解析失败则返回 `None`。