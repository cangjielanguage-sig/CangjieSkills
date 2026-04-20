## class ConsoleReader <sup>(deprecated)</sup>

```cangjie
public class ConsoleReader <: InputStream {}
```

功能：提供从控制台读出数据并转换成字符或字符串的功能。

该类型无法构造实例，只能通过 [Console.stdIn](console_package_class.md#static-prop-stdin) 获取实例。
读操作是同步的，内部设有缓存区来保存控制台输入的内容，当到达控制台输入流的结尾时，控制台读取函数将返回`None`。

[ConsoleReader](console_package_class.md#class-consolereader-deprecated) 只有一个实例，所有方法共享同一个缓存区，相关`read`方法返回`None`的情形有：

- 将标准输入重定向到文件时，读取到文件结尾 EOF。
- Linux 环境，按下 `Ctrl+D`。
- Windows 环境，按下 `Ctrl+Z` 后加回车。

> **注意：**
>
> 未来版本即将废弃，使用 [ConsoleReader](../../env/env_package_api/env_package_classes.md#class-consolereader) 替代。

父类型：

- [InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### func read()

```cangjie
public func read(): ?Rune
```

功能：从标准输入中读取下一个字符。

返回值：

- ?[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)  - 读取到字符，返回 ?[Rune](../../core/core_package_api/core_package_intrinsics.md#rune) ，否则返回 `None`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception)：当输入不符合`UTF-8`编码的字符串时，抛此异常。

### func read(Array\<Byte>)

```cangjie
public func read(arr: Array<Byte>): Int64
```

功能：从标准输入中读取并放入 `arr` 中。

> **注意：**
>
> 该函数存在风险，可能读取出来的结果恰好把 `UTF-8 code point` 从中截断，如果发生截断，将导致该 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> 转换成字符串的结果不正确或抛出异常。

参数：

- arr: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 目标 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回读取到的字节长度。

### func readln()

```cangjie
public func readln(): ?String
```

功能：从标准输入中读取一行字符串。

读取到字符，返回 ?[String](../../core/core_package_api/core_package_structs.md#struct-string)，结果不包含末尾换行符。该接口不会抛出异常，即使输入不符合`UTF-8`编码的字符串，也会构造出一个 [String](../../core/core_package_api/core_package_structs.md#struct-string) 并返回，其行为等同于 [String](../../core/core_package_api/core_package_structs.md#struct-string).fromUtf8Uncheck([Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)>)。

返回值：

- ?[String](../../core/core_package_api/core_package_structs.md#struct-string) - 读取到的行数据，读取失败返回 `None`。