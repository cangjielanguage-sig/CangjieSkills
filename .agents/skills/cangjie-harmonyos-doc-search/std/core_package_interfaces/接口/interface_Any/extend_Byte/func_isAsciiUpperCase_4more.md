#### func isAsciiUpperCase()

```cangjie
public func isAsciiUpperCase(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 大写拉丁字母范围内。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 大写拉丁字母范围内返回 true，否则返回 false。

#### func isAsciiWhiteSpace()

```cangjie
public func isAsciiWhiteSpace(): Bool
```

功能：判断 [Byte](core_package_types.md#type-byte) 是否是在 Ascii 空白字符范围内。其取值范围为 [09, 0D] 和 {20} 的并集。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 [Byte](core_package_types.md#type-byte) 在 Ascii 空白字符范围内返回 true，否则返回 false。

#### func toAsciiLowerCase()

```cangjie
public func toAsciiLowerCase(): Byte
```

功能：将 [Byte](core_package_types.md#type-byte) 换为对应的 Ascii 小写字符 [Byte](core_package_types.md#type-byte)，如果无法转换则保持现状。

返回值：

- [Byte](core_package_types.md#type-byte) - 转换后的 [Byte](core_package_types.md#type-byte)，如果无法转换则返回原来的 [Byte](core_package_types.md#type-byte)。

#### func toAsciiUpperCase()

```cangjie
public func toAsciiUpperCase(): Byte
```

功能：将 [Byte](core_package_types.md#type-byte) 换为对应的 Ascii 大写字符 [Byte](core_package_types.md#type-byte)，如果无法转换则保持现状。

返回值：

- [Byte](core_package_types.md#type-byte) - 转换后的 [Byte](core_package_types.md#type-byte)，如果无法转换则返回原来的 [Byte](core_package_types.md#type-byte)。