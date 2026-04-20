## interface RadixConvertible\<T>

```cangjie
public interface RadixConvertible<T> {
    
    static func parse(value: String, radix!: Int64): T

    static func tryParse(value: String, radix!: Int64): Option<T>

    func toString(radix!: Int64): String
}
```

功能：本接口提供了统一的方法，以支持将指定进制的字符串解析为特定类型。

进制将以参数指定，不按字符串前缀指定，进制表示范围必须在 2-36 之间，否则会抛异常，超过十进制的表示按大或者小写英文字母序表示，即 10 个数字 + 26 个英文字母 = 36 进制，Int 系列的字符串可以以 `+`、`-` 开头，如果不以这两个符号开头则处理成 `+`，UInt 系列的字符串可以以 `+` 开头，如果以 `-` 开头会抛出异常。返回指定进制形式字符串，超过十进制的表示按小写英文字母序表示，即 10 个数字 + 26 个小写英文字母 = 36 进制。

本接口提供了 parse 和 tryParse 两套方法，parse 方法将在解析失败时抛出异常，tryParse 方法将返回值用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 包裹，解析失败时将返回 None。
本包内已经为[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)，[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 等基础类型实现该接口，可用于将字符串转换为这些类型。

### static func parse(String, Int64)

```cangjie
static func parse(value: String, radix!: Int64): T
```

功能：从指定进制字符串中解析特定类型。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待解析的字符串。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- T - 转换后的值。

### static func tryParse(String, Int64)

```cangjie
static func tryParse(value: String, radix!: Int64): Option<T>
```

功能：从指定进制字符串中解析特定类型。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待解析的字符串。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 转换后值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。

### func toString(Int64)

```cangjie
func toString(radix!: Int64): String
```

功能：返回指定进制形式字符串。

参数：

- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定进制形式字符串。