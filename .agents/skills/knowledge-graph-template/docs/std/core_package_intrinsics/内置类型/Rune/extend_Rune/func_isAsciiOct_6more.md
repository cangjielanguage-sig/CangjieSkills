#### func isAsciiOct()

```cangjie
public func isAsciiOct(): Bool
```

功能：判断字符是否是 Ascii 八进制字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 八进制字符返回 true，否则返回 false。

#### func isAsciiPunctuation()

```cangjie
public func isAsciiPunctuation(): Bool
```

功能：判断字符是否是 Ascii 标点符号字符。其取值范围为 [21, 2F]、[3A, 40]、[5B, 60] 和 [7B, 7E] 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 标点符号字符返回 true，否则返回 false。

#### func isAsciiUpperCase()

```cangjie
public func isAsciiUpperCase(): Bool
```

功能：判断字符是否是 Ascii 大写字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 大写字符返回 true，否则返回 false。

#### func isAsciiWhiteSpace()

```cangjie
public func isAsciiWhiteSpace(): Bool
```

功能：判断字符是否是 Ascii 空白字符。其取值范围为 [09, 0D] 和 {20} 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 空白字符返回 true，否则返回 false。

#### func toAsciiLowerCase()

```cangjie
public func toAsciiLowerCase(): Rune
```

功能：将字符转换为 Ascii 小写字符，如果无法转换则保持现状。

返回值：

- [Rune](core_package_intrinsics.md#rune) - 转换后的字符，如果无法转换则返回原来的 [Rune](core_package_intrinsics.md#rune)。

#### func toAsciiUpperCase()

```cangjie
public func toAsciiUpperCase(): Rune
```

功能：将字符转换为 Ascii 大写字符，如果无法转换则保持现状。

返回值：

- [Rune](core_package_intrinsics.md#rune) - 转换后的字符，如果无法转换则返回原来的 [Rune](core_package_intrinsics.md#rune)。