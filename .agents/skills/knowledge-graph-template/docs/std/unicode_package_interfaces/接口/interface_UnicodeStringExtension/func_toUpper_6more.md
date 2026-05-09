### func toUpper()

```cangjie
func toUpper(): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的小写字符转化为大写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

### func toUpper(CasingOption)

```cangjie
func toUpper(opt: CasingOption): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的小写字符转化为大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

### func trim()

```cangjie
func trim(): String
```

功能：去除字符串开头结尾的空字符串，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除首尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

### func trimEnd()

```cangjie
func trimEnd(): String
```

功能：去除字符串结尾的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除结尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

### func trimLeft() <sup>(deprecated)</sup>

```cangjie
func trimLeft(): String
```

功能：去除字符串开头的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

> **注意：**
>
> 未来版本即将废弃，使用 [trimStart](./unicode_package_interfaces.md#func-trimstart) 替代。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除开头空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

### func trimRight() <sup>(deprecated)</sup>

```cangjie
func trimRight(): String
```

功能：去除字符串结尾的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

> **注意：**
>
> 未来版本即将废弃，使用 [trimEnd](./unicode_package_interfaces.md#func-trimend) 替代。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除结尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。