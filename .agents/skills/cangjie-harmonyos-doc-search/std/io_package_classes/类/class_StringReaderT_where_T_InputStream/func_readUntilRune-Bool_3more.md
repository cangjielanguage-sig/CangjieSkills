### func readUntil((Rune)->Bool)

```cangjie
public func readUntil(predicate: (Rune)->Bool): Option<String>
```

功能：从流内读取到使 `predicate` 返回 true 的字符位置（包含这个字符）或者流结束位置的数据。

参数：

- predicate: ([Rune](../../core/core_package_api/core_package_intrinsics.md#rune))->Bool - 满足一定条件返回 `true` 的表达式。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 读取成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.Some(str)，str 为该次读出的字符串；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.None。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当读取到非法字符时，抛出异常。

### func readUntil(Rune)

```cangjie
public func readUntil(v: Rune): Option<String>
```

功能：从流内读取到指定字符（包含指定字符）或者流结束位置的数据。

参数：

- v: [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 指定字符。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 读取成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.Some(str)，str 为该次读出的字符串；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>.None。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当读取到非法字符时，抛出异常。

### func runes()

```cangjie
public func runes(): Iterator<Rune>
```

功能：获得 [StringReader](io_package_classes.md#class-stringreadert-where-t--inputstream) 的 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 迭代器。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)> - 字符串的 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 迭代器。

异常：

- [ContentFormatException](io_package_exceptions.md#class-contentformatexception) - 当`for-in`或者调用`next()`方法时读取到非法字符，抛出异常。