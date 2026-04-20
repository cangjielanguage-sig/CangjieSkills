### extend String <: UnicodeStringExtension

```cangjie
extend String <: UnicodeStringExtension
```

功能：为 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型扩展 [UnicodeRuneExtension](unicode_package_interfaces.md#interface-unicodestringextension) 接口，支持字符集相关的操作。

父类型：

- [UnicodeStringExtension](#interface-unicodestringextension)

#### func isBlank()

```cangjie
public func isBlank(): Bool
```

功能：判断当前字符串是否为空，或仅包含 `Unicode` 字符集中的空字符。

空白字符包括 `0x0009`、`0x000A`、`0x000B`、`0x000C`、`0x000D`、`0x0020`、`0x0085`、`0x00A0`、`0x1680`、`0x2000`、`0x2001`、`0x2002`、`0x2003`、`0x2004`、`0x2005`、`0x2006`、`0x2007`、`0x2008`、`0x2009`、`0x200A`、`0x2028`、`0x2029`、`0x202F`、`0x205F`、`0x3000`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果字符串为空，或仅包含空字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(" \t\n\r".isBlank())
}
```

运行结果：

```text
true
```

#### func toLower()

```cangjie
public func toLower(): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的大写字符转化为小写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全小写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toLower())
}
```

运行结果：

```text
abcdef
```

#### func toLower(CasingOption)

```cangjie
public func toLower(opt: CasingOption): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的大写字符转化为小写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全小写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toLower(CasingOption.Other))
}
```

运行结果：

```text
abcdef
```

#### func toTitle()

```cangjie
public func toTitle(): String
```

功能：将当前字符串中 `Unicode` 字符集范围内可以转换为标题大写字符的转换为标题大写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的标题大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toTitle())
}
```

运行结果：

```text
ABCDEF
```