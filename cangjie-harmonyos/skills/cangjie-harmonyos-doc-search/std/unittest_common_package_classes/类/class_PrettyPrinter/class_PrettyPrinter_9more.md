## class PrettyPrinter

```cangjie
public abstract class PrettyPrinter {
    public PrettyPrinter(let indentationSize!: UInt64 = 4, let startingIndent!: UInt64 = 0)
}
```

功能：拥有颜色和对齐、缩进控制的打印器。

### PrettyPrinter(UInt64,UInt64)

```cangjie
public PrettyPrinter(let indentationSize!: UInt64 = 4, let startingIndent!: UInt64 = 0)
```

功能：PrettyPrinter 构造器。

参数：

- indentationSize!: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 一个缩进的空格数，默认 4 格。
- startingIndent!: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 开头的缩进个数，默认 0 个缩进。

### prop isTopLevel

```cangjie
public prop isTopLevel: Bool
```

功能：获取是否在打印的缩进顶层。

类型：Bool 。

### func append(String)

```cangjie
public func append(text: String): PrettyPrinter
```

功能：增加一个字符串到打印器中。不支持多行字符串，对多行字符串不支持缩进。

参数：

- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被增加的字符串。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func append\<PP>(PP)where PP <: PrettyPrintable

```cangjie
public func append<PP>(value: PP): PrettyPrinter where PP <: PrettyPrintable
```

功能：增加一个实现了 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 的对象到打印器中。

参数：

- value: PP - 一个实现了 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 的对象。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func appendCentered(String, UInt64)

```cangjie
public func appendCentered(text: String, space: UInt64): PrettyPrinter
```

功能：增加一个字符串到打印器中。居中对齐至指定字符数，不足的字符由空格补齐。不支持多行字符串，对多行字符串不支持缩进。

参数：

- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被增加的字符串。
- space: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 对齐的字符数量。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func appendLeftAligned(String, UInt64)

```cangjie
public func appendLeftAligned(text: String, space: UInt64): PrettyPrinter
```

功能：增加一个字符串到打印器中。左对齐至指定字符数，不足的字符由空格补齐。不支持多行字符串，对多行字符串不支持缩进。

参数：

- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被增加的字符串。
- space: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 对齐的字符数量。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func appendLine(String): PrettyPrinter

```cangjie
public func appendLine(text: String): PrettyPrinter
```

功能：增加一个字符串到打印器中，跟着一个换行符。

参数：

- text: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被增加的字符串。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。

### func appendLine\<PP>(PP) where PP <: PrettyPrintable

```cangjie
public func appendLine<PP>(value: PP): PrettyPrinter where PP <: PrettyPrintable
```

功能：增加一个实现了 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 的对象到打印器中，跟着一个换行符。

参数：

- value: PP - 一个实现了 [PrettyPrintable](./unittest_common_package_interfaces.md#interface-prettyprintable) 的对象。

返回值：

- [PrettyPrinter](#class-prettyprinter) - 打印器。