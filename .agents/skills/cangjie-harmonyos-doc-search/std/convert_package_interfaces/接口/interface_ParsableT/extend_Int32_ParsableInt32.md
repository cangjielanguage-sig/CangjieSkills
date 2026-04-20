### extend Int32 <: Parsable\<Int32>

```cangjie
extend Int32 <: Parsable<Int32>
```

功能：此扩展主要用于实现将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值的相关操作函数。

父类型：

- [Parsable](#interface-parsablet)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### static func parse(String)

```cangjie
public static func parse(data: String): Int32
```

功能：将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回转换后 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串为空，首位为 `+` ，转换失败，或转换后超出 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 范围，或字符串中含有无效的 UTF-8 字符时，抛出异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(data: String): Option<Int32>
```

功能：将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>.None。