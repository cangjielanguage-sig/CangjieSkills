## Unit

功能：表示仓颉语言中只关心副作用而不关心值的表达式的类型。

例如，print 函数、赋值表达式、复合赋值表达式、自增和自减表达式、循环表达式，它们的类型都是 [Unit](core_package_intrinsics.md#unit)。

[Unit](core_package_intrinsics.md#unit) 类型只有一个值，也是它的字面量：()。除了赋值、判等和判不等外，[Unit](core_package_intrinsics.md#unit) 类型不支持其他操作。

### extend Unit <: Equatable\<Unit>

```cangjie
extend Unit <: Equatable<Unit>
```

功能：为 [Unit](core_package_intrinsics.md#unit) 类型扩展 [Equatable](core_package_interfaces.md#interface-equatablet)\<[Unit](core_package_intrinsics.md#unit)> 接口。

父类型：

- [Equatable](core_package_interfaces.md#interface-equatablet)\<[Unit](#unit)>

### extend Unit <: Hashable

```cangjie
extend Unit <: Hashable
```

功能：为 [Unit](core_package_intrinsics.md#unit) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值，[Unit](core_package_intrinsics.md#unit) 的哈希值为 0。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend Unit <: ToString

```cangjie
extend Unit <: ToString
```

功能：为 [Unit](core_package_intrinsics.md#unit) 类型其扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。

[Unit](core_package_intrinsics.md#unit) 的字符串表示是 "()"。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Unit](core_package_intrinsics.md#unit) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。