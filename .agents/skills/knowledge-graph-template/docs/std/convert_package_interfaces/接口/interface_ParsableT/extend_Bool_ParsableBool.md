### extend Bool <: Parsable\<Bool>

```cangjie
extend Bool <: Parsable<Bool>
```

功能：此扩展主要用于实现将 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型字面量的字符串转换为 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 值的相关操作函数。

父类型：

- [Parsable](#interface-parsablet)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)>

#### static func parse(String)

```cangjie
public static func parse(data: String): Bool
```

功能：将 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型字面量的字符串转换为 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回转换后 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串为空或转换失败时，抛出异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(data: String): Option<Bool>
```

功能：将 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)> 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)>.None。