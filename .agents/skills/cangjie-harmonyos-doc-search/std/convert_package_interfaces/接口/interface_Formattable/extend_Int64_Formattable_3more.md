### extend Int64 <: Formattable

```cangjie
extend Int64 <: Formattable
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend Int8 <: Formattable

```cangjie
extend Int8 <: Formattable
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend Rune <: Formattable

```cangjie
extend Rune <: Formattable
```

功能：为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。