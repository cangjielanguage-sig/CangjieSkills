### extend Rune <: UnicodeRuneExtension

```cangjie
extend Rune <: UnicodeRuneExtension
```

功能：为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型扩展 [UnicodeRuneExtension](unicode_package_interfaces.md#interface-unicoderuneextension) 接口，支持字符集相关的操作。

父类型：

- [UnicodeRuneExtension](#interface-unicoderuneextension)

#### func isLetter()

```cangjie
public func isLetter(): Bool
```

功能：判断字符是否是 `Unicode` 字母字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 字母字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.isLetter())
    println(r'1'.isLetter())
}
```

运行结果：

```text
true
false
```

#### func isLowerCase()

```cangjie
public func isLowerCase(): Bool
```

功能：判断字符是否是 `Unicode` 小写字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 小写字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.isLowerCase())
    println(r'A'.isLowerCase())
}
```

运行结果：

```text
true
false
```

#### func isNumber()

```cangjie
public func isNumber(): Bool
```

功能：判断字符是否是 `Unicode` 数字字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 数字字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.isNumber())
    println(r'1'.isNumber())
}
```

运行结果：

```text
false
true
```

#### func isTitleCase()

```cangjie
public func isTitleCase(): Bool
```

功能：判断字符是否是 `Unicode` 标题化字符。

`Unicode` 中的标题化字符指的是一种特殊的字母形式，它们在某些语言中用于表示标题中每个单词的首字母大写的形式。这些字母由特殊的字符表示，例如 U+01C5（ǅ）和 U+01F1（Ǳ）。这些字符通常用于一些东欧语言，如克罗地亚语和塞尔维亚语。

标题化字符包括：`0x01C5`、`0x01C8`、`0x01CB`、`0x01F2`、`0x1F88 - 0x1F8F`、`0x1F98 - 0x1F9F`、`0x1F98 - 0x1F9F`、`0x1FA8 - 0x1FAF`、`0x1FBC`、`0x1FCC`、`0x1FFC`

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 标题大写字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'ǅ'.isTitleCase())
}
```

运行结果：

```text
true
```

#### func isUpperCase()

```cangjie
public func isUpperCase(): Bool
```

功能：判断字符是否是 `Unicode` 大写字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 大写字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.isUpperCase())
    println(r'A'.isUpperCase())
}
```

运行结果：

```text
false
true
```

#### func isWhiteSpace()

```cangjie
public func isWhiteSpace(): Bool
```

功能：判断字符是否是 `Unicode` 空白字符。

空白字符包括 `0x0009`、`0x000A`、`0x000B`、`0x000C`、`0x000D`、`0x0020`、`0x0085`、`0x00A0`、`0x1680`、`0x2000`、`0x2001`、`0x2002`、`0x2003`、`0x2004`、`0x2005`、`0x2006`、`0x2007`、`0x2008`、`0x2009`、`0x200A`、`0x2028`、`0x2029`、`0x202F`、`0x205F`、`0x3000`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该字符是 `Unicode` 空白字符，返回 `true`，否则返回 `false`。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r' '.isWhiteSpace())
}
```

运行结果：

```text
true
```