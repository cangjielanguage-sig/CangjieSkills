#### func toLowerCase()

```cangjie
public func toLowerCase(): Rune
```

功能：获取该字符对应的 `Unicode` 小写字符。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的小写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'A'.toLowerCase())
}
```

运行结果：

```text
a
```

#### func toLowerCase(CasingOption)

```cangjie
public func toLowerCase(opt: CasingOption): Rune
```

功能：获取该字符对应的 `Unicode` 小写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的小写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'A'.toLowerCase(CasingOption.Other))
}
```

运行结果：

```text
a
```

#### func toTitleCase()

```cangjie
public func toTitleCase(): Rune
```

功能：获取该字符对应的 `Unicode` 标题大写字符。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的标题大写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.toTitleCase())
}
```

运行结果：

```text
A
```

#### func toTitleCase(CasingOption)

```cangjie
public func toTitleCase(opt: CasingOption): Rune
```

功能：获取该字符对应的 `Unicode` 标题大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的标题大写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.toTitleCase(CasingOption.Other))
}
```

运行结果：

```text
A
```

#### func toUpperCase()

```cangjie
public func toUpperCase(): Rune
```

功能：获取该字符对应的 `Unicode` 大写字符。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的小写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.toUpperCase())
}
```

运行结果：

```text
A
```

#### func toUpperCase(CasingOption)

```cangjie
public func toUpperCase(opt: CasingOption): Rune
```

功能：获取该字符对应的 `Unicode` 大写字符。

参数：

- opt: [CasingOption](./unicode_package_enums.md#enum-casingoption) - 传入的语言枚举。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 当前字符对应的小写字符。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    println(r'a'.toUpperCase(CasingOption.Other))
}
```

运行结果：

```text
A
```