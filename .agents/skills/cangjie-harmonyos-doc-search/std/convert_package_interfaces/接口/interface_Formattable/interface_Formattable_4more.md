## interface Formattable

```cangjie
public interface Formattable {
    func format(fmt: String): String
}
```

功能：该接口定义了格式化函数，即根据格式化参数将指定类型实例转换为对应格式的字符串。

格式化参数相关的说明请参见 convert 包中的[功能介绍](./../convert_package_overview.md#功能介绍)。

其他类型可通过实现该接口提供格式化功能。

### func format(String)

```cangjie
func format(fmt: String): String
```

功能：根据格式化参数将当前实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前实例格式化后得到的字符串。

### extend Float16 <: Formattable

```cangjie
extend Float16 <: Formattable
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend Float32 <: Formattable

```cangjie
extend Float32 <: Formattable
```

功能：为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。