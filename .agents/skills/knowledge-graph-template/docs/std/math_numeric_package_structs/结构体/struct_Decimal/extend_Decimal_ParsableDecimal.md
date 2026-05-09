### extend Decimal <: Parsable\<Decimal>

```cangjie
extend Decimal <: Parsable<Decimal>
```

功能：此扩展主要用于实现将 [Decimal](#struct-decimal) 类型字面量的字符串转换为 [Decimal](#struct-decimal) 结构体的相关操作函数。

父类型：

- [Parsable](../../convert/convert_package_api/convert_package_interfaces.md#interface-parsablet)\<[Decimal](#struct-decimal)>

#### static func parse(String)

```cangjie
public static func parse(value: String): Decimal
```

功能：通过规定格式字符串构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。默认采用精度值为 0，即无限精度进行构建。字符串需满足如下格式，即开头可选的符号（正号或负号），接 ValueString 字符串，再接可选的 ExponentString 字符串：

[Decimal](math_numeric_package_structs.md#struct-decimal) 字符串: SignString? ValueString ExponentString?

- SignString: + | -

- ValueString: IntegerPart.(FractionPart)? | .FractionPart | IntegerPart

    - IntegerPart：Digits

    - FractionPart：Digits

    - Digits: Digit | Digit Digits

        - Digit：'0' ~ '9'

- ExponentString: ExponentIndicator (SignString)? IntegerPart

    - ExponentIndicator：e | E

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 规定格式字符串。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 解析出的 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参字符串不满足规定格式时，抛此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当构建值标度溢出时，抛此异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(value: String): ?Decimal
```

功能：尝试通过规定格式字符串构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。默认采用精度值为 0，即无限精度进行构建。字符串需满足如下格式，即开头可选的符号（正号或负号），接 ValueString 字符串，再接可选的 ExponentString 字符串：

[Decimal](math_numeric_package_structs.md#struct-decimal) 字符串: SignString? ValueString ExponentString?

- SignString: + | -

- ValueString: IntegerPart.(FractionPart)? | .FractionPart | IntegerPart

    - IntegerPart：Digits

    - FractionPart：Digits

    - Digits: Digit | Digit Digits

        - Digit：'0' ~ '9'

- ExponentString: ExponentIndicator (SignString)? IntegerPart

    - ExponentIndicator：e | E

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 规定格式字符串。

返回值：

- ?[Decimal](math_numeric_package_structs.md#struct-decimal) - 解析出的 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体，解析失败则返回 `None`。