## class PrimitiveTypeInfo

```cangjie
public class PrimitiveTypeInfo <: TypeInfo {}
```

功能：描述原始数据类型的类型信息。

原始数据类型包括无类型（`Nothing`）、单元类型（[Unit](../../core/core_package_api/core_package_intrinsics.md#unit)）、字符类型（[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)）、布尔类型（[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)），整形类型（[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)，[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)，[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)，[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)，[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)，[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)，[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)，[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)，[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)，[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)）和浮点类型（[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)，[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)，[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)）。

> **注意：**
>
> 目前尚不支持 `Nothing` 原始数据类型。

父类型：

- [TypeInfo](#class-typeinfo)

### static func get(String)

```cangjie
public static redef func get(qualifiedName: String): PrimitiveTypeInfo
```

功能：获取给定的类型的限定名称所对应类型的 [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo)。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo) - 类型的限定名称 `qualifiedName` 所对应的类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 匹配的类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

main(): Unit {
    var pti = PrimitiveTypeInfo.get("Int64")
    println(pti)
    return
}
```

运行结果：

```text
Int64
```