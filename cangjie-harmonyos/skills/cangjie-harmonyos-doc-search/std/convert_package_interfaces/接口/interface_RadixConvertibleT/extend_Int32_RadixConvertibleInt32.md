### extend Int32 <: RadixConvertible\<Int32>

```cangjie
extend Int32 <: RadixConvertible<Int32>
```

功能：此扩展主要用于实现将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值的相关操作函数。

父类型：

- [RadixConvertible](#interface-radixconvertiblet)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### static func parse(String, Int64)

```cangjie
public static func parse(value: String, radix!: Int64): Int32
```

功能：将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回转换后 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当字符串为空、进制超出范围、转换后超出 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 范围、字符串中含有无效的 UTF-8 字符、转换失败时，抛出异常。

#### static func tryParse(String, Int64)

```cangjie
public static func tryParse(value: String, radix!: Int64): Option<Int32>
```

功能：将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型字面量的字符串转换为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> 值。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要转换的字符串。
- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> - 返回转换后 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)> 值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>.None。

#### func toString(Int64)

```cangjie
public func toString(radix!: Int64): String
```

功能：返回指定进制形式字符串。

参数：

- radix!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定的进制。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定进制形式字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当进制不合规时，抛出异常。