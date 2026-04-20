### extend Rune <: Parsable\<Rune>

```cangjie
extend Rune <: Parsable<Rune>
```

功能：此扩展主要用于实现将 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型字面量的字符串转换为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 值的相关操作函数。

父类型：

- [Parsable](#interface-parsablet)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>

#### static func parse(String)

```cangjie
public static func parse(data: String): Rune
```

功能：将 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型字面量的字符串转换为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 返回转换后 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串为空，或转换失败时，或字符串中含有无效的 UTF-8 字符时，抛出异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(data: String): Option<Rune>
```

功能：将 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)> 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>.None。