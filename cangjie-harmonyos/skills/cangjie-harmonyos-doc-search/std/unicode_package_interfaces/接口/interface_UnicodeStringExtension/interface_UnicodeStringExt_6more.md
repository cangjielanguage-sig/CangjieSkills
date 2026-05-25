## interface UnicodeStringExtension

```cangjie
public interface UnicodeStringExtension {
    func isBlank(): Bool
    func toLower(): String
    func toLower(opt: CasingOption): String
    func toTitle(): String
    func toTitle(opt: CasingOption): String
    func toUpper(): String
    func toUpper(opt: CasingOption): String
    func trim(): String
    func trimEnd(): String
    func trimLeft(): String
    func trimRight(): String
    func trimStart(): String
}
```

功能：`Unicode` 字符集相关扩展的接口。

可用于为 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型增加一系列与 `Unicode` 字符集相关的扩展函数，包括字符类型判断，字符大小写转换，删除空白字符等。

### func isBlank()

```cangjie
func isBlank(): Bool
```

功能：判断当前字符串是否为空，或仅包含 `Unicode` 字符集中的空字符。

空白字符包括 `0x0009`、`0x000A`、`0x000B`、`0x000C`、`0x000D`、`0x0020`、`0x0085`、`0x00A0`、`0x1680`、`0x2000`、`0x2001`、`0x2002`、`0x2003`、`0x2004`、`0x2005`、`0x2006`、`0x2007`、`0x2008`、`0x2009`、`0x200A`、`0x2028`、`0x2029`、`0x202F`、`0x205F`、`0x3000`。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果字符串为空，或仅包含空字符，返回 `true`，否则返回 `false`。

### func toLower()

```cangjie
func toLower(): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的大写字符转化为小写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全小写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

### func toLower(CasingOption)

```cangjie
func toLower(opt: CasingOption): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的大写字符转化为小写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全小写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

### func toTitle()

```cangjie
func toTitle(): String
```

功能：将当前字符串中 `Unicode` 字符集范围内可以转换为标题大写字符的转换为标题大写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的标题大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

### func toTitle(CasingOption)

```cangjie
func toTitle(opt: CasingOption): String
```

功能：将当前字符串中 `Unicode` 字符集范围内可以转换为标题大写字符的转换为标题大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的标题大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。