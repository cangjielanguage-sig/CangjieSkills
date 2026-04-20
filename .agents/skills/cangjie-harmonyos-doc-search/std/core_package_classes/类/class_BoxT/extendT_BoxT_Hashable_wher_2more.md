### extend\<T> Box\<T> <: Hashable where T <: Hashable

```cangjie
extend<T> Box<T> <: Hashable where T <: Hashable
```

功能：为 [Box](core_package_classes.md#class-boxt)\<T> 类扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，提供比较大小的能力。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 [Box](core_package_classes.md#class-boxt) 对象的哈希值。

实际上该值为 [Box](core_package_classes.md#class-boxt) 中封装的 `T` 类型实例的哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [Box](core_package_classes.md#class-boxt) 对象的哈希值。

### extend\<T> Box\<T> <: ToString where T <: ToString

```cangjie
extend<T> Box<T> <: ToString where T <: ToString
```

功能：为 [Box](core_package_classes.md#class-boxt)\<T> 类型扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：获取 [Box](core_package_classes.md#class-boxt) 对象的字符串表示，字符串内容为当前实例封装的 `T` 类型实例的字符串表示。

返回值：

- [String](core_package_structs.md#struct-string) - 转换后的字符串。