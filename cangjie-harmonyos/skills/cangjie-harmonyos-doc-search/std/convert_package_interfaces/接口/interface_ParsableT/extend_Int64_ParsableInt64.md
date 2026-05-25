### extend Int64 <: Parsable\<Int64>

```cangjie
extend Int64 <: Parsable<Int64>
```

功能：此扩展主要用于实现将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型字面量的字符串转换为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值的相关操作函数。

父类型：

- [Parsable](#interface-parsablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

#### static func parse(String)

```cangjie
public static func parse(data: String): Int64
```

功能：将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型字面量的字符串转换为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回转换后 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串为空，首位为 `+` ，转换失败，或转换后超出 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 范围，或字符串中含有无效的 UTF-8 字符时，抛出异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(data: String): Option<Int64>
```

功能：将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>.None。