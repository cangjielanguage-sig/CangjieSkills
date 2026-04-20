### init(String) <sup>(deprecated)</sup>

```cangjie
public init(val: String)
```

功能：通过规定格式字符串构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 结构体。默认采用精度值为 0，即无限精度进行构建。字符串需满足如下格式，即开头可选的符号（正号或负号），接 ValueString 字符串，再接可选的 ExponentString 字符串：

[Decimal](math_numeric_package_structs.md#struct-decimal) 字符串: (SignString)? ValueString (ExponentString)?

- SignString: + | -

- ValueString: IntegerPart.(FractionPart)? | .FractionPart | IntegerPart

    - IntegerPart：Digits

    - FractionPart：Digits

    - Digits: Digit | Digit Digits

        - Digit：'0' ~ '9'

- ExponentString: ExponentIndicator (SignString)? IntegerPart

    - ExponentIndicator：e | E

> **注意：**
>
> 未来版本即将废弃，使用 `parse(String)` 替代。

参数：

- val: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 规定格式字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参字符串不满足规定格式时，抛此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当构建值标度溢出时，抛此异常。

### init(UInt16)

```cangjie
public init(val: UInt16)
```

功能：通过 16 位无符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 16 位无符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let uint16: UInt16 = 24
    let decimal = Decimal(uint16)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(UInt32)

```cangjie
public init(val: UInt32)
```

功能：通过 32 位无符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 32 位无符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let uint32: UInt32 = 24
    let decimal = Decimal(uint32)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(UInt64)

```cangjie
public init(val: UInt64)
```

功能：通过 64 位无符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 64 位无符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let uint64: UInt64 = 24
    let decimal = Decimal(uint64)
    println(decimal)
}
```

运行结果：

```text
24
```

### init(UInt8)

```cangjie
public init(val: UInt8)
```

功能：通过 8 位无符号整数构建 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象。默认采用精度值为 0，即无限精度进行构建。

参数：

- val: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 8 位无符号整数。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main() {
    let uint8: UInt8 = 24
    let decimal = Decimal(uint8)
    println(decimal)
}
```

运行结果：

```text
24
```