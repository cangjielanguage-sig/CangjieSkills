### extend\<T> ArrayStack\<T> <: ToString where T <: ToString

```cangjie
extend<T> ArrayStack<T> <: ToString where T <: ToString
```

功能：为 ArrayStack 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：获取当前 [ArrayStack](./collection_package_class.md#class-arraystackt)\<T> 实例的字符串表示。

该字符串包含栈内每个元素的字符串表示，其顺序为从后到前的顺序。形如："[elem1, elem2, elem3]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前栈的字符串表示。