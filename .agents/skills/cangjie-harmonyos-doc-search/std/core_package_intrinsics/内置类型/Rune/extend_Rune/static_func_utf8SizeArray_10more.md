#### static func utf8Size(Array\<UInt8>, Int64)

```cangjie
public static func utf8Size(arr: Array<UInt8>, index: Int64): Int64
```

功能：该函数会返回字节数组指定索引位置为起始的字符占用的字节数。

在 UTF-8 编码中，ASCII 码首位字节第一位不为 1，其他长度的字符首位字节开头 1 的个数表明了该字符对应的字节码长度，该函数通过扫描首位，判断字节码长度。如果索引对应的不是首位字节码，就会抛出异常。

参数：

- arr: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 待获取字符的字节数组。
- index: [Int64](core_package_intrinsics.md#int64) - 指定字符的索引。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 字符的字节码长度，例如中文是三个字节码长度。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果索引位置的字节码不符合首位字节码规则，会抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<UInt8> = [1u8, 2u8, 231u8, 136u8, 177u8, 145u8]
    var len: Int64 = Rune.utf8Size(arr, 2)
    println(len) // 索引为2-4的数组元素为中文字符爱的utf-8编码，占用三字节
}
```

运行结果：

```text
3
```

#### static func utf8Size(Rune)

```cangjie
public static func utf8Size(c: Rune): Int64
```

功能：返回字符对应的 UTF-8 编码的字节码长度，例如中文字符的字节码长度是 3。

参数：

- c: [Rune](core_package_intrinsics.md#rune) - 待计算 UTF-8 字节码长度的字符。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 字符的 UTF-8 字节码长度。

示例：

<!-- verify -->
```cangjie
main() {
    var char: Rune = r'爱'
    var len: Int64 = Rune.utf8Size(char)
    println(len) // 中文字符爱的utf-8编码，占用三字节
}
```

运行结果：

```text
3
```

#### func isAscii()

```cangjie
public func isAscii(): Bool
```

功能：判断字符是否是 Ascii 中的字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 字符返回 true，否则返回 false。

#### func isAsciiControl()

```cangjie
public func isAsciiControl(): Bool
```

功能：判断字符是否是 Ascii 控制字符。其取值范围为 [00, 1F] 和 {7F} 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 控制字符返回 true，否则返回 false。

#### func isAsciiGraphic()

```cangjie
public func isAsciiGraphic(): Bool
```

功能：判断字符是否是 Ascii 图形字符。其取值范围为 [21, 7E]。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 图形字符返回 true，否则返回 false。

#### func isAsciiHex()

```cangjie
public func isAsciiHex(): Bool
```

功能：判断字符是否是 Ascii 十六进制字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 十六进制字符返回 true，否则返回 false。

#### func isAsciiLetter()

```cangjie
public func isAsciiLetter(): Bool
```

功能：判断字符是否是 Ascii 字母字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 字母字符返回 true，否则返回 false。

#### func isAsciiLowerCase()

```cangjie
public func isAsciiLowerCase(): Bool
```

功能：判断字符是否是 Ascii 小写字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 小写字符返回 true，否则返回 false。

#### func isAsciiNumber()

```cangjie
public func isAsciiNumber(): Bool
```

功能：判断字符是否是 Ascii 数字字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 数字字符返回 true，否则返回 false。

#### func isAsciiNumberOrLetter()

```cangjie
public func isAsciiNumberOrLetter(): Bool
```

功能：判断字符是否是 Ascii 数字或拉丁字母字符。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是 Ascii 数字或拉丁字母字符返回 true，否则返回 false。