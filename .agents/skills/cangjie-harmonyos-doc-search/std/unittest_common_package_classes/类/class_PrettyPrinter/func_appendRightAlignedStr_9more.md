### func appendRightAligned(String, UInt64)

```cangjie
public func appendRightAligned(text: String, space: UInt64): PrettyPrinter
```

功能：增加一个字符串到打印器中。右对齐至指定字符数。不支持多行字符串，对多行字符串不支持缩进。

参数：

- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被增加的字符串。
- space: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 对齐的字符数量。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func colored(Color, () -> Unit)

```cangjie
public func colored(color: Color, body: () -> Unit): PrettyPrinter
```

功能：对闭包中给打印器增加的字符串指定颜色。
常见的用法如下：

```cangjie
pp.colored(RED) {
    pp.appendLine("1")
    pp.appendLine("2")
    pp.appendLine("3")
}
```

此时字符串 "1" "2" "3" 均被打印为红色。

参数：

- color: [Color](./unittest_common_package_enums.md#enum-color) - 指定打印的颜色。
- body: () -> Unit - 添加字符串的闭包。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func fillLimitedSpace(Int64, () -\> Unit)

```cangjie
public open func fillLimitedSpace(spaceSize: Int64, body: () -> Unit): c
```

功能：指定大小填充代码块。

参数：

- spaceSize: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)  - 所指定的大小。
- body: () -\> body - 填充的方式。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func colored(Color, String)

```cangjie
public func colored(color: Color, text: String): PrettyPrinter
```

功能：对给打印器增加的字符串指定颜色。

参数：

- color: [Color](./unittest_common_package_enums.md#enum-color) - 指定打印的颜色。
- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 添加的字符串。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func customOffset(UInt64, () -> Unit)

```cangjie
public func customOffset(symbols: UInt64, body: () -> Unit): PrettyPrinter
```

功能：对闭包中给打印器增加的字符串指定额外缩进的个数。
常见的用法如下：

```cangjie
pp.customOffset(5) {
    pp.appendLine("1")
    pp.appendLine("2")
    pp.appendLine("3")
}
```

此时字符串 "1" "2" "3" 均额外缩进 5 个字符。

参数：

- symbols: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指定缩进个数。
- body: () -> Unit - 添加字符串的闭包。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func indent(() -> Unit)

```cangjie
public func indent(body: () -> Unit): PrettyPrinter
```

功能：对闭包中给打印器增加的字符串指定额外缩进一次。
常见的用法如下：

```cangjie
pp.indent {
    pp.appendLine("1")
    pp.appendLine("2")
    pp.appendLine("3")
}
```

此时字符串 "1" "2" "3" 均额外缩进一次。

参数：

- body: () -> Unit - 添加字符串的闭包。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func indent(UInt64, () -> Unit)

```cangjie
public func indent(indents: UInt64, body: () -> Unit): PrettyPrinter
```

功能：对闭包中给打印器增加的字符串指定额外缩进指定次数。
常见的用法如下：

```cangjie
pp.indent(2) {
    pp.appendLine("1")
    pp.appendLine("2")
    pp.appendLine("3")
}
```

此时字符串 "1" "2" "3" 均额外缩进 2 次。

参数：

- indents: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指定额外缩进的次数。
- body: () -> Unit - 添加字符串的闭包。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func newLine()

```cangjie
public func newLine(): PrettyPrinter
```

功能：增加新行。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func put(String)

```cangjie
protected func put(s: String): Unit
```

功能：打印字符串。

参数：

- s: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 需打印的字符串。