#### func toTitle(CasingOption)

```cangjie
public func toTitle(opt: CasingOption): String
```

功能：将当前字符串中 `Unicode` 字符集范围内可以转换为标题大写字符的转换为标题大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的标题大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toTitle(CasingOption.Other))
}
```

运行结果：

```text
ABCDEF
```

#### func toUpper()

```cangjie
public func toUpper(): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的小写字符转化为大写字符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toUpper())
}
```

运行结果：

```text
ABCDEF
```

#### func toUpper(CasingOption)

```cangjie
public func toUpper(opt: CasingOption): String
```

功能：将当前字符串中所有 `Unicode` 字符集范围内的小写字符转化为大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的全大写字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中存在无效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println("AbcDEF".toUpper(CasingOption.Other))
}
```

运行结果：

```text
ABCDEF
```

#### func trim()

```cangjie
public func trim(): String
```

功能：去除字符串开头结尾的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除首尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    let str = "  x  "
    println("\"${str.trim()}\"")
}
```

运行结果：

```text
"x"
```

#### func trimEnd()

```cangjie
public func trimEnd(): String
```

功能：去除字符串结尾的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除结尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    let str = "  x  "
    println("\"${str.trimEnd()}\"")
}
```

运行结果：

```text
"  x"
```