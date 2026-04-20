### extend UInt32 <: ToString

```cangjie
extend UInt32 <: ToString
```

功能：这里为 [UInt32](core_package_intrinsics.md#uint32) 类型扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [UInt32](core_package_intrinsics.md#uint32) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。