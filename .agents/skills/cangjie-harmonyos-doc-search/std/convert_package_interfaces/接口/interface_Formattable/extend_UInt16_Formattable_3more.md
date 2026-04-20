### extend UInt16 <: Formattable

```cangjie
extend UInt16 <: Formattable
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend UInt32 <: Formattable

```cangjie
extend UInt32 <: Formattable
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend UInt64 <: Formattable

```cangjie
extend UInt64 <: Formattable
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 扩展 [Formattable](convert_package_interfaces.md#interface-formattable) 接口，以实现将 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 实例转换为格式化字符串。

父类型：

- [Formattable](#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。