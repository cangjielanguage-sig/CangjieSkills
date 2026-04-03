### func startsWith(String)

```cangjie
public func startsWith(prefix: String): Bool
```

功能：判断原字符串是否以 prefix 字符串为前缀。

参数：

- prefix: [String](core_package_structs.md#struct-string) - 被判断的前缀字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果字符串 str 是原字符串的前缀，返回 true，否则返回 false，特别地，如果 str 字符串长度为 0，返回 true。

### func toArray()

```cangjie
public func toArray(): Array<Byte>
```

功能：获取字符串的 UTF-8 编码的字节数组。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[Byte](core_package_types.md#type-byte)> - 字符串的 UTF-8 编码的字节数组。

### func toAsciiLower()

```cangjie
public func toAsciiLower(): String
```

功能：将该字符串中所有 Ascii 大写字母转化为 Ascii 小写字母。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。

### func toAsciiTitle()

```cangjie
public func toAsciiTitle(): String
```

功能：将该字符串标题化。

该函数只转换 Ascii 英文字符，当该英文字符是字符串中第一个字符或者该字符的前一个字符不是英文字符，则该字符大写，其他英文字符小写。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。

### func toAsciiUpper()

```cangjie
public func toAsciiUpper(): String
```

功能：将该字符串中所有 Ascii 小写字母转化为 Ascii 大写字母。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。

### func toRuneArray()

```cangjie
public func toRuneArray(): Array<Rune>
```

功能：获取字符串的 Rune 数组。如果原字符串为空字符串，则返回空数组。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<Rune> - 字符串的 Rune 数组。

### func toString()

```cangjie
public func toString(): String
```

功能：获得字符串本身。

返回值：

- [String](core_package_structs.md#struct-string) - 返回字符串本身。

### func trimAscii()

```cangjie
public func trimAscii(): String
```

功能：去除原字符串开头结尾以 ASCII 空白字符组成的子字符串。

ASCII 空白字符包括 ASCII 码在区间 [0x09, 0x0D] 范围内的字符以及 ASCII 码为 0x20 的字符。具体字符见下表。

| 字符含义 | ASCII 码 |
| --- | --- |
| 水平制表符 (\t, HT) | 0x09 |
| 换行符 (\n, LF) | 0x0A |
| 垂直制表符 (\v, VT) | 0x0B |
| 换页符 (\f, FF) | 0x0C |
| 回车符 (\r, CR) | 0x0D |
| 空格 (Space) | 0x20 |

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。

### func trimAsciiEnd()

```cangjie
public func trimAsciiEnd(): String
```

功能：去除原字符串结尾以 ASCII 空白字符组成的子字符串。

ASCII 空白字符包括 ASCII 码在区间 [0x09, 0x0D] 范围内的字符以及 ASCII 码为 0x20 的字符。具体字符见 [trimAscii()](#func-trimascii)。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。

### func trimAsciiStart()

```cangjie
public func trimAsciiStart(): String
```

功能：去除原字符串开头以 ASCII 空白字符组成的子字符串。

ASCII 空白字符包括 ASCII 码在区间 [0x09, 0x0D] 范围内的字符以及 ASCII 码为 0x20 的字符。具体字符见 [trimAscii()](#func-trimascii)。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的新字符串。