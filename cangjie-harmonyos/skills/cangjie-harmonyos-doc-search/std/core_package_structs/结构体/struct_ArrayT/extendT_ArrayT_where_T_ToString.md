### extend\<T> Array\<T> where T <: ToString

```cangjie
extend<T> Array<T> <: ToString where T <: ToString
```

功能：为 [Array](core_package_structs.md#struct-arrayt)\<T> 类型扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将数组转换为可输出的字符串。

字符串形如 "[1, 2, 3, 4, 5]"

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。