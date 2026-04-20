## interface UnicodeRuneExtension

```cangjie
public interface UnicodeRuneExtension {
    func isLetter(): Bool
    func isLowerCase(): Bool
    func isNumber(): Bool
    func isTitleCase(): Bool
    func isUpperCase(): Bool
    func isWhiteSpace(): Bool
    func toLowerCase(): Rune
    func toLowerCase(opt: CasingOption): Rune
    func toTitleCase(): Rune
    func toTitleCase(opt: CasingOption): Rune
    func toUpperCase(): Rune
    func toUpperCase(opt: CasingOption): Rune
}
```

功能：`Unicode` 字符集相关扩展的接口。

可用于为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型增加一系列与 `Unicode` 字符集相关的扩展函数，包括字符类型判断，字符大小写转换，删除空白字符等。

### func isLetter()

```cangjie
func isLetter(): Bool
```

功能：判断该类型否是 `Unicode` 字母字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 字母字符，返回 `true`，否则返回 `false`。

### func isLowerCase()

```cangjie
func isLowerCase(): Bool
```

功能：判断该类型是否是 `Unicode` 小写字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 小写字符，返回 `true`，否则返回 `false`。

### func isNumber()

```cangjie
func isNumber(): Bool
```

功能：判断类型是否是 `Unicode` 数字字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 数字字符，返回 `true`，否则返回 `false`。

### func isTitleCase()

```cangjie
func isTitleCase(): Bool
```

功能：判断该类型是否是 `Unicode` 标题化字符。

`Unicode` 中的标题化字符指的是一种特殊的字母形式，它们在某些语言中用于表示标题中每个单词的首字母大写的形式。这些字母由特殊的字符表示，例如 U+01C5（ǅ）和 U+01F1（Ǳ）。这些字符通常用于一些东欧语言，如克罗地亚语和塞尔维亚语。

标题化字符包括：`0x01C5`、`0x01C8`、`0x01CB`、`0x01F2`、`0x1F88 - 0x1F8F`、`0x1F98 - 0x1F9F`、`0x1F98 - 0x1F9F`、`0x1FA8 - 0x1FAF`、`0x1FBC`、`0x1FCC`、`0x1FFC`

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 标题大写字符，返回 `true`，否则返回 `false`。

### func isUpperCase()

```cangjie
func isUpperCase(): Bool
```

功能：判断该类型是否是 `Unicode` 大写字符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 大写字符，返回 `true`，否则返回 `false`。

### func isWhiteSpace()

```cangjie
func isWhiteSpace(): Bool
```

功能：判断该类型是否是 `Unicode` 空白字符。

空白字符包括 `0x0009`、`0x000A`、`0x000B`、`0x000C`、`0x000D`、`0x0020`、`0x0085`、`0x00A0`、`0x1680`、`0x2000`、`0x2001`、`0x2002`、`0x2003`、`0x2004`、`0x2005`、`0x2006`、`0x2007`、`0x2008`、`0x2009`、`0x200A`、`0x2028`、`0x2029`、`0x202F`、`0x205F`、`0x3000`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型是 `Unicode` 空白字符，返回 `true`，否则返回 `false`。

### func toLowerCase()

```cangjie
func toLowerCase(): Rune
```

功能：获取该类型对应的 `Unicode` 小写字符。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前类型对应的小写字符。

### func toLowerCase(CasingOption)

```cangjie
func toLowerCase(opt: CasingOption): Rune
```

功能：获取该类型对应的 `Unicode` 小写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前类型对应的小写字符。