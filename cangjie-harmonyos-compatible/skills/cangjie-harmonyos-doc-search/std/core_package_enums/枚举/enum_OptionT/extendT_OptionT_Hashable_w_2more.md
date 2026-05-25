### extend\<T> Option\<T> <: Hashable where T <: Hashable

```cangjie
extend<T> Option<T> <: Hashable where T <: Hashable
```

功能：为 [Option](core_package_enums.md#enum-optiont) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口。

[Some](#somet)\<T> 的哈希值等于 `T` 的值对应的哈希值，[None](#none) 的哈希值等于 [Int64](core_package_intrinsics.md#int64)(0)。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend\<T> Option\<T> <: ToString where T <: ToString

```cangjie
extend<T> Option<T> <: ToString where T <: ToString
```

功能：为 [Option](core_package_enums.md#enum-optiont)\<T> 枚举实现 [ToString](core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Option](core_package_enums.md#enum-optiont) 转换为可输出的字符串，字符串内容为 "Some(${T.toString()})" 或 "None"。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。