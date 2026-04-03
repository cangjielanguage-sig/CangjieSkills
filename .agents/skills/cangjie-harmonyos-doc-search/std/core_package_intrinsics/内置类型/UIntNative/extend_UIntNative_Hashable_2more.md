### extend UIntNative <: Hashable

```cangjie
extend UIntNative <: Hashable
```

功能：为 [UIntNative](core_package_intrinsics.md#uintnative) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend UIntNative <: ToString

```cangjie
extend UIntNative <: ToString
```

功能：这里为 [UIntNative](core_package_intrinsics.md#uintnative) 类型扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [UIntNative](core_package_intrinsics.md#uintnative) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。