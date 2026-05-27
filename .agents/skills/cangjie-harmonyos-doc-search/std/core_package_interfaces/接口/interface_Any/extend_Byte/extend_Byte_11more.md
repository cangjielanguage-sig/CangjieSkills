### extend Byte

```cangjie
extend Byte
```

功能：为 [Byte](core_package_types.md#type-byte) 类型实现一系列扩展方法，主要为在 Ascii 字符集范围内的一些字符判断、转换等操作。

#### func isAscii()

```cangjie
public func isAscii(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 范围内返回 true，否则返回 false。

#### func isAsciiControl()

```cangjie
public func isAsciiControl(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 控制字符范围内。其取值范围为 [00, 1F] 和 {7F} 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 控制字符范围内返回 true，否则返回 false。

#### func isAsciiGraphic()

```cangjie
public func isAsciiGraphic(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 图形字符范围内。其取值范围为 [21, 7E]。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 图形字符范围内返回 true，否则返回 false。

#### func isAsciiHex()

```cangjie
public func isAsciiHex(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 十六进制数字范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 十六进制数字范围内返回 true，否则返回 false。

#### func isAsciiLetter()

```cangjie
public func isAsciiLetter(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 拉丁字母范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 拉丁字母范围内返回 true，否则返回 false。

#### func isAsciiLowerCase()

```cangjie
public func isAsciiLowerCase(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 小写拉丁字母范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 小写拉丁字母范围内返回 true，否则返回 false。

#### func isAsciiNumber()

```cangjie
public func isAsciiNumber(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 十进制数字范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 十进制数字范围内返回 true，否则返回 false。

#### func isAsciiNumberOrLetter()

```cangjie
public func isAsciiNumberOrLetter(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 十进制数字和拉丁字母范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 十进制数字和拉丁字母范围内返回 true，否则返回 false。

#### func isAsciiOct()

```cangjie
public func isAsciiOct(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 八进制数字范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 八进制数字范围内返回 true，否则返回 false。

#### func isAsciiPunctuation()

```cangjie
public func isAsciiPunctuation(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 标点符号范围内。其取值范围为 [21, 2F]、[3A, 40]、[5B, 60] 和 [7B, 7E] 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 标点符号范围内返回 true，否则返回 false。