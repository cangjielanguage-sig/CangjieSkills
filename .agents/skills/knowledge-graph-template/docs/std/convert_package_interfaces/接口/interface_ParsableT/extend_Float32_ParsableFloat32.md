### extend Float32 <: Parsable\<Float32>

```cangjie
extend Float32 <: Parsable<Float32>
```

功能：此扩展主要用于实现将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型字面量的字符串转换为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值的相关操作函数。

> **注意：**
>
> 目前不支持二进制和八进制的浮点数转换。

父类型：

- [Parsable](#interface-parsablet)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

#### static func parse(String)

```cangjie
public static func parse(data: String): Float32
```

功能：将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型字面量的字符串转换为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 返回转换后 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串不符合浮点数语法时，抛出异常。

#### static func tryParse(String)

```cangjie
public static func tryParse(data: String): Option<Float32>
```

功能：将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)> 值。

参数：

- data: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>.None。