## class StringReader\<T> where T <: InputStream

```cangjie
public class StringReader<T> where T <: InputStream {
    public init(input: T)
}
```

功能：提供从 [InputStream](io_package_interfaces.md#interface-inputstream) 输入流中读出数据并转换成字符或字符串的能力。

> **说明：**
>
> - [StringReader](io_package_classes.md#class-stringreadert-where-t--inputstream) 内部默认有缓冲区，缓冲区容量 4096 个字节。
> - [StringReader](io_package_classes.md#class-stringreadert-where-t--inputstream) 目前仅支持 UTF-8 编码，暂不支持 UTF-16、UTF-32。

### init(T)

```cangjie
public init(input: T)
```

功能：创建 [StringReader](io_package_classes.md#class-stringreadert-where-t--inputstream) 实例。

参数：

- input: T - 待读取数据的输入流。

### func lines()

```cangjie
public func lines(): Iterator<String>
```

功能：获得 [StringReader](io_package_classes.md#class-stringreadert-where-t--inputstream) 的行迭代器。

相当于循环调用 `func readln()`，内部遇到非法字符时也会抛出异常。

> **说明：**
>
> - 每行都由换行符进行分隔。
> - 换行符是 `\n` `\r` `\r\n` 之一。
> - 每行不包括换行符。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 字符串的行迭代器。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当`for-in`或者调用`next()`方法时读取到非法字符，抛出异常。

### func read()

```cangjie
public func read(): ?Rune
```

功能：按字符读取流中的数据。

返回值：

- ?[Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 读取成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>.Some(c)，c 为该次读出的字符；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>.None。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当读取到非法字符时，抛出异常。

### func readln()

```cangjie
public func readln(): Option<String>
```

功能：按行读取流中的数据。

> **说明：**
>
> - 读取的数据会去掉原换行符。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 读取成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.Some(str)，str 为该次读出的字符串；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.None。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当读取到非法字符时，抛出异常。

### func readToEnd()

```cangjie
public func readToEnd(): String
```

功能：读取流中所有剩余数据。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 流中所有剩余数据。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当读取到非法字符时，抛出异常。